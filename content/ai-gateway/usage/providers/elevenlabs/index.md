---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/
  description: Route ElevenLabs text-to-speech requests through AI Gateway for observability and control.
  full_title: ElevenLabs · Cloudflare AI Gateway docs
  head_html: <title>ElevenLabs · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route ElevenLabs text-to-speech requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/index.md"><meta property="og:title" content="ElevenLabs · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route ElevenLabs text-to-speech requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/#page","headline":"ElevenLabs \u00b7 Cloudflare AI Gateway docs","description":"Route ElevenLabs text-to-speech requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/elevenlabs/
  schema: 1
---
<p><a href="https://elevenlabs.io/">ElevenLabs</a> offers advanced text-to-speech services, enabling high-quality voice synthesis in multiple languages.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/elevenlabs&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to ElevenLabs, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active ElevenLabs API token.</li>
<li>The model ID of the ElevenLabs voice model you want to use.</li>
</ul>
<h2 id="example">Example</h2>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/elevenlabs/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128 \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;xi-api-key: {elevenlabs_api_token}&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;text&quot;: &quot;Welcome to Cloudflare - AI Gateway!&quot;,&#10;    &quot;model_id&quot;: &quot;eleven_multilingual_v2&quot;&#10;}&#x27;&#10;</code></pre>
