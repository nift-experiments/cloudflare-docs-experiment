---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/
  description: Customize how your AI Search instance indexes data, retrieves results, and generates responses.
  full_title: Configuration · Cloudflare AI Search docs
  head_html: <title>Configuration · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize how your AI Search instance indexes data, retrieves results, and generates responses."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/index.md"><meta property="og:title" content="Configuration · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize how your AI Search instance indexes data, retrieves results, and generates responses."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/ai-search/configuration/#page","headline":"Configuration \u00b7 Cloudflare AI Search docs","description":"Customize how your AI Search instance indexes data, retrieves results, and generates responses.","url":"https://developers.cloudflare.com/ai-search/configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/
  schema: 1
---
<p>You can customize how your AI Search instance indexes your data, retrieves results, and generates responses. Some settings can be updated after the instance is created, while others are fixed at creation time.</p>
<h2 id="data-source">Data source</h2>
<table>
<thead>
<tr>
<th>Configuration</th>
<th>Editable after creation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ai-search/configuration/data-source/built-in-storage/">Built-in storage</a></td>
<td>n/a</td>
<td>Upload files directly to an instance</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/">Website</a></td>
<td>no</td>
<td>Connect a domain you own to index website pages</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/r2/">R2 Bucket</a></td>
<td>no</td>
<td>Connect a Cloudflare R2 bucket to index stored documents</td>
</tr>
</tbody>
</table>
<h2 id="indexing">Indexing</h2>
<table>
<thead>
<tr>
<th>Configuration</th>
<th>Editable after creation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ai-search/configuration/indexing/vector-search/">Vector search</a></td>
<td>yes</td>
<td>Vector search and the built-in vector index</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/path-filtering/">Path filtering</a></td>
<td>yes</td>
<td>Include or exclude specific paths from indexing</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/chunking/">Chunking</a></td>
<td>yes</td>
<td>Number of tokens per chunk and overlap between chunks</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/syncing/">Syncing</a></td>
<td>yes</td>
<td>Sync jobs and indexing controls</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/keyword-search/">Keyword search</a></td>
<td>yes</td>
<td>Enable keyword (BM25) search for exact term matching</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/hybrid-search/">Hybrid search</a></td>
<td>yes</td>
<td>Combine vector and keyword search with configurable fusion</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/metadata/">Metadata attributes</a></td>
<td>yes</td>
<td>Define built-in and custom metadata fields</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/service-api-token/">Service API token</a></td>
<td>yes</td>
<td>API token that grants AI Search permission to access R2 buckets</td>
</tr>
</tbody>
</table>
<h2 id="retrieval">Retrieval</h2>
<table>
<thead>
<tr>
<th>Configuration</th>
<th>Editable after creation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ai-search/configuration/retrieval/result-controls/">Result controls</a></td>
<td>yes</td>
<td>Match threshold and maximum number of results</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/filtering/">Filtering</a></td>
<td>yes</td>
<td>Filter results by metadata attributes</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/boosting/">Relevance boosting</a></td>
<td>yes</td>
<td>Bias results by metadata characteristics</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/reranking/">Reranking</a></td>
<td>yes</td>
<td>Reorder results by semantic relevance using a reranking model</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/query-rewriting/">Query rewriting</a></td>
<td>yes</td>
<td>Rewrite follow-up queries using conversation context</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/system-prompt/">System prompt</a></td>
<td>yes</td>
<td>Guide query rewriting and response generation behavior</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/cache/">Similarity caching</a></td>
<td>yes</td>
<td>Cache responses for similar prompts</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint</a></td>
<td>yes</td>
<td>Enable public access to search, chat, and MCP endpoints</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">Custom domains</a></td>
<td>yes</td>
<td>Serve a public endpoint from a hostname that you own</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a></td>
<td>yes</td>
<td>Require callers to authenticate before they can search</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">Namespace public endpoints</a></td>
<td>yes</td>
<td>Search across several instances from a single public endpoint</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippets</a></td>
<td>yes</td>
<td>Embed pre-built search and chat components in your website</td>
</tr>
</tbody>
</table>
<h2 id="models">Models</h2>
<table>
<thead>
<tr>
<th>Configuration</th>
<th>Editable after creation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ai-search/configuration/models/">Embedding model</a></td>
<td>no</td>
<td>Model used to generate vector embeddings</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/models/">Generation model</a></td>
<td>yes</td>
<td>Model used to generate the final response</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/models/">Query rewriting model</a></td>
<td>yes</td>
<td>Model used for query rewriting</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/models/">Reranking model</a></td>
<td>yes</td>
<td>Model used to reorder results by semantic relevance</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/models/ai-gateway/">AI Gateway</a></td>
<td>yes</td>
<td>Observe and control the model calls AI Search makes</td>
</tr>
</tbody>
</table>
