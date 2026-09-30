<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 21, 2026</time><h2 id="post-title">Improved SCIM 2.0 group synchronization</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Dashboard SCIM now supports replacing groups using HTTP <code>PUT</code>, as defined by <a href="https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.1">RFC 7644 section 3.5.1</a>. This allows identity providers to synchronize a group's full state, including its display name, external ID, and members, in a single request.</p>
<p><strong>What's New</strong></p>
<p><strong>Group replacement via <code>PUT</code></strong>: Full-state group synchronization improves compatibility with identity providers that use replacement semantics and helps keep Cloudflare groups aligned with their source identity provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17732.md")</aside>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/account/account-security/scim-setup/">SCIM provisioning overview</a></li>
</ul>
</div></article></div>
