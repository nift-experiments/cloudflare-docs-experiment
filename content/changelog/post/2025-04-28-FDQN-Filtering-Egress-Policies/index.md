<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 28, 2025</time><h2 id="post-title">FQDN Filtering For Gateway Egress Policies</h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Cloudflare One administrators can now control which egress IP is used based on a destination's fully qualified domain name (FDQN) within Gateway Egress policies.</p>
<ul>
<li>Host, Domain, Content Categories, and Application selectors are now available in the Gateway Egress policy builder in beta.</li>
<li>During the beta period, you can use these selectors with traffic on-ramped to Gateway with the WARP client, proxy endpoints (commonly deployed with PAC files), or Cloudflare Browser Isolation.
<ul>
<li>For WARP client support, additional configuration is required. For more information, refer to the <a href="/cloudflare-one/traffic-policies/egress-policies/#limitations">WARP client configuration documentation</a>.</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/gateway/Gateway-Egress-FQDN-Policy-preview.png" alt="Egress by FQDN and Hostname" /></p>
<p>This will help apply egress IPs to your users' traffic when an upstream application or network requires it, while the rest of their traffic can take the most performant egress path.</p>
</div></article></div>
