<p>When you use Cloudflare <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">as a reverse proxy</a>, <a href="https://www.cloudflare.com/network/">Cloudflare's global network</a> sits between client requests and your origin servers.</p>
<pre><code class="language-mermaid">flowchart LR&#10;        accTitle: Cloudflare as a reverse proxy&#10;        accDescr: Diagram showing Cloudflare&#x27;s network between clients and the origin server.&#10;        A[Client] &lt;--&gt; B((Cloudflare))&lt;--&gt; C[(Origin server)]&#10;</code></pre>
<p>Zooming into what happens as a request routes through Cloudflare, you can consider two parts of the process: ingress and egress.</p>
<pre><code class="language-mermaid">flowchart LR&#10;        accTitle: Cloudflare as a reverse proxy&#10;        accDescr: Diagram showing Cloudflare&#x27;s network between clients and the origin server.&#10;        A[Client] --ingress--&gt; B((Cloudflare))--egress--&gt; C[(Origin server)]&#10;</code></pre>
<p>Ingress refers to the data center where the client request lands on, based on Internet routing. From there on, the request will be processed according to your Cloudflare configurations and, if needed, a connection to the origin will be initiated via an egress data center.</p>
<p>Traditionally, Cloudflare maintains a very large pool of egress IPs that are used by all Cloudflare customers and are <a href="https://www.cloudflare.com/ips/">publicly documented</a>. With Dedicated CDN Egress IPs, Cloudflare connects to your origin using IPs that are reserved for you.</p>
<h2 id="byoip-or-cloudflare-leased">BYOIP or Cloudflare-leased</h2>
<p>Each dedicated CDN egress IP pool can consist of either IPs from a <a href="/byoip/">BYOIP prefix</a> or Cloudflare-leased IPs. A single dedicated CDN egress IP pool cannot contain both BYOIPs and leased IPs.</p>
<p>You can find your leased dedicated IPs for CDN egress on the dashboard under <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Address space</strong> &gt; <strong>Leased IPs</strong></a>.</p>
<p>If you are using BYOIP, refer to <strong>BYOIP prefixes</strong> instead.</p>
<h2 id="ips-allocation">IPs allocation</h2>
<p>Dedicated CDN Egress IPs support both IPv4 and IPv6 addresses.</p>
<p>IPv6 address ranges are deployed globally, meaning your dedicated IPv6 addresses can be used for connections from Cloudflare to your origin servers across all Cloudflare data centers.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="china-exception">China exception</h3>
@markup("md", "content/.markup/bodies/13861.md")
</aside>
<p>For IPv4 addresses, you should work with your account team to choose the locations where each IP should be deployed. Ideally, your dedicated IPv4 addresses should be placed near your origin servers and adjusted to the amount of traffic expected for each region.</p>
<p>Refer to <a href="/smart-shield/configuration/dedicated-egress-ips/how-it-works/connection-forwarding/">connection forwarding</a> to understand how requests are processed when reaching different Cloudflare data centers.</p>
<h3 id="connections-to-your-origin">Connections to your origin</h3>
<p>Each Dedicated CDN Egress IP can support 40,000 concurrent connections per origin IP port. For example, if you have one dedicated IP and two origins (A and B), this single IP can support 40,000 concurrent connections to origin A, while simultaneously supporting 40,000 concurrent connections to origin B.</p>
<p>Dedicated CDN Egress IPs also benefit from <a href="/smart-shield/concepts/connection-reuse/">connection reuse and coalescing</a>.</p>
<p>GraphQL Analytics API allows you to get visibility over <a href="/smart-shield/configuration/dedicated-egress-ips/ips-utilization/">IPs utilization</a>.</p>
<h3 id="regional-services">Regional Services</h3>
<p>If you are using <a href="/data-localization/regional-services/">Regional Services</a>, you should take this into consideration when allocating dedicated IPv4 addresses. Traffic will egress from the specified locations as long as you have Dedicated CDN Egress IPs provisioned in those locations.</p>
