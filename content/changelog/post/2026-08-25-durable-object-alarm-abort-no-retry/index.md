<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 25, 2026</time><h2 id="post-title">Prevent Durable Object alarm retries when using `ctx.abort()`</h2>
<div class="changelog-badges"><span>durable-objects</span></div><div class="changelog-body"><p>By default, an alarm interrupted by <code>ctx.abort()</code> retries after the Durable Object resets. Pass <code>{ retryAlarm: false }</code> when the alarm should stop instead:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17720.md")</div>
<p>For example, an alarm that deletes its storage can use this option to avoid repeating the cleanup or re-running the Durable Object constructor.</p>
<p>Alarms can run concurrently with other requests to the same Durable Object. If another request calls <code>ctx.abort()</code> while an alarm is running, the <code>retryAlarm</code> option on that call also controls whether the alarm retries.</p>
<p>The default retry prevents an unrelated request from permanently canceling the alarm. Set <code>retryAlarm: false</code> on every abort path that should stop an in-progress alarm, not only on calls from the alarm handler. Existing calls to <code>ctx.abort()</code> keep retrying alarms.</p>
<p>For local development, <code>retryAlarm</code> requires Wrangler 4.126.0 or later.</p>
<p>For more information, refer to <a href="/durable-objects/api/state/#abort"><code>ctx.abort()</code></a>.</p>
</div></article></div>
