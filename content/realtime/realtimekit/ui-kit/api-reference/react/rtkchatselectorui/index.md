---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/
  description: API reference for RtkChatSelectorUi component (React Library)
  full_title: RtkChatSelectorUi · Cloudflare Realtime docs
  head_html: <title>RtkChatSelectorUi · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkChatSelectorUi component (React Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/index.md"><meta property="og:title" content="RtkChatSelectorUi · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkChatSelectorUi component (React Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/#page","headline":"RtkChatSelectorUi \u00b7 Cloudflare Realtime docs","description":"API reference for RtkChatSelectorUi component (React Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/
  schema: 1
---
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
<td><code>groups</code></td>
<td><code>ChatGroup[]</code></td>
<td>✅</td>
<td>-</td>
<td>Participants</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>selectedGroupId</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Selected participant</td>
</tr>
<tr>
<td><code>selfUserId</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Self User ID</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
<tr>
<td><code>unreadCounts</code></td>
<td><code>Record&lt;string, number&gt;</code></td>
<td>✅</td>
<td>-</td>
<td>Unread counts</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkChatSelectorUi } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkChatSelectorUi /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkChatSelectorUi } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkChatSelectorUi&#10;      groups={[]}&#10;      selectedGroupId=&quot;example&quot;&#10;      selfUserId=&quot;example&quot;&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
