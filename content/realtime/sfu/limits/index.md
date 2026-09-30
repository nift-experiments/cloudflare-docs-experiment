---
cp9:
  canonical: https://developers.cloudflare.com/realtime/sfu/limits/
  description: Realtime SFU rate limits, track timeouts, session constraints, and free tier quotas.
  full_title: Limits, timeouts and quotas · Cloudflare Realtime docs
  head_html: <title>Limits, timeouts and quotas · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Realtime SFU rate limits, track timeouts, session constraints, and free tier quotas."><link rel="canonical" href="https://developers.cloudflare.com/realtime/sfu/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/sfu/limits/index.md"><meta property="og:title" content="Limits, timeouts and quotas · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Realtime SFU rate limits, track timeouts, session constraints, and free tier quotas."><meta property="og:url" content="https://developers.cloudflare.com/realtime/sfu/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/sfu/limits/#page","headline":"Limits, timeouts and quotas \u00b7 Cloudflare Realtime docs","description":"Realtime SFU rate limits, track timeouts, session constraints, and free tier quotas.","url":"https://developers.cloudflare.com/realtime/sfu/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/sfu/limits/
  schema: 1
---
<p>Understanding the limits and timeouts of Cloudflare Realtime is crucial for optimizing the performance and reliability of your applications. This section outlines the key constraints and behaviors you should be aware of when integrating Cloudflare Realtime into your app.</p>
<h2 id="free">Free</h2>
<ul>
<li>Each account gets 1,000GB/month of data transfer from Cloudflare to your client for free.</li>
<li>Data transfer from your client to Cloudflare is always free of charge.</li>
</ul>
<h2 id="limits">Limits</h2>
<ul>
<li>
<p><strong>API Realtime per Session</strong>: You can make up to 50 API calls per second for each session. There is no ratelimit on a App basis, just sessions.</p>
</li>
<li>
<p><strong>Tracks per API Call</strong>: Up to 64 tracks can be added with a single API call. If you need to add more tracks to a session, you should distribute them across multiple API calls.</p>
</li>
<li>
<p><strong>Tracks per Session</strong>: There's no upper limit to the number of tracks a session can contain, the practical limit is governed by your connection's bandwidth to and from Cloudflare.</p>
</li>
<li>
<p><strong>DataChannel canReply exclusivity</strong>: At most one subscriber may hold <code>canReply</code> for a given publisher DataChannel at a time. Granting <code>canReply</code> to another subscriber replaces the previous selection. The publisher receives reverse traffic only, and it is not fanned out to other subscribers. For more information, refer to <a href="/realtime/sfu/datachannels/#return-to-publisher-canreply">Return to publisher (canReply)</a>.</p>
</li>
</ul>
<h2 id="inactivity-timeout">Inactivity Timeout</h2>
<ul>
<li><strong>Track Timeout</strong>: Tracks will automatically timeout and be garbage collected after 30 seconds of inactivity, where inactivity is defined as no media packets being received by Cloudflare. This mechanism ensures efficient use of resources and session cleanliness across all Sessions that use a track.</li>
<li><strong>DataChannel acknowledgment timeout</strong>: When <code>waitForAck</code> is enabled on a remote DataChannel, the subscriber must send its first message (the acknowledgment) within 30 seconds of creating the channel. If it does not, the SFU tears down the gated channel and forwards no messages. Create the remote DataChannel again to retry.</li>
</ul>
<h2 id="peerconnection-requirements">PeerConnection Requirements</h2>
<ul>
<li><strong>Session State</strong>: For any operation on a session (e.g., pulling or pushing tracks), the PeerConnection state must be <code>connected</code>. Operations will block for up to 5 seconds awaiting this state before timing out. This ensures that only active and viable sessions are engaged in media transmission.</li>
</ul>
<h2 id="handling-connectivity-issues">Handling Connectivity Issues</h2>
<ul>
<li><strong>Internet Connectivity Considerations</strong>: The potential for internet connectivity loss between the client and Cloudflare is an operational reality that must be addressed. Implementing a detection and reconnection strategy is recommended to maintain session continuity. This could involve periodic 'heartbeat' signals to your backend server to monitor connectivity status. Upon detecting connectivity issues, automatically attempting to reconnect and establish a new session is advised. Sessions and tracks will remain available for reuse for 30 seconds before timing out, providing a brief window for reconnection attempts.</li>
</ul>
<p>Adhering to these limits and understanding the timeout behaviors will help ensure that your applications remain responsive and stable while providing a seamless user experience.</p>
<h2 id="supported-codecs">Supported Codecs</h2>
<p>Cloudflare Realtime supports the following codecs:</p>
<h3 id="supported-video-codecs">Supported video codecs</h3>
<ul>
<li><strong>H264</strong></li>
<li><strong>H265</strong></li>
<li><strong>VP8</strong></li>
<li><strong>VP9</strong></li>
<li><strong>AV1</strong></li>
</ul>
<h3 id="supported-audio-codecs">Supported audio codecs</h3>
<ul>
<li><strong>Opus</strong></li>
<li><strong>G.711 PCM (A-law)</strong></li>
<li><strong>G.711 PCM (µ-law)</strong></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11574.md")
</aside>
