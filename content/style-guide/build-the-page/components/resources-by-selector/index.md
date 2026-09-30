---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/resources-by-selector/
  description: Display resources filtered by selector values.
  full_title: Resources by selector · Cloudflare Style Guide
  head_html: <title>Resources by selector · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Display resources filtered by selector values."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/resources-by-selector/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/resources-by-selector/index.md"><meta property="og:title" content="Resources by selector · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Display resources filtered by selector values."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/resources-by-selector/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/resources-by-selector/#page","headline":"Resources by selector \u00b7 Cloudflare Style Guide","description":"Display resources filtered by selector values.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/resources-by-selector/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/resources-by-selector/
  schema: 1
---
<p>The <code>ResourcesBySelector</code> component allows you to pull in documentation resources based on the <code>pcx_content_type</code> and <code>products</code> frontmatter properties.</p>
<h2 id="component">Component</h2>
<pre tabindex="0"><code class="language-mdx">import { ResourcesBySelector } from &quot;~/components&quot;;&#10;&#10;&lt;ResourcesBySelector&#10;	directory=&quot;workers/examples/&quot;&#10;	types={[&quot;example&quot;]}&#10;	filterables={[&quot;products&quot;]}&#10;/&gt;&#10;</code></pre>
<h3 id="inputs">Inputs</h3>
<ul>
<li>
<p><code>directory</code> <span class="nb-type">string</span></p>
<p>The directory to search for resources in, relative to <code>src/content/docs/</code>. For example, for Workers tutorials, <code>directory=&quot;workers/tutorials/&quot;</code>.</p>
</li>
<li>
<p><code>filterables</code> <span class="nb-type">string[]</span></p>
<p>An array of frontmatter properties to show in the frontend filter dropdown. For example, <code>filterables={[&quot;products&quot;]}</code> will allow users to filter based on each pages' <code>products</code> frontmatter.</p>
</li>
<li>
<p><code>types</code> <span class="nb-type">string[]</span></p>
<p>An array of <code>pcx_content_type</code> values to filter which content gets pulled into the component. For example, <code>types={[&quot;example&quot;]}</code>.</p>
</li>
<li>
<p><code>products</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span></p>
<p>An array of <code>products</code> values to filter which content gets pulled into the component. For example, <code>products={[&quot;D1&quot;]}</code>.</p>
</li>
<li>
<p><code>showDescriptions</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional (default true)</span></p>
<p>If set to <code>false</code>, will only show the titles of associated pages, not the showDescriptions</p>
</li>
<li>
<p><code>showLastUpdated</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional (default false)</span></p>
<p>If set to <code>true</code>, will add the last updated date, which is added in the <a href="/style-guide/build-the-page/frontmatter/custom-properties/#properties"><code>updated</code> frontmatter value</a>.</p>
</li>
</ul>
