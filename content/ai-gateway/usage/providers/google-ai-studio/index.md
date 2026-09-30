---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/
  description: Route Google AI Studio and Gemini requests through AI Gateway for observability and control.
  full_title: Google AI Studio · Cloudflare AI Gateway docs
  head_html: <title>Google AI Studio · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Google AI Studio and Gemini requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/index.md"><meta property="og:title" content="Google AI Studio · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Google AI Studio and Gemini requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/#page","headline":"Google AI Studio \u00b7 Cloudflare AI Gateway docs","description":"Route Google AI Studio and Gemini requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/google-ai-studio/
  schema: 1
---
<p><a href="https://ai.google.dev/aistudio">Google AI Studio</a> helps you build quickly with Google Gemini models.</p>
<h2 id="endpoint">Endpoint</h2>
<p><strong>Base URL:</strong></p>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-ai-studio&#10;</code></pre>
<p>Then you can append the endpoint you want to hit, for example: <code>v1/models/{model}:{generative_ai_rest_resource}</code></p>
<p>So your final URL will come together as: <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-ai-studio/v1/models/{model}:{generative_ai_rest_resource}</code>.</p>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<details class="nb-details"><summary>With API Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2973.md")
</div></details>
<details class="nb-details" open><summary>With Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2974.md")
</div></details>
<h3 id="google-genai"><code>@google/genai</code></h3>
<p>If you are using the <code>@google/genai</code> package, you can set your endpoint like this:</p>
<details class="nb-details"><summary>With Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2978.md")
</div></details>
<details class="nb-details" open><summary>With Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2979.md")
</div></details>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access Google AI Studio models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&amp;quot;model&amp;quot;: &amp;quot;google-ai-studio/{model}&amp;quot;&#10;}</code></pre>
