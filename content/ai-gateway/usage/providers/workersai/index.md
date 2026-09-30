<p>Use AI Gateway as a unified control layer for <a href="/workers-ai/">Workers AI</a> requests, with analytics, logging, caching, security, and prepaid billing. To use prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>, set the gateway's <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">Workers AI billing setting</a> to <strong>Unified billing</strong>. Requests to frontier models billed with prepaid credits receive <a href="/workers-ai/platform/limits/#paid-models">higher rate limits</a>.</p>
<h2 id="rest-api">REST API</h2>
<p>Use the <a href="/ai-gateway/usage/rest-api/">REST API</a> to call Workers AI models. Workers AI models use the <code>@cf/</code> prefix in the model name and require the <code>cf-aig-gateway-id</code> header to specify which gateway to route through.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;cf-aig-gateway-id: default&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;@cf/moonshotai/kimi-k2.6&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h2 id="workers-binding">Workers binding</h2>
<p>You can integrate Workers AI with AI Gateway using an environment binding. To include an AI Gateway within your Worker, add the gateway as an object in your Workers AI request.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2949.md")
</div>
<p>For a detailed step-by-step guide on integrating Workers AI with AI Gateway using a binding, refer to <a href="/ai-gateway/integrations/aig-workers-ai-binding/">Integrations in AI Gateway</a>.</p>
<p>Workers AI supports the following parameters for AI gateways:</p>
<ul>
<li><code>id</code> string
<ul>
<li>Name of your existing <a href="/ai-gateway/get-started/">AI Gateway</a>. Must be in the same account as your Worker.</li>
</ul>
</li>
<li><code>skipCache</code> boolean(default: false)
<ul>
<li>Controls whether the request should <a href="/ai-gateway/features/caching/#skip-cache-cf-aig-skip-cache">skip the cache</a>.</li>
</ul>
</li>
<li><code>cacheTtl</code> number
<ul>
<li>Controls the <a href="/ai-gateway/features/caching/#cache-ttl-cf-aig-cache-ttl">Cache TTL</a>.</li>
</ul>
</li>
</ul>
