---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/
  description: Route Mistral AI requests through AI Gateway for observability and control.
  full_title: Mistral AI · Cloudflare AI Gateway docs
  head_html: <title>Mistral AI · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Mistral AI requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/index.md"><meta property="og:title" content="Mistral AI · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Mistral AI requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/#page","headline":"Mistral AI \u00b7 Cloudflare AI Gateway docs","description":"Route Mistral AI requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/mistral/
  schema: 1
---
<p><a href="https://mistral.ai">Mistral AI</a> helps you build quickly with Mistral's advanced AI models.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to the Mistral AI, you will need:</p>
<ul>
<li>AI Gateway Account ID</li>
<li>AI Gateway gateway name</li>
<li>Mistral AI API token</li>
<li>Mistral AI model name</li>
</ul>
<h2 id="url-structure">URL structure</h2>
<p>Your new base URL will use the data above in this structure: <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral/</code>.</p>
<p>Then you can append the endpoint you want to hit, for example: <code>v1/chat/completions</code></p>
<p>So your final URL will come together as: <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral/v1/chat/completions</code>.</p>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral/v1/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer MISTRAL_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;mistral-large-latest&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<h3 id="use-mistralai-mistralai-package-with-javascript">Use <code>@mistralai/mistralai</code> package with JavaScript</h3>
<p>If you are using the <code>@mistralai/mistralai</code> package, you can set your endpoint like this:</p>
<pre tabindex="0"><code class="language-js">import { Mistral } from &quot;@mistralai/mistralai&quot;;&#10;&#10;const client = new Mistral({&#10;	apiKey: MISTRAL_TOKEN,&#10;	serverURL: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral`,&#10;});&#10;&#10;await client.chat.create({&#10;	model: &quot;mistral-large-latest&quot;,&#10;	messages: [&#10;		{&#10;			role: &quot;user&quot;,&#10;			content: &quot;What is Cloudflare?&quot;,&#10;		},&#10;	],&#10;});&#10;</code></pre>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access Mistral models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&amp;quot;model&amp;quot;: &amp;quot;mistral/{model}&amp;quot;&#10;}</code></pre>
