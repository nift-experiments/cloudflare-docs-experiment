---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/
  description: API reference for rtk-button component (Angular Library)
  full_title: rtk-button · Cloudflare Realtime docs
  head_html: <title>rtk-button · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for rtk-button component (Angular Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/index.md"><meta property="og:title" content="rtk-button · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for rtk-button component (Angular Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/#page","headline":"rtk-button \u00b7 Cloudflare Realtime docs","description":"API reference for rtk-button component (Angular Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/
  schema: 1
---
<p>A button that follows RTK Design System.</p>
<h2 id="properties">Properties</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>disabled</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Where the button is disabled or not</td>
</tr>
<tr>
<td><code>kind</code></td>
<td><code>ButtonKind</code></td>
<td>✅</td>
<td>-</td>
<td>Button type</td>
</tr>
<tr>
<td><code>reverse</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether to reverse order of children</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>type</code></td>
<td><code>HTMLButtonElement['type']</code></td>
<td>✅</td>
<td>-</td>
<td>Button type</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>ButtonVariant</code></td>
<td>✅</td>
<td>-</td>
<td>Button variant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-button&gt;&lt;/rtk-button&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre tabindex="0"><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-button&#10; [disabled]=&quot;true&quot;&#10; [kind]=&quot;buttonkind&quot;&#10; [reverse]=&quot;true&quot;&gt;&#10;&lt;/rtk-button&gt;&#10;</code></pre>
