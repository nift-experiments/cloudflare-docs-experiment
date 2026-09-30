---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/
  description: Cloudflare's Markdown for Agents converts HTML to Markdown at the edge, allowing AI systems to request content in text/markdown format.
  full_title: Markdown for Agents · Cloudflare Fundamentals docs
  head_html: <title>Markdown for Agents · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare&#x27;s Markdown for Agents converts HTML to Markdown at the edge, allowing AI systems to request content in text/markdown format."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/index.md"><meta property="og:title" content="Markdown for Agents · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare&#x27;s Markdown for Agents converts HTML to Markdown at the edge, allowing AI systems to request content in text/markdown format."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/#page","headline":"Markdown for Agents \u00b7 Cloudflare Fundamentals docs","description":"Cloudflare's Markdown for Agents converts HTML to Markdown at the edge, allowing AI systems to request content in text/markdown format.","url":"https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/markdown-for-agents/
  schema: 1
---
<h2 id="what-is-markdown-for-agents">What is Markdown for Agents</h2>
<p>Markdown has quickly become the lingua franca for agents and AI systems as a whole. The format’s explicit structure makes it ideal for AI processing, ultimately resulting in better results while minimizing token waste.</p>
<p>Cloudflare's network supports real-time content conversion at the source, for enabled zones using <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation">content negotiation</a> headers. When AI systems request pages from any website that uses Cloudflare and has Markdown for Agents enabled, they can express the preference for <code>text/markdown</code> in the request and our network will automatically and efficiently convert the HTML to Markdown, when possible, on the fly.</p>
<p>Read the <a href="https://blog.cloudflare.com/markdown-for-agents/">announcement</a> in our blog for more information.</p>
<h2 id="how-to-use">How to use</h2>
<p>To fetch the Markdown version of any page from a zone with Markdown for Agents enabled, the client needs to add the <code>Accept</code> negotiation header with <code>text/markdown</code> as one of the options. Cloudflare will detect this, fetch the original HTML version from the origin, and convert it to Markdown before serving it to the client.</p>
<p>Here's a curl example with the <code>Accept</code> negotiation header requesting this page from our developer documentation:</p>
<pre tabindex="0"><code class="language-bash">curl https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ \&#10;  &#45;H &quot;Accept: text/markdown&quot;&#10;</code></pre>
<p>Or if you’re building an AI Agent using Workers, you can use TypeScript:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8783.md")
</div>
<p>The response to this request is now formatting in markdown:</p>
<pre tabindex="0"><code class="language-http">HTTP/2 200&#10;date: Wed, 11 Feb 2026 11:44:48 GMT&#10;content-type: text/markdown; charset=utf-8&#10;content-length: 2899&#10;vary: accept&#10;cache-control: public, max-age=3600&#10;strict-transport-security: max-age=63072000; includeSubDomains&#10;x-markdown-tokens: 725&#10;x-original-tokens: 12345&#10;content-signal: ai-train=yes, search=yes, ai-input=yes&#10;&#10;&#45;--&#10;title: Markdown for Agents · Cloudflare Agents docs&#10;&#45;--&#10;&#10;&#35;# What is Markdown for Agents&#10;&#10;Markdown has quickly become the lingua franca for agents and AI systems&#10;as a whole. The format’s explicit structure makes it ideal for AI processing,&#10;ultimately resulting in better results while minimizing token waste.&#10;...&#10;</code></pre>
<h3 id="response-headers">Response headers</h3>
<p>Markdown for Agents preserves the headers from your origin response on the converted response, so security- and cache-relevant headers survive conversion. This includes headers such as <code>Strict-Transport-Security</code> (HSTS), <code>Content-Security-Policy</code> (CSP), <code>X-Frame-Options</code>, <code>Set-Cookie</code>, CORS headers (for example, <code>Access-Control-Allow-Origin</code>), and caching headers (<code>Cache-Control</code>, <code>Expires</code>, <code>Age</code>).</p>
<p>Because the body is replaced with converted Markdown, the following changes are applied:</p>
<ul>
<li><code>Content-Type</code> is set to <code>text/markdown; charset=utf-8</code>.</li>
<li><code>Vary</code> includes <code>Accept</code> (any <code>Vary</code> dimensions your origin already declared are preserved) so that caches store separate variants for Markdown and HTML.</li>
<li><code>Content-Length</code> is recalculated to match the size of the Markdown response.</li>
<li>Headers that describe the original body are removed, because they no longer match the converted response: <code>Content-Encoding</code>, <code>Content-Range</code>, <code>Transfer-Encoding</code>, <code>ETag</code>, and <code>Last-Modified</code>. <code>ETag</code> and <code>Last-Modified</code> are dropped because conditional requests (<code>If-None-Match</code>, <code>If-Modified-Since</code>) cannot be honored for converted responses.</li>
</ul>
<p>Markdown for Agents also adds the token count headers described below.</p>
<h3 id="token-count-headers">Token count headers</h3>
<p>Note that we include token count headers with the converted response. <code>x-markdown-tokens</code> indicates the estimated number of tokens in the Markdown document, and <code>x-original-tokens</code> indicates the estimated number of tokens in the original HTML document before conversion. You can use these values in your flow, for example to calculate the size of a context window, estimate the token savings from Markdown conversion, or decide on your chunking strategy.</p>
<h3 id="content-signals-policy">Content Signals Policy</h3>
<p><a href="https://contentsignals.org/">Content Signals</a> is a framework that allows anyone to express their preferences for how their content can be used after it has been accessed.</p>
<p>If your origin already sets a <code>content-signal</code> header, Markdown for Agents preserves that value on the converted response — your origin's policy is authoritative. This lets you define custom Content Signal policies by setting the <code>content-signal</code> header at your origin.</p>
<p>When the origin response does not include a <code>content-signal</code> header, Markdown for Agents adds a default <code>Content-Signal: ai-train=yes, search=yes, ai-input=yes</code>, signaling that the content can be used for AI Training, Search results, and AI Input, which includes agentic use.</p>
<h2 id="output-format">Output format</h2>
<p>Markdown for Agents returns a Markdown document with a consistent, predictable structure so AI systems can rely on it without per-site parsing logic. The response always follows this layout:</p>
<ol>
<li><strong>YAML frontmatter</strong> with metadata extracted from the page's <code>&lt;meta&gt;</code> tags. Only emitted when at least one supported meta tag is present.</li>
<li><strong>Body Markdown</strong> converted from the document body. Non-content elements (such as headers, footers, navigation, scripts, and styles) are stripped during pre-processing. For the full list of elements that are removed, refer to <a href="/workers-ai/features/markdown-conversion/how-it-works/#html">HTML pre-processing</a> in the Workers AI Markdown Conversion documentation.</li>
<li><strong>JSON-LD</strong> structured data preserved as a fenced <code>json</code> code block at the end of the document. Only emitted when the source HTML contains JSON-LD.</li>
</ol>
<h3 id="yaml-frontmatter">YAML frontmatter</h3>
<p>When the source HTML contains supported <code>&lt;meta&gt;</code> tags, Markdown for Agents prepends a YAML frontmatter block to the response. The block uses the following fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Source <code>&lt;meta&gt;</code> tag</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>title</code></td>
<td><code>&lt;meta name=&quot;title&quot;&gt;</code>, with fallback to <code>&lt;meta property=&quot;og:title&quot;&gt;</code></td>
</tr>
<tr>
<td><code>description</code></td>
<td><code>&lt;meta name=&quot;description&quot;&gt;</code>, with fallback to <code>&lt;meta property=&quot;og:description&quot;&gt;</code></td>
</tr>
<tr>
<td><code>image</code></td>
<td><code>&lt;meta property=&quot;og:image&quot;&gt;</code></td>
</tr>
</tbody>
</table>
<p>Only fields with a value are emitted. If the source HTML does not contain any of the supported meta tags, the frontmatter block is omitted entirely.</p>
<p>For <code>title</code> and <code>description</code>, the standard <code>&lt;meta name=&quot;...&quot;&gt;</code> form always takes priority over the Open Graph <code>&lt;meta property=&quot;og:...&quot;&gt;</code> form, regardless of the order they appear in the HTML. Open Graph values are used only as fallbacks when the standard form is missing.</p>
<p>Example output:</p>
<pre tabindex="0"><code class="language-markdown">&#45;--&#10;title: My Page Title&#10;description: A short summary of the page.&#10;image: https://example.com/cover.png&#10;&#45;--&#10;&#10;&#35; Page heading&#10;&#10;...&#10;</code></pre>
<h3 id="json-ld">JSON-LD</h3>
<p><a href="https://json-ld.org/">JSON-LD</a> is a structured-data format used by search engines and AI systems to interpret a page's semantic content. Markdown for Agents preserves any <code>&lt;script type=&quot;application/ld+json&quot;&gt;</code> blocks from the source HTML by appending them at the end of the converted Markdown inside a single fenced <code>json</code> code block.</p>
<p>If the source HTML contains multiple JSON-LD scripts, all of them are concatenated within the same code block, each on its own line.</p>
<p>JSON-LD is the only <code>&lt;script&gt;</code> content preserved in the output — all other <code>&lt;script&gt;</code> and <code>&lt;style&gt;</code> content is stripped during <a href="/workers-ai/features/markdown-conversion/how-it-works/#html">HTML pre-processing</a>.</p>
<p>Example output:</p>
<pre tabindex="0"><code class="language-markdown">... main markdown content ...&#10;</code></pre>
<p>{
&quot;@context&quot;: &quot;<a href="https://schema.org">https://schema.org</a>&quot;,
&quot;@type&quot;: &quot;Article&quot;,
&quot;headline&quot;: &quot;Article Title&quot;,
&quot;author&quot;: { &quot;@type&quot;: &quot;Person&quot;, &quot;name&quot;: &quot;Jane Doe&quot; }
}</p>
<pre tabindex="0"><code>&#10;</code></pre>
<h2 id="how-to-enable">How to enable</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8787.md")
</div></div>
<h2 id="availability-and-pricing">Availability and Pricing</h2>
<p>Markdown for Agents is available to Pro, Business and Enterprise plans, and SSL for SaaS customers at no cost.</p>
<h2 id="try-it-with-cloudflare">Try it with Cloudflare</h2>
<p>We have enabled this feature in our <a href="https://developers.cloudflare.com/">Developer Documentation</a> and our <a href="https://blog.cloudflare.com/">Blog</a>, inviting all AI crawlers and agents to consume our content using markdown instead of HTML.</p>
<pre tabindex="0"><code class="language-bash">curl https://blog.cloudflare.com/markdown-for-agents/ \&#10;  &#45;H &quot;Accept: text/markdown&quot;&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<ul>
<li>We only convert from HTML, other types of documents may be included in the future.</li>
<li>The origin response cannot exceed 2 MB (2,097,152 bytes).</li>
</ul>
<h2 id="other-markdown-conversion-apis">Other Markdown conversion APIs</h2>
<p>If you’re building AI systems that require arbitrary document conversion from outside Cloudflare or Markdown for Agents is not available from the content source, we provide other ways to convert documents to Markdown for your applications:</p>
<ul>
<li>Workers AI <a href="/workers-ai/features/markdown-conversion/">AI.toMarkdown()</a> supports multiple document types and summarization.</li>
<li>The Browser Run <a href="/browser-run/quick-actions/markdown-endpoint/">/markdown</a> endpoint supports markdown conversion if you need to render a dynamic page or application in a real browser before converting it.</li>
</ul>
