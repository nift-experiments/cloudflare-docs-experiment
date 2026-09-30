<div class="nb-description">
@markup("md", "content/.markup/bodies/1267.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p>Cloudflare WAN (formerly Magic WAN) connects your data centers, offices, and cloud resources through Cloudflare's global network. Instead of backhauling traffic through a central data center or maintaining dedicated MPLS circuits at every site, your traffic routes through the nearest Cloudflare data center where security policies apply inline.</p>
<p>Cloudflare WAN provides secure, performant <a href="https://www.cloudflare.com/learning/network-layer/what-is-routing/">routing</a> for your entire corporate network. <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> integrates with Cloudflare WAN, enabling you to enforce network firewall policies at Cloudflare's global network, across traffic from any entity within your network.</p>
<p>You connect your sites to Cloudflare through <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1268.md")
</div> — tunnels or direct connections from your network to Cloudflare. Cloudflare WAN supports any device that uses <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/1269.md")
</div> <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/1270.md")
</div> or <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/1271.md")
</div> tunnels. To make it easier to onboard your cloud resources, you can use [Multi-Cloud Networking](/cloudflare-wan/configuration/multi-cloud-networking/), which automates creating on-ramps from your cloud networks. Refer to [On-ramps](/cloudflare-wan/on-ramps/) for a full list of supported on-ramps.
<p>Refer to <a href="/cloudflare-wan/wan-transformation/">WAN transformation</a> to compare approaches and plan your migration, or go straight to <a href="/cloudflare-wan/get-started/">get started</a>.</p>
<h2 id="cloudflare-wan-and-cloudflare-one">Cloudflare WAN and Cloudflare One</h2>
<p>Cloudflare WAN is a standalone WAN-as-a-Service (WANaaS) product. It provides site-to-site connectivity over Cloudflare's global network, with packet-level security through <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a>. Cloudflare WAN supports IPsec tunnels, GRE tunnels, <a href="/network-interconnect/">Cloudflare Network Interconnect</a>, and the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> for connecting your sites.</p>
<p><a href="/cloudflare-one/">Cloudflare One</a> is the full SASE (Secure Access Service Edge) platform. It extends Cloudflare WAN with identity-aware security services:</p>
<ul>
<li><strong><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client (WARP)</a></strong> — deploys on user devices to route traffic through Cloudflare with identity context.</li>
<li><strong><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a></strong> — creates outbound-only connections from your infrastructure to Cloudflare, with no inbound ports required.</li>
<li><strong><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a></strong> — applies secure web gateway (SWG) policies to filter and inspect Internet-bound traffic.</li>
<li><strong><a href="/cloudflare-one/access-controls/">Cloudflare Access</a></strong> — enforces Zero Trust Network Access (ZTNA) policies based on user identity, device posture, and context.</li>
</ul>
<p>If your requirements are limited to site-to-site connectivity and network-layer security, Cloudflare WAN provides what you need. When you need user-level security policies, identity-based access controls, or secure Internet egress, you can add Cloudflare One capabilities to your existing deployment.</p>
<p>Cloudflare One builds on the same network infrastructure as Cloudflare WAN, so there is no migration required.</p>
<p>For more information about Cloudflare One, refer to the <a href="/cloudflare-one/">Cloudflare One documentation</a>.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/86f22d1f760b77cdc349f89b25b63c3e/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2Fe71b5fcd-6de8-4ec5-28b2-4667c34c3900%2Fpublic" title="SASE - Connect and secure from any network to anywhere" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1272.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1273.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1274.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1275.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1276.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1277.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1278.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1279.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1280.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1281.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1282.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1283.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/1285.md")
</div>
