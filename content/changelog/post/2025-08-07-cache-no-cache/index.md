<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 7, 2025</time><h2 id="post-title">Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>By setting the value of the <code>cache</code> property to <code>no-cache</code>, you can force <a href="/workers/reference/how-the-cache-works/">Cloudflare's
cache</a> to revalidate its contents with the origin when
making subrequests from <a href="/workers">Cloudflare Workers</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17783.md")</div>
<p>When <code>no-cache</code> is set, the Worker request will first look for a match in Cloudflare's cache, then:</p>
<ul>
<li>If there is a match, a conditional request is sent to the origin, regardless of whether or not the match is fresh or stale. If the resource has not changed, the
cached version is returned. If the resource has changed, it will be downloaded from the origin, updated in the cache, and returned.</li>
<li>If there is no match, Workers will make a standard request to the origin and cache the response.</li>
</ul>
<p>This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the
<a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property, which is a cross-platform standard part
of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface. Previously, if you set the <code>cache</code>
property on <code>Request</code> to <code>'no-cache'</code>, the Workers runtime threw an exception.</p>
<ul>
<li>Learn <a href="/workers/reference/how-the-cache-works/">how the Cache works with Cloudflare Workers</a></li>
<li>Enable <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> for your Cloudflare Worker</li>
<li>Explore <a href="/workers/runtime-apis/">Runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">Bindings</a> available in Cloudflare Workers</li>
</ul>
</div></article></div>
