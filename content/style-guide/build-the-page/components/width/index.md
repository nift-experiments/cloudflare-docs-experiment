---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/width/
  description: Constrain content width for layout control.
  full_title: Width · Cloudflare Style Guide
  head_html: <title>Width · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Constrain content width for layout control."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/width/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/width/index.md"><meta property="og:title" content="Width · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Constrain content width for layout control."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/width/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/width/#page","headline":"Width \u00b7 Cloudflare Style Guide","description":"Constrain content width for layout control.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/width/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/width/
  schema: 1
---
<p>This component can be used to constrain the width of content, such as text or images.</p>
<h2 id="import">Import</h2>
<pre tabindex="0"><code class="language-mdx">import { Width } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre tabindex="0"><code class="language-mdx">import { Width } from &quot;~/components&quot;;&#10;&#10;&lt;Width size=&quot;large&quot;&gt;This content will take up 75% of the container width&lt;/Width&gt;&#10;&#10;&lt;Width size=&quot;medium&quot;&gt;&#10;	This content will take up 50% of the container width&#10;&lt;/Width&gt;&#10;&#10;&lt;Width size=&quot;small&quot;&gt;This content will take up 25% of the container width&lt;/Width&gt;&#10;&#10;&lt;Width size=&quot;small&quot; center&gt;&#10;	This content will take up 25% of the container width and be centered&#10;&lt;/Width&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;Width&gt;</code> Props</h2>
<h3 id="size"><code>size</code></h3>
<p><strong>required</strong></p>
<p><strong>type:</strong> <code>&quot;large&quot; | &quot;medium&quot; | &quot;small&quot;</code></p>
<p>Controls the width of the container:</p>
<ul>
<li><code>large</code>: 75% of container width</li>
<li><code>medium</code>: 50% of container width</li>
<li><code>small</code>: 25% of container width</li>
</ul>
<h3 id="center"><code>center</code></h3>
<p><strong>type:</strong> <code>boolean</code></p>
<p>Whether to horizontally center the content.</p>
