<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 17, 2025</time><h2 id="post-title">Import `env` to access bindings in your Worker's global scope</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now access <a href="/workers/runtime-apis/bindings/">bindings</a>
from anywhere in your Worker by importing the <code>env</code> object from <code>cloudflare:workers</code>.</p>
<p>Previously, <code>env</code> could only be accessed during a request. This meant that
bindings could not be used in the top-level context of a Worker.</p>
<p>Now, you can import <code>env</code> and access bindings such as <a href="/workers/configuration/secrets/">secrets</a>
or <a href="/workers/configuration/environment-variables/">environment variables</a> in the
initial setup for your Worker:</p>
<pre><code class="language-js">import { env } from &quot;cloudflare:workers&quot;;&#10;import ApiClient from &quot;example-api-client&quot;;&#10;&#10;// API_KEY and LOG_LEVEL now usable in top-level scope&#10;const apiClient = ApiClient.new({ apiKey: env.API_KEY });&#10;const LOG_LEVEL = env.LOG_LEVEL || &quot;info&quot;;&#10;&#10;export default {&#10;	fetch(req) {&#10;		// you can use apiClient or LOG_LEVEL, configured before any request is handled&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17767.md")</aside>
<p>Additionally, <code>env</code> was normally accessed as a argument to a Worker's entrypoint handler,
such as <a href="/workers/runtime-apis/fetch/"><code>fetch</code></a>.
This meant that if you needed to access a binding from a deeply nested function,
you had to pass <code>env</code> as an argument through many functions to get it to the
right spot. This could be cumbersome in complex codebases.</p>
<p>Now, you can access the bindings from anywhere in your codebase
without passing <code>env</code> as an argument:</p>
<pre><code class="language-js">// helpers.js&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;// env is *not* an argument to this function&#10;export async function getValue(key) {&#10;	let prefix = env.KV_PREFIX;&#10;	return await env.KV.get(`${prefix}-${key}`);&#10;}&#10;</code></pre>
<p>For more information, see <a href="/workers/runtime-apis/bindings#how-to-access-env">documentation on accessing <code>env</code></a>.</p>
</div></article></div>
