---
cp9:
  canonical: https://developers.cloudflare.com/kv/api/delete-key-value-pairs/
  description: Remove keys and their associated values from a Workers KV namespace using the delete() method.
  full_title: Delete key-value pairs · Cloudflare Workers KV docs
  head_html: <title>Delete key-value pairs · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Remove keys and their associated values from a Workers KV namespace using the delete() method."><link rel="canonical" href="https://developers.cloudflare.com/kv/api/delete-key-value-pairs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/api/delete-key-value-pairs/index.md"><meta property="og:title" content="Delete key-value pairs · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Remove keys and their associated values from a Workers KV namespace using the delete() method."><meta property="og:url" content="https://developers.cloudflare.com/kv/api/delete-key-value-pairs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/api/delete-key-value-pairs/#page","headline":"Delete key-value pairs \u00b7 Cloudflare Workers KV docs","description":"Remove keys and their associated values from a Workers KV namespace using the delete() method.","url":"https://developers.cloudflare.com/kv/api/delete-key-value-pairs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/api/delete-key-value-pairs/
  schema: 1
---
<p>To delete a key-value pair, call the <code>delete()</code> method of the <a href="/kv/concepts/kv-bindings/">KV binding</a> on any <a href="/kv/concepts/kv-namespaces/">KV namespace</a> you have bound to your Worker code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9596.md")
</div></div>
<h4 id="example">Example</h4>
<p>An example of deleting a key-value pair from within a Worker:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9599.md")
</div></div>
<h2 id="reference">Reference</h2>
<p>The following method is provided to delete from KV:</p>
<ul>
<li><a href="#delete-method">delete()</a></li>
</ul>
<h3 id="delete-method"><code>delete()</code> method</h3>
<p>To delete a key-value pair, call the <code>delete()</code> method of the <a href="/kv/concepts/kv-bindings/">KV binding</a> on any KV namespace you have bound to your Worker code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9602.md")
</div></div>
<h4 id="parameters">Parameters</h4>
<ul>
<li><code>key</code>: <code>string</code>
<ul>
<li>The key to associate with the value.</li>
</ul>
</li>
</ul>
<h4 id="response">Response</h4>
<ul>
<li><code>response</code>: <code>Promise&lt;void&gt;</code>
<ul>
<li>A <code>Promise</code> that resolves if the delete is successful.</li>
</ul>
</li>
</ul>
<p>This method returns a promise that you should <code>await</code> on to verify successful deletion. Calling <code>delete()</code> on a non-existing key is returned as a successful delete.</p>
<p>Calling the <code>delete()</code> method will remove the key and value from your KV namespace. As with any operations, it may take some time for the key to be deleted from various points in the Cloudflare global network.</p>
<h2 id="guidance">Guidance</h2>
<h3 id="delete-data-in-bulk">Delete data in bulk</h3>
<p>Delete more than one key-value pair at a time with Wrangler or <a href="/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_delete/">via the REST API</a>.</p>
<p>The bulk REST API can accept up to 10,000 KV pairs at once. Bulk writes are not supported using the <a href="/kv/concepts/kv-bindings/">KV binding</a>.</p>
<h2 id="other-methods-to-access-kv">Other methods to access KV</h2>
<p>You can also <a href="/kv/reference/kv-commands/#kv-namespace-delete">delete key-value pairs from the command line with Wrangler</a> or <a href="/api/resources/kv/subresources/namespaces/subresources/values/methods/delete/">with the REST API</a>.</p>
