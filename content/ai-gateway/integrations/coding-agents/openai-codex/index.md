<p><a href="https://developers.openai.com/codex/">OpenAI Codex</a> is a coding agent you run in your terminal. It supports <a href="https://developers.openai.com/codex/config-advanced#custom-model-providers">custom model providers</a> defined in <code>config.toml</code>. This configuration adds a provider that points at AI Gateway's <a href="/ai-gateway/usage/providers/openai/">OpenAI endpoint</a>, so Codex sends its requests through AI Gateway. AI Gateway authenticates the model provider for you through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>, so you pass a Cloudflare API token instead of an OpenAI API key. If your gateway is protected by Cloudflare Access, refer to <a href="#use-with-cloudflare-access">Use with Cloudflare Access</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2911.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, you need:</p>
<ul>
<li>Your Cloudflare account ID. To find it, refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find your account and zone IDs</a>.</li>
<li>An AI Gateway. You can use your account's <code>default</code> gateway or <a href="/ai-gateway/get-started/">create a gateway</a> and use its slug.</li>
<li>A <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with <code>AI Gateway</code> permission.</li>
<li><a href="/ai-gateway/features/unified-billing/#load-credits">Credits loaded</a> on your account for third-party models.</li>
<li><a href="https://developers.openai.com/codex/cli/">Codex</a> installed and updated to the latest version.</li>
</ul>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2915.md")
</div>
<h2 id="use-with-cloudflare-access">Use with Cloudflare Access</h2>
<p>If your gateway is protected by <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>, Codex can authenticate with a short-lived Access token instead of a Cloudflare API token. Point the provider at your <a href="/ai-gateway/configuration/custom-domains/">custom domain</a>, and configure the provider's <code>auth</code> command to fetch the token with <a href="/cloudflare-one/access-controls/authenticate-agents/#make-requests-with-cloudflared-access-curl"><code>cloudflared</code></a> instead of passing a token through an environment variable.</p>
<p>Update the same <code>~/.codex/cloudflare-aig.config.toml</code> profile from the Unified Billing setup so the provider points at your custom domain and uses <code>cloudflared</code> for authentication. The <code>cloudflare-aig</code> in <code>codex --profile cloudflare-aig</code> refers to this file's name. Replace <code>ai-gateway.example.com</code> with your custom domain.</p>
<pre><code class="language-toml">model_provider = &quot;cloudflare-ai-gateway&quot;&#10;model = &quot;gpt-5.5&quot;&#10;model_reasoning_effort = &quot;medium&quot;&#10;&#10;[model_providers.cloudflare-ai-gateway]&#10;name = &quot;Cloudflare AI Gateway&quot;&#10;base_url = &quot;https://ai-gateway.example.com/openai&quot;&#10;wire_api = &quot;responses&quot;&#10;&#10;[model_providers.cloudflare-ai-gateway.auth]&#10;command = &quot;cloudflared&quot;&#10;args = [&quot;access&quot;, &quot;login&quot;, &quot;--no-verbose&quot;, &quot;https://ai-gateway.example.com&quot;]&#10;timeout_ms = 30000&#10;refresh_interval_ms = 0&#10;</code></pre>
<p>Compared to the Unified Billing setup in the previous section, the custom domain replaces the account ID and gateway ID in <code>base_url</code>, and the <code>auth</code> block replaces <code>env_key</code>.</p>
<p>Start Codex with the profile:</p>
<pre><code class="language-bash">codex --profile cloudflare-aig&#10;</code></pre>
<p>The first request opens your identity provider's login flow. After you authenticate, requests route through AI Gateway with your Access identity attached as <a href="/ai-gateway/observability/custom-metadata/#reserved-metadata"><code>cf.user_id</code></a>.</p>
<p>To confirm traffic reaches AI Gateway, refer to <a href="/ai-gateway/integrations/coding-agents/#verify-it-works">Verify it works</a>.</p>
