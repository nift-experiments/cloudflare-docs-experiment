---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/product-changelog/
  description: Display product changelog entries.
  full_title: Product changelog · Cloudflare Style Guide
  head_html: <title>Product changelog · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Display product changelog entries."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/product-changelog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/product-changelog/index.md"><meta property="og:title" content="Product changelog · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Display product changelog entries."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/product-changelog/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/product-changelog/#page","headline":"Product changelog \u00b7 Cloudflare Style Guide","description":"Display product changelog entries.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/product-changelog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/product-changelog/
  schema: 1
---
<p>This component can be used to display entries from the <a href="/changelog/">changelog</a> for a given product or product area.</p>
<h2 id="import">Import</h2>
<pre tabindex="0"><code class="language-mdx">import { ProductChangelog } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre tabindex="0"><code class="language-mdx">import { ProductChangelog } from &quot;~/components&quot;;&#10;&#10;&lt;ProductChangelog product=&quot;workers&quot; /&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;ProductChangelog&gt;</code> Props</h2>
<p>The <code>product</code> and <code>area</code> props cannot be used at the same time.</p>
<h3 id="product"><code>product</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>The name of the product.</p>
<h3 id="area"><code>area</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>The name of the product area.</p>
<h3 id="hideentry"><code>hideEntry</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>The id of a specific entry to hide.</p>
<h3 id="publish-future-dated-entry"><code>publish_future_dated_entry</code></h3>
<p><strong>type:</strong> <code>boolean</code></p>
<p><strong>default:</strong> <code>false</code></p>
<p>Set to <code>true</code> to show future-dated entries (used for WAF scheduled changelogs).</p>
<h3 id="numberofentries"><code>numberOfEntries</code></h3>
<p><strong>type:</strong> <code>number</code></p>
<p>Limits the number of entries shown.</p>
