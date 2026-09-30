---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/
  description: Configure per-format options for Workers AI Markdown Conversion, including HTML and image settings.
  full_title: Conversion Options · Cloudflare Workers AI docs
  head_html: <title>Conversion Options · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure per-format options for Workers AI Markdown Conversion, including HTML and image settings."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/index.md"><meta property="og:title" content="Conversion Options · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure per-format options for Workers AI Markdown Conversion, including HTML and image settings."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/#page","headline":"Conversion Options \u00b7 Cloudflare Workers AI docs","description":"Configure per-format options for Workers AI Markdown Conversion, including HTML and image settings.","url":"https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/features/markdown-conversion/conversion-options/
  schema: 1
---
<p>By default, the <code>toMarkdown</code> service extracts text content from your files. To further extend the capabilities of the conversion process, you can pass options to the service to control how specific file types are converted.</p>
<p>Options are organized by file type and are all optional.</p>
<h2 id="available-options">Available options</h2>
<h3 id="output">Output</h3>
<pre tabindex="0"><code class="language-typescript">{&#10;  output?: {&#10;    format?: &#x27;markdown&#x27; | &#x27;text&#x27;;&#10;  }&#10;}&#10;</code></pre>
<ul>
<li><code>format</code>: controls the format of the converted content. Defaults to <code>markdown</code>. Set to <code>text</code> to receive plain text with Markdown syntax removed.</li>
</ul>
<p>When <code>format</code> is <code>text</code>, the <code>format</code> field of the <a href="/workers-ai/features/markdown-conversion/usage/binding/#conversionresult-definition"><code>ConversionResult</code></a> is also set to <code>text</code>.</p>
<h3 id="images">Images</h3>
<pre tabindex="0"><code class="language-typescript">{&#10;  image?: {&#10;    descriptionLanguage?: &#x27;en&#x27; | &#x27;it&#x27; | &#x27;de&#x27; | &#x27;es&#x27; | &#x27;fr&#x27; | &#x27;pt&#x27;;&#10;  }&#10;}&#10;</code></pre>
<ul>
<li><code>descriptionLanguage</code>: controls the language of the AI-generated image descriptions.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15818.md")
</aside>
<h3 id="html">HTML</h3>
<pre tabindex="0"><code class="language-typescript">{&#10;  html?: {&#10;    hostname?: string;&#10;    cssSelector?: string;&#10;  }&#10;}&#10;</code></pre>
<ul>
<li>
<p><code>hostname</code>: string to use as a host when resolving relative links inside the HTML.</p>
</li>
<li>
<p><code>cssSelector</code>: string containing a CSS selector pattern to pick specific elements from your HTML. Refer to <a href="/workers-ai/features/markdown-conversion/how-it-works/#html">how HTML is processed</a> for more details.</p>
</li>
</ul>
<h3 id="pdf">PDF</h3>
<pre tabindex="0"><code class="language-typescript">{&#10;  pdf?: {&#10;    metadata?: boolean;&#10;  }&#10;}&#10;</code></pre>
<ul>
<li><code>metadata</code>: Previously, all converted PDF files always included metadata information when converted. This option allows you to opt-out of this behavior.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="binding">Binding</h3>
<p>To configure custom options, pass a <code>conversionOptions</code> object inside the second argument of the binding call, like this:</p>
<pre tabindex="0"><code class="language-typescript">await env.AI.toMarkdown(..., {&#10;  conversionOptions: {&#10;    html: { ... },&#10;    pdf: { ... },&#10;    ...&#10;   }&#10;})&#10;</code></pre>
<h3 id="rest-api">REST API</h3>
<p>Since the REST API uses file uploads, the request's <code>Content-Type</code> will be <code>multipart/form-data</code>. As such, include a new form field with your stringified object as a value:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;X POST \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  ...&#10;  &#45;F &#x27;conversionOptions={ &quot;html&quot;: { ... }, ... }&#x27;&#10;</code></pre>
