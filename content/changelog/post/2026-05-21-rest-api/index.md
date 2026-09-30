<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 21, 2026</time><h2 id="post-title">Call any AI model through AI Gateway's new REST API</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway now uses the AI REST API on <code>api.cloudflare.com</code>. You can call any model — whether from OpenAI, Anthropic, Google, or hosted on Workers AI — through one unified API, using the same endpoints and authentication regardless of provider. Four endpoints are available:</p>
<ul>
<li><code>POST /ai/run</code> — universal endpoint for all models and modalities</li>
<li><code>POST /ai/v1/chat/completions</code> — OpenAI SDK compatible</li>
<li><code>POST /ai/v1/responses</code> — OpenAI Responses API compatible</li>
<li><code>POST /ai/v1/messages</code> — Anthropic SDK compatible</li>
</ul>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-5.5&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p>All AI Gateway features — logging, caching, rate limiting, and guardrails — are applied automatically. Third-party models are billed through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>, so you do not need to manage separate provider API keys.</p>
<p>Third-party model requests are routed through your account's default gateway, which is created automatically on first use. To route requests through a specific gateway, add the <code>cf-aig-gateway-id</code> header.</p>
<p>If you are already calling Workers AI models through the existing REST API, that path (<code>/ai/run/@cf/{model}</code>) continues to work. To call Workers AI models through AI Gateway, use the <code>@cf/</code> model prefix (for example, <code>@cf/moonshotai/kimi-k2.6</code>) and include the <code>cf-aig-gateway-id</code> header to specify which gateway to route through.</p>
<p>For more details and examples, refer to the <a href="/ai-gateway/usage/rest-api/">REST API documentation</a>.</p>
</div></article></div>
