<p><a href="https://pi.dev">Pi</a> is a coding agent you run in your terminal. It has built-in support for AI Gateway, so instead of setting a base URL you select the <code>cloudflare-ai-gateway</code> provider and point Pi at your gateway. Pi builds the gateway endpoint from your account ID and gateway slug and routes requests through it.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, you need:</p>
<ul>
<li>An <a href="/ai-gateway/configuration/authentication/">authenticated gateway</a> and its <a href="/ai-gateway/configuration/authentication/#setting-up-authenticated-gateway-using-the-dashboard">gateway token</a>. The gateway token must have <code>Run</code> permissions.</li>
<li>Your Cloudflare account ID. To find it, refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find your account and zone IDs</a>.</li>
<li>Pi installed and updated to the latest version.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2898.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2902.md")
</div>
<p>To confirm traffic reaches AI Gateway, refer to <a href="/ai-gateway/integrations/coding-agents/#verify-it-works">Verify it works</a>.</p>
