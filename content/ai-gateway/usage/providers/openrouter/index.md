---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/
  description: Route OpenRouter API requests through AI Gateway for observability and control.
  full_title: OpenRouter · Cloudflare AI Gateway docs
  head_html: <title>OpenRouter · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route OpenRouter API requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/index.md"><meta property="og:title" content="OpenRouter · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route OpenRouter API requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/#page","headline":"OpenRouter \u00b7 Cloudflare AI Gateway docs","description":"Route OpenRouter API requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/openrouter/
  schema: 1
---
<p><a href="https://openrouter.ai/">OpenRouter</a> is a platform that provides a unified interface for accessing and using large language models (LLMs).</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter&#10;</code></pre>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to <a href="https://openrouter.ai/">OpenRouter</a>, replace <code>https://openrouter.ai/api/v1/chat/completions</code> in the URL you are currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter/chat/completions</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to OpenRouter, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active OpenRouter API token or a token from the original model provider.</li>
<li>The name of the OpenRouter model you want to use.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter/v1/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer OPENROUTER_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-5-mini&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<h3 id="use-openai-sdk-with-javascript">Use OpenAI SDK with JavaScript</h3>
<p>If you are using the OpenAI SDK with JavaScript, you can set your endpoint like this:</p>
<pre tabindex="0"><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;&#10;const openai = new OpenAI({&#10;	apiKey: env.OPENROUTER_TOKEN,&#10;	baseURL:&#10;		&quot;https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/openrouter&quot;,&#10;});&#10;&#10;try {&#10;	const chatCompletion = await openai.chat.completions.create({&#10;		model: &quot;openai/gpt-5-mini&quot;,&#10;		messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	});&#10;&#10;	const response = chatCompletion.choices[0].message;&#10;&#10;	return new Response(JSON.stringify(response));&#10;} catch (e) {&#10;	return new Response(e);&#10;}&#10;</code></pre>
