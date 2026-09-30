---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/reference/faq/
  description: Frequently asked questions about Durable Objects pricing, limits, and metrics.
  full_title: FAQs · Cloudflare Durable Objects docs
  head_html: <title>FAQs · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Frequently asked questions about Durable Objects pricing, limits, and metrics."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/reference/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/reference/faq/index.md"><meta property="og:title" content="FAQs · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Frequently asked questions about Durable Objects pricing, limits, and metrics."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/reference/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/reference/faq/#page","headline":"FAQs \u00b7 Cloudflare Durable Objects docs","description":"Frequently asked questions about Durable Objects pricing, limits, and metrics.","url":"https://developers.cloudflare.com/durable-objects/reference/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/reference/faq/
  schema: 1
---
<h2 id="pricing">Pricing</h2>
<h3 id="when-does-a-durable-object-incur-duration-charges">When does a Durable Object incur duration charges?</h3>
<p>A Durable Object incurs duration charges when it is actively executing JavaScript — either handling a request or running event handlers — or when it is idle but does not meet the <a href="/durable-objects/concepts/durable-object-lifecycle/">conditions for hibernation</a>. An idle Durable Object that qualifies for hibernation does not incur duration charges, even during the brief window before the runtime hibernates it.</p>
<p>Once an object has been evicted from memory, the next time it is needed, it will be recreated (calling the constructor again).</p>
<p>There are several factors that can prevent a Durable Object from hibernating and cause it to continue incurring duration charges.</p>
<p>Find more information in <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>
<h3 id="does-an-empty-table-sqlite-database-contribute-to-my-storage">Does an empty table / SQLite database contribute to my storage?</h3>
<p>Yes, although minimal. Empty tables can consume at least a few kilobytes, based on the number of columns (table width) in the table. An empty SQLite database consumes approximately 12 KB of storage.</p>
<h3 id="does-metadata-stored-in-durable-objects-count-towards-my-storage">Does metadata stored in Durable Objects count towards my storage?</h3>
<p>All writes to a SQLite-backed Durable Object stores nominal amounts of metadata in internal tables in the Durable Object, which counts towards your billable storage.</p>
<p>The metadata remains in the Durable Object until you call <a href="/durable-objects/api/sqlite-storage-api/#deleteall"><code>deleteAll()</code></a>.</p>
<h2 id="limits">Limits</h2>
<h3 id="how-much-work-can-a-single-durable-object-do">How much work can a single Durable Object do?</h3>
<p>Durable Objects can scale horizontally across many Durable Objects. Each individual Object is inherently single-threaded.</p>
<ul>
<li>An individual Object has a soft limit of 1,000 requests per second. You can have an unlimited number of individual objects per namespace.</li>
<li>A simple <a href="/durable-objects/api/sqlite-storage-api/">storage</a> <code>get()</code> on a small value that directly returns the response may realize a higher request throughput compared to a Durable Object that (for example) serializes and/or deserializes large JSON values.</li>
<li>Similarly, a Durable Object that performs multiple <code>list()</code> operations may be more limited in terms of request throughput.</li>
</ul>
<p>A Durable Object that receives too many requests will, after attempting to queue them, return an <a href="/durable-objects/observability/troubleshooting/#durable-object-is-overloaded">overloaded</a> error to the caller.</p>
<h3 id="how-many-durable-objects-can-i-create">How many Durable Objects can I create?</h3>
<p>Durable Objects are designed such that the number of individual objects in the system do not need to be limited, and can scale horizontally.</p>
<ul>
<li>You can create and run as many separate Durable Objects as you want within a given Durable Object <span class="nb-glossary-tooltip" title="namespace">namespace</span>.</li>
<li>There are no limits for storage per account when using SQLite-backed Durable Objects on a Workers Paid plan.</li>
<li>Each SQLite-backed Durable Object has a storage limit of 10 GB on a Workers Paid plan.</li>
<li>Refer to <a href="/durable-objects/platform/limits/">Durable Object limits</a> for more information.</li>
</ul>
<h3 id="can-i-increase-durable-objects-cpu-limit">Can I increase Durable Objects' CPU limit?</h3>
<p>Durable Objects are Worker scripts, and have the same <a href="/workers/platform/limits/#account-plan-limits">per invocation CPU limits</a> as any Workers do. Note that CPU time is active processing time: not time spent waiting on network requests, storage calls, or other general I/O, which don't count towards your CPU time or Durable Objects compute consumption.</p>
<p>By default, the maximum CPU time per Durable Objects invocation (HTTP request, WebSocket message, or Alarm) is set to 30 seconds, but can be increased for all Durable Objects associated with a Durable Object definition by setting <code>limits.cpu_ms</code> in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8097.md")
</div>
<h3 id="what-happens-when-a-durable-object-exceeds-its-storage-limit">What happens when a Durable Object exceeds its storage limit?</h3>
<p>When a SQLite-backed Durable Object reaches its <a href="/durable-objects/platform/limits/">maximum storage limit</a> (10 GB on Workers Paid, or 1 GB on the Free plan), write operations (such as <code>INSERT</code>, <code>UPDATE</code>, or calls to the <code>put()</code> and <code>sql.exec()</code> storage APIs) will fail with the following error:</p>
<pre tabindex="0"><code class="language-txt">database or disk is full: SQLITE_FULL&#10;</code></pre>
<p>Read operations (such as <code>SELECT</code> queries, <code>get()</code>, and <code>list()</code> calls) will continue to work, and <code>DELETE</code> operations will also succeed so that you can remove data to free up space.</p>
<p>To handle this error in your Durable Object, catch the exception thrown by the storage API:</p>
<pre tabindex="0"><code class="language-ts">try {&#10;	this.ctx.storage.sql.exec(&#10;		&quot;INSERT INTO my_table (key, value) VALUES (?, ?)&quot;,&#10;		key,&#10;		value,&#10;	);&#10;} catch (e) {&#10;	if (e.message.includes(&quot;SQLITE_FULL&quot;)) {&#10;		// Storage limit reached — reads and deletes still work&#10;		// Consider deleting old data or returning a meaningful error to the caller&#10;	}&#10;	throw e;&#10;}&#10;</code></pre>
<h2 id="metrics-and-analytics">Metrics and analytics</h2>
<h3 id="how-can-i-identify-which-durable-object-instance-generated-a-log-entry">How can I identify which Durable Object instance generated a log entry?</h3>
<p>Durable Object request logs include the instance ID in <code>$workers.durableObjectId</code>. Filter on this field to isolate a specific instance for debugging.</p>
