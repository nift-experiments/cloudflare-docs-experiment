---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/vectorize/
  description: '2026-08-04'
  full_title: vectorize changelog | Cloudflare Docs
  head_html: <title>vectorize changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-08-04"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/vectorize/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="vectorize changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-08-04"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/vectorize/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/vectorize/#page","headline":"vectorize changelog | Cloudflare Docs","description":"2026-08-04","url":"https://developers.cloudflare.com/changelog/product/vectorize/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/vectorize/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="vectorize-indexes-now-support-up-to-20-million-vectors"><a href="/changelog/post/2026-08-04-index-capacity-20-million/">Vectorize indexes now support up to 20 million vectors</a></h2>
<p><em>2026-08-04</em></p>
<p>You can now store up to 20 million vectors in a single Vectorize index, doubling the previous limit of 10 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.</p>
<p>Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the <a href="/vectorize/platform/limits/">Vectorize limits documentation</a> for complete details.</p>


<h2 id="reduced-end-to-end-latency-for-vector-changes"><a href="/changelog/post/2026-06-30-improved-wal-throughput/">Reduced end-to-end latency for vector changes</a></h2>
<p><em>2026-07-01</em></p>
<p>We have greatly improved the throughput of the Vectorize <a href="https://blog.cloudflare.com/building-vectorize-a-distributed-vector-database-on-cloudflare-developer-platform/#the-wal">write-ahead log (WAL)</a>. As a result, we have significantly reduced the end-to-end latency for a vector change to become queryable: median latency has dropped from 2 minutes to under 30 seconds, and p99 latency from 5 minutes to under 2 minutes.</p>
<p><img src="/assets/upstream/images/vectorize/vectorize-p99-wal-batch-end-to-end-latency-improvement.png" alt="Vectorize p99 WAL batch end-to-end latency improved" /></p>
<p>This means inserts, upserts, and deletes are reflected in query results faster, improving the freshness of semantic search, recommendation, and retrieval-augmented generation (RAG) workloads. You do not need to change your code or configuration to benefit from this improvement.</p>
<p>For more information, refer to the <a href="/vectorize/">Vectorize documentation</a>.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="return-up-to-50-query-results-with-values-or-metadata"><a href="/changelog/post/2026-03-16-topk-limit-increased-to-50/">Return up to 50 query results with values or metadata</a></h2>
<p><em>2026-03-16</em></p>
<p>You can now set <code>topK</code> up to <code>50</code> when a Vectorize query returns values or full metadata. This raises the previous limit of <code>20</code> for queries that use <code>returnValues: true</code> or <code>returnMetadata: &quot;all&quot;</code>.</p>
<p>Use the higher limit when you need more matches in a single query response without dropping values or metadata. Refer to the <a href="/vectorize/reference/client-api/">Vectorize API reference</a> for query options and current <code>topK</code> limits.</p>


<h2 id="vectorize-indexes-now-support-up-to-10-million-vectors"><a href="/changelog/post/2026-01-23-increased-index-capacity/">Vectorize indexes now support up to 10 million vectors</a></h2>
<p><em>2026-01-23</em></p>
<p>You can now store up to 10 million vectors in a single Vectorize index, doubling the previous limit of 5 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.</p>
<p>Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the <a href="/vectorize/platform/limits/">Vectorize limits documentation</a> for complete details.</p>


<h2 id="list-all-vectors-in-a-vectorize-index-with-the-new-list-vectors-operation"><a href="/changelog/post/2025-08-26-vectorize-list-vectors/">List all vectors in a Vectorize index with the new list-vectors operation</a></h2>
<p><em>2025-08-26</em></p>
<p>You can now list all vector identifiers in a Vectorize index using the new <code>list-vectors</code> operation. This enables bulk operations, auditing, and data migration workflows through paginated requests that maintain snapshot consistency.</p>
<p>The operation is available via Wrangler CLI and REST API. Refer to the <a href="/vectorize/best-practices/list-vectors/">list-vectors best practices guide</a> for detailed usage guidance.</p>


<h2 id="create-fully-managed-rag-pipelines-for-your-ai-applications-with-autorag"><a href="/changelog/post/2025-04-07-autorag-open-beta/">Create fully-managed RAG pipelines for your AI applications with AutoRAG</a></h2>
<p><em>2025-04-07</em></p>
<p><a href="/ai-search/">AutoRAG</a> is now in open beta, making it easy for you to build fully-managed retrieval-augmented generation (RAG) pipelines without managing infrastructure. Just upload your docs to <a href="/r2/get-started/">R2</a>, and AutoRAG handles the rest: embeddings, indexing, retrieval, and response generation via API.</p>
<p>With AutoRAG, you can:</p>
<ul>
<li><strong>Customize your pipeline:</strong> Choose from <a href="/workers-ai">Workers AI</a> models, configure chunking strategies, edit system prompts, and more.</li>
<li><strong>Instant setup:</strong> AutoRAG provisions everything you need from <a href="/vectorize">Vectorize</a>, <a href="/ai-gateway">AI gateway</a>, to pipeline logic for you, so you can go from zero to a working RAG pipeline in seconds.</li>
<li><strong>Keep your index fresh:</strong> AutoRAG continuously syncs your index with your data source to ensure responses stay accurate and up to date.</li>
<li><strong>Ask questions:</strong> Query your data and receive grounded responses via a <a href="/ai-search/api/search/workers-binding/">Workers binding</a> or <a href="/ai-search/api/search/rest-api/">API</a>.</li>
</ul>
<p>Whether you're building internal tools, AI-powered search, or a support assistant, AutoRAG gets you from idea to deployment in minutes.</p>
<p>Get started in the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a> or check out the <a href="/ai-search/get-started/">guide</a> for instructions on how to build your RAG pipeline today.</p>



