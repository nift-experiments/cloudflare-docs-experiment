---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar-ui/
  description: API reference for rtk-sidebar-ui component (Angular Library)
  full_title: rtk-sidebar-ui · Cloudflare Realtime docs
  head_html: <title>rtk-sidebar-ui · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for rtk-sidebar-ui component (Angular Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar-ui/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar-ui/index.md"><meta property="og:title" content="rtk-sidebar-ui · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for rtk-sidebar-ui component (Angular Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar-ui/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar-ui/#page","headline":"rtk-sidebar-ui \u00b7 Cloudflare Realtime docs","description":"API reference for rtk-sidebar-ui component (Angular Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar-ui/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar-ui/
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
<td><code>currentTab</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Default tab to open</td>
</tr>
<tr>
<td><code>focusCloseButton</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Option to focus close button when opened</td>
</tr>
<tr>
<td><code>hideCloseAction</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Hide Close Action</td>
</tr>
<tr>
<td><code>hideHeader</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Hide Main Header</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>{ people: string; people_checked: string; chat: string; poll: string; participants: string; rocket: string; call_end: string; share: string; mic_on: string; mic_off: string; video_on: string; video_off: string; share_screen_start: string; share_screen_stop: string; share_screen_person: string; clock: string; dismiss: string; send: string; search: string; more_vertical: string; chevron_down: string; chevron_up: string; chevron_left: string; chevron_right: string; settings: string; wifi: string; speaker: string; speaker_off: string; download: string; full_screen_maximize: string; full_screen_minimize: string; copy: string; attach: string; image: string; emoji_multiple: string; image_off: string; disconnected: string; wand: string; recording: string; subtract: string; stop_recording: string; warning: string; pin: string; pin_off: string; spinner: string; breakout_rooms: string; add: string; shuffle: string; edit: string; delete: string; back: string; save: string; web: string; checkmark: string; spotlight: string; join_stage: string; leave_stage: string; pip_off: string; pip_on: string; signal_1: string; signal_2: string; signal_3: string; signal_4: string; signal_5: string; start_livestream: string; stop_livestream: string; viewers: string; debug: string; info: string; devices: string; horizontal_dots: string; ai_sparkle: string; meeting_ai: string; captionsOn: string; captionsOff: string; play: string; pause: string; fastForward: string; minimize: string; maximize: string; }</code></td>
<td>✅</td>
<td>-</td>
<td>Icon Pack</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n1</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
<tr>
<td><code>tabs</code></td>
<td><code>RtkSidebarTab1[]</code></td>
<td>✅</td>
<td>-</td>
<td>Tabs</td>
</tr>
<tr>
<td><code>view</code></td>
<td><code>RtkSidebarView1</code></td>
<td>✅</td>
<td>-</td>
<td>View</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-sidebar-ui&gt;&lt;/rtk-sidebar-ui&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre tabindex="0"><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-sidebar-ui&#10; currentTab=&quot;example&quot;&#10; [focusCloseButton]=&quot;true&quot;&#10; [hideCloseAction]=&quot;true&quot;&gt;&#10;&lt;/rtk-sidebar-ui&gt;&#10;</code></pre>
