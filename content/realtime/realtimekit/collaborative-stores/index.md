---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/
  description: Create real-time key-value stores and broadcast messages to participants in RealtimeKit.
  full_title: Storage and Broadcast · Cloudflare Realtime docs
  head_html: <title>Storage and Broadcast · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Create real-time key-value stores and broadcast messages to participants in RealtimeKit."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/index.md"><meta property="og:title" content="Storage and Broadcast · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create real-time key-value stores and broadcast messages to participants in RealtimeKit."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/#page","headline":"Storage and Broadcast \u00b7 Cloudflare Realtime docs","description":"Create real-time key-value stores and broadcast messages to participants in RealtimeKit.","url":"https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/collaborative-stores/
  schema: 1
---
<p>The RealtimeKit Stores API allows you to create multiple key-value pair realtime stores. Users can subscribe to changes in a store and receive real-time updates. Data is stored until a <a href="/realtime/realtimekit/concepts/meeting/#session">session</a> is active.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h3 id="create-a-store">Create a Store</h3>
<p>You can create a realtime store (changes are synced with other users):</p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>string</td>
<td>Name of the store</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>To create a store:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12472.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12473.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12474.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12475.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12476.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12471.md")
</aside>
<h3 id="update-a-store">Update a Store</h3>
<p>You can add, update or delete entries in a store:</p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>key</code></td>
<td>string</td>
<td>Unique identifier used to store/update a value in the store</td>
<td>Yes</td>
</tr>
<tr>
<td><code>value</code></td>
<td>StoreValue</td>
<td>Value that can be stored against a key</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12477.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12478.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12479.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12480.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12481.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12470.md")
</aside>
<h3 id="subscribe-to-a-store">Subscribe to a Store</h3>
<p>You can attach event listeners on a store's key, which fire when the value changes.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12482.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12483.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12484.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12485.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12486.md")
</div>
<h3 id="fetch-store-data">Fetch Store Data</h3>
<p>You can fetch the data stored in the store:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12487.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12488.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12489.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12490.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12491.md")
</div>
