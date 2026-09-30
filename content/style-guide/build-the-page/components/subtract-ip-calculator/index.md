---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/
  description: Interactive IP subtraction calculator component.
  full_title: Subtract IP calculator · Cloudflare Style Guide
  head_html: <title>Subtract IP calculator · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Interactive IP subtraction calculator component."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/index.md"><meta property="og:title" content="Subtract IP calculator · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Interactive IP subtraction calculator component."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/#page","headline":"Subtract IP calculator \u00b7 Cloudflare Style Guide","description":"Interactive IP subtraction calculator component.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/subtract-ip-calculator/
  schema: 1
---
<h2 id="import">Import</h2>
<pre tabindex="0"><code class="language-mdx">import { SubtractIPCalculator } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<br />
<div class="nb-interactive-component" data-cf-component="SubtractIPCalculator"></div>
<pre tabindex="0"><code class="language-mdx">import { SubtractIPCalculator } from &quot;~/components&quot;;&#10;&#10;&lt;SubtractIPCalculator client:load /&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;SubtractIPCalculator&gt;</code> Props</h2>
<h3 id="defaults"><code>defaults</code></h3>
<p><strong>type:</strong> <code>object</code></p>
<p>An optional object containing <code>base</code> (<code>string</code>) and <code>subtract</code> (<code>string[]</code>) properties, to set default inputs.</p>
<p><strong>example:</strong></p>
<div class="nb-interactive-component" data-cf-component="SubtractIPCalculator"></div>
<pre tabindex="0"><code class="language-mdx">import { SubtractIPCalculator } from &quot;~/components&quot;;&#10;&#10;&lt;SubtractIPCalculator&#10;	client:load&#10;	defaults={{&#10;		base: &quot;10.0.0.0/8&quot;,&#10;		subtract: [&quot;10.0.0.0/24&quot;, &quot;10.32.0.0/11&quot;]&#10;	}}&#10;/&gt;&#10;</code></pre>
