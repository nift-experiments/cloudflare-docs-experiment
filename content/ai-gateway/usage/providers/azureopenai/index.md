---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/
  description: Route Azure OpenAI requests through AI Gateway for observability and control.
  full_title: Azure OpenAI · Cloudflare AI Gateway docs
  head_html: <title>Azure OpenAI · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Azure OpenAI requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/index.md"><meta property="og:title" content="Azure OpenAI · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Azure OpenAI requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/#page","headline":"Azure OpenAI \u00b7 Cloudflare AI Gateway docs","description":"Route Azure OpenAI requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/azureopenai/
  schema: 1
---
<p><a href="https://azure.microsoft.com/en-gb/products/ai-services/openai-service/">Azure OpenAI</a> allows you apply natural language algorithms on your data.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/azure-openai/{resource_name}/{deployment_name}&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Azure OpenAI, you will need:</p>
<ul>
<li>AI Gateway account ID</li>
<li>AI Gateway gateway name</li>
<li>Azure OpenAI API key</li>
<li>Azure OpenAI resource name</li>
<li>Azure OpenAI deployment name (aka model name)</li>
</ul>
<h2 id="url-structure">URL structure</h2>
<p>Your new base URL will use the data above in this structure: <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/azure-openai/{resource_name}/{deployment_name}</code>. Then, you can append your endpoint and api-version at the end of the base URL, like <code>.../chat/completions?api-version=2023-05-15</code>.</p>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl &#x27;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway}/azure-openai/{resource_name}/{deployment_name}/chat/completions?api-version=2023-05-15&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;api-key: {azure_api_key}&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;messages&quot;: [&#10;    {&#10;      &quot;role&quot;: &quot;user&quot;,&#10;      &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<h3 id="use-openai-javascript-sdk">Use <code>openai</code> JavaScript SDK</h3>
<pre tabindex="0"><code class="language-js">import { AzureOpenAI } from &quot;openai&quot;;&#10;&#10;const azure_openai = new AzureOpenAI({&#10;  apiKey: &quot;{azure_api_key}&quot;,&#10;  baseURL: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway}/azure-openai/{resource_name}/`,&#10;  apiVersion: &quot;2023-05-15&quot;,&#10;  defaultHeaders: { &quot;cf-aig-authorization&quot;: &quot;{cf-api-token}&quot; }, // if authenticated&#10;});&#10;&#10;const result = await azure_openai.chat.completions.create({&#10;  model: &#x27;{deployment_name}&#x27;,&#10;  messages: [{ role: &quot;user&quot;, content: &quot;Hello&quot; }],&#10;});&#10;</code></pre>
