---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/
  description: Define rate limits and interact with them directly from your Cloudflare Worker
  full_title: Rate Limiting · Cloudflare Workers docs
  head_html: <title>Rate Limiting · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Define rate limits and interact with them directly from your Cloudflare Worker"><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/index.md"><meta property="og:title" content="Rate Limiting · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Define rate limits and interact with them directly from your Cloudflare Worker"><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/#page","headline":"Rate Limiting \u00b7 Cloudflare Workers docs","description":"Define rate limits and interact with them directly from your Cloudflare Worker","url":"https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/bindings/rate-limit/
  schema: 1
---
<p>The Rate Limiting API lets you define rate limits and write code around them in your Worker.</p>
<p>You can use it to enforce:</p>
<ul>
<li>Rate limits that are applied after your Worker starts, only once a specific part of your code is reached</li>
<li>Different rate limits for different types of customers or users (ex: free vs. paid)</li>
<li>Resource-specific or path-specific limits (ex: limit per API route)</li>
<li>Any combination of the above</li>
</ul>
<p>The Rate Limiting API is backed by the same infrastructure that serves <a href="/waf/rate-limiting-rules/">rate limiting rules</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17187.md")
</aside>
<h2 id="get-started">Get started</h2>
<p>First, add a <a href="/workers/runtime-apis/bindings">binding</a> to your Worker that gives it access to the Rate Limiting API:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17188.md")
</div>
<p>This binding makes the <code>MY_RATE_LIMITER</code> binding available, which provides a <code>limit()</code> method:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17191.md")
</div></div>
<p>The <code>limit()</code> API accepts a single argument — a configuration object with the <code>key</code> field.</p>
<ul>
<li>The key you provide can be any <code>string</code> value.</li>
<li>A common pattern is to define your key by combining a string that uniquely identifies the actor initiating the request (ex: a user ID or customer ID) and a string that identifies a specific resource (ex: a particular API route).</li>
</ul>
<p>You can define and configure multiple rate limiting configurations per Worker, which allows you to define different limits against incoming request and/or user parameters as needed to protect your application or upstream APIs.</p>
<p>For example, here is how you can define two rate limiting configurations for free and paid tier users:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17192.md")
</div>
<h2 id="configuration">Configuration</h2>
<p>A rate limiting binding has the following settings:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>namespace_id</code></td>
<td><code>string</code></td>
<td>A string containing a positive integer that uniquely defines this rate limiting namespace within your Cloudflare account (for example, <code>&quot;1001&quot;</code>). Although the value must be a valid integer, it is specified as a string. This is intentional.</td>
</tr>
<tr>
<td><code>simple</code></td>
<td><code>object</code></td>
<td>The rate limit configuration. <code>simple</code> is the only supported type.</td>
</tr>
<tr>
<td><code>simple.limit</code></td>
<td><code>number</code></td>
<td>The number of allowed requests (or calls to <code>limit()</code>) within the given <code>period</code>.</td>
</tr>
<tr>
<td><code>simple.period</code></td>
<td><code>number</code></td>
<td>The duration of the rate limit window, in seconds. Must be either <code>10</code> or <code>60</code>.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17186.md")
</aside>
<p>For example, to apply a rate limit of 1500 requests per minute, you would define a rate limiting configuration as follows:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17193.md")
</div>
<h2 id="best-practices">Best practices</h2>
<p>The <code>key</code> passed to the <code>limit</code> function, that determines what to rate limit on, should represent a unique characteristic of a user or class of user that you wish to rate limit.</p>
<ul>
<li>Good choices include API keys in <code>Authorization</code> HTTP headers, URL paths or routes, specific query parameters used by your application, and/or user IDs and tenant IDs. These are all stable identifiers and are unlikely to change from request-to-request.</li>
<li>It is not recommended to use IP addresses or locations (regions or countries), since these can be shared by many users in many valid cases. You may find yourself unintentionally rate limiting a wider group of users than you intended by rate limiting on these keys.</li>
</ul>
<pre tabindex="0"><code class="language-ts">// Recommended: use a key that represents a specific user or class of user&#10;const url = new URL(req.url)&#10;const userId = url.searchParams.get(&quot;userId&quot;) || &quot;&quot;&#10;const { success } = await env.MY_RATE_LIMITER.limit({ key: userId })&#10;&#10;// Not recommended:  many users may share a single IP, especially on mobile networks&#10;// or when using privacy-enabling proxies&#10;const ipAddress = req.headers.get(&quot;cf-connecting-ip&quot;) || &quot;&quot;&#10;const { success } = await env.MY_RATE_LIMITER.limit({ key: ipAddress })&#10;</code></pre>
<h2 id="locality">Locality</h2>
<p>Rate limits that you define and enforce in your Worker are local to the <a href="https://www.cloudflare.com/network/">Cloudflare location</a> that your Worker runs in.</p>
<p>For example, if a request comes in from Sydney, Australia, to the Worker shown above, after 100 requests in a 60 second window, any further requests for a particular path would be rejected, and a 429 HTTP status code returned. But this would only apply to requests served in Sydney. For each unique key you pass to your rate limiting binding, there is a unique limit per Cloudflare location.</p>
<h2 id="performance">Performance</h2>
<p>The Rate Limiting API in Workers is designed to be fast.</p>
<p>The underlying counters are cached on the same machine that your Worker runs in, and updated asynchronously in the background by communicating with a backing store that is within the same Cloudflare location.</p>
<p>This means that while in your code you <code>await</code> a call to the <code>limit()</code> method:</p>
<pre tabindex="0"><code class="language-javascript">const { success } = await env.MY_RATE_LIMITER.limit({ key: customerId })&#10;</code></pre>
<p>You are not waiting on a network request. You can use the Rate Limiting API without introducing any meaningful latency to your Worker.</p>
<h2 id="accuracy">Accuracy</h2>
<p>The above also means that the Rate Limiting API is permissive, eventually consistent, and intentionally designed to not be used as an accurate accounting system.</p>
<p>For example, if many requests come in to your Worker in a single Cloudflare location, all rate limited on the same key, the <a href="/workers/reference/how-workers-works">isolate</a> that serves each request will check against its locally cached value of the rate limit. Very quickly, but not immediately, these requests will count towards the rate limit within that Cloudflare location.</p>
<h2 id="monitoring">Monitoring</h2>
<p>Rate limiting bindings are not currently visible in the Cloudflare dashboard. To monitor rate-limited requests from your Worker:</p>
<ul>
<li><strong><a href="/workers/observability/">Workers Observability</a></strong> — Use <a href="/workers/observability/logs/workers-logs/">Workers Logs</a> and <a href="/workers/observability/traces/">Traces</a> to observe HTTP 429 responses returned by your Worker when rate limits are exceeded.</li>
<li><strong><a href="/analytics/analytics-engine/">Workers Analytics Engine</a></strong> — Add an Analytics Engine binding to your Worker and emit custom data points (for example, a <code>rate_limited</code> event) when <code>limit()</code> returns <code>{ success: false }</code>. This lets you build dashboards and query rate limiting metrics over time.</li>
</ul>
<h2 id="examples">Examples</h2>
<ul>
<li><a href="https://github.com/elithrar/workers-hono-rate-limit"><code>@elithrar/workers-hono-rate-limit</code></a> — Middleware that lets you easily add rate limits to routes in your <a href="https://hono.dev/">Hono</a> application.</li>
<li><a href="https://github.com/rhinobase/hono-rate-limiter"><code>@hono-rate-limiter/cloudflare</code></a> — Middleware that lets you easily add rate limits to routes in your <a href="https://hono.dev/">Hono</a> application, with multiple data stores to choose from.</li>
<li><a href="https://github.com/bytaesu/hono-cf-rate-limit"><code>hono-cf-rate-limit</code></a> — Middleware for Hono applications that applies rate limiting in Cloudflare Workers, powered by Wrangler’s built-in features.</li>
</ul>
