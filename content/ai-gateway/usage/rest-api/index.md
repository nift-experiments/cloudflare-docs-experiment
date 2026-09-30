<p>The REST API lets you call any model — whether hosted on Cloudflare or by a third-party provider like OpenAI, Anthropic, or Google — through the same Cloudflare API, with all AI Gateway features — logging, caching, rate limiting, and more — applied automatically.</p>
<p>No provider SDKs or API keys are needed. Authentication and billing are handled through your Cloudflare account. Third-party models are billed via <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>. Workers AI models can use prepaid AI Gateway credits or <a href="/workers-ai/platform/pricing/">Workers AI billing</a>.</p>
<h2 id="endpoints">Endpoints</h2>
<p>Four endpoints are available, each suited to different use cases:</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Format</th>
<th>Use case</th>
<th>Third-Party Models</th>
<th>Workers AI Models (<code>@cf/</code>)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>POST /ai/run</code></td>
<td>Envelope with <code>model</code>, <code>input</code></td>
<td>All models and modalities (LLM, image, TTS, ASR)</td>
<td>✅ Yes</td>
<td>✅ Yes</td>
</tr>
<tr>
<td><code>POST /ai/v1/chat/completions</code></td>
<td>OpenAI chat completions</td>
<td>LLMs — OpenAI SDK compatible</td>
<td>✅ Yes</td>
<td>✅ Yes</td>
</tr>
<tr>
<td><code>POST /ai/v1/responses</code></td>
<td>OpenAI Responses API</td>
<td>Agentic workflows — OpenAI SDK compatible</td>
<td>✅ Yes</td>
<td>✅ Model dependent</td>
</tr>
<tr>
<td><code>POST /ai/v1/messages</code></td>
<td>Anthropic Messages API</td>
<td>LLMs — Anthropic SDK compatible</td>
<td>✅ Yes</td>
<td>❌ No</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2787.md")
</aside>
<h2 id="authentication">Authentication</h2>
<p>Authenticate with a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> that has the <strong>Account</strong> &gt; <strong>Workers AI</strong> &gt; <strong>Read</strong> permission. Pass it in the <code>Authorization</code> header.</p>
<p>All <code>/accounts/{account_id}/ai/*</code> endpoints require the Workers AI permission. This applies to third-party models and to Workers AI (<code>@cf/</code>) models. A token that holds only an <code>AI Gateway</code> permission returns <code>401</code> with error code <code>10000</code>.</p>
<p>The <code>AI Gateway</code> permissions apply to the <code>/accounts/{account_id}/ai-gateway/*</code> endpoints, which manage gateway configuration, logs, and routes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2786.md")
</aside>
<h2 id="model-naming">Model naming</h2>
<p>Third-party models use the <code>author/model</code> format:</p>
<ul>
<li><code>openai/gpt-4.1</code> — OpenAI</li>
<li><code>anthropic/claude-sonnet-4</code> — Anthropic</li>
<li><code>google/gemini-3-flash</code> — Google</li>
<li><code>xai/grok-3</code> — xAI</li>
</ul>
<p>Workers AI models use the <code>@cf/author/model</code> format (for example, <code>@cf/moonshotai/kimi-k2.6</code>). Workers AI requests also require the <code>cf-aig-gateway-id</code> header — refer to <a href="#call-a-workers-ai-model">Call a Workers AI model</a> for details.</p>
<p>Browse available models in the <a href="/ai/models/">model catalog</a>.</p>
<h2 id="ai-run-universal-endpoint"><code>/ai/run</code> — universal endpoint</h2>
<p>Accepts any model with its per-model schema. Model-specific parameters go inside <code>input</code>.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1&quot;,&#10;    &quot;input&quot;: {&#10;      &quot;messages&quot;: [&#10;        {&#10;          &quot;role&quot;: &quot;user&quot;,&#10;          &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;      ],&#10;      &quot;max_tokens&quot;: 512&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h3 id="call-a-workers-ai-model">Call a Workers AI model</h3>
<p>To call a Workers AI model, use the <code>@cf/</code> prefix in the model name and include the <code>cf-aig-gateway-id</code> header to specify which gateway to route through.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;cf-aig-gateway-id: default&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;@cf/moonshotai/kimi-k2.6&quot;,&#10;    &quot;input&quot;: {&#10;      &quot;messages&quot;: [&#10;        {&#10;          &quot;role&quot;: &quot;user&quot;,&#10;          &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;      ]&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>The existing Workers AI endpoint with the model ID in the URL path also continues to work:</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/moonshotai/kimi-k2.6&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;cf-aig-gateway-id: default&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>To use prepaid AI Gateway credits for Workers AI, use the model-in-path endpoint shown above, set the gateway's <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">Workers AI billing setting</a> to <strong>Unified billing</strong>, and include its ID in the <code>cf-aig-gateway-id</code> header. Requests to frontier models billed with prepaid credits receive <a href="/workers-ai/platform/limits/#paid-models">higher rate limits</a>.</p>
<h3 id="background-requests-and-webhooks">Background requests and webhooks</h3>
<p>By default, <code>/ai/run</code> requests are synchronous — the connection stays open until the model finishes and the result comes back in the response. For long-running models — such as image, video, or audio generation — or when you do not want to hold a connection open, run the request in the background and have AI Gateway notify a webhook when it completes.</p>
<p>Set <code>background</code> to <code>true</code> and provide a <code>webhookUrl</code>. Both are fields of the <code>options</code> object in the <code>/ai/run</code> body, alongside <code>model</code> and <code>input</code>.</p>
<p><code>webhookUrl</code> can only be provided when <code>background</code> is <code>true</code>. Providing a <code>webhookUrl</code> without <code>background: true</code> returns a <code>400</code> error.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;google/nano-banana&quot;,&#10;    &quot;input&quot;: {&#10;      &quot;prompt&quot;: &quot;A cozy coffee shop interior with warm lighting, plants hanging from the ceiling, and a cat sleeping on a velvet armchair by the window&quot;,&#10;      &quot;aspect_ratio&quot;: &quot;16:9&quot;&#10;    },&#10;    &quot;options&quot;: {&#10;      &quot;background&quot;: true,&#10;      &quot;webhookUrl&quot;: &quot;https://example.com/my-webhook&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>A background request returns immediately while the model runs. The result is delivered to your webhook when the run completes.</p>
<h4 id="webhook-payload">Webhook payload</h4>
<p>When the run completes, AI Gateway sends a single <code>POST</code> request to your <code>webhookUrl</code> with the run outcome:</p>
<pre><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;run-id&gt;&quot;,&#10;	&quot;state&quot;: &quot;&lt;run-state&gt;&quot;,&#10;	&quot;result&quot;: {},&#10;	&quot;error&quot;: null,&#10;	&quot;provider&quot;: &quot;google&quot;,&#10;	&quot;model&quot;: &quot;google/nano-banana&quot;,&#10;	&quot;usage&quot;: {}&#10;}&#10;</code></pre>
<p>Webhook delivery is best-effort and is not retried. The destination must be an HTTPS URL that does not resolve to a private network address.</p>
<h4 id="webhook-format">Webhook format</h4>
<p>Use the optional <code>webhookFormat</code> field in the <code>options</code> object to control the shape of the webhook body. The default is <code>raw</code>. <code>webhookFormat</code> can only be provided when <code>webhookUrl</code> is present. Otherwise, the request returns a <code>400</code> error.</p>
<table>
<thead>
<tr>
<th>Format</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>raw</code></td>
<td>Sends the payload as-is (default).</td>
</tr>
<tr>
<td><code>chat</code></td>
<td>Wraps the payload in <code>{ &quot;text&quot;: &quot;&lt;prettified JSON&gt;&quot; }</code>, matching the incoming-webhook body accepted by Google Chat and Slack.</td>
</tr>
</tbody>
</table>
<h2 id="ai-v1-chat-completions-openai-compatible"><code>/ai/v1/chat/completions</code> — OpenAI compatible</h2>
<p>Uses the standard OpenAI chat completions format. The <code>model</code> field uses the same <code>author/model</code> naming. This endpoint is compatible with the OpenAI SDK and other OpenAI-compatible clients.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;system&quot;,&#10;        &quot;content&quot;: &quot;You are a helpful assistant.&quot;&#10;      },&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ],&#10;    &quot;max_tokens&quot;: 512,&#10;    &quot;temperature&quot;: 0.7,&#10;    &quot;stream&quot;: true&#10;  }&#x27;&#10;</code></pre>
<h3 id="openai-sdk">OpenAI SDK</h3>
<p>Point the OpenAI SDK <code>baseURL</code> at the Cloudflare API:</p>
<pre><code class="language-javascript">import OpenAI from &quot;openai&quot;;&#10;&#10;const openai = new OpenAI({&#10;	apiKey: CLOUDFLARE_API_TOKEN,&#10;	baseURL: `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/ai/v1`,&#10;});&#10;&#10;const response = await openai.chat.completions.create({&#10;	model: &quot;openai/gpt-4.1&quot;,&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;});&#10;</code></pre>
<h2 id="ai-v1-responses-openai-responses-api"><code>/ai/v1/responses</code> — OpenAI Responses API</h2>
<p>Uses the OpenAI Responses API format for agentic workflows. Compatible with the OpenAI SDK.</p>
<pre><code class="language-javascript">import OpenAI from &quot;openai&quot;;&#10;&#10;const openai = new OpenAI({&#10;	apiKey: CLOUDFLARE_API_TOKEN,&#10;	baseURL: `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/ai/v1`,&#10;});&#10;&#10;const response = await openai.responses.create({&#10;	model: &quot;openai/gpt-4.1&quot;,&#10;	input: &quot;What is Cloudflare?&quot;,&#10;});&#10;</code></pre>
<h2 id="ai-v1-messages-anthropic-compatible"><code>/ai/v1/messages</code> — Anthropic compatible</h2>
<p>Uses the Anthropic Messages API format. Compatible with the Anthropic SDK.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;anthropic/claude-sonnet-4-5&quot;,&#10;    &quot;max_tokens&quot;: 512,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>Point the Anthropic SDK <code>baseURL</code> at the Cloudflare API:</p>
<pre><code class="language-javascript">import Anthropic from &quot;@anthropic-ai/sdk&quot;;&#10;&#10;const anthropic = new Anthropic({&#10;	apiKey: CLOUDFLARE_API_TOKEN,&#10;	baseURL: `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/ai/v1`,&#10;});&#10;&#10;const message = await anthropic.messages.create({&#10;	model: &quot;anthropic/claude-sonnet-4-5&quot;,&#10;	max_tokens: 512,&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;});&#10;</code></pre>
<h2 id="provider-tools-and-web-search">Provider tools and web search</h2>
<p>Some providers expose native tools — including server-side web search — through these endpoints. Refer to <a href="/ai-gateway/usage/web-search/">Web Search</a> for the supported models per provider and the request shape each one uses. Browse the <a href="/ai/models/">model catalog</a> for canonical model IDs.</p>
<h2 id="specify-a-gateway">Specify a gateway</h2>
<p>By default, third-party model requests route through your account's default AI Gateway. To use a specific gateway, include the <code>cf-aig-gateway-id</code> header. Workers AI requests always require this header.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;cf-aig-gateway-id: default&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;anthropic/claude-sonnet-4&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;Hello&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>With the OpenAI SDK, set the header via <code>defaultHeaders</code>:</p>
<pre><code class="language-javascript">const openai = new OpenAI({&#10;	apiKey: CLOUDFLARE_API_TOKEN,&#10;	baseURL: `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/ai/v1`,&#10;	defaultHeaders: {&#10;		&quot;cf-aig-gateway-id&quot;: &quot;default&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>All AI Gateway features configured on that gateway — caching, rate limiting, guardrails, and logging — apply to the request.</p>
<h2 id="per-request-configuration">Per-request configuration</h2>
<p>Use <code>cf-aig-*</code> headers to control AI Gateway behavior on a per-request basis:</p>
<table>
<thead>
<tr>
<th>Header</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf-aig-skip-cache</code></td>
<td>boolean</td>
<td>Skip the cache for this request.</td>
</tr>
<tr>
<td><code>cf-aig-cache-ttl</code></td>
<td>number</td>
<td>Cache TTL in seconds.</td>
</tr>
<tr>
<td><code>cf-aig-cache-key</code></td>
<td>string</td>
<td>Custom cache key.</td>
</tr>
<tr>
<td><code>cf-aig-collect-log</code></td>
<td>boolean</td>
<td>Turn logging on or off for this request.</td>
</tr>
<tr>
<td><code>cf-aig-request-timeout</code></td>
<td>number</td>
<td>Request timeout in milliseconds.</td>
</tr>
<tr>
<td><code>cf-aig-max-attempts</code></td>
<td>number</td>
<td>Retry attempts (max 5).</td>
</tr>
<tr>
<td><code>cf-aig-retry-delay</code></td>
<td>number</td>
<td>Retry delay in milliseconds (max 60000).</td>
</tr>
<tr>
<td><code>cf-aig-backoff</code></td>
<td>string</td>
<td>Backoff method: <code>constant</code>, <code>linear</code>, or <code>exponential</code>.</td>
</tr>
<tr>
<td><code>cf-aig-metadata</code></td>
<td>JSON string</td>
<td>Custom metadata to attach to the log entry.</td>
</tr>
</tbody>
</table>
<p>For more details on these options, refer to <a href="/ai-gateway/configuration/request-handling/">Request handling</a> and <a href="/ai-gateway/features/caching/">Caching</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ai-gateway/features/unified-billing/">Unified Billing</a> — load credits and pay for inference requests with a single Cloudflare bill.</li>
<li><a href="/ai-gateway/usage/worker-binding-methods/">Workers AI binding</a> — call models from within a Cloudflare Worker using <code>env.AI.run()</code>.</li>
<li><a href="/ai/models/">Model catalog</a> — browse models supported by the REST API.</li>
</ul>
