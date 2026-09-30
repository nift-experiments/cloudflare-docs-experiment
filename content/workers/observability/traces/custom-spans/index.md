---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/traces/custom-spans/
  description: Create custom spans to trace your own application logic alongside Cloudflare's automatic instrumentation.
  full_title: Custom spans · Cloudflare Workers docs
  head_html: <title>Custom spans · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Create custom spans to trace your own application logic alongside Cloudflare&#x27;s automatic instrumentation."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/traces/custom-spans/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/traces/custom-spans/index.md"><meta property="og:title" content="Custom spans · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create custom spans to trace your own application logic alongside Cloudflare&#x27;s automatic instrumentation."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/traces/custom-spans/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/traces/custom-spans/#page","headline":"Custom spans \u00b7 Cloudflare Workers docs","description":"Create custom spans to trace your own application logic alongside Cloudflare's automatic instrumentation.","url":"https://developers.cloudflare.com/workers/observability/traces/custom-spans/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/traces/custom-spans/
  schema: 1
---
<p>Cloudflare Workers <a href="/workers/observability/traces/spans-and-attributes/">automatically instruments</a> platform operations like fetch calls, KV reads, and D1 queries. Custom spans let you extend this visibility into your own application logic, so you can trace custom code paths alongside the built-in instrumentation.</p>
<p>The custom spans API is available in two ways — both provide the same methods and behave identically:</p>
<ul>
<li><strong><code>import { tracing } from &quot;cloudflare:workers&quot;</code></strong> — works anywhere in your codebase, including utility functions, libraries, and modules that do not have access to the handler context.</li>
<li><strong><code>ctx.tracing</code></strong> — available on the <a href="/workers/runtime-apis/context/"><code>ExecutionContext</code></a> passed to your handler, convenient when you are already working within a handler.</li>
</ul>
<p>There are two span creation methods:</p>
<ul>
<li><strong><code>enterSpan()</code></strong> — creates a span that automatically ends when the callback returns or its returned promise settles. Use this for most instrumentation.</li>
<li><strong><code>startActiveSpan()</code></strong> — creates a span that you end manually by calling <code>span.end()</code>. Use this when the span must outlive the callback, such as when instrumenting streams or other long-lived operations.</li>
</ul>
<h2 id="enable-tracing">Enable tracing</h2>
<p>Custom spans require tracing to be enabled on your Worker. If you have not already done so, set <code>observability.traces.enabled</code> to <code>true</code> in your <a href="/workers/wrangler/configuration/#observability">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17023.md")
</div>
<h2 id="create-a-custom-span">Create a custom span</h2>
<p>Use <code>tracing.enterSpan()</code> to wrap a section of code in a named span. The span automatically becomes a child of whichever span is currently active, and ends when the callback returns or its returned promise settles.</p>
<p>The following example uses both access methods — the <code>cloudflare:workers</code> import and <code>ctx.tracing</code> — to show that they are interchangeable:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17024.md")
</div>
<h2 id="api-reference">API reference</h2>
<h3 id="tracing-enterspan-name-callback-args"><code>tracing.enterSpan(name, callback, ...args)</code></h3>
<p>Creates a new span and runs <code>callback</code> inside it. The span is automatically ended when the callback returns (synchronous or asynchronous) or throws.</p>
<p><strong>Parameters:</strong></p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>The name of the span. This appears in trace visualizations.</td>
</tr>
<tr>
<td><code>callback</code></td>
<td><code>(span: Span, ...args: A) =&gt; T</code></td>
<td>The function to execute within the span. Receives the <code>Span</code> object as its first argument, followed by any additional arguments passed to <code>enterSpan</code>.</td>
</tr>
<tr>
<td><code>...args</code></td>
<td><code>A</code></td>
<td>Optional additional arguments forwarded to the callback after the <code>span</code> parameter.</td>
</tr>
</tbody>
</table>
<p><strong>Returns:</strong> The return value of <code>callback</code>.</p>
<p><strong>Behavior:</strong></p>
<ul>
<li>The new span is a child of whichever span is currently active on the async context. If no span is active, it becomes a child of the request's root span.</li>
<li>Nested <code>enterSpan</code> calls and runtime-created spans (such as <code>fetch</code> or KV operations) that run inside the callback automatically become children of this span.</li>
<li>The span ends when the callback returns synchronously, throws synchronously, or when its returned promise fulfills or rejects.</li>
</ul>
<pre tabindex="0"><code class="language-ts">// Synchronous callback — span ends when the function returns&#10;const result = tracing.enterSpan(&quot;parse&quot;, (span) =&gt; {&#10;	span.setAttribute(&quot;format&quot;, &quot;json&quot;);&#10;	return JSON.parse(body);&#10;});&#10;&#10;// Async callback — span ends when the promise settles&#10;const data = await tracing.enterSpan(&quot;fetchData&quot;, async (span) =&gt; {&#10;	const res = await fetch(&quot;https://api.example.com/data&quot;);&#10;	span.setAttribute(&quot;http.response.status_code&quot;, res.status);&#10;	return res.json();&#10;});&#10;&#10;// Forwarding arguments&#10;const doubled = tracing.enterSpan(&quot;compute&quot;, (span, x) =&gt; x * 2, 21);&#10;</code></pre>
<h3 id="tracing-startactivespan-name-callback-args"><code>tracing.startActiveSpan(name, callback, ...args)</code></h3>
<p>Creates a new span, makes it the active span while <code>callback</code> runs, and returns the callback result <strong>without</strong> automatically ending the span. You must call <code>span.end()</code> explicitly when the operation is complete.</p>
<p><strong>Parameters:</strong></p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>The name of the span. This appears in trace visualizations.</td>
</tr>
<tr>
<td><code>callback</code></td>
<td><code>(span: Span, ...args: A) =&gt; T</code></td>
<td>The function to execute while the span is active. Receives the <code>Span</code> object as its first argument, followed by any additional arguments.</td>
</tr>
<tr>
<td><code>...args</code></td>
<td><code>A</code></td>
<td>Optional additional arguments forwarded to the callback after the <code>span</code> parameter.</td>
</tr>
</tbody>
</table>
<p><strong>Returns:</strong> The return value of <code>callback</code>.</p>
<p><strong>Behavior:</strong></p>
<ul>
<li>Unlike <code>enterSpan</code>, the span is <strong>not</strong> automatically ended when the callback returns or throws. You are responsible for calling <code>span.end()</code>.</li>
<li>If you forget to call <code>span.end()</code>, the span is still submitted when the request-owned span object is destroyed, as a backstop. Do not rely on this behavior — always call <code>span.end()</code> explicitly.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17022.md")
</aside>
<p>Use <code>startActiveSpan</code> when you need a span to cover an operation that extends beyond a single callback — for example, instrumenting a stream pipeline where the span should remain open until the stream is fully consumed:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17025.md")
</div>
<p>You can also capture the span reference for later use without streams:</p>
<pre tabindex="0"><code class="language-ts">let capturedSpan;&#10;const value = tracing.startActiveSpan(&quot;manual-operation&quot;, (span) =&gt; {&#10;	capturedSpan = span;&#10;	span.setAttribute(&quot;phase&quot;, &quot;started&quot;);&#10;	return computeResult();&#10;});&#10;&#10;// The span is still open here — you can set more attributes&#10;capturedSpan.setAttribute(&quot;phase&quot;, &quot;complete&quot;);&#10;capturedSpan.end(); // Now the span is submitted&#10;</code></pre>
<h3 id="span"><code>Span</code></h3>
<p>The <code>Span</code> object is passed into the <code>enterSpan</code> and <code>startActiveSpan</code> callbacks. It provides methods to annotate the span with metadata and control its lifecycle.</p>
<h4 id="span-setattribute-key-value"><code>span.setAttribute(key, value)</code></h4>
<p>Sets an attribute on the span.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>key</code></td>
<td><code>string</code></td>
<td>The attribute name.</td>
</tr>
<tr>
<td><code>value</code></td>
<td><code>string | number | boolean | undefined</code></td>
<td>The attribute value. Passing <code>undefined</code> is a no-op.</td>
</tr>
</tbody>
</table>
<p>Attributes appear alongside the span in your traces and OpenTelemetry exports.</p>
<pre tabindex="0"><code class="language-ts">span.setAttribute(&quot;user.plan&quot;, &quot;enterprise&quot;);&#10;span.setAttribute(&quot;item.count&quot;, 42);&#10;span.setAttribute(&quot;cache.hit&quot;, true);&#10;</code></pre>
<h4 id="span-istraced"><code>span.isTraced</code></h4>
<p>A <code>readonly boolean</code> indicating whether this invocation is being traced. When the request is not sampled (based on your <a href="/workers/observability/traces/#sampling"><code>head_sampling_rate</code></a>), <code>isTraced</code> is <code>false</code> and <code>enterSpan</code> still runs the callback but does not record any telemetry.</p>
<p>You can use this to skip expensive attribute computation when the request is not being traced:</p>
<pre tabindex="0"><code class="language-ts">tracing.enterSpan(&quot;process&quot;, (span) =&gt; {&#10;	if (span.isTraced) {&#10;		span.setAttribute(&#10;			&quot;request.body.preview&quot;,&#10;			JSON.stringify(body).slice(0, 200),&#10;		);&#10;	}&#10;	return processBody(body);&#10;});&#10;</code></pre>
<h4 id="span-end"><code>span.end()</code></h4>
<p>Ends the span and submits its attributes to the tracing system. This method is idempotent — calling it multiple times has no effect after the first call. After <code>end()</code> is called, <code>span.isTraced</code> returns <code>false</code> and any further <code>setAttribute</code> calls are silently ignored, including calls from in-flight async work that has not yet completed.</p>
<ul>
<li>For spans created with <code>enterSpan</code>, you do not need to call <code>end()</code> — the runtime calls it automatically. Calling <code>end()</code> yourself is safe but has no effect since the runtime has already ended the span.</li>
<li>For spans created with <code>startActiveSpan</code>, you <strong>must</strong> call <code>end()</code> to submit the span.</li>
</ul>
<pre tabindex="0"><code class="language-ts">let mySpan;&#10;const result = tracing.startActiveSpan(&quot;manual-op&quot;, (span) =&gt; {&#10;	mySpan = span;&#10;	span.setAttribute(&quot;step&quot;, &quot;processing&quot;);&#10;	return doWork();&#10;});&#10;&#10;// Later, when the work is truly complete:&#10;mySpan.end(); // Span is submitted&#10;mySpan.end(); // No-op, safe to call again&#10;</code></pre>
<h2 id="nested-spans">Nested spans</h2>
<p>Spans nest automatically based on the JavaScript async context. Any <code>enterSpan</code> call or platform operation (such as <code>fetch</code> and <code>env.MY_KV.get()</code>) that runs inside a callback becomes a child of the enclosing span.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17026.md")
</div>
<p><img src="/assets/upstream/images/workers-observability/wobs_custom_spans_screenshot.png" alt="Trace waterfall showing custom spans nested alongside automatic KV and fetch instrumentation" /></p>
<h2 id="logging-within-spans">Logging within spans</h2>
<p><code>console.log()</code> and other console methods emit log events that are automatically attributed to the currently active span. This means log output from inside an <code>enterSpan</code> or <code>startActiveSpan</code> callback is associated with that span in your traces and OpenTelemetry exports.</p>
<pre tabindex="0"><code class="language-ts">tracing.enterSpan(&quot;processPayment&quot;, async (span) =&gt; {&#10;	console.log(&quot;Starting payment processing&quot;); // attributed to &quot;processPayment&quot;&#10;	const result = await chargeCard(token, amount);&#10;	console.log(&quot;Payment complete&quot;, result.id); // also attributed to &quot;processPayment&quot;&#10;});&#10;</code></pre>
<h2 id="typescript-types">TypeScript types</h2>
<p>The full type declarations for the custom spans API:</p>
<pre tabindex="0"><code class="language-ts">declare module &quot;cloudflare:workers&quot; {&#10;	namespace tracing {&#10;		function enterSpan&lt;T, A extends unknown[]&gt;(&#10;			name: string,&#10;			callback: (span: Span, ...args: A) =&gt; T,&#10;			...args: A&#10;		): T;&#10;&#10;		function startActiveSpan&lt;T, A extends unknown[]&gt;(&#10;			name: string,&#10;			callback: (span: Span, ...args: A) =&gt; T,&#10;			...args: A&#10;		): T;&#10;	}&#10;&#10;	class Span {&#10;		readonly isTraced: boolean;&#10;		setAttribute(&#10;			key: string,&#10;			value: string | number | boolean | undefined,&#10;		): void;&#10;		end(): void;&#10;	}&#10;}&#10;</code></pre>
<p>The same API is available on the handler context as <code>ctx.tracing</code>, with the same types.</p>
<h2 id="choosing-between-enterspan-and-startactivespan">Choosing between <code>enterSpan</code> and <code>startActiveSpan</code></h2>
<table>
<thead>
<tr>
<th></th>
<th><code>enterSpan</code></th>
<th><code>startActiveSpan</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>Span ends</td>
<td>Automatically, when the callback returns, throws, or its returned promise settles</td>
<td>Manually, when you call <code>span.end()</code></td>
</tr>
<tr>
<td>Active context scope</td>
<td>During the callback</td>
<td>During the callback</td>
</tr>
<tr>
<td>Use case</td>
<td>Most instrumentation — sync and async work that fits within a single callback</td>
<td>Operations that outlive the callback, such as stream pipelines</td>
</tr>
<tr>
<td>Error handling</td>
<td>Span auto-ends on throw</td>
<td>Span stays open on throw — call <code>span.end()</code> or rely on the runtime backstop</td>
</tr>
</tbody>
</table>
<p>Both methods set the span as the active context parent <strong>only during the callback</strong>. After the callback returns, the span is no longer the active parent. With <code>enterSpan</code>, this distinction does not matter because the span is also ended. With <code>startActiveSpan</code>, the span remains open but is no longer the context parent — new spans created after the callback returns are not children of this span.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li><strong>No manual parent-child wiring.</strong> Parent-child relationships are determined by the JavaScript async context automatically.</li>
<li><strong>No <code>setAttributes</code> (bulk set) yet.</strong> Use individual <code>setAttribute</code> calls. Bulk setting is planned for a future release.</li>
<li><strong>No <code>spanContext()</code> (trace/span IDs) yet.</strong> Access to trace and span identifiers for manual propagation across boundaries is planned for a future release.</li>
<li><strong>No <code>setOutcome</code> yet.</strong> Setting span outcome status is planned for a future release.</li>
</ul>
<p>For other tracing limitations, refer to the <a href="/workers/observability/traces/known-limitations/">known limitations</a> page.</p>
