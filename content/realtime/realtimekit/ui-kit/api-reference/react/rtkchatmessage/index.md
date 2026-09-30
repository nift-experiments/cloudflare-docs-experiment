---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/
  description: API reference for RtkChatMessage component (React Library)
  full_title: RtkChatMessage · Cloudflare Realtime docs
  head_html: <title>RtkChatMessage · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkChatMessage component (React Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/index.md"><meta property="og:title" content="RtkChatMessage · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkChatMessage component (React Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/#page","headline":"RtkChatMessage \u00b7 Cloudflare Realtime docs","description":"API reference for RtkChatMessage component (React Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/
  schema: 1
---
<p>@deprecated <code>rtk-chat-message</code> is deprecated and will be removed soon. Use <code>rtk-message-view</code> instead.</p>
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
<td><code>alignRight</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>aligns message to right</td>
</tr>
<tr>
<td><code>canDelete</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>can delete message</td>
</tr>
<tr>
<td><code>canEdit</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>can edit message</td>
</tr>
<tr>
<td><code>canPin</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>can pin this message</td>
</tr>
<tr>
<td><code>canReply</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>can quote reply this message</td>
</tr>
<tr>
<td><code>child</code></td>
<td><code>HTMLElement</code></td>
<td>✅</td>
<td>-</td>
<td>Child</td>
</tr>
<tr>
<td><code>disableControls</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>disables controls</td>
</tr>
<tr>
<td><code>hideAvatar</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>hides avatar</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>isContinued</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>is continued</td>
</tr>
<tr>
<td><code>isSelf</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>if sender is self</td>
</tr>
<tr>
<td><code>isUnread</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>is unread</td>
</tr>
<tr>
<td><code>leftAlign</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether to left align the chat bubbles</td>
</tr>
<tr>
<td><code>message</code></td>
<td><code>Message</code></td>
<td>✅</td>
<td>-</td>
<td>message item</td>
</tr>
<tr>
<td><code>senderDisplayPicture</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>sender display picture url</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n1</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkChatMessage } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkChatMessage /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkChatMessage } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkChatMessage&#10;      alignRight={true}&#10;      canDelete={true}&#10;      canEdit={true}&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
