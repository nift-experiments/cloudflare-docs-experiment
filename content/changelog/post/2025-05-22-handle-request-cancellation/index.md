<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 22, 2025</time><h2 id="post-title">Handle incoming request cancellation in Workers with Request.signal</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>In Cloudflare Workers, you can now attach an event listener to <a href="/workers/runtime-apis/request/"><code>Request</code></a> objects, using the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Request/signal"><code>signal</code> property</a>. This allows you to perform tasks when the request to your Worker is canceled by the client. To use this feature, you must set the <a href="/workers/configuration/compatibility-flags/#enable-requestsignal-for-incoming-requests"><code>enable_request_signal</code></a> compatibility flag.</p>
<p>You can use a listener to perform cleanup tasks or write to logs before your Worker's invocation ends. For example, if you run the Worker below, and then abort the request from the client, a log will be written:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17775.md")</div>
<p>For more information see the <a href="/workers/runtime-apis/request"><code>Request</code> documentation</a>.</p>
</div></article></div>
