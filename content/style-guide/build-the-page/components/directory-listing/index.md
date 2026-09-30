---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/directory-listing/
  description: Auto-generate listings of child pages.
  full_title: Directory listing · Cloudflare Style Guide
  head_html: <title>Directory listing · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Auto-generate listings of child pages."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/directory-listing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/directory-listing/index.md"><meta property="og:title" content="Directory listing · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Auto-generate listings of child pages."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/directory-listing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/directory-listing/#page","headline":"Directory listing \u00b7 Cloudflare Style Guide","description":"Auto-generate listings of child pages.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/directory-listing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/directory-listing/
  schema: 1
---
<p>Use <code>&lt;DirectoryListing /&gt;</code> to display the directory of a specific folder, which appears as a list of links.</p>
<h2 id="usage">Usage</h2>
<pre tabindex="0"><code class="language-mdx">import { DirectoryListing } from &quot;~/components&quot;;&#10;&#10;&lt;p&gt;&#10;	&lt;strong&gt;Default&lt;/strong&gt;&#10;&lt;/p&gt;&#10;&lt;DirectoryListing folder=&quot;workers/wrangler&quot; /&gt;&#10;&#10;&lt;br /&gt;&#10;&#10;&lt;p&gt;&#10;	&lt;strong&gt;maxDepth&lt;/strong&gt;&#10;&lt;/p&gt;&#10;&lt;DirectoryListing folder=&quot;workers/wrangler&quot; maxDepth={2} /&gt;&#10;&#10;&lt;p&gt;&#10;	&lt;strong&gt;Descriptions&lt;/strong&gt;&#10;&lt;/p&gt;&#10;&lt;DirectoryListing folder=&quot;workers/wrangler&quot; descriptions /&gt;&#10;&#10;&lt;p&gt;&#10;	&lt;strong&gt;Button&lt;/strong&gt;&#10;&lt;/p&gt;&#10;&lt;DirectoryListing folder=&quot;workers/wrangler&quot; button /&gt;&#10;</code></pre>
<h2 id="props">Props</h2>
<h3 id="folder"><code>folder</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>The folder path to list contents from. If not provided, defaults to the current page's path.</p>
<h3 id="button"><code>button</code></h3>
<p><strong>type:</strong> <code>boolean</code>
<strong>default:</strong> <code>false</code></p>
<p>When enabled, displays the listing as a 3-column grid of button-style cards (sorted alphabetically) instead of a bullet list. The cards match the style of our <a href="/style-guide/build-the-page/components/link-cards/"><code>LinkCard</code></a> component.</p>
<h3 id="descriptions"><code>descriptions</code></h3>
<p><strong>type:</strong> <code>boolean</code>
<strong>default:</strong> <code>false</code></p>
<p>When enabled, shows the <a href="/style-guide/build-the-page/frontmatter/">frontmatter <code>description</code></a> field for each page in the listing.</p>
<h3 id="maxdepth"><code>maxDepth</code></h3>
<p><strong>type:</strong> <code>number</code>
<strong>default:</strong> <code>1</code></p>
<p>Controls how many levels of nested pages to display. A value of <code>1</code> shows only direct children, while higher values will show deeper nesting levels.</p>
<h3 id="tag"><code>tag</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>Optionally, filter the listing to only pages with a specific tag.</p>
<h2 id="associated-content-types">Associated content types</h2>
<ul>
<li><a href="/style-guide/documentation-content-strategy/content-types/navigation/">Navigation</a></li>
</ul>
