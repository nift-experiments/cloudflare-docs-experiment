---
cp9:
  canonical: https://developers.cloudflare.com/queues/examples/list-messages-from-dash/
  description: Use the dashboard to fetch and acknowledge the messages currently in a queue.
  full_title: Cloudflare Queues - Listing and acknowledging messages from the dashboard · Cloudflare Queues docs
  head_html: <title>Cloudflare Queues - Listing and acknowledging messages from the dashboard · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the dashboard to fetch and acknowledge the messages currently in a queue."><link rel="canonical" href="https://developers.cloudflare.com/queues/examples/list-messages-from-dash/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/examples/list-messages-from-dash/index.md"><meta property="og:title" content="Cloudflare Queues - Listing and acknowledging messages from the dashboard · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the dashboard to fetch and acknowledge the messages currently in a queue."><meta property="og:url" content="https://developers.cloudflare.com/queues/examples/list-messages-from-dash/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/examples/list-messages-from-dash/#page","headline":"Cloudflare Queues - Listing and acknowledging messages from the dashboard \u00b7 Cloudflare Queues docs","description":"Use the dashboard to fetch and acknowledge the messages currently in a queue.","url":"https://developers.cloudflare.com/queues/examples/list-messages-from-dash/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/examples/list-messages-from-dash/
  schema: 1
---
<p class="article-summary">Use the dashboard to fetch and acknowledge the messages currently in a queue.</p>
<h2 id="list-messages-from-the-dashboard">List messages from the dashboard</h2>
<p>Listing messages from the dashboard allows you to debug Queues or queue producers without a consumer Worker. Fetching a batch of messages to preview will not acknowledge or retry the message or affect its position in the queue. The queue can still be consumed normally by a consumer Worker.</p>
<p>To list messages in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11246.md")
</div>
<p>This will preview a batch of messages currently in the Queue.</p>
<h2 id="acknowledge-messages-from-the-dashboard">Acknowledge messages from the dashboard</h2>
<p>Acknowledging messages from the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> will permanently remove them from the queue, with equivalent behavior as <code>ack()</code> in a Worker.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11247.md")
</div>
<p>This will remove the selected messages from the queue and prevent consumers from processing them further.</p>
<p>Refer to the <a href="/queues/get-started/">Get Started guide</a> to learn how to process and acknowledge messages from a queue in a Worker.</p>
