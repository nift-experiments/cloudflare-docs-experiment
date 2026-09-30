---
cp9:
  canonical: https://developers.cloudflare.com/waiting-room/how-to/control-waiting-room/
  description: Manage active user limits and queueing behavior.
  full_title: Control waiting room traffic · Cloudflare Waiting Room docs
  head_html: <title>Control waiting room traffic · Cloudflare Waiting Room docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage active user limits and queueing behavior."><link rel="canonical" href="https://developers.cloudflare.com/waiting-room/how-to/control-waiting-room/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waiting-room/how-to/control-waiting-room/index.md"><meta property="og:title" content="Control waiting room traffic · Cloudflare Waiting Room docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage active user limits and queueing behavior."><meta property="og:url" content="https://developers.cloudflare.com/waiting-room/how-to/control-waiting-room/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Waiting Room"><meta name="algolia_product_filter" content="Waiting Room"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Waiting Room"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waiting-room/how-to/control-waiting-room/#page","headline":"Control waiting room traffic \u00b7 Cloudflare Waiting Room docs","description":"Manage active user limits and queueing behavior.","url":"https://developers.cloudflare.com/waiting-room/how-to/control-waiting-room/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waiting-room/how-to/control-waiting-room/
  schema: 1
---
<p>To change whether and how traffic reaches a waiting room, update the values for <strong>Enabled</strong>, <strong>Queue All</strong>, and <strong>Queueing Method</strong> on your waiting room.</p>
<h2 id="enable-a-waiting-room">Enable a waiting room</h2>
<p>To enable a waiting room:</p>
<ol>
<li>Go to <strong>Traffic</strong> &gt; <strong>Waiting Room</strong>.</li>
<li>On a waiting room, set <strong>Enabled</strong> to <strong>On</strong>.</li>
</ol>
<h2 id="queue-options">Queue options</h2>
<p>By default, an active waiting room puts visitors in a queue when traffic approaches the target thresholds defined in <strong>Total active users</strong> and <strong>New users per minute</strong>. Refer to <a href="/waiting-room/how-to/monitor-waiting-room/#queueing-activation">Queueing activation</a> for more information.</p>
<p>However, if you want all visitors to be queued for a predefined amount of time — in preparation for a product release or other time-based event — use the <a href="/waiting-room/additional-options/create-events/">Create scheduled events</a> option.</p>
<p>You may also use the <strong>Queue-all</strong> option on a waiting room as an emergency stop to all traffic during unexpected or temporary downtime. As long as the waiting room is active and <strong>Queue-all</strong> is enabled, no traffic will reach your application.</p>
<h3 id="queue-visitors-when-necessary">Queue visitors when necessary</h3>
<p>To queue visitors only when necessary:</p>
<ol>
<li>Go to <strong>Traffic</strong> &gt; <strong>Waiting Room</strong>.</li>
<li>On a waiting room, set <strong>Enabled</strong> to <strong>On</strong>.</li>
<li>Your waiting room will begin queueing visitors once it approaches the target traffic thresholds defined in <a href="/waiting-room/reference/configuration-settings/"><strong>Total active users</strong></a> and in <a href="/waiting-room/reference/configuration-settings/"><strong>New users per minute</strong></a>.</li>
</ol>
<h3 id="queue-all-visitors">Queue all visitors</h3>
<p>To queue all visitors prior to a time-based offering, set up a pre-queue as part of a <a href="/waiting-room/additional-options/create-events/#create-an-event-from-the-dashboard">waiting room event</a>.</p>
<p>To start queueing all new visitors without a scheduled event:</p>
<ol>
<li>Go to <strong>Traffic</strong> &gt; <strong>Waiting Room</strong>.</li>
<li>On a waiting room:
<ol>
<li>Ensure <strong>Enabled</strong> is set to <strong>On</strong>.</li>
<li>Set <strong>Queue-all</strong> to <strong>On</strong>.</li>
</ol>
</li>
<li>Your waiting room will begin queueing all new visitors and will not allow any new visitors to the path protected by your waiting room. Queue-all will override all other waiting room settings, including event settings.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/15752.md")
</aside>
<ol start="4">
<li>To begin allowing visitors to the path protected by your waiting room, set <strong>Queue-all</strong> to <strong>Off</strong>.</li>
</ol>
<h2 id="queueing-method">Queueing method</h2>
<p>For more details about queueing method, refer to <a href="/waiting-room/reference/queueing-methods/">Queueing methods</a>.</p>
