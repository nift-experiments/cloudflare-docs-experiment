---
cp9:
  canonical: https://developers.cloudflare.com/workers/configuration/integrations/apis/
  description: Integrate Cloudflare Workers with third-party APIs using the Fetch API.
  full_title: APIs · Cloudflare Workers docs
  head_html: <title>APIs · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Cloudflare Workers with third-party APIs using the Fetch API."><link rel="canonical" href="https://developers.cloudflare.com/workers/configuration/integrations/apis/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/integrations/apis/index.md"><meta property="og:title" content="APIs · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Cloudflare Workers with third-party APIs using the Fetch API."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/integrations/apis/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/configuration/integrations/apis/#page","headline":"APIs \u00b7 Cloudflare Workers docs","description":"Integrate Cloudflare Workers with third-party APIs using the Fetch API.","url":"https://developers.cloudflare.com/workers/configuration/integrations/apis/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/integrations/apis/
  schema: 1
---
<p>To integrate with third party APIs from Cloudflare Workers, use the <a href="/workers/runtime-apis/fetch/">fetch API</a> to make HTTP requests to the API endpoint. Then use the response data to modify or manipulate your content as needed.</p>
<p>For example, if you want to integrate with a weather API, make a fetch request to the API endpoint and retrieve the current weather data. Then use this data to display the current weather conditions on your website.</p>
<p>To make the <code>fetch()</code> request, add the following code to your project's <code>src/index.js</code> file:</p>
<pre tabindex="0"><code class="language-js">async function handleRequest(request) {&#10;	// Make the fetch request to the third party API endpoint&#10;	const response = await fetch(&quot;https://weather-api.com/endpoint&quot;, {&#10;		method: &quot;GET&quot;,&#10;		headers: {&#10;			&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;		},&#10;	});&#10;&#10;	// Retrieve the data from the response&#10;	const data = await response.json();&#10;&#10;	// Use the data to modify or manipulate your content as needed&#10;	return new Response(data);&#10;}&#10;</code></pre>
<h2 id="authentication">Authentication</h2>
<p>If your API requires authentication, use Wrangler secrets to securely store your credentials. To do this, create a secret in your Cloudflare Workers project using the following <a href="/workers/wrangler/commands/general/#secret"><code>wrangler secret</code></a> command:</p>
<pre tabindex="0"><code class="language-sh">wrangler secret put SECRET_NAME&#10;</code></pre>
<p>Then, retrieve the secret value in your code using the following code snippet:</p>
<pre tabindex="0"><code class="language-js">const secretValue = env.SECRET_NAME;&#10;</code></pre>
<p>Then use the secret value to authenticate with the external service. For example, if the external service requires an API key for authentication, include it in your request headers.</p>
<p>For services that require mTLS authentication, use <a href="/workers/runtime-apis/bindings/mtls">mTLS certificates</a> to present a client certificate.</p>
<h2 id="tips">Tips</h2>
<ul>
<li>
<p>Use the <a href="/workers/runtime-apis/cache/">Cache API</a> to cache data from the third party API. This allows you to optimize cacheable requests made to the API. Integrating with third party APIs from Cloudflare Workers adds additional functionality and features to your application.</p>
</li>
<li>
<p>Use <a href="/workers/configuration/routing/custom-domains/">Custom Domains</a> when communicating with external APIs, which treat your Worker as your core application.</p>
</li>
</ul>
