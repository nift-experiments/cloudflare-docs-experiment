<h2 id="introduction">Introduction</h2>
<p>SaaS applications have become essential tools in today's business operations. While SaaS applications reduce IT and infrastructure burden, they also introduce new security challenges that traditional architectures struggle to address. Many companies today are on the path to implementing a <a href="https://zerotrustroadmap.org/">Zero Trust architecture</a>, which heavily combines identity, device and network information to better secure applications.</p>
<p>However SaaS applications tend to focus their security on their own platform, such as storing data at rest in a secure manner and ensuring their applications are not exposing customer data due to application vulnerabilities. This document is going to cover how to address some of the limitations of SaaS applications by using Cloudflare's Secure Access Service Edge (SASE) platform. Specifically our Zero Trust Network Access (ZTNA) and Secure Web Gateway (SWG) services, combined with integrations to your existing identity and device security vendors.</p>
<h2 id="is-saas-not-already-secure">Is SaaS not already secure?</h2>
<p>Before discussing the specifics of implementing SASE for SaaS applications, we should consider asking: is SaaS not already secure? Major providers like Salesforce, ServiceNow, Microsoft and more have implemented robust security capabilities, including integrations with identity providers for Single Sign On (SSO), SSL/TLS for all application communication, encryption of data at rest and comprehensive audit logs. Unfortunately, SaaS vendors are not attempting to rebuild entire security platforms in their applications, so they are not able to provide many features required for a modern Zero Trust architecture.</p>
<p>SaaS applications are unable to evaluate the security posture of connecting devices. A compromised laptop with valid credentials appears identical to a securely managed, corporate device. When data is downloaded from the SaaS application, it has no visibility into where it goes or if the device it is being downloaded to is secure. Typically authentication for SaaS applications is externalized by redirecting users to an identity service, therefore the SaaS application has no sense of how the user authenticated and as such all trust is placed in the identity provider.</p>
<p>These security challenges are compounded by poor network access controls — most SaaS applications accept connections from any Internet source, but sometimes they can be limited to only accessing from a specific set of IP addresses that might be associated with one or more physical offices. But these rudimentary network controls are hard to expand for remote users working from home, or partners and contractors who need access.</p>
<p>Cloudflare's SASE platform offers the ability to bring a more Zero Trust orientated approach to securing SaaS applications. Centralized policies, based on device posture, identity attributes and granular network location can be applied across one or many SaaS applications. Cloudflare becomes the new corporate network, and it is possible to gate access to Internet based SaaS applications to those users and devices that are connected to Cloudflare. Essentially it is a new corporate network in the cloud.</p>
<h2 id="securing-access-with-cloudflare">Securing access with Cloudflare</h2>
<p>The diagram below shows how Cloudflare sits between your users, devices and networks that require access to any SaaS application. The two main services proving security capabilities are:</p>
<ul>
<li><a href="/cloudflare-one/access-controls/policies/">Zero Trust Network Access</a>. Allows Cloudflare to become an identity proxy, so that you can easily enable authentication with a wide variety of identity providers to a single SaaS application. This service also incorporates the ability to evaluate access based on device posture and network location.</li>
<li><a href="/cloudflare-one/traffic-policies/">Secure Web Gateway</a>. Once all traffic to access the SaaS application flows through our gateway, HTTPS connections are terminated at Cloudflare and you have the ability to inspect the data flowing to and from the SaaS application. This allows you to block sensitive data from being exported to insecure locations.</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/secure-access-to-saas-applications-with-sase/figure1.svg" alt="Figure 1: Only traffic that has passed the Cloudflare network and relevant policies is authorized to access the SaaS application." title="Figure 1: Only traffic that has passed the Cloudflare network and relevant policies is authorized to access the SaaS application." /></p>
<p>The above diagram shows the variety of ways in which traffic can on-ramp to Cloudflare, where the ZNTA service ensures authentication and the Secure Web Gateway filters both inbound and outbound traffic to/from the SaaS application.</p>
<ol>
<li>Initial requests to the SaaS application are redirected to Cloudflare as part of SSO flow. ZTNA service authenticates users against existing identity providers.</li>
<li>A user, authenticated or not, is denied access to the SaaS application if their traffic is not sourced from Cloudflare.</li>
<li>A user on a non-managed device can use browser isolation, where the browser accessing the SaaS application runs on a Cloudflare server, and the results of the rendered page are securely delivered to a user's local browser.</li>
<li>A managed device is connected to Cloudflare using a secure tunnel and therefore all communication from device to SaaS application is filtered and secured.
<ol>
<li>Cloudflare agent device posture can also be incorporated into authorizing traffic from these devices.</li>
</ol>
</li>
<li>A device connected to a local network, where all Internet traffic is routed to Cloudflare via a secure IPsec tunnel to Cloudflare, also ensures all traffic from network to SaaS application is filtered and secured.</li>
<li>Traffic then passes through our secure web gateway, where DNS and HTTP policies can be applied to traffic.
<ol>
<li>HTTP policies allow the examination of the data being both uploaded and downloaded from the SaaS application using DLP profiles.</li>
</ol>
</li>
<li>Traffic egresses Cloudflare with a specific IP. The SaaS application is configured to allow all traffic coming from that address.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="xdr-platform-integrations">XDR platform integrations</h3>
@markup("md", "content/.markup/bodies/12721.md")
</aside>
<h2 id="example-policy">Example policy</h2>
<p>The following is an example set of policies which demonstrate how you can use Cloudflare to secure access to Salesforce.</p>
<p>The first step is using an <a href="/cloudflare-one/traffic-policies/egress-policies/">egress IP policy under Cloudflare Gateway</a>. This allows you to purchase and assign specific IPs to users that have their traffic filtered via Gateway. Then in Salesforce, you enforce that access is only permitted for traffic with a source IP that matches the one in your egress policy. This combination ensures that the only way to get access to Salesforce is via Cloudflare.</p>
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
<td align="left"><code>203.0.113.88</code></td>
</tr>
</tbody>
</table>
<p>This is important not only for securing access to Salesforce, but also for adequately protecting its contents while in use. Now let us examine the access policy that is limiting access to members of the Sales or Executives groups. We are also using our Crowdstrike integration to ensure that users are on company managed devices.</p>
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
<p>This second policy applies to all employees but we are going to apply a few more steps before access is granted.</p>
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
<td align="left"><code>salesforce-admin@company.com</code></td>
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
<p>Cloudflare's SASE platform allows organizations to centralize security policy for accessing SaaS applications. It also enhances security by allowing you to leverage device posture and network attributes. You can configure it in a way where your SaaS application essentially is only accessible via your new corporate network which is built on Cloudflare.</p>
<h2 id="related-resources">Related Resources</h2>
<ul>
<li><a href="/reference-architecture/architectures/sase/">Evolving to a SASE architecture with Cloudflare</a></li>
<li><a href="/reference-architecture/design-guides/designing-ztna-access-policies/">Designing ZTNA access policies for Cloudflare Access</a></li>
<li><a href="/reference-architecture/diagrams/sase/sase-clientless-access-private-dns/">Access to private apps without having to deploy client agents</a></li>
</ul>
