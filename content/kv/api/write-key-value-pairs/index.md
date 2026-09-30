---
cp9:
  canonical: https://developers.cloudflare.com/kv/api/write-key-value-pairs/
  description: Store data in a Workers KV namespace using the put() method, with options for expiration and metadata.
  full_title: Write key-value pairs · Cloudflare Workers KV docs
  head_html: <title>Write key-value pairs · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Store data in a Workers KV namespace using the put() method, with options for expiration and metadata."><link rel="canonical" href="https://developers.cloudflare.com/kv/api/write-key-value-pairs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/api/write-key-value-pairs/index.md"><meta property="og:title" content="Write key-value pairs · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Store data in a Workers KV namespace using the put() method, with options for expiration and metadata."><meta property="og:url" content="https://developers.cloudflare.com/kv/api/write-key-value-pairs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/api/write-key-value-pairs/#page","headline":"Write key-value pairs \u00b7 Cloudflare Workers KV docs","description":"Store data in a Workers KV namespace using the put() method, with options for expiration and metadata.","url":"https://developers.cloudflare.com/kv/api/write-key-value-pairs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/api/write-key-value-pairs/
  schema: 1
---
<p>To create a new key-value pair, or to update the value for a particular key, call the <code>put()</code> method of the <a href="/kv/concepts/kv-bindings/">KV binding</a> on any <a href="/kv/concepts/kv-namespaces/">KV namespace</a> you have bound to your Worker code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9532.md")
</div></div>
<h4 id="example">Example</h4>
<p>An example of writing a key-value pair from within a Worker:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9535.md")
</div></div>
<h2 id="reference">Reference</h2>
<p>The following method is provided to write to KV:</p>
<ul>
<li><a href="#put-method">put()</a></li>
</ul>
<h3 id="put-method"><code>put()</code> method</h3>
<p>To create a new key-value pair, or to update the value for a particular key, call the <code>put()</code> method on any KV namespace you have bound to your Worker code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9538.md")
</div></div>
<h4 id="parameters">Parameters</h4>
<ul>
<li>
<p><code>key</code>: <code>string</code></p>
<ul>
<li>The key to associate with the value. A key cannot be empty or be exactly equal to <code>.</code> or <code>..</code>. All other keys are valid. Keys have a maximum length of 512 bytes.</li>
</ul>
</li>
<li>
<p><code>value</code>: <code>string</code> | <code>ReadableStream</code> | <code>ArrayBuffer</code></p>
<ul>
<li>The value to store. The type is inferred. The maximum size of a value is 25 MiB.</li>
</ul>
</li>
<li>
<p><code>options</code>: <code>{ expiration?: number, expirationTtl?: number, metadata?: object }</code></p>
<ul>
<li>Optional. An object containing the <code>expiration</code> (optional), <code>expirationTtl</code> (optional), and <code>metadata</code> (optional) attributes.
<ul>
<li><code>expiration</code> is the number that represents when to expire the key-value pair in seconds since epoch.</li>
<li><code>expirationTtl</code> is the number that represents when to expire the key-value pair in seconds from now. The minimum value is 60.</li>
<li><code>metadata</code> is an object that must serialize to JSON. The maximum size of the serialized JSON representation of the metadata object is 1024 bytes.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h4 id="response">Response</h4>
<ul>
<li><code>response</code>: <code>Promise&lt;void&gt;</code>
<ul>
<li>A <code>Promise</code> that resolves if the update is successful.</li>
</ul>
</li>
</ul>
<p>The put() method returns a Promise that you should <code>await</code> on to verify a successful update.</p>
<h2 id="guidance">Guidance</h2>
<h3 id="concurrent-writes-to-the-same-key">Concurrent writes to the same key</h3>
<p>Due to the eventually consistent nature of KV, concurrent writes to the same key can end up overwriting one another. It is a common pattern to write data from a single process with Wrangler, Durable Objects, or the API. This avoids competing concurrent writes because of the single stream. All data is still readily available within all Workers bound to the namespace.</p>
<p>If concurrent writes are made to the same key, the last write will take precedence.</p>
<p>Writes are immediately visible to other requests in the same global network location, but can take up to 60 seconds (or the value of the <code>cacheTtl</code> parameter of the <code>get()</code> or <code>getWithMetadata()</code> methods) to be visible in other parts of the world.</p>
<p>Refer to <a href="/kv/concepts/how-kv-works/">How KV works</a> for more information on this topic.</p>
<h3 id="write-data-in-bulk">Write data in bulk</h3>
<p>Write more than one key-value pair at a time with Wrangler or <a href="/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_update/">via the REST API</a>.</p>
<p>The bulk API can accept up to 10,000 KV pairs at once.</p>
<p>A <code>key</code> and a <code>value</code> are required for each KV pair. The entire request size must be less than 100 megabytes. Bulk writes are not supported using the <a href="/kv/concepts/kv-bindings/">KV binding</a>.</p>
<h3 id="expiring-keys">Expiring keys</h3>
<p>KV offers the ability to create keys that automatically expire. You may configure expiration to occur either at a particular point in time (using the <code>expiration</code> option), or after a certain amount of time has passed since the key was last modified (using the <code>expirationTtl</code> option).</p>
<p>Once the expiration time of an expiring key is reached, it will be deleted from the system. After its deletion, attempts to read the key will behave as if the key does not exist. The deleted key will not count against the KV namespace’s storage usage for billing purposes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9529.md")
</aside>
<p>There are two ways to specify when a key should expire:</p>
<ul>
<li>
<p>Set a key's expiration using an absolute time specified in a number of <a href="https://en.wikipedia.org/wiki/Unix_time">seconds since the UNIX epoch</a>. For example, if you wanted a key to expire at 12:00AM UTC on April 1, 2019, you would set the key’s expiration to <code>1554076800</code>.</p>
</li>
<li>
<p>Set a key's expiration time to live (TTL) using a relative number of seconds from the current time. For example, if you wanted a key to expire 10 minutes after creating it, you would set its expiration TTL to <code>600</code>.</p>
</li>
</ul>
<p>Expiration targets that are less than 60 seconds into the future are not supported. This is true for both expiration methods.</p>
<h4 id="create-expiring-keys">Create expiring keys</h4>
<p>To create expiring keys, set <code>expiration</code> in the <code>put()</code> options to a number representing the seconds since epoch, or set <code>expirationTtl</code> in the <code>put()</code> options to a number representing the seconds from now:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9541.md")
</div></div>
<p>These assume that <code>secondsSinceEpoch</code>/<code>seconds_since_epoch</code> and <code>secondsFromNow</code>/<code>seconds_from_now</code> are variables defined elsewhere in your Worker code.</p>
<h3 id="metadata">Metadata</h3>
<p>To associate metadata with a key-value pair, set <code>metadata</code> in the <code>put()</code> options to an object (serializable to JSON):</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9544.md")
</div></div>
<h3 id="limits-to-kv-writes-to-the-same-key">Limits to KV writes to the same key</h3>
<p>Workers KV has a maximum of 1 write to the same key per second. Writes made to the same key within 1 second will cause rate limiting (<code>429</code>) errors to be thrown.</p>
<p>You should not write more than once per second to the same key. Consider consolidating your writes to a key within a Worker invocation to a single write, or wait at least 1 second between writes.</p>
<p>The following example serves as a demonstration of how multiple writes to the same key may return errors by forcing concurrent writes within a single Worker invocation. This is not a pattern that should be used in production.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9547.md")
</div></div>
<p>To handle these errors, we recommend implementing a retry logic, with exponential backoff. Here is a simple approach to add retries to the above code.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9550.md")
</div></div>
<h2 id="other-methods-to-access-kv">Other methods to access KV</h2>
<p>You can also <a href="/kv/reference/kv-commands/#kv-namespace-create">write key-value pairs from the command line with Wrangler</a> and <a href="/api/resources/kv/subresources/namespaces/subresources/values/methods/update/">write data via the REST API</a>.</p>
