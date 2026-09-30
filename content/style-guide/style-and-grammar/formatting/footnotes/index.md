---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/footnotes/
  description: Use footnotes in documentation.
  full_title: Footnotes · Cloudflare Style Guide
  head_html: <title>Footnotes · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Use footnotes in documentation."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/footnotes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/footnotes/index.md"><meta property="og:title" content="Footnotes · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use footnotes in documentation."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/footnotes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/footnotes/#page","headline":"Footnotes \u00b7 Cloudflare Style Guide","description":"Use footnotes in documentation.","url":"https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/footnotes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/style-and-grammar/formatting/footnotes/
  schema: 1
---
<p>Use footnotes to add details or context about something without distracting from the main content. We recommend using hover-activated footnotes, but you can also use plain text.</p>
<h3 id="hover-activated-footnotes">Hover-activated footnotes</h3>
<p>To add hover-activated footnotes, use the following syntax:</p>
<pre tabindex="0"><code class="language-mdx">This is a sentence with a footnote.[^1]&#10;&#10;[^1]: A footnote adds details or context.&#10;</code></pre>
<p>With this type of footnote, you can add the numbers to the MDX file in any order and they will still display in numerical order on the page.</p>
<p>The hover ability of this type of footnote is powered by <a href="https://atomiks.github.io/tippyjs/">tippy.js</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14678.md")
</aside>
<h3 id="plain-text-footnotes">Plain text footnotes</h3>
<p>To add plain text footnotes, use the syntax in this example:</p>
<pre tabindex="0"><code class="language-mdx">This is a sentence with a footnote.&lt;sup&gt;1&lt;/sup&gt;&#10;&#10;&lt;sup&gt;1&lt;/sup&gt; A footnote adds details or context.&#10;</code></pre>
<p>With this type of footnote, you can add the footnote note anywhere on the page. We recommend adding it to the bottom of the section or table where the footnote is referenced or to the bottom of the page.</p>
