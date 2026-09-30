---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/
  description: Route Deepgram speech-to-text and text-to-speech requests through AI Gateway for observability and control.
  full_title: Deepgram · Cloudflare AI Gateway docs
  head_html: <title>Deepgram · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Deepgram speech-to-text and text-to-speech requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/index.md"><meta property="og:title" content="Deepgram · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Deepgram speech-to-text and text-to-speech requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/#page","headline":"Deepgram \u00b7 Cloudflare AI Gateway docs","description":"Route Deepgram speech-to-text and text-to-speech requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/deepgram/
  schema: 1
---
<p><a href="https://developers.deepgram.com/home">Deepgram</a> provides Voice AI APIs for speech-to-text, text-to-speech, and voice agents.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2980.md")
</aside>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram&#10;</code></pre>
<h2 id="url-structure">URL Structure</h2>
<p>When making requests to Deepgram, replace <code>https://api.deepgram.com/</code> in the URL you are currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram/</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Deepgram, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Deepgram API token.</li>
</ul>
<h2 id="example">Example</h2>
<h3 id="sdk">SDK</h3>
<pre tabindex="0"><code class="language-ts">import { createClient, LiveTranscriptionEvents } from &quot;@deepgram/sdk&quot;;&#10;&#10;&#10;const deepgram = createClient(&quot;{deepgram_api_key}&quot;, {&#10;    global: {&#10;      websocket: {&#10;        options: {&#10;          url: &quot;wss://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram/&quot;,&#10;          _nodeOnlyHeaders: {&#10;            &quot;cf-aig-authorization&quot;: &quot;Bearer {CF_AIG_TOKEN}&quot;&#10;          }&#10;        }&#10;      }&#10;    }&#10;});&#10;&#10;&#10;const connection = deepgram.listen.live({&#10;    model: &quot;nova-3&quot;,&#10;    language: &quot;en-US&quot;,&#10;    smart_format: true,&#10;});&#10;&#10;connection.send(...);&#10;</code></pre>
