---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/
  description: Route Replicate API requests through AI Gateway for observability and control.
  full_title: Replicate · Cloudflare AI Gateway docs
  head_html: <title>Replicate · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Replicate API requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/index.md"><meta property="og:title" content="Replicate · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Replicate API requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/#page","headline":"Replicate \u00b7 Cloudflare AI Gateway docs","description":"Route Replicate API requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/replicate/
  schema: 1
---
<p><a href="https://replicate.com/">Replicate</a> runs and fine tunes open-source models.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate&#10;</code></pre>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to Replicate, replace <code>https://api.replicate.com/v1</code> in the URL you're currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Replicate, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Replicate API token. You can create one at <a href="https://replicate.com/account/api-tokens">replicate.com/account/api-tokens</a></li>
<li>The name of the Replicate model you want to use, like <code>anthropic/claude-4.5-haiku</code> or <code>google/nano-banana</code>.</li>
</ul>
<h2 id="example">Example</h2>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate/predictions \&#10;  &#45;-header &#x27;Authorization: Bearer {replicate_api_token}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;version&quot;: &quot;anthropic/claude-4.5-haiku&quot;,&#10;    &quot;input&quot;:&#10;      {&#10;        &quot;prompt&quot;: &quot;Write a haiku about Cloudflare&quot;&#10;      }&#10;    }&#x27;&#10;</code></pre>
