<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 11, 2024</time><h2 id="post-title">Bypass caching for subrequests made from Cloudflare Workers, with Request.cache</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now use the <a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface to bypass <a href="/workers/reference/how-the-cache-works/">Cloudflare's cache</a> when making subrequests from <a href="/workers">Cloudflare Workers</a>, by setting its value to <code>no-store</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17761.md")</div>
<p>When you set the value to <code>no-store</code> on a subrequest made from a Worker, the Cloudflare Workers runtime will not check whether a match exists in the cache, and not add the response to the cache, even if the response includes directives in the <code>Cache-Control</code> HTTP header that otherwise indicate that the response is cacheable.</p>
<p>This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the <a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property, which is a cross-platform standard part of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface. Previously, if you set the <code>cache</code> property on <code>Request</code>, the Workers runtime threw an exception.</p>
<p>If you've tried to use <code>@planetscale/database</code>, <code>redis-js</code>, <code>stytch-node</code>, <code>supabase</code>, <code>axiom-js</code> or have seen the error message <code>The cache field on RequestInitializerDict is not implemented in fetch</code> — you should try again, making sure that the <a href="/workers/configuration/compatibility-dates/">Compatibility Date</a> of your Worker is set to on or after <code>2024-11-11</code>, or the <a href="/workers/configuration/compatibility-flags/#enable-cache-no-store-http-standard-api"><code>cache_option_enabled</code> compatibility flag</a> is enabled for your Worker.</p>
<ul>
<li>Learn <a href="/workers/reference/how-the-cache-works/">how the Cache works with Cloudflare Workers</a></li>
<li>Enable <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> for your Cloudflare Worker</li>
<li>Explore <a href="/workers/runtime-apis/">Runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">Bindings</a> available in Cloudflare Workers</li>
</ul>
</div></article></div>
