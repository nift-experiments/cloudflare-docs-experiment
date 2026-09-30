---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/
  description: Route DeepSeek API requests through AI Gateway for observability and control.
  full_title: DeepSeek · Cloudflare AI Gateway docs
  head_html: <title>DeepSeek · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route DeepSeek API requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/index.md"><meta property="og:title" content="DeepSeek · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route DeepSeek API requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/#page","headline":"DeepSeek \u00b7 Cloudflare AI Gateway docs","description":"Route DeepSeek API requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/deepseek/
  schema: 1
---
<p><a href="https://www.deepseek.com/">DeepSeek</a> helps you build quickly with DeepSeek's advanced AI models.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to DeepSeek, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active DeepSeek AI API token.</li>
<li>The name of the DeepSeek AI model you want to use.</li>
</ul>
<h2 id="url-structure">URL structure</h2>
<p>Your new base URL will use the data above in this structure:</p>
<p><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/</code>.</p>
<p>You can then append the endpoint you want to hit, for example: <code>chat/completions</code>.</p>
<p>So your final URL will come together as:</p>
<p><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions</code>.</p>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer DEEPSEEK_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;deepseek-chat&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<h3 id="use-deepseek-with-javascript">Use DeepSeek with JavaScript</h3>
<p>If you are using the OpenAI SDK, you can set your endpoint like this:</p>
<pre tabindex="0"><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;&#10;const openai = new OpenAI({&#10;	apiKey: env.DEEPSEEK_TOKEN,&#10;	baseURL:&#10;		&quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek&quot;,&#10;});&#10;&#10;try {&#10;	const chatCompletion = await openai.chat.completions.create({&#10;		model: &quot;deepseek-chat&quot;,&#10;		messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	});&#10;&#10;	const response = chatCompletion.choices[0].message;&#10;&#10;	return new Response(JSON.stringify(response));&#10;} catch (e) {&#10;	return new Response(e);&#10;}&#10;</code></pre>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access DeepSeek models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&amp;quot;model&amp;quot;: &amp;quot;deepseek/{model}&amp;quot;&#10;}</code></pre>
