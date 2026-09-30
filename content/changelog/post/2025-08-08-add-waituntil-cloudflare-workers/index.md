<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 8, 2025</time><h2 id="post-title">Directly import `waitUntil` in Workers for easily spawning background tasks</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now import <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code></a> from <code>cloudflare:workers</code> to extend your Worker's execution beyond the request lifecycle from anywhere in your code.</p>
<p>Previously, <code>waitUntil</code> could only be accessed through the <a href="/workers/runtime-apis/context/">execution context</a> (<code>ctx</code>) parameter passed to your Worker's handler functions. This meant that if you needed to schedule background tasks from deeply nested functions or utility modules, you had to pass the <code>ctx</code> object through multiple function calls to access <code>waitUntil</code>.</p>
<p>Now, you can import <code>waitUntil</code> directly and use it anywhere in your Worker without needing to pass <code>ctx</code> as a parameter:</p>
<pre><code class="language-js">import { waitUntil } from &quot;cloudflare:workers&quot;;&#10;&#10;export function trackAnalytics(eventData) {&#10;	const analyticsPromise = fetch(&quot;https://analytics.example.com/track&quot;, {&#10;		method: &quot;POST&quot;,&#10;		body: JSON.stringify(eventData),&#10;	});&#10;&#10;	// Extend execution to ensure analytics tracking completes&#10;	waitUntil(analyticsPromise);&#10;}&#10;</code></pre>
<p>This is particularly useful when you want to:</p>
<ul>
<li>Schedule background tasks from utility functions or modules</li>
<li>Extend execution for analytics, logging, or cleanup operations</li>
<li>Avoid passing the execution context through multiple layers of function calls</li>
</ul>
<pre><code class="language-js">import { waitUntil } from &quot;cloudflare:workers&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// Background task that should complete even after response is sent&#10;		cleanupTempData(env.KV_NAMESPACE);&#10;		return new Response(&quot;Hello, World!&quot;);&#10;	}&#10;};&#10;&#10;function cleanupTempData(kvNamespace) {&#10;	// This function can now use waitUntil without needing ctx&#10;	const deletePromise = kvNamespace.delete(&quot;temp-key&quot;);&#10;	waitUntil(deletePromise);&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17784.md")</aside>
<p>For more information, see the <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code> documentation</a>.</p>
</div></article></div>
