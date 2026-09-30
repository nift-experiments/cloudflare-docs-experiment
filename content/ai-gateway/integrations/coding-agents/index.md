<p>Coding agents send model requests to a provider on your behalf. By pointing the agent at AI Gateway instead of the provider, you observe and control that traffic without changing how you work.</p>
<h2 id="why-route-a-coding-agent-through-ai-gateway">Why route a coding agent through AI Gateway</h2>
<p>Routing a coding agent through AI Gateway gives you:</p>
<ul>
<li><strong>Observability</strong> — view every request, token count, and latency in the dashboard.</li>
<li><strong>Caching</strong> — return <a href="/ai-gateway/features/caching/">cached responses</a> for repeated prompts.</li>
<li><strong>Rate limiting</strong> — cap request volume with <a href="/ai-gateway/features/rate-limiting/">rate limiting</a>.</li>
<li><strong>Cost tracking</strong> — attribute spend across sessions and models.</li>
<li><strong>Data Loss Prevention</strong> — scan prompts and responses for secrets, credentials, and other sensitive data with <a href="/ai-gateway/features/dlp/">DLP</a>.</li>
</ul>
<h2 id="set-up-your-agent">Set up your agent</h2>
<p>Follow the setup guide for your coding agent:</p>
<ul>
<li><a href="/ai-gateway/integrations/coding-agents/claude-code/">Claude Code</a></li>
<li><a href="/ai-gateway/integrations/coding-agents/claude-desktop/">Claude Desktop</a></li>
<li><a href="/ai-gateway/integrations/coding-agents/github-copilot-cli/">GitHub Copilot CLI</a></li>
<li><a href="/ai-gateway/integrations/coding-agents/openai-codex/">OpenAI Codex</a></li>
<li><a href="/ai-gateway/integrations/coding-agents/opencode/">OpenCode</a></li>
<li><a href="/ai-gateway/integrations/coding-agents/pi/">Pi</a></li>
</ul>
<h2 id="protect-sensitive-code-with-dlp">Protect sensitive code with DLP</h2>
<p>Coding agents routinely send source code, configuration files, and snippets to model providers. That traffic can include API keys, customer data, or other sensitive material. Because AI Gateway sits between the agent and the provider, you can inspect and control it without changing the agent.</p>
<p><a href="/ai-gateway/features/dlp/">Data Loss Prevention (DLP)</a> scans request and response bodies against <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">detection profiles</a> and either flags or blocks matches. Use it to catch secrets, credentials, or regulated data leaving (or returning to) the agent.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2916.md")
</aside>
<h2 id="verify-it-works">Verify it works</h2>
<p>After you configure a tool, confirm that traffic reaches AI Gateway.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2917.md")
</div>
<p>For more information on logs, refer to <a href="/ai-gateway/observability/logging/">Logging</a>.</p>
