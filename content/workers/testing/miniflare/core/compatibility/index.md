---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/
  description: Configure compatibility dates and flags in Miniflare to match Cloudflare Workers runtime behavior.
  full_title: Compatibility Dates · Cloudflare Workers docs
  head_html: <title>Compatibility Dates · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure compatibility dates and flags in Miniflare to match Cloudflare Workers runtime behavior."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/index.md"><meta property="og:title" content="Compatibility Dates · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure compatibility dates and flags in Miniflare to match Cloudflare Workers runtime behavior."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/#page","headline":"Compatibility Dates \u00b7 Cloudflare Workers docs","description":"Configure compatibility dates and flags in Miniflare to match Cloudflare Workers runtime behavior.","url":"https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/miniflare/core/compatibility/
  schema: 1
---
<ul>
<li><a href="/workers/configuration/compatibility-dates">Compatibility Dates Reference</a></li>
</ul>
<h2 id="compatibility-dates">Compatibility Dates</h2>
<p>Miniflare uses compatibility dates to opt-into backwards-incompatible changes
from a specific date. If one isn't set, it will default to some time far in the
past.</p>
<pre tabindex="0"><code class="language-js">const mf = new Miniflare({&#10;	compatibilityDate: &quot;2021-11-12&quot;,&#10;});&#10;</code></pre>
<h2 id="compatibility-flags">Compatibility Flags</h2>
<p>Miniflare also lets you opt-in/out of specific changes using compatibility
flags:</p>
<pre tabindex="0"><code class="language-js">const mf = new Miniflare({&#10;	compatibilityFlags: [&#10;		&quot;formdata_parser_supports_files&quot;,&#10;		&quot;durable_object_fetch_allows_relative_url&quot;,&#10;	],&#10;});&#10;</code></pre>
