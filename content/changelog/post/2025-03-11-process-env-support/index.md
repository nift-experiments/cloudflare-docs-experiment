<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 11, 2025</time><h2 id="post-title">Access your Worker's environment variables from process.env</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now access <a href="/workers/configuration/environment-variables/">environment variables</a> and
<a href="/workers/configuration/secrets/">secrets</a> on <a href="/workers/runtime-apis/nodejs/process/#processenv"><code>process.env</code></a>
when using the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag"><code>nodejs_compat</code> compatibility flag</a>.</p>
<pre><code class="language-js">const apiClient = ApiClient.new({ apiKey: process.env.API_KEY });&#10;const LOG_LEVEL = process.env.LOG_LEVEL || &quot;info&quot;;&#10;</code></pre>
<p>In Node.js, environment variables are exposed via the global <code>process.env</code> object. Some libraries
assume that this object will be populated, and many developers may be used to accessing variables
in this way.</p>
<p>Previously, the <code>process.env</code> object was always empty unless written to in Worker code. This could
cause unexpected errors or friction when developing Workers using code previously written for Node.js.</p>
<p>Now, <a href="/workers/configuration/environment-variables/">environment variables</a>,
<a href="/workers/configuration/secrets/">secrets</a>, and <a href="/workers/runtime-apis/bindings/version-metadata/">version metadata</a>
can all be accessed on <code>process.env</code>.</p>
<p>To opt-in to the new <code>process.env</code> behaviour now, add the <a href="/workers/configuration/compatibility-flags/#enable-auto-populating-processenv"><code>nodejs_compat_populate_process_env</code></a> compatibility flag to your
<code>wrangler.json</code> configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17766.md")</div>
<p>After April 1, 2025, populating <code>process.env</code> will become the default behavior when both <code>nodejs_compat</code> is enabled and
your Worker's <code>compatibility_date</code> is after &quot;2025-04-01&quot;.</p>
</div></article></div>
