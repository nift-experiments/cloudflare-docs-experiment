---
cp9:
  canonical: https://developers.cloudflare.com/kv/api/list-keys/
  description: Enumerate all keys in a Workers KV namespace using the list() method, with support for pagination and filtering by prefix.
  full_title: List keys · Cloudflare Workers KV docs
  head_html: <title>List keys · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Enumerate all keys in a Workers KV namespace using the list() method, with support for pagination and filtering by prefix."><link rel="canonical" href="https://developers.cloudflare.com/kv/api/list-keys/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/api/list-keys/index.md"><meta property="og:title" content="List keys · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enumerate all keys in a Workers KV namespace using the list() method, with support for pagination and filtering by prefix."><meta property="og:url" content="https://developers.cloudflare.com/kv/api/list-keys/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/api/list-keys/#page","headline":"List keys \u00b7 Cloudflare Workers KV docs","description":"Enumerate all keys in a Workers KV namespace using the list() method, with support for pagination and filtering by prefix.","url":"https://developers.cloudflare.com/kv/api/list-keys/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/api/list-keys/
  schema: 1
---
<p>To list all the keys in your KV namespace, call the <code>list()</code> method of the <a href="/kv/concepts/kv-bindings/">KV binding</a> on any <a href="/kv/concepts/kv-namespaces/">KV namespace</a> you have bound to your Worker code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9575.md")
</div></div>
<p>The <code>list()</code> method returns a promise you can <code>await</code> on to get the value.</p>
<h4 id="example">Example</h4>
<p>An example of listing keys from within a Worker:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9578.md")
</div></div>
<h2 id="reference">Reference</h2>
<p>The following method is provided to list the keys of KV:</p>
<ul>
<li><a href="#list-method">list()</a></li>
</ul>
<h3 id="list-method"><code>list()</code> method</h3>
<p>To list all the keys in your KV namespace, call the <code>list()</code> method of the <a href="/kv/concepts/kv-bindings/">KV binding</a> on any KV namespace you have bound to your Worker code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9581.md")
</div></div>
<h4 id="parameters">Parameters</h4>
* `options`: `{
  prefix?: string,
  limit?: string,
  cursor?: string
}`
  * An object with attributes `prefix` (optional), `limit` (optional), or `cursor` (optional).
    * `prefix` is a `string` that represents a prefix you can use to filter all keys.
    * `limit` is the maximum number of keys returned. The default is 1,000 keys, which is the maximum. It is unlikely that you will want to change this default but it is included for completeness.
    * `cursor` is a `string` used for paginating responses.
<h4 id="response">Response</h4>
* `response`: `Promise<{
  keys: {
    name: string,
    expiration?: number,
    metadata?: object
  }[],
  list_complete: boolean,
  cursor: string
}>`
  * A `Promise` that resolves to an object containing `keys`, `list_complete`, and `cursor` attributes.
    * `keys` is an array that contains an object for each key listed. Each object has attributes `name`, `expiration` (optional), and `metadata` (optional). If the key-value pair has an expiration set, the expiration will be present and in absolute value form (even if it was set in TTL form). If the key-value pair has non-null metadata set, the metadata will be present.
    * `list_complete` is a boolean, which will be `false` if there are more keys to fetch, even if the `keys` array is empty.
    * `cursor` is a `string` used for paginating responses.
<p>The <code>list()</code> method returns a promise which resolves with an object that looks like the following:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;keys&quot;: [&#10;    {&#10;      &quot;name&quot;: &quot;foo&quot;,&#10;      &quot;expiration&quot;: 1234,&#10;      &quot;metadata&quot;: { &quot;someMetadataKey&quot;: &quot;someMetadataValue&quot; }&#10;    }&#10;  ],&#10;  &quot;list_complete&quot;: false,&#10;  &quot;cursor&quot;: &quot;6Ck1la0VxJ0djhidm1MdX2FyD&quot;&#10;}&#10;</code></pre>
<p>The <code>keys</code> property will contain an array of objects describing each key. That object will have one to three keys of its own: the <code>name</code> of the key, and optionally the key's <code>expiration</code> and <code>metadata</code> values.</p>
<p>The <code>name</code> is a <code>string</code>, the <code>expiration</code> value is a number, and <code>metadata</code> is whatever type was set initially. The <code>expiration</code> value will only be returned if the key has an expiration and will be in the absolute value form, even if it was set in the TTL form. Any <code>metadata</code> will only be returned if the given key has non-null associated metadata.</p>
<p>If <code>list_complete</code> is <code>false</code>, there are more keys to fetch, even if the <code>keys</code> array is empty. You will use the <code>cursor</code> property to get more keys. Refer to <a href="#pagination">Pagination</a> for more details.</p>
<p>Consider storing your values in metadata if your values fit in the <a href="/kv/platform/limits/">metadata-size limit</a>. Storing values in metadata is more efficient than a <code>list()</code> followed by a <code>get()</code> per key. When using <code>put()</code>, leave the <code>value</code> parameter empty and instead include a property in the metadata object:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9584.md")
</div></div>
<p>Changes may take up to 60 seconds (or the value set with <code>cacheTtl</code> of the <code>get()</code> or <code>getWithMetadata()</code> method) to be reflected on the application calling the method on the KV namespace.</p>
<h2 id="guidance">Guidance</h2>
<h3 id="list-by-prefix">List by prefix</h3>
<p>List all the keys starting with a particular prefix.</p>
<p>For example, you may have structured your keys with a user, a user ID, and key names, separated by colons (such as <code>user:1:&lt;key&gt;</code>). You could get the keys for user number one by using the following code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9587.md")
</div></div>
<p>This will return all keys starting with the <code>&quot;user:1:&quot;</code> prefix.</p>
<h3 id="ordering">Ordering</h3>
<p>Keys are always returned in lexicographically sorted order according to their UTF-8 bytes.</p>
<h3 id="pagination">Pagination</h3>
<p>If there are more keys to fetch, the <code>list_complete</code> key will be set to <code>false</code> and a <code>cursor</code> will also be returned. In this case, you can call <code>list()</code> again with the <code>cursor</code> value to get the next batch of keys:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9590.md")
</div></div>
<p>Checking for an empty array in <code>keys</code> is not sufficient to determine whether there are more keys to fetch. Instead, use <code>list_complete</code>.</p>
<p>It is possible to have an empty array in <code>keys</code>, but still have more keys to fetch, because <a href="https://en.wikipedia.org/wiki/Tombstone_%28data_store%29">recently expired or deleted keys</a> must be iterated through but will not be included in the returned <code>keys</code>.</p>
<p>When de-paginating a large result set while also providing a <code>prefix</code> argument, the <code>prefix</code> argument must be provided in all subsequent calls along with the initial arguments.</p>
<h3 id="optimizing-storage-with-metadata-for-list-operations">Optimizing storage with metadata for <code>list()</code> operations</h3>
<p>Consider storing your values in metadata if your values fit in the <a href="/kv/platform/limits/">metadata-size limit</a>. Storing values in metadata is more efficient than a <code>list()</code> followed by a <code>get()</code> per key. When using <code>put()</code>, leave the <code>value</code> parameter empty and instead include a property in the metadata object:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9593.md")
</div></div>
<h2 id="other-methods-to-access-kv">Other methods to access KV</h2>
<p>You can also <a href="/kv/reference/kv-commands/#kv-namespace-list">list keys on the command line with Wrangler</a> or <a href="/api/resources/kv/subresources/namespaces/subresources/keys/methods/list/">with the REST API</a>.</p>
