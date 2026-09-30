---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/
  description: API reference for RtkParticipantTileView component (Android Library)
  full_title: RtkParticipantTileView · Cloudflare Realtime docs
  head_html: <title>RtkParticipantTileView · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkParticipantTileView component (Android Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/index.md"><meta property="og:title" content="RtkParticipantTileView · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkParticipantTileView component (Android Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/#page","headline":"RtkParticipantTileView \u00b7 Cloudflare Realtime docs","description":"API reference for RtkParticipantTileView component (Android Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/
  schema: 1
---
<p>A component which plays a participant's video and allows for placement of components like name tag and avatar.</p>
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
<td><code>rtk_ptv_nameTagPosition</code></td>
<td><code>BOTTOM_LEFT | TOP_CENTER</code></td>
<td>❌</td>
<td><code>BOTTOM_LEFT</code></td>
<td>Position of the name tag</td>
</tr>
<tr>
<td><code>cardBackgroundColor</code></td>
<td><code>color</code></td>
<td>❌</td>
<td>-</td>
<td>Background color of the tile</td>
</tr>
<tr>
<td><code>cardCornerRadius</code></td>
<td><code>dimension</code></td>
<td>❌</td>
<td>-</td>
<td>Corner radius of the tile</td>
</tr>
</tbody>
</table>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Parameters</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>activate</code></td>
<td><code>participant: RtkMeetingParticipant</code></td>
<td>Bind the tile to a specific participant</td>
</tr>
<tr>
<td><code>refreshParticipantName</code></td>
<td>-</td>
<td>Refresh the name tag and avatar</td>
</tr>
<tr>
<td><code>refreshParticipantVideo</code></td>
<td>-</td>
<td>Refresh the video view state</td>
</tr>
<tr>
<td><code>applyDesignTokens</code></td>
<td><code>designTokens: RtkDesignTokens</code></td>
<td>Apply custom design tokens for theming</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.participanttile.RtkParticipantTileView&#10;    android:id=&quot;@+id/rtk_participant_tile&quot;&#10;    android:layout_width=&quot;match_parent&quot;&#10;    android:layout_height=&quot;200dp&quot;&#10;    app:rtk_ptv_nameTagPosition=&quot;BOTTOM_LEFT&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre tabindex="0"><code class="language-kotlin">val tile = findViewById&lt;RtkParticipantTileView&gt;(R.id.rtk_participant_tile)&#10;tile.activate(participant)&#10;</code></pre>
