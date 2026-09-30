---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/
  description: A button component for RSS feed subscriptions.
  full_title: RSSButton · Cloudflare Style Guide
  head_html: <title>RSSButton · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="A button component for RSS feed subscriptions."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/index.md"><meta property="og:title" content="RSSButton · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A button component for RSS feed subscriptions."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/#page","headline":"RSSButton \u00b7 Cloudflare Style Guide","description":"A button component for RSS feed subscriptions.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/rss-button/
  schema: 1
---
<h2 id="example">Example</h2>
<pre tabindex="0"><code class="language-mdx">import { RSSButton } from &quot;~/components&quot;;&#10;&#10;&lt;RSSButton changelog=&quot;Workers&quot; /&gt;&#10;&lt;br /&gt;&#10;&lt;RSSButton href=&quot;/custom/feed.xml&quot; text=&quot;Custom Feed&quot; icon=&quot;external&quot; /&gt;&#10;</code></pre>
<h2 id="props">Props</h2>
<h3 id="text"><code>text</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p><strong>default:</strong> <code>&quot;Subscribe to RSS&quot;</code></p>
<p>The text to display in the button.</p>
<h3 id="icon"><code>icon</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p><strong>default:</strong> <code>&quot;rss&quot;</code></p>
<p>The icon to display next to the text. Renders via the Nimbus <code>Icon</code> component; accepts any iconify icon name (for example, <code>ph:rss-simple</code>). The default <code>&quot;rss&quot;</code> maps to <code>ph:rss-simple</code>.</p>
<h3 id="changelog-or-href"><code>changelog</code> or <code>href</code></h3>
<p>You must provide either <code>changelog</code> or <code>href</code>, but not both:</p>
<h4 id="changelog"><code>changelog</code></h4>
<p><strong>type:</strong> <code>string</code></p>
<p>The name of the changelog to link to. This will be transformed into a lowercase, hyphen-separated string and used to construct the RSS feed URL in the format <code>/changelog/rss/{changelog}.xml</code>.</p>
<h4 id="href"><code>href</code></h4>
<p><strong>type:</strong> <code>string</code></p>
<p>A custom URL to link to. Use this when you need to link to an RSS feed that doesn't follow the standard changelog URL pattern.</p>
