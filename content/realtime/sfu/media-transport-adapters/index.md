---
cp9:
  canonical: https://developers.cloudflare.com/realtime/sfu/media-transport-adapters/
  description: Bridge WebRTC and other transport protocols using Realtime SFU media adapters.
  full_title: Media Transport Adapters · Cloudflare Realtime docs
  head_html: <title>Media Transport Adapters · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Bridge WebRTC and other transport protocols using Realtime SFU media adapters."><link rel="canonical" href="https://developers.cloudflare.com/realtime/sfu/media-transport-adapters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/sfu/media-transport-adapters/index.md"><meta property="og:title" content="Media Transport Adapters · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bridge WebRTC and other transport protocols using Realtime SFU media adapters."><meta property="og:url" content="https://developers.cloudflare.com/realtime/sfu/media-transport-adapters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/sfu/media-transport-adapters/#page","headline":"Media Transport Adapters \u00b7 Cloudflare Realtime docs","description":"Bridge WebRTC and other transport protocols using Realtime SFU media adapters.","url":"https://developers.cloudflare.com/realtime/sfu/media-transport-adapters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/sfu/media-transport-adapters/
  schema: 1
---
<p>Media Transport Adapters bridge WebRTC and other transport protocols. Adapters handle protocol conversion, codec transcoding, and bidirectional media flow between WebRTC sessions and external endpoints.</p>
<h2 id="what-adapters-do">What adapters do</h2>
<p>Adapters extend Realtime beyond WebRTC-to-WebRTC communication:</p>
<ul>
<li>Ingest audio/video from external sources into WebRTC sessions</li>
<li>Stream WebRTC media to external systems for processing or storage</li>
<li>Integrate with AI services for transcription, translation, or generation</li>
<li>Bridge WebRTC applications with legacy communication systems</li>
</ul>
<h2 id="available-adapters">Available adapters</h2>
<h3 id="websocket-adapter-beta">WebSocket adapter (beta)</h3>
<p>Stream audio and video between WebRTC tracks and WebSocket endpoints. Video is egress-only and is converted to JPEG. Currently in beta; the API may change.</p>
<p><a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">Learn more</a></p>
<h2 id="architecture">Architecture</h2>
<p>Media Transport Adapters operate as intermediaries between Cloudflare Realtime SFU sessions and external endpoints:</p>
<pre tabindex="0"><code class="language-mermaid">graph LR&#10;    A[WebRTC Client] &lt;--&gt; B[Realtime SFU Session]&#10;    B &lt;--&gt; C[Media Transport Adapter]&#10;    C &lt;--&gt; D[External Endpoint]&#10;</code></pre>
<h3 id="key-concepts">Key concepts</h3>
<p><strong>Adapter instance</strong>: Each connection creates a unique instance with an <code>adapterId</code> to manage its lifecycle.</p>
<p><strong>Location types</strong>:</p>
<ul>
<li><code>local</code> (Ingest): Receives media from external endpoints to create new WebRTC tracks</li>
<li><code>remote</code> (Stream): Sends media from existing WebRTC tracks to external endpoints</li>
</ul>
<p><strong>Codec support</strong>: Adapters convert between WebRTC and external system formats.</p>
<h2 id="common-use-cases">Common use cases</h2>
<h3 id="ai-processing">AI processing</h3>
<ul>
<li>Speech-to-text transcription</li>
<li>Text-to-speech generation</li>
<li>Real-time translation</li>
<li>Audio enhancement</li>
</ul>
<h3 id="media-recording">Media recording</h3>
<ul>
<li>Cloud recording</li>
<li>Content delivery networks</li>
<li>Media processing pipelines</li>
</ul>
<h3 id="legacy-integration">Legacy integration</h3>
<ul>
<li>Traditional telephony</li>
<li>Broadcasting infrastructure</li>
<li>Custom media servers</li>
</ul>
<h2 id="api-overview">API overview</h2>
<p>Media Transport Adapters are managed through the Realtime SFU API:</p>
<pre tabindex="0"><code>POST /v1/apps/{appId}/adapters/{adapterType}/new&#10;POST /v1/apps/{appId}/adapters/{adapterType}/close&#10;</code></pre>
<p>Each adapter type has specific configuration requirements and capabilities. Refer to individual adapter documentation for detailed API specifications.</p>
<h2 id="best-practices">Best practices</h2>
<ul>
<li>Close adapter instances when no longer needed</li>
<li>Implement reconnection logic for network failures</li>
<li>Choose codecs based on bandwidth and quality requirements</li>
<li>Secure endpoints with authentication for sensitive media</li>
</ul>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Each adapter type has specific codec and format support</li>
<li>Network latency between Cloudflare edge and external endpoints affects real-time performance</li>
<li>Maximum message size and streaming modes vary by adapter type</li>
</ul>
<h2 id="get-started">Get started</h2>
<p><a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter (beta)</a> - Stream audio and video between WebRTC and WebSocket endpoints (video egress to JPEG)</p>
