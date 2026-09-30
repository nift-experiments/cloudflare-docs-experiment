---
cp9:
  canonical: https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/
  description: Learn how to create, view, and delete event subscriptions for your queues.
  full_title: Manage event subscriptions · Cloudflare Queues docs
  head_html: <title>Manage event subscriptions · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to create, view, and delete event subscriptions for your queues."><link rel="canonical" href="https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/index.md"><meta property="og:title" content="Manage event subscriptions · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to create, view, and delete event subscriptions for your queues."><meta property="og:url" content="https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/#page","headline":"Manage event subscriptions \u00b7 Cloudflare Queues docs","description":"Learn how to create, view, and delete event subscriptions for your queues.","url":"https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/event-subscriptions/manage-event-subscriptions/
  schema: 1
---
<p>Learn how to:</p>
<ul>
<li>Create event subscriptions to receive messages from Cloudflare services.</li>
<li>View existing subscriptions on your queues.</li>
<li>Delete subscriptions you no longer need.</li>
</ul>
<h2 id="create-subscription">Create subscription</h2>
<p>Creating a subscription allows your queue to receive messages when events occur in Cloudflare services. You can specify which source and events you want to subscribe to.</p>
<h3 id="dashboard">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11248.md")
</div>
<h3 id="wrangler-cli">Wrangler CLI</h3>
<p>To create a subscription using Wrangler, run the <a href="/queues/reference/wrangler-commands/#queues-subscription-create"><code>queues subscription create command</code></a>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler queues subscription create &lt;queue-name&gt; --source &lt;source-type&gt; --events &lt;event1,event2&gt; --&lt;source-specific-option&gt; &lt;value&gt;&#10;</code></pre>
<p>To learn more about which sources and events you can subscribe to, refer to <a href="/queues/event-subscriptions/events-schemas/">Events &amp; schemas</a>.</p>
<h2 id="view-existing-subscriptions">View existing subscriptions</h2>
<p>You can view all subscriptions configured for a queue to see what events it is currently receiving.</p>
<h3 id="dashboard-1">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11249.md")
</div>
<h3 id="wrangler-cli-1">Wrangler CLI</h3>
<p>To list subscriptions for a queue, run the <a href="/queues/reference/wrangler-commands/#queues-subscription-list"><code>queues subscription list command</code></a>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler queues subscription list &lt;queue-name&gt;&#10;</code></pre>
<h2 id="delete-subscription">Delete subscription</h2>
<p>When you delete a subscription, your queue will stop receiving messages for those events immediately.</p>
<h3 id="dashboard-2">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11250.md")
</div>
<h3 id="wrangler-cli-2">Wrangler CLI</h3>
<p>To delete a subscription, run the <a href="/queues/reference/wrangler-commands/#queues-subscription-delete"><code>queues subscription delete command</code></a>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler queues subscription delete &lt;queue-name&gt; --id &lt;subscription-id&gt;&#10;</code></pre>
<h2 id="learn-more">Learn more</h2>
<div class="nb-card nb-link-card"><h3 id="card-events-schemas-queues-event-subscriptions-events-schemas"><a href="/queues/event-subscriptions/events-schemas/">Events &amp; schemas</a></h3><p>Explore available event sources and types that you can subscribe to.</p></div>
