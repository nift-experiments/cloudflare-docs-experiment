<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 24, 2026</time><h2 id="post-title">OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies</h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Cloudflare Gateway now supports <a href="/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims">OIDC Claims</a> as a selector in Firewall, Resolver, and Egress policies. Administrators can use custom OIDC claims from their identity provider to build fine-grained, identity-based traffic policies across all Gateway policy types.</p>
<p>With this update, you can:</p>
<ul>
<li>Filter traffic in <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> firewall policies based on OIDC claim values.</li>
<li>Apply custom <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> to route DNS queries to specific resolvers depending on a user's OIDC claims.</li>
<li>Control <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policies</a> to assign dedicated egress IPs based on OIDC claim attributes.</li>
</ul>
<p>For example, you can create a policy that routes traffic differently for users with <code>department=engineering</code> in their OIDC claims, or restrict access to certain destinations based on a user's role claim.</p>
<p>To get started, configure <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> on your identity provider and use the <strong>OIDC Claims</strong> selector in the Gateway policy builder.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/identity-selectors/">Identity-based policies</a>.</p>
</div></article></div>
