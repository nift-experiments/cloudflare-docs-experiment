<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 2, 2026</time><h2 id="post-title">Hostname routing for Cloudflare Mesh</h2>
<div class="changelog-badges"><span>mesh</span><span>cloudflare-one</span></div><div class="changelog-body"><p>You can now add <a href="/mesh/features/routes/#hostname-routes">hostname routes</a> to a Cloudflare Mesh node, in addition to CIDR routes.</p>
<div class="nb-interactive-component" data-cf-component="MeshHostnameRoutingDiagram"></div>
<p>Instead of managing IP ranges, you can attract traffic for a hostname to a Mesh node:</p>
<ul>
<li><strong>Private hostname</strong> (for example, <code>wiki.internal.local</code>) — reach an internal application by name, which is useful when it has an unknown or ephemeral IP. On Mesh you do not need to run a DNS server; a local hosts-file entry on the node is enough, or you can use a Gateway resolver policy for split DNS.</li>
<li><strong>Public hostname</strong> (for example, <code>www.example.com</code>) — route that hostname's traffic through the node and egress via the node's public IP.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For setup steps, prerequisites, and DNS options, refer to <a href="/mesh/features/routes/#hostname-routes">Hostname routes</a>.</p>
</div></article></div>
