---
cp9:
  canonical: https://developers.cloudflare.com/kv/examples/workers-kv-to-serve-assets/
  description: Example of how to use Workers KV to store static assets
  full_title: Store and retrieve static assets · Cloudflare Workers KV docs
  head_html: <title>Store and retrieve static assets · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Example of how to use Workers KV to store static assets"><link rel="canonical" href="https://developers.cloudflare.com/kv/examples/workers-kv-to-serve-assets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/examples/workers-kv-to-serve-assets/index.md"><meta property="og:title" content="Store and retrieve static assets · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Example of how to use Workers KV to store static assets"><meta property="og:url" content="https://developers.cloudflare.com/kv/examples/workers-kv-to-serve-assets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/examples/workers-kv-to-serve-assets/#page","headline":"Store and retrieve static assets \u00b7 Cloudflare Workers KV docs","description":"Example of how to use Workers KV to store static assets","url":"https://developers.cloudflare.com/kv/examples/workers-kv-to-serve-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/examples/workers-kv-to-serve-assets/
  schema: 1
---
<p class="article-summary">Store static assets in Workers KV and serve them from a Worker application with low-latency and high-throughput</p>
<p>By storing static assets in Workers KV, you can retrieve these assets globally with low-latency and high throughput. You can then serve these assets directly, or use them to dynamically generate responses. This can be useful when serving files such as custom scripts, small images that fit within <a href="/kv/platform/limits/">KV limits</a>, or when generating dynamic HTML responses from static assets such as translations.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/9501.md")
</aside>
<h2 id="write-static-assets-to-workers-kv-using-wrangler">Write static assets to Workers KV using Wrangler</h2>
<p>To store static assets in Workers KV, you can use the <a href="/workers/wrangler/">Wrangler CLI</a> (commonly used during development), the <a href="/kv/concepts/kv-bindings/">Workers KV binding</a> from a Workers application, or the <a href="/api/resources/kv/subresources/namespaces/methods/list/">Workers KV REST API</a> (commonly used to access Workers KV from an external application). We will demonstrate how to use the Wrangler CLI.</p>
<p>For this scenario, we will store a sample HTML file within our Workers KV store.</p>
<p>Create a new file <code>index.html</code> with the following content:</p>
<pre tabindex="0"><code class="language-html">Hello World!&#10;</code></pre>
<p>We can then use the following Wrangler commands to create a KV pair for this file within our production and preview namespaces:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler kv key put index.html --path index.html --namespace-id=&lt;ENTER_NAMESPACE_ID_HERE&gt;&#10;</code></pre>
<p>This will create a KV pair with the filename as key and the file content as value, within the our production and preview namespaces specified by your binding in your Wrangler file.</p>
<h2 id="serve-static-assets-from-kv-from-your-worker-application">Serve static assets from KV from your Worker application</h2>
<p>In this example, our Workers application will accept any key name as the path of the HTTP request and return the value stored in the KV store for that key.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9504.md")
</div></div>
<p>This code parses the key name for the key-value pair to fetch from the HTTP request. Then, it determines the proper MIME type for the response to inform the browser how to handle the response.
To retrieve the value from the KV store, this code uses <code>arrayBuffer</code> to properly handle binary data such as images, documents, and video/audio files.</p>
<p>Given a sample key-value pair with key <code>index.html</code> with value containing some HTML content in our Workers KV namespace store, we can access our Workers application
at <code>https://&lt;YOUR-WORKER-HOSTNAME&gt;/index.html</code> to see the contents of the <code>index.html</code> file.</p>
<p>Try it out with an image or a document and you will see that this Worker is also properly serving those assets from KV.</p>
<h2 id="generate-dynamic-responses-from-your-key-value-pairs">Generate dynamic responses from your key-value pairs</h2>
<p>In addition to serving static assets, we can also generate dynamic HTML or API responses based on the values stored in our KV store.</p>
<ol>
<li>Start by creating this file in the root of your project:</li>
</ol>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;language_code&quot;: &quot;en&quot;,&#10;		&quot;message&quot;: &quot;Hello World!&quot;&#10;	},&#10;	{&#10;		&quot;language_code&quot;: &quot;es&quot;,&#10;		&quot;message&quot;: &quot;¡Hola Mundo!&quot;&#10;	},&#10;	{&#10;		&quot;language_code&quot;: &quot;fr&quot;,&#10;		&quot;message&quot;: &quot;Bonjour le monde!&quot;&#10;	},&#10;	{&#10;		&quot;language_code&quot;: &quot;de&quot;,&#10;		&quot;message&quot;: &quot;Hallo Welt!&quot;&#10;	},&#10;	{&#10;		&quot;language_code&quot;: &quot;zh&quot;,&#10;		&quot;message&quot;: &quot;你好，世界！&quot;&#10;	},&#10;	{&#10;		&quot;language_code&quot;: &quot;ja&quot;,&#10;		&quot;message&quot;: &quot;こんにちは、世界！&quot;&#10;	},&#10;	{&#10;		&quot;language_code&quot;: &quot;hi&quot;,&#10;		&quot;message&quot;: &quot;नमस्ते दुनिया!&quot;&#10;	},&#10;	{&#10;		&quot;language_code&quot;: &quot;ar&quot;,&#10;		&quot;message&quot;: &quot;مرحبا بالعالم!&quot;&#10;	}&#10;]&#10;</code></pre>
<ol start="2">
<li>Open a terminal and enter the following KV command to create a KV entry for the translations file:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler kv key put hello-world.json --path hello-world.json --namespace-id=&lt;ENTER_NAMESPACE_ID_HERE&gt;&#10;</code></pre>
<ol start="3">
<li>Update your Workers code to add logic to serve a translated HTML file based on the language of the Accept-Language header of the request:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9507.md")
</div></div>
<p>This new code provides a specific endpoint, <code>/hello-world</code>, which will provide translated responses. When this URL is accessed, our Worker code will first retrieve the language that is requested by the client in the <code>Accept-Language</code> request header and the translations from our KV store for the <code>hello-world.json</code> key. It then gets the translated message and returns the generated HTML.</p>
<p>When accessing the Worker application at <code>https://&lt;YOUR-WORKER-HOSTNAME&gt;/hello-world</code>, we can notice that our application is now returning the properly translated &quot;Hello World&quot; message.</p>
<p>From your browser's developer console, change the locale language (on Chromium browsers, Run <code>Show Sensors</code> to get a dropdown selection for locales). You will see that the Worker is now returning the translated message based on the locale language.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/languages/rust/">Rust support in Workers</a>.</li>
<li><a href="/kv/get-started/">Using KV in Workers</a>.</li>
</ul>
