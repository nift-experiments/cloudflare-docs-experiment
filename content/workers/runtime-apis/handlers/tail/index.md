---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/
  description: Process real-time logs from producer Workers using the tail() handler in Tail Workers.
  full_title: Tail Handler · Cloudflare Workers docs
  head_html: <title>Tail Handler · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Process real-time logs from producer Workers using the tail() handler in Tail Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/index.md"><meta property="og:title" content="Tail Handler · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Process real-time logs from producer Workers using the tail() handler in Tail Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/#page","headline":"Tail Handler \u00b7 Cloudflare Workers docs","description":"Process real-time logs from producer Workers using the tail() handler in Tail Workers.","url":"https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/handlers/tail/
  schema: 1
---
<h2 id="background">Background</h2>
<p>The <code>tail()</code> handler is the handler you implement when writing a <a href="/workers/observability/logs/tail-workers/">Tail Worker</a>. Tail Workers can be used to process logs in real-time and send them to a logging or analytics service.</p>
<p>The <code>tail()</code> handler is called once each time the connected producer Worker is invoked.</p>
<p>To configure a Tail Worker, refer to <a href="/workers/observability/logs/tail-workers/">Tail Workers documentation</a>.</p>
<h2 id="syntax">Syntax</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17166.md")
</div></div>
<h3 id="parameters">Parameters</h3>
<ul>
<li>
<p><code>events</code> array</p>
<ul>
<li>An array of <a href="/workers/runtime-apis/handlers/tail/#tailitems"><code>TailItems</code></a>. One <code>TailItem</code> is collected for each event that triggers a Worker. For Workers for Platforms customers with a Tail Worker installed on the dynamic dispatch Worker, <code>events</code> will contain two elements: one for the dynamic dispatch Worker and one for the User Worker.</li>
</ul>
</li>
<li>
<p><code>env</code> object</p>
<ul>
<li>An object containing the bindings associated with your Worker using <a href="/workers/reference/migrate-to-module-workers/">ES modules format</a>, such as KV namespaces and Durable Objects.</li>
</ul>
</li>
<li>
<p><code>ctx</code> object</p>
<ul>
<li>An object containing the context associated with your Worker using <a href="/workers/reference/migrate-to-module-workers/">ES modules format</a>. Currently, this object just contains the <code>waitUntil</code> function.</li>
</ul>
</li>
</ul>
<h3 id="properties">Properties</h3>
<ul>
<li>
<p><code>event.type</code> string</p>
<ul>
<li>The type of event. This will always return <code>&quot;tail&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>event.traces</code> array</p>
<ul>
<li>An array of <a href="/workers/runtime-apis/handlers/tail/#tailitems"><code>TailItems</code></a>. One <code>TailItem</code> is collected for each event that triggers a Worker. For Workers for Platforms customers with a Tail Worker installed on the dynamic dispatch Worker, <code>events</code> will contain two elements: one for the dynamic dispatch Worker and one for the user Worker.</li>
</ul>
</li>
<li>
<p><code>event.waitUntil(promisePromise)</code> : void</p>
<ul>
<li>Refer to <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code></a>. Note that unlike fetch event handlers, tail handlers do not return a value, so this is the only way for trace Workers to do asynchronous work.</li>
</ul>
</li>
</ul>
<h3 id="tailitems"><code>TailItems</code></h3>
<h4 id="properties-1">Properties</h4>
<ul>
<li>
<p><code>scriptName</code> string</p>
<ul>
<li>The name of the producer script.</li>
</ul>
</li>
<li>
<p><code>event</code> object</p>
<ul>
<li>Contains information about the Worker’s triggering event.
<ul>
<li>For fetch events: a <a href="/workers/runtime-apis/handlers/tail/#fetcheventinfo"><code>FetchEventInfo</code> object</a></li>
<li>For other event types: <code>null</code>, currently.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>eventTimestamp</code> number</p>
<ul>
<li>Measured in epoch time.</li>
</ul>
</li>
<li>
<p><code>logs</code> array</p>
<ul>
<li>An array of <a href="/workers/runtime-apis/handlers/tail/#taillog">TailLogs</a>.</li>
</ul>
</li>
<li>
<p><code>exceptions</code> array</p>
<ul>
<li>An array of <a href="/workers/runtime-apis/handlers/tail/#tailexception"><code>TailExceptions</code></a>. A single Worker invocation might result in multiple unhandled exceptions, since a Worker can register multiple asynchronous tasks.</li>
</ul>
</li>
<li>
<p><code>outcome</code> string</p>
<ul>
<li>The outcome of the Worker invocation, one of:
<ul>
<li><code>unknown</code>: outcome status was not set.</li>
<li><code>ok</code>: The worker invocation succeeded.</li>
<li><code>exception</code>: An unhandled exception was thrown.  This can happen for many reasons, including:
<ul>
<li>An uncaught JavaScript exception.</li>
<li>A fetch handler that does not result in a Response.</li>
<li>An internal error.</li>
</ul>
</li>
<li><code>exceededCpu</code>: The Worker invocation exceeded either its CPU limits.</li>
<li><code>exceededMemory</code>: The Worker invocation exceeded memory limits.</li>
<li><code>scriptNotFound</code>: An internal error from difficulty retrieving the Worker script.</li>
<li><code>canceled</code>: The worker invocation was canceled before it completed. Commonly because the client disconnected before a response could be sent.</li>
<li><code>responseStreamDisconnected</code>: The response stream was disconnected during deferred proxying. Happens when either the client or server hangs up early.</li>
</ul>
</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="outcome-is-not-the-same-as-http-status">Outcome is not the same as HTTP status.</h3>
@markup("md", "content/.markup/bodies/17163.md")
</aside>
<h3 id="fetcheventinfo"><code>FetchEventInfo</code></h3>
<h4 id="properties-2">Properties</h4>
<ul>
<li>
<p><code>request</code> object</p>
<ul>
<li>A <a href="/workers/runtime-apis/handlers/tail/#tailrequest"><code>TailRequest</code> object</a>.</li>
</ul>
</li>
<li>
<p><code>response</code> object</p>
<ul>
<li>A <a href="/workers/runtime-apis/handlers/tail/#tailresponse"><code>TailResponse</code> object</a>.</li>
</ul>
</li>
</ul>
<h3 id="tailrequest"><code>TailRequest</code></h3>
<h4 id="properties-3">Properties</h4>
<ul>
<li>
<p><code>cf</code> object</p>
<ul>
<li>Contains the data from <a href="/workers/runtime-apis/request/#incomingrequestcfproperties"><code>IncomingRequestCfProperties</code></a>.</li>
</ul>
</li>
<li>
<p><code>headers</code> object</p>
<ul>
<li>Header name/value entries (redacted by default). Header names are lowercased, and the values associated with duplicate header names are concatenated, with the string <code>&quot;, &quot;</code> (comma space) interleaved, similar to <a href="https://fetch.spec.whatwg.org/#concept-header-list-get">the Fetch standard</a>.</li>
</ul>
</li>
<li>
<p><code>method</code> string</p>
<ul>
<li>The HTTP request method.</li>
</ul>
</li>
<li>
<p><code>url</code> string</p>
<ul>
<li>The HTTP request URL (redacted by default).</li>
</ul>
</li>
</ul>
<h4 id="methods">Methods</h4>
<ul>
<li>
<p><code>getUnredacted()</code> object</p>
<ul>
<li>Returns a TailRequest object with unredacted properties</li>
</ul>
</li>
</ul>
<p>Some of the properties of <code>TailRequest</code> are redacted by default to make it harder to accidentally record sensitive information, like user credentials or API tokens. The redactions use heuristic rules, so they are subject to false positives and negatives. Clients can call <code>getUnredacted()</code> to bypass redaction, but they should always be careful about what information is retained, whether using the redaction or not.</p>
<ul>
<li>Header redaction: The header value will be the string <code>“REDACTED”</code> when the (case-insensitive) header name is <code>cookie</code>/<code>set-cookie</code> or contains a substring <code>&quot;auth”</code>, <code>“key”</code>, <code>“secret”</code>, <code>“token”</code>, or <code>&quot;jwt&quot;</code>.</li>
<li>URL redaction: For each greedily matched substring of ID characters (a-z, A-Z, 0-9, '+', '-', '_') in the URL, if it meets the following criteria for a hex or base-64 ID, the substring will be replaced with the string <code>“REDACTED”</code>.</li>
<li>Hex ID: Contains 32 or more hex digits, and contains only hex digits and separators ('+', '-', '_')</li>
<li>Base-64 ID: Contains 21 or more characters, and contains at least two uppercase, two lowercase, and two digits.</li>
</ul>
<h3 id="tailresponse"><code>TailResponse</code></h3>
<h4 id="properties-4">Properties</h4>
<ul>
<li>
<p><code>status</code> number</p>
<ul>
<li>The HTTP status code.</li>
</ul>
</li>
</ul>
<h3 id="taillog"><code>TailLog</code></h3>
<p>Records information sent to console functions.</p>
<h4 id="properties-5">Properties</h4>
<ul>
<li>
<p><code>timestamp</code> number</p>
<ul>
<li>Measured in epoch time.</li>
</ul>
</li>
<li>
<p><code>level</code> string</p>
<ul>
<li>A string indicating the console function that was called. One of: <code>debug</code>, <code>info</code>, <code>log</code>, <code>warn</code>, <code>error</code>.</li>
</ul>
</li>
<li>
<p><code>message</code> object</p>
<ul>
<li>The array of parameters passed to the console function.</li>
</ul>
</li>
</ul>
<h3 id="tailexception"><code>TailException</code></h3>
<p>Records an unhandled exception that occurred during the Worker invocation.</p>
<h4 id="properties-6">Properties</h4>
<ul>
<li>
<p><code>timestamp</code> number</p>
<ul>
<li>Measured in epoch time.</li>
</ul>
</li>
<li>
<p><code>name</code> string</p>
<ul>
<li>The error type (For example,<code>Error</code>, <code>TypeError</code>, etc.).</li>
</ul>
</li>
<li>
<p><code>message</code> object</p>
<ul>
<li>The error description (For example, <code>&quot;x&quot; is not a function</code>).</li>
</ul>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/observability/logs/tail-workers/">Tail Workers</a> - Configure a Tail Worker to receive information about the execution of other Workers.</li>
</ul>
