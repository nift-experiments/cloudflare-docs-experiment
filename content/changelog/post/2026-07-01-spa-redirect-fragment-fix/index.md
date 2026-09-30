<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 1, 2026</time><h2 id="post-title">Fix redirect URL fragment encoding for single-page applications</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Access now correctly preserves URL fragment characters (<code>/</code>, <code>?</code>, <code>=</code>, <code>&amp;</code>, <code>;</code>) when redirecting users back to an application after login. Previously, these characters were encoded with <code>encodeURIComponent</code>, which mangled fragment-based routes used by single-page applications (SPAs).</p>
<p>For example, an SPA URL like <code>https://app.example.com/#/dashboard?tab=settings&amp;view=advanced</code> would previously redirect to a broken URL after login. This is now handled correctly.</p>
<p>If your SPA users were experiencing broken navigation after authenticating through Access, this fix resolves the issue without any configuration changes.</p>
</div></article></div>
