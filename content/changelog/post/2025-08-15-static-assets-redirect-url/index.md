<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 15, 2025</time><h2 id="post-title">Workers Static Assets: Corrected handling of double slashes in redirect rule paths</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/static-assets/">Static Assets</a>: Fixed a bug in how <a href="https://developers.cloudflare.com/workers/static-assets/redirects/">redirect rules</a> defined in your Worker's <code>_redirects</code> file are processed.</p>
<p>If you're serving Static Assets with a <code>_redirects</code> file containing a rule like <code>/ja/* /:splat</code>, paths with double slashes were previously misinterpreted as external URLs. For example, visiting <code>/ja//example.com</code> would incorrectly redirect to <code>https://example.com</code> instead of <code>/example.com</code> on your domain. This has been fixed and double slashes now correctly resolve as local paths. Note: <a href="/pages/">Cloudflare Pages</a> was not affected by this issue.</p>
</div></article></div>
