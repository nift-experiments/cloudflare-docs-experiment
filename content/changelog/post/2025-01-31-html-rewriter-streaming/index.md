<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 31, 2025</time><h2 id="post-title">Transform HTML quickly with streaming content</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now transform HTML elements with streamed content using <a href="/workers/runtime-apis/html-rewriter"><code>HTMLRewriter</code></a>.</p>
<p>Methods like <code>replace</code>, <code>append</code>, and <code>prepend</code> now accept <a href="/workers/runtime-apis/response/"><code>Response</code></a> and <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>
values as <a href="/workers/runtime-apis/html-rewriter/#global-types"><code>Content</code></a>.</p>
<p>This can be helpful in a variety of situations. For instance, you may have a Worker in front of an origin,
and want to replace an element with content from a different source. Prior to this change, you would have to load
all of the content from the upstream URL and convert it into a string before replacing the element. This slowed
down overall response times.</p>
<p>Now, you can pass the <code>Response</code> object directly into the <code>replace</code> method, and HTMLRewriter will immediately
start replacing the content as it is streamed in. This makes responses faster.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17765.md")</div>
<p>For more information, see the <a href="/workers/runtime-apis/html-rewriter"><code>HTMLRewriter</code> documentation</a>.</p>
</div></article></div>
