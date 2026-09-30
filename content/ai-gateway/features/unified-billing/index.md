<p>Unified Billing allows users to call Workers AI and connect to various AI providers (such as OpenAI, Anthropic, and Google AI Studio) and receive a single Cloudflare bill. To use Unified Billing, you must purchase and load credits into your Cloudflare account in the Cloudflare dashboard, which you can then spend with AI Gateway.</p>
<p>A 5% fee is applied to all credits purchased through Unified Billing. For example, a $100 credit purchase will result in a $105 charge. Inference pricing from providers is passed through with no markup — you pay the same per-token rates as you would directly with the provider.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2814.md")
</aside>
<h2 id="pre-requisites">Pre-requisites</h2>
<ul>
<li>Ensure your Cloudflare account has <a href="#load-credits">sufficient credits loaded</a>.</li>
<li>Ensure you have <a href="/ai-gateway/configuration/authentication/">authenticated</a> your AI Gateway.</li>
<li>To use credits for Workers AI, set your gateway's <strong>Workers AI Billing</strong> setting to <strong>Unified billing</strong>.</li>
</ul>
<h2 id="load-credits">Load credits</h2>
<p>To load credits for AI Gateway:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>AI Gateway</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<p>The <strong>Credits Available</strong> card on the top right shows how many AI gateway credits you have on your account currently.</p>
<ol start="2">
<li>In <strong>Credits Available</strong>, select <strong>Manage</strong>.</li>
<li>If your account does not have an available payment method, AI Gateway will prompt you to add a payment method to purchase credits. Add a payment method.</li>
<li>Select <strong>Top-up credits</strong>.</li>
<li>Add the amount of credits you want to purchase, then select <strong>Confirm and pay</strong>.</li>
</ol>
<h3 id="auto-top-up">Auto-top up</h3>
<p>You can configure AI Gateway to automatically replenish your credits when they fall below a certain threshold. To configure auto top-up:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>AI Gateway</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Credits Available</strong>, select <strong>Manage</strong>.</li>
<li>Select <strong>Setup auto top-up credits</strong>.</li>
<li>Choose a threshold and a recharge amount for auto top-up.</li>
</ol>
<p>When your balance falls below the set threshold, AI Gateway will automatically apply the auto top-up amount to your account.</p>
<h2 id="credential-precedence">Credential precedence</h2>
<p>When a request reaches AI Gateway, credentials are resolved in this order:</p>
<ol>
<li><strong>Provider key on the request</strong> — if the request carries provider authentication (for example, an <code>Authorization</code> header), AI Gateway forwards it to the provider unchanged. BYOK and Unified Billing are not consulted.</li>
<li><strong>BYOK (stored key)</strong> — if no provider key is on the request and the gateway has a <a href="/ai-gateway/configuration/bring-your-own-keys/">stored key</a> for the provider under the <code>default</code> alias, that key is used.</li>
<li><strong>Unified Billing</strong> — if neither of the above applies, the request is served with Cloudflare-managed credentials and billed against your Cloudflare credit balance.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2813.md")
</aside>
<h2 id="prevent-unified-billing-fallback-for-byok-third-party-providers">Prevent Unified Billing fallback for BYOK third-party providers</h2>
<p>Turn on <strong>Require provider credentials</strong> to prevent Unified Billing fallback for third-party providers. Third-party provider requests must use credentials supplied with the request or stored on the gateway. Requests without applicable credentials return an HTTP <code>400</code> response instead of using Cloudflare-managed credentials.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2818.md")
</div></div>
<p>To require provider credentials for one third-party provider request, set the <code>cf-aig-no-wholesale</code> header to <code>true</code>. This header can prevent Unified Billing fallback but cannot relax the gateway setting. If <strong>Require provider credentials</strong> is on, setting the header to <code>false</code> has no effect.</p>
<p>Workers AI requests do not use provider credentials. This setting does not block these requests or change the gateway's configured Workers AI billing mode.</p>
<h2 id="use-unified-billing">Use Unified Billing</h2>
<p>Unified Billing works in two ways: through the AI binding or through the HTTP API. Both deduct credits from your account automatically without requiring provider API keys.</p>
<p>To use credits for Workers AI, <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">configure the gateway's Workers AI billing setting</a> as <strong>Unified billing</strong>. Workers AI requests routed through that gateway deduct from your prepaid credit balance in real time. In the AI binding, include the gateway ID in the third argument to <code>env.AI.run()</code>. For REST API requests, include the <code>cf-aig-gateway-id</code> header. Prepaid credits provide access to Workers AI models that otherwise require the Workers Paid plan and provide <a href="/workers-ai/platform/limits/#paid-models">higher rate limits for frontier models</a>.</p>
<h3 id="ai-binding">AI binding</h3>
<p>Call any model listed in the <a href="/ai/models/">model catalog</a> using <code>env.AI.run()</code>. This includes both Workers AI models and third-party models from providers like OpenAI, Anthropic, and Google.</p>
<pre><code class="language-typescript">const resp = await env.AI.run(&#10;	&quot;openai/gpt-4.1-mini&quot;,&#10;	{&#10;		messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	},&#10;	{&#10;		gateway: { id: &quot;my-gateway&quot; },&#10;	},&#10;);&#10;</code></pre>
<p>Refer to the <a href="/ai-gateway/usage/worker-binding-methods/">binding reference</a> for the full API surface.</p>
<h3 id="http-api">HTTP API</h3>
<p>Call a supported provider through the AI Gateway REST API without passing a provider API key.</p>
<h4 id="rest-api">REST API</h4>
<p>Use the Cloudflare API to call third-party models. Pass your Cloudflare API token in the <code>Authorization</code> header:</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p>Refer to <a href="/ai-gateway/usage/rest-api/">REST API</a> for more details on all available endpoints.</p>
<h4 id="ai-gateway-provider-native-endpoints">AI Gateway provider-native endpoints</h4>
<p>You can also call providers directly through <a href="/ai-gateway/usage/providers/">provider-native endpoints</a> using the <code>cf-aig-authorization</code> header to authenticate:</p>
<p>The HTTP API supports the following providers:</p>
<ul>
<li><a href="/ai-gateway/usage/providers/openai/">OpenAI</a></li>
<li><a href="/ai-gateway/usage/providers/anthropic/">Anthropic</a></li>
<li><a href="/ai-gateway/usage/providers/google-ai-studio/">Google AI Studio</a></li>
<li><a href="/ai-gateway/usage/providers/vertex/">Google Vertex AI</a></li>
<li><a href="/ai-gateway/usage/providers/grok/">xAI</a></li>
<li><a href="/ai-gateway/usage/providers/groq/">Groq</a></li>
</ul>
<h3 id="spend-limits">Spend limits</h3>
<p>Set <a href="/ai-gateway/features/spend-limits/">spend limit rules</a> on individual gateways to cap spend, scoped by model, provider, or custom metadata dimensions like user or team.</p>
<h3 id="zero-data-retention-zdr">Zero Data Retention (ZDR)</h3>
<p>Zero Data Retention (ZDR) routes Unified Billing traffic through provider endpoints that do not retain prompts or responses. Enable it with the gateway-level <code>zdr</code> setting, which maps to ZDR-capable upstream provider configurations. This setting only applies to Unified Billing requests that use Cloudflare-managed credentials. It does not apply to BYOK or other AI Gateway requests.</p>
<p>ZDR does not control AI Gateway logging. To disable request/response logging in AI Gateway, update the logging settings separately in <a href="/ai-gateway/observability/logging/">Logging</a>.</p>
<p>ZDR is currently supported for:</p>
<ul>
<li><a href="/ai-gateway/usage/providers/openai/">OpenAI</a></li>
<li><a href="/ai-gateway/usage/providers/anthropic/">Anthropic</a></li>
</ul>
<p>If ZDR is enabled for a provider that does not support it, AI Gateway falls back to the standard (non-ZDR) Unified Billing configuration.</p>
<h4 id="default-configuration">Default configuration</h4>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2821.md")
</div></div>
<h4 id="per-request-override-cf-aig-zdr">Per-request override (<code>cf-aig-zdr</code>)</h4>
<p>Use the <code>cf-aig-zdr</code> header to override the gateway default for a single Unified Billing request. Set it to <code>true</code> to force ZDR, or <code>false</code> to disable ZDR for the request.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-header &quot;cf-aig-zdr: true&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;Explain Zero Data Retention.&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
