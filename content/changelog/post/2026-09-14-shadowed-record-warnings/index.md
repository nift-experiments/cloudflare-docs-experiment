<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 14, 2026</time><h2 id="post-title">Shadowed record warnings are now available for all zones</h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Cloudflare now displays warnings for shadowed records in all zones. A record is shadowed when a subdomain delegation gives authority for its name, or a name below it, to another set of nameservers. The record remains present, but your zone is not authoritative for it thus Cloudflare will not respond with it to matching DNS queries. These warnings help you find records that may no longer resolve from the expected zone.</p>
<p>Shadow metadata is also available in DNS records API responses when you set <code>include_shadow_metadata=true</code>. The metadata identifies the delegating <code>NS</code> records and, when applicable, whether an <code>A</code> or <code>AAAA</code> record is glue. For more information, refer to <a href="/dns/manage-dns-records/reference/shadowed-records/">Shadowed records</a>.</p>
</div></article></div>
