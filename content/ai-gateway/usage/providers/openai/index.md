---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/openai/
  description: Route OpenAI API requests through AI Gateway for observability and control.
  full_title: OpenAI · Cloudflare AI Gateway docs
  head_html: <title>OpenAI · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route OpenAI API requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/openai/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/openai/index.md"><meta property="og:title" content="OpenAI · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route OpenAI API requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/openai/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/openai/#page","headline":"OpenAI \u00b7 Cloudflare AI Gateway docs","description":"Route OpenAI API requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/openai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/openai/
  schema: 1
---
<p><a href="https://openai.com/about/">OpenAI</a> helps you build with GPT models.</p>
<h2 id="endpoint">Endpoint</h2>
<p><strong>Base URL</strong></p>
<pre tabindex="0"><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai&#10;</code></pre>
<p>When making requests to OpenAI, replace <code>https://api.openai.com/v1</code> in the URL you are currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai</code>.</p>
<p><strong>Chat completions endpoint</strong></p>
<p><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions</code></p>
<p><strong>Responses endpoint</strong></p>
<p><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses</code></p>
<h2 id="examples">Examples</h2>
<h3 id="openai-sdk">OpenAI SDK</h3>
<details class="nb-details"><summary>With Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2958.md")
</div></details>
<details class="nb-details" open><summary>With Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2959.md")
</div></details>
<h3 id="curl">cURL</h3>
<details class="nb-details"><summary>Responses API with API Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2963.md")
</div></details>
<details class="nb-details"><summary>Chat Completions with API Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2967.md")
</div></details>
<details class="nb-details"><summary>Responses API with Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2968.md")
</div></details>
<details class="nb-details" open><summary>Chat Completions with Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2969.md")
</div></details>
