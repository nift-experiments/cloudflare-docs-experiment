<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 9, 2026</time><h2 id="post-title">Workflows now supports delay functions when retrying</h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p>With <a href="/workflows/">Workflows</a>, you can configure built-in retry behavior for each step. Previously, you could configure step retries with fixed delay durations, such as seconds, minutes, or hours, and backoff strategies such as <code>constant</code>, <code>linear</code>, or <code>exponential</code>.</p>
<p>Step retries now support dynamic delay functions. Instead of choosing only a base delay and backoff strategy, pass a function to <code>retries.delay</code> and calculate the next delay from the failed attempt and thrown error.</p>
<p>This is useful when retries should depend on the failure. Your Workflow may need to wait longer after a rate-limit error, but retry sooner after a short network failure. The delay function can also accommodate provider guidance if, for example, a downstream API returns a <code>Retry-After</code> value in its error messaging.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17833.md")</div>
<p>Dynamic delay functions can return a duration string, a number, or a promise that resolves to a duration. Use them to add adaptive retry behavior without writing separate queue or scheduling logic. For more information, refer to <a href="/workflows/build/sleeping-and-retrying/">Sleeping and retrying</a>.</p>
</div></article></div>
