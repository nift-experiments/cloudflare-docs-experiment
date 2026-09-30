<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 28, 2026</time><h2 id="post-title">Workers tracing — write custom spans with new startActiveSpan() and span.end() runtime APIs</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The Workers runtime now provides built-in <code>tracing.startActiveSpan()</code> and <code>span.end()</code> APIs, allowing you to write custom spans for operations that last beyond a single callback — for example, instrumenting a stream pipeline where the span should stay open until the stream is fully consumed.</p>
<p>This augments the <a href="/changelog/post/2026-06-16-custom-spans/">existing API for writing custom spans</a>, <code>tracing.enterSpan()</code>, which automatically ends a span when its callback is returned. With <code>startActiveSpan()</code>, the span remains open after the callback returns, and you call <code>span.end()</code> when the work is complete:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17808.md")</div>
<p>For more details, refer to the <a href="/workers/observability/traces/custom-spans/">custom spans documentation</a>.</p>
</div></article></div>
