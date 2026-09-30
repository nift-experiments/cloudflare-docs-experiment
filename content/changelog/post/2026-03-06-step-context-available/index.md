<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 6, 2026</time><h2 id="post-title">Workflow steps now expose retry attempt number via step context</h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>Cloudflare Workflows allows you to configure specific retry logic for each step in your workflow execution. Now, you can access <strong>which</strong> retry attempt is currently executing for calls to <code>step.do()</code>:</p>
<pre><code class="language-ts">await step.do(&quot;my-step&quot;, async (ctx) =&gt; {&#10;	// ctx.attempt is 1 on first try, 2 on first retry, etc.&#10;	console.log(`Attempt ${ctx.attempt}`);&#10;});&#10;</code></pre>
<p>You can use the step context for improved logging &amp; observability, progressive backoff, or conditional logic in your workflow definition.</p>
<p>Note that the current attempt number is 1-indexed. For more information on retry behavior, refer to <a href="/workflows/build/sleeping-and-retrying/">Sleeping and Retrying</a>.</p>
</div></article></div>
