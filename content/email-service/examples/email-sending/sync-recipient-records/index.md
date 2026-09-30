---
cp9:
  canonical: https://developers.cloudflare.com/email-service/examples/email-sending/sync-recipient-records/
  description: Remove recipients after hard bounces and spam complaints.
  full_title: Sync recipient records · Cloudflare Email Service docs
  head_html: <title>Sync recipient records · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Remove recipients after hard bounces and spam complaints."><link rel="canonical" href="https://developers.cloudflare.com/email-service/examples/email-sending/sync-recipient-records/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/examples/email-sending/sync-recipient-records/index.md"><meta property="og:title" content="Sync recipient records · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Remove recipients after hard bounces and spam complaints."><meta property="og:url" content="https://developers.cloudflare.com/email-service/examples/email-sending/sync-recipient-records/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/examples/email-sending/sync-recipient-records/#page","headline":"Sync recipient records \u00b7 Cloudflare Email Service docs","description":"Remove recipients after hard bounces and spam complaints.","url":"https://developers.cloudflare.com/email-service/examples/email-sending/sync-recipient-records/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/examples/email-sending/sync-recipient-records/
  schema: 1
---
<p class="article-summary">Synchronize application recipient records with Email Sending lifecycle events.</p>
<p>Use <a href="/email-service/platform/event-subscriptions/">Email Sending event subscriptions</a> to update application records after delivery problems. This example uses <a href="/queues/">Cloudflare Queues</a> and <a href="/kv/">Workers KV</a> to remove recipients from transactional notifications.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="suppression-lists">Suppression lists</h3>
@markup("md", "content/.markup/bodies/8662.md")
</aside>
<h2 id="prepare-the-resources">Prepare the resources</h2>
<p>Before you begin:</p>
<ul>
<li>Enable an <a href="/email-service/configuration/domains/">Email Sending domain</a>.</li>
<li>Create a <a href="/workers/get-started/guide/">Worker project</a>.</li>
<li>Create a <a href="/kv/get-started/#2-create-a-kv-namespace">Workers KV namespace</a>.</li>
</ul>
<p>Store each eligible recipient address as a key in KV. The value can contain notification preferences or related metadata.</p>
<h2 id="review-the-event-flow">Review the event flow</h2>
<ol>
<li>Email Sending publishes bounce and complaint events.</li>
<li>A queue delivers those events to a Worker.</li>
<li>The Worker removes ineligible recipient records from KV.</li>
</ol>
<h2 id="choose-removal-events">Choose removal events</h2>
<p>Remove records for every <code>message.complained</code> event. These events indicate that a recipient reported the message as spam.</p>
<p>Remove bounced records only when <code>payload.bounce.type</code> is <code>&quot;hard&quot;</code>. Temporary failures produce <code>message.deferred</code> events while retries remain. Exhausted temporary retries can produce <code>message.bounced</code> events with a <code>&quot;soft&quot;</code> bounce type.</p>
<p>For payload details, refer to <a href="/email-service/platform/event-subscriptions/#available-email-sending-events">Available Email Sending events</a>.</p>
<h2 id="create-the-queue-and-subscription">Create the queue and subscription</h2>
<p>Create a queue and subscribe it to your sending domain:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8663.md")
</div>
<h2 id="configure-the-worker">Configure the Worker</h2>
<p>Bind the KV namespace and register the Worker as the queue consumer:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8664.md")
</div>
<p>The configuration creates <code>email-events-dlq</code> during deployment. Queues moves events there after three retries.</p>
<h2 id="add-the-queue-consumer">Add the queue consumer</h2>
<p>The <a href="/queues/configuration/javascript-apis/#consumer"><code>queue()</code> handler</a> processes each event independently. It deletes applicable recipient records and retries failed KV operations.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8665.md")
</div>
<p>Deleting a missing KV key succeeds. This makes repeated event delivery safe.</p>
<p>The handler acknowledges each successful message. Failed operations move to the <a href="/queues/configuration/dead-letter-queues/">dead letter queue</a> after three retries.</p>
<h2 id="deploy-the-worker">Deploy the Worker</h2>
<p>Deploy the Worker and its queue consumer configuration:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Monitor the dead letter queue for failed events. Reprocess them after fixing the underlying error.</p>
<h2 id="explore-related-resources">Explore related resources</h2>
<ul>
<li><a href="/email-service/platform/event-subscriptions/">Event subscriptions</a> — review event schemas.</li>
<li><a href="/email-service/concepts/suppressions/">Suppression lists</a> — understand automatic suppressions.</li>
<li><a href="/queues/configuration/batching-retries/">Queues retries</a> — control message retries.</li>
<li><a href="/kv/concepts/how-kv-works/#consistency">Workers KV consistency</a> — account for propagation delays.</li>
</ul>
