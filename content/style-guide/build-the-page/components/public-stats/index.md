---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/public-stats/
  description: Display public statistics from Cloudflare data.
  full_title: Public stats · Cloudflare Style Guide
  head_html: <title>Public stats · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Display public statistics from Cloudflare data."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/public-stats/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/public-stats/index.md"><meta property="og:title" content="Public stats · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Display public statistics from Cloudflare data."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/public-stats/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/public-stats/#page","headline":"Public stats \u00b7 Cloudflare Style Guide","description":"Display public statistics from Cloudflare data.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/public-stats/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/public-stats/
  schema: 1
---
<p>The <code>PublicStats</code> component allows you to reference specific values about Cloudflare's network without maintaining those values in multiple files.</p>
<p>Refer to the examples below for more information.</p>
<pre tabindex="0"><code class="language-mdx">import { PublicStats } from &quot;~/components&quot;;&#10;&#10;Cloudflare has data centers in &lt;PublicStats id=&quot;data_center_cities&quot; /&gt;.&#10;&#10;Our network has &lt;PublicStats id=&quot;total_bandwidth&quot; /&gt;.&#10;&#10;Cloudflare also has &lt;PublicStats id=&quot;network_peers&quot; /&gt;.&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14636.md")
</aside>
<h2 id="associated-content-types">Associated content types</h2>
<p>The <code>PublicStats</code> component is commonly used on the following type of pages:</p>
<ul>
<li><a href="/style-guide/documentation-content-strategy/content-types/overview/">Overview</a></li>
<li><a href="/style-guide/documentation-content-strategy/content-types/reference-architecture/">Reference Architecture</a></li>
<li><a href="/style-guide/documentation-content-strategy/content-types/reference-architecture/#reference-architecture-diagrams">Reference Architecture Diagrams</a></li>
</ul>
