<h2 id="introduction">Introduction</h2>
<p>Organizations today are increasingly adopting a <a href="https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/">Zero Trust security</a> posture to safeguard company assets and infrastructure in a constantly evolving threat landscape. The traditional security associated with legacy network design assumes trust within the corporate network perimeter. In contrast, Zero Trust operates on the principle of &quot;Never trust, always verify&quot; and implements continuous <a href="https://www.cloudflare.com/learning/access-management/what-is-access-control/">authentication and strict access controls</a> for all users, devices, and applications, regardless of their location or network.</p>
<p>Typically two technologies play a role in a Zero Trust architecture. First, a <a href="https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/">Secure Web Gateway (SWG)</a> filters outbound traffic destined for the Internet and blocks users from accessing high risk websites such as those involved in phishing campaigns. Then, to enable remote access for users to SaaS apps, internally-hosted applications and networks, Zero Trust Network Access (<a href="https://www.cloudflare.com/learning/access-management/what-is-ztna/">ZTNA</a>) services are used to create secure tunnels and provide access for remote users into private applications.</p>
<p>This guide is for customers looking to deploy Cloudflare's ZTNA service (<a href="/cloudflare-one/access-controls/policies/">Access</a>) and provides best practices and guidelines for how to effectively build the right policies. If you have not already done so, we recommend also reading Cloudflare's <a href="/reference-architecture/architectures/sase/">SASE reference architecture</a>, which goes into detail on all aspects of how to use Cloudflare as part of your Zero Trust initiatives.</p>
<h3 id="who-is-this-document-for-and-what-will-you-learn">Who is this document for and what will you learn?</h3>
<p>This document is aimed at administrators who are evaluating or have adopted Cloudflare to replace existing VPN services or provide new remote access to internal resources. This serves as a starting point for designing your first ZTNA policies and as an ongoing reference. This guide covers three main sections:</p>
<ul>
<li><strong>Technical prerequisites</strong>: What needs to be in place before you can secure access to your first application and define access policies.</li>
<li><strong>Building policies</strong>: The main components of an access policy and how they are combined.</li>
<li><strong>Use cases</strong>: Common use cases and policies that can serve as blueprints for your own policy designs.</li>
</ul>
<p>This design guide assumes you have a basic understanding of Cloudflare's ZTNA solution, <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>. Therefore, this guide focuses on designing effective access policies and assumes you have already configured <a href="/cloudflare-one/traffic-policies/get-started/dns/">DNS</a>, <a href="/cloudflare-one/integrations/identity-providers/">identity</a> and <a href="/cloudflare-one/integrations/service-providers/">device posture providers</a> as well as <a href="/cloudflare-one/networks/">created connectivity</a> to self-hosted applications and related networks.</p>
<p>By the end of this guide, you will be equipped to implement granular access policies that enforce Zero Trust principles across various common enterprise scenarios.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>This section covers the essential architectural components and concepts to understand before you can design granular access policies.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/12709.md")
</aside>
<p>Cloudflare allows organizations to facilitate application access using our <a href="https://www.cloudflare.com/connectivity-cloud/">connectivity cloud</a>, which securely connects users, applications and data regardless of their location. Core to the platform is Cloudflare's <a href="https://www.cloudflare.com/network/">extensive global network</a> which delivers low-latency connectivity for users worldwide. By running every service in every data center, Cloudflare applies networking, performance and security functions in a single pass, eliminating the need to route traffic through multiple, specialized security servers, and therefore reduces latency and avoids performance bottlenecks.</p>
<p><img src="/assets/upstream/images/reference-architecture/designing-ztna-access-policies-for-cloudflare-access/figure1.svg" alt="Figure 1 shows the basic components involved in remote access with Cloudflare's ZTNA service." title="Figure 1 shows the basic components involved in remote access with Cloudflare's ZTNA service." /></p>
<p>There are two main ways to provide access to private applications and networks: by public hostname, where requests are proxied to the application, or by private IP, where the user is on a device or network that is connecting them to their private corporate network via Cloudflare.</p>
<h3 id="active-domain-in-cloudflare">Active domain in Cloudflare</h3>
<p>To use public hostnames, you need to have an <a href="/fundamentals/manage-domains/add-site/">active domain</a> in Cloudflare. Most customers use Cloudflare as their primary DNS service, but it is possible to configure domains for use with Access and maintain <a href="/dns/zone-setups/partial-setup/">DNS records elsewhere</a>.</p>
<h3 id="network-route-to-applications">Network route to applications</h3>
<p>For Cloudflare to control access, it needs to be in front of the application and have a secure and reliable network route for successfully authenticated users. Requests for application access come to Cloudflare first, where policy is applied, and then if successful, user requests are routed to the application.</p>
<p>Cloudflare supports access to the following types of applications:</p>
<ul>
<li>SaaS applications on the Internet</li>
<li>Self-hosted applications accessed via public hostname</li>
<li>Self-hosted applications accessed via private IP</li>
</ul>
<p>For SaaS and other Internet-facing applications, access from Cloudflare is simple — it is already on the Internet. But for self-hosted applications, you create a tunnel from Cloudflare to the private network where the application is running. There are two methods for doing this:</p>
<ul>
<li>Our recommended approach is to use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">software agents</a> such as <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">cloudflared</a> or <a href="/mesh/">Cloudflare Mesh</a>. (Note, only cloudflared currently supports proxying of public hostnames to private applications.)</li>
<li>For network-based connectivity, <a href="/cloudflare-wan/">Cloudflare WAN</a> (formerly Magic WAN) uses IPsec or GRE tunnels connecting Cloudflare to existing network appliances that are connected to the private networks, and <a href="/network-interconnect/">Network Interconnect</a> creates direct connectivity if your applications run on servers in a data center Cloudflare operates in. (For migrating from existing legacy VPN solutions to network-based tunnels, you may find <a href="/reference-architecture/design-guides/network-vpn-migration/">this guide</a> useful.)</li>
</ul>
<p>Once we have established connectivity to your applications, it is time to facilitate user access. Depending on your policy requirements (more on this later) users can access the application directly over an Internet connection to a public hostname, or — for greater security — we recommend using our <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">device agent</a>, the Cloudflare One Client, which creates a tunnel directly to Cloudflare and also provides information about their device for use in access policies.</p>
<h3 id="identity">Identity</h3>
<p>A critical part of application access is authenticating a user. Cloudflare has a <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">built-in authentication</a> method based on email. But we highly recommend configuring a third-party identity provider. We support both consumer and enterprise <a href="/cloudflare-one/integrations/identity-providers/">identity providers</a>, and any SAML or OpenID compliant service can be used. Group membership is one of the most common attributes of defining application access and can be defined manually or imported using the System for Cross-Domain Identity Management (<a href="/cloudflare-one/team-and-resources/users/scim/">SCIM</a>).</p>
<h3 id="device-posture">Device posture</h3>
<p>The final prerequisite for building really effective access policies is to configure <a href="/cloudflare-one/reusable-components/posture-checks/">device posture</a>. When using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">device agent</a>, Cloudflare has access to a <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">variety of information</a> about the device which can then be used in an access policy. When using an <a href="/reference-architecture/diagrams/sase/sase-clientless-access-private-dns/">agentless method</a> to access applications, only the user identity information is available. We also support using device posture information from <a href="/cloudflare-one/integrations/service-providers/">other vendors</a>, such as Microsoft, Crowdstrike and Sentinel One.</p>
<p><img src="/assets/upstream/images/reference-architecture/designing-ztna-access-policies-for-cloudflare-access/figure2.svg" alt="Figure 2 - two employees with different devices trying to access the same corporate application. Only the user with the device agent can access the SSH service." title="Figure 2 - two employees with different devices trying to access the same corporate application. Only the user with the device agent can access the SSH service." /></p>
<h2 id="building-policies">Building policies</h2>
<p>To quickly summarize the architecture described so far, Cloudflare is:</p>
<ul>
<li>In front of network access to the application.</li>
<li>Integrated with your identity providers.</li>
<li>Aware of device posture details for your users using our device agent or a third party vendor.</li>
</ul>
<p>When a user makes a request to access an application, they must first authenticate, then, before access is granted, policies in the application are evaluated based on the data associated with the requesting user. Policies and other application specific settings are defined in an Access application.</p>
<h3 id="access-application-types">Access application types</h3>
<p>Cloudflare Access supports four main types of applications:</p>
<ul>
<li><strong>Self-hosted</strong> refers to applications that your organization hosts and manages, either on premises or in the cloud. Cloudflare creates a public hostname which it uses to proxy traffic through a secure tunnel to the application. While access via public hostnames is supported if your server is just publicly facing on the Internet, we recommend you use <code>cloudflared</code> to create a secure, outbound-only connection from your application to Cloudflare's edge. Once that occurs, Cloudflare will then reverse proxy the target application/content to your users.</li>
<li><strong>Private IP</strong> applications are similarly privately hosted, but lack fully-qualified public hostnames. Access can be facilitated via <code>cloudflared</code>, Cloudflare Mesh, Cloudflare WAN, or Cloudflare Network Interconnect. Remote users not connected to a network already connected to Cloudflare will need to use the device client to get access to the application via private IP and to avoid using IP addresses with users, use <a href="/cloudflare-one/traffic-policies/resolver-policies/#use-cases">internal DNS services</a> to resolve private hostnames to private IP addresses. But it is possible to provide access without any software deployed to the client by using our agentless <a href="/reference-architecture/diagrams/sase/sase-clientless-access-private-dns/">browser isolation service</a>.</li>
<li><strong>SaaS</strong> applications are accessed over the public Internet, and therefore do not require any tunnel connectivity to Cloudflare. Instead, Access acts as an identity proxy between users and the SaaS application. When a user attempts to access the SaaS app, they are first authenticated by Cloudflare, which redirects to your main identity service. SaaS applications are then configured via SAML or OAuth to trust Cloudflare. This allows organizations to implement additional security layers (like device posture checks) and centralize access control for their SaaS applications, even if the SaaS or identity provider does not natively support these features.</li>
<li><strong>Infrastructure</strong> applications enable users to control access to individual servers, clusters or databases in a private network. Infrastructure apps work by defining a 'target' proxied over <code>cloudflared</code>, but allows users to group multiple machines under the same target - essentially, allowing users to define common access policies across potentially disparate infrastructure resources. Built-in access and command logging capabilities means organizations can maintain detailed audit trails for compliance and security investigation purposes.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12708.md")
</aside>
<p>Access applications typically map directly to a single application. However, it is possible to have an Access application, and its associated policies sit in front of more than one application endpoint. This might be a range of IPs related to multiple Windows RDP servers where you wish to implement a common access policy. The same idea can also be applied to public hostnames, where you might have more than one hostname that refers to several applications you wish to have the same policies. For instance, you might have wiki.domain.com and wiki.domain.co.uk — different application instances, but with common access policy requirements.</p>
<p>Next, we examine the main elements of a ZTNA-protected application that need to be understood to create effective access policies, then later in the document we will examine some use cases that apply those specific elements.</p>
<h3 id="authentication">Authentication</h3>
<p>Authenticating a user's identity is a key component of any Zero Trust policy. When attempting to log into an application, a user will be redirected to a configured identity provider. If a user fails to authenticate with the identity provider, Cloudflare will not accept their request for the application.</p>
<p>As mentioned above, Cloudflare can be integrated with all your identity providers (IdPs), both enterprise and consumer. Then at the application and policy level, you choose which IdPs you want to allow for authentication. For example, you may have an application that only a limited number of employees can access. Therefore, you would only enable your corporate IdP. For another application, you may wish to allow access to a wider group of non-employee users, such as contractors or third-party partners. Some of those users you might authenticate via their GitHub or LinkedIn credentials.</p>
<p>When a user attempts to access an application they will be presented with a sign-in page where they choose which IdP to authenticate with. For applications with only a single IdP, you can automatically redirect the user to that IdP. It is also possible to configure the application to display every possible IdP that has been configured, allowing you to add new providers in the future without the need to update the policy.</p>
<p><img src="/assets/upstream/images/reference-architecture/designing-ztna-access-policies-for-cloudflare-access/figure3.svg" alt="Figure 3 - How employees from different parts of the organization authenticate to the same application." title="Figure 3 - How employees from different parts of the organization authenticate to the same application." /></p>
<p>After authentication, the IdP is going to send information about the identity back to Cloudflare. Depending on the IdP, this information may include <a href="https://datatracker.ietf.org/doc/html/rfc8176">Authentication Method Reference</a> (amr) values, IdP groups, SAML attributes or OIDC claims which can then be used in policies.</p>
<p>When using our device agent, users must also authenticate and can be presented a custom list of IdPs. Once the agent is authenticated, they are able to connect to Cloudflare and it is possible to configure applications to skip authentication, instead trusting the existing authentication session associated with the device agent.</p>
<h3 id="policies">Policies</h3>
<p>Now we arrive at the main focus of this guide: the policies which define access to applications. This is where the real work is done to define who has access, and how. Before looking at example use cases, here is a breakdown of how policies work.</p>
<p><img src="/assets/upstream/images/reference-architecture/designing-ztna-access-policies-for-cloudflare-access/figure4.svg" alt="Figure 4 - Our ZNTA service Access can use a wide variety of attributes in an access policy." title="Figure 4 - Our ZNTA service Access can use a wide variety of attributes in an access policy." /></p>
<p>Each application can contain multiple policies, and are evaluated in order. Because multiple policies — each with multiple sets of rules — can get quite complex, there is a policy tester where you provide a username and see how the user is evaluated against all the policies and rules. Policies consist of the following elements:</p>
<h4 id="name">Name</h4>
<p>While it seems obvious what this is for, we highly recommend having a strategy for naming your policies. This is because you will likely create similar policies across multiple applications, such as &quot;Allow all full-time employees&quot; or &quot;Block high-risk users&quot;. Using the same naming scheme across all applications will vastly streamline your ability to review application access and to understand the full list of policies in the future.</p>
<h4 id="action">Action</h4>
<p>The Action field in a policy determines what happens when a user or service matches the policy's criteria. There are four main types of actions:</p>
<ul>
<li><strong>Allow</strong> grants access to the application. A login page will be presented to a user on initial access request.</li>
<li><strong>Block</strong> denies access to the application. This is generally not required because Access is denied by default. The only reason users should implement a block policy is for testing a specific policy condition or short-circuiting policy evaluation. If a block policy has higher precedent than an Allow, and a user matches the block policy, all other policy evaluation ceases.</li>
<li><strong>Bypass</strong> allows users or services to disable any enforcement for traffic before accessing the application. For example, a specific endpoint in an application may need to be broadly accessible over the Internet.</li>
<li><strong>Service Auth</strong> allows you to authenticate requests from other services or applications using <a href="/ssl/client-certificates/enable-mtls/">mTLS</a> or <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service tokens</a>. No login page will be presented to the user or service if they meet this policy criteria. This is designed so that non-user requests, such as those from other applications, can access secured resources.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12707.md")
</aside>
<h4 id="session-duration">Session duration</h4>
<p>Session duration refers to the length of time a user's authentication remains valid after they have successfully logged in to an application. Typically, the session duration is set for 24 hours, but you can also set durations for sensitive applications to expire immediately. This approach aligns with the core Zero Trust principle of &quot;never trust, always verify.&quot; Even if a user initially presents the appropriate device posture and identity context, continuous verification ensures that access rights are reassessed with each new request. This method significantly reduces the risk window, as it removes the assumption that the initial authentication and authorization state remains valid over an extended period.</p>
<h4 id="rules">Rules</h4>
<p>These are the main focus of a policy. Rules define all the attributes that dictate if the policy allows or denies access, or renders the application in an isolated browser. They are composed of a selector and value, which is essentially the attribute you wish to evaluate and the data you are evaluating.</p>
<p>Each rule is a filter to determine which users this policy is going to affect. There are several categories of rules:</p>
<ul>
<li>
<p><strong>Include</strong> rules define who or what is eligible for access. When a user matches an &quot;Include&quot; rule, they become a candidate for access, subject to other rules types in the policy. These rules use OR logic — satisfying any one is sufficient. For example, you may make an application available to a specific group, but need to add in contractors for an email list, and as long as the user matches one of these (group membership, or a valid email) they are included in the rule. Every policy must have at least one Include clause.</p>
</li>
<li>
<p><strong>Require</strong> rules set mandatory conditions that must be met for access to be granted. Unlike Include rules, &quot;Require&quot; rules use AND logic — every rule must be met. This is typically used to layer security on top of the basic access criteria defined by Include rules. For example, administrators can require that anyone trying to access an application use specific MFA methods.</p>
</li>
<li>
<p><strong>Exclude</strong> rules define exceptions to access, overriding other rule types. If a user matches an &quot;Exclude&quot; rule, they're denied access regardless of other policy conditions. For example, a user may meet a requirement to use a MFA method during login, but if their specific <a href="/cloudflare-one/access-controls/policies/mfa-requirements/">multifactor authentication (MFA) method</a> is defined in an Exclude rule, they will be blocked by the policy. Alternatively, if a user is associated with a 'high risk' IdP group, they can be excluded on that basis even if they meet all the other posture requirements.</p>
</li>
</ul>
<p>A useful way to imagine how these different types of rules are applied, is to imagine a funnel. Include selectors define what attributes of the user, traffic or device are included in the policy that will be Allowed, Blocked and so on. Require then further filters from that list what attributes must be associated with the user with the Exclude type filtering out users who have matched both the Include and Require.</p>
<p><img src="/assets/upstream/images/reference-architecture/designing-ztna-access-policies-for-cloudflare-access/figure5.svg" alt="Figure 5 - Policies and rules are evaluated in a funnel. With Include rules aggregating all users, Require rules mandating specific requirements and Exclude rules removing user identities from the policy evaluation." title="Figure 5 - Policies and rules are evaluated in a funnel. With Include rules aggregating all users, Require rules mandating specific requirements and Exclude rules removing user identities from the policy evaluation." /></p>
<p>The above diagram visualises an example for the policy &quot;All employees and contractors on secure devices using strong MFA&quot;. Anyone in the group &quot;All Employees&quot; or contractors who have authenticated with a username in their company domain will match this policy. They are required to be using a device that has the latest OS and is using encrypted storage. They must have authenticated with an MFA factor, but not SMS. Also, they must be accessing the application via Cloudflare's secure web gateway.</p>
<p>There are many different <a href="/cloudflare-one/access-controls/policies/#selectors">types of selectors</a>. While every possible selector is not listed here, the following lists specific outcomes that organizations using Cloudflare Access typically desire when building policies. This will help you understand how to achieve a specific outcome.</p>
<ul>
<li>
<p><strong>Is user traffic coming over Cloudflare Gateway?</strong>
Guaranteeing that a user only accesses an application over our SWG, Cloudflare Gateway, is a great way to prevent unauthorized access due to phishing or credential theft. Additionally, you can ensure all traffic bound to the application is logged and filtered by Cloudflare Gateway.</p>
<p>You can configure this control by enabling the &quot;gateway&quot; device posture check and then requiring &quot;gateway&quot; in your application policies. Requiring &quot;gateway&quot; is more flexible than relying solely on the device agent because users can also on-ramp from Browser Isolation or a Cloudflare WAN-connected site, both of which provide traffic logging and filtering. Additionally, when using the device agent, this allows you to guarantee that a user is coming from a compliant device that has passed a set of device posture checks.</p>
<p>Requiring the gateway is enforced continuously for <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted applications</a>. For SaaS apps, it is only enforced at the time of login. However, a dedicated egress IP can be leveraged in tandem to enforce that traffic always goes via Cloudflare Gateway.</p>
</li>
<li>
<p><strong>Does the user belong to an existing group, or have specific identity attributes?</strong>
If your IdP supports SCIM, group membership information can be imported into Cloudflare, where it can be used in policies. Group information can also come from the SAML or OAuth data sent as part of authentication. In fact, when OIDC or SAML is used and claims are sent, they can be used in a policy. So if your users authenticate to your IDP using SAML, and the resulting token contains their &quot;role,&quot; you can query that value in the rule.</p>
</li>
<li>
<p><strong>Which identity service was used for authentication ?</strong>
Similar to IdP groups and attributes, this &quot;Login methods&quot; selector asks which identity service was used, and, like IdP groups, this is better suited to an access group rather than a specific line item on an access policy. Login methods allow you to apply different policies to specific users who authenticated with certain identity providers. For example, you might only allow users who have authenticated with a consumer identity such as GitHub or LinkedIn to gain access if their authentication method included a hard token-based MFA.</p>
<p>This is an atypical scenario, but if you do need to enable multiple IdPs for authentication, then you can use this selector to make sure users are authenticating with a specific service. The value of this requirement becomes clearer when dealing with multiple layered security policies, and need to define different levels of access based on the login.</p>
</li>
<li>
<p><strong>Individual or organizational emails</strong>
All identity services provide an email address, which in many cases matches the individual's username. Using an email in a policy can be useful when wanting to allow access to an entire domain of users, but they might authenticate via a consumer IdP that allows for any email. For example, you might only allow access for users who have authenticated via GitHub using their @company.com email address.</p>
<p>Another good use of this selector is if you are managing a <a href="/cloudflare-one/reusable-components/lists/">list of emails</a> of users that might be high risk or have been blocked from a specific application. You can use an Exclude rule, with your list to ensure a subset of users cannot access an application.</p>
</li>
<li>
<p><strong>How did the user authenticate?</strong>
When an identity provider authenticates a user and then redirects them back to Cloudflare, it includes information about what authentication method was used. This is typically sent as <a href="https://datatracker.ietf.org/doc/html/rfc8176">Authentication Method Reference</a> data. Using this you can check if MFA was used and what type.</p>
<p>This can be useful to define different levels of credential requirements for different applications. For example, a general company application might just require that MFA was used and not care how. But a really sensitive administration tool might require a FIDO2 hardware-based security key,and therefore explicitly deny access if only an OTP via SMS is used as part of the authentication process.</p>
</li>
<li>
<p><strong>What country is the request coming from?</strong>
You can set rules based on the geographic lookup of the incoming request. This could be useful for restricting access to certain countries where you do business.</p>
</li>
<li>
<p><strong>What IP range is the request coming from?</strong>
You can set rules based on the IP range of the incoming request. This could be allowing access only from your corporate network IP ranges.</p>
</li>
<li>
<p><strong>Is it possible to verify device or user information from a list?</strong>
Sometimes, you might want to grant or restrict access based on specific device or user characteristics that do not fit neatly into other categories. This is where <a href="/cloudflare-one/reusable-components/lists/">lists</a> come in handy: you can define or import a list of contractor emails, or a list of approved device serial numbers and use those as criteria within an Access policy. These lists can be updated manually or via our <a href="/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/create/">API</a>, allowing for integration with other device or user management systems.</p>
</li>
<li>
<p><strong>Is the device's security posture adequate?</strong>
This is where the device client provides telemetry on the native device making the access request. It accomplishes this by performing device-level scans. Is the device's hard drive encrypted? The agent can check if technologies like BitLocker or FileVault are active, in addition to checking for specific volume names. If you are protecting a sensitive application, or something that holds critical information, this is an effective requirement to enforce.</p>
</li>
<li>
<p><strong>Is the request being made by another process or application?</strong>
It is not always a real human on a device attempting to access an application. This makes it useful to leverage Cloudflare Access to manage communication to APIs by other software. The request may contain service tokens, mutual TLS certificates, and SSH certificates, which enables logins for automated processes and machine-to-machine communication. Using service auth options within Cloudflare also centralizes the storage and lifecycle management of these tokens and certificates.</p>
</li>
<li>
<p><strong>What does your third-party tool say about your device?</strong>
Many organizations use other specialized tools for endpoint security, such as Crowdstrike, SentinelOne, or Microsoft Intune, to provide telemetry regarding the security posture of the device making the application request. Rather than require the user to navigate multiple UIs, you can integrate these tools into Cloudflare One via their API, and apply their insights into device posture attributes that can be enforced during an application login.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12706.md")
</aside>
<h4 id="additional-settings">Additional settings</h4>
<p>Below are a few additional application settings to consider that help improve security.</p>
<h5 id="isolate-application">Isolate application</h5>
<p>Sometimes you want to manage access to a self-hosted application for less trusted, third-party users such as contractors or partners. You might want to allow them to read content in an application, but limit their ability to download files, copy and paste data, and print the page. Cloudflare Access allows you to render the application in a remote <a href="/cloudflare-one/access-controls/policies/isolate-application/">browser</a> (using <a href="/cloudflare-one/remote-browser-isolation/">remote browser isolation, or RBI</a>) so that the application is rendered using a headless browser on our network versus sending all the content down to the user's browser. This allows Cloudflare to then enforce a range of controls over how the user can interact with the content.</p>
<p>The setting is at the policy level, so one policy can allow trusted users (such as employees) to access applications normally, while another policy with browser isolation enabled can apply the RBI service for contractors.</p>
<p>This setting forces traffic to an isolated browser before being delivered to the end user, which means all traffic is then inspected and managed by Cloudflare Gateway. To limit what the user can do, you need to create an accompanying policy in the gateway, which also identifies the same users and then enforces the <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings">controls</a> you wish to limit access. Note that it is important to write the Gateway policy such that it only enforces RBI for the same group of users accessing the application that the Cloudflare Access policy applies to. Otherwise, the policy will default to enforce browser isolation for all users.</p>
<p>It is possible to actually enforce RBI for the same set of users if they attempt to access the application using a non-secured device. In this case, you would continue to define a policy for employees in Cloudflare Access. But then, also create a policy in Cloudflare Gateway to isolate the application if users going to the same application URL have failed a device posture check that deems the device is not managed or secure. This could be if the device does not have the company endpoint security client (Crowdstrike or SentinelOne for example) installed, or has failed a security check. We will demonstrate this in the use cases below.</p>
<p>Inversely, isolating the browser also protects the local device from anyone attempting to exploit vulnerabilities or execute malicious code against the application.</p>
<h5 id="justification">Justification</h5>
<p>You may wish to audit an application's every authentication event and capture justification details. This setting creates a more well-defined audit trail of user access, and allows administrators to review and analyze access patterns and justifications. When enabled, users will be prompted to provide a brief explanation before gaining access. This can be particularly useful for sensitive applications or during specific time periods, such as outside normal business hours.</p>
<h5 id="temporary-authentication">Temporary authentication</h5>
<p>Add an additional layer of access control by requiring users to obtain &quot;temporary authentication&quot; approval from designated authorizers before accessing the application. When enabled, users requesting access will trigger a notification to authorized approvers.</p>
<h3 id="access-groups">Access Groups</h3>
<p>One of the most important parts of defining ZTNA policies is to leverage reusable elements called <a href="/cloudflare-one/access-controls/policies/groups/">Access Groups</a>. Each access group uses the same rules we've just described to define users, traffic or devices. These groups can then be used across many policies to allow, deny, bypass, or isolate access to an application.</p>
<p>For example, you can define &quot;Employees&quot; once as an Access Group, and then use that in every application policy where you want to refer to employees. Updates to this Access Group would then be reflected in every policy. This is also a good way to include nested logic (for example, users with a Linux device and has antivirus software enabled)</p>
<p>Below is a diagram featuring an Access Group named &quot;Secure Administrators,&quot; which uses a range of attributes to define the characteristics of secure administrators. The diagram shows the addition of two other Access Groups within &quot;Secure Administrators&quot;. The groups include devices running on either the latest Windows or macOS, along with the requirement that the device must have either File</p>
<p><img src="/assets/upstream/images/reference-architecture/designing-ztna-access-policies-for-cloudflare-access/figure6.svg" alt="Figure 6 - An access group that matches to IT administrators on secure systems." title="Figure 6 - An access group that matches to IT administrators on secure systems." /></p>
<h2 id="use-cases">Use cases</h2>
<p>Now that the basic infrastructure to secure access to an application and the policy systems have been covered, let's dive into some common use cases.</p>
<h3 id="only-allow-company-wiki-access-to-users-on-trusted-devices">Only allow company wiki access to users on trusted devices</h3>
<p>Many companies host some sort of internal content system where confidential company information resides. Wiki's are a common type of application that allows employees to collaborate easily with anyone. But because this information is confidential, it is important to both validate the user authentication with strong credentials, and also ensure that their access is via a secure device, via a secure connection.</p>
<p>However, sometimes company users use non-company devices and need to access the wiki. You may wish to set up a policy that allows this, but limits the user's actions. For instance, prevent them from editing the data, or from copying and pasting it to their unmanaged device. This use case explains how to set up a Cloudflare Access application to define secure access for employees, giving them fully functional access when they are on a secured device over a secured connection, but still allow them some limited access from a non secure device.</p>
<p>First, create an Access application with the following parameters:</p>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">Company Wiki</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Type</td>
<td align="left">Self-hosted</td>
</tr>
<tr>
<td align="left">Public Hostname</td>
<td align="left">wiki.mycustomerexample.com</td>
</tr>
<tr>
<td align="left">Authentication</td>
<td align="left">Company Microsoft Entra IdP</td>
</tr>
<tr>
<td align="left">Policies</td>
<td align="left">Employees on trusted devices Employees using untrusted devices</td>
</tr>
</tbody>
</table>
<p>Before we examine how the two policies are defined, observe an example where an Access Group was created to identify an employee and approved devices were running the latest operating system version.</p>
<h4 id="access-group-secure-employees">Access Group: Secure employees</h4>
<p>This access group is going to be used in both policies, and its sole goal is to identify what a &quot;Secure Employee&quot; is.</p>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">Secure Employees</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Include</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Azure AD Groups</td>
<td align="left">&quot;Full-Time Employees&quot;</td>
</tr>
<tr>
<td align="left"><strong>Require</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Azure AD Groups</td>
<td align="left">&quot;Completed security training&quot;</td>
</tr>
<tr>
<td align="left">OS Version</td>
<td align="left">&quot;Latest version of macOS&quot;, &quot;Latest version of Windows&quot;, &quot;Latest Kernel version for Linux&quot;</td>
</tr>
</tbody>
</table>
<p>This is a very simple Access Group, with just two group selectors. Note that because we are checking membership based on groups from a specific directory, it also implies that the user must have authenticated to that directory. It means in the future, if you move to another identity provider or change the group membership requirements for what defines a Full-Time Employee, you change just this Access Group once.</p>
<p>As you can see, it defines that &quot;all employees&quot; are those in the Azure AD group &quot;Full Time Employees&quot;, who are also in the group &quot;Completed security training.&quot; The first selector defines the initial scope of the Access Group, and the second selector requires that they must also be in that specific group.</p>
<p>This Access Group requires that three <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">device posture checks</a> have been created for the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/">OS version</a>. For example, the posture check &quot;Latest version of macOS&quot; is defined as &quot;macOS version is greater than or equal to 15.1&quot; and reflects the latest version the company considers stable and secure (vs. the very latest OS version). Once included in the Access policy, this will enforce the logic we’ve established here - if any user wants to sign in as a 'Secure Employee', they'll need to meet these requirements.</p>
<h4 id="employees-on-trusted-devices">Employees on trusted devices</h4>
<p>Now we define the first policy in the application. First, select the Access Group that has already been defined. Then, define the following rules to determine how users authenticate and how they connect to the application.</p>
<table>
<thead>
<tr>
<th align="left">Policy name</th>
<th align="left">Employees on trusted devices</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Action</td>
<td align="left">Allow</td>
</tr>
<tr>
<td align="left">Access groups</td>
<td align="left">Include - Secure employees</td>
</tr>
<tr>
<td align="left"><strong>Rules</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Require</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Authentication Method</td>
<td align="left">MFA - Multiple Factor Authentication</td>
</tr>
<tr>
<td align="left">Gateway</td>
<td align="left">On</td>
</tr>
<tr>
<td align="left"><strong>Additional settings</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Isolate Application</td>
<td align="left">No</td>
</tr>
</tbody>
</table>
<p>This policy ensures that users can gain full access to your company wiki only if they have passed the following requirements:</p>
<ul>
<li>They are full-time employees on devices with the latest operating system.</li>
<li>Users have authenticated using MFA.</li>
<li>Users are accessing the application via a device that has the Cloudflare device agent running.</li>
</ul>
<h4 id="employees-using-untrusted-devices">Employees using untrusted devices</h4>
<p>The second policy should handle users who are not on secure devices. Note that this policy is second in the list of policies in the application and therefore will be evaluated when users do not meet the requirements of the first policy.</p>
<table>
<thead>
<tr>
<th align="left">Policy name</th>
<th align="left">Employees using untrusted devices</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Action</td>
<td align="left">Allow</td>
</tr>
<tr>
<td align="left">Access groups</td>
<td align="left">Include - All Employees</td>
</tr>
<tr>
<td align="left"><strong>Rules</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Require</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Authentication Method</td>
<td align="left">MFA - Multiple Factor Authentication</td>
</tr>
<tr>
<td align="left"><strong>Additional settings</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Isolate Application</td>
<td align="left">Yes</td>
</tr>
</tbody>
</table>
<p>Although this policy is very similar to the first, it removes the requirement to have a device on the latest operating system and also using our device agent. The user is still required to be a full-time employee authenticated with strong, MFA-backed credentials.</p>
<p>But notice we now enable &quot;Isolate Application.&quot; What does this mean? This forces all requests to the application to now be rendered on our RBI technology. RBI will prevent the wiki UX from loading directly in the end user's browser, and instead renders the content in a headless browser running on a server in Cloudflare's global cloud network. Then, the results of that render are securely and efficiently communicated down to the end user's browser. Because of this, the request is also sent via our SWG service, which enables you to write a policy that controls how users can interact with the wiki.</p>
<p><strong>Gateway HTTP Policy</strong></p>
<table>
<thead>
<tr>
<th align="left">Isolate company applications for users on insecure devices</th>
<th align="left"></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Action</td>
<td align="left">Isolate</td>
</tr>
<tr>
<td align="left"><strong>Traffic</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Domain in</td>
<td align="left">wiki.mycustomerexample.com</td>
</tr>
<tr>
<td align="left"><strong>Device Posture</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Passed device posture not in</td>
<td align="left">Warp Check</td>
</tr>
<tr>
<td align="left"><strong>Settings</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Disable copy / paste</td>
<td align="left">Yes</td>
</tr>
<tr>
<td align="left">Disable file downloads</td>
<td align="left">Yes</td>
</tr>
<tr>
<td align="left">Disable file uploads</td>
<td align="left">Yes</td>
</tr>
<tr>
<td align="left">Disable keyboard</td>
<td align="left">Yes</td>
</tr>
<tr>
<td align="left">Disable printing</td>
<td align="left">Yes</td>
</tr>
</tbody>
</table>
<p>In the example above, the SWG policy is matching any traffic heading to your company wiki, then enforcing RBI (to match the ZTNA application policy) and then disabling all interaction with the wiki.</p>
<p>It also adds the device posture check &quot;WARP Check (Mac OS)&quot; to scan the user's device for the presence of our device agent. If the user's device does not have the agent installed and enabled, then the device posture check cannot occur and they will automatically fail to meet the policy requirements. If the user does have the device agent enabled, then they will pass the posture check and be granted full wiki access. Note that &quot;WARP&quot; is the previous name for the Cloudflare One Client, which is Cloudflare's device agent.</p>
<p>Essentially, the employee on an insecure device is permitted to view the wiki in a &quot;read-only&quot; mode, but is restricted from further interactions like uploading/downloading or copying/pasting confidential information.</p>
<p>This policy approach accomplishes several objectives:</p>
<ol>
<li>It enforces the use of trusted devices for full access to the wiki, aligning with your Zero Trust security goals.</li>
<li>It provides a fallback option for employees using personal devices, allowing them to access the wiki in a limited, secure manner through browser isolation.</li>
<li>It incentivizes employees to use their company devices and/or keep the Cloudflare One Client enabled, which is a net positive for an organization's security posture.</li>
<li>It demonstrates the power and flexibility of more granular security controls achieved by combining Cloudflare Access policies with Cloudflare Gateway HTTP policies.</li>
</ol>
<p>This approach both secures your wiki and establishes a model for protecting other applications — allowing your organization to maintain strong cyber hygiene while adapting to the realities of hybrid work scenarios.</p>
<h3 id="secure-access-to-salesforce">Secure access to Salesforce</h3>
<p>The second use case implements a secure access strategy that also requires the use of the device client. However, the implementation is slightly more involved than the previous wiki example.</p>
<p>Before addressing the specifics, you will learn about the benefits of securing access to SaaS apps through Cloudflare. After all, Salesforce and other major SaaS providers already offer robust security features, including their own access controls, MFA, and audit logs. So why do some organizations still choose to route their SaaS traffic through Cloudflare?</p>
<p>The key benefit here is centralizing security policy enforcement across your entire IT ecosystem. By routing Salesforce access through Cloudflare, you are not just securing Salesforce – you are integrating it into a broader Zero Trust strategy that includes a single point of visibility for all user activity, and reduces the complexity of managing multiple security systems. It also allows you to implement the enforcement of many different IdPs for access to a single SaaS application.</p>
<p>In the context of this use case, it is important to protect Salesforce — which contains sensitive customer data — against misuse, and to secure access only to authorized users. We are going to design a secure access policy that can cover both of these objectives.</p>
<p>The first step is to configure an <a href="/cloudflare-one/traffic-policies/egress-policies/">egress IP policy under Cloudflare Gateway</a>. This allows you to purchase and assign specific IPs to your users that have their traffic filtered via Gateway. Then in Salesforce, you can enforce that access is only permitted for traffic with a source IP that matches the one in your egress policy. This combination ensures that the only way to get access to Salesforce is via Cloudflare.</p>
<table>
<thead>
<tr>
<th align="left">Egress Policy</th>
<th align="left"></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Identity</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">User Group Names</td>
<td align="left">All Employees</td>
</tr>
<tr>
<td align="left"><strong>Select Egress IP</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Use dedicated Cloudflare Egress IPs</td>
<td align="left">[203.0.113.88]</td>
</tr>
</tbody>
</table>
<p>This is important not only for securing access to Salesforce, but also for adequately protecting its contents while in use. The next step is to examine the access policy which is similar to the one we just created for the wiki. However, this policy is limiting access to members of the Sales or Executives groups. We are also using our Crowdstrike integration to ensure that users are on company managed devices.</p>
<table>
<thead>
<tr>
<th align="left">Policy name</th>
<th align="left">Account executives on trusted devices</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Action</td>
<td align="left">Allow</td>
</tr>
<tr>
<td align="left"><strong>Include</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Member of group</td>
<td align="left">Sales, Executives</td>
</tr>
<tr>
<td align="left"><strong>Require</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Authentication method</td>
<td align="left">MFA - multi-factor authentication</td>
</tr>
<tr>
<td align="left">Gateway</td>
<td align="left">On</td>
</tr>
<tr>
<td align="left">Crowdstrike Service to Service</td>
<td align="left">Overall Score above 80</td>
</tr>
</tbody>
</table>
<p>The second policy now applies to all employees but we are going to apply a few more steps before access is granted.</p>
<table>
<thead>
<tr>
<th align="left">Policy name</th>
<th align="left">Employees on trusted devices</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Action</td>
<td align="left">Allow</td>
</tr>
<tr>
<td align="left"><strong>Include</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Member of group</td>
<td align="left">All Employees</td>
</tr>
<tr>
<td align="left"><strong>Require</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Authentication method</td>
<td align="left">MFA - multi-factor authentication</td>
</tr>
<tr>
<td align="left">Gateway</td>
<td align="left">On</td>
</tr>
<tr>
<td align="left">Crowdstrike Service to Service</td>
<td align="left">Overall Score above 80</td>
</tr>
<tr>
<td align="left"><strong>Additional Settings</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Purpose justification</td>
<td align="left">On</td>
</tr>
<tr>
<td align="left">Temporary authentication</td>
<td align="left">On</td>
</tr>
<tr>
<td align="left">Email addresses of approvers</td>
<td align="left"><a href="mailto:salesforce-admin@company.com">salesforce-admin@company.com</a></td>
</tr>
</tbody>
</table>
<p>We are going to add in temporary authentication to this second policy. That means if Cloudflare determines that the incoming request is from someone outside of the Sales or Executives department, an administrator will need to explicitly grant them temporary access. In context, this policy could be used to secure access to Salesforce for employees outside the Sales department, as the customer information could be sensitive and confidential.</p>
<p>This approach is important for several reasons:</p>
<ul>
<li>It allows for human oversight on potentially risky access attempts, reducing the chance of unauthorized access through compromised or insecure devices.</li>
<li>It provides flexibility for legitimate users to access the application even when their device fails to meet the highest security standards. This encourages users to maintain good security practices on their devices.</li>
<li>In addition, since all user traffic is routed through Cloudflare, we can enforce additional security measures (such as preventing the download of sensitive data) via web traffic policies.</li>
</ul>
<h3 id="only-allow-secure-admins-access-to-database-tools">Only allow secure admins access to database tools</h3>
<p>This scenario covers protecting a PostgreSQL database administration tool. This represents a privately-hosted, high-value target due to its access to sensitive data. It also requires taking extra care in designing secure access for it. Given the nature of database tools, access policies will not be layered for this use case.</p>
<table>
<thead>
<tr>
<th align="left">Policy name</th>
<th align="left">Only IT admin access</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Action</td>
<td align="left">Allow</td>
</tr>
<tr>
<td align="left"><strong>Include</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Assign a group</td>
<td align="left">IT Admins</td>
</tr>
<tr>
<td align="left"><strong>Require</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Authentication method</td>
<td align="left">MFA - multi-factor authentication</td>
</tr>
<tr>
<td align="left">Gateway</td>
<td align="left">On</td>
</tr>
<tr>
<td align="left">Device Posture - Serial Number List</td>
<td align="left">Company Managed Device Serial Numbers</td>
</tr>
<tr>
<td align="left">OS Version</td>
<td align="left">Latest version of Windows</td>
</tr>
<tr>
<td align="left">Domain Joined</td>
<td align="left">Joined to corporate AD domain</td>
</tr>
<tr>
<td align="left"><strong>Exclude</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Authentication method</td>
<td align="left">SMS</td>
</tr>
<tr>
<td align="left"><strong>Additional Settings</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Purpose justification</td>
<td align="left">On</td>
</tr>
</tbody>
</table>
<p>Here, we are introducing a high number of security posture checks, starting with MFA. We have two expressions regarding MFA: the first one requires that users authenticate with a MFA method. The second 'excludes' expression pointing out that SMS is not considered a valid authentication method. We do this because SMS is one of the easier methods for attackers to exploit and subvert, and therefore <a href="https://sec.okta.com/articles/2020/05/sms-two-factor-authentication-worse-just-good-password">considered less secure</a> than other MFA methods. As a result, we are only allowing access when the user provides stronger credentials such as a hard key or an OTP from an authenticator app. Enforcing these stricter MFA requirements reduces the risk of credential-based attacks, and makes it much more challenging for potential attackers to gain unauthorized access to this critical database—even if they have obtained the user's password.</p>
<p>Other posture elements here include:</p>
<ul>
<li>Requiring the latest OS.</li>
<li>The user's device is joined to a Microsoft Active Directory domain.</li>
<li>The user's device is explicitly a company-managed device (shown by referencing a list of managed device serial numbers).</li>
</ul>
<p>These combined posture checks ensure that only up-to-date, company-controlled devices within your managed environment can access the database, further reducing the attack surface and the risk of access from potentially compromised or uncontrolled endpoints.</p>
<p>Under additional settings, we are also requiring that users enter a purpose justification for accessing the database. This allows your security teams to analyze access patterns and identify potentially suspicious behavior. This set of security controls also ensures that access to your critical database is tightly regulated, logged, and justified — significantly reducing the risk of unauthorized access or misuse.</p>
<p>This level of protection and visibility would be significantly more complex and resource-intensive to achieve with disparate, standalone security solutions. Centralizing security policy enforcement via Cloudflare allows you to simplify how you implement fine-grained access to critical internal resources.</p>
<h3 id="secure-rdp-access">Secure RDP access</h3>
<p>This final use case centers on securing remote access to devices via RDP in two ways — self-hosted or private IP. Both options offer unique benefits, but ultimately it comes down to your priorities: is it more important to simplify access, or to tightly monitor activity?</p>
<p>We will start with the self-hosted option — proxying port 3389 over a tunnel, mapping it to a hostname.</p>
<table>
<thead>
<tr>
<th align="left">Application Configuration</th>
<th align="left"></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Application Name</td>
<td align="left">RDP service on database server</td>
</tr>
<tr>
<td align="left">Hostname</td>
<td align="left">rdp.databaseserver.company.internal</td>
</tr>
</tbody>
</table>
<p>Define the policy:</p>
<table>
<thead>
<tr>
<th align="left">Policy name</th>
<th align="left">Admin Access</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Action</td>
<td align="left">Allow</td>
</tr>
<tr>
<td align="left"><strong>Include</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Member of Group</td>
<td align="left">IT Admins</td>
</tr>
<tr>
<td align="left"><strong>Require</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Authentication method</td>
<td align="left">MFA - multi-factor authentication</td>
</tr>
<tr>
<td align="left">Gateway</td>
<td align="left">On</td>
</tr>
<tr>
<td align="left">WARP</td>
<td align="left">On</td>
</tr>
<tr>
<td align="left">Device Posture - Serial Number List</td>
<td align="left">Company Managed Device Serial Numbers</td>
</tr>
<tr>
<td align="left">External Evaluation</td>
<td align="left">[Time Evaluator URL]</td>
</tr>
</tbody>
</table>
<p>Inside the policy, we have made this application available to our new access group for IT Admins. Under &quot;Require,&quot; we are enforcing the use of the Cloudflare One Client specifically (as opposed to only Cloudflare Gateway). The user must be on a company-managed device, with an active device client that is authenticated to the company's instance of Cloudflare, MFA must be used during login, and there is an additional option below for external evaluation.</p>
<p><a href="/cloudflare-one/access-controls/policies/external-evaluation/">External evaluation</a> means we have an API endpoint containing some sort of <a href="https://github.com/cloudflare/workers-access-external-auth-example">access logic</a> — in this case, time of day access. We are making an API call to this endpoint, and defining the key that Cloudflare is using to verify that the response came from the API. This is useful for several reasons:</p>
<p>External evaluation allows users to create bespoke security posture checks based on criteria that may not be covered by the default set of posture checks. For this example, we will be using a service built on <a href="https://workers.cloudflare.com/">Cloudflare Workers</a>.</p>
<ul>
<li>Restricting access to the terminal outside of business hours implements a form of time-based access control. This adds an extra layer of security by limiting the window of opportunity for potential attackers.</li>
</ul>
<p>Now, you will learn how to secure RDP access as a private IP application:</p>
<table>
<thead>
<tr>
<th align="left">Application Configuration</th>
<th align="left"></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Application Name</td>
<td align="left">RDP</td>
</tr>
<tr>
<td align="left">Destination IP</td>
<td align="left">169.254.255.254</td>
</tr>
</tbody>
</table>
<p>As mentioned before, private IP applications work because Cloudflare proxies the IP range across its network. The nature of this application necessitates the use of the device client, as unless the user is connected to Cloudflare (and more specifically, unless they can take advantage of the Client-to-Tunnel connectivity), they will not be able to reach non-local RFC 1918 addresses.</p>
<table>
<thead>
<tr>
<th align="left">Traffic</th>
<th align="left"></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Destination IP</td>
<td align="left">169.254.255.254</td>
</tr>
<tr>
<td align="left">Destination Port</td>
<td align="left">3389</td>
</tr>
<tr>
<td align="left"><strong>Identity</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">User Group Names</td>
<td align="left">Server Admins</td>
</tr>
<tr>
<td align="left"><strong>Device Posture</strong></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Passed Device Posture Checks</td>
<td align="left">WARP Check (Mac OS) (File) Latest Version of macOS (OS version)</td>
</tr>
<tr>
<td align="left"><strong>Action</strong></td>
<td align="left">Allow</td>
</tr>
<tr>
<td align="left"><strong>Enforce Cloudflare One Client session duration</strong></td>
<td align="left">60m0s</td>
</tr>
</tbody>
</table>
<p>Defining the application here is simple, as Cloudflare automatically fills in the IP range, and you need to limit the detected protocol to RDP. However, the rules for private IP applications are slightly different. You will notice they appear as network policies under the Cloudflare Gateway menu, despite managing them in Access. Certain options, such as checking for MFA and external evaluation, do not appear here. However, these attributes can be verified when the user activates their device client and authenticates to their organization.</p>
<p>One option available here is enforcing the device agent client session duration. This means that after a certain amount of time, the user will be forced to reauthenticate. This feature allows you to take a Zero Trust approach to protecting private IP applications as well. It ensures that even if a user's credentials are compromised or their device is left unattended, the potential window for unauthorized access is limited. By regularly requiring reauthentication, we are continuously verifying the user's identity and authorization status, aligning with the core Zero Trust principle of &quot;never trust, always verify.&quot;</p>
<p>By combining granular access controls with detailed activity logging, Cloudflare provides a comprehensive security solution for protecting and monitoring access to critical resources in a Zero Trust methodology.</p>
<h2 id="summary">Summary</h2>
<p>Successful ZTNA implementation is about more than just technical configuration — it requires careful consideration of your organization's specific needs, user workflows, and security requirements. Cloudflare's flexibility allows you to start with basic secure access policies, then evolve them as your organization's needs change and security requirements mature. By following the principles and practices outlined in this guide, you can create a robust security posture that protects you as precisely and transparently as possible.</p>
<p>If you are interested in learning more about ZTNA, SASE, or other aspects of the Cloudflare One platform, please visit our <a href="/reference-architecture/">reference architecture library</a> or our <a href="/">developer docs</a> to get started.</p>
<p>Related resources</p>
<ul>
<li><a href="/reference-architecture/architectures/sase/">Cloudflare SASE reference architecture</a></li>
<li><a href="/reference-architecture/architectures/cloudflare-sase-with-microsoft/">Using Cloudflare SASE with Microsoft</a></li>
<li><a href="/learning-paths/clientless-access/concepts/">How to deploy Cloudflare ZTNA</a></li>
</ul>
