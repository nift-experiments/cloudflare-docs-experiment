---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/
  description: Combine vector and keyword search in AI Search for broader, more accurate retrieval results.
  full_title: Hybrid search · Cloudflare AI Search docs
  head_html: <title>Hybrid search · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Combine vector and keyword search in AI Search for broader, more accurate retrieval results."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/index.md"><meta property="og:title" content="Hybrid search · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Combine vector and keyword search in AI Search for broader, more accurate retrieval results."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/#page","headline":"Hybrid search \u00b7 Cloudflare AI Search docs","description":"Combine vector and keyword search in AI Search for broader, more accurate retrieval results.","url":"https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/indexing/hybrid-search/
  schema: 1
---
<p>Hybrid search runs vector and keyword search in parallel and merges the results. It requires <a href="/ai-search/configuration/indexing/keyword-search/">keyword search</a> to be enabled. For an overview of search modes, refer to <a href="/ai-search/concepts/search-modes/">Search modes</a>.</p>
<h2 id="enable-hybrid-search">Enable hybrid search</h2>
<p>Set both <code>index_method.vector</code> and <code>index_method.keyword</code> to <code>true</code>:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;	index_method: {&#10;		vector: true,&#10;		keyword: true,&#10;	},&#10;	fusion_method: &quot;rrf&quot;,&#10;});&#10;</code></pre>
<p>To disable hybrid search, set <code>index_method.keyword</code> to <code>false</code>. The keyword index is deleted.</p>
<p>For each search method, you can configure the following to adjust retrieval behavior:</p>
<ul>
<li><strong>Vector search</strong>: Configure the <a href="/ai-search/configuration/models/">embedding model</a>.</li>
<li><strong>Keyword search</strong>: Configure the <a href="/ai-search/configuration/indexing/keyword-search/">tokenizer and match mode</a>.</li>
</ul>
<h2 id="fusion-method">Fusion method</h2>
<p>The <code>fusion_method</code> field controls how vector and keyword results are merged.</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rrf</code></td>
<td>Yes</td>
<td>Reciprocal Rank Fusion. Scores results based on rank position across both search methods. Recommended for most use cases.</td>
</tr>
<tr>
<td><code>max</code></td>
<td>No</td>
<td>Takes the higher of the normalized vector and keyword scores. Use when one search method is consistently more relevant.</td>
</tr>
</tbody>
</table>
<h2 id="reranking">Reranking</h2>
<p>After fusion, you can optionally apply reranking to further reorder results by semantic relevance. Reranking uses a cross-encoder model that evaluates the query and each chunk together, which can improve precision beyond what fusion alone provides.</p>
<p>Reranking is disabled by default. Refer to <a href="/ai-search/configuration/retrieval/reranking/">Reranking</a> to enable and configure it.</p>
<h2 id="per-request-overrides">Per-request overrides</h2>
<p>Override search settings on individual requests using <code>ai_search_options.retrieval</code>.</p>
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
<td><code>retrieval_type</code></td>
<td><code>&quot;vector&quot;</code>, <code>&quot;keyword&quot;</code>, or <code>&quot;hybrid&quot;</code></td>
<td>Force a specific search mode. Must be compatible with <code>index_method</code>.</td>
</tr>
<tr>
<td><code>fusion_method</code></td>
<td><code>&quot;rrf&quot;</code> or <code>&quot;max&quot;</code></td>
<td>Override the fusion method.</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			retrieval_type: &quot;hybrid&quot;,&#10;			fusion_method: &quot;rrf&quot;,&#10;		},&#10;	},&#10;});&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3081.md")
</aside>
<h2 id="scoring-details">Scoring details</h2>
<p>When hybrid search is active, each chunk includes a <code>scoring_details</code> object:</p>
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
<td><code>keyword_score</code></td>
<td>number</td>
<td>Raw BM25 keyword score.</td>
</tr>
<tr>
<td><code>vector_rank</code></td>
<td>number</td>
<td>Rank position in the vector result set.</td>
</tr>
<tr>
<td><code>keyword_rank</code></td>
<td>number</td>
<td>Rank position in the keyword result set.</td>
</tr>
<tr>
<td><code>fusion_method</code></td>
<td>string</td>
<td>Fusion method used (<code>rrf</code> or <code>max</code>).</td>
</tr>
<tr>
<td><code>reranking_score</code></td>
<td>number</td>
<td>Score from the reranking model, if enabled.</td>
</tr>
</tbody>
</table>
<h2 id="limits">Limits</h2>
<p>Instances with keyword search enabled support up to 500,000 files per instance on the Workers Paid tier, compared to 1,000,000 for vector-only instances. Refer to <a href="/ai-search/platform/limits-pricing/">Limits and pricing</a> for the full list of limits.</p>
