---
cp9:
  canonical: https://developers.cloudflare.com/queues/configuration/pause-purge/
  description: Pause message delivery or purge all messages from a Cloudflare Queue.
  full_title: Pause and Purge · Cloudflare Queues docs
  head_html: <title>Pause and Purge · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Pause message delivery or purge all messages from a Cloudflare Queue."><link rel="canonical" href="https://developers.cloudflare.com/queues/configuration/pause-purge/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/configuration/pause-purge/index.md"><meta property="og:title" content="Pause and Purge · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pause message delivery or purge all messages from a Cloudflare Queue."><meta property="og:url" content="https://developers.cloudflare.com/queues/configuration/pause-purge/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/configuration/pause-purge/#page","headline":"Pause and Purge \u00b7 Cloudflare Queues docs","description":"Pause message delivery or purge all messages from a Cloudflare Queue.","url":"https://developers.cloudflare.com/queues/configuration/pause-purge/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/configuration/pause-purge/
  schema: 1
---
<h2 id="pause-delivery">Pause Delivery</h2>
<p>You can pause delivery of messages from your queue to any connected consumers. Pausing a queue is useful when managing downtime (for example, if your consumer Worker is unhealthy) without losing any messages.</p>
<p>Queues continue to receive and store messages even while delivery is paused. Messages in a paused queue are still subject to expiry, if the messages become older than the queue message retention period.</p>
<p>Pausing affects both <a href="/queues/reference/how-queues-works#consumers">push-based consumer Workers</a> and <a href="/queues/configuration/pull-consumers">pull based consumers</a>.</p>
<h3 id="pause-and-resume-delivery-using-wrangler">Pause and resume delivery using Wrangler</h3>
<p>The following command will pause message delivery from your queue:</p>
<pre tabindex="0"><code class="language-sh">$ npx wrangler queues pause-delivery &lt;QUEUE-NAME&gt;&#10;</code></pre>
<ul>
<li><code>queue-name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the queue for which delivery should be paused.</li>
</ul>
</li>
</ul>
<p>The following command will resume message delivery:</p>
<pre tabindex="0"><code class="language-sh">$ npx wrangler queues resume-delivery &lt;QUEUE-NAME&gt;&#10;</code></pre>
<ul>
<li><code>queue-name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the queue for which delivery should be resumed.</li>
</ul>
</li>
</ul>
<h3 id="what-happens-to-http-pull-consumers-with-a-paused-queue">What happens to HTTP Pull consumers with a paused queue?</h3>
When a queue is paused, messages cannot be pulled by an [HTTP pull based consumer](/queues/configuration/pull-consumers). Requests to pull messages will receive a `409` response, along with an error message stating `queue_delivery_paused`.
<h2 id="purge-queue">Purge queue</h2>
Purging a queue permanently deletes any messages currently stored in the Queue. Purging is useful while developing a new application, especially to clear out any test data. It can also be useful in production to handle scenarios when a batch of bad messages have been sent to a Queue.
<p>Note that any in flight messages, which are currently being processed by consumers, might still be processed. Messages sent to a queue during a purge operation might not be purged. Any delayed messages will also be deleted from the queue.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11262.md")
</aside>
<h3 id="purge-queue-using-wrangler">Purge queue using Wrangler</h3>
The following command will purge messages from your queue. You will be prompted to enter the queue name to confirm the operation.
<pre tabindex="0"><code class="language-sh">$ npx wrangler queues purge &lt;QUEUE-NAME&gt;&#10;<p>This operation will permanently delete all the messages in Queue &lt;QUEUE-NAME&gt;. Type &lt;QUEUE-NAME&gt; to proceed.&#10;</code></pre></p>
<h3 id="does-purging-a-queue-affect-my-bill">Does purging a Queue affect my bill?</h3>
Purging a queue counts as a single billable operation, regardless of how many messages are deleted. For example, if you purge a queue which has 100 messages, all 100 messages will be permanently deleted, and you will be billed for 1 billable operation. Refer to the [pricing](/queues/platform/pricing) page for more information about how Queues is billed.
