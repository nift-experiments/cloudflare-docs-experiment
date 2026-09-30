---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/configuration/environment-variables/
  description: Pass configuration, secrets, and runtime settings to Sandbox SDK containers using environment variables.
  full_title: Environment variables · Cloudflare Sandbox SDK docs
  head_html: <title>Environment variables · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Pass configuration, secrets, and runtime settings to Sandbox SDK containers using environment variables."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/configuration/environment-variables/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/configuration/environment-variables/index.md"><meta property="og:title" content="Environment variables · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pass configuration, secrets, and runtime settings to Sandbox SDK containers using environment variables."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/configuration/environment-variables/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/configuration/environment-variables/#page","headline":"Environment variables \u00b7 Cloudflare Sandbox SDK docs","description":"Pass configuration, secrets, and runtime settings to Sandbox SDK containers using environment variables.","url":"https://developers.cloudflare.com/sandbox/configuration/environment-variables/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/configuration/environment-variables/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13561.md")
</aside>
<p>Pass configuration, secrets, and runtime settings to your sandboxes using environment variables.</p>
<h2 id="sdk-configuration-variables">SDK configuration variables</h2>
<p>These environment variables configure how the Sandbox SDK behaves. Set these as Worker <code>vars</code> in your <code>wrangler.jsonc</code> file. The SDK reads them from the Worker's environment bindings.</p>
<h3 id="sandbox-transport">SANDBOX_TRANSPORT</h3>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Type</strong></td>
<td><code>&quot;http&quot;</code> | <code>&quot;websocket&quot;</code> | <code>&quot;rpc&quot;</code></td>
</tr>
<tr>
<td><strong>Default</strong></td>
<td><code>&quot;http&quot;</code></td>
</tr>
</tbody>
</table>
<p>Controls the transport protocol for SDK-to-container communication. RPC transport multiplexes all operations over a single persistent connection, avoiding <a href="/workers/platform/limits/#subrequests">subrequest limits</a> when performing many SDK operations per request.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13562.md")
</div>
<p>For a complete guide including valid transport modes, performance considerations, and migration instructions, refer to <a href="/sandbox/configuration/transport/">Transport modes</a>.</p>
<h3 id="command-timeout-ms">COMMAND_TIMEOUT_MS</h3>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Type</strong></td>
<td><code>number</code> (milliseconds)</td>
</tr>
<tr>
<td><strong>Default</strong></td>
<td>None (no timeout)</td>
</tr>
</tbody>
</table>
<p>Sets a global default timeout for every <code>exec()</code> call. When set, any command that exceeds this duration raises an error on the caller side and closes the connection.</p>
<p>Per-command <code>timeout</code> on <code>exec()</code> and session-level <code>commandTimeoutMs</code> on <a href="/sandbox/api/sessions/#createsession"><code>createSession()</code></a> both override this value. For more details on timeout precedence, refer to <a href="/sandbox/guides/execute-commands/#timeouts">Execute commands - Timeouts</a>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13563.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13560.md")
</aside>
<h2 id="three-ways-to-set-environment-variables">Three ways to set environment variables</h2>
<p>The Sandbox SDK provides three methods for setting environment variables, each suited for different use cases:</p>
<h3 id="1-sandbox-level-with-setenvvars"><ol>
<li>Sandbox-level with setEnvVars()</li>
</ol></h3>
<p>Set environment variables globally for all commands in the sandbox:</p>
<pre tabindex="0"><code class="language-typescript">const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;&#10;// Set once, available for all subsequent commands&#10;await sandbox.setEnvVars({&#10;	DATABASE_URL: env.DATABASE_URL,&#10;	API_KEY: env.API_KEY,&#10;});&#10;&#10;await sandbox.exec(&quot;python migrate.py&quot;); // Has DATABASE_URL and API_KEY&#10;await sandbox.exec(&quot;python seed.py&quot;); // Has DATABASE_URL and API_KEY&#10;&#10;// Unset variables by passing undefined&#10;await sandbox.setEnvVars({&#10;	API_KEY: &quot;new-key&quot;, // Updates API_KEY&#10;	OLD_SECRET: undefined, // Unsets OLD_SECRET&#10;});&#10;</code></pre>
<p><strong>Use when:</strong> You need the same environment variables for multiple commands.</p>
<p><strong>Unsetting variables</strong>: Pass <code>undefined</code> or <code>null</code> to unset environment variables:</p>
<pre tabindex="0"><code class="language-typescript">await sandbox.setEnvVars({&#10;	API_KEY: &#x27;new-key&#x27;,     // Sets API_KEY&#10;	OLD_SECRET: undefined,  // Unsets OLD_SECRET&#10;	DEBUG_MODE: null        // Unsets DEBUG_MODE&#10;});&#10;</code></pre>
<h3 id="2-per-command-with-exec-options"><ol start="2">
<li>Per-command with exec() options</li>
</ol></h3>
<p>Pass environment variables for a specific command:</p>
<pre tabindex="0"><code class="language-typescript">await sandbox.exec(&quot;node app.js&quot;, {&#10;	env: {&#10;		NODE_ENV: &quot;production&quot;,&#10;		PORT: &quot;3000&quot;,&#10;	},&#10;});&#10;&#10;// Also works with startProcess()&#10;await sandbox.startProcess(&quot;python server.py&quot;, {&#10;	env: {&#10;		DATABASE_URL: env.DATABASE_URL,&#10;	},&#10;});&#10;</code></pre>
<p><strong>Use when:</strong> You need different environment variables for different commands, or want to override sandbox-level variables.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13559.md")
</aside>
<h3 id="3-session-level-with-createsession"><ol start="3">
<li>Session-level with createSession()</li>
</ol></h3>
<p>Create an isolated session with its own environment variables:</p>
<pre tabindex="0"><code class="language-typescript">const session = await sandbox.createSession({&#10;	env: {&#10;		DATABASE_URL: env.DATABASE_URL,&#10;		SECRET_KEY: env.SECRET_KEY,&#10;	},&#10;});&#10;&#10;// All commands in this session have these vars&#10;await session.exec(&quot;python migrate.py&quot;);&#10;await session.exec(&quot;python seed.py&quot;);&#10;</code></pre>
<p><strong>Use when:</strong> You need isolated execution contexts with different environment variables running concurrently.</p>
<h2 id="unsetting-environment-variables">Unsetting environment variables</h2>
<p>The Sandbox SDK supports unsetting environment variables by passing <code>undefined</code> or <code>null</code> values. This enables idiomatic JavaScript patterns for managing configuration:</p>
<pre tabindex="0"><code class="language-typescript">await sandbox.setEnvVars({&#10;	// Set new values&#10;	API_KEY: &#x27;new-key&#x27;,&#10;	DATABASE_URL: env.DATABASE_URL,&#10;&#10;	// Unset variables (removes them from the environment)&#10;	OLD_API_KEY: undefined,&#10;	TEMP_TOKEN: null&#10;});&#10;</code></pre>
<p><strong>Before this change</strong>: Passing <code>undefined</code> values would throw a runtime error.</p>
<p><strong>After this change</strong>: <code>undefined</code> and <code>null</code> values run <code>unset VARIABLE_NAME</code> in the shell.</p>
<h3 id="use-cases-for-unsetting">Use cases for unsetting</h3>
<p><strong>Remove sensitive data after use:</strong></p>
<pre tabindex="0"><code class="language-typescript">// Use a temporary token&#10;await sandbox.setEnvVars({ TEMP_TOKEN: &#x27;abc123&#x27; });&#10;await sandbox.exec(&#x27;curl -H &quot;Authorization: $TEMP_TOKEN&quot; api.example.com&#x27;);&#10;&#10;// Clean up the token&#10;await sandbox.setEnvVars({ TEMP_TOKEN: undefined });&#10;</code></pre>
<p><strong>Conditional environment setup:</strong></p>
<pre tabindex="0"><code class="language-typescript">await sandbox.setEnvVars({&#10;	API_KEY: env.API_KEY,&#10;	DEBUG_MODE: env.NODE_ENV === &#x27;development&#x27; ? &#x27;true&#x27; : undefined,&#10;	PROFILING: env.ENABLE_PROFILING ? &#x27;true&#x27; : undefined&#10;});&#10;</code></pre>
<p><strong>Reset to system defaults:</strong></p>
<pre tabindex="0"><code class="language-typescript">// Unset to fall back to container&#x27;s default NODE_ENV&#10;await sandbox.setEnvVars({ NODE_ENV: undefined });&#10;</code></pre>
<h2 id="common-patterns">Common patterns</h2>
<h3 id="pass-worker-secrets-to-sandbox">Pass Worker secrets to sandbox</h3>
<p>Securely pass secrets from your Worker to the sandbox. First, set secrets using Wrangler:</p>
<pre tabindex="0"><code class="language-bash">wrangler secret put OPENAI_API_KEY&#10;wrangler secret put DATABASE_URL&#10;</code></pre>
<p>Then pass them to your sandbox:</p>
<pre tabindex="0"><code class="language-typescript">import { getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;interface Env {&#10;	Sandbox: DurableObjectNamespace&lt;Sandbox&gt;;&#10;	OPENAI_API_KEY: string;&#10;	DATABASE_URL: string;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		const sandbox = getSandbox(env.Sandbox, &quot;user-sandbox&quot;);&#10;&#10;		// Option 1: Set globally for all commands&#10;		await sandbox.setEnvVars({&#10;			OPENAI_API_KEY: env.OPENAI_API_KEY,&#10;			DATABASE_URL: env.DATABASE_URL,&#10;		});&#10;		await sandbox.exec(&quot;python analyze.py&quot;);&#10;&#10;		// Option 2: Pass per-command&#10;		await sandbox.exec(&quot;python analyze.py&quot;, {&#10;			env: {&#10;				OPENAI_API_KEY: env.OPENAI_API_KEY,&#10;			},&#10;		});&#10;&#10;		return Response.json({ success: true });&#10;	},&#10;};&#10;</code></pre>
<h3 id="combine-default-and-specific-variables">Combine default and specific variables</h3>
<pre tabindex="0"><code class="language-typescript">const defaults = { NODE_ENV: &quot;production&quot;, LOG_LEVEL: &quot;info&quot; };&#10;&#10;await sandbox.exec(&quot;npm start&quot;, {&#10;	env: { ...defaults, PORT: &quot;3000&quot;, API_KEY: env.API_KEY },&#10;});&#10;</code></pre>
<h3 id="multiple-isolated-sessions">Multiple isolated sessions</h3>
<p>Run different tasks with different environment variables concurrently:</p>
<pre tabindex="0"><code class="language-typescript">// Production database session&#10;const prodSession = await sandbox.createSession({&#10;	env: { DATABASE_URL: env.PROD_DATABASE_URL },&#10;});&#10;&#10;// Staging database session&#10;const stagingSession = await sandbox.createSession({&#10;	env: { DATABASE_URL: env.STAGING_DATABASE_URL },&#10;});&#10;&#10;// Run migrations on both concurrently&#10;await Promise.all([&#10;	prodSession.exec(&quot;python migrate.py&quot;),&#10;	stagingSession.exec(&quot;python migrate.py&quot;),&#10;]);&#10;</code></pre>
<h3 id="configure-transport-mode">Configure transport mode</h3>
<p>Set <code>SANDBOX_TRANSPORT</code> in your Worker's <code>vars</code> to switch between HTTP, WebSocket, and RPC transport. For details on when and how to configure each transport, refer to <a href="/sandbox/configuration/transport/">Transport modes</a>.</p>
<h3 id="bucket-mounting-credentials">Bucket mounting credentials</h3>
<p>When mounting S3-compatible object storage, the SDK uses <strong>s3fs-fuse</strong> under the hood, which requires AWS-style credentials. For R2, generate API tokens from the Cloudflare dashboard and provide them using AWS environment variable names:</p>
<p><strong>Get R2 API tokens:</strong></p>
<ol>
<li>Go to <a href="https://dash.cloudflare.com/?to=/:account/r2"><strong>R2</strong> &gt; <strong>Overview</strong></a> in the Cloudflare dashboard</li>
<li>Select <strong>Manage R2 API Tokens</strong></li>
<li>Create a token with <strong>Object Read &amp; Write</strong> permissions</li>
<li>Copy the <strong>Access Key ID</strong> and <strong>Secret Access Key</strong></li>
</ol>
<p><strong>Set credentials as Worker secrets:</strong></p>
<pre tabindex="0"><code class="language-bash">wrangler secret put AWS_ACCESS_KEY_ID&#10;&#35; Paste your R2 Access Key ID&#10;&#10;wrangler secret put AWS_SECRET_ACCESS_KEY&#10;&#35; Paste your R2 Secret Access Key&#10;</code></pre>
<p><strong>Mount buckets with automatic credential detection:</strong></p>
<pre tabindex="0"><code class="language-typescript">import { getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;interface Env {&#10;	Sandbox: DurableObjectNamespace&lt;Sandbox&gt;;&#10;	AWS_ACCESS_KEY_ID: string;&#10;	AWS_SECRET_ACCESS_KEY: string;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		const sandbox = getSandbox(env.Sandbox, &quot;data-processor&quot;);&#10;&#10;		// Credentials automatically detected from environment&#10;		await sandbox.mountBucket(&quot;my-r2-bucket&quot;, &quot;/data&quot;, {&#10;			endpoint: &quot;https://YOUR_ACCOUNT_ID.r2.cloudflarestorage.com&quot;,&#10;		});&#10;&#10;		// Access mounted bucket using standard file operations&#10;		await sandbox.exec(&quot;python&quot;, { args: [&quot;process.py&quot;, &quot;/data/input.csv&quot;] });&#10;&#10;		return Response.json({ success: true });&#10;	},&#10;};&#10;</code></pre>
<p>The SDK automatically detects <code>AWS_ACCESS_KEY_ID</code> and <code>AWS_SECRET_ACCESS_KEY</code> from your Worker's environment when you call <code>mountBucket()</code> without explicit credentials.</p>
<p><strong>Pass credentials explicitly</strong> (if using custom secret names):</p>
<pre tabindex="0"><code class="language-typescript">await sandbox.mountBucket(&quot;my-r2-bucket&quot;, &quot;/data&quot;, {&#10;	endpoint: &quot;https://YOUR_ACCOUNT_ID.r2.cloudflarestorage.com&quot;,&#10;	credentials: {&#10;		accessKeyId: env.R2_ACCESS_KEY_ID,&#10;		secretAccessKey: env.R2_SECRET_ACCESS_KEY,&#10;	},&#10;});&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="aws-nomenclature-for-r2">AWS nomenclature for R2</h3>
@markup("md", "content/.markup/bodies/13558.md")
</aside>
<p>See <a href="/sandbox/guides/mount-buckets/">Mount buckets guide</a> for complete bucket mounting documentation.</p>
<h2 id="environment-variable-precedence">Environment variable precedence</h2>
<p>When the same variable is set at multiple levels, the most specific level takes precedence:</p>
<ol>
<li><strong>Command-level</strong> (highest) - Passed to <code>exec()</code> or <code>startProcess()</code> options</li>
<li><strong>Sandbox or session-level</strong> - Set with <code>setEnvVars()</code></li>
<li><strong>Container default</strong> - Built into the Docker image with <code>ENV</code></li>
<li><strong>System default</strong> (lowest) - Operating system defaults</li>
</ol>
<p>Example:</p>
<pre tabindex="0"><code class="language-typescript">// In Dockerfile: ENV NODE_ENV=development&#10;&#10;// Sandbox-level&#10;await sandbox.setEnvVars({ NODE_ENV: &quot;staging&quot; });&#10;&#10;// Command-level overrides all&#10;await sandbox.exec(&quot;node app.js&quot;, {&#10;	env: { NODE_ENV: &quot;production&quot; }, // This wins&#10;});&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/configuration/transport/">Transport modes</a> - Configure HTTP, WebSocket, and RPC transport</li>
<li><a href="/sandbox/configuration/wrangler/">Wrangler configuration</a> - Setting Worker-level environment</li>
<li><a href="/workers/configuration/secrets/">Secrets</a> - Managing sensitive data</li>
<li><a href="/sandbox/api/sessions/">Sessions API</a> - Session-level environment variables</li>
<li><a href="/sandbox/concepts/security/">Security model</a> - Understanding data isolation</li>
<li><a href="/sandbox/guides/outbound-traffic/">Handle outbound traffic</a> - Keep credentials out of the sandbox entirely using outbound handlers</li>
</ul>
