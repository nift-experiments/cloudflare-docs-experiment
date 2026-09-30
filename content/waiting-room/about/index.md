---
cp9:
  canonical: https://developers.cloudflare.com/waiting-room/about/
  description: How Cloudflare Waiting Room queues visitors during traffic surges.
  full_title: About · Cloudflare Waiting Room docs
  head_html: <title>About · Cloudflare Waiting Room docs</title><meta name="generator" content="Nift"><meta name="description" content="How Cloudflare Waiting Room queues visitors during traffic surges."><link rel="canonical" href="https://developers.cloudflare.com/waiting-room/about/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waiting-room/about/index.md"><meta property="og:title" content="About · Cloudflare Waiting Room docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Cloudflare Waiting Room queues visitors during traffic surges."><meta property="og:url" content="https://developers.cloudflare.com/waiting-room/about/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Waiting Room"><meta name="algolia_product_filter" content="Waiting Room"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Waiting Room"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waiting-room/about/#page","headline":"About \u00b7 Cloudflare Waiting Room docs","description":"How Cloudflare Waiting Room queues visitors during traffic surges.","url":"https://developers.cloudflare.com/waiting-room/about/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waiting-room/about/
  schema: 1
---
<p>Waiting Room queues visitors when your traffic approaches a previously defined threshold that might otherwise bring an application down.</p>
<p><img src="/assets/upstream/images/waiting-room/waiting-room-process-flow.png" alt="Waiting Room process flow showing how a request is managed by Cloudflare and placed in a waiting room before reaching the origin website" /></p>
<h2 id="user-flow">User flow</h2>
<p>Once you have <a href="/waiting-room/get-started/">created and activated a waiting room</a> for a specific application page:</p>
<ul>
<li>
<p>If a page is not experiencing heavy traffic, a visitor accesses the page directly.</p>
</li>
<li>
<p>If page traffic approaches a <a href="/waiting-room/reference/configuration-settings/#session-duration">user-defined threshold</a>, a visitor enters a virtual waiting room until it is their turn to access the page:</p>
<ul>
<li>Each user receives a <a href="/waiting-room/reference/waiting-room-cookie/">cookie</a> to manage the dynamic outflow of requests from the waiting room to the origin website in <a href="/waiting-room/reference/queueing-methods/#first-in-first-out-fifo">First In First Out (FIFO)</a> order.</li>
<li>While in the waiting room, the user's browser automatically refreshes every 20 seconds to give them updated information about their estimated wait time.</li>
<li>When a user exits the waiting room and reaches your application, they can leave and re-enter without waiting for the length of time specified by the <a href="/waiting-room/reference/configuration-settings/#session-duration">session duration</a>.</li>
<li>Because waiting rooms support dynamic inflow and <a href="/waiting-room/reference/configuration-settings/#session-duration">outflow</a>, new spots appear more quickly and estimated wait times are lower and more accurate.</li>
</ul>
</li>
</ul>
<h2 id="architecture">Architecture</h2>
<p>Waiting Room is built on <a href="/workers/">Workers</a> that runs across a global network of Cloudflare data centers.</p>
<p>When a request comes to a host or path covered by a Waiting Room, that request goes to a Waiting Room Worker in the closest geographic data center. The Worker then needs to make a decision: whether to send users to the queue or the website.</p>
<p>That decision itself depends on two factors: <a href="/waiting-room/reference/configuration-settings/">admin-defined thresholds</a> and the Waiting Room state.</p>
<p>For admin-defined thresholds, the two measures that matter are <code>total active users</code> and <code>new users per minute</code>:</p>
<ul>
<li>
<p><code>total active users</code> is a target threshold for how many simultaneous users you want to allow on the pages covered by your waiting room.</p>
</li>
<li>
<p><code>new users per minute</code> defines the target threshold for the maximum rate of user influx to your website per minute.</p>
</li>
</ul>
<p>A sharp spike in either of these values might result in queuing. Another configuration that affects how we calculate <code>the total active users</code> is <code>session duration</code>. A user is considered active for <code>session duration</code> minutes since the request is made to any page covered by a waiting room.</p>
<p>The other factor is the Waiting Room state, which is maintained at the local data center level but then also changes continuously based on the traffic around the world. Each data center works with its own Waiting Room state. This state is a snapshot of the traffic pattern for the website around the world available at that point in time. The advantage of using this approach - making decisions at the Worker level - is that we can make decisions without any significant latency added to the request. The algorithm for Waiting Room dynamically allocates a certain number of slots available to each Worker based on the Waiting Room state. Queueing starts when the slots run out within the Worker. The lack of additional latency added enables the customers to turn on the waiting room all the time without worrying about extra latency to their users.</p>
<p>The Waiting Room state is updated with global information every few seconds. We have a pipeline set up in Cloudflare <a href="/durable-objects/">Durable Objects</a> that ensures changes in traffic get propagated around the world. This architecture ensures that we do not introduce additional latency, as well as that we are making decisions with as near-time accuracy as possible.</p>
<p>For even more details about the architecture and why we made these decisions, refer to our <a href="https://blog.cloudflare.com/how-waiting-room-queues">deep-dive technical blog</a>.</p>
