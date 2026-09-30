<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 2, 2026</time><h2 id="post-title">Configure Origin Range Requests with the Rulesets API</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>The Rulesets API now supports Origin Range Requests in Cache Rules. This setting lets Cloudflare fetch large files from your origin in cache-aligned byte ranges. Cloudflare may expand a client range and issue several single-range origin requests.</p>
<p>Set <code>origin_range_requests.mode</code> to <code>on</code>, <code>off</code>, or <code>default</code> for any traffic matched by a Cache Rule.</p>
<p>To override Cloudflare's default Origin Range Requests behavior, set the mode to <code>off</code>. The following rule turns off generated origin range requests for all traffic without changing cache eligibility:</p>
<pre><code class="language-json">{&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;action&quot;: &quot;set_cache_settings&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;origin_range_requests&quot;: {&#10;      &quot;mode&quot;: &quot;off&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Origin Range Requests do not make otherwise ineligible content cacheable. If your origin ignores <code>Range</code> and returns a complete <code>200 OK</code>, Cloudflare can use the response but must download the complete file. Origins should honor <code>Accept-Encoding: identity</code> and return consistent, unencoded partial responses.</p>
<p>For configuration details and mode behavior, refer to <a href="/cache/how-to/cache-rules/settings/#origin-range-requests">Origin Range Requests in Cache Rules</a>. For client responses and the complete origin contract, refer to <a href="/cache/reference/range-requests/">Range request behavior</a>.</p>
</div></article></div>
