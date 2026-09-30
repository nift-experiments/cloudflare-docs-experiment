---
cp9:
  canonical: https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/
  description: Publish to a Queue directly from your Worker.
  full_title: Queues - Publish Directly via a Worker · Cloudflare Queues docs
  head_html: <title>Queues - Publish Directly via a Worker · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Publish to a Queue directly from your Worker."><link rel="canonical" href="https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/index.md"><meta property="og:title" content="Queues - Publish Directly via a Worker · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Publish to a Queue directly from your Worker."><meta property="og:url" content="https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Queues,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/#page","headline":"Queues - Publish Directly via a Worker \u00b7 Cloudflare Queues docs","description":"Publish to a Queue directly from your Worker.","url":"https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/examples/publish-to-a-queue-via-workers/
  schema: 1
---
<p class="article-summary">Publish to a Queue directly from your Worker.</p>
<p>The following example shows you how to publish messages to a Queue from a Worker. The example uses a Worker that receives a JSON payload from the request body and writes it as-is to the Queue, but in a real application you might have more logic before you queue a message.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="/queues/get-started/#3-create-a-queue">queue created</a> via the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> or the <a href="/workers/wrangler/install-and-update/">wrangler CLI</a>.</li>
<li>A <a href="/queues/configuration/configure-queues/#producer-worker-configuration">configured <strong>producer</strong> binding</a> in the Cloudflare dashboard or Wrangler file.</li>
</ul>
<p>Configure your Wrangler file as follows:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11245.md")
</div>
<h3 id="1-create-the-worker"><ol>
<li>Create the Worker</li>
</ol></h3>
<p>The following Worker script:</p>
<ol>
<li>Validates that the request body is valid JSON.</li>
<li>Publishes the payload to the queue.</li>
</ol>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;	YOUR_QUEUE: Queue;&#10;}&#10;&#10;export default {&#10;	async fetch(req, env, ctx): Promise&lt;Response&gt; {&#10;		// Validate the payload is JSON&#10;		// In a production application, we may more robustly validate the payload&#10;		// against a schema using a library like &#x27;zod&#x27;&#10;		let messages;&#10;		try {&#10;			messages = await req.json();&#10;		} catch {&#10;			// Return a HTTP 400 (Bad Request) if the payload isn&#x27;t JSON&#10;			return Response.json({ error: &quot;payload not valid JSON&quot; }, { status: 400 });&#10;		}&#10;&#10;		// Publish to the Queue&#10;		try {&#10;			await env.YOUR_QUEUE.send(messages);&#10;		} catch (e) {&#10;			const message = e instanceof Error ? e.message : &quot;Unknown error&quot;;&#10;			console.error(`failed to send to the queue: ${message}`);&#10;			// Return a HTTP 500 (Internal Error) if our publish operation fails&#10;			return Response.json({ error: message }, { status: 500 });&#10;		}&#10;&#10;		// Return a HTTP 200 if the send succeeded!&#10;		return Response.json({ success: true });&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>To deploy this Worker:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<h3 id="2-send-a-test-message"><ol start="2">
<li>Send a test message</li>
</ol></h3>
<p>To make sure you successfully write a message to your queue, use <code>curl</code> on the command line:</p>
<pre tabindex="0"><code class="language-sh">&#35; Make sure to replace the placeholder with your shared secret&#10;curl -XPOST &quot;https://YOUR_WORKER.YOUR_ACCOUNT.workers.dev&quot; --data &#x27;{&quot;messages&quot;: [{&quot;msg&quot;:&quot;hello world&quot;}]}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">{&quot;success&quot;:true}&#10;</code></pre>
<p>This will issue a HTTP POST request, and if successful, return a HTTP 200 with a <code>success: true</code> response body.</p>
<ul>
<li>If you receive a HTTP 400, this is because you attempted to send malformed JSON to your queue.</li>
<li>If you receive a HTTP 500, this is because the message was not written to your Queue successfully.</li>
</ul>
<p>You can use <a href="/workers/observability/logs/real-time-logs/"><code>wrangler tail</code></a> to debug the output of <code>console.log</code>.</p>
