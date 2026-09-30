---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/
  description: Route Cartesia text-to-speech requests through AI Gateway for observability and control.
  full_title: Cartesia · Cloudflare AI Gateway docs
  head_html: <title>Cartesia · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Cartesia text-to-speech requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/index.md"><meta property="og:title" content="Cartesia · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Cartesia text-to-speech requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/#page","headline":"Cartesia \u00b7 Cloudflare AI Gateway docs","description":"Route Cartesia text-to-speech requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/cartesia/
  schema: 1
---
<p><a href="https://docs.cartesia.ai/">Cartesia</a> provides advanced text-to-speech services with customizable voice models.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia&#10;</code></pre>
<h2 id="url-structure">URL Structure</h2>
<p>When making requests to Cartesia, replace <code>https://api.cartesia.ai/v1</code> in the URL you are currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Cartesia, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Cartesia API token.</li>
<li>The model ID and voice ID for the Cartesia voice model you want to use.</li>
</ul>
<h2 id="example">Example</h2>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia/tts/bytes \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;Cartesia-Version: 2024-06-10&#x27; \&#10;  &#45;-header &#x27;X-API-Key: {cartesia_api_token}&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;transcript&quot;: &quot;Welcome to Cloudflare - AI Gateway!&quot;,&#10;    &quot;model_id&quot;: &quot;sonic-english&quot;,&#10;    &quot;voice&quot;: {&#10;        &quot;mode&quot;: &quot;id&quot;,&#10;        &quot;id&quot;: &quot;694f9389-aac1-45b6-b726-9d9369183238&quot;&#10;    },&#10;    &quot;output_format&quot;: {&#10;        &quot;container&quot;: &quot;wav&quot;,&#10;        &quot;encoding&quot;: &quot;pcm_f32le&quot;,&#10;        &quot;sample_rate&quot;: 44100&#10;    }&#10;}&#10;</code></pre>
