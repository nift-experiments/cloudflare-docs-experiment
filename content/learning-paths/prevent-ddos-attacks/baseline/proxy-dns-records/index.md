<p>The first - and often easiest - step of DDoS protection is making sure your DNS records are <a href="/dns/proxy-status/">proxied</a> through Cloudflare.</p>
<h2 id="how-it-works">How it works</h2>
<h3 id="without-cloudflare">Without Cloudflare</h3>
<p>Without Cloudflare, DNS lookups for your application's URL return the IP address of your <a href="https://www.cloudflare.com/learning/cdn/glossary/origin-server/">origin server</a>.</p>
<table>
<thead>
<tr>
<th>URL</th>
<th>Returned IP address</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com</code></td>
<td><code>192.0.2.1</code></td>
</tr>
</tbody>
</table>
<p>When using Cloudflare with <a href="/dns/proxy-status/">unproxied DNS records</a>, DNS lookups for unproxied domains or subdomains also return your origin's IP address.</p>
<p>Another way of thinking about this concept is that visitors directly connect with your origin server.</p>
<pre><code class="language-mermaid">        flowchart LR&#10;        accTitle: Connections without Cloudflare&#10;        A[Visitor] &lt;-- Connection --&gt; B[Origin server]&#10;</code></pre>
<h3 id="with-cloudflare">With Cloudflare</h3>
<p>With Cloudflare — meaning your domain or subdomain is using <a href="/dns/proxy-status/">proxied DNS records</a> — DNS lookups for your application's URL will resolve to <a href="https://www.cloudflare.com/ips/">Cloudflare anycast IPs</a> instead of their original DNS target.</p>
<table>
<thead>
<tr>
<th>URL</th>
<th>Returned IP address</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com</code></td>
<td><code>104.16.77.250</code></td>
</tr>
</tbody>
</table>
<p>All requests intended for proxied hostnames are directed to Cloudflare first and then forwarded to your origin server.</p>
<pre><code class="language-mermaid">        flowchart LR&#10;        accTitle: Connections with Cloudflare&#10;        A[Visitor] &lt;-- Connection --&gt; B[Cloudflare global network] &lt;-- Connection --&gt; C[Origin server]&#10;</code></pre>
<p>Cloudflare assigns specific anycast IPs to your domain dynamically and these IPs may change at any time. This is an expected part of the operation of our anycast network and does not affect the proxy behavior described above.</p>
<h2 id="how-it-helps">How it helps</h2>
<h3 id="ddos-protection">DDoS protection</h3>
<p>When your traffic is proxied through Cloudflare, Cloudflare can automatically stop <a href="/ddos-protection/about/">DDoS attacks</a> from ever reaching your application (and your origin server).</p>
<h3 id="caching">Caching</h3>
<p>Proxied traffic also benefits from the default optimizations of the Cloudflare <a href="/cache/">cache</a>. Cloudflare caches <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">certain types of resources</a> automatically, which both speeds up your application's performance and reduces the overall number of requests.</p>
<h3 id="hides-origin-ip-address">Hides origin IP address</h3>
<p>Proxying your DNS records in Cloudflare also hides the IP address of your origin server (because requests to your application resolve to Cloudflare anycast IP addresses instead).</p>
<p>This obscurity makes it harder for someone to connect directly to your origin, which - by extension - also makes it harder to target your origin with a DDoS attack.</p>
<h2 id="how-to-do-it">How to do it</h2>
<p>Before proxying your records, you should likely <a href="/fundamentals/concepts/cloudflare-ip-addresses/">allow Cloudflare IP addresses</a> at your origin to prevent requests from being blocked.</p>
<p>Then, <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">update your Cloudflare DNS records</a> so their <strong>Proxy status</strong> is <strong>Proxied</strong>.</p>
<p><img src="/assets/upstream/images/dns/proxy-status-screenshot.png" alt="Proxy status affects how Cloudflare treats traffic intended for specific DNS records" /></p>
