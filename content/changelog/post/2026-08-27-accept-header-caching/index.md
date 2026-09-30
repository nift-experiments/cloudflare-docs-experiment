<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 27, 2026</time><h2 id="post-title">APO caches more crawler and bot traffic again</h2>
<div class="changelog-badges"><span>automatic-platform-optimization</span></div><div class="changelog-body"><p>We fixed a regression where Automatic Platform Optimization (APO) stopped caching some HTML requests that did not send an explicit <code>Accept: text/html</code> header — commonly crawlers, bots, and uptime monitors. These requests were being served from your origin (<code>cf-cache-status: DYNAMIC</code>) instead of the cache.</p>
<p>APO now caches these requests again. No action is needed. If you added a Transform Rule to set <code>Accept: text/html</code> as a workaround, you can remove it.</p>
<p>For details on how APO decides what to cache, refer to <a href="/automatic-platform-optimization/about/">About APO</a>.</p>
</div></article></div>
