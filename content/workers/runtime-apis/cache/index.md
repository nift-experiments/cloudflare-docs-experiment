---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/cache/
  description: Control reading and writing from the Cloudflare global network cache.
  full_title: Cache · Cloudflare Workers docs
  head_html: <title>Cache · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Control reading and writing from the Cloudflare global network cache."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/cache/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/cache/index.md"><meta property="og:title" content="Cache · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control reading and writing from the Cloudflare global network cache."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/cache/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/cache/#page","headline":"Cache \u00b7 Cloudflare Workers docs","description":"Control reading and writing from the Cloudflare global network cache.","url":"https://developers.cloudflare.com/workers/runtime-apis/cache/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/cache/
  schema: 1
---
<h2 id="background">Background</h2>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/Cache">Cache API</a> allows fine grained control of reading and writing from the <a href="https://www.cloudflare.com/network/">Cloudflare global network</a> cache.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16170.md")
</aside>
<p>The Cache API is available globally but the contents of the cache do not replicate outside of the originating data center. A <code>GET /users</code> response can be cached in the originating data center, but will not exist in another data center unless it has been explicitly created.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="tiered-caching">Tiered caching</h3>
@markup("md", "content/.markup/bodies/16169.md")
</aside>
<p>Workers deployed to custom domains have access to functional <code>cache</code> operations. So do <a href="/pages/functions/">Pages functions</a>, whether attached to custom domains or <code>*.pages.dev</code> domains.</p>
<p>However, any Cache API operations in the Cloudflare Workers dashboard editor and <a href="/workers/playground/">Playground</a> previews will have no impact. For Workers fronted by <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>, the Cache API is not currently available.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16168.md")
</aside>
<hr />
<h2 id="accessing-cache">Accessing Cache</h2>
<p>The <code>caches.default</code> API is strongly influenced by the web browsers’ Cache API, but there are some important differences. For instance, Cloudflare Workers runtime exposes a single global cache object.</p>
<pre tabindex="0"><code class="language-js">let cache = caches.default;&#10;await cache.match(request);&#10;</code></pre>
<p>You may create and manage additional Cache instances via the <a href="https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage/open"><code>caches.open</code></a> method.</p>
<pre tabindex="0"><code class="language-js">let myCache = await caches.open(&#x27;custom:cache&#x27;);&#10;await myCache.match(request);&#10;</code></pre>
<hr />
<h2 id="headers">Headers</h2>
<p>Our implementation of the Cache API respects the following HTTP headers on the response passed to <code>put()</code>:</p>
<ul>
<li><code>Cache-Control</code>
<ul>
<li>Controls caching directives. This is consistent with <a href="/cache/concepts/cache-control#cache-control-directives">Cloudflare Cache-Control Directives</a>. Refer to <a href="/cache/how-to/configure-cache-status-code#edge-ttl">Edge TTL</a> for a list of HTTP response codes and their TTL when <code>Cache-Control</code> directives are not present.</li>
</ul>
</li>
<li><code>Cache-Tag</code>
<ul>
<li>Allows resource purging by tag(s) later.</li>
</ul>
</li>
<li><code>ETag</code>
<ul>
<li>Allows <code>cache.match()</code> to evaluate conditional requests with <code>If-None-Match</code>.</li>
</ul>
</li>
<li><code>Expires</code> string
<ul>
<li>A string that specifies when the resource becomes invalid.</li>
</ul>
</li>
<li><code>Last-Modified</code>
<ul>
<li>Allows <code>cache.match()</code> to evaluate conditional requests with <code>If-Modified-Since</code>.</li>
</ul>
</li>
</ul>
<p>This differs from the web browser Cache API as they do not honor any headers on the request or response.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16167.md")
</aside>
<hr />
<h2 id="methods">Methods</h2>
<h3 id="put"><code>Put</code></h3>
<pre tabindex="0"><code class="language-js">cache.put(request, response);&#10;</code></pre>
<ul>
<li>
<p><code>put(request, response)</code> : Promise</p>
<ul>
<li>Attempts to add a response to the cache, using the given request as the key. Returns a promise that resolves to <code>undefined</code> regardless of whether the cache successfully stored the response.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16166.md")
</aside>
<h4 id="parameters">Parameters</h4>
<ul>
<li>
<p><code>request</code> string | Request</p>
<ul>
<li>Either a string or a <a href="/workers/runtime-apis/request/"><code>Request</code></a> object to serve as the key. If a string is passed, it is interpreted as the URL for a new Request object.</li>
</ul>
</li>
<li>
<p><code>response</code> Response</p>
<ul>
<li>A <a href="/workers/runtime-apis/response/"><code>Response</code></a> object to store under the given key.</li>
</ul>
</li>
</ul>
<h4 id="invalid-parameters">Invalid parameters</h4>
<p><code>cache.put</code> will throw an error if:</p>
<ul>
<li>The <code>request</code> passed is a method other than <code>GET</code>.</li>
<li>The <code>response</code> passed has a <code>status</code> of <a href="https://www.webfx.com/web-development/glossary/http-status-codes/what-is-a-206-status-code/"><code>206 Partial Content</code></a>.</li>
<li>The <code>response</code> passed contains the header <code>Vary: *</code>. The value of the <code>Vary</code> header is an asterisk (<code>*</code>). Refer to the <a href="https://w3c.github.io/ServiceWorker/#cache-put">Cache API specification</a> for more information.</li>
</ul>
<h4 id="errors">Errors</h4>
<p><code>cache.put</code> returns a <code>413</code> error if <code>Cache-Control</code> instructs not to cache or if the response is too large.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16165.md")
</aside>
<h3 id="match"><code>Match</code></h3>
<pre tabindex="0"><code class="language-js">cache.match(request, options);&#10;</code></pre>
<ul>
<li>
<p><code>match(request, options)</code> : Promise<code>&lt;Response | undefined&gt;</code></p>
<ul>
<li>Returns a promise wrapping the response object keyed to that request.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16164.md")
</aside>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li>
<p><code>request</code> string | Request</p>
<ul>
<li>The string or <a href="/workers/runtime-apis/request/"><code>Request</code></a> object used as the lookup key. Strings are interpreted as the URL for a new <code>Request</code> object.</li>
</ul>
</li>
<li>
<p><code>options</code></p>
<ul>
<li>Can contain one possible property: <code>ignoreMethod</code> (Boolean). When <code>true</code>, the request is considered to be a <code>GET</code> request regardless of its actual value.</li>
</ul>
</li>
</ul>
<p>Unlike the browser Cache API, Cloudflare Workers do not support the <code>ignoreSearch</code> or <code>ignoreVary</code> options on <code>match()</code>. You can accomplish this behavior by removing query strings or HTTP headers at <code>put()</code> time.</p>
<p>Our implementation of the Cache API respects the following HTTP headers on the request passed to <code>match()</code>:</p>
<ul>
<li>
<p><code>Range</code></p>
<ul>
<li>Results in a <code>206</code> response if a matching response with a Content-Length header is found. Your Cloudflare cache always respects range requests, even if an <code>Accept-Ranges</code> header is on the response.</li>
</ul>
</li>
<li>
<p><code>If-Modified-Since</code></p>
<ul>
<li>Results in a <code>304</code> response if a matching response is found with a <code>Last-Modified</code> header with a value before the time specified in <code>If-Modified-Since</code>.</li>
</ul>
</li>
<li>
<p><code>If-None-Match</code></p>
<ul>
<li>Results in a <code>304</code> response if a matching response is found with an <code>ETag</code> header with a value that matches a value in <code>If-None-Match</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16163.md")
</aside>
<h4 id="errors-1">Errors</h4>
<p><code>cache.match</code> generates a <code>504</code> error response when the requested content is missing or expired. The Cache API does not expose this <code>504</code> directly to the Worker script, instead returning <code>undefined</code>. Nevertheless, the underlying <code>504</code> is still visible in Cloudflare Logs.</p>
<p>If you use Cloudflare Logs, you may see these <code>504</code> responses with the <code>RequestSource</code> of <code>edgeWorkerCacheAPI</code>. Again, these are expected if the cached asset was missing or expired. Note that <code>edgeWorkerCacheAPI</code> requests are already filtered out in other views, such as Cache Analytics. To filter out these requests or to filter requests by end users of your website only, refer to <a href="/analytics/graphql-api/features/filtering/#filter-end-users">Filter end users</a>.</p>
<h3 id="delete"><code>Delete</code></h3>
<pre tabindex="0"><code class="language-js">cache.delete(request, options);&#10;</code></pre>
<ul>
<li><code>delete(request, options)</code> : Promise<code>&lt;boolean&gt;</code></li>
</ul>
<p>Deletes the <code>Response</code> object from the cache and returns a <code>Promise</code> for a Boolean response:</p>
<ul>
<li><code>true</code>: The response was cached but is now deleted</li>
<li><code>false</code>: The response was not in the cache at the time of deletion.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="global-purges">Global purges</h3>
@markup("md", "content/.markup/bodies/16162.md")
</aside>
<h4 id="parameters-2">Parameters</h4>
<ul>
<li>
<p><code>request</code> string | Request</p>
<ul>
<li>The string or <a href="/workers/runtime-apis/request/"><code>Request</code></a> object used as the lookup key. Strings are interpreted as the URL for a new <code>Request</code> object.</li>
</ul>
</li>
<li>
<p><code>options</code> object</p>
<ul>
<li>Can contain one possible property: <code>ignoreMethod</code> (Boolean). Consider the request method a GET regardless of its actual value.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/reference/how-the-cache-works/">How the cache works</a></li>
<li><a href="/workers/examples/cache-using-fetch/">Example: Cache using <code>fetch()</code></a></li>
<li><a href="/workers/examples/cache-api/">Example: using the Cache API</a></li>
<li><a href="/workers/examples/cache-post-request/">Example: caching POST requests</a></li>
</ul>
