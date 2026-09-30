---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/
  description: Route OpenCode model requests through AI Gateway using a gateway token or an Access-protected custom domain.
  full_title: OpenCode · Cloudflare AI Gateway docs
  head_html: <title>OpenCode · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route OpenCode model requests through AI Gateway using a gateway token or an Access-protected custom domain."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/index.md"><meta property="og:title" content="OpenCode · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route OpenCode model requests through AI Gateway using a gateway token or an Access-protected custom domain."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/#page","headline":"OpenCode \u00b7 Cloudflare AI Gateway docs","description":"Route OpenCode model requests through AI Gateway using a gateway token or an Access-protected custom domain.","url":"https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/integrations/coding-agents/opencode/
  schema: 1
---
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
