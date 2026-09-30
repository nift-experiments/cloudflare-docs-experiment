---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/configuration/bindings/
  description: Create an AI binding to connect your Cloudflare Worker to Workers AI.
  full_title: Workers Bindings · Cloudflare Workers AI docs
  head_html: <title>Workers Bindings · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Create an AI binding to connect your Cloudflare Worker to Workers AI."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/configuration/bindings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/configuration/bindings/index.md"><meta property="og:title" content="Workers Bindings · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create an AI binding to connect your Cloudflare Worker to Workers AI."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/configuration/bindings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/configuration/bindings/#page","headline":"Workers Bindings \u00b7 Cloudflare Workers AI docs","description":"Create an AI binding to connect your Cloudflare Worker to Workers AI.","url":"https://developers.cloudflare.com/workers-ai/configuration/bindings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/configuration/bindings/
  schema: 1
---
<h2 id="workers">Workers</h2>
<p><a href="/workers/">Workers</a> provides a serverless execution environment that allows you to create new applications or augment existing ones.</p>
<p>To use Workers AI with Workers, you must create a Workers AI <a href="/workers/runtime-apis/bindings/">binding</a>. Bindings allow your Workers to interact with resources, like Workers AI, on the Cloudflare Developer Platform. You create bindings on the Cloudflare dashboard or by updating your <a href="/workers/wrangler/configuration/">Wrangler file</a>.</p>
<p>To bind Workers AI to your Worker, add the following to the end of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15817.md")
</div>
<h2 id="pages-functions">Pages Functions</h2>
<p><a href="/pages/functions/">Pages Functions</a> allow you to build full-stack applications with Cloudflare Pages by executing code on the Cloudflare network. Functions are Workers under the hood.</p>
<p>To configure a Workers AI binding in your Pages Function, you must use the Cloudflare dashboard. Refer to <a href="/pages/functions/bindings/#workers-ai">Workers AI bindings</a> for instructions.</p>
<h2 id="methods">Methods</h2>
<h3 id="async-env-ai-run">async env.AI.run()</h3>
<p><code>async env.AI.run()</code> runs a model. Takes a model as the first parameter, and an object as the second parameter.</p>
<pre tabindex="0"><code class="language-javascript">const answer = await env.AI.run(&#x27;@cf/meta/llama-3.1-8b-instruct&#x27;, {&#10;    prompt: &quot;What is the origin of the phrase &#x27;Hello, World&#x27;&quot;&#10;});&#10;</code></pre>
<p><strong>Parameters</strong></p>
<ul>
<li>
<p><code>model</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The model to run.</li>
</ul>
<p><strong>Supported options</strong></p>
<ul>
<li><code>stream</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Returns a stream of results as they are available.</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-javascript">const answer = await env.AI.run(&#x27;@cf/meta/llama-3.1-8b-instruct&#x27;, {&#10;    prompt: &quot;What is the origin of the phrase &#x27;Hello, World&#x27;&quot;,&#10;    stream: true&#10;});&#10;&#10;return new Response(answer, {&#10;    headers: { &quot;content-type&quot;: &quot;text/event-stream&quot; }&#10;});&#10;</code></pre>
