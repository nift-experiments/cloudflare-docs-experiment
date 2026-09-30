---
cp9:
  canonical: https://developers.cloudflare.com/kv/api/read-key-value-pairs/
  description: Retrieve values from a Workers KV namespace using the get() method, with support for types, caching, and metadata.
  full_title: Read key-value pairs · Cloudflare Workers KV docs
  head_html: <title>Read key-value pairs · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Retrieve values from a Workers KV namespace using the get() method, with support for types, caching, and metadata."><link rel="canonical" href="https://developers.cloudflare.com/kv/api/read-key-value-pairs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/api/read-key-value-pairs/index.md"><meta property="og:title" content="Read key-value pairs · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Retrieve values from a Workers KV namespace using the get() method, with support for types, caching, and metadata."><meta property="og:url" content="https://developers.cloudflare.com/kv/api/read-key-value-pairs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/api/read-key-value-pairs/#page","headline":"Read key-value pairs \u00b7 Cloudflare Workers KV docs","description":"Retrieve values from a Workers KV namespace using the get() method, with support for types, caching, and metadata.","url":"https://developers.cloudflare.com/kv/api/read-key-value-pairs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/api/read-key-value-pairs/
  schema: 1
---
<p>To get the value for a given key, call the <code>get()</code> method of the <a href="/kv/concepts/kv-bindings/">KV binding</a> on any <a href="/kv/concepts/kv-namespaces/">KV namespace</a> you have bound to your Worker code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9557.md")
</div></div>
<p>The <code>get()</code> method returns a promise you can <code>await</code> on to get the value.</p>
<p>If you request a single key as a string, you will get a single response in the promise. If the key is not found, the promise will resolve with the literal value <code>null</code>.</p>
<p>You can also request an array of keys. The return value with be a <code>Map</code> of the key-value pairs found,
with keys not found having <code>null</code> values.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9560.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9554.md")
</aside>
<h2 id="reference">Reference</h2>
<p>The following methods are provided to read from KV:</p>
<ul>
<li><a href="#request-a-single-key-with-getkey-string">get()</a></li>
<li><a href="#request-multiple-keys-with-getkeys-string">getWithMetadata()</a></li>
</ul>
<h3 id="get-method"><code>get()</code> method</h3>
<p>Use the <code>get()</code> method to get a single value, or multiple values if given multiple keys:</p>
<ul>
<li>Read single keys with <a href="#request-a-single-key-with-getkey-string">get(key: string)</a></li>
<li>Read multiple keys with <a href="#request-multiple-keys-with-getkeys-string">get(keys: string[])</a></li>
</ul>
<h4 id="request-a-single-key-with-get-key-string">Request a single key with <code>get(key: string)</code></h4>
<p>To get the value for a single key, call the <code>get()</code> method on any KV namespace you have bound to your Worker code with:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9563.md")
</div></div>
<h5 id="parameters">Parameters</h5>
<ul>
<li><code>key</code>: <code>string</code>
<ul>
<li>The key of the KV pair.</li>
</ul>
</li>
<li><code>type</code>: <code>&quot;text&quot; | &quot;json&quot; | &quot;arrayBuffer&quot; | &quot;stream&quot;</code>
<ul>
<li>Optional. The type of the value to be returned. <code>text</code> is the default.</li>
</ul>
</li>
<li><code>options</code>: <code>{ cacheTtl?: number, type?: &quot;text&quot; | &quot;json&quot; | &quot;arrayBuffer&quot; | &quot;stream&quot; }</code>
<ul>
<li>Optional. Object containing the optional <code>cacheTtl</code> and <code>type</code> properties. The <code>cacheTtl</code> property defines the length of time in seconds that a KV result is cached in the global network location it is accessed from (minimum: 30). The <code>type</code> property defines the type of the value to be returned.</li>
</ul>
</li>
</ul>
<h5 id="response">Response</h5>
<ul>
<li><code>response</code>: <code>Promise&lt;string | Object | ArrayBuffer | ReadableStream | null&gt;</code>
<ul>
<li>The value for the requested KV pair. The response type will depend on the <code>type</code> parameter provided for the <code>get()</code> command as follows:</li>
<li><code>text</code>: A <code>string</code> (default).</li>
<li><code>json</code>: An object decoded from a JSON string.</li>
<li><code>arrayBuffer</code>: An <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer"><code>ArrayBuffer</code></a> instance.</li>
<li><code>stream</code>: A <a href="https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream"><code>ReadableStream</code></a>.</li>
</ul>
</li>
</ul>
<h4 id="request-multiple-keys-with-get-keys-string">Request multiple keys with <code>get(keys: string[])</code></h4>
<p>To get the values for multiple keys, call the <code>get()</code> method on any KV namespace you have bound to your Worker code with:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9566.md")
</div></div>
<h5 id="parameters-1">Parameters</h5>
<ul>
<li><code>keys</code>: <code>string[]</code>
<ul>
<li>The keys of the KV pairs. Max: 100 keys</li>
</ul>
</li>
<li><code>type</code>: <code>&quot;text&quot; | &quot;json&quot;</code>
<ul>
<li>Optional. The type of the value to be returned. <code>text</code> is the default.</li>
</ul>
</li>
<li><code>options</code>: <code>{ cacheTtl?: number, type?: &quot;text&quot; | &quot;json&quot; }</code>
<ul>
<li>Optional. Object containing the optional <code>cacheTtl</code> and <code>type</code> properties. The <code>cacheTtl</code> property defines the length of time in seconds that a KV result is cached in the global network location it is accessed from (minimum: 30). The <code>type</code> property defines the type of the value to be returned.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9553.md")
</aside>
<h5 id="response-1">Response</h5>
<ul>
<li><code>response</code>: <code>Promise&lt;Map&lt;string, string | Object | null&gt;&gt;</code>
<ul>
<li>The value for the requested KV pair. If no key is found, <code>null</code> is returned for the key. The response type will depend on the <code>type</code> parameter provided for the <code>get()</code> command as follows:
<ul>
<li><code>text</code>: A <code>string</code> (default).</li>
<li><code>json</code>: An object decoded from a JSON string.</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The limit of the response size is 25 MB. Responses above this size will fail with a <code>413 Error</code> error message.</p>
<h3 id="getwithmetadata-method"><code>getWithMetadata()</code> method</h3>
<p>Use the <code>getWithMetadata()</code> method to get a single value along with its metadata, or multiple values with their metadata:</p>
<ul>
<li>Read single keys with <a href="#request-a-single-key-with-getwithmetadatakey-string">getWithMetadata(key: string)</a></li>
<li>Read multiple keys with <a href="#request-multiple-keys-with-getwithmetadatakeys-string">getWithMetadata(keys: string[])</a></li>
</ul>
<h4 id="request-a-single-key-with-getwithmetadata-key-string">Request a single key with <code>getWithMetadata(key: string)</code></h4>
<p>To get the value for a given key along with its metadata, call the <code>getWithMetadata()</code> method on any KV namespace you have bound to your Worker code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9569.md")
</div></div>
<p>Metadata is a serializable value you append to each KV entry.</p>
<h5 id="parameters-2">Parameters</h5>
<ul>
<li><code>key</code>: <code>string</code>
<ul>
<li>The key of the KV pair.</li>
</ul>
</li>
<li><code>type</code>: <code>&quot;text&quot; | &quot;json&quot; | &quot;arrayBuffer&quot; | &quot;stream&quot;</code>
<ul>
<li>Optional. The type of the value to be returned. <code>text</code> is the default.</li>
</ul>
</li>
<li><code>options</code>: <code>{ cacheTtl?: number, type?: &quot;text&quot; | &quot;json&quot; | &quot;arrayBuffer&quot; | &quot;stream&quot; }</code>
<ul>
<li>Optional. Object containing the optional <code>cacheTtl</code> and <code>type</code> properties. The <code>cacheTtl</code> property defines the length of time in seconds that a KV result is cached in the global network location it is accessed from (minimum: 30). The <code>type</code> property defines the type of the value to be returned.</li>
</ul>
</li>
</ul>
<h5 id="response-2">Response</h5>
<ul>
<li>
<p><code>response</code>: <code>Promise&lt;{ value: string | Object | ArrayBuffer | ReadableStream | null, metadata: string | null }&gt;</code></p>
<ul>
<li>An object containing the value and the metadata for the requested KV pair. The type of the value attribute will depend on the <code>type</code> parameter provided for the <code>getWithMetadata()</code> command as follows:
<ul>
<li><code>text</code>: A <code>string</code> (default).</li>
<li><code>json</code>: An object decoded from a JSON string.</li>
<li><code>arrayBuffer</code>: An <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer"><code>ArrayBuffer</code></a> instance.</li>
<li><code>stream</code>: A <a href="https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream"><code>ReadableStream</code></a>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>If there is no metadata associated with the requested key-value pair, <code>null</code> will be returned for metadata.</p>
<h4 id="request-multiple-keys-with-getwithmetadata-keys-string">Request multiple keys with <code>getWithMetadata(keys: string[])</code></h4>
<p>To get the values for a given set of keys along with their metadata, call the <code>getWithMetadata()</code> method on any KV namespace you have bound to your Worker code with:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9572.md")
</div></div>
<h5 id="parameters-3">Parameters</h5>
<ul>
<li><code>keys</code>: <code>string[]</code>
<ul>
<li>The keys of the KV pairs. Max: 100 keys</li>
</ul>
</li>
<li><code>type</code>: <code>&quot;text&quot; | &quot;json&quot;</code>
<ul>
<li>Optional. The type of the value to be returned. <code>text</code> is the default.</li>
</ul>
</li>
<li><code>options</code>: <code>{ cacheTtl?: number, type?: &quot;text&quot; | &quot;json&quot; }</code>
<ul>
<li>Optional. Object containing the optional <code>cacheTtl</code> and <code>type</code> properties. The <code>cacheTtl</code> property defines the length of time in seconds that a KV result is cached in the global network location it is accessed from (minimum: 30). The <code>type</code> property defines the type of the value to be returned.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9552.md")
</aside>
<h5 id="response-3">Response</h5>
<ul>
<li>
<p><code>response</code>: <code>Promise&lt;Map&lt;string , { value: string | Object | null, metadata: string | Object | null }&gt;</code></p>
<ul>
<li>An object containing the value and the metadata for the requested KV pair. The type of the value attribute will depend on the <code>type</code> parameter provided for the <code>getWithMetadata()</code> command as follows:
<ul>
<li><code>text</code>: A <code>string</code> (default).</li>
<li><code>json</code>: An object decoded from a JSON string.</li>
</ul>
</li>
<li>The type of the metadata will just depend on what is stored, which can be either a string or an object.</li>
</ul>
</li>
</ul>
<p>If there is no metadata associated with the requested key-value pair, <code>null</code> will be returned for metadata.</p>
<p>The limit of the response size is 25 MB. Responses above this size will fail with a <code>413 Error</code> error message.</p>
<h2 id="guidance">Guidance</h2>
<h3 id="type-parameter">Type parameter</h3>
<p>For simple values, use the default <code>text</code> type which provides you with your value as a <code>string</code>. For convenience, a <code>json</code> type is also specified which will convert a JSON value into an object before returning the object to you. For large values, use <code>stream</code> to request a <code>ReadableStream</code>. For binary values, use <code>arrayBuffer</code> to request an <code>ArrayBuffer</code>.</p>
<p>For large values, the choice of <code>type</code> can have a noticeable effect on latency and CPU usage. For reference, the <code>type</code> can be ordered from fastest to slowest as <code>stream</code>, <code>arrayBuffer</code>, <code>text</code>, and <code>json</code>.</p>
<h3 id="cachettl-parameter">CacheTtl parameter</h3>
<p><code>cacheTtl</code> is a parameter that defines the length of time in seconds that a KV result is cached in the global network location it is accessed from.</p>
<p>Defining the length of time in seconds is useful for reducing cold read latency on keys that are read relatively infrequently. <code>cacheTtl</code> is useful if your data is write-once or write-rarely.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="hot-and-cold-read">Hot and cold read</h3>
@markup("md", "content/.markup/bodies/9551.md")
</aside>
<p><code>cacheTtl</code> is not recommended if your data is updated often and you need to see updates shortly after they are written, because writes that happen from other global network locations will not be visible until the cached value expires.</p>
<p>The <code>cacheTtl</code> parameter must be an integer greater than or equal to <code>30</code>. <code>60</code> is the default. The maximum value for <code>cacheTtl</code> is <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER"><code>Number.MAX_SAFE_INTEGER</code></a>.</p>
<p>Once a key has been read with a given <code>cacheTtl</code> in a region, it will remain cached in that region until the end of the <code>cacheTtl</code> or eviction. This affects regional and central tiers of KV's built-in caching layers. When writing to Workers KV, the regions in the regional and central caching layers internal to KV will get revalidated with the newly written result.</p>
<h3 id="requesting-more-keys-per-worker-invocation-with-bulk-requests">Requesting more keys per Worker invocation with bulk requests</h3>
<p>Workers are limited to 1,000 operations to external services per invocation. This applies to Workers KV, as documented in <a href="/kv/platform/limits/">Workers KV limits</a>.</p>
<p>To read more than 1,000 keys per operation, you can use the bulk read operations to read multiple keys in a single operation. These count as a single operation against the 1,000 operation limit.</p>
<h3 id="reducing-cardinality-by-coalescing-keys">Reducing cardinality by coalescing keys</h3>
<p>If you have a set of related key-value pairs that have a mixed usage pattern (some hot keys and some cold keys), consider coalescing them. By coalescing cold keys with hot keys, cold keys will be cached alongside hot keys which can provide faster reads than if they were uncached as individual keys.</p>
<h4 id="merging-into-a-super-kv-entry">Merging into a &quot;super&quot; KV entry</h4>
<p>One coalescing technique is to make all the keys and values part of a super key-value object. An example is shown below.</p>
<pre tabindex="0"><code>key1: value1&#10;key2: value2&#10;key3: value3&#10;</code></pre>
<p>becomes</p>
<pre tabindex="0"><code>coalesced: {&#10;  key1: value1,&#10;  key2: value2,&#10;  key3: value3,&#10;}&#10;</code></pre>
<p>By coalescing the values, the cold keys benefit from being kept warm in the cache because of access patterns of the warmer keys.</p>
<p>This works best if you are not expecting the need to update the values independently of each other, which can pose race conditions.</p>
<ul>
<li><strong>Advantage</strong>: Infrequently accessed keys are kept in the cache.</li>
<li><strong>Disadvantage</strong>: Size of the resultant value can push your worker out of its memory limits. Safely updating the value requires a <a href="/kv/api/write-key-value-pairs/#concurrent-writes-to-the-same-key">locking mechanism</a> of some kind.</li>
</ul>
<h2 id="other-methods-to-access-kv">Other methods to access KV</h2>
<p>You can <a href="/kv/reference/kv-commands/#kv-key-get">read key-value pairs from the command line with Wrangler</a> and <a href="/api/resources/kv/subresources/namespaces/subresources/values/methods/get/">from the REST API</a>.</p>
