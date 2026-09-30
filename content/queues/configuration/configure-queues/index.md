---
cp9:
  canonical: https://developers.cloudflare.com/queues/configuration/configure-queues/
  description: Set up Cloudflare Queues bindings, producers, and consumers using Wrangler.
  full_title: Cloudflare Queues - Configuration · Cloudflare Queues docs
  head_html: <title>Cloudflare Queues - Configuration · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Cloudflare Queues bindings, producers, and consumers using Wrangler."><link rel="canonical" href="https://developers.cloudflare.com/queues/configuration/configure-queues/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/configuration/configure-queues/index.md"><meta property="og:title" content="Cloudflare Queues - Configuration · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Cloudflare Queues bindings, producers, and consumers using Wrangler."><meta property="og:url" content="https://developers.cloudflare.com/queues/configuration/configure-queues/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/configuration/configure-queues/#page","headline":"Cloudflare Queues - Configuration \u00b7 Cloudflare Queues docs","description":"Set up Cloudflare Queues bindings, producers, and consumers using Wrangler.","url":"https://developers.cloudflare.com/queues/configuration/configure-queues/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/configuration/configure-queues/
  schema: 1
---
<p>Cloudflare Queues can be configured using <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the command-line interface for Cloudflare's Developer Platform, which includes <a href="/workers/">Workers</a>, <a href="/r2/">R2</a>, and other developer products.</p>
<p>Each Producer and Consumer Worker has a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> that specifies environment variables, triggers, and resources, such as a queue. To enable Worker-to-resource communication, you must set up a <a href="/workers/runtime-apis/bindings/">binding</a> in your Worker project's Wrangler file.</p>
<p>Use the options below to configure your queue.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11282.md")
</aside>
<h2 id="queue-configuration">Queue configuration</h2>
The following queue level settings can be configured using Wrangler:
<pre tabindex="0"><code class="language-sh">npx wrangler queues update &lt;QUEUE-NAME&gt; --delivery-delay-secs 60 --message-retention-period-secs 3000&#10;</code></pre>
<ul>
<li>
<p><code>--delivery-delay-secs</code> <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>How long a published message is delayed for, before it is delivered to consumers.</li>
<li>Must be between 0 and 86400 (24 hours).</li>
<li>Defaults to 0.</li>
</ul>
</li>
<li>
<p><code>--message-retention-period-secs</code>  <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>How long messages are retained on the Queue.</li>
<li>Defaults to 345600 (4 days).</li>
<li>Must be between 60 and 1209600 (14 days)</li>
</ul>
</li>
</ul>
<h2 id="producer-worker-configuration">Producer Worker configuration</h2>
<p>A producer is a <a href="/workers/">Cloudflare Worker</a> that writes to one or more queues. A producer can accept messages over HTTP, asynchronously write messages when handling requests, and/or write to a queue from within a <a href="/durable-objects/">Durable Object</a>. Any Worker can write to a queue.</p>
<p>To produce to a queue, set up a binding in your Wrangler file. These options should be used when a Worker wants to send messages to a queue.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11283.md")
</div>
<ul>
<li>
<p><code>queue</code> <span class="nb-type">string</span></p>
<ul>
<li>The name of the queue.</li>
</ul>
</li>
<li>
<p><code>binding</code> <span class="nb-type">string</span></p>
<ul>
<li>The name of the binding, which is a JavaScript variable.</li>
</ul>
</li>
</ul>
<h2 id="consumer-worker-configuration">Consumer Worker Configuration</h2>
<p>To consume messages from one or more queues, set up a binding in your Wrangler file. These options should be used when a Worker wants to receive messages from a queue.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11284.md")
</div>
<p>Refer to <a href="/queues/platform/limits">Limits</a> to review the maximum values for each of these options.</p>
<ul>
<li>
<p><code>queue</code> <span class="nb-type">string</span></p>
<ul>
<li>The name of the queue.</li>
</ul>
</li>
<li>
<p><code>max_batch_size</code> <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>The maximum number of messages allowed in each batch.</li>
<li>Defaults to <code>10</code> messages.</li>
</ul>
</li>
<li>
<p><code>max_batch_timeout</code> <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>The maximum number of seconds to wait until a batch is full.</li>
<li>Defaults to <code>5</code> seconds.</li>
</ul>
</li>
<li>
<p><code>max_retries</code> <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>The maximum number of retries for a message, if it fails or <a href="/queues/configuration/javascript-apis/#messagebatch"><code>retryAll()</code></a> is invoked.</li>
<li>Defaults to <code>3</code> retries.</li>
</ul>
</li>
<li>
<p><code>dead_letter_queue</code> <span class="nb-type">string</span> <span class="nb-type">optional</span></p>
<ul>
<li>The name of another queue to send a message if it fails processing at least <code>max_retries</code> times.</li>
<li>If a <code>dead_letter_queue</code> is not defined, messages that repeatedly fail processing will eventually be discarded.</li>
<li>If there is no queue with the specified name, it will be created automatically.</li>
</ul>
</li>
<li>
<p><code>max_concurrency</code> <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>The maximum number of concurrent consumers allowed to run at once. Leaving this unset will mean that the number of invocations will scale to the <a href="/queues/platform/limits/">currently supported maximum</a>.</li>
<li>Refer to <a href="/queues/configuration/consumer-concurrency/">Consumer concurrency</a> for more information on how consumers autoscale, particularly when messages are retried.</li>
</ul>
</li>
</ul>
<h2 id="pull-based">Pull-based</h2>
<p>A queue can have a HTTP-based consumer that pulls from the queue. This consumer can be any HTTP-speaking service that can communicate over the Internet. Review <a href="/queues/configuration/pull-consumers/">Pull consumers</a> to learn how to configure a pull-based consumer.</p>
