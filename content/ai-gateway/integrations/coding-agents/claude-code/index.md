---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-code/
  description: Route Claude Code through AI Gateway using your Cloudflare gateway token.
  full_title: Claude Code · Cloudflare AI Gateway docs
  head_html: <title>Claude Code · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Claude Code through AI Gateway using your Cloudflare gateway token."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-code/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-code/index.md"><meta property="og:title" content="Claude Code · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Claude Code through AI Gateway using your Cloudflare gateway token."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-code/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-code/#page","headline":"Claude Code \u00b7 Cloudflare AI Gateway docs","description":"Route Claude Code through AI Gateway using your Cloudflare gateway token.","url":"https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-code/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/integrations/coding-agents/claude-code/
  schema: 1
---
<p>By pointing <a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code</a> at AI Gateway instead of a provider directly, you get observability, caching, rate limiting, and centralized credentials for Anthropic, Amazon Bedrock, or Google Vertex AI, without changing how you invoke <code>claude</code>. Claude Code reads its endpoint and credentials from environment variables. If your gateway is protected by Cloudflare Access, refer to <a href="#use-with-cloudflare-access">Use with Cloudflare Access</a>. This configuration sends requests to AI Gateway's <a href="/ai-gateway/usage/providers/anthropic/">Anthropic endpoint</a>, authenticated with your Cloudflare gateway token. The Anthropic endpoint exposes the same <code>/v1/messages</code> API that Claude Code expects. When AI Gateway supplies the Anthropic credentials for you — using either an Anthropic API key you <a href="/ai-gateway/configuration/bring-your-own-keys/">store as a provider key (BYOK)</a> or <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> credits — the <code>ANTHROPIC_API_KEY</code> that Claude Code requires can be any placeholder value.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, you need:</p>
<ul>
<li>An <a href="/ai-gateway/configuration/authentication/">authenticated gateway</a> and its <a href="/ai-gateway/configuration/authentication/#setting-up-authenticated-gateway-using-the-dashboard">gateway token</a>. The gateway token must have <code>Run</code> permissions.</li>
<li>Your Cloudflare account ID. To find it, refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find your account and zone IDs</a>.</li>
<li>Credentials for the provider you route to:
<ul>
<li><strong>Anthropic</strong>: Either <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> credits loaded on your Cloudflare account (Cloudflare bills you), or your own Anthropic API key (Anthropic bills you). You can provide your own key either by storing it in AI Gateway as a <a href="/ai-gateway/configuration/bring-your-own-keys/">provider key (BYOK)</a> or by passing it directly in <code>ANTHROPIC_API_KEY</code>.</li>
<li><strong>Amazon Bedrock</strong> or <strong>Google Vertex AI</strong>: your provider credentials stored in AI Gateway as a <a href="/ai-gateway/configuration/bring-your-own-keys/">provider key (BYOK)</a>.</li>
</ul>
</li>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/setup">Claude Code</a> installed and updated to the latest version.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2925.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2929.md")
</div>
<h2 id="use-amazon-bedrock">Use Amazon Bedrock</h2>
<p>To run Claude models through <a href="/ai-gateway/usage/providers/bedrock/">Amazon Bedrock</a> instead, point Claude Code at your gateway's Amazon Bedrock endpoint. AI Gateway authenticates to Bedrock with the AWS credentials you <a href="/ai-gateway/configuration/bring-your-own-keys/">store as a provider key</a>, so you can skip Claude Code's own AWS authentication.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2933.md")
</div>
<h2 id="use-google-vertex-ai">Use Google Vertex AI</h2>
<p>To run Claude models through <a href="/ai-gateway/usage/providers/vertex/">Google Vertex AI</a> instead, point Claude Code at your gateway's Google Vertex AI endpoint. AI Gateway authenticates to Vertex AI with the Google Cloud credentials you <a href="/ai-gateway/configuration/bring-your-own-keys/">store as a provider key</a>, so you can skip Claude Code's own Vertex authentication.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2937.md")
</div>
<h2 id="use-with-cloudflare-access">Use with Cloudflare Access</h2>
<p>If your gateway is protected by <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>, Claude Code can authenticate with a short-lived Access token instead of a gateway token. Point <code>ANTHROPIC_BASE_URL</code> at your <a href="/ai-gateway/configuration/custom-domains/">custom domain</a> and use Claude Code's <code>apiKeyHelper</code> to fetch the token with <a href="/cloudflare-one/access-controls/authenticate-agents/#make-requests-with-cloudflared-access-curl"><code>cloudflared</code></a>. Claude Code sends the token as the API key, and Access verifies it at the edge.</p>
<p>Add the following to Claude Code's <a href="https://docs.anthropic.com/en/docs/claude-code/settings#settings-files"><code>settings.json</code></a>, replacing <code>ai-gateway.example.com</code> with your custom domain:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;apiKeyHelper&quot;: &quot;cloudflared access login --no-verbose https://ai-gateway.example.com&quot;,&#10;	&quot;env&quot;: {&#10;		&quot;ANTHROPIC_BASE_URL&quot;: &quot;https://ai-gateway.example.com/anthropic&quot;&#10;	}&#10;}&#10;</code></pre>
<p>The first request opens your identity provider's login flow. After you authenticate, requests route through AI Gateway with your Access identity attached as <a href="/ai-gateway/observability/custom-metadata/#reserved-metadata"><code>cf.user_id</code></a>.</p>
<p>To confirm traffic reaches AI Gateway, refer to <a href="/ai-gateway/integrations/coding-agents/#verify-it-works">Verify it works</a>.</p>
