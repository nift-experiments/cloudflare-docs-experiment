<p>With incoming zone transfers, you can keep your primary DNS provider and use Cloudflare as a secondary DNS provider.</p>
<p>When you make edits in your primary DNS provider, those DNS records will be transferred from your primary DNS provider to Cloudflare via zone transfer using <a href="https://datatracker.ietf.org/doc/html/rfc5936">AXFR</a> or <a href="https://datatracker.ietf.org/doc/html/rfc1995">IXFR</a>.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Cloudflare as Secondary DNS&#10;A((Zone Admin)) --DNS record &lt;br /&gt; management--&gt; B[Primary DNS &lt;br /&gt; provider]&#10;B --Zone transfer--&gt; C[Cloudflare &lt;br /&gt; DNS]&#10;B &amp; C &lt;--DNS lookups--&gt; D[Resolver] &lt;--DNS lookups--&gt; E((User))&#10;</code></pre>
<h2 id="how-to">How to</h2>
<ul>
<li><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/">Set up incoming zone transfers</a></li>
<li>Proxy traffic through Cloudflare with <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">Secondary DNS Override</a></li>
</ul>
<h2 id="availability">Availability</h2>
<p>Secondary DNS is only available to Enterprise customers. For more details on activation and pricing, contact your account team.</p>
