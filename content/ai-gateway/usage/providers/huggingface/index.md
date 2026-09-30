---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/
  description: Route HuggingFace Inference API requests through AI Gateway for observability and control.
  full_title: HuggingFace · Cloudflare AI Gateway docs
  head_html: <title>HuggingFace · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route HuggingFace Inference API requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/index.md"><meta property="og:title" content="HuggingFace · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route HuggingFace Inference API requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/#page","headline":"HuggingFace \u00b7 Cloudflare AI Gateway docs","description":"Route HuggingFace Inference API requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/huggingface/
  schema: 1
---
<p><a href="https://huggingface.co/">HuggingFace</a> helps users build, deploy and train machine learning models.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface&#10;</code></pre>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to HuggingFace Inference API, replace <code>https://api-inference.huggingface.co/models/</code> in the URL you're currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface</code>. Note that the model you're trying to access should come right after, for example <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface/bigcode/starcoder</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to HuggingFace, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active HuggingFace API token.</li>
<li>The name of the HuggingFace model you want to use.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface/bigcode/starcoder \&#10;  &#45;-header &#x27;Authorization: Bearer {hf_api_token}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;inputs&quot;: &quot;console.log&quot;&#10;}&#x27;&#10;</code></pre>
<h3 id="use-huggingface-js-library-with-javascript">Use HuggingFace.js library with JavaScript</h3>
<p>If you are using the HuggingFace.js library, you can set your inference endpoint like this:</p>
<pre tabindex="0"><code class="language-js">import { HfInferenceEndpoint } from &quot;@huggingface/inference&quot;;&#10;&#10;const accountId = &quot;{account_id}&quot;;&#10;const gatewayId = &quot;{gateway_id}&quot;;&#10;const model = &quot;gpt2&quot;;&#10;const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/huggingface/${model}`;&#10;const apiToken = env.HF_API_TOKEN;&#10;&#10;const hf = new HfInferenceEndpoint(baseURL, apiToken);&#10;</code></pre>
