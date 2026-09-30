---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/retrieval/query-rewriting/
  description: Improve AI Search retrieval quality by enabling query rewriting to rephrase user queries.
  full_title: Query rewriting · Cloudflare AI Search docs
  head_html: <title>Query rewriting · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Improve AI Search retrieval quality by enabling query rewriting to rephrase user queries."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/retrieval/query-rewriting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/retrieval/query-rewriting/index.md"><meta property="og:title" content="Query rewriting · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Improve AI Search retrieval quality by enabling query rewriting to rephrase user queries."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/retrieval/query-rewriting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/retrieval/query-rewriting/#page","headline":"Query rewriting \u00b7 Cloudflare AI Search docs","description":"Improve AI Search retrieval quality by enabling query rewriting to rephrase user queries.","url":"https://developers.cloudflare.com/ai-search/configuration/retrieval/query-rewriting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/retrieval/query-rewriting/
  schema: 1
---
<p>Query rewriting is an optional step in the AI Search pipeline that improves retrieval quality for follow-up queries. It applies to both <a href="/ai-search/api/search/workers-binding/#search">Search</a> and <a href="/ai-search/api/search/workers-binding/#chatcompletions">Chat Completions</a> requests.</p>
<h2 id="why-use-query-rewriting">Why use query rewriting?</h2>
<p>The wording of a user's question may not match how your documents are written. Query rewriting helps bridge this gap by:</p>
<ul>
<li>Rephrasing informal or vague queries into precise, information-dense terms</li>
<li>Adding synonyms or related keywords</li>
<li>Removing filler words or irrelevant details</li>
<li>Resolving follow-up queries that reference previous messages (for example, &quot;tell me more about that&quot; becomes a specific query based on conversation history)</li>
</ul>
<p>This leads to more relevant search matches, which improves the accuracy of results and generated responses.</p>
<h2 id="how-it-works">How it works</h2>
<p>Query rewriting requires the <code>messages</code> format and does not apply when using the <code>query</code> format. The first message is always used as-is. For follow-up queries, AI Search sends the conversation history, the latest user message, and the <a href="/ai-search/configuration/retrieval/system-prompt/">query rewrite system prompt</a> to the configured LLM. The rewritten query is then embedded and used to perform the search.</p>
<h2 id="example">Example</h2>
<p><strong>First message:</strong> <code>What is Cloudflare Workers?</code>
(used as-is, no rewriting)</p>
<p><strong>Follow-up message:</strong> <code>How do I deploy one?</code>
<strong>Rewritten query:</strong> <code>deploy Cloudflare Worker getting started</code></p>
<p>The follow-up &quot;How do I deploy one?&quot; is vague on its own. Query rewriting uses the conversation context to understand &quot;one&quot; refers to a Cloudflare Worker. How the query is rewritten depends on your <a href="/ai-search/configuration/retrieval/system-prompt/#query-rewriting-system-prompt">query rewrite system prompt</a>.</p>
<h2 id="considerations">Considerations</h2>
<p>Enabling query rewriting adds an extra LLM call to the query pipeline, which may increase latency.</p>
