---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/
  description: Route the Pi coding agent through AI Gateway using its built-in Cloudflare AI Gateway provider.
  full_title: Pi · Cloudflare AI Gateway docs
  head_html: <title>Pi · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route the Pi coding agent through AI Gateway using its built-in Cloudflare AI Gateway provider."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/index.md"><meta property="og:title" content="Pi · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route the Pi coding agent through AI Gateway using its built-in Cloudflare AI Gateway provider."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/#page","headline":"Pi \u00b7 Cloudflare AI Gateway docs","description":"Route the Pi coding agent through AI Gateway using its built-in Cloudflare AI Gateway provider.","url":"https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/integrations/coding-agents/pi/
  schema: 1
---
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
