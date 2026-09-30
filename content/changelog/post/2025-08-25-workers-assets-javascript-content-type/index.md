<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 25, 2025</time><h2 id="post-title">Content type returned in Workers Assets for Javascript files is now `text/javascript`</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>JavaScript asset responses have been updated to use the <code>text/javascript</code> Content-Type header instead of <code>application/javascript</code>. While both MIME types are widely supported by browsers, the HTML Living Standard explicitly recommends <code>text/javascript</code> as the preferred type going forward.</p>
<p>This change improves:</p>
<ul>
<li>Standards alignment: Ensures consistency with the HTML spec and modern web platform guidance.</li>
<li>Interoperability: Some developer tools, validators, and proxies expect text/javascript and may warn or behave inconsistently with application/javascript.</li>
<li>Future-proofing: By following the spec-preferred MIME type, we reduce the risk of deprecation warnings or unexpected behavior in evolving browser environments.</li>
<li>Consistency: Most frameworks, CDNs, and hosting providers now default to text/javascript, so this change matches common ecosystem practice.</li>
</ul>
<p>Because all major browsers accept both MIME types, this update is backwards compatible and should not cause breakage.</p>
<p>Users will see this change on the next deployment of their assets.</p>
</div></article></div>
