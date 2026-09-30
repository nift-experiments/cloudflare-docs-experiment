<p>A Secure Web Gateway (SWG) is a security service that sits between an organization's users and the Internet. It inspects outbound traffic to enforce security policies, block threats, and prevent data loss. Core SWG capabilities include:</p>
<ul>
<li><strong>URL and domain filtering</strong> – Controls which websites users can access.</li>
<li><strong>Anti-malware scanning</strong> – Inspects files in transit for malicious code.</li>
<li><strong>Application control</strong> – Manages which applications users can reach and what actions they can perform.</li>
<li><strong>Data Loss Prevention (DLP)</strong> – Detects and blocks sensitive data before it leaves the network.fprotecting</li>
<li><strong>Traffic inspection</strong> – Decrypts and examines encrypted (HTTPS) traffic for hidden threats.</li>
</ul>
<h2 id="the-need-for-an-swg">The need for an SWG</h2>
<p>Traditional network security relied on hardware firewalls at the perimeter of a corporate network. That model assumed users, applications, and data all lived inside the same network boundary. Modern organizations face a different reality:</p>
<ul>
<li><strong>Distributed workforce</strong> – Employees connect from home networks, public Wi-Fi, and mobile devices, outside any corporate perimeter.</li>
<li><strong>Cloud and SaaS adoption</strong> – Business-critical applications and data have moved to cloud platforms like Microsoft 365, Google Workspace, and Salesforce.</li>
<li><strong>Expanding threat surface</strong> – Phishing, ransomware, command-and-control botnets, and data exfiltration attempts target users regardless of their location.</li>
</ul>
<p>Without an SWG, organizations lose visibility into what websites and applications users access, what threats reach user devices, and what data leaves the organization. An SWG restores that visibility and control by inspecting traffic in the cloud, close to users, rather than forcing all traffic through a central data center.</p>
<p>Cloudflare Gateway is Cloudflare's SWG, built into the <a href="https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/">Cloudflare One</a> SASE platform. It inspects and filters traffic at the DNS, network (Layer 4), and HTTP (Layer 7) layers.</p>
<p>For more information on how SWGs work, refer to the <a href="https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/">Cloudflare Learning Center</a>.</p>
<h2 id="traffic-policy-types">Traffic policy types</h2>
<p>Every organization needs a way to control what users can reach on the Internet — blocking malware sites, restricting risky applications, and deciding how traffic exits the corporate network. Think of traffic policies as a set of security checkpoints, each inspecting a different layer of your traffic before it is allowed through.</p>
<h3 id="how-gateway-relates-to-traditional-firewalls">How Gateway relates to traditional firewalls</h3>
<p>If you are familiar with traditional network security, Gateway's policy layers map to familiar firewall functions:</p>
<ul>
<li><strong>DNS policies</strong> correspond to DNS-layer filtering (blocking domains before connections are established).</li>
<li><strong>Network policies</strong> correspond to a Layer 4 stateful firewall, sometimes called Firewall-as-a-Service (FWaaS), filtering by IP address, port, and protocol.</li>
<li><strong>HTTP policies</strong> correspond to a Layer 7 application firewall (forward proxy with TLS decryption and deep packet inspection).</li>
</ul>
<p>Unlike hardware firewalls that sit at a single network perimeter, Gateway enforces these policies across Cloudflare's global network, protecting traffic regardless of where users connect.</p>
<p>Gateway supports several policy types because network traffic can be inspected at different layers — from raw packets up to full HTTP requests. Each policy type gives you control at a specific layer:</p>
<details class="nb-details"><summary>Packet filtering</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4403.md")
</div></details>
<details class="nb-details"><summary>DNS policies</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4404.md")
</div></details>
<details class="nb-details"><summary>Network policies</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4405.md")
</div></details>
<details class="nb-details"><summary>HTTP policies</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4406.md")
</div></details>
<details class="nb-details"><summary>Egress policies</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4407.md")
</div></details>
<details class="nb-details"><summary>Resolver policies</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4408.md")
</div></details>
<h3 id="identity-and-device-context">Identity and device context</h3>
<p>Gateway policies can go beyond network attributes (domains, IPs, ports) and incorporate user identity and device health into every decision.</p>
<p>When users connect through the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, Gateway can evaluate:</p>
<ul>
<li><strong>User identity</strong> – Email address, group membership, and authentication method from your <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> (for example, Okta, Microsoft Entra ID, or Google Workspace).</li>
<li><strong>Device posture</strong> – Signals such as operating system version, disk encryption status, firewall state, and whether the device serial number matches a managed device list. For the full list of available checks, refer to <a href="/cloudflare-one/reusable-components/posture-checks/">Device posture</a>.</li>
</ul>
<p>These signals can be combined with traffic selectors to create context-aware policies. For example, you can create an HTTP policy that allows access to a sensitive SaaS application only when the user belongs to a specific group <strong>and</strong> the device has disk encryption turned on.</p>
<p>For details on building policies with identity selectors, refer to <a href="/cloudflare-one/traffic-policies/identity-selectors/">Identity-based policies</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4402.md")
</aside>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/48a3b49b7cdfaef0b3044d1530c82c19/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2Fa6fd20a9-4cdf-4640-81b1-cada4c4f3f00%2Fpublic" title="SASE - Protect your users from Internet risks" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="set-up-cloudflare-gateway-traffic-policies">Set up Cloudflare Gateway traffic policies</h2>
<p>Before you create Cloudflare Gateway traffic policies, you need connect the devices or networks you want to protect and confirm that Cloudflare Gateway can inspect their traffic. For each traffic policy type, follow this workflow:</p>
<ol>
<li>Connect the devices or networks you want to protect.</li>
<li>Verify that Gateway is receiving traffic from your devices.</li>
<li>Set up recommended security policies — for example, block all <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security threat categories</a> with a DNS policy.</li>
<li>Add policies specific to your organization's needs.</li>
</ol>
<p>For example, if your goal is to prevent employees from accessing known malware domains, you would start by enrolling devices with the Cloudflare One Client (step 1), confirm DNS queries appear in your Gateway logs (step 2), then create a DNS policy that blocks all security-risk categories (step 3).</p>
<p>For step-by-step setup guides, refer to <a href="/cloudflare-one/traffic-policies/get-started/dns/">DNS</a>, <a href="/cloudflare-one/traffic-policies/get-started/network/">Network</a>, and <a href="/cloudflare-one/traffic-policies/get-started/http/">HTTP</a> policies.</p>
<h3 id="how-to-choose-a-cloudflare-gateway-policy-type">How to choose a Cloudflare Gateway policy type</h3>
<p>The following table maps common traffic-filtering goals to the best Cloudflare Gateway policy type:</p>
<table>
<thead>
<tr>
<th>Filtering goal</th>
<th>Policy type</th>
<th>Why</th>
</tr>
</thead>
<tbody>
<tr>
<td>Block websites by URL</td>
<td>HTTP</td>
<td>Inspects the full URL path, not just the domain</td>
</tr>
<tr>
<td>Block domains (all pages)</td>
<td>DNS</td>
<td>Prevents the domain from resolving</td>
</tr>
<tr>
<td>Block non-HTTP traffic (SSH, RDP)</td>
<td>Network</td>
<td>Inspects TCP/UDP packets on any port</td>
</tr>
<tr>
<td>Block malware and threats</td>
<td>DNS <em>and</em> HTTP</td>
<td>DNS blocks known-bad domains. HTTP catches threats in allowed traffic.</td>
</tr>
<tr>
<td>Assign static egress IPs</td>
<td>Egress</td>
<td>Lets third-party services identify your organization</td>
</tr>
<tr>
<td>Drop traffic before other policies run</td>
<td>Packet filtering</td>
<td>Blocks by packet attributes without user context</td>
</tr>
<tr>
<td>Route DNS to custom nameservers</td>
<td>Resolver</td>
<td>Overrides the default Cloudflare resolver</td>
</tr>
</tbody>
</table>
<p>After you choose a Cloudflare Gateway policy type, continue with the matching setup guide to create the policy that fits your traffic-filtering goal.</p>
<h3 id="choose-a-connection-method">Choose a connection method</h3>
<p>The connection method (on-ramp) you use determines which policy types Gateway can enforce. The following table summarizes each method:</p>
<table>
<thead>
<tr>
<th>Connection method</th>
<th>DNS policies</th>
<th>Network policies</th>
<th>HTTP policies</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> (WARP)</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Roaming users on managed devices (laptops, phones)</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS resolver</a> configuration</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>Unmanaged devices, entire networks, or initial rollout</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">Proxy endpoint</a> (PAC file)</td>
<td>No</td>
<td>No</td>
<td>Yes (browser only)</td>
<td>Browser-level HTTP filtering without a device agent</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/">Network tunnel</a> (IPsec/GRE via Magic WAN)</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Branch offices, data centers, and site-level connectivity</td>
</tr>
</tbody>
</table>
<ul>
<li>The <strong>Cloudflare One Client</strong> provides the broadest coverage and is the recommended method for per-device deployments.</li>
<li><strong>DNS resolver</strong> configuration is the easiest to deploy (change a DNS setting on your router or device) and provides immediate protection, but it only enforces DNS policies.</li>
<li><strong>Proxy endpoints</strong> enable HTTP inspection through browser proxy configuration without installing an agent, but they are limited to browser traffic.</li>
<li><strong>Network tunnels</strong> route all site traffic through Gateway and are best for protecting entire office locations or data centers.</li>
</ul>
<p>You can combine multiple on-ramps. For example, use the Cloudflare One Client for remote employees and network tunnels for branch offices.</p>
<h2 id="how-gateway-processes-traffic">How Gateway processes traffic</h2>
<p>When a user makes a request, Gateway inspects it at multiple layers before allowing the connection through. The following diagram shows the end-to-end flow:</p>
<pre><code class="language-mermaid">flowchart LR&#10;    accTitle: Gateway traffic flow&#10;    accDescr: Diagram showing how traffic flows from user device through an on-ramp to Cloudflare Gateway for policy evaluation, then to the destination.&#10;&#10;    A[&quot;User device&quot;] --&gt; B[&quot;On-ramp&quot;]&#10;    B --&gt; C[&quot;Cloudflare edge&lt;br/&gt;(nearest location)&quot;]&#10;    C --&gt; D[&quot;Policy evaluation&quot;]&#10;    D --&gt; E[&quot;Destination&lt;br/&gt;server&quot;]&#10;    E --&gt; D&#10;    D --&gt; C&#10;    C --&gt; B&#10;    B --&gt; A&#10;</code></pre>
<ol>
<li>The user's device sends a request (DNS query, TCP connection, or HTTP request).</li>
<li>The request reaches Cloudflare through an <strong>on-ramp</strong> — the Cloudflare One Client, a DNS resolver configuration, a proxy endpoint, or a network tunnel.</li>
<li>Cloudflare processes the request at the <strong>nearest edge location</strong>, not a centralized data center. This keeps latency low regardless of where the user connects from.</li>
<li>Gateway evaluates the request against your configured policies in <a href="/cloudflare-one/traffic-policies/order-of-enforcement/">order of enforcement</a>: DNS policies first, then network policies, then HTTP policies.</li>
<li>If policies allow the request, Gateway proxies it to the destination server and inspects the response on the return path.</li>
</ol>
<p>For details on how Gateway proxies traffic and establishes connections, refer to <a href="/cloudflare-one/traffic-policies/proxy/">Proxy</a>.</p>
<h2 id="troubleshoot-cloudflare-gateway-policies">Troubleshoot Cloudflare Gateway policies</h2>
<p>For help resolving common issues with Cloudflare Gateway policies, refer to <a href="/cloudflare-one/traffic-policies/troubleshooting/">Troubleshooting</a>.</p>
