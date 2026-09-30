<p>Internet traffic is made up of people, services, and agents requesting online resources from wherever they are hosted. Your resources may be publicly available, like a website or application that anyone on the Internet can access. Or your resources may be privately available, like an internal app or network that only your employees and partners should be able to access.</p>
<p>Both public and private resources can be connected to the Cloudflare network to ensure only good actors can access what they are supposed to be able to access with high performance.</p>
<p>For example, you may not always want the direct traffic because it can come from malicious sources, like hackers, or in the form of <a href="https://www.cloudflare.com/learning/ddos/ddos-attack-tools/how-to-ddos/">DDoS attacks</a>. Additionally, depending on the location where the request originated, you want to ensure the traffic is <a href="/argo-smart-routing/">routed through the most efficient and fastest path</a>.</p>
<h2 id="cloudflare-s-network">Cloudflare's network</h2>
<p><a href="https://www.cloudflare.com/network/">Cloudflare's global network</a>, coupled with <a href="https://www.cloudflare.com/learning/dns/what-is-anycast-dns/">Anycast</a> IP addressing, ensures that requests are handled by a Cloudflare server that is as close to the source as possible.</p>
<p>If you want to protect your traffic and ensure it travels efficiently, you need to configure Cloudflare to be in front of whatever you are trying to protect, such as your application, service, or server. How you put your resources behind Cloudflare's network will depend on the type of traffic and how you want to control it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8924.md")
</aside>
<h2 id="on-ramp-and-off-ramp-traffic">On-ramp and off-ramp traffic</h2>
<p>Traffic that enters Cloudflare's network is referred to as &quot;on-ramping,&quot; and traffic that exits Cloudflare's network is referred to as &quot;off-ramping.&quot; You may also know this as ingress and egress or &quot;routing your traffic&quot; through a network.</p>
<h3 id="on-ramp-traffic-to-cloudflare">On-ramp traffic to Cloudflare</h3>
<p>When you on-ramp traffic to Cloudflare, this allows Cloudflare to act on, secure, and increase performance of that traffic.</p>
<p>One example of on-ramping traffic to Cloudflare is updating your public website to use Cloudflare as the primary authoritative <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-dns-provider">DNS provider</a> for your domain.</p>
<p>However, maybe you need to protect a private application that is not directly available on the Internet. In this scenario, you can:</p>
<ul>
<li>Connect your private application to Cloudflare using <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">secure tunnels</a>, and use a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">device agent</a> to connect as a user.</li>
<li>For users already connected to a private company network, connect the entire network to Cloudflare using secure tunnels, and any request from a user device will access the private application through those tunnels.</li>
</ul>
<p>With these options, any request from a user device can access internal private applications via the secure private tunnels.</p>
<p>Refer to the list below for products you can use to on-ramp traffic to Cloudflare.</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">Anycast routing</a> uses Anycast IP addressing to route traffic to the nearest Cloudflare data center. Selective routing allows an Anycast network to be resilient in the face of high traffic volume, network congestion, and<a href="https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/"> DDoS attacks</a>.</li>
<li><a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-dns-provider">DNS-based</a> traffic resolves domains onboarded to <a href="/fundamentals/concepts/how-cloudflare-works/">Cloudflare's CDN</a>. Cloudflare's DNS directs traffic to Cloudflare's global network of servers instead of a website's origin server.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> connects your resources to Cloudflare without a publicly routable IP address so that your origins can serve traffic through Cloudflare without being vulnerable to attacks that bypass Cloudflare.</li>
<li><a href="/magic-transit/about/">Magic Transit</a> offers DDoS protection, traffic acceleration, and more for on-premise, cloud-hosted, and hybrid networks by accepting IP packets destined for your network, processing them, and outputting the packets to your origin infrastructure.</li>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> securely and privately sends traffic from corporate devices to Cloudflare's global network while also applying advanced Zero Trust policies that check for a device's health before it connects to corporate applications.</li>
</ul>
<h3 id="off-ramp-traffic-from-cloudflare">Off-ramp traffic from Cloudflare</h3>
<p>If you need to ensure traffic leaves Cloudflare's network in a specific way, you can manage how traffic is off-ramped.</p>
<p>For example, if you need to adhere to <a href="/data-localization/regional-services/">regional laws</a> that dictate user traffic and require data never leaves your country, you can configure off-ramp and on-ramp traffic on servers in the same geographical area.</p>
<p>Or maybe you want to force traffic to off-ramp in a certain country to maintain your user's experience. For example, if you have employees in India who travel frequently, you can configure the off-ramp traffic to always appear to come from India so websites they visit maintain their language and preferences.</p>
<p>You can also utilize <a href="/cache/">caching</a> to help with performance. Instead of off-ramp traffic going to a server across the globe, Cloudflare can cache that content locally for the user to reduce the overall time for their request.</p>
<p>Refer to the list below for products you can use to off-ramp traffic from Cloudflare.</p>
<ul>
<li><a href="/argo-smart-routing/">Argo Smart Routing</a> detects real-time network issues and routes your web traffic across the most efficient network path, avoiding congestion.</li>
<li><a href="/cache/">Cache</a> works with cached content to avoid off-ramping to origin servers and instead serving directly from Cloudflare's global network.</li>
<li><a href="/data-localization/regional-services/">Regional services</a> lets you choose which subset of data centers decrypt and service HTTPS traffic, which can help customers who have to meet regional compliance or have preferences for maintaining regional control over their data.</li>
</ul>
