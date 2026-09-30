<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 16, 2026</time><h2 id="post-title">Workers tracing now supports custom spans</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now create custom trace spans in your Workers code using <code>tracing.enterSpan()</code>. Custom spans appear alongside the automatic platform instrumentation (fetch calls, KV reads, D1 queries, and other platform operations) in your traces and OpenTelemetry exports, with correct parent-child nesting.</p>
<p>The API is available via <code>import { tracing } from &quot;cloudflare:workers&quot;</code> or through the handler context as <code>ctx.tracing</code>:</p>
<pre><code class="language-ts">import { tracing } from &quot;cloudflare:workers&quot;;&#10;&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    return tracing.enterSpan(&quot;handleRequest&quot;, async (span) =&gt; {&#10;      span.setAttribute(&quot;url.path&quot;, new URL(request.url).pathname);&#10;      const data = await env.MY_KV.get(&quot;key&quot;);&#10;      return new Response(data);&#10;    });&#10;  },&#10;};&#10;</code></pre>
<p>Spans nest automatically based on the JavaScript async context, and are auto-ended when the callback returns or its returned promise settles. The <code>Span</code> object provides <code>setAttribute(key, value)</code> for attaching metadata and an <code>isTraced</code> property to check whether the current request is being sampled.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_custom_spans_screenshot.png" alt="Trace waterfall showing custom spans nested alongside automatic KV and fetch instrumentation" /></p>
<p><a href="/workers/observability/traces/#how-to-enable-tracing">Tracing must be enabled</a> in your Wrangler configuration for spans to be recorded.</p>
<p>For full API details and examples, refer to <a href="/workers/observability/traces/custom-spans/">Custom spans</a>.</p>
</div></article></div>
