---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/curl/
  description: Display formatted curl command examples.
  full_title: CURL · Cloudflare Style Guide
  head_html: <title>CURL · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Display formatted curl command examples."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/curl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/curl/index.md"><meta property="og:title" content="CURL · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Display formatted curl command examples."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/curl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/curl/#page","headline":"CURL \u00b7 Cloudflare Style Guide","description":"Display formatted curl command examples.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/curl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/curl/
  schema: 1
---
<p>The <code>CURL</code> component is used to display a cURL command for making HTTP requests.</p>
<h2 id="import">Import</h2>
<pre tabindex="0"><code class="language-mdx">import { CURL } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre tabindex="0"><code class="language-mdx">import { CURL } from &quot;~/components&quot;;&#10;&#10;&lt;CURL&#10;	url=&quot;https://httpbin.org/anything&quot;&#10;	method=&quot;POST&quot;&#10;	json={{&#10;		key: &quot;va&#x27;l&#x27;ue&quot;,&#10;	}}&#10;	query={{&#10;		foo: &quot;bar&quot;,&#10;		bar: [&quot;baz&quot;, &quot;qux&quot;],&#10;	}}&#10;	code={{&#10;		mark: &quot;value&quot;,&#10;	}}&#10;/&gt;&#10;&#10;&lt;CURL&#10;	url=&quot;https://httpbin.org/anything&quot;&#10;	method=&quot;POST&quot;&#10;	form={{&#10;		key: &quot;value&quot;,&#10;	}}&#10;	code={{&#10;		mark: &quot;value&quot;,&#10;	}}&#10;/&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;CURL&gt;</code> Props</h2>
<h3 id="url"><code>url</code></h3>
<p><strong>required</strong></p>
<p><strong>type:</strong> <code>string</code></p>
<p>The URL to make the request to.</p>
<h3 id="method"><code>method</code></h3>
<p><strong>type:</strong> <code>&quot;GET&quot; | &quot;HEAD&quot; | &quot;POST&quot; | &quot;PUT&quot; | &quot;DELETE&quot; | &quot;OPTIONS&quot; | &quot;PATCH&quot;</code></p>
<p><strong>default:</strong> <code>&quot;GET&quot;</code></p>
<p>The HTTP method to use for the request.</p>
<h3 id="headers"><code>headers</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, string&gt;</code></p>
<p>The headers to include in the request.</p>
<h3 id="json"><code>json</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, any&gt; | Record&lt;string, any&gt;[]</code></p>
<p>JSON data to include in the request.</p>
<h3 id="form"><code>form</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, any&gt;</code></p>
<p>The FormData payload to send.</p>
<h3 id="query"><code>query</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, string | string[]&gt;</code></p>
<p>URL query parameters to append to the request URL.</p>
<h3 id="code"><code>code</code></h3>
<p><strong>type:</strong> <code>object</code></p>
<p>An object of Astro <code>Code</code> props. Refer to the <a href="https://docs.astro.build/en/reference/api-reference/#code-">Astro <code>Code</code> component documentation</a> for available props.</p>
