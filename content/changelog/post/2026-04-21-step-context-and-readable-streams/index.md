<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 21, 2026</time><h2 id="post-title">Additional step context and ReadableStream support now available in Workflows step.do()</h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> now provides additional context inside <code>step.do()</code> callbacks and supports returning <code>ReadableStream</code> to handle larger step outputs.</p>
<h4 id="step-context-properties">Step context properties</h4>
<p>The <code>step.do()</code> callback receives a context object with new properties <a href="/changelog/post/2026-03-06-step-context-available/">alongside</a> <code>attempt</code>:</p>
<ul>
<li><strong><code>step.name</code></strong> — The name passed to <code>step.do()</code></li>
<li><strong><code>step.count</code></strong> — How many times a step with that name has been invoked in this instance (1-indexed)
<ul>
<li>Useful when running the same step in a loop.</li>
</ul>
</li>
<li><strong><code>config</code></strong> — The resolved step configuration, including <code>timeout</code> and <code>retries</code> with defaults applied</li>
</ul>
<pre><code class="language-ts">type ResolvedStepConfig = {&#10;	retries: {&#10;		limit: number;&#10;		delay: WorkflowDelayDuration | number;&#10;		backoff?: &quot;constant&quot; | &quot;linear&quot; | &quot;exponential&quot;;&#10;	};&#10;	timeout: WorkflowTimeoutDuration | number;&#10;};&#10;&#10;type WorkflowStepContext = {&#10;	step: {&#10;		name: string;&#10;		count: number;&#10;	};&#10;	attempt: number;&#10;	config: ResolvedStepConfig;&#10;};&#10;</code></pre>
<h4 id="readablestream-support-in-step-do">ReadableStream support in <code>step.do()</code></h4>
<p>Steps can now return a <code>ReadableStream</code> directly. Although non-stream step outputs are <a href="/workflows/reference/limits/">limited to 1 MiB</a>, streamed outputs support much larger payloads.</p>
<pre><code class="language-ts">const largePayload = await step.do(&quot;fetch-large-file&quot;, async () =&gt; {&#10;	const object = await env.MY_BUCKET.get(&quot;large-file.bin&quot;);&#10;	return object.body;&#10;});&#10;</code></pre>
<p>Note that streamed outputs are still considered part of the Workflow instance storage limit.</p>
</div></article></div>
