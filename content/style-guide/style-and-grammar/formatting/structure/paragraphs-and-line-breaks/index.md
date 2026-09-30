---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/
  description: Format paragraphs and line breaks correctly.
  full_title: Paragraphs and line breaks · Cloudflare Style Guide
  head_html: <title>Paragraphs and line breaks · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Format paragraphs and line breaks correctly."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/index.md"><meta property="og:title" content="Paragraphs and line breaks · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Format paragraphs and line breaks correctly."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/#page","headline":"Paragraphs and line breaks \u00b7 Cloudflare Style Guide","description":"Format paragraphs and line breaks correctly.","url":"https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/
  schema: 1
---
<h2 id="paragraphs-in-markdown">Paragraphs in Markdown</h2>
<p>To start a new paragraph, leave an empty line (with no spaces) before adding the new paragraph content.</p>
<pre tabindex="0"><code class="language-txt">This sentence is the first one in this paragraph.&#10;This second sentence also belongs to the first paragraph.&#10;&#10;This is the first sentence of the second paragraph.&#10;</code></pre>
<h2 id="line-breaks-in-markdown">Line breaks in Markdown</h2>
<p>Avoid line breaks when possible. Considering creating a separate paragraph, even inside numbered lists.</p>
<p>If you need to add a line break, use the <code>&lt;br/&gt;</code> HTML element.</p>
<p>Example inside a table:</p>
<pre tabindex="0"><code class="language-txt">| Feature                          | Enabled |&#10;|----------------------------------|---------|&#10;| Feature name&lt;br/&gt;Additional info | Yes     |&#10;</code></pre>
<p>This is how the table looks:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Enabled</th>
</tr>
</thead>
<tbody>
<tr>
<td>Feature name<br/>Additional info</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14684.md")
</aside>
