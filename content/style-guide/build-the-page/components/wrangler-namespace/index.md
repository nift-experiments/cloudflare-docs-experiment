---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-namespace/
  description: Display Wrangler command namespace documentation.
  full_title: WranglerNamespace · Cloudflare Style Guide
  head_html: <title>WranglerNamespace · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Display Wrangler command namespace documentation."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-namespace/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-namespace/index.md"><meta property="og:title" content="WranglerNamespace · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Display Wrangler command namespace documentation."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-namespace/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-namespace/#page","headline":"WranglerNamespace \u00b7 Cloudflare Style Guide","description":"Display Wrangler command namespace documentation.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-namespace/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/wrangler-namespace/
  schema: 1
---
<p>The <code>WranglerNamespace</code> component documents the available commands for a given namespace.</p>
<p>This is generated using the Wrangler version in the <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/package.json"><code>cloudflare-docs</code> repository</a>.</p>
<h2 id="import">Import</h2>
<pre tabindex="0"><code class="language-mdx">import { WranglerNamespace } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre tabindex="0"><code class="language-mdx">import { WranglerNamespace } from &quot;~/components&quot;;&#10;&#10;&lt;WranglerNamespace namespace=&quot;d1&quot; /&gt;&#10;</code></pre>
<h2 id="arguments">Arguments</h2>
<ul>
<li><code>namespace</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The namespace to pull the related commands from (<code>d1</code>, <code>hyperdrive</code>).</li>
</ul>
</li>
<li><code>headingLevel</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: 2) optional</span>
<ul>
<li>The heading level that the commands should be added at on the page, i.e <code>2</code> for <code>h2</code>.</li>
</ul>
</li>
</ul>
