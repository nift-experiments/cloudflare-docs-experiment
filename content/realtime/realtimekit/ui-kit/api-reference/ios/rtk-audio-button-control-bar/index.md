---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/
  description: API reference for RtkAudioButtonControlBar component (iOS Library)
  full_title: RtkAudioButtonControlBar · Cloudflare Realtime docs
  head_html: <title>RtkAudioButtonControlBar · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkAudioButtonControlBar component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/index.md"><meta property="og:title" content="RtkAudioButtonControlBar · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkAudioButtonControlBar component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/#page","headline":"RtkAudioButtonControlBar \u00b7 Cloudflare Realtime docs","description":"API reference for RtkAudioButtonControlBar component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/
  schema: 1
---
<p>A control bar button that toggles the local microphone on and off.
Checks microphone permissions before toggling.</p>
<h2 id="initializer-parameters">Initializer parameters</h2>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit client instance</td>
</tr>
<tr>
<td><code>onClick</code></td>
<td><code>((RtkAudioButtonControlBar) -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Closure called when the button is tapped</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkControlBarButtonAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Appearance configuration for the button</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let audioButton = RtkAudioButtonControlBar(meeting: rtkClient)&#10;view.addSubview(audioButton)&#10;</code></pre>
<h3 id="with-tap-handler">With tap handler</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let audioButton = RtkAudioButtonControlBar(&#10;    meeting: rtkClient,&#10;    onClick: { button in&#10;        print(&quot;Audio toggled&quot;)&#10;    }&#10;)&#10;view.addSubview(audioButton)&#10;</code></pre>
