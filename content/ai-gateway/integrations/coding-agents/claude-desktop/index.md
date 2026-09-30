<p>By pointing <a href="https://claude.ai/download">Claude Desktop</a> at AI Gateway instead of Anthropic directly, you get observability, caching, and centralized credentials for your Anthropic requests, without changing how you use Claude Desktop. Claude Desktop can send third-party inference requests to a custom gateway; this configuration sends those requests to AI Gateway's <a href="/ai-gateway/usage/providers/anthropic/">Anthropic endpoint</a>, authenticated with your Cloudflare gateway token. AI Gateway can supply the Anthropic credentials for you through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> or a <a href="/ai-gateway/configuration/bring-your-own-keys/">stored provider key (BYOK)</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, you need:</p>
<ul>
<li>An <a href="/ai-gateway/configuration/authentication/">authenticated gateway</a> and its <a href="/ai-gateway/configuration/authentication/#setting-up-authenticated-gateway-using-the-dashboard">gateway token</a>. The gateway token must have <code>Run</code> permissions.</li>
<li>Your Cloudflare account ID. To find it, refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find your account and zone IDs</a>.</li>
<li>Credentials for Anthropic requests. Use either <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> credits or an Anthropic API key stored in AI Gateway as a <a href="/ai-gateway/configuration/bring-your-own-keys/">provider key (BYOK)</a>.</li>
<li>Claude Desktop installed and updated to the latest version.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2923.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2924.md")
</div>
<p>To confirm traffic reaches AI Gateway, refer to <a href="/ai-gateway/integrations/coding-agents/#verify-it-works">Verify it works</a>.</p>
