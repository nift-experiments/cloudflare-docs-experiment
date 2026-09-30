---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/
  description: Durable Objects provide globally unique, single-threaded compute instances with persistent storage on Cloudflare.
  full_title: What are Durable Objects? · Cloudflare Durable Objects docs
  head_html: <title>What are Durable Objects? · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Durable Objects provide globally unique, single-threaded compute instances with persistent storage on Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/index.md"><meta property="og:title" content="What are Durable Objects? · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Durable Objects provide globally unique, single-threaded compute instances with persistent storage on Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/#page","headline":"What are Durable Objects? \u00b7 Cloudflare Durable Objects docs","description":"Durable Objects provide globally unique, single-threaded compute instances with persistent storage on Cloudflare.","url":"https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/concepts/what-are-durable-objects/
  schema: 1
---
<p>A Durable Object is a special kind of <a href="/workers/">Cloudflare Worker</a> which uniquely combines compute with storage. Like a Worker, a Durable Object is automatically provisioned geographically close to where it is first requested, starts up quickly when needed, and shuts down when idle. You can have millions of them around the world. However, unlike regular Workers:</p>
<ul>
<li>Each Durable Object has a <strong>globally-unique name</strong>, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together.</li>
<li>Each Durable Object has some <strong>durable storage</strong> attached. Since this storage lives together with the object, it is strongly consistent yet fast to access.</li>
</ul>
<p>Therefore, Durable Objects enable <strong>stateful</strong> serverless applications.</p>
<h2 id="durable-objects-highlights">Durable Objects highlights</h2>
<p>Durable Objects have properties that make them a great fit for distributed stateful scalable applications.</p>
<p><strong>Serverless compute, zero infrastructure management</strong></p>
<ul>
<li>Durable Objects are built on-top of the Workers runtime, so they support exactly the same code (JavaScript and WASM), and similar memory and CPU limits.</li>
<li>Each Durable Object is <a href="/durable-objects/api/namespace/#get">implicitly created on first access</a>. User applications are not concerned with their lifecycle, creating them or destroying them. Durable Objects migrate among healthy servers, and therefore applications never have to worry about managing them.</li>
<li>Each Durable Object stays alive as long as requests are being processed, and remains alive for several seconds after being idle before hibernating, allowing applications to <a href="/durable-objects/reference/in-memory-state/">exploit in-memory caching</a> while handling many consecutive requests and boosting their performance.</li>
</ul>
<p><strong>Storage colocated with compute</strong></p>
<ul>
<li>Each Durable Object has its own <a href="/durable-objects/api/sqlite-storage-api/">durable, transactional, and strongly consistent storage</a> (up to 10 GB<sup><a href="#footnote-1">1</a></sup>), persisted across requests, and accessible only within that object.</li>
</ul>
<p><strong>Single-threaded concurrency</strong></p>
<ul>
<li>Each <a href="/durable-objects/api/id/">Durable Object instance has an identifier</a>, either randomly-generated or user-generated, which allows you to globally address which Durable Object should handle a specific action or request.</li>
<li>Durable Objects are single-threaded and cooperatively multi-tasked, just like code running in a web browser. For more details on how safety and correctness are achieved, refer to the blog post <a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">&quot;Durable Objects: Easy, Fast, Correct — Choose three&quot;</a>.</li>
</ul>
<p><strong>Elastic horizontal scaling across Cloudflare's global network</strong></p>
<ul>
<li>Durable Objects can be spread around the world, and you can <a href="/durable-objects/reference/data-location/#provide-a-location-hint">optionally influence where each instance should be located</a>. Durable Objects are not yet available in every Cloudflare data center; refer to the <a href="https://where.durableobjects.live/">where.durableobjects.live</a> project for live locations.</li>
<li>Each Durable Object type (or <a href="/durable-objects/api/namespace/">&quot;Namespace binding&quot;</a> in Cloudflare terms) corresponds to a JavaScript class implementing the actual logic. There is no hard limit on how many Durable Objects can be created for each namespace.</li>
<li>Durable Objects scale elastically as your application creates millions of objects. There is no need for applications to manage infrastructure or plan ahead for capacity.</li>
</ul>
<h2 id="durable-objects-features">Durable Objects features</h2>
<h3 id="in-memory-state">In-memory state</h3>
<p>Each Durable Object has its own <a href="/durable-objects/reference/in-memory-state/">in-memory state</a>. Applications can use this in-memory state to optimize the performance of their applications by keeping important information in-memory, thereby avoiding the need to access the durable storage at all.</p>
<p>Useful cases for in-memory state include batching and aggregating information before persisting it to storage, or for immediately rejecting/handling incoming requests meeting certain criteria, and more.</p>
<p>In-memory state is reset when the Durable Object hibernates after being idle for some time. Therefore, it is important to persist any in-memory data to the durable storage if that data will be needed at a later time when the Durable Object receives another request.</p>
<h3 id="storage-api">Storage API</h3>
<p>The <a href="/durable-objects/api/sqlite-storage-api/">Durable Object Storage API</a> allows Durable Objects to access fast, transactional, and strongly consistent storage. A Durable Object's attached storage is private to its unique instance and cannot be accessed by other objects.</p>
<p>There are two flavors of the storage API, a <a href="/durable-objects/api/legacy-kv-storage-api/">key-value (KV) API</a> and an <a href="/durable-objects/api/sqlite-storage-api/">SQL API</a>.</p>
<p>When using the <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">new SQLite in Durable Objects storage backend</a>, you have access to both the APIs. However, if you use the previous storage backend you only have access to the key-value API.</p>
<h3 id="alarms-api">Alarms API</h3>
<p>Durable Objects provide an <a href="/durable-objects/api/alarms/">Alarms API</a> which allows you to schedule the Durable Object to be woken up at a time in the future. This is useful when you want to do certain work periodically, or at some specific point in time, without having to manually manage infrastructure such as job scheduling runners on your own.</p>
<p>You can combine Alarms with in-memory state and the durable storage API to build batch and aggregation applications such as queues, workflows, or advanced data pipelines.</p>
<h3 id="websockets">WebSockets</h3>
<p>WebSockets are long-lived TCP connections that enable bi-directional, real-time communication between client and server. Because WebSocket sessions are long-lived, applications commonly use Durable Objects to accept either the client or server connection.</p>
<p>Because Durable Objects provide a single-point-of-coordination between Cloudflare Workers, a single Durable Object instance can be used in parallel with WebSockets to coordinate between multiple clients, such as participants in a chat room or a multiplayer game.</p>
<p>Durable Objects support the <a href="/durable-objects/best-practices/websockets/#websocket-standard-api">WebSocket Standard API</a>, as well as the <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSockets Hibernation API</a> which extends the Web Standard WebSocket API to reduce costs by not incurring billing charges during periods of inactivity.</p>
<h3 id="rpc">RPC</h3>
<p>Durable Objects support Workers <a href="/workers/runtime-apis/rpc/">Remote-Procedure-Call (RPC)</a> which allows applications to use JavaScript-native methods and objects to communicate between Workers and Durable Objects.</p>
<p>Using RPC for communication makes application development easier and simpler to reason about, and more efficient.</p>
<h2 id="actor-programming-model">Actor programming model</h2>
<p>Another way to describe and think about Durable Objects is through the lens of the <a href="https://en.wikipedia.org/wiki/Actor_model">Actor programming model</a>. There are several popular examples of the Actor model supported at the programming language level through runtimes or library frameworks, like <a href="https://www.erlang.org/">Erlang</a>, <a href="https://elixir-lang.org/">Elixir</a>, <a href="https://akka.io/">Akka</a>, or <a href="https://learn.microsoft.com/en-us/dotnet/orleans/overview">Microsoft Orleans for .NET</a>.</p>
<p>The Actor model simplifies a lot of problems in distributed systems by abstracting away the communication between actors using RPC calls (or message sending) that could be implemented on-top of any transport protocol, and it avoids most of the concurrency pitfalls you get when doing concurrency through shared memory such as race conditions when multiple processes/threads access the same data in-memory.</p>
<p>Each Durable Object instance can be seen as an Actor instance, receiving messages (incoming HTTP/RPC requests), executing some logic in its own single-threaded context using its attached durable storage or in-memory state, and finally sending messages to the outside world (outgoing HTTP/RPC requests or responses), even to another Durable Object instance.</p>
<p>Each Durable Object has certain capabilities in terms of <a href="/durable-objects/platform/limits/#how-much-work-can-a-single-durable-object-do">how much work it can do</a>, which should influence the application's <a href="/reference-architecture/diagrams/storage/durable-object-control-data-plane-pattern/">architecture to fully take advantage of the platform</a>.</p>
<p>Durable Objects are natively integrated into Cloudflare's infrastructure, giving you the ultimate serverless platform to build distributed stateful applications exploiting the entirety of Cloudflare's network.</p>
<h2 id="durable-objects-in-cloudflare">Durable Objects in Cloudflare</h2>
<p>Many of Cloudflare's products use Durable Objects. Some of our technical blog posts showcase real-world applications and use-cases where Durable Objects make building applications easier and simpler.</p>
<p>These blog posts may also serve as inspiration on how to architect scalable applications using Durable Objects, and how to integrate them with the rest of Cloudflare Developer Platform.</p>
<ul>
<li><a href="https://blog.cloudflare.com/how-we-built-cloudflare-queues/">Durable Objects aren't just durable, they're fast: a 10x speedup for Cloudflare Queues</a></li>
<li><a href="https://blog.cloudflare.com/behind-the-scenes-with-stream-live-cloudflares-live-streaming-service/">Behind the scenes with Stream Live, Cloudflare's live streaming service</a></li>
<li><a href="https://blog.cloudflare.com/do-it-again/">DO it again: how we used Durable Objects to add WebSockets support and authentication to AI Gateway</a></li>
<li><a href="https://blog.cloudflare.com/workers-builds-integrated-ci-cd-built-on-the-workers-platform/">Workers Builds: integrated CI/CD built on the Workers platform</a></li>
<li><a href="https://blog.cloudflare.com/building-workflows-durable-execution-on-workers/">Build durable applications on Cloudflare Workers: you write the Workflows, we take care of the rest</a></li>
<li><a href="https://blog.cloudflare.com/building-d1-a-global-database/">Building D1: a Global Database</a></li>
<li><a href="https://blog.cloudflare.com/billions-and-billions-of-logs-scaling-ai-gateway-with-the-cloudflare/">Billions and billions (of logs): scaling AI Gateway with the Cloudflare Developer Platform</a></li>
<li><a href="https://blog.cloudflare.com/r2-rayid-retrieval/">Indexing millions of HTTP requests using Durable Objects</a></li>
</ul>
<p>Finally, the following blog posts may help you learn some of the technical implementation aspects of Durable Objects, and how they work.</p>
<ul>
<li><a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">Durable Objects: Easy, Fast, Correct — Choose three</a></li>
<li><a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">Zero-latency SQLite storage in every Durable Object</a></li>
<li><a href="https://blog.cloudflare.com/introducing-workers-durable-objects/">Workers Durable Objects Beta: A New Approach to Stateful Serverless</a></li>
</ul>
<h2 id="get-started">Get started</h2>
<p>Get started now by following the <a href="/durable-objects/get-started/">&quot;Get started&quot; guide</a> to create your first application using Durable Objects.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Storage per Durable Object with SQLite is currently 1 GB. This will be raised to 10 GB for general availability.</li></ol></section>
