<h1 id="changelog">Changelog</h1>

<h2 id="apo-caches-more-crawler-and-bot-traffic-again"><a href="/changelog/post/2026-08-27-accept-header-caching/">APO caches more crawler and bot traffic again</a></h2>
<p><em>2026-08-27</em></p>
<p>We fixed a regression where Automatic Platform Optimization (APO) stopped caching some HTML requests that did not send an explicit <code>Accept: text/html</code> header — commonly crawlers, bots, and uptime monitors. These requests were being served from your origin (<code>cf-cache-status: DYNAMIC</code>) instead of the cache.</p>
<p>APO now caches these requests again. No action is needed. If you added a Transform Rule to set <code>Accept: text/html</code> as a workaround, you can remove it.</p>
<p>For details on how APO decides what to cache, refer to <a href="/automatic-platform-optimization/about/">About APO</a>.</p>



