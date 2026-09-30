<p>The AI binding (<code>env.AI</code>) lets you call AI models and access AI Gateway features directly from your Worker.</p>
<p>For a step-by-step setup guide, refer to <a href="/ai-gateway/integrations/aig-workers-ai-binding/">Set up Workers AI with AI Gateway</a>.</p>
<h2 id="configuration">Configuration</h2>
<p>Add an AI binding to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2777.md")
</div>
<p>The binding is accessible in your Worker code as <code>env.AI</code>.</p>
<p>If you're using TypeScript, run <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a> whenever you modify your Wrangler configuration file. This generates types for the <code>env</code> object based on your bindings, as well as <a href="/workers/languages/typescript/">runtime types</a>.</p>
<h2 id="env-ai-run"><code>env.AI.run()</code></h2>
<p>Runs an inference request through AI Gateway. Accepts Workers AI models (<code>@cf/</code> prefix) and third-party models (<code>{author}/{model}</code> format).</p>
<p><strong>Workers AI model:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2778.md")
</div>
<p>To use prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>, set the gateway's <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">Workers AI billing setting</a> to <strong>Unified billing</strong> and specify that gateway in the binding request. Prepaid credits provide access to Workers AI models that otherwise require the Workers Paid plan and provide <a href="/workers-ai/platform/limits/#paid-models">higher rate limits for frontier models</a>.</p>
<p><strong>Third-party model:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2779.md")
</div>
<p>Third-party models require an AI Gateway and use <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>. Cloudflare manages the provider credentials and deducts credits from your account. You do not need to supply your own API keys.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2776.md")
</aside>
<p>Browse available models in the <a href="/ai/models/">model catalog</a>.</p>
<h3 id="gateway-options">Gateway options</h3>
<p>The third argument to <code>env.AI.run()</code> accepts a <code>gateway</code> object with the following parameters:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td><code>string</code></td>
<td><em>required</em></td>
<td>Name of your <a href="/ai-gateway/get-started/">AI Gateway</a>. Must be in the same account as your Worker. Use <code>&quot;default&quot;</code> to automatically create a gateway on the first authenticated request. Refer to <a href="/ai-gateway/configuration/manage-gateway/#default-gateway">Default gateway</a> for details.</td>
</tr>
<tr>
<td><code>skipCache</code></td>
<td><code>boolean</code></td>
<td><code>false</code></td>
<td>Skip the <a href="/ai-gateway/features/caching/">cache</a> for this request.</td>
</tr>
<tr>
<td><code>cacheTtl</code></td>
<td><code>number</code></td>
<td>—</td>
<td><a href="/ai-gateway/features/caching/">Cache TTL</a> in seconds.</td>
</tr>
<tr>
<td><code>cacheKey</code></td>
<td><code>string</code></td>
<td>—</td>
<td>Custom <a href="/ai-gateway/features/caching/">cache key</a> for this request.</td>
</tr>
<tr>
<td><code>collectLog</code></td>
<td><code>boolean</code></td>
<td>—</td>
<td>Whether to <a href="/ai-gateway/observability/logging/">collect logs</a> for this request.</td>
</tr>
<tr>
<td><code>metadata</code></td>
<td><code>object</code></td>
<td>—</td>
<td><a href="/ai-gateway/observability/custom-metadata/">Custom metadata</a> to attach to the log entry.</td>
</tr>
</tbody>
</table>
<h2 id="env-ai-aigatewaylogid"><code>env.AI.aiGatewayLogId</code></h2>
<p>Returns the log ID from the most recent <code>env.AI.run()</code> request.</p>
<pre><code class="language-typescript">const myLogId = env.AI.aiGatewayLogId;&#10;</code></pre>
<h2 id="env-ai-gateway"><code>env.AI.gateway()</code></h2>
<p>Returns a gateway instance for accessing AI Gateway methods directly.</p>
<pre><code class="language-typescript">const gateway = env.AI.gateway(&quot;my-gateway&quot;);&#10;</code></pre>
<p>The gateway instance exposes the following methods.</p>
<h3 id="patchlog"><code>patchLog()</code></h3>
<p>Sends feedback, score, and metadata for a specific log entry. All properties in the second argument are optional.</p>
<pre><code class="language-typescript">await gateway.patchLog(&quot;my-log-id&quot;, {&#10;	feedback: 1,&#10;	score: 100,&#10;	metadata: {&#10;		user: &quot;123&quot;,&#10;	},&#10;});&#10;</code></pre>
<p><strong>Returns:</strong> <code>Promise&lt;void&gt;</code></p>
<h3 id="getlog"><code>getLog()</code></h3>
<p>Retrieves details of a specific log entry. If the <code>AiGatewayLog</code> type is missing, run <a href="/workers/languages/typescript/#generate-types"><code>wrangler types</code></a>.</p>
<pre><code class="language-typescript">const log = await gateway.getLog(&quot;my-log-id&quot;);&#10;</code></pre>
<p><strong>Returns:</strong> <code>Promise&lt;AiGatewayLog&gt;</code></p>
<h3 id="geturl"><code>getUrl()</code></h3>
<p>Returns the base URL for your AI Gateway. Pass an optional provider name to get the provider-specific endpoint.</p>
<pre><code class="language-typescript">const baseUrl = await gateway.getUrl();&#10;// https://gateway.ai.cloudflare.com/v1/my-account-id/my-gateway/&#10;&#10;const openaiUrl = await gateway.getUrl(&quot;openai&quot;);&#10;// https://gateway.ai.cloudflare.com/v1/my-account-id/my-gateway/openai&#10;</code></pre>
<p><strong>Parameters:</strong> Optional <code>provider</code> (string or <code>AIGatewayProviders</code> enum)</p>
<p><strong>Returns:</strong> <code>Promise&lt;string&gt;</code></p>
<h4 id="sdk-integration-examples">SDK integration examples</h4>
<p><strong>OpenAI SDK:</strong></p>
<pre><code class="language-typescript">import OpenAI from &quot;openai&quot;;&#10;&#10;const openai = new OpenAI({&#10;	apiKey: &quot;my api key&quot;, // defaults to process.env[&quot;OPENAI_API_KEY&quot;]&#10;	baseURL: await env.AI.gateway(&quot;my-gateway&quot;).getUrl(&quot;openai&quot;),&#10;});&#10;</code></pre>
<p><strong>Vercel AI SDK with OpenAI:</strong></p>
<pre><code class="language-typescript">import { createOpenAI } from &quot;@ai-sdk/openai&quot;;&#10;&#10;const openai = createOpenAI({&#10;	baseURL: await env.AI.gateway(&quot;my-gateway&quot;).getUrl(&quot;openai&quot;),&#10;});&#10;</code></pre>
<p><strong>Vercel AI SDK with Anthropic:</strong></p>
<pre><code class="language-typescript">import { createAnthropic } from &quot;@ai-sdk/anthropic&quot;;&#10;&#10;const anthropic = createAnthropic({&#10;	baseURL: await env.AI.gateway(&quot;my-gateway&quot;).getUrl(&quot;anthropic&quot;),&#10;});&#10;</code></pre>
