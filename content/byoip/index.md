<div class="nb-description">
@markup("md", "content/.markup/bodies/1378.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p>When you use Cloudflare as a <a href="/fundamentals/concepts/how-cloudflare-works/">reverse proxy</a>, Cloudflare responds to DNS queries for proxied records with Cloudflare-owned IP addresses<sup><a href="#footnote-1">1</a></sup>. For some organizations, it is important to keep their website or application associated with IP addresses they already own rather than using Cloudflare's.</p>
<p>With Bring Your Own IP (BYOIP), Cloudflare announces your IP prefixes in all our locations. Use your IPs with <a href="/magic-transit/">Magic Transit</a>, <a href="/spectrum/">Spectrum</a>, <a href="/cache/">CDN services</a>, or Gateway <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a>.</p>
<p>Learn how to <a href="/byoip/get-started/">get started</a>.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1379.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1380.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/1383.md")
</div>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Without BYOIP, when your domain's records are `proxied`, Cloudflare responds with a Cloudflare-owned [anycast IP address](/fundamentals/concepts/cloudflare-ip-addresses/).</li></ol></section>
