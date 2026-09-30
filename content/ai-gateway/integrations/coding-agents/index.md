---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/
  description: Route Claude Code, Claude Desktop, GitHub Copilot CLI, OpenAI Codex, OpenCode, and Pi through AI Gateway for observability, caching, rate limiting, and cost tracking.
  full_title: Coding agents · Cloudflare AI Gateway docs
  head_html: <title>Coding agents · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Claude Code, Claude Desktop, GitHub Copilot CLI, OpenAI Codex, OpenCode, and Pi through AI Gateway for observability, caching, rate limiting, and cost tracking."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/index.md"><meta property="og:title" content="Coding agents · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Claude Code, Claude Desktop, GitHub Copilot CLI, OpenAI Codex, OpenCode, and Pi through AI Gateway for observability, caching, rate limiting, and cost tracking."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/#page","headline":"Coding agents \u00b7 Cloudflare AI Gateway docs","description":"Route Claude Code, Claude Desktop, GitHub Copilot CLI, OpenAI Codex, OpenCode, and Pi through AI Gateway for observability, caching, rate limiting, and cost tracking.","url":"https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/integrations/coding-agents/
  schema: 1
---
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
