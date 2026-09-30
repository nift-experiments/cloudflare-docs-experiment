<p><a href="https://opencode.ai/">OpenCode</a> is an open source coding agent that supports custom provider configuration. Point its built-in providers at AI Gateway to observe and control model requests from OpenCode.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2904.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, you need:</p>
<ul>
<li>An AI Gateway and its gateway slug.</li>
<li><a href="/ai-gateway/features/unified-billing/#load-credits">Sufficient Unified Billing credits</a> or a stored <a href="/ai-gateway/configuration/bring-your-own-keys/">provider key</a> with the <code>default</code> alias for each provider.</li>
<li><a href="https://opencode.ai/docs/">OpenCode installed</a>.</li>
</ul>
<h2 id="connect-with-a-gateway-token">Connect with a gateway token</h2>
<p>To use this method, you also need an <a href="/ai-gateway/configuration/authentication/">authenticated gateway</a> and its gateway token. The token must have <code>Run</code> permissions. You also need your Cloudflare account ID. To find it, refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find your account and zone IDs</a>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2908.md")
</div>
<p>To confirm traffic reaches AI Gateway, refer to <a href="/ai-gateway/integrations/coding-agents/#verify-it-works">Verify it works</a>.</p>
<h2 id="use-with-cloudflare-access">Use with Cloudflare Access</h2>
<p>If your gateway is protected by <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>, OpenCode can authenticate with a short-lived Access token instead of a gateway token. You can also host the configuration centrally so users connect with one login command.</p>
<p>This setup requires an AI Gateway <a href="/ai-gateway/configuration/custom-domains/">custom domain</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/"><code>cloudflared</code></a> on each user's device, and a public HTTPS location for two configuration files. You can use an <a href="/r2/buckets/public-buckets/#custom-domains">R2 bucket with a custom domain</a>.</p>
<p>The files contain configuration, but no credentials. A Single Redirect sends <code>/.well-known/opencode</code> requests from your AI Gateway custom domain to the discovery file.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2903.md")
</aside>
<p>Users can override remote configuration in their global or project configuration. To enforce organization-wide settings, refer to <a href="https://opencode.ai/docs/config/#managed-settings">OpenCode managed settings</a>.</p>
<p>The following example uses <code>ai.example.com</code> for the AI Gateway domain and <code>config.example.com</code> for the configuration host. Replace both hostnames with your own values.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2909.md")
</div>
