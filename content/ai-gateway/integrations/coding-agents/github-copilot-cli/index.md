<p><a href="https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli">GitHub Copilot CLI</a> supports bring-your-own-key (BYOK) model providers configured through environment variables. Route it through AI Gateway's <a href="/ai-gateway/usage/rest-api/">REST API</a>, an OpenAI-compatible <code>/chat/completions</code> endpoint authenticated with a Cloudflare API token. Third-party models are billed through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>, so no provider API keys are needed in your environment. Alternatively, you can store your own provider API keys in AI Gateway with <a href="/ai-gateway/configuration/bring-your-own-keys/">BYOK (Store Keys)</a> and use the same Cloudflare API token to authenticate — AI Gateway resolves the stored key on each request.</p>
<p>Unlike <a href="/ai-gateway/integrations/coding-agents/claude-code/">Claude Code</a>, GitHub Copilot CLI authenticates the model provider with a single <code>Authorization</code> header and cannot send custom request headers. This is why the configuration uses the REST API — it accepts a Cloudflare API token in the standard <code>Authorization</code> header — rather than the gateway token and <code>cf-aig-authorization</code> header flow used for Claude Code. Because Copilot CLI cannot set the <code>cf-aig-gateway-id</code> header either, requests route through your account's <a href="/ai-gateway/usage/rest-api/#specify-a-gateway">default gateway</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, you need:</p>
<ul>
<li>GitHub Copilot CLI installed. To install it, refer to <a href="https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli">Installing GitHub Copilot CLI</a>.</li>
<li>A <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with <code>AI Gateway</code> permission.</li>
<li><a href="/ai-gateway/features/unified-billing/#load-credits">Credits loaded</a> on your account for third-party models.</li>
<li>A model that supports tool calling and streaming. For best results, use a model with a context window of at least 128k tokens.</li>
</ul>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2922.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2918.md")
</aside>
<p>To confirm traffic reaches AI Gateway, refer to <a href="/ai-gateway/integrations/coding-agents/#verify-it-works">Verify it works</a>.</p>
