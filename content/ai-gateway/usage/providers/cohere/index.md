---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/
  description: Route Cohere API requests through AI Gateway for observability and control.
  full_title: Cohere · Cloudflare AI Gateway docs
  head_html: <title>Cohere · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Cohere API requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/index.md"><meta property="og:title" content="Cohere · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Cohere API requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/#page","headline":"Cohere \u00b7 Cloudflare AI Gateway docs","description":"Route Cohere API requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/cohere/
  schema: 1
---
<p><a href="https://cohere.com/">Cohere</a> build AI models designed to solve real-world business challenges.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cohere&#10;</code></pre>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to <a href="https://cohere.com/">Cohere</a>, replace <code>https://api.cohere.ai/v1</code> in the URL you're currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cohere</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Cohere, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Cohere API token.</li>
<li>The name of the Cohere model you want to use.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cohere/v1/chat \&#10;  &#45;-header &#x27;Authorization: Token {cohere_api_token}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;chat_history&quot;: [&#10;    {&quot;role&quot;: &quot;USER&quot;, &quot;message&quot;: &quot;Who discovered gravity?&quot;},&#10;    {&quot;role&quot;: &quot;CHATBOT&quot;, &quot;message&quot;: &quot;The man who is widely credited with discovering gravity is Sir Isaac Newton&quot;}&#10;  ],&#10;  &quot;message&quot;: &quot;What year was he born?&quot;,&#10;  &quot;connectors&quot;: [{&quot;id&quot;: &quot;web-search&quot;}]&#10;}&#x27;&#10;</code></pre>
<h3 id="use-cohere-sdk-with-python">Use Cohere SDK with Python</h3>
<p>If using the <a href="https://github.com/cohere-ai/cohere-python"><code>cohere-python-sdk</code></a>, set your endpoint like this:</p>
<pre tabindex="0"><code class="language-js">&#10;import cohere&#10;import os&#10;&#10;api_key = os.getenv(&#x27;API_KEY&#x27;)&#10;account_id = &#x27;{account_id}&#x27;&#10;gateway_id = &#x27;{gateway_id}&#x27;&#10;base_url = f&quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cohere/v1&quot;&#10;&#10;co = cohere.Client(&#10;  api_key=api_key,&#10;  base_url=base_url,&#10;)&#10;&#10;message = &quot;hello world!&quot;&#10;model = &quot;command-r-plus&quot;&#10;&#10;chat = co.chat(&#10;  message=message,&#10;  model=model&#10;)&#10;&#10;print(chat)&#10;</code></pre>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access Cohere models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&amp;quot;model&amp;quot;: &amp;quot;cohere/{model}&amp;quot;&#10;}</code></pre>
