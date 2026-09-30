---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/
  description: Show product availability by plan type.
  full_title: Product availability text · Cloudflare Style Guide
  head_html: <title>Product availability text · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Show product availability by plan type."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/index.md"><meta property="og:title" content="Product availability text · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Show product availability by plan type."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/#page","headline":"Product availability text \u00b7 Cloudflare Style Guide","description":"Show product availability by plan type.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/product-availability-text/
  schema: 1
---
<p>The <code>ProductAvailabilityText</code> component dynamically renders a product's lifecycle status (such as &quot;Beta&quot; or &quot;Alpha&quot;) inline with the product name. It renders nothing for generally available (GA) products, so it is safe to leave in place as a product matures.</p>
<p>The <code>product</code> prop must match a file in <code>src/content/directory/</code>.</p>
<pre tabindex="0"><code class="language-mdx">import { ProductAvailabilityText } from &quot;~/components&quot;;&#10;&#10;Cloud Connector &lt;ProductAvailabilityText product=&quot;cloud-connector&quot; /&gt; allows you to route matching traffic to a public cloud provider.&#10;</code></pre>
<h2 id="props">Props</h2>
<table>
<thead>
<tr>
<th>Prop</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>product</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>—</td>
<td>Product slug matching a file in <code>src/content/directory/</code>.</td>
</tr>
<tr>
<td><code>parentheses</code></td>
<td><code>string</code></td>
<td>No</td>
<td><code>&quot;true&quot;</code></td>
<td>When <code>&quot;true&quot;</code>, wraps the output in parentheses (for example, <code>(Beta)</code>). Set to <code>&quot;false&quot;</code> for the raw text.</td>
</tr>
</tbody>
</table>
<h2 id="behavior">Behavior</h2>
<ul>
<li>If the product availability is <strong>GA</strong>, the component renders nothing.</li>
<li>If the product or its availability data is not found, the component renders nothing (and logs a warning at build time).</li>
</ul>
