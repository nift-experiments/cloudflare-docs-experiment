---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/groq/
  description: Route Groq API requests through AI Gateway for observability and control.
  full_title: Groq · Cloudflare AI Gateway docs
  head_html: <title>Groq · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Groq API requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/groq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/groq/index.md"><meta property="og:title" content="Groq · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Groq API requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/groq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/groq/#page","headline":"Groq \u00b7 Cloudflare AI Gateway docs","description":"Route Groq API requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/groq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/groq/
  schema: 1
---
<p><a href="https://groq.com/">Groq</a> delivers high-speed processing and low-latency performance.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/groq&#10;</code></pre>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to <a href="https://groq.com/">Groq</a>, replace <code>https://api.groq.com/openai/v1</code> in the URL you're currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/groq</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Groq, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Groq API token.</li>
<li>The name of the Groq model you want to use.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/groq/chat/completions \&#10;  &#45;-header &#x27;Authorization: Bearer {groq_api_key}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ],&#10;    &quot;model&quot;: &quot;llama3-8b-8192&quot;&#10;}&#x27;&#10;</code></pre>
<h3 id="use-groq-sdk-with-javascript">Use Groq SDK with JavaScript</h3>
<p>If using the <a href="https://www.npmjs.com/package/groq-sdk"><code>groq-sdk</code></a>, set your endpoint like this:</p>
<pre tabindex="0"><code class="language-js">import Groq from &quot;groq-sdk&quot;;&#10;&#10;const apiKey = env.GROQ_API_KEY;&#10;const accountId = &quot;{account_id}&quot;;&#10;const gatewayId = &quot;{gateway_id}&quot;;&#10;const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/groq`;&#10;&#10;const groq = new Groq({&#10;	apiKey,&#10;	baseURL,&#10;});&#10;&#10;const messages = [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }];&#10;const model = &quot;llama3-8b-8192&quot;;&#10;&#10;const chatCompletion = await groq.chat.completions.create({&#10;	messages,&#10;	model,&#10;});&#10;</code></pre>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access Groq models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&amp;quot;model&amp;quot;: &amp;quot;groq/{model}&amp;quot;&#10;}</code></pre>
