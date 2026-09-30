---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/indexing/vector-search/
  description: Configure vector search in AI Search to find semantically similar content using embeddings.
  full_title: Vector search · Cloudflare AI Search docs
  head_html: <title>Vector search · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure vector search in AI Search to find semantically similar content using embeddings."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/indexing/vector-search/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/indexing/vector-search/index.md"><meta property="og:title" content="Vector search · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure vector search in AI Search to find semantically similar content using embeddings."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/indexing/vector-search/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/indexing/vector-search/#page","headline":"Vector search \u00b7 Cloudflare AI Search docs","description":"Configure vector search in AI Search to find semantically similar content using embeddings.","url":"https://developers.cloudflare.com/ai-search/configuration/indexing/vector-search/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/indexing/vector-search/
  schema: 1
---
<p>Vector search converts your query into a vector embedding and finds chunks with similar meaning. It is enabled by default on all AI Search instances. For an overview of search modes, refer to <a href="/ai-search/concepts/search-modes/">Search modes</a>.</p>
<h2 id="built-in-vector-index">Built-in vector index</h2>
<p>AI Search instances include a built-in vector index powered by <a href="/vectorize/">Vectorize</a>. The vector index stores embeddings generated from your content and is created and maintained automatically. You do not need to create or manage a Vectorize index yourself.</p>
<h2 id="embedding-model">Embedding model</h2>
<p>The <a href="/ai-search/configuration/models/">embedding model</a> determines the vector dimensions for the vector index. The embedding model is set when creating an instance and cannot be changed after creation.</p>
<h2 id="disable-vector-search">Disable vector search</h2>
<p>Vector search is the default index method for all instances. To switch to <a href="/ai-search/configuration/indexing/keyword-search/">keyword search</a> only, set <code>index_method.vector</code> to <code>false</code>. At least one of <code>vector</code> or <code>keyword</code> must be <code>true</code>.</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;	index_method: {&#10;		vector: false,&#10;		keyword: true,&#10;	},&#10;});&#10;</code></pre>
<h2 id="per-request-overrides">Per-request overrides</h2>
<p>You can force vector-only search on a per-request basis using <code>ai_search_options.retrieval.retrieval_type</code>, even if keyword search is also enabled on the instance.</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			retrieval_type: &quot;vector&quot;,&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h2 id="scoring-details">Scoring details</h2>
<p>When using vector search, each chunk includes a <code>scoring_details</code> object:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>vector_score</code></td>
<td>number</td>
<td>Vector similarity score (0 to 1).</td>
</tr>
<tr>
<td><code>vector_rank</code></td>
<td>number</td>
<td>Rank position in the result set.</td>
</tr>
</tbody>
</table>
<h2 id="limits">Limits</h2>
<p>For vector index limits, refer to <a href="/ai-search/platform/limits-pricing/">Limits and pricing</a>.</p>
