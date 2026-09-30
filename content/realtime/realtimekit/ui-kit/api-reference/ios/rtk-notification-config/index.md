---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/
  description: API reference for RtkNotificationConfig component (iOS Library)
  full_title: RtkNotificationConfig · Cloudflare Realtime docs
  head_html: <title>RtkNotificationConfig · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkNotificationConfig component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/index.md"><meta property="og:title" content="RtkNotificationConfig · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkNotificationConfig component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/#page","headline":"RtkNotificationConfig \u00b7 Cloudflare Realtime docs","description":"API reference for RtkNotificationConfig component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/
  schema: 1
---
<p>Configuration class for controlling notification behavior in meetings.
Manages sound and toast notifications for participant join/leave events, chat messages, and polls.</p>
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
<td><code>participantJoined</code></td>
<td><code>RtkNotification</code></td>
<td>❌</td>
<td><code>RtkNotification()</code></td>
<td>Notification settings for participant join events</td>
</tr>
<tr>
<td><code>participantLeft</code></td>
<td><code>RtkNotification</code></td>
<td>❌</td>
<td><code>RtkNotification()</code></td>
<td>Notification settings for participant leave events</td>
</tr>
<tr>
<td><code>newChatArrived</code></td>
<td><code>RtkNotification</code></td>
<td>❌</td>
<td><code>RtkNotification()</code></td>
<td>Notification settings for new chat messages</td>
</tr>
<tr>
<td><code>newPollArrived</code></td>
<td><code>RtkNotification</code></td>
<td>❌</td>
<td><code>RtkNotification()</code></td>
<td>Notification settings for new poll events</td>
</tr>
</tbody>
</table>
<h2 id="rtknotification-properties">RtkNotification properties</h2>
<p>Each <code>RtkNotification</code> instance contains the following properties:</p>
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
<td><code>playSound</code></td>
<td><code>Bool</code></td>
<td>❌</td>
<td><code>true</code></td>
<td>Whether to play a notification sound</td>
</tr>
<tr>
<td><code>showToast</code></td>
<td><code>Bool</code></td>
<td>❌</td>
<td><code>true</code></td>
<td>Whether to show a toast notification</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let rtkUI = RealtimeKitUI(meetingInfo: meetingInfo)&#10;// Access the default notification config&#10;let notificationConfig = rtkUI.notification&#10;</code></pre>
<h3 id="customize-notifications">Customize notifications</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let rtkUI = RealtimeKitUI(meetingInfo: meetingInfo)&#10;&#10;// Disable sound for participant join events&#10;rtkUI.notification.participantJoined.playSound = false&#10;&#10;// Disable toast for chat messages&#10;rtkUI.notification.newChatArrived.showToast = false&#10;</code></pre>
