---
cp9:
  canonical: https://developers.cloudflare.com/realtime/sfu/sessions-tracks/
  description: Understand Realtime SFU core concepts including applications, sessions, and tracks.
  full_title: Sessions and Tracks · Cloudflare Realtime docs
  head_html: <title>Sessions and Tracks · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand Realtime SFU core concepts including applications, sessions, and tracks."><link rel="canonical" href="https://developers.cloudflare.com/realtime/sfu/sessions-tracks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/sfu/sessions-tracks/index.md"><meta property="og:title" content="Sessions and Tracks · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand Realtime SFU core concepts including applications, sessions, and tracks."><meta property="og:url" content="https://developers.cloudflare.com/realtime/sfu/sessions-tracks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/sfu/sessions-tracks/#page","headline":"Sessions and Tracks \u00b7 Cloudflare Realtime docs","description":"Understand Realtime SFU core concepts including applications, sessions, and tracks.","url":"https://developers.cloudflare.com/realtime/sfu/sessions-tracks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/sfu/sessions-tracks/
  schema: 1
---
<p>Cloudflare Realtime offers a simple yet powerful framework for building real-time experiences. At the core of this system are three key concepts: <strong>Applications</strong>,  <strong>Sessions</strong> and <strong>Tracks</strong>. Familiarizing yourself with these concepts is crucial for using Realtime.</p>
<h2 id="application">Application</h2>
<p>A Realtime Application is an environment within different Sessions and Tracks can interact. Examples of this could be production, staging or different environments where you'd want separation between Sessions and Tracks. Cloudflare Realtime usage can be queried at Application, Session or Track level.</p>
<h2 id="sessions">Sessions</h2>
<p>A <strong>Session</strong> in Cloudflare Realtime correlates directly to a WebRTC PeerConnection. It represents the establishment of a communication channel between a client and the nearest Cloudflare data center, as determined by Cloudflare's anycast routing. Typically, a client will maintain a single Session, encompassing all communications between the client and Cloudflare.</p>
<ul>
<li><strong>One-to-One Mapping with PeerConnection</strong>: Each Session is a direct representation of a WebRTC PeerConnection, facilitating real-time media data transfer.</li>
<li><strong>Anycast Routing</strong>: The client connects to the closest Cloudflare data center, optimizing latency and performance.</li>
<li><strong>Unified Communication Channel</strong>: A single Session can handle all types of communication between a client and Cloudflare, ensuring streamlined data flow.</li>
</ul>
<h2 id="tracks">Tracks</h2>
<p>Within a Session, there can be one or more <strong>Tracks</strong>.</p>
<ul>
<li><strong>Tracks map to MediaStreamTrack</strong>: Tracks align with the MediaStreamTrack concept, facilitating audio, video, or data transmission.</li>
<li><strong>Globally Unique Ids</strong>: When you push a track to Cloudflare, it is assigned a unique ID, which can then be used to pull the track into another session elsewhere.</li>
<li><strong>Available globally</strong>: The ability to push and pull tracks is central to what makes Realtime a versatile tool for real-time applications. Each track is available globally to be retrieved from any Session within an App.</li>
</ul>
<h2 id="realtime-as-a-programmable-switchboard">Realtime as a Programmable &quot;Switchboard&quot;</h2>
<p>The analogy of a switchboard is apt for understanding Realtime. Historically, switchboard operators connected calls by manually plugging in jacks. Similarly, Realtime allows for the dynamic routing of media streams, acting as a programmable switchboard for modern real-time communication.</p>
<h2 id="beyond-rooms-users-and-participants">Beyond &quot;Rooms&quot;, &quot;Users&quot;, and &quot;Participants&quot;</h2>
<p>While many SFUs utilize concepts like &quot;rooms&quot; to manage media streams among users, this approach has scalability and flexibility limitations. Cloudflare Realtime opts for a more granular and flexible model with Sessions and Tracks, enabling a wide range of use cases:</p>
<ul>
<li>Large-scale remote events, like 'fireside chats' with thousands of participants.</li>
<li>Interactive conversations with the ability to bring audience members &quot;on stage.&quot;</li>
<li>Educational applications where an instructor can present to multiple virtual classrooms simultaneously.</li>
</ul>
<h3 id="presence-protocol-vs-media-flow">Presence Protocol vs. Media Flow</h3>
<p>Realtime distinguishes between the presence protocol and media flow, allowing for scalability and flexibility in real-time applications. This separation enables developers to craft tailored experiences, from intimate calls to massive, low-latency broadcasts.</p>
