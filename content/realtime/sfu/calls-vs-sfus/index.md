---
cp9:
  canonical: https://developers.cloudflare.com/realtime/sfu/calls-vs-sfus/
  description: Compare Cloudflare Realtime SFU with traditional centralized SFUs for WebRTC applications.
  full_title: Realtime vs Regular SFUs · Cloudflare Realtime docs
  head_html: <title>Realtime vs Regular SFUs · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Compare Cloudflare Realtime SFU with traditional centralized SFUs for WebRTC applications."><link rel="canonical" href="https://developers.cloudflare.com/realtime/sfu/calls-vs-sfus/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/sfu/calls-vs-sfus/index.md"><meta property="og:title" content="Realtime vs Regular SFUs · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Compare Cloudflare Realtime SFU with traditional centralized SFUs for WebRTC applications."><meta property="og:url" content="https://developers.cloudflare.com/realtime/sfu/calls-vs-sfus/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/sfu/calls-vs-sfus/#page","headline":"Realtime vs Regular SFUs \u00b7 Cloudflare Realtime docs","description":"Compare Cloudflare Realtime SFU with traditional centralized SFUs for WebRTC applications.","url":"https://developers.cloudflare.com/realtime/sfu/calls-vs-sfus/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/sfu/calls-vs-sfus/
  schema: 1
---
<h2 id="cloudflare-realtime-vs-traditional-sfus">Cloudflare Realtime vs. Traditional SFUs</h2>
<p>Cloudflare Realtime represents a paradigm shift in building real-time applications by leveraging a distributed real-time data plane. It creates a seamless experience in real-time communication, transcending traditional geographical limitations and scalability concerns. Realtime is designed for developers looking to integrate WebRTC functionalities in a server-client architecture without delving deep into the complexities of regional scaling or server management.</p>
<h3 id="the-limitations-of-centralized-sfus">The Limitations of Centralized SFUs</h3>
<p>Selective Forwarding Units (SFUs) play a critical role in managing WebRTC connections by selectively forwarding media streams to participants in a video call. However, their centralized nature introduces inherent limitations:</p>
<ul>
<li>
<p><strong>Regional Dependency:</strong> A centralized SFU requires a specific region for deployment, leading to latency issues for global users except for those in proximity to the selected region.</p>
</li>
<li>
<p><strong>Scalability Concerns:</strong> Scaling a centralized SFU to meet global demand can be challenging and inefficient, often requiring additional infrastructure and complexity.</p>
</li>
</ul>
<h3 id="how-is-cloudflare-realtime-different">How is Cloudflare Realtime different?</h3>
<p>Cloudflare Realtime addresses these limitations by leveraging Cloudflare's global network infrastructure:</p>
<ul>
<li>
<p><strong>Global Distribution Without Regions:</strong> Unlike traditional SFUs, Cloudflare Realtime operates on a global scale without regional constraints. It utilizes Cloudflare's extensive network of over 250 locations worldwide to ensure low-latency video forwarding, making it fast and efficient for users globally.</p>
</li>
<li>
<p><strong>Decentralized Architecture:</strong> There are no dedicated servers for Realtime. Every server within Cloudflare's network contributes to handling Realtime, ensuring scalability and reliability. This approach mirrors the distributed nature of Cloudflare's products such as 1.1.1.1 DNS or Cloudflare's CDN.</p>
</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/11588.md")
</aside>
<h2 id="how-cloudflare-realtime-works">How Cloudflare Realtime Works</h2>
<h3 id="establishing-peer-connections">Establishing Peer Connections</h3>
<p>To initiate a real-time communication session, an end user's client establishes a WebRTC PeerConnection to the nearest Cloudflare location. This connection benefits from anycast routing, optimizing for the lowest possible latency.</p>
<h3 id="signaling-and-media-stream-management">Signaling and Media Stream Management</h3>
<ul>
<li>
<p><strong>HTTPS API for Signaling:</strong> Cloudflare Realtime simplifies signaling with a straightforward HTTPS API. This API manages the initiation and coordination of media streams, enabling clients to push new MediaStreamTracks or request these tracks from the server.</p>
</li>
<li>
<p><strong>Efficient Media Handling:</strong> Unlike traditional approaches that require multiple connections for different media streams from different clients, Cloudflare Realtime maintains a single PeerConnection per client. This streamlined process reduces complexity and improves performance by handling both the push and pull of media through a singular connection.</p>
</li>
</ul>
<h3 id="application-level-management">Application-Level Management</h3>
<p>Cloudflare Realtime delegates the responsibility of state management and participant tracking to the application layer. Developers are empowered to design their logic for handling events such as participant joins or media stream updates, offering flexibility to create tailored experiences in applications.</p>
<h2 id="getting-started-with-cloudflare-realtime">Getting Started with Cloudflare Realtime</h2>
<p>Integrating Cloudflare Realtime into your application promises a straightforward and efficient process, removing the hurdles of regional scalability and server management so you can focus on creating engaging real-time experiences for users worldwide.</p>
