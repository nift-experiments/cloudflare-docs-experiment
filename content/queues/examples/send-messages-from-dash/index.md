---
cp9:
  canonical: https://developers.cloudflare.com/queues/examples/send-messages-from-dash/
  description: Use the dashboard to send messages to a queue.
  full_title: Cloudflare Queues - Sending messages from the dashboard · Cloudflare Queues docs
  head_html: <title>Cloudflare Queues - Sending messages from the dashboard · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the dashboard to send messages to a queue."><link rel="canonical" href="https://developers.cloudflare.com/queues/examples/send-messages-from-dash/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/examples/send-messages-from-dash/index.md"><meta property="og:title" content="Cloudflare Queues - Sending messages from the dashboard · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the dashboard to send messages to a queue."><meta property="og:url" content="https://developers.cloudflare.com/queues/examples/send-messages-from-dash/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/examples/send-messages-from-dash/#page","headline":"Cloudflare Queues - Sending messages from the dashboard \u00b7 Cloudflare Queues docs","description":"Use the dashboard to send messages to a queue.","url":"https://developers.cloudflare.com/queues/examples/send-messages-from-dash/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/examples/send-messages-from-dash/
  schema: 1
---
<p class="article-summary">Use the dashboard to send messages to a queue.</p>
<p>Sending messages from the dashboard allows you to debug Queues or queue consumers without a producer Worker.</p>
<p>To send messages from the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Queues</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the queue to send a message to.</li>
<li>Select the <strong>Messages</strong> tab.</li>
<li>Select <strong>Send</strong>.</li>
<li>Choose your message <strong>Content Type</strong>: <em>Text</em> or <em>JSON</em>.</li>
<li>Enter your message. Alternatively, drag a file over the textbox to upload a file as a message.</li>
<li>Select <strong>Send</strong>.</li>
</ol>
<p>Your message will be sent to the queue.</p>
<p>Refer to the <a href="/queues/get-started/">Get Started guide</a> to learn how to send messages to a queue from a Worker.</p>
