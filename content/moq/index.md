---
cp9:
  canonical: https://developers.cloudflare.com/moq/
  description: Deliver low-latency live media content using the MoQ protocol over QUIC transport on Cloudflare's network.
  full_title: Overview · Cloudflare MoQ docs
  head_html: <title>Overview · Cloudflare MoQ docs</title><meta name="generator" content="Nift"><meta name="description" content="Deliver low-latency live media content using the MoQ protocol over QUIC transport on Cloudflare&#x27;s network."><link rel="canonical" href="https://developers.cloudflare.com/moq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/moq/index.md"><meta property="og:title" content="Overview · Cloudflare MoQ docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deliver low-latency live media content using the MoQ protocol over QUIC transport on Cloudflare&#x27;s network."><meta property="og:url" content="https://developers.cloudflare.com/moq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="MoQ"><meta name="algolia_product_filter" content="MoQ"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="MoQ"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/moq/#page","headline":"Overview \u00b7 Cloudflare MoQ docs","description":"Deliver low-latency live media content using the MoQ protocol over QUIC transport on Cloudflare's network.","url":"https://developers.cloudflare.com/moq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /moq/
  schema: 1
---
<p>MoQ (Media over QUIC) is a protocol for delivering live media content using QUIC transport. It provides efficient, low-latency media streaming by leveraging QUIC's multiplexing and connection management capabilities.</p>
<p>MoQ is designed to be an Internet infrastructure level service that provides media delivery to applications, similar to how HTTP provides content delivery and WebRTC provides real-time communication.</p>
<p>Cloudflare currently supports <a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-14</a> and <a href="https://www.ietf.org/archive/id/draft-ietf-moq-transport-16.html">draft-16</a> of the MoQ Transport specification. For a full breakdown of supported messages per draft, refer to <a href="/moq/feature-matrix/">MoQ Feature Matrix</a>.</p>
<p>For the most up-to-date documentation on the protocol, please visit the IETF working group documentation.</p>
<h2 id="get-started">Get started</h2>
<p>Cloudflare MoQ relays are available through the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and the <a href="/api/resources/moq">API</a>. They are free to use during the beta period.</p>
<h3 id="provision-a-relay">Provision a relay</h3>
<p>Each relay provides an isolated scope — your namespaces, tracks, and objects are separated from those belonging to other relays. You control who can publish and who can subscribe by issuing tokens scoped to the operations each client needs.</p>
<p>To create a relay via the API:</p>
<pre tabindex="0"><code class="language-sh">curl -X POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/moq/relays&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;name&quot;: &quot;My Relay&quot;}&#x27;&#10;</code></pre>
<p>Cloudflare returns a relay ID and two default tokens: one that can publish and subscribe, and one that can only subscribe. Token secrets are shown once in the response and never stored.</p>
<p>You can also create and manage relays in the Cloudflare dashboard under <strong>Media</strong> &gt; <strong>Realtime</strong> &gt; <strong>MoQ Relay</strong>.</p>
<h3 id="connect-a-publisher-and-subscriber-draft-16">Connect a publisher and subscriber (draft-16)</h3>
<p>Draft-16 requires authentication. Clients send a token in the URL path when opening a MoQ session. Using the open-source <a href="https://github.com/cloudflare/moq-rs">moq-rs</a> tools:</p>
<p><strong>Publisher:</strong></p>
<pre tabindex="0"><code class="language-sh">ffmpeg -stream_loop -1 -re -i input.mp4 \&#10;  &#45;f mp4 -movflags empty_moov+frag_every_frame+separate_moof+omit_tfhd_offset - \&#10;  | moq-pub --name my-namespace \&#10;    &quot;https://draft-16.cloudflare.mediaoverquic.com/&lt;publish_subscribe_token&gt;&quot;&#10;</code></pre>
<p><strong>Subscriber:</strong></p>
<pre tabindex="0"><code class="language-sh">moq-sub --name my-namespace \&#10;  &quot;https://draft-16.cloudflare.mediaoverquic.com/&lt;subscribe_token&gt;&quot; \&#10;  | ffplay -hide_banner -&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="token-security">Token security</h3>
@markup("md", "content/.markup/bodies/742.md")
</aside>
<h3 id="connect-a-publisher-and-subscriber-draft-14">Connect a publisher and subscriber (draft-14)</h3>
<p>Draft-14 clients connect to:</p>
<pre tabindex="0"><code class="language-txt">https://draft-14.cloudflare.mediaoverquic.com/&#10;</code></pre>
<h3 id="test-draft-18">Test draft-18</h3>
<p>Cloudflare is working on draft-18 support ahead of a global deployment. To test against a draft-18 relay in the meantime, refer to <a href="https://github.com/englishm/moq-interop-runner">moq-interop-runner</a>.</p>
