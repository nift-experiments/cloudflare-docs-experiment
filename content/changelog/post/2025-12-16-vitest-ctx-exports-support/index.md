<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 16, 2025</time><h2 id="post-title">Support for ctx.exports in @cloudflare/vitest-pool-workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="/workers/testing/vitest-integration/"><code>@cloudflare/vitest-pool-workers</code></a> package now supports the <a href="/workers/runtime-apis/context/#exports"><code>ctx.exports</code> API</a>, allowing you to access your Worker's top-level exports during tests.</p>
<p>You can access <code>ctx.exports</code> in unit tests by calling <code>createExecutionContext()</code>:</p>
<pre><code class="language-ts">import { createExecutionContext } from &quot;cloudflare:test&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;&#10;it(&quot;can access ctx.exports&quot;, async () =&gt; {&#10;  const ctx = createExecutionContext();&#10;  const result = await ctx.exports.MyEntryPoint.myMethod();&#10;  expect(result).toBe(&quot;expected value&quot;);&#10;});&#10;</code></pre>
<p>Alternatively, you can import <code>exports</code> directly from <code>cloudflare:workers</code>:</p>
<pre><code class="language-ts">import { exports } from &quot;cloudflare:workers&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;&#10;it(&quot;can access imported exports&quot;, async () =&gt; {&#10;  const result = await exports.MyEntryPoint.myMethod();&#10;  expect(result).toBe(&quot;expected value&quot;);&#10;});&#10;</code></pre>
<p>See the <a href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/context-exports">context-exports fixture</a> for a complete example.</p>
</div></article></div>
