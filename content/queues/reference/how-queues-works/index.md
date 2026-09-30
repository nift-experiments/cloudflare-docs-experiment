---
cp9:
  canonical: https://developers.cloudflare.com/queues/reference/how-queues-works/
  description: Learn about Queues architecture including producers, consumers, and message lifecycle.
  full_title: How Queues Works · Cloudflare Queues docs
  head_html: <title>How Queues Works · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about Queues architecture including producers, consumers, and message lifecycle."><link rel="canonical" href="https://developers.cloudflare.com/queues/reference/how-queues-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/reference/how-queues-works/index.md"><meta property="og:title" content="How Queues Works · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about Queues architecture including producers, consumers, and message lifecycle."><meta property="og:url" content="https://developers.cloudflare.com/queues/reference/how-queues-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/reference/how-queues-works/#page","headline":"How Queues Works \u00b7 Cloudflare Queues docs","description":"Learn about Queues architecture including producers, consumers, and message lifecycle.","url":"https://developers.cloudflare.com/queues/reference/how-queues-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/reference/how-queues-works/
  schema: 1
---
<p>Cloudflare Queues is a flexible messaging queue that allows you to queue messages for asynchronous processing. Message queues are great at decoupling components of applications, like the checkout and order fulfillment services for an e-commerce site. Decoupled services are easier to reason about, deploy, and implement, allowing you to ship features that delight your customers without worrying about synchronizing complex deployments. Queues also allow you to batch and buffer calls to downstream services and APIs.</p>
<p>There are four major concepts to understand with Queues:</p>
<ol>
<li><a href="#what-is-a-queue">Queues</a></li>
<li><a href="#producers">Producers</a></li>
<li><a href="#consumers">Consumers</a></li>
<li><a href="#messages">Messages</a></li>
</ol>
<h2 id="what-is-a-queue">What is a queue</h2>
<p>A queue is a buffer or list that automatically scales as messages are written to it, and allows a consumer Worker to pull messages from that same queue.</p>
<p>Queues are designed to be reliable, and messages written to a queue should never be lost once the write succeeds. Similarly, messages are not deleted from a queue until the <a href="#consumers">consumer</a> has successfully consumed the message.</p>
<p>Queues does not guarantee that messages will be delivered to a consumer in the same order in which they are published.</p>
<p>Developers can create multiple queues. Creating multiple queues can be useful to:</p>
<ul>
<li>Separate different use-cases and processing requirements: for example, a logging queue vs. a password reset queue.</li>
<li>Horizontally scale your overall throughput (messages per second) by using multiple queues to scale out.</li>
<li>Configure different batching strategies for each consumer connected to a queue.</li>
</ul>
<p>For most applications, a single producer Worker per queue, with a single consumer Worker consuming messages from that queue allows you to logically separate the processing for each of your queues.</p>
<h2 id="producers">Producers</h2>
<p>A producer is the term for a client that is publishing or producing messages on to a queue. A producer is configured by <a href="/workers/runtime-apis/bindings/">binding</a> a queue to a Worker and writing messages to the queue by calling that binding.</p>
<p>For example, if we bound a queue named <code>my-first-queue</code> to a binding of <code>MY_FIRST_QUEUE</code>, messages can be written to the queue by calling <code>send()</code> on the binding:</p>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;  readonly MY_FIRST_QUEUE: Queue;&#10;}&#10;&#10;export default {&#10;  async fetch(req, env, ctx): Promise&lt;Response&gt; {&#10;    const message = {&#10;      url: req.url,&#10;      method: req.method,&#10;      headers: Object.fromEntries(req.headers),&#10;    };&#10;&#10;    await env.MY_FIRST_QUEUE.send(message); // This will throw an exception if the send fails for any reason&#10;    return new Response(&quot;Sent!&quot;);&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11238.md")
</aside>
<p>A queue can have multiple producer Workers. For example, you may have multiple producer Workers writing events or logs to a shared queue based on incoming HTTP requests from users. There is no limit to the total number of producer Workers that can write to a single queue.</p>
<p>Additionally, multiple queues can be bound to a single Worker. That single Worker can decide which queue to write to (or write to multiple) based on any logic you define in your code.</p>
<h3 id="content-types">Content types</h3>
<p>Messages published to a queue can be published in different formats, depending on what interoperability is needed with your consumer. The default content type is <code>json</code>, which means that any object that can be passed to <code>JSON.stringify()</code> will be accepted.</p>
<p>To explicitly set the content type or specify an alternative content type, pass the <code>contentType</code> option to the <code>send()</code> method of your queue:</p>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;  readonly MY_FIRST_QUEUE: Queue;&#10;}&#10;&#10;export default {&#10;  async fetch(req, env, ctx): Promise&lt;Response&gt; {&#10;    const message = {&#10;      url: req.url,&#10;      method: req.method,&#10;      headers: Object.fromEntries(req.headers),&#10;    };&#10;    try {&#10;      await env.MY_FIRST_QUEUE.send(message, { contentType: &quot;json&quot; }); // &quot;json&quot; is the default&#10;      return new Response(&quot;Sent!&quot;);&#10;    } catch (e) {&#10;      // Catch cases where send fails, including due to a mismatched content type&#10;      const msg = e instanceof Error ? e.message : &quot;Unknown error&quot;;&#10;      return Response.json({ error: msg }, { status: 500 });&#10;    }&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>To only accept simple strings when writing to a queue, set <code>{ contentType: &quot;text&quot; }</code> instead:</p>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;  readonly MY_FIRST_QUEUE: Queue;&#10;}&#10;&#10;export default {&#10;  async fetch(req, env, ctx): Promise&lt;Response&gt; {&#10;    try {&#10;      // This will throw an exception (error) if you pass a non-string to the queue,&#10;      // such as a native JavaScript object or ArrayBuffer.&#10;      await env.MY_FIRST_QUEUE.send(&quot;hello there&quot;, { contentType: &quot;text&quot; }); // explicitly set &#x27;text&#x27;&#10;      return new Response(&quot;Sent!&quot;);&#10;    } catch (e) {&#10;      const msg = e instanceof Error ? e.message : &quot;Unknown error&quot;;&#10;      return Response.json({ error: msg }, { status: 500 });&#10;    }&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>The <a href="/queues/configuration/javascript-apis/#queuescontenttype"><code>QueuesContentType</code></a> API documentation describes how each format is serialized to a queue.</p>
<h2 id="consumers">Consumers</h2>
<p>Queues supports two types of consumer:</p>
<ol>
<li>A <a href="/queues/configuration/configure-queues/">consumer Worker</a>, which is push-based: the Worker is invoked when the queue has messages to deliver.</li>
<li>A <a href="/queues/configuration/pull-consumers/">HTTP pull consumer</a>, which is pull-based: the consumer calls the queue endpoint over HTTP to receive and then acknowledge messages.</li>
</ol>
<p>A queue can only have one type of consumer configured.</p>
<h3 id="create-a-consumer-worker">Create a consumer Worker</h3>
<p>A consumer is the term for a client that is subscribing to or <em>consuming</em> messages from a queue. In its most basic form, a consumer is defined by creating a <code>queue</code> handler in a Worker:</p>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;  // Add your bindings here, e.g. KV namespaces, R2 buckets, D1 databases&#10;}&#10;&#10;export default {&#10;  async queue(batch, env, ctx): Promise&lt;void&gt; {&#10;    // Do something with messages in the batch&#10;    // i.e. write to R2 storage, D1 database, or POST to an external API&#10;    for (const msg of batch.messages) {&#10;      // Process each message&#10;      console.log(msg.body);&#10;    }&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>You then connect that consumer to a queue with <code>wrangler queues consumer &lt;queue-name&gt; &lt;worker-script-name&gt;</code> or by defining a <code>[[queues.consumers]]</code> configuration in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> manually:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11239.md")
</div>
<p>Importantly, each queue can only have one active consumer. This allows Cloudflare Queues to achieve at least once delivery and minimize the risk of duplicate messages beyond that.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="best-practice">Best practice</h3>
@markup("md", "content/.markup/bodies/11237.md")
</aside>
<p>Notably, you can use the same consumer with multiple queues. The queue handler that defines your consumer Worker will be invoked by the queues it is connected to.</p>
<ul>
<li>The <code>MessageBatch</code> that is passed to your <code>queue</code> handler includes a <code>queue</code> property with the name of the queue the batch was read from.</li>
<li>This can reduce the amount of code you need to write, and allow you to process messages based on the name of your queues.</li>
</ul>
<p>For example, a consumer configured to consume messages from multiple queues would resemble the following:</p>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;  // Add your bindings here&#10;}&#10;&#10;export default {&#10;  async queue(batch, env, ctx): Promise&lt;void&gt; {&#10;    // MessageBatch has a `queue` property we can switch on&#10;    switch (batch.queue) {&#10;      case &quot;log-queue&quot;:&#10;        // Write the batch to R2&#10;        break;&#10;      case &quot;debug-queue&quot;:&#10;        // Write the message to the console or to another queue&#10;        break;&#10;      case &quot;email-reset&quot;:&#10;        // Trigger a password reset email via an external API&#10;        break;&#10;      default:&#10;        // Handle messages we haven&#x27;t mentioned explicitly (write a log, push to a DLQ)&#10;        break;&#10;    }&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h3 id="remove-a-consumer">Remove a consumer</h3>
<p>To remove a queue from your project, run <code>wrangler queues consumer remove &lt;queue-name&gt; &lt;script-name&gt;</code> and then remove the desired queue below the <code>[[queues.consumers]]</code> in Wrangler file.</p>
<h3 id="pull-consumers">Pull consumers</h3>
<p>A queue can have a HTTP-based consumer that pulls from the queue, instead of messages being pushed to a Worker.</p>
<p>This consumer can be any HTTP-speaking service that can communicate over the Internet. Review the <a href="/queues/configuration/pull-consumers/">pull consumer guide</a> to learn how to configure a pull-based consumer for a queue.</p>
<h2 id="messages">Messages</h2>
<p>A message is the object you are producing to and consuming from a queue.</p>
<p>Any JSON serializable object can be published to a queue. For most developers, this means either simple strings or JSON objects. You can explicitly <a href="#content-types">set the content type</a> when sending a message.</p>
<p>Messages themselves can be <a href="/queues/configuration/batching-retries/">batched when delivered to a consumer</a>. By default, messages within a batch are treated as all or nothing when determining retries. If the last message in a batch fails to be processed, the entire batch will be retried. You can also choose to <a href="/queues/configuration/batching-retries/">explicitly acknowledge</a> messages as they are successfully processed, and/or mark individual messages to be retried.</p>
