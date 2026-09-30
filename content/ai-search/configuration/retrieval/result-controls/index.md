---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/retrieval/result-controls/
  description: Control AI Search result count and minimum score thresholds for returned results.
  full_title: Result controls · Cloudflare AI Search docs
  head_html: <title>Result controls · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Control AI Search result count and minimum score thresholds for returned results."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/retrieval/result-controls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/retrieval/result-controls/index.md"><meta property="og:title" content="Result controls · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control AI Search result count and minimum score thresholds for returned results."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/retrieval/result-controls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/retrieval/result-controls/#page","headline":"Result controls \u00b7 Cloudflare AI Search docs","description":"Control AI Search result count and minimum score thresholds for returned results.","url":"https://developers.cloudflare.com/ai-search/configuration/retrieval/result-controls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/retrieval/result-controls/
  schema: 1
---
<p>These settings control how many results are returned and the minimum score required. To filter results by metadata attributes like folder or category, refer to <a href="/ai-search/configuration/retrieval/filtering/">Filtering</a>.</p>
<h2 id="match-threshold">Match threshold</h2>
<p>The <code>match_threshold</code> sets the minimum vector similarity score that a chunk must meet to be included in the results. Threshold values range from <code>0</code> to <code>1</code>. The threshold filters on the vector similarity score, not the fused score returned in the response.</p>
<ul>
<li>A higher threshold means stricter filtering, returning only highly similar matches.</li>
<li>A lower threshold allows broader matches, increasing recall but possibly reducing precision.</li>
</ul>
<h2 id="maximum-number-of-results">Maximum number of results</h2>
<p>The <code>max_num_results</code> setting controls the number of top-matching chunks returned. The maximum allowed value is 50.</p>
<ul>
<li>Use a higher value if you want to synthesize across multiple documents. However, providing more input to the model can increase latency and cost.</li>
<li>Use a lower value if you prefer concise answers with minimal context.</li>
</ul>
<h2 id="how-they-work-together">How they work together</h2>
<ol>
<li>Your query is embedded using the configured embedding model.</li>
<li>The search index is queried. For <a href="/ai-search/configuration/indexing/hybrid-search/">hybrid search</a>, vector and keyword results are fused into a single ranked list.</li>
<li>Chunks with a vector similarity score below <code>match_threshold</code> are filtered out.</li>
<li>The filtered results are limited to <code>max_num_results</code> and passed into the generation step as context.</li>
</ol>
<p>If no results meet the threshold, AI Search will not generate a response.</p>
<p>If <a href="/ai-search/configuration/retrieval/reranking/">reranking</a> is enabled, a separate <code>reranking.match_threshold</code> can be configured to filter chunks by their reranking score.</p>
<h2 id="per-request-override">Per-request override</h2>
<p>These values can be configured at the instance level or overridden per request:</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			match_threshold: 0.5,&#10;			max_num_results: 10,&#10;		},&#10;	},&#10;});&#10;</code></pre>
