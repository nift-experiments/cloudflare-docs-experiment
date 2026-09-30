---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/details/
  description: Create collapsible content sections.
  full_title: Details · Cloudflare Style Guide
  head_html: <title>Details · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Create collapsible content sections."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/details/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/details/index.md"><meta property="og:title" content="Details · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create collapsible content sections."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/details/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/details/#page","headline":"Details \u00b7 Cloudflare Style Guide","description":"Create collapsible content sections.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/details/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/details/
  schema: 1
---
<p>When you want to provide additional information in context, but you do not want it to clutter up the more important content, use <code>&lt;Details&gt;</code> to add a collapsible container.</p>
<pre tabindex="0"><code class="language-mdx">import { Details } from &quot;~/components&quot;;&#10;&#10;&lt;Details header=&quot;Open me!&quot;&gt;Hello, world!&lt;/Details&gt;&#10;</code></pre>
<p>You can specify the default configuration of each instance of the <code>&lt;Details&gt;</code> component (that is, whether it is open or closed by default).</p>
<pre tabindex="0"><code class="language-mdx">import { Details } from &quot;~/components&quot;;&#10;&#10;&lt;Details header=&quot;Close me!&quot; open={true}&gt;&#10;	Long piece of code example.&#10;&lt;/Details&gt;&#10;</code></pre>
<h2 id="additional-guidance">Additional guidance</h2>
<p>The primary answer or core instruction should always appear in the main content flow, not exclusively inside a tab or collapsible section.</p>
<p>Use tabs for platform-specific variations (for example, Dashboard versus API versus Terraform) only after stating the general concept. Use Details for supplementary information, not for the primary answer.</p>
<h2 id="properties">Properties</h2>
<ul>
<li>
<p><code>header</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
</li>
<li>
<p><code>id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>Adds a specific <code>id</code> to the HTML element</p>
</li>
<li>
<p><code>open</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
</li>
</ul>
