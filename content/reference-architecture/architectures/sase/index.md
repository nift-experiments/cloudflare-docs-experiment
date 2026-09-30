<p>Download a <a href="/reference-architecture/static/cloudflare-evolving-to-a-sase-architecture.pdf">PDF version</a> of this reference architecture.</p>
<h2 id="introduction">Introduction</h2>
<p>Cloudflare One is a secure access service edge (SASE) platform that protects enterprise applications, users, devices, and networks. By progressively adopting Cloudflare One, organizations can move away from their patchwork of hardware appliances and other point solutions and instead consolidate security and networking capabilities on one unified control plane. Such network and security transformation helps address key challenges modern businesses face, including:</p>
<ul>
<li>Securing access for any user to any resource with Zero Trust practices</li>
<li>Defending against cyber threats, including multi-channel phishing and ransomware attacks</li>
<li>Protecting data in order to comply with regulations and prevent leaks</li>
<li>Simplifying connectivity across offices, data centers, and cloud environments</li>
</ul>
<p>Cloudflare One is built on Cloudflare's <a href="https://www.cloudflare.com/connectivity-cloud/">connectivity cloud</a>, ​​a unified, intelligent platform of programmable cloud-native services that enable any-to-any connectivity between all networks (enterprise and Internet), cloud environments, applications, and users. It is one of the <a href="https://www.cloudflare.com/network/">largest global networks</a>, with data centers spanning <a href="https://www.cloudflare.com/network/">hundreds of cities worldwide</a> and interconnection with <div class="nb-data-component" data-cf-component="PublicStats"></div>. It also has a greater presence in <a href="https://bgp.he.net/report/exchanges#_participants">core Internet exchanges</a> than many other large technology companies.</p>
<p>As a result, Cloudflare operates within ~50 ms of ~95% of the world's Internet-connected population. And since all Cloudflare services are designed to run across every network location, all traffic is connected, inspected, and filtered close to the source for the best performance and consistent user experience.</p>
<p>This document describes a reference architecture for organizations working towards a SASE architecture, and shows how Cloudflare One enables such security and networking transformation.</p>
<h3 id="who-is-this-document-for-and-what-will-you-learn">Who is this document for and what will you learn?</h3>
<p>This reference architecture is designed for IT or security professionals with some responsibility over or familiarity with their organization's existing infrastructure. It is useful to have some experience with technologies important to securing hybrid work, including identity providers (IdPs), user directories, single sign on (SSO), endpoint security or management (EPP, XDR, UEM, MDM), firewalls, routers, and point solutions like packet or content inspection hardware, threat prevention, and data loss prevention technologies.</p>
<p>To build a stronger baseline understanding of Cloudflare, we recommend the following resources:</p>
<ul>
<li>What is Cloudflare? | <a href="https://www.cloudflare.com/what-is-cloudflare/">Website</a> (5 minute read) or <a href="https://youtu.be/XHvmX3FhTwU?feature=shared">video</a> (2 minutes)</li>
</ul>
<ul>
<li>Solution Brief: <a href="https://cfl.re/SASE-SSE-platform-brief">Cloudflare One</a> (3 minute read)</li>
<li>Whitepaper: <a href="https://cfl.re/internet-native-sase-architecture-whitepaper">Overview of Internet-Native SASE Architecture</a> (10 minute read)</li>
<li>Blog: <a href="https://blog.cloudflare.com/zero-trust-sase-and-sse-foundational-concepts-for-your-next-generation-network/">Zero Trust, SASE, and SSE: foundational concepts for your next-generation network</a> (14 minute read)</li>
</ul>
<p>Those who read this reference architecture will learn:</p>
<ul>
<li>How Cloudflare One protects an organization's employees, devices, applications, data, and networks</li>
<li>How Cloudflare One fits into your existing infrastructure, and how to approach migration to a SASE architecture</li>
<li>How to plan for deploying Cloudflare One</li>
</ul>
<p>While this document examines Cloudflare One at a technical level, it does not offer fine detail about every product in the platform. Instead, it looks at how all the services in Cloudflare One enable networking and network security to be consolidated on one architecture. Visit the <a href="https://developers.cloudflare.com/">developer documentation</a> for further information specific to a product area or use case.</p>
<h2 id="disintegration-of-the-traditional-network-perimeter">Disintegration of the traditional network perimeter</h2>
<p>Traditionally, most employees worked in an office and connected locally to the company network via Ethernet or Wi-Fi. Most business systems (e.g. file servers, printers, applications) were located on and accessible only from this internal network. Once connected, users would typically have broad access to local resources. A security perimeter was created around the network to protect against outsider threats, most of which came from the public Internet. The majority of business workloads were hosted on-premises and only accessible inside the network, with very little or no company data or applications existing on the Internet.</p>
<p>However, three important trends created problems for this &quot;castle and moat&quot; approach to IT security:</p>
<ol>
<li><strong>Employees became more mobile</strong>. Organizations increasingly embrace remote / hybrid work and support the use of personal (i.e. not company-owned) devices.</li>
<li><strong>Cloud migration accelerated</strong>. Organizations are moving applications, data, and infrastructure from expensive on-premises data centers to public or private cloud environments in order to improve flexibility, scalability, and cost-effectiveness.</li>
<li><strong>Cyber threats evolved</strong>. The above trends expand an organization's attack surface. For example, attack campaigns have become more sophisticated and persistent in exploiting multiple channels to infiltrate organizations, and cybercriminals face lower barriers to entry with the popularity of the &quot;cybercrime-as-a-service&quot; black market.</li>
</ol>
<p>Traditional perimeter-based security has struggled to adapt to these changes. In particular, extending the &quot;moat&quot; outwards has introduced operational complexity for administrators, poor experiences for users, and inconsistency in how security controls are applied across users and applications.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-1.svg" alt="With many different methods to connect networks and filter/block traffic, managing access to company applications is costly and time consuming." /></p>
<p>The diagram above shows an example of this adapted perimeter-based approach, in which a mix of firewalls, WAN routers, and VPN concentrators are connected with dedicated WAN on-ramps consisting of MPLS circuits and/or leased lines. The diagram also demonstrates common problem areas. In an effort to centralize policy, organizations sometimes force all employee Internet traffic through their VPN infrastructure, which results in slow browsing and user complaints. Employees then seek workarounds — such as using non-approved devices — which increases their exposure to Internet-borne attacks when they work from home or on public Wi-Fi. In addition, IT teams are unable to respond quickly to changing business needs due to the complexity of their network infrastructure.</p>
<p>Such challenges are driving many organizations to prioritize goals like:</p>
<ul>
<li>Accelerating business agility by supporting remote / hybrid work with secure any-to-any access</li>
<li>Improving productivity by simplifying policy management and by streamlining user experiences</li>
<li>Reducing cyber risk by protecting users and data from phishing, ransomware, and other threats across all channels</li>
<li>Consolidating visibility and controls across networking and security</li>
<li>Reducing costs by replacing expensive appliances and infrastructure (e.g. VPNs, hardware firewalls, and MPLS connections)</li>
</ul>
<h2 id="understanding-a-sase-architecture">Understanding a SASE architecture</h2>
<p>In recent years, <a href="https://www.cloudflare.com/learning/access-management/security-service-edge-sse/">secure access service edge</a>, or SASE, has emerged as an aspirational architecture to help achieve these goals. In a SASE architecture, network connectivity and security are unified on a single cloud platform and control plane for consistent visibility, control, and experiences from any user to any application.</p>
<p>SASE platforms consist of networking and security services, all underpinned by supporting operational services and a policy engine:</p>
<ul>
<li>Network services forward traffic from a variety of networks into a single global corporate network. These services provide capabilities like firewalling, routing, and load balancing.</li>
<li>Security services apply to traffic flowing over the network, allowing for filtering of certain types of traffic and control over who can access what.</li>
<li>Operational services provide platform-wide capabilities like logging, API access, and comprehensive Infrastructure-as-Code support through providers like Terraform.</li>
<li>A policy engine integrates across all services, allowing admins to define policies which are then applied across all the connected services.</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-2.svg" alt="Cloudflare's SASE cloud platform offers network, security, and operational services, as well as policy engine features, to provide zero trust connectivity between a variety of user identities, devices and access locations to customer applications, infrastructure and networks." /></p>
<h2 id="cloudflare-one-single-vendor-single-network-sase">Cloudflare One: single-vendor, single-network SASE</h2>
<p>Most organizations move towards a SASE architecture progressively rather than all at once, prioritizing key security and connectivity use cases and adopting services like <a href="https://www.cloudflare.com/learning/access-management/what-is-ztna/">Zero Trust Network Access</a> (ZTNA) or <a href="https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/">Secure Web Gateway</a> (SWG). Some organizations choose to use SASE services from multiple vendors. For most organizations, however, the aspiration is to consolidate security with a single vendor, in order to achieve simplified management, comprehensive visibility, and consistent experiences.</p>
<p><a href="https://www.cloudflare.com/cloudflare-one/">Cloudflare One</a> is a single-vendor SASE platform where all services are designed to run across all locations. All traffic is inspected closest to its source, which delivers consistent speed and scale everywhere. And thanks to composable and flexible on-ramps, traffic can be routed from any source to reach any destination.</p>
<p>Cloudflare's connectivity cloud also offers many other services that improve application performance and security, such as <a href="https://www.cloudflare.com/learning/security/api/what-is-an-api-gateway/">API Gateway</a>, <a href="https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/">Web Application Firewall</a>, <a href="https://www.cloudflare.com/learning/cdn/what-is-a-cdn/">Content Delivery</a>, or <a href="https://www.cloudflare.com/learning/ddos/ddos-mitigation/">DDoS mitigation</a>, all of which can complement an organization's SASE architecture. For example, our Content Delivery Network (CDN) features can be used to improve the performance of a self hosted company intranet. Cloudflare's full range of services are illustrated below.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-4.svg" alt="Cloudflare's anycast network allows provides services on all connected servers to enable secure connections on public and home networks and at corporate offices." /></p>
<h3 id="cloudflare-s-anycast-network">Cloudflare's anycast network</h3>
<p>Cloudflare's SASE platform benefits from our use of <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">anycast</a> technology. Anycast allows Cloudflare to announce the IP addresses of our services from every data center worldwide, so traffic is always routed to the Cloudflare data center closest to the source. This means traffic inspection, authentication, and policy enforcement take place close to the end user, leading to consistently high-quality experiences.</p>
<p>Using anycast ensures the Cloudflare network is well balanced. If there is a sudden increase in traffic on the network, the load can be distributed across multiple data centers – which in turn, helps maintain consistent and reliable connectivity for users. Further, Cloudflare's large <a href="https://www.cloudflare.com/network/">network capacity</a> and <a href="https://blog.cloudflare.com/meet-traffic-manager/">AI/ML-optimized smart routing</a> also help ensure that performance is constantly optimized.</p>
<p>By contrast, many other SASE providers use Unicast routing in which a single IP address is associated with a single server and/or data center. In many such architectures, a single IP address is then associated with a specific application, which means requests to access that application may have very different network routing experiences depending on how far that traffic needs to travel. For example, performance may be excellent for employees working in the office next to the application's servers, but poor for remote employees or those working overseas. Unicast also complicates scaling traffic loads — that single service location must ramp up resources when load increases, whereas anycast networks can share traffic across many data centers and geographies.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-5.svg" alt="Cloudflare's anycast network ensures fast and reliable connectivity, whereas Unicast routing often sends all traffic to a single IP address, resulting in slower and failure prone connections." /></p>
<h2 id="deploying-a-sase-architecture-with-cloudflare">Deploying a SASE architecture with Cloudflare</h2>
<p>To understand how SASE fits into an organization's IT infrastructure, see the diagram below, which maps out all the common components of said infrastructure. Subsequent sections of this guide will add to the diagram, showing where each part of Cloudflare's SASE platform fits in.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-6.svg" alt="Typical enterprise IT infrastructure may consist of different physical locations, devices and data centers that require connectivity to multiple cloud and on-premises applications." /></p>
<p>In the diagram's top half there are a variety of Internet resources (e.g. Facebook), SaaS applications (e.g. ServiceNow), and applications running in an <a href="https://www.cloudflare.com/learning/cloud/what-is-iaas/">infrastructure-as-a-service (IaaS)</a> platform (e.g. AWS). This example organization has already deployed cloud based <a href="https://www.cloudflare.com/learning/access-management/what-is-an-identity-provider/">identity providers</a> (IdP), <a href="https://www.cloudflare.com/learning/security/glossary/what-is-endpoint/">unified endpoint management</a> (UEM) and endpoint protection platforms (EPP) as part of a Zero Trust initiative.</p>
<p>In the bottom half are a variety of users, devices, networks, and locations. Users work from a variety of locations: homes, headquarters and branch offices, airports, and others. The devices they use might be managed by the organization or may be personal devices. In addition to the cloud, applications run in a data center in the organization's headquarters and in a data center operators' colo facility (<a href="https://www.equinix.com/">Equinix</a>, in this example).</p>
<p>A SASE architecture will define, secure, and streamline how each user and device will connect to the various resources in the diagram. Over the following sections, this guide will show ways to integrate Cloudflare One into the above infrastructure:</p>
<ul>
<li><strong>Applications and services</strong>: Placing access to private applications and services behind Cloudflare</li>
<li><strong>Networks</strong>: Connecting entire networks to Cloudflare</li>
<li><strong>Forwarding device traffic</strong>: Facilitating access to Cloudflare-protected resources from any device</li>
<li><strong>Verifying users and devices</strong>: Identifying which users access requests come from, and which devices those users have</li>
</ul>
<h3 id="connecting-applications">Connecting applications</h3>
<p>This journey to a SASE architecture starts with an organization needing to provide remote access to non-Internet facing, internal-only web applications and services (e.g. SSH or RDP). Organizations typically deploy VPN appliances to connect users to the company network where the applications are hosted. However, many applications now live in cloud Infrastructure-as-a-Service platforms, where traditional VPN solutions are hard to configure. This often results in poor application and connectivity performance for users.</p>
<h4 id="tunnels-to-self-hosted-applications">Tunnels to self-hosted applications</h4>
<p><a href="https://www.cloudflare.com/learning/access-management/what-is-ztna/">Zero Trust Network Access</a> (ZTNA) is a SASE service that secures access to self-hosted applications and services. ZTNA functionality can be divided broadly into two categories: 1) establishing connectivity between Cloudflare's network and the environments where the applications are running, and 2) setting policies to define how users are able to access these applications. In this section, we first examine the former — how to connect apps to Cloudflare.</p>
<p>Connectivity to self-hosted applications is facilitated through tunnels that are created and maintained by a software connector,
<a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/"><code>cloudflared</code></a>. <code>cloudflared</code> is a lightweight daemon installed in an organizations' infrastructure that creates a tunnel via an outbound connection to Cloudflare's global network. The connector can be installed in a variety of ways:</p>
<ul>
<li>In the OS installed on the bare metal server</li>
<li>In the OS that is running in a virtualized environment</li>
<li>In a <a href="https://hub.docker.com/r/cloudflare/cloudflared">container</a> running in a Docker or Kubernetes environment</li>
</ul>
<p><code>cloudflared</code> runs on Windows, Linux, or macOS operating systems and creates an encrypted tunnel using QUIC, a modern protocol that uses UDP (instead of TCP) for fast tunnel performance and modern encryption standards. Generally speaking, there are two approaches for how users can deploy <code>cloudflared</code> in their environment:</p>
<ol>
<li><strong>On the same server and operating system where the application or service is running</strong>. This is typically in high-risk or compliance deployments where organizations require independent tunnels per application. <code>cloudflared</code> consumes a small amount of CPU and RAM, so impact to server performance is marginal.</li>
<li><strong>On a dedicated server(s) in the same network where the applications run</strong>. This often takes the form of multiple containers in a Docker or Kubernetes environment.</li>
</ol>
<p><code>cloudflared</code> manages multiple outbound connections back to Cloudflare and usually requires no changes to network firewalls. Those connections are spread across servers in more than one Cloudflare data center for reliability and failover. Traffic destined for a tunnel is forwarded to the connection that is geographically closest to the request, and if a <code>cloudflared</code> connection isn't responding, the tunnel will automatically failover to the next available.</p>
<p>For more control over the traffic routed through each tunnel connection, users can integrate with the Cloudflare <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/">load balancing</a> service. To ensure reliable local connectivity, organizations should deploy more than one instance of <code>cloudflared</code> across their application infrastructure. For example, with ten front-end web servers running in a Kubernetes cluster, you might deploy three kubernetes services <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/">running <code>cloudflared</code> replicas</a>.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-7.svg" alt="Using cloudflared, multiple outbound connections are created back to Cloudflare across multiple data centers to improve overall performance and reliability." /></p>
<p>Once tunnels have been established, there are two methods for how user traffic is forwarded to your application or service. Each method below is protected by policies managed by the ZTNA service that enforces authentication and access (which will be explored in further depth <a href="#secure-access-to-self-hosted-apps-and-services">later in this document</a>).</p>
<h5 id="public-hostname">Public hostname</h5>
<p>Each public hostname is specific to an address, protocol, and port associated with a private application, allowing for narrow access to a specific service when there might be multiple applications running on the same host.</p>
<p>For example, organizations can define a public hostname (<code>mywebapp.domain.com</code>) to provide access to a web server running on <code>https://localhost:8080</code>, while ensuring no access to local Kubernetes services.</p>
<p>Key capabilities:</p>
<ul>
<li>A hostname is created in a public DNS zone and all requests to that hostname are first routed to the Cloudflare network, inspected against configured security and access policies, before being routed through the tunnel to the secured private resource</li>
<li>Multiple hostnames can be defined per tunnel, with each hostname mapping to a single application (service address and port)</li>
<li>Support for HTTP/HTTPS protocols</li>
<li>Access to resources only requires a browser</li>
<li>When Cloudflare's device client is deployed on a user device, policies can leverage additional contextual signals (e.g. determining whether the device is managed or running the latest OS) in policy enforcement</li>
<li>For access to SSH/VNC services, Cloudflare renders an SSH/VNC terminal using webassembly in the browser</li>
</ul>
<p>Applications exposed this way receive all of the benefits of Cloudflare's leading DNS, CDN, and DDoS services as well as our web application firewall (WAF), API, and bot services, all without exposing application servers directly to the Internet.</p>
<h5 id="private-network">Private network</h5>
<p>In some cases, users may want to leverage ZTNA policies to provide access to many applications on an entire private network. This allows for greater flexibility over the ways clients connect and how services are exposed. It also enables communication to resources over protocols other than HTTP. In this scenario, users specify the subnet for the private network they wish to be accessible via Cloudflare.</p>
<p>Key capabilities:</p>
<ul>
<li><code>cloudflared</code>, combined with Cloudflare device agent, provides access to private networks, allowing for any arbitrary L4 TCP, UDP or ICMP connections</li>
<li>One or many networks can be configured using CIDR notation (e.g. 172.21.0.16/28)</li>
<li>Access to resources on the private network requires the Cloudflare device agent to be installed on clients, and at least one Cloudflare Tunnel server on the connecting network</li>
</ul>
<p>For both methods, it is important to note that <code>cloudflared</code> only proxies inbound traffic to a private application or network. It does not become a gateway or &quot;on-ramp&quot; back to Cloudflare for the network that it proxies inbound connections to. This means that if the web server starts its own connection to another Internet-based API, that connection will not be routed via Cloudflare Tunnel and will instead be routed via the host server's default route and gateway.</p>
<p>This is the desirable outcome in most network topologies, but there are some instances in which network services need to communicate directly with a remotely-connected user, or with services on other segmented networks.</p>
<p>If users require connections that originate from the server or network to be routed through Cloudflare, there are multiple on-ramps through which to achieve this, which will be explained further in the &quot;Connecting Networks&quot; section.</p>
<h4 id="saas-applications">SaaS applications</h4>
<p>SaaS applications are inherently always connected to and accessed via the public Internet. As a result, the aforementioned tunnel-and-app-connector approach does not apply. Instead, organizations with a SASE architecture inspect and enforce policies on Internet-bound SaaS traffic via a <a href="https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/">secure web gateway</a> (SWG), which serves as a cloud-native forward proxy.</p>
<p>The SWG includes policies that examine outbound traffic requests and inbound content responses to determine if the user, device, or network location has access to resources on the Internet. Organizations can use these policies to control access to approved SaaS applications, as well as detect and block the use of unapproved applications (also known as <a href="https://www.cloudflare.com/learning/access-management/what-is-shadow-it/">shadow IT</a>).</p>
<p>Some SaaS applications allow organizations to configure an IP address allowlist, which limits access to the application based on the source IP address of the request. With Cloudflare, organizations can obtain dedicated <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">egress IP</a> addresses, which can be used as the source address for all traffic leaving their network. When combined with an allowlist in a SaaS application, organizations can ensure that users are only able to access applications if they are first connected to Cloudflare. (More detail on this approach is outlined in a later section about connecting user devices.)</p>
<p>Another method to secure access to SaaS applications is to configure single sign-on (SSO) so that Cloudflare becomes an identity proxy — acting as the identity provider (IDP) — as part of the authentication and authorization process.</p>
<p>Key capabilities:</p>
<ul>
<li>Apply consistent access policies across both self-hosted and SaaS applications</li>
<li>Layer device security posture into the authentication process (e.g. users can ensure that only managed devices, running the latest operating system and passing all endpoint security checks, are able to access SaaS applications)</li>
<li>Ensure that certain network routes are used for access (e.g. users can require that devices are connected to Cloudflare using the device agent, which allows them to filter traffic to the SaaS application and prevent downloads of protected data)</li>
<li>Centralize SSO applications to Cloudflare and create one SSO integration from Cloudflare to their IdP — making both infrastructure and access policies SSO-agnostic (e.g. users can allow access to critical applications only when MFA is used, no matter which IdP is used to authenticate)</li>
</ul>
<p>When Cloudflare acts as the SSO service to an application, user authentication is still handled by an organization's existing identity provider, but is proxied via Cloudflare, where additional access restrictions can be applied. The diagram below is a high-level example of a typical request flow:</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-8.svg" alt="The flow of SSO requests is proxied through Cloudflare, where the IdP is still used to authenticate, but Cloudflare provides additional access controls." /></p>
<p>The last method of connecting SaaS applications to Cloudflare's SASE architecture is with an API-based <a href="https://www.cloudflare.com/learning/access-management/what-is-a-casb/">cloud access security broker</a> (CASB). The Cloudflare CASB integrates via API to <a href="/cloudflare-one/integrations/cloud-and-saas/">popular SaaS suites</a> — including Google Workspace, Microsoft 365, Salesforce, and more — and continuously scans these applications for misconfigurations, unauthorized user activity, and other security risks.</p>
<p>Native integration with the Cloudflare <a href="https://www.cloudflare.com/learning/access-management/what-is-dlp/">data loss prevention</a> (DLP) service enables CASB to scan for sensitive or regulated data that may be stored in files with incorrect permissions — further risking leaks or unauthorized access. CASB reports findings that alert IT teams to items such as:</p>
<ul>
<li>Administrative accounts without adequate MFA</li>
<li>Company-sensitive data in files stored with public access permissions</li>
<li>Missing application configurations (e.g. domains missing SPF/DMARC records)</li>
</ul>
<h4 id="checkpoint-connecting-applications-to-cloudflare">Checkpoint: Connecting applications to Cloudflare</h4>
<p>Now, this is what the architecture of a typical organization might look like once they have integrated with Cloudflare services. It is important to note that Cloudflare is designed to secure organizations' existing applications and services in the following ways:</p>
<ul>
<li>All self-hosted applications and services are only accessible through Cloudflare and controlled by policies defined by the Cloudflare ZTNA</li>
<li>SaaS application traffic is filtered and secured via the Cloudflare SWG</li>
<li>SaaS services are scanned via the Cloudflare CASB to check for configuration and permissions of data at rest</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-9.svg" alt="Access to all applications is now only available via Cloudflare." /></p>
<h3 id="connecting-networks">Connecting networks</h3>
<p>Once an organization's applications and services have been integrated, it is time to connect Cloudflare to their existing networks. Regional offices, corporate headquarters, retail locations, data centers, and cloud-hosted infrastructure all need to forward traffic to the new corporate SASE network.</p>
<p>When all traffic flows through Cloudflare, SASE services perform the following actions:</p>
<ul>
<li>Granting application access</li>
<li>Filtering general Internet-bound traffic (e.g. blocking access to sites that host malware)</li>
<li>Isolating web sites to protect users from day-zero or unknown harmful Internet content</li>
<li>Filtering traffic to identify data defined by DLP policies — then blocking the download/upload of that data to insecure devices or applications</li>
<li>Providing visibility into the use of non-approved applications and allowing admins to either block or apply policies around their use</li>
</ul>
<p>There are several approaches for connecting networks to Cloudflare, which can provide further flexibility in how an organization provides access to SASE-protected resources:</p>
<ol>
<li><strong>Use software agents to create tunnels from host machines back to Cloudflare</strong>. This is typically the method favored by users who own their own servers and applications.</li>
<li><strong>Set up IPsec or GRE tunnels from network routers and firewalls to connect them to the Cloudflare WAN service</strong>. This is the approach that network administrators use when they want to forward traffic to and from entire networks.</li>
<li><strong>Connect a network directly to Cloudflare</strong>. This method works best when an organization's network resides in a supported data center, usually one that is colocated with a Cloudflare data center.</li>
</ol>
<p>These methods will be explained further in the next sections.</p>
<h4 id="using-software-agents">Using software agents</h4>
<p>There are two software-based methods of connecting networks to Cloudflare, depending on the type of applications that currently exist on the network.</p>
<h5 id="client-to-server-connectivity">Client-to-server connectivity</h5>
<p>As described in the previous section, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/"><code>cloudflared</code></a> proxies requests to applications and services on private networks. It installs on servers in the private network and creates secure tunnels to Cloudflare over the Internet. These connections are balanced across multiple Cloudflare data centers for reliability and can be made via multiple connectors, which helps increase the capacity of the tunnels.</p>
<p>Using <code>cloudflared</code>, Cloudflare Tunnel supports client to server connections over the Tunnel. Any service or application running behind the Tunnel will use the default routing table when initiating outbound connectivity.</p>
<p>This model is appropriate for a majority of scenarios, in which external users need to access resources within a private network that does not require bidirectionally-initiated communication.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-10.svg" alt="Requests initiated from a client are securely tunneled to Cloudflare via a device agent, while requests from inside the private network follow the default route." /></p>
<p>For bidirectional, or meshed connectivity, organizations should use Cloudflare Mesh.</p>
<h5 id="mesh-connectivity">Mesh connectivity</h5>
<p><a href="/mesh/">Cloudflare Mesh</a> (formerly WARP Connector) is a lightweight solution for site-to-site, bidirectional, and mesh networking connectivity that does not require changes to underlying network routing infrastructure. Cloudflare Mesh is installed on a Linux server within an organization's network, which then becomes a gateway for other local networks that need to on-ramp traffic to Cloudflare.</p>
<p>This provides a lightweight solution to support services such as Microsoft's System Center Configuration Manager (SCCM), Active Directory server updates, VOIP and SIP traffic, and developer workflows with complex CI/CD pipeline interaction. It can either be run supplementally to <code>cloudflared</code> and Cloudflare WAN (formerly Magic WAN), or can be a standalone remote access and site-to-site connector to the Cloudflare network.</p>
<p>Cloudflare Mesh can proxy both user-to-network and network-to-network connectivity, or can be used to establish an overlay network of Carrier Grade NAT (<a href="https://en.wikipedia.org/wiki/Carrier-grade_NAT">CGNAT</a>) addressed endpoints to provide secure, direct connectivity to established resources using CGNAT IP ranges. This helps address overlapping network IP range challenges, point-solution access problems, or the process of shifting network design without impacting a greater underlying system.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-11.svg" alt="In an example scenario, a developer might push code to a git repository, which ends up in a Kubernetes cluster in a staging network. From staging, it is accessed by a QA tester. All of this traffic is routed and protected via a Cloudflare Mesh node." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>Cloudflare Tunnel via <code>cloudflared</code> is the primary method for connecting users to applications and services on private networks because it is a simpler, more granular and agile solution for many application owners (vs. IP tunnel based connectivity technology, like <a href="https://www.cloudflare.com/learning/network-layer/what-is-ipsec/">IPsec</a> and <a href="https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/">GRE</a>). Cloudflare Mesh is the preferred method for mesh or other software-defined networking — most of which require bidirectional connectivity — when organizations do not want to make changes to the underlying network routing or edge infrastructure.</p>
<h4 id="using-network-equipment">Using network equipment</h4>
<p>Where it is not optimal or possible to install software agents, networks can also be connected to Cloudflare using existing network equipment, such as routers and network firewalls. To do this, organizations create IPsec or GRE tunnels that connect to Cloudflare's cloud-native <a href="https://www.cloudflare.com/network-services/products/magic-wan/">Cloudflare WAN</a> service. With Cloudflare WAN, existing network hardware can connect and route traffic from their respective network locations to Cloudflare through a) secure, IPsec-based tunnels over the Internet or, b) across <a href="https://www.cloudflare.com/network-services/products/network-interconnect/">Cloudflare Network Interconnect</a> (CNI) — private, direct connections that link existing network locations to the nearest Cloudflare data center.</p>
<p>Cloudflare's WAN service uses a &quot;light-branch, heavy-cloud&quot; architecture that represents the evolution of software-defined WAN (SD-WAN) connectivity. With Cloudflare WAN, as depicted in the network architecture diagram below, the Cloudflare global network functions as a centrally-managed connectivity hub that securely and efficiently routes traffic between all existing network locations:</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-12.svg" alt="Cloudflare's Connectivity Cloud securely links a variety of network locations to the Internet through products such as Firewall, ZTNA, CASB and Load Balancer." /></p>
<p>As previously described, Cloudflare uses a routing technique called <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">anycast</a> to globally advertise all of the services and endpoints on the Cloudflare network, including the endpoints for WAN IP tunnels.</p>
<p>With <a href="https://blog.cloudflare.com/anycast-ipsec/">anycast IPsec</a> or anycast GRE tunnels, each tunnel configured from an organization's network device (e.g. edge router, firewall appliance, etc.) connects to hundreds of global Cloudflare data centers. Traffic sourced from an organization's network location is sent directly over these tunnels and always routes to the closest active Cloudflare data center. If the closest Cloudflare data center is unavailable, the traffic is automatically rerouted to the next-closest data center.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-13.svg" alt="In an example scenario, IPsec traffic from an office network's router would be sent to the closest Cloudflare data center." /></p>
<p>To further network resiliency, Cloudflare WAN also supports Equal Cost Multi-Path (ECMP) routing between the Cloudflare network and an organization's network location(s). With ECMP, traffic can be load-balanced across multiple anycast IP tunnels, which helps increase throughput and maximize network reliability. In the event of network path failure of one or more tunnels, traffic can be automatically failed over to the remaining healthy tunnels.</p>
<p>The simplest and easiest way to on-ramp existing network locations to the Cloudflare WAN service is to deploy Cloudflare One Appliance, a lightweight appliance you can install in corporate network locations to automatically connect, steer, and shape any IP traffic through secure IPsec tunnels. When the WAN Connector is installed into a network, it will automatically establish communication with the Cloudflare network, download and provision relevant configurations, establish resilient IPsec tunnels, and route connected site network traffic to Cloudflare.</p>
<p>The WAN Connector can be deployed as either a hardware or virtual appliance, making it versatile for a variety of user network environments — on-premises, virtual, or public cloud. Management, configuration, observability, and software updates for WAN Connectors is centrally managed from Cloudflare via either the dashboard or the Cloudflare API. As of 2023, the WAN Connector is currently best-suited for connecting small and medium-sized networks to Cloudflare (for example, small offices and retail stores).</p>
<p>In situations where deploying the Cloudflare One Appliance is not feasible or desirable, organizations can securely connect their site networks to Cloudflare by configuring IPsec tunnels from their existing IPsec-capable network devices, including WAN or SD-WAN routers, firewalls, and cloud VPN gateways. Please refer to the Cloudflare <a href="/cloudflare-wan/configuration/third-party/">documentation</a> for up-to-date examples of validated IPsec devices.</p>
<p>There may also be situations where network-layer encryption is not necessary — for example, when a site's WAN-bound traffic is already encrypted at the application layer (via TLS), or when an IPsec network device offers very limited throughput performance as it encrypts and decrypts IPsec traffic. Under these circumstances, organizations can connect to the Cloudflare network using <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">GRE tunnels</a>.</p>
<p>Organizations may also connect their network locations directly to the Cloudflare network via <a href="https://www.cloudflare.com/network-services/products/network-interconnect/">Cloudflare Network Interconnect</a> (CNI). Cloudflare <a href="/network-interconnect/">supports a variety of options</a> to connect your network to Cloudflare:</p>
<ul>
<li>Direct CNI for Cloudflare WAN and Magic Transit</li>
<li>Classic CNI for Magic Transit</li>
<li>Cloud CNI for Cloudflare WAN and Magic Transit</li>
<li>Peering via either an internet exchange, or a private network interconnect (PNI).</li>
</ul>
<p>The following table summarizes the different methods of connecting networks to Cloudflare:</p>
<table>
<thead>
<tr>
<th><strong>Use case</strong></th>
<th><strong>Recommended</strong></th>
<th><strong>Alternative solution</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Remote users connecting to applications on private networks in a Zero Trust model (e.g. most VPN replacement scenarios)</td>
<td><strong>Cloudflare Tunnel (with <code>cloudflared</code>)</strong></td>
<td><strong>Cloudflare WAN</strong> Alternative option if <code>cloudflared</code> not suitable for environment</td>
</tr>
<tr>
<td>Site-to-site connectivity between branches, headquarters, and data centers</td>
<td><strong>Cloudflare WAN</strong></td>
<td><strong>Cloudflare Mesh</strong> Alternative option if routing changes cannot be made at perimeter</td>
</tr>
<tr>
<td>Egress traffic from physical sites or cloud environments to cloud security inspection (e.g. most common SWG and branch firewall replacement scenarios)</td>
<td><strong>Cloudflare WAN</strong></td>
<td><strong>N/A</strong></td>
</tr>
<tr>
<td>Service-initiated communication with remote users (e.g. AD or SCCM updates, DevOps workflows, VOIP)</td>
<td><strong>Cloudflare Mesh</strong></td>
<td><strong>Cloudflare WAN</strong> Alternative option if inbound source IP fidelity not required</td>
</tr>
<tr>
<td>Mesh networking and device-to-device connectivity</td>
<td><strong>Cloudflare Mesh</strong></td>
<td><strong>N/A</strong></td>
</tr>
</tbody>
</table>
<p>Each of these methods of connecting and routing traffic can be deployed concurrently from any location. The following diagram highlights how different connectivity methods can be used in a single architecture.</p>
<p>Note the following traffic flows:</p>
<ul>
<li>All traffic connected via a Cloudflare Mesh node or device agent can communicate with each other over the mesh network
<ul>
<li>Developers working from home can communicate with the production and staging servers in the cloud</li>
<li>The employee in the retail location, as well as the developer at home, can receive VOIP calls on their laptop</li>
</ul>
</li>
<li>A HPC Cluster in AWS represents a proprietary solution in which no third-party software agents can be installed; as a result, it uses an IPsec connection to Cloudflare WAN</li>
<li>In the retail location, the Cloudflare One Appliance routes all traffic to Cloudflare via an IPsec tunnel
<ul>
<li>An employee's laptop running the device agent creates its own secure connection to Cloudflare that is routed over the IPsec tunnel</li>
</ul>
</li>
<li>The application owner of the reporting system maintains a connection to Cloudflare using <code>cloudflared</code> and doesn't require any networking help to expose their application to employees</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-14.svg" alt="Connecting and routing traffic can be created using various methods such as Cloudflare Network Interconnect, IPSEC tunnels, Cloudflare Mesh and cloudflared." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p><em>Note: All of the endpoints connected via Cloudflare Mesh or device agent are automatically assigned IP addresses from the 100.96.0.0/12 address range, while endpoints connected to Cloudflare WAN retain their assigned RFC1918 private IP addresses. <code>cloudflared</code> can be deployed in any of the locations by an application owner to provide hostname-based connectivity to the application.</em></p>
<p>Once the networks, applications, and user devices are connected to Cloudflare — regardless of the connection methods and devices used — all traffic can be inspected, authenticated, and filtered by the Cloudflare SASE services, then securely routed to their intended destinations. Additionally, consistent policies can be applied across all traffic, no matter how it arrives at Cloudflare.</p>
<h4 id="checkpoint-connecting-networks-to-cloudflare">Checkpoint: Connecting networks to Cloudflare</h4>
<p>Now this is what a SASE architecture looks like where corporate network traffic from everywhere is forwarded to and processed by Cloudflare. In this architecture, it is possible to make a network connection from any remote location, office location or data center and connect to applications and services living in SaaS infrastructure, cloud-hosted infrastructure or an organization's own on-premise data centers.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-15.svg" alt="Traffic from all networks, North and South, as well as East and West, is now flowing through and secured by Cloudflare." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<h3 id="forwarding-device-traffic">Forwarding device traffic</h3>
<p>The previous sections explain using ZTNA to secure access to self-hosted applications and using an SWG to inspect and filter traffic destined for the Internet. When a user is working on a device in any of the company networks that is connected to Cloudflare's connectivity cloud, all that traffic is inspected and policies applied without disrupting the user's workflow. Yet, users are not always (or ever) in the office; they work from home, on the road, or from other public networks. How do you ensure they have reliable access to your internal applications? How do you ensure their Internet browsing is secure no matter their work location?</p>
<p>There are several approaches to ensure that traffic from a user device which isn't connected to an existing Cloudflare protected network, are also forwarding traffic through Cloudflare and be protected.</p>
<ul>
<li><a href="#connecting-with-a-device-agent">Install an agent on the device</a></li>
<li><a href="#browser-proxy-configuration">Modify browser proxy configuration</a></li>
<li><a href="#using-remote-browser-instances">Direct the user to a remote browser instance</a></li>
<li><a href="#agentless-dns-filtering">Modify DNS configuration</a></li>
</ul>
<h4 id="connecting-with-a-device-agent">Connecting with a device agent</h4>
<p>The preferred method of ensuring device traffic is forwarded to Cloudflare is to install the device agent (also referred to as <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>). The agent runs on Windows, macOS, Linux, iOS, and Android/ChromeOS, and creates a secure connection to Cloudflare where all non-local traffic is sent. Because of Cloudflare's use of anycast networking, the device agent always connects to the nearest Cloudflare server to ensure the best performance for the user. The device agent also collects local machine and network information, which is sent in the request to enrich the policy in Cloudflare.</p>
<p>To allow for flexibility in how different devices and users connect, there are multiple <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">deployment modes</a>:</p>
<ul>
<li>A full L4 traffic proxy</li>
<li>L7 DNS proxy</li>
<li>L7 HTTP proxy</li>
<li>The ability to just collect device posture information</li>
</ul>
<p>For example, organizations might have an office that continues to use an existing <a href="https://www.cloudflare.com/learning/access-management/what-is-dns-filtering/">DNS filtering</a> service, so they can configure the agent to just proxy network and HTTP traffic.</p>
<p>The agent can also be configured with flexible routing controls that allow for scenarios in which traffic destined for office printers is not sent to the Cloudflare network but, instead, routed to the local network. These <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">split tunnel configurations</a> can be made specific to groups of users, types of device operating system, or networks and by default, traffic destined to all private <a href="https://datatracker.ietf.org/doc/html/rfc1918">IPv4 and IPv6 ranges</a> is sent to the device's default gateway. If the application the user is attempting to reach is not in public DNS, you can configure the hostname and domain to be resolved with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/private-dns/">local DNS services</a>, so that the device agent does not attempt to resolve these using Cloudflare DNS.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-16.svg" alt="Using the device agent allows Internet and company application bound traffic to be secured by Cloudflare's SWG and ZTNA services." /></p>
<p>The agent is more than just a network proxy; it is able to examine the device's security posture, such as if the operating system is fully up-to-date or if the hard disk is encrypted. Cloudflare's integrations with <a href="https://www.cloudflare.com/partners/technology-partners/crowdstrike/endpoint-partners/">CrowdStrike</a>, <a href="https://www.cloudflare.com/partners/technology-partners/sentinelone/">SentinelOne</a>, and other third-party services also provide additional data about the security posture of the device. All of this information is associated with each request and, therefore, available for use in company policies — as explained in the &quot;Unified Management&quot; section.</p>
<p>The agent can be <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> to a device either manually or using existing endpoint management (UEM) technologies. Using the agent, users register and authenticate their device to Cloudflare with the integrated identity providers. Identity information — combined with information about the local device — is then used in your SWG and ZTNA policies (including inline CASB capabilities shared across these Cloudflare services).</p>
<h4 id="browser-proxy-configuration">Browser proxy configuration</h4>
<p>When it is not possible to install software on the device, there are agentless approaches.</p>
<p>One option is to configure the browser to forward HTTP requests to Cloudflare by configuring proxy server details in the browser or OS. Although this can be done manually, it is more common for organizations to automate the configuration of browser proxy settings using Internet-hosted <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">Proxy Auto-Configuration</a> (PAC) files. The browser identifies the PAC file location in several ways:</p>
<ul>
<li>MDM software configuring the setting in the browser</li>
<li>In Windows domains, Group Policy Objects (GPO) can configure the browser's PAC file</li>
<li>Browsers can use <a href="https://datatracker.ietf.org/doc/html/draft-ietf-wrec-wpad-01">Web Proxy Auto-Discovery</a> (WPAD)</li>
</ul>
<p>From there, configure a proxy endpoint where the browser will send all HTTP requests to. If using this method, please note that:</p>
<ul>
<li>Filtering HTTPS traffic will also require <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">installing and trusting Cloudflare root certificates</a> on the devices.</li>
<li>A proxy endpoint will only proxy traffic sourced from a set of known IP addresses, such as the pool of public IP addresses used by a site's NAT gateway, that the administrator must specify.</li>
</ul>
<h4 id="using-remote-browser-instances">Using remote browser instances</h4>
<p>Another option to ensure device traffic is sent to Cloudflare is to use <a href="https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/">remote browser isolation</a> (RBI). When a remote user attempts to visit a website, the corresponding requests and responses are handled by a headless remote browser running in the Cloudflare network that functions as a &quot;clone&quot; of the user device's local browser. This shields the user's device from potential harmful content and code execution that may be downloaded from the website it visits.</p>
<p>RBI renders the received content in an isolated and secure cloud environment. Instead of executing the web content locally, the user device receives commands for how to &quot;draw&quot; the final rendered web page over a highly optimized protocol supported by all HTML5-compliant browsers on all operating systems. Because the remote browser runs on Cloudflare's servers, SWG policies are automatically applied to all browser requests.</p>
<p>Ensuring access to sites is protected with RBI does not require any local software installation or reconfiguring the user's browser. Below are <a href="/cloudflare-one/remote-browser-isolation/setup/">several ways</a> to accomplish this:</p>
<ul>
<li>Typically, a remote browser session is started as the result of an SWG policy — the user just requests websites without being notified that the content is loading in a remote browser.</li>
<li>Organizations can also provide users with a link that automatically ensures RBI always processes each request.</li>
<li>Organizations can also opt to use the ZTNA service to redirect all traffic from self-hosted applications via RBI instances.</li>
</ul>
<p>All requests via a remote browser pass through the Cloudflare SWG; therefore, policies can enforce certain website access limitations. For instance, browser isolation policies can be established to:</p>
<ul>
<li>Disable copy/paste between a remote web page and the user's local machine; this can prevent the employee from pasting proprietary code into third-party chatbots.</li>
<li>Disable printing of remote web content to prevent contractors from printing confidential information</li>
<li>Disable file uploads/downloads to ensure sensitive company data is not sent to — or downloaded from — certain websites.</li>
<li>Disable keyboard input (in combination with other policies) to limit data being exposed, such as someone typing in passwords to a phishing site.</li>
</ul>
<p>Isolating web applications and applying policies to risky websites helps organizations limit data loss from cyber threats or user error. And, like many Cloudflare One capabilities, RBI can be leveraged across other areas of the SASE architecture. Cloudflare's <a href="https://www.cloudflare.com/learning/email-security/what-is-email-security/">email security</a> service, for example, can automatically rewrite and isolate suspicious links in emails. This &quot;email link isolation&quot; capability helps protect the user from potential malicious activity such as credential harvesting phishing.</p>
<h4 id="agentless-dns-filtering">Agentless DNS Filtering</h4>
<p>Another option for securing traffic via the Cloudflare network is to configure the device to forward DNS traffic to Cloudflare to be inspected and filtered. First <a href="/cloudflare-one/traffic-policies/get-started/dns/#connect-dns-locations">DNS locations</a> are created which allow policies to be applied based on different network locations. They can be determined either by the source IP address for the request or you can use &quot;<a href="https://www.cloudflare.com/learning/dns/dns-over-tls/">DNS over TLS</a>&quot; or &quot;<a href="https://www.cloudflare.com/learning/dns/dns-over-tls/">DNS over HTTPS</a>&quot;.</p>
<p>When using source IP addresses, either the device will need to be told which DNS servers to use, or the local DNS server on the network the device is connected to needs to forward all DNS queries to Cloudflare. For DNS over TLS or HTTPS support, the devices need to be configured and support varies. Our recommendation is to use DNS over HTTPS which has wider operating system support.</p>
<p>All of the above methods result in only the DNS requests — not all traffic — being sent to Cloudflare. SWG DNS policies are then implemented at this level to manage access to corporate network resources.</p>
<h4 id="summary-of-swg-capabilities-for-each-traffic-forwarding-method">Summary of SWG capabilities for each traffic forwarding method</h4>
<p>The following table summarizes SWG capabilities for the various methods of forwarding traffic to Cloudflare (as of Oct 2023):</p>
<table>
<thead>
<tr>
<th></th>
<th>IP tunnel or Interconnect (Cloudflare WAN)</th>
<th>Device Agent (WARP)<sup>*1</sup></th>
<th>Remote Browser</th>
<th>Browser proxy</th>
<th>DNS proxy</th>
</tr>
</thead>
<tbody>
<tr>
<td>Types of traffic forwarded</td>
<td>TCP/UDP</td>
<td>TPC/UDP</td>
<td>HTTP</td>
<td>HTTP</td>
<td>DNS</td>
</tr>
<tr>
<td><strong>Policy types</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>DNS</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>HTTP/S<sup>*2</sup></td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>N/A</td>
</tr>
<tr>
<td>Network (L3/L4 parameter)</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td><strong>Data available in policies</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Identity information</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
<td>No<sup>*3</sup></td>
</tr>
<tr>
<td>Device posture</td>
<td>No</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<td><strong>Capabilities</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Remote browser isolation</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>N/A</td>
</tr>
<tr>
<td>Enforce egress IP</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>N/A</td>
</tr>
</tbody>
</table>
<p>Notes:</p>
<ol>
<li>Running the device agent in DNS over HTTP mode provides user identity information, in addition to the same capabilities as connecting via DNS.</li>
<li>To filter HTTPS traffic, the Cloudflare <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">certificate</a> needs to be installed on each device. This can be automated when using the device agent.</li>
<li>If configuring DNS over HTTPS, it is possible to inject a <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/#filter-doh-requests-by-user">service token</a> into the request, which associates the query with an authenticated user.</li>
</ol>
<h4 id="checkpoint-forwarding-device-traffic-to-cloudflare">Checkpoint: Forwarding device traffic to Cloudflare</h4>
<p>By connecting entire networks or individual devices, organizations can now route user traffic to Cloudflare for secure access to privately-hosted applications and secure public Internet access.</p>
<p>Once traffic from all user devices is forwarded to the Cloudflare network, it is time for organizations to revisit their high-level SASE architecture:</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-17.svg" alt="With all devices and networks connected, any traffic destined for company applications and services all flows through Cloudflare, where policies are applied to determine access." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<h3 id="verifying-users-and-devices">Verifying users and devices</h3>
<p>At this point in implementing SASE architecture, organizations have the ability to route and secure traffic beginning from the point a request is made from a browser on a user's device, all the way through Cloudflare's network to either a company-hosted private application/service or to the public Internet.</p>
<p>But, before organizations define policies to manage that access, they need to know who is making the request and determine the security posture of the device.</p>
<h4 id="integrating-identity-providers">Integrating identity providers</h4>
<p>The first step in any access decision is to determine who is making the request – i.e., to authenticate the user.</p>
<p>Cloudflare integrates with identity providers that manage secure access to resources for organizations' employees, contractors, partners, and other users. This includes support for integrations with any <a href="/cloudflare-one/integrations/identity-providers/generic-saml/">SAML</a> - or OpenID Connect (<a href="/cloudflare-one/integrations/identity-providers/generic-oidc/">OIDC</a>) - compliant service; Cloudflare One also includes pre-built integrations with <a href="/cloudflare-one/integrations/identity-providers/okta/">Okta</a>, <a href="/cloudflare-one/integrations/identity-providers/entra-id/">Microsoft Entra ID (formerly Azure Active Directory)</a>, <a href="/cloudflare-one/integrations/identity-providers/google-workspace/">Google Workspace</a>, as well as consumer IdPs such as <a href="/cloudflare-one/integrations/identity-providers/facebook-login/">Facebook</a>, <a href="/cloudflare-one/integrations/identity-providers/github/">GitHub</a> and <a href="/cloudflare-one/integrations/identity-providers/linkedin/">LinkedIn</a>.</p>
<p>Multiple IdPs can be integrated, allowing organizations to apply policies to a wide range of both internal and external users. When a user attempts to access a Cloudflare secured application or service, they are redirected to authenticate via one of the integrated IdPs. When using the device agent, users must also authenticate to one of their organization's configured IdPs.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-18.svg" alt="Users are presented with a list of integrated identity providers before accessing protected applications." /></p>
<p>Once a user is authenticated, Cloudflare receives that user's information, such as username, group membership, authentication method (password, whether MFA was involved and what type), and other associated attributes (i.e., the user's role, department, or office location). This information from the IdP is then made available to the policy engine.</p>
<p>In addition to user identities, most corporate directories also contain groups to which those identities are members. Cloudflare supports the importing of group information, which is then used as part of the policy. Group membership is a critical part of aggregating single identities so that policies can be less complex. It is far easier — for example — to set a policy allowing all employees in the sales department to access Salesforce, than to identify each user in the sales organization.</p>
<p>Cloudflare also supports authentication of devices that are not typically associated with a human user – such as an IoT device monitoring weather conditions at a factory. For those secure connections, organizations can generate <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service tokens</a> or create <a href="https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/">Mutual TLS</a> (mTLS) certificates that can be deployed to such devices or machine applications.</p>
<h4 id="trusting-devices">Trusting devices</h4>
<p>Not only does the user identity need to be verified, but the security posture of the user's device needs to be assessed. The device agent is able to provide a range of device information, which Cloudflare uses to build comprehensive security policies.</p>
<p>The following built-in posture checks are available:</p>
<ul>
<li><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/application-check/">Application check</a>: Checks that a specific application process is running</li>
<li><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/">File check</a>: Checks for the presence of a file</li>
<li><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/">Firewall</a>: Checks if a firewall is running</li>
<li><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/disk-encryption/">Disk encryption</a>: Checks if/how many disks are encrypted</li>
<li><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/">Domain joined</a>: Checks if the device is joined to a Microsoft Active Directory domain</li>
<li><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/">OS version</a>: Checks what version of the OS is running</li>
<li><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/device-uuid/">Unique Client ID</a>: When using an MDM too, organizations can assign a verifiable UUID to a mobile, desktop, or laptop device</li>
<li><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/">Device serial number</a>: Checks to see if the device serial matches a list of company desktop/laptop computers</li>
</ul>
<p>Cloudflare One can also integrate with any deployed endpoint security solution, such as <a href="/cloudflare-one/integrations/service-providers/microsoft/">Microsoft Endpoint Manager</a>, <a href="/cloudflare-one/integrations/service-providers/taniums2s/">Tanium</a>, <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/carbon-black/">Carbon Black</a>, <a href="/cloudflare-one/integrations/service-providers/crowdstrike/">CrowdStrike</a>, <a href="/cloudflare-one/integrations/service-providers/sentinelone/">SentinelOne</a>, and more. Any data from those products can be passed to Cloudflare for use in access decisions.</p>
<p>All of the above device information, combined with data on the user identity and also the network the device is on, is available in Cloudflare to be used as part of the company policy. For example, organizations could choose to only allow administrators to SSH into servers when all of the following conditions are met: their device is free from threats, running the latest operating system, and joined to the company domain.</p>
<p>Because this information is available for every network request, any time a device posture changes, its ability to connect to an organization's resources is immediately impacted.</p>
<h4 id="integrating-email-services">Integrating email services</h4>
<p>Email — the #1 communication tool for many organizations and the most common channel by which phishing attacks occur — is another important corporate resource that should be secured via a SASE architecture. Phishing is the root cause of upwards of 90% of breaches that lead to financial loss and brand damage.</p>
<p>Cloudflare's email security service scans for signs of malicious content or attachments before they can reach the inbox, and also proactively scans the Internet for attacker infrastructure and attack delivery mechanisms, looking for programmatically-created domains that are used to host content as part of a planned attack. Our service uses all this data to also protect against business and vendor email compromises (<a href="https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/">BEC</a> / <a href="https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/">VEC</a>), which are notoriously hard to detect due to their lack of payloads and ability to look like legitimate email traffic.</p>
<p>Instead of deploying tunnels to manage and control traffic to email servers, Cloudflare provides two methods of email security <a href="/email-security/deployment/">setup</a>:</p>
<ul>
<li><a href="/email-security/deployment/inline/">Inline</a>: Redirect all inbound email traffic through Cloudflare before they reach a user's inbox by modifying MX records</li>
<li><a href="/email-security/deployment/api/">API</a>: Integrate Cloudflare directly with an email provider such as Microsoft 365 or Gmail</li>
</ul>
<p>Modifying MX records (inline deployment) forces all inbound email traffic through our cloud email security service where it is scanned, and — if found to be malicious — blocked from reaching a user's inbox. Because the service works at the MX record level, it is possible to use the email security service with any <a href="https://www.cloudflare.com/learning/email-security/what-is-smtp/">SMTP-compliant</a> email service.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-19.svg" alt="Protecting email with Cloudflare using MX records ensures all emails are scanned and categorized." /></p>
<p>Organizations can also opt to integrate email security directly with their email service via APIs. Note that this approach has two drawbacks: there are fewer integrations Cloudflare supports and there is always a small delay between the email being delivered to the service and Cloudflare detecting it via the API.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-20.svg" alt="Protecting email with Cloudflare using APIs avoids the need to change DNS policy, but introduces delays into email detection and limits the types of email services that can be protected." /></p>
<h4 id="checkpoint-a-complete-sase-architecture-with-cloudflare">Checkpoint: A complete SASE architecture with Cloudflare</h4>
<p>The steps above provide a complete view of evolving to SASE architecture using Cloudflare One. As the diagram below shows, secure access to all private applications, services, and networks — as well as ensuring the security of users' general Internet access — is now applied to all users in the organization, internal or external.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-21.svg" alt="A fully deployed SASE solution with Cloudflare protects every aspect of your business. Ensuring all access to applications is secured and all threats from the Internet mitigated." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>For ease of use, the entire Cloudflare One platform can be configured via <a href="/api/">API</a>; and with Cloudflare's <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a>, organizations can manage the Cloudflare global network using the same tools they use to automate the rest of their infrastructure. This allows IT teams to fully manage their Cloudflare One infrastructure, including all the policies detailed in the next section, using code. There are also (as of Oct 2023) more than 500 <a href="https://github.com/cloudflare">GitHub</a> repositories, many of which allow IT teams to use and build tools to manage their Cloudflare deployment.</p>
<h2 id="unified-management">Unified management</h2>
<p>Now that all users, devices, applications, networks, and other components are seamlessly integrated within a SASE architecture, Cloudflare One provides a centralized platform for comprehensive management. Because of the visibility Cloudflare has across the entire IT infrastructure, Cloudflare can aggregate signals from various sources, including devices, users, and networks. These signals can inform the creation of policies that govern access to organization resources.</p>
<p>Before we go into the details of how policies can be written to manage access to applications, services, and networks connected to Cloudflare, it's worth taking a look at the two main enforcement points in Cloudflare's SASE platform that control access: SWG and the ZTNA services. These services are configured through a single administrative dashboard, simplifying policy management across the entire SASE deployment.</p>
<p>The following diagram illustrates the flow of a request through these services, including the application of policies and the source of data for these policies. In the diagram below, the user request can either enter through the SWG or ZTNA depending on the type of service requested. It's also possible to combine both services, such as implementing a SWG HTTP policy that uses DLP service to inspect traffic related to a privately hosted application behind a ZTNA Cloudflare Tunnel. This configuration enables organizations to block downloads of sensitive data from internal applications that organizations have authorized for external access.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-23.svg" alt="User requests to the Internet or self hosted applications go through our SWG and/or ZTNA service. Administrators have a single dashboard to manage policies across both." /></p>
<p>In the following sections, we introduce examples of how different policies can be configured to satisfy specific use cases. While these examples are not exhaustive, the goal is to demonstrate common ways Cloudflare One can be configured to address the challenges organizations encounter in its transition to a SASE architecture.</p>
<p>Connecting an IdP to Cloudflare provides the ability to make access decisions based on factors such as group membership, authentication method, or specific user attributes. Cloudflare's device agent also supplies additional signals for policy considerations, such as assessing the operating system or verifying the device's serial number against company-managed devices. However, there are features that allow users to incorporate additional data into deployment for building powerful policies.</p>
<h3 id="lists">Lists</h3>
<p>Cloudflare's vast intelligent network continually monitors billions of web assets and <a href="/cloudflare-one/traffic-policies/domain-categories/">categorizes them</a> based on our threat intelligence and general knowledge of Internet content. You can use our free <a href="https://radar.cloudflare.com/">Cloudflare Radar</a> service to examine what categories might be applied to any specific domain. Policies can then include these categories to block known and potential security risks on the public Internet, as well as specific categories of content.</p>
<p>Additionally, Cloudflare's SWG offers the flexibility to create and maintain customized <a href="/cloudflare-one/reusable-components/lists/">lists of data</a>. These lists can be uploaded via CSV files, manually maintained, or integrated with other processes and applications using the Cloudflare API. A list can contain the following data:</p>
<ul>
<li>URLs</li>
<li>Hostnames</li>
<li>Serial numbers (macOS, Windows, Linux)</li>
<li>Emails</li>
<li>IP addresses</li>
<li>Device IDs (iOS, Android)</li>
</ul>
<p>For example, organizations can maintain a list of IP addresses of all remote office locations, of short term contractors' email addresses, or trusted company domains. These lists can be used in a policy to allow contractors access to a specific application if their traffic is coming from a known office IP address.</p>
<h3 id="dlp-profiles-and-datasets">DLP profiles and datasets</h3>
<p>Cloudflare looks at various aspects of a request, including the source IP, the requested domain, and the identity of the authenticated user initiating the request. Cloudflare also offers a DLP service which has the ability to detect and block requests based on the presence of sensitive content. The service has built in DLP profiles for common data types such as financial information, personally identifiable information (PII), and API keys.</p>
<p>There is even a profile for source code, so users can detect and block the transfer of C++ or Python files. Organizations can create customized DLP profiles and use regular expressions to define the patterns of data they are looking for. For data that is hard to define a pattern for, datasets can be used which match exact data values. These datasets allow for the bulk upload of any data to be matched, such as lists of customer account IDs or sensitive project names. These profiles and data sets can be incorporated into policies to prevent users from downloading large files containing confidential customer data.</p>
<p>To reduce the risk of false positives, internal users have the option to establish a match count on the profile. This means that a specific number of matches within the data are required before profile triggers. This approach prevents scenarios where a random string resembling PII or a credit card number would trigger the profile unnecessarily. By implementing a match count, the policy demands that multiple data elements align with the profile, significantly increasing its accuracy.</p>
<p>Organizations can further increase the accuracy of the DLP profile by enabling context analysis. This feature requires certain proximity keywords to exist within approximately 1000 characters of a match. For example, the string &quot;123-45-6789&quot; will only count as a detection if it is in proximity to keywords such as &quot;ssn&quot;. This contextual requirement bolsters the accuracy of the detection process.</p>
<p>The DLP service seamlessly integrates with both Cloudflare's SWG and API-driven CASB services. In the case of the API CASB, DLP profiles are selected for scanning each integration with each SaaS application. This customization allows tailored detection criteria based on the type of data you wish to secure within each application.</p>
<p>For the SWG service, DLP profiles can be included into any policy to detect the existence of sensitive data in any request passing through the gateway. The most common action associated with this detection is to block the request, providing a robust layer of security.</p>
<h3 id="access-groups">Access Groups</h3>
<p>Access Groups are a powerful tool in the ZTNA service for aggregating users or devices into a unified entity that can be referenced within a policy. Within Cloudflare, multiple pieces of information can be combined into a single Access Group, efficiently reusing data across multiple policies while maintaining it in one centralized location.</p>
<p>Consider an Access Group designed to manage access to critical server infrastructure. The same Access Group can be used in a device agent policy that prevents administrators from disabling their connection to Cloudflare. This approach streamlines policy management and ensures consistency across various policy implementations.</p>
<p>Below is a diagram featuring an Access Group named &quot;Secure Administrators,&quot; which uses a range of attributes to define the characteristics of secure administrators. The diagram shows the addition of two other Access Groups within &quot;Secure Administrators&quot;. The groups include devices running on either the latest Windows or macOS, along with the requirement that the device must have either File Vault or Bitlocker enabled.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-24.svg" alt="An example of using Access Groups can be for grouping up many device, network or user attributes into a single policy that can be reused across applications." /></p>
<p>Consistent with Cloudflare's overarching flexibility, Access Groups can be created, updated, and applied to policies through Cloudflare API or using Terraform. This allows a seamless integration with existing IT systems and processes, ensuring a cohesive approach to access management.</p>
<p>Now that we have a solid understanding of all the components available, let's zoom in and take a look at some common use cases and how they are configured. Keep in mind that Cloudflare's policy engines are incredibly powerful and flexible, so these examples are just a glimpse into the capabilities of Cloudflare's SASE platform.</p>
<h3 id="example-use-cases">Example use cases</h3>
<h4 id="secure-access-to-self-hosted-apps-and-services">Secure access to self hosted apps and services</h4>
<p>One common driver for moving to a SASE architecture is replacing existing VPN connectivity with a more flexible and secure solution. Cloudflare One SASE architecture enables high performance and secure access to self hosted applications from anywhere in the world. However, the next step entails defining the policies that control access to resources.</p>
<p>In this example, consider two services: a database administration application (<a href="https://www.pgadmin.org/">pgadmin</a> for example) and an SSH daemon running on the database server. The diagram below illustrates the flow of traffic and highlights the ZTNA service. It's important to note that all other services still retain the ability to inspect the request. For instance, the contractor using their personal cell phone in Germany should only have access to the db admin tool, while the employee on a managed device can access both the db admin tool and SSH into the database server.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-25.svg" alt="An employee working on a managed device at home can access both the db admin tool as well as the SSH service. However a contractor in Germany only has access to the db admin tool." /></p>
<p>The policies that enable access rely on two Access Groups.</p>
<ul>
<li>Contractors
<ul>
<li>Users who authenticate through Okta and are part of the Okta group labeled &quot;Contractors&quot;</li>
<li>Authentication requires the use of a hardware token</li>
</ul>
</li>
<li>Database and IT administrators
<ul>
<li>Users who authenticate through Okta and are in the Okta groups &quot;IT administrators&quot; or &quot;Database administrators&quot;</li>
<li>Authentication requires the use of a hardware token</li>
<li>Users should be on a device with a serial number in the &quot;Managed Devices&quot; list</li>
</ul>
</li>
</ul>
<p>Both of these groups are then used in two different access policies.</p>
<ul>
<li>Database administration tool access
<ul>
<li>Database and IT admins are allowed access</li>
<li>Members of the &quot;Contractor&quot; access group are allowed access, but each authenticated session requires the user to complete a justification request</li>
<li>The admin tool is rendered in an isolated browser on Cloudflare's Edge network and file downloads are disabled</li>
</ul>
</li>
<li>Database server SSH access
<ul>
<li>&quot;Database and IT administrators&quot; group is allowed access</li>
<li>Their device must pass a Crowdstrike risk score of at least 80</li>
<li>Access must come from a device that is running our device agent and is connected to Cloudflare</li>
</ul>
</li>
</ul>
<p>These policies show that contractors are only allowed access to the database administration tool and do not have SSH access to the server. IT and database administrators can access the SSH service only when their devices are securely connected to Cloudflare via the device agent. Every element of the access groups and policies is evaluated for every login, so an IT administrator using a compromised laptop or a contractor unable to authenticate with a hardware token will be denied access.</p>
<p>Both user groups will connect to Cloudflare through the closest and fastest access point of Cloudflare's globally distributed network, resulting in a high quality experience for all users no matter where they are.</p>
<h4 id="threat-defense-for-distributed-offices-and-remote-workers">Threat defense for distributed offices and remote workers</h4>
<p>Another reason for using a SASE solution is to apply company security policies consistently across all users (whether they are employees or contractors) in the organization, regardless of where they work. The Cloudflare One SASE architecture shows that all user traffic, whether routed directly on the device or through the connected network, will go through Cloudflare. Cloudflare's SWG then handles inspection of this traffic. Depending on the connection method, policies can be applied either to the HTTP or DNS request. For example:</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-26.svg" alt="Blocking high risk websites can be done by selecting a few options in the SWG policy" /></p>
<p>This can then be applied to secure and protect all users in one policy. Cloudflare can write another policy allowing access to social media websites while isolating all sessions in a remote browser hosted on Cloudflare's network.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-27.svg" alt="Isolating all social media websites can be done by identifying the application or website name and selecting what actions the user can take, such as stopping them from copy and pasting or printing." /></p>
<p>With this setup, every request to a social media website ensures the following security measures:</p>
<ul>
<li>Any content on the social media website that contains harmful code is prevented from executing on the local device</li>
<li>External users are restricted from downloading content from the site that could potentially be infected with malware or spyware</li>
</ul>
<h4 id="data-protection-for-regulatory-compliance">Data protection for regulatory compliance</h4>
<p>Because Cloudflare One has visibility over every network request, Cloudflare can create policies that apply to the data in the request. This means that the DLP services can be used to detect the download of content from an application and block it for specific user demographics. Let's look at the following policy.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-28.svg" alt="Our DLP policies allow for the inspection of content in a request and blocking it." /></p>
<p>This policy would prevent contractors from downloading a file containing customer accounts information. Furthermore, Cloudflare can configure an additional policy to block the same download if the user's device does not meet specific security posture requirements. This ensures the consistent enforcement of a common rule: no sensitive customer data can be downloaded onto a device that does not meet the required security standards.</p>
<p>DLP policies can also be applied in the other direction, ensuring that company sensitive documents are not uploaded to non approved cloud storage or social media.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-29.svg" alt="A DLP policy can also examine if a HTTP PUT, i.e. a file upload, is taking place to a non approved application where the request contains sensitive data." /></p>
<h3 id="visibility-across-the-deployment">Visibility across the deployment</h3>
<p>At this point in the SASE journey, users have re-architected the IT network and security infrastructure to fully leverage all the capabilities of the Cloudflare One SASE platform. A critical element in long term deployment involves establishing complete visibility into the organization and the ability to diagnose and quickly resolve issues.</p>
<p>For quick analysis, Cloudflare provides built-in dashboards and analytics that offers a daily overview of the deployment's operational status. As traffic flows through Cloudflare, the dashboard will alert internal users to the most frequently used SaaS applications, enabling quick actions if any unauthorized applications are accessed by external users. Moreover, all logging information from all Cloudflare One services is accessible and searchable from the administrator's dashboard. This makes it efficient to filter for specific blocked requests, with each log containing useful information such as the user's identity, device information, and the specific rule that triggered the block. This can be very handy in the early stages of deployment where rules can often need tweaking.</p>
<p>However, many organizations rely on existing dedicated tools to manage long term visibility over the performance of their infrastructure. To support this, Cloudflare allows the export of all logging information into such tools. Every aspect of Cloudflare One is logged and can be exported. Cloudflare offers built in integrations for continuous transmission of small data batches to a variety of platforms, including AWS, Google Cloud Storage, SumoLogic, Azure, Splunk, Datadog, and any S3 compatible service. This flexibility allows organizations to selectively choose which fields to control the type and volume of data to incorporate into existing tools.</p>
<p>On top of logs which are related to traffic and policies, Cloudflare also audits management activity. All administrative actions and changes to Cloudflare Tunnels are logged. This allows for change management auditing and, like all other logs, can be exported into other tools as part of a wider change management monitoring solution.</p>
<h4 id="digital-experience-monitoring">Digital Experience Monitoring</h4>
<p>Cloudflare has <a href="https://radar.cloudflare.com/">deep insight</a> into the performance of the Internet and connected networks and devices. This knowledge empowers IT administrators with visibility into minute-by-minute experiences of their end-users, enabling swift resolution of issues that impact productivity.</p>
<p>The Digital Experience Monitoring (DEM) service enables IT to run constant tests against user devices to determine the quality of the connection to company resources. The results of these tests are available on the Cloudflare One dashboard, enabling IT administrators to review and identify root causes when a specific user encounters difficulties accessing an application. These issues could stem from the user's local ISP or a specific underperforming SaaS service provider. This data is invaluable in helping administrators in diagnosing and addressing poor user experiences, leading to faster issue resolution.</p>
<p>The dashboard shows a comprehensive summary of the entire device fleet, displaying real-time and historical connectivity metrics for all organization devices. IT admins can then drill down into specific devices for further analysis.</p>
<h2 id="summary">Summary</h2>
<p>Having acquired a comprehensive understanding of Cloudflare's SASE platform, you are now well-equipped to integrate it with existing infrastructure. This system efficiently secures access to applications for both employees and external users, starting from the initial request on the device and extending across every network to the application, regardless of its location. This powerful new model for securing networks, applications, devices, and users is built on the massive Cloudflare network and managed through an intuitive management interface.</p>
<p>It's worth noting that many of the capabilities described in this document can be used for free, without any time constraints, for up to 50 users. <a href="https://dash.cloudflare.com/sign-up">Sign up</a> for an account and head to the <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> section. While this document has provided an overview of the platform as a whole, for those interested in delving deeper into specific areas, we recommend exploring the following resources.</p>
<table>
<thead>
<tr>
<th>Topic</th>
<th>Content</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Tunnels</td>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Understanding Cloudflare Tunnel</a> - <a href="https://github.com/cloudflare/cloudflared">Open source repository for <code>cloudflared</code></a></td>
</tr>
<tr>
<td>WAN as a Service</td>
<td><a href="/cloudflare-wan/">Cloudflare WAN documentation</a> - <a href="/cloudflare-one/networks/connectors/cloudflare-wan/wan-transformation/">WAN transformation</a></td>
</tr>
<tr>
<td>Secure Web Gateway</td>
<td><a href="/cloudflare-one/traffic-policies/">How to build Gateway policies</a></td>
</tr>
<tr>
<td>Zero Trust Network Access</td>
<td><a href="/cloudflare-one/access-controls/policies/">How to build Access policies</a></td>
</tr>
<tr>
<td>Remote Browser Isolation</td>
<td><a href="/cloudflare-one/remote-browser-isolation/">Understanding browser isolation</a></td>
</tr>
<tr>
<td>API-Driven CASB</td>
<td><a href="/cloudflare-one/integrations/cloud-and-saas/">Scanning SaaS applications</a></td>
</tr>
<tr>
<td>Email security</td>
<td><a href="/email-security/">Understanding Cloudflare Email security</a></td>
</tr>
<tr>
<td>Replacing your VPN</td>
<td><a href="/learning-paths/replace-vpn/concepts/">Using Cloudflare to replace your VPN</a></td>
</tr>
</tbody>
</table>
<p>If you would like to discuss your SASE requirements in greater detail and connect with one of our architects, please visit <a href="https://www.cloudflare.com/cloudflare-one/">https://www.cloudflare.com/cloudflare-one/</a> and request a consultation.</p>
