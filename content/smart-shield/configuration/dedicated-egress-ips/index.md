<p>Enterprise customers can leverage dedicated egress<sup><a href="#footnote-1">1</a></sup> IPs for layer 7 <a href="/waf/">WAF</a> and <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/13857.md")
</div> services, as well as [Spectrum](/spectrum/). The egress IPs are reserved exclusively for your account so that you can increase your origin security by only allowing traffic from a small list of IP addresses.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13856.md")
</aside>
<p>Dedicated CDN Egress IPs was formerly known as Cloudflare Aegis (<a href="https://blog.cloudflare.com/cloudflare-aegis/">release blog post</a>).</p>
<h2 id="benefits">Benefits</h2>
<p>With Dedicated CDN Egress IPs, you can:</p>
<ul>
<li>Lock down your network firewall to only allow traffic from your dedicated IPs.</li>
<li>Use <a href="/smart-shield/configuration/dedicated-egress-ips/other-products/#access-and-cni">Cloudflare Access and CNI</a> to secure your applications without installing software or customizing code on your server.</li>
<li>Ensure only authorized <a href="/smart-shield/configuration/dedicated-egress-ips/other-products/#workers">Workers</a> can access your origin services.</li>
</ul>
<h2 id="scope">Scope</h2>
<p>You can assign Dedicated CDN Egress IPs to single or multiple Cloudflare zones, and across different Cloudflare accounts.</p>
<p>Dedicated CDN Egress IPs are included within <a href="/network-interconnect/">BGP advertisement over CNI</a>.</p>
<p>Each dedicated egress pool can consist of either IPs from a <a href="/byoip/">BYOIP prefix</a> or Cloudflare-leased IPs. A single dedicated egress pool cannot contain both BYOIPs and leased IPs. Also, a single BYOIP prefix can be used for either CDN ingress or CDN egress, but not both.</p>
<h2 id="resources">Resources</h2>
<ul class="directory-listing"><li><a href="/smart-shield/configuration/dedicated-egress-ips/how-it-works/">How it works</a></li><li><a href="/smart-shield/configuration/dedicated-egress-ips/setup/">Setup</a></li><li><a href="/smart-shield/configuration/dedicated-egress-ips/ips-utilization/">IPs utilization</a></li><li><a href="/smart-shield/configuration/dedicated-egress-ips/other-products/">Use with other Cloudflare products</a></li></ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">From Cloudflare to your origin. Refer to [how it works](/smart-shield/configuration/dedicated-egress-ips/how-it-works/egress-ips/) for details.</li></ol></section>
