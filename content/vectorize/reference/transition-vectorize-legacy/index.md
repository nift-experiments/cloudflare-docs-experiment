---
cp9:
  canonical: https://developers.cloudflare.com/vectorize/reference/transition-vectorize-legacy/
  description: Migrate from legacy Vectorize V1 indexes to the current V2 format.
  full_title: Transition legacy Vectorize indexes · Cloudflare Vectorize docs
  head_html: <title>Transition legacy Vectorize indexes · Cloudflare Vectorize docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate from legacy Vectorize V1 indexes to the current V2 format."><link rel="canonical" href="https://developers.cloudflare.com/vectorize/reference/transition-vectorize-legacy/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/vectorize/reference/transition-vectorize-legacy/index.md"><meta property="og:title" content="Transition legacy Vectorize indexes · Cloudflare Vectorize docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate from legacy Vectorize V1 indexes to the current V2 format."><meta property="og:url" content="https://developers.cloudflare.com/vectorize/reference/transition-vectorize-legacy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Vectorize"><meta name="algolia_product_filter" content="Vectorize"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Vectorize"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/vectorize/reference/transition-vectorize-legacy/#page","headline":"Transition legacy Vectorize indexes \u00b7 Cloudflare Vectorize docs","description":"Migrate from legacy Vectorize V1 indexes to the current V2 format.","url":"https://developers.cloudflare.com/vectorize/reference/transition-vectorize-legacy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /vectorize/reference/transition-vectorize-legacy/
  schema: 1
---
<p>Legacy Vectorize (V1) indexes are on a deprecation path as of Aug 15, 2024. Your Vectorize index may be a legacy index if it fulfills any of the following crieria:</p>
<ol>
<li>Was created with a Wrangler version lower than <code>v3.71.0</code>.</li>
<li>Was created using the &quot;--deprecated-v1&quot; flag enabled.</li>
<li>Was created using the legacy REST API.</li>
</ol>
<p>This document provides details around any transition steps that may be needed to move away from legacy Vectorize indexes.</p>
<h2 id="why-should-i-transition">Why should I transition?</h2>
<p>Legacy Vectorize (V1) indexes are on a deprecation path. Support for these indexes would be limited and their usage is not recommended for any production workloads.</p>
<p>Furthermore, you will no longer be able to create legacy Vectorize indexes by December 2024. Other operations will be unaffected and will remain functional.</p>
<p>Additionally, the new Vectorize (V2) indexes can operate at a significantly larger scale (with a capacity for multi-million vectors), and provide faster performance. Please review the <a href="/vectorize/platform/limits/">Limits</a> page to understand the latest capabilities supported by Vectorize.</p>
<h2 id="notable-changes">Notable changes</h2>
<p>In addition to supporting significantly larger indexes with multi-million vectors, and faster performance, these are some of the changes that need to be considered when transitioning away from legacy Vectorize indexes:</p>
<ol>
<li>
<p>The new Vectorize (V2) indexes now support asynchronous mutations. Any vector inserts or deletes, and metadata index creation or deletes may take a few seconds to be reflected.</p>
</li>
<li>
<p>Vectorize (V2) support metadata and namespace filtering for much larger indexes with significantly lower latencies. However, the fields on which metadata filtering can be applied need to be specified before vectors are inserted. Refer to the <a href="/vectorize/reference/client-api/#create-metadata-index">metadata index creation</a> page for more details.</p>
</li>
<li>
<p>Vectorize (V2) <a href="/vectorize/reference/client-api/#query-vectors">query operation</a> now supports the ability to search for and return up to 100 most similar vectors.</p>
</li>
<li>
<p>Vectorize (V2) query operations provide a more granular control for querying metadata along with vectors. Refer to the <a href="/vectorize/reference/client-api/#query-vectors">query operation</a> page for more details.</p>
</li>
<li>
<p>Vectorize (V2) expands the Vectorize capabilities that are available via Wrangler (with Wrangler version &gt; <code>v3.71.0</code>).</p>
</li>
</ol>
<h2 id="transition">Transition</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="automated-migration">Automated Migration</h3>
@markup("md", "content/.markup/bodies/15251.md")
</aside>
<ol>
<li>
<p>Wrangler now supports operations on the new version of Vectorize (V2) indexes by default. To use Wrangler commands for legacy (V1) indexes, the <code>--deprecated-v1</code> flag must be enabled. Please note that this flag is only supported to create, get, list and delete indexes and to insert vectors.</p>
</li>
<li>
<p>Refer to the <a href="/api/resources/vectorize/subresources/indexes/methods/create/">REST API</a> page for details on the routes and payload types for the new Vectorize (V2) indexes.</p>
</li>
<li>
<p>To use the new version of Vectorize indexes in Workers, the environment binding must be defined as a <code>Vectorize</code> interface.</p>
</li>
</ol>
<pre tabindex="0"><code class="language-typescript">export interface Env {&#10;	// This makes your vector index methods available on env.VECTORIZE.*&#10;	// For example, env.VECTORIZE.insert() or query()&#10;	VECTORIZE: Vectorize;&#10;}&#10;</code></pre>
<p>The <code>Vectorize</code> interface includes the type changes and the capabilities supported by new Vectorize (V2) indexes.</p>
<p>For legacy Vectorize (V1) indexes, use the <code>VectorizeIndex</code> interface.</p>
<pre tabindex="0"><code class="language-typescript">export interface Env {&#10;	// This makes your vector index methods available on env.VECTORIZE.*&#10;	// For example, env.VECTORIZE.insert() or query()&#10;	VECTORIZE: VectorizeIndex;&#10;}&#10;</code></pre>
<ol start="4">
<li>
<p>With the new Vectorize (V2) version, the <code>returnMetadata</code> option for the <a href="/vectorize/reference/client-api/#query-vectors">query operation</a> now expects either <code>all</code>, <code>indexed</code> or <code>none</code> string values. For legacy Vectorize (V1), the <code>returnMetadata</code> option was a boolean field.</p>
</li>
<li>
<p>With the new Vectorize (V2) indexes, all index and vector mutations are asynchronous and return a <code>mutationId</code> in the response as a unique identifier for that mutation operation.</p>
<p>These mutation operations are: <a href="/vectorize/reference/client-api/#insert-vectors">Vector Inserts</a>, <a href="/vectorize/reference/client-api/#upsert-vectors">Vector Upserts</a>, <a href="/vectorize/reference/client-api/#delete-vectors-by-id">Vector Deletes</a>, <a href="/vectorize/reference/client-api/#create-metadata-index">Metadata Index Creation</a>, <a href="/vectorize/reference/client-api/#delete-metadata-index">Metadata Index Deletion</a>.</p>
<p>To check the identifier and the timestamp of the last mutation processed, use the Vectorize <a href="/vectorize/reference/client-api/#get-index-info">Info command</a>.</p>
</li>
</ol>
