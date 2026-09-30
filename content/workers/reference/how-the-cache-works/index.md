---
cp9:
  canonical: https://developers.cloudflare.com/workers/reference/how-the-cache-works/
  description: How Workers interacts with the Cloudflare cache.
  full_title: How the Cache works · Cloudflare Workers docs
  head_html: <title>How the Cache works · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="How Workers interacts with the Cloudflare cache."><link rel="canonical" href="https://developers.cloudflare.com/workers/reference/how-the-cache-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/reference/how-the-cache-works/index.md"><meta property="og:title" content="How the Cache works · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Workers interacts with the Cloudflare cache."><meta property="og:url" content="https://developers.cloudflare.com/workers/reference/how-the-cache-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/reference/how-the-cache-works/#page","headline":"How the Cache works \u00b7 Cloudflare Workers docs","description":"How Workers interacts with the Cloudflare cache.","url":"https://developers.cloudflare.com/workers/reference/how-the-cache-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/reference/how-the-cache-works/
  schema: 1
---
<p>Workers was designed and built on top of Cloudflare's global network to allow developers to interact directly with the Cloudflare cache. The cache can provide ephemeral, data center-local storage, as a convenient way to frequently access static or dynamic content.</p>
<p>By allowing developers to write to the cache, Workers provide a way to customize cache behavior on Cloudflare’s CDN. To learn about the benefits of caching, refer to the Learning Center’s article on <a href="https://www.cloudflare.com/learning/cdn/what-is-caching/">What is Caching?</a>.</p>
<p>Cloudflare Workers run before the cache but can also be utilized to modify assets once they are returned from the cache. Modifying assets returned from cache allows for the ability to sign or personalize responses while also reducing load on an origin and reducing latency to the end user by serving assets from a nearby location.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16184.md")
</aside>
<h2 id="interact-with-the-cloudflare-cache">Interact with the Cloudflare Cache</h2>
<p>Conceptually, there are two ways to interact with Cloudflare’s Cache using a Worker:</p>
<ul>
<li>
<p>Call to <a href="/workers/runtime-apis/fetch/"><code>fetch()</code></a> in a Workers script. Requests proxied through Cloudflare are cached even without Workers according to a zone’s default or configured behavior (for example, static assets like files ending in <code>.jpg</code> are cached by default). Workers can further customize this behavior by:</p>
<ul>
<li>Setting Cloudflare cache rules (that is, operating on the <code>cf</code> object of a <a href="/workers/runtime-apis/request/">request</a>).</li>
</ul>
</li>
<li>
<p>Store responses using the <a href="/workers/runtime-apis/cache/">Cache API</a> from a Workers script. This allows caching responses that did not come from an origin and also provides finer control by:</p>
<ul>
<li>
<p>Customizing cache behavior of any asset by setting headers such as <code>Cache-Control</code> on the response passed to <code>cache.put()</code>.</p>
</li>
<li>
<p>Caching responses generated by the Worker itself through <code>cache.put()</code>.</p>
</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="tiered-caching">Tiered caching</h3>
@markup("md", "content/.markup/bodies/16183.md")
</aside>
<h3 id="single-file-purge-assets-cached-by-a-worker">Single file purge assets cached by a worker</h3>
<p>When using single-file purge to purge assets cached by a Worker, make sure not to purge the end user URL. Instead, purge the URL that is in the <code>fetch</code> request. For example, you have a Worker that runs on <code>https://example.com/hello</code> and this Worker makes a <code>fetch</code> request to <code>https://notexample.com/hello</code>.</p>
<p>As far as cache is concerned, the asset in the <code>fetch</code> request (<code>https://notexample.com/hello</code>) is the asset that is cached. To purge it, you need to purge <code>https://notexample.com/hello</code>.</p>
<p>Purging the end user URL, <code>https://example.com/hello</code>, will not work because that is not the URL that cache sees. You need to confirm in your Worker which URL you are actually fetching, so you can purge the correct asset.</p>
<p>In the previous example, <code>https://notexample.com/hello</code> is not proxied through Cloudflare. If <code>https://notexample.com/hello</code> was proxied (<a href="/dns/proxy-status/">orange-clouded</a>) through Cloudflare, then you must own <code>notexample.com</code> and purge <code>https://notexample.com/hello</code> from the <code>notexample.com</code> zone.</p>
<p>To better understand the example, review the following diagram:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart TD&#10;accTitle: Single file purge  assets cached by a worker&#10;accDescr: This diagram is meant to help choose how to purge a file.&#10;A(&quot;You have a Worker script that runs on &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;example.com/hello&lt;/code&gt; &lt;br&gt; and this Worker makes a &lt;code&gt;fetch&lt;/code&gt; request to &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;notexample.com/hello&lt;/code&gt;.&quot;) --&gt; B(Is &lt;code&gt;notexample.com&lt;/code&gt; &lt;br&gt; an active zone on Cloudflare?)&#10;    B -- Yes --&gt; C(Is &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;notexample.com/&lt;/code&gt; &lt;br&gt; proxied through Cloudflare?)&#10;    B -- No  --&gt; D(Purge &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;notexample.com/hello&lt;/code&gt; &lt;br&gt; from the original &lt;code&gt;example.com&lt;/code&gt; zone.)&#10;    C -- Yes --&gt; E(Do you own &lt;br&gt; &lt;code&gt;notexample.com&lt;/code&gt;?)&#10;    C -- No --&gt; F(Purge &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;notexample.com/hello&lt;/code&gt; &lt;br&gt; from the original &lt;code&gt;example.com&lt;/code&gt; zone.)&#10;    E -- Yes --&gt; G(Purge &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;notexample.com/hello&lt;/code&gt; &lt;br&gt; from the &lt;code&gt;notexample.com&lt;/code&gt; zone.)&#10;    E -- No --&gt; H(Sorry, you can not purge the asset. &lt;br&gt; Only the owner of &lt;code&gt;notexample.com&lt;/code&gt; can purge it.)&#10;</code></pre>
<h3 id="purge-assets-stored-with-the-cache-api">Purge assets stored with the Cache API</h3>
<p>Assets stored in the cache through <a href="/workers/runtime-apis/cache/">Cache API</a> operations can be purged in a couple of ways:</p>
<ul>
<li>
<p>Call <code>cache.delete</code> within a Worker to invalidate the cache for the asset with a matching request variable.</p>
<ul>
<li>Assets purged in this way are only purged locally to the data center the Worker runtime was executed.</li>
</ul>
</li>
<li>
<p>To purge an asset globally, use the standard <a href="/cache/how-to/purge-cache/">cache purge options</a>. Based on cache API implementation, not all cache purge endpoints function for purging assets stored by the Cache API.</p>
<ul>
<li>
<p>All assets on a zone can be purged by using the <a href="/cache/how-to/purge-cache/purge-everything/">Purge Everything</a> cache operation. This purge will remove all assets associated with a Cloudflare zone from cache in all data centers regardless of the method set.</p>
</li>
<li>
<p><a href="/cache/how-to/purge-cache/purge-by-tags/#add-cache-tag-http-response-headers">Cache Tags</a> can be added to requests dynamically in a Worker by calling <code>response.headers.append()</code> and appending <code>Cache-Tag</code> values dynamically to that request. Once set, those tags can be used to selectively purge assets from cache without invalidating all cached assets on a zone.</p>
</li>
</ul>
</li>
<li>
<p>Currently, it is not possible to purge a URL that uses a custom cache key set by a Worker. Instead, use a <a href="/cache/how-to/cache-rules/settings/#cache-key">custom key created via Cache Rules</a>. Alternatively, purge your assets using purge everything, purge by tag, purge by host or purge by prefix.</p>
</li>
</ul>
<h2 id="edge-versus-browser-caching">Edge versus browser caching</h2>
<p>The browser cache is controlled through the <code>Cache-Control</code> header sent in the response to the client (the <code>Response</code> instance return from the handler). Workers can customize browser cache behavior by setting this header on the response.</p>
<p>Other means to control Cloudflare’s cache that are not mentioned in this documentation include: Page Rules and Cloudflare cache settings. Refer to the <a href="/cache/concepts/customize-cache/">How to customize Cloudflare’s cache</a> if you wish to avoid writing JavaScript with still some granularity of control.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="what-should-i-use-the-cache-api-or-fetch-for-caching-objects-on-cloudflare">What should I use: the Cache API or fetch for caching objects on Cloudflare?</h3>
@markup("md", "content/.markup/bodies/16182.md")
</aside>
<h3 id="fetch"><code>fetch</code></h3>
<p>In the context of Workers, a <a href="/workers/runtime-apis/fetch/"><code>fetch</code></a> provided by the runtime communicates with the Cloudflare cache. First, <code>fetch</code> checks to see if the URL matches a different zone. If it does, it reads through that zone’s cache (or Worker). Otherwise, it reads through its own zone’s cache, even if the URL is for a non-Cloudflare site. Cache settings on <code>fetch</code> automatically apply caching rules based on your Cloudflare settings. <code>fetch</code> does not allow you to modify or inspect objects before they reach the cache, but does allow you to modify how it will cache.</p>
<p>When a response fills the cache, the response header contains <code>CF-Cache-Status: HIT</code>. You can tell an object is attempting to cache if one sees the <code>CF-Cache-Status</code> at all.</p>
<p>This <a href="/workers/examples/cache-using-fetch/">template</a> shows ways to customize Cloudflare cache behavior on a given request using fetch.</p>
<h3 id="cache-api">Cache API</h3>
<p>The <a href="/workers/runtime-apis/cache/">Cache API</a> can be thought of as an ephemeral key-value store, whereby the <code>Request</code> object (or more specifically, the request URL) is the key, and the <code>Response</code> is the value.</p>
<p>There are two types of cache namespaces available to the Cloudflare Cache:</p>
<ul>
<li><strong><code>caches.default</code></strong> – You can access the default cache (the same cache shared with <code>fetch</code> requests) by accessing <code>caches.default</code>. This is useful when needing to override content that is already cached, after receiving the response.</li>
<li><strong><code>caches.open()</code></strong> – You can access a namespaced cache (separate from the cache shared with <code>fetch</code> requests) using <code>let cache = await caches.open(CACHE_NAME)</code>. Note that <a href="https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage/open"><code>caches.open</code></a> is an async function, unlike <code>caches.default</code>.</li>
</ul>
<p>When to use the Cache API:</p>
<ul>
<li>
<p>When you want to programmatically save and/or delete responses from a cache. For example, say an origin is responding with a <code>Cache-Control: max-age:0</code> header and cannot be changed. Instead, you can clone the <code>Response</code>, adjust the header to the <code>max-age=3600</code> value, and then use the Cache API to save the modified <code>Response</code> for an hour.</p>
</li>
<li>
<p>When you want to programmatically access a Response from a cache without relying on a <code>fetch</code> request. For example, you can check to see if you have already cached a <code>Response</code> for the <code>https://example.com/slow-response</code> endpoint. If so, you can avoid the slow request.</p>
</li>
</ul>
<p>This <a href="/workers/examples/cache-api/">template</a> shows ways to use the cache API. For limits of the cache API, refer to <a href="/workers/platform/limits/#cache-api-limits">Limits</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="tiered-caching-and-the-cache-api">Tiered caching and the Cache API</h3>
@markup("md", "content/.markup/bodies/16181.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/cache/">Cache API</a></li>
<li><a href="/cache/interaction-cloudflare-products/workers/">Customize cache behavior with Workers</a></li>
</ul>
