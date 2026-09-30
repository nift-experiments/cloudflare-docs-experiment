---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/
  description: Enable BM25 keyword search in AI Search to match documents containing exact query terms.
  full_title: Keyword search · Cloudflare AI Search docs
  head_html: <title>Keyword search · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable BM25 keyword search in AI Search to match documents containing exact query terms."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/index.md"><meta property="og:title" content="Keyword search · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable BM25 keyword search in AI Search to match documents containing exact query terms."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/#page","headline":"Keyword search \u00b7 Cloudflare AI Search docs","description":"Enable BM25 keyword search in AI Search to match documents containing exact query terms.","url":"https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/indexing/keyword-search/
  schema: 1
---
<p>Enable keyword search to match chunks that contain your query terms exactly. For an overview of search modes, refer to <a href="/ai-search/concepts/search-modes/">Search modes</a>.</p>
<h2 id="enable-keyword-search">Enable keyword search</h2>
<p>Set <code>index_method.keyword</code> to <code>true</code> when creating or updating an instance. You can use keyword search on its own or alongside vector search for <a href="/ai-search/configuration/indexing/hybrid-search/">hybrid search</a>.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>vector</code></td>
<td>boolean</td>
<td><code>true</code></td>
<td>Enable vector (semantic) search.</td>
</tr>
<tr>
<td><code>keyword</code></td>
<td>boolean</td>
<td><code>false</code></td>
<td>Enable keyword (BM25) search.</td>
</tr>
</tbody>
</table>
<p>At least one of <code>vector</code> or <code>keyword</code> must be <code>true</code>. Changing <code>index_method</code> triggers a full reindex of your content.</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;	index_method: {&#10;		vector: false,&#10;		keyword: true,&#10;	},&#10;});&#10;</code></pre>
<h2 id="keyword-tokenizer">Keyword tokenizer</h2>
<p>The <code>keyword_tokenizer</code> field (inside <code>indexing_options</code>) controls how text is split into tokens. Changing this triggers a full reindex.</p>
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
<td><code>porter</code></td>
<td>Yes</td>
<td>Applies Porter stemming. &quot;running&quot; matches &quot;run.&quot; Best for natural language.</td>
</tr>
<tr>
<td><code>trigram</code></td>
<td>No</td>
<td>Overlapping 3-character windows. &quot;config&quot; matches &quot;configuration.&quot; Best for code.</td>
</tr>
</tbody>
</table>
<h2 id="keyword-match-mode">Keyword match mode</h2>
<p>The <code>keyword_match_mode</code> field (inside <code>retrieval_options</code>) controls how multiple query terms are combined.</p>
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
<td><code>and</code></td>
<td>Yes</td>
<td>All query terms must appear. Higher precision, fewer results.</td>
</tr>
<tr>
<td><code>or</code></td>
<td>No</td>
<td>Any query term can match. Higher recall, more results.</td>
</tr>
</tbody>
</table>
<p>You can override <code>keyword_match_mode</code> per request:</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			keyword_match_mode: &quot;or&quot;,&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h2 id="limits">Limits</h2>
<p>Instances with keyword search enabled support up to 500,000 files per instance on the Workers Paid tier, compared to 1,000,000 for vector-only instances. Refer to <a href="/ai-search/platform/limits-pricing/">Limits and pricing</a> for the full list of limits.</p>
