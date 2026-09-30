---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/
  description: Extract metadata from the HTML meta tags on crawled pages so you can filter search results by it.
  full_title: Custom metadata · Cloudflare AI Search docs
  head_html: <title>Custom metadata · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Extract metadata from the HTML meta tags on crawled pages so you can filter search results by it."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/index.md"><meta property="og:title" content="Custom metadata · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Extract metadata from the HTML meta tags on crawled pages so you can filter search results by it."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/#page","headline":"Custom metadata \u00b7 Cloudflare AI Search docs","description":"Extract metadata from the HTML meta tags on crawled pages so you can filter search results by it.","url":"https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/data-source/website/custom-metadata/
  schema: 1
---
<p>You can attach custom metadata to web pages using HTML <code>&lt;meta&gt;</code> tags. AI Search extracts metadata from the <code>&lt;head&gt;</code> section of each crawled page.</p>
<p>Before custom metadata can be extracted, you must <a href="/ai-search/configuration/indexing/metadata/#define-a-schema">define a schema</a> in your AI Search configuration.</p>
<h2 id="add-metadata-to-web-pages">Add metadata to web pages</h2>
<p>Add <code>&lt;meta&gt;</code> tags using either the <code>name</code> or <code>property</code> attribute:</p>
<pre tabindex="0"><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;meta name=&quot;title&quot; content=&quot;Getting Started Guide&quot; /&gt;&#10;		&lt;meta name=&quot;description&quot; content=&quot;Learn how to set up the application&quot; /&gt;&#10;		&lt;meta property=&quot;og:title&quot; content=&quot;Getting Started Guide&quot; /&gt;&#10;		&lt;meta property=&quot;og:image&quot; content=&quot;https://example.com/og-image.png&quot; /&gt;&#10;		&lt;meta name=&quot;category&quot; content=&quot;documentation&quot; /&gt;&#10;		&lt;meta name=&quot;version&quot; content=&quot;2.5&quot; /&gt;&#10;		&lt;meta name=&quot;is_public&quot; content=&quot;true&quot; /&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;!-- Page content --&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<h2 id="recognized-fields">Recognized fields</h2>
<p>For the following fields, AI Search knows which meta tags to extract from. You must still define these in your schema to enable extraction.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Source</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>title</code></td>
<td><code>&lt;meta name=&quot;title&quot;&gt;</code> or <code>&lt;meta property=&quot;og:title&quot;&gt;</code></td>
</tr>
<tr>
<td><code>description</code></td>
<td><code>&lt;meta name=&quot;description&quot;&gt;</code> or <code>&lt;meta property=&quot;og:description&quot;&gt;</code></td>
</tr>
<tr>
<td><code>image</code></td>
<td><code>&lt;meta property=&quot;og:image&quot;&gt;</code></td>
</tr>
</tbody>
</table>
<p>When both a standard meta tag and an Open Graph tag are present, the standard meta tag takes precedence.</p>
<h2 id="how-metadata-extraction-works">How metadata extraction works</h2>
<p>When the crawler fetches a page:</p>
<ol>
<li>All <code>&lt;meta&gt;</code> tags with <code>name</code> or <code>property</code> attributes are parsed from the <code>&lt;head&gt;</code> section.</li>
<li>Tag names are matched against your schema (case-insensitive).</li>
<li>The <code>content</code> attribute value is cast to the configured data type.</li>
<li>Extracted metadata is stored alongside the cached HTML.</li>
<li>On subsequent processing, metadata flows into the vector index.</li>
</ol>
<h2 id="boolean-value-parsing">Boolean value parsing</h2>
<p>For <code>boolean</code> fields, the following values are accepted (case-insensitive):</p>
<table>
<thead>
<tr>
<th>True values</th>
<th>False values</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>true</code>, <code>1</code>, <code>yes</code></td>
<td><code>false</code>, <code>0</code>, <code>no</code></td>
</tr>
</tbody>
</table>
<p>Any other value is treated as invalid and the field is omitted.</p>
