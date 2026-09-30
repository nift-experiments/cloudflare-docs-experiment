---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/rest-api/
  description: Convert documents to Markdown using the Workers AI REST API endpoint.
  full_title: REST API · Cloudflare Workers AI docs
  head_html: <title>REST API · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Convert documents to Markdown using the Workers AI REST API endpoint."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/rest-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/rest-api/index.md"><meta property="og:title" content="REST API · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Convert documents to Markdown using the Workers AI REST API endpoint."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/rest-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/rest-api/#page","headline":"REST API \u00b7 Cloudflare Workers AI docs","description":"Convert documents to Markdown using the Workers AI REST API endpoint.","url":"https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/rest-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/features/markdown-conversion/usage/rest-api/
  schema: 1
---
<p>You can also use the Markdown Conversion REST API to convert your documents into Markdown.</p>
<h2 id="prerequisite-get-workers-ai-api-token">Prerequisite: Get Workers AI API token</h2>
<p>To use the Markdown Conversion service via the REST API, you need an API token with permissions for the <a href="/workers-ai/">Workers AI</a> REST API. Refer to <a href="/workers-ai/get-started/rest-api/">Get started with the Workers AI REST API</a> for instructions on obtaining an API token with the correct permissions.</p>
<h2 id="transform">Transform</h2>
<p>This endpoint lets you convert any file given to us into markdown.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;X POST \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &quot;files=@cat.jpeg&quot; \&#10;  &#45;F &quot;files=@somatosensory.pdf&quot; \&#10;  &#45;F &#x27;conversionOptions={ ... }&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15833.md")
</aside>
<h3 id="parameters">Parameters</h3>
<p><code>files</code> <span class="nb-type">File[]</span> <span class="nb-metainfo">required</span></p>
<p>The files you want to convert.</p>
<p><code>conversionOptions</code> <span class="nb-type">ConversionOptions</span> <span class="nb-metainfo">optional</span></p>
<p>Options that allow you to control how your files are converted. Refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/">Conversion Options</a> for further details.</p>
<h3 id="response">Response</h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;...&quot;,&#10;			&quot;name&quot;: &quot;good.html&quot;,&#10;			&quot;mimeType&quot;: &quot;text/html&quot;,&#10;			&quot;format&quot;: &quot;markdown&quot;,&#10;			&quot;tokens&quot;: 49,&#10;			&quot;data&quot;: &quot;# Image Embedded with a Data URI\n\nThis _image_ is directly encoded in the HTML:\n\n\n\nAn image description\n\n \n\nIt&#x27;s a tiny 5x5 pixel PNG, scaled up to 50x50px.\n\n&quot;&#10;		},&#10;		{&#10;			&quot;id&quot;: &quot;...&quot;,&#10;			&quot;name&quot;: &quot;bad.pdf&quot;,&#10;			&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;			&quot;format&quot;: &quot;error&quot;,&#10;			&quot;error&quot;: &quot;Some error that prevented this image from being converted&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h2 id="supported">Supported</h2>
<p>This endpoint lets you programmatically retrieve the full set of rich formats that are supported for conversion.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown/supported \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15832.md")
</aside>
<h3 id="response-1">Response</h3>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;extension&quot;: &quot;.html&quot;,&#10;      &quot;mimeType&quot;: &quot;text/html&quot;&#10;    },&#10;    {&#10;      &quot;extension&quot;: &quot;.pdf&quot;,&#10;      &quot;mimeType&quot;: &quot;application/pdf&quot;&#10;    },&#10;    ...&#10;  ]&#10;}&#10;</code></pre>
