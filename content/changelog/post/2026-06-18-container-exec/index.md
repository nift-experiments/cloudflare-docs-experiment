<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 18, 2026</time><h2 id="post-title">exec() is now available for Containers</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><code>exec()</code> is now available for <a href="/containers/">Containers</a>. Use <code>this.ctx.container.exec()</code> to start processes inside a running Container, stream standard input and output, inspect exit codes, and signal each process.</p>
<p>Call <code>exec()</code> from a class extending <code>Container</code>, or from another Durable Object through <code>this.ctx.container</code>. The associated Container must already be running.</p>
<p>This example starts the Container when needed, then reads its Node.js version:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17713.md")</div>
<p>The command array starts an executable directly, without an implicit shell. Invoke a shell explicitly for pipes, redirects, or variable expansion.</p>
<p>One RPC method can coordinate multiple <code>exec()</code> calls in one caller-to-Durable Object round trip. It can also pass byte-oriented <code>ReadableStream</code> input or return streamed output with flow control.</p>
<p>For options and streaming examples, refer to <a href="/containers/guides/execute-commands/">Execute commands</a>.</p>
</div></article></div>
