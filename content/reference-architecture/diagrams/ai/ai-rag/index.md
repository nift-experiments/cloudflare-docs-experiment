---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-rag/
  description: RAG combines retrieval with generative models for better text. It uses external knowledge to create factual, relevant responses, improving coherence and accuracy in NLP tasks like chatbots.
  full_title: Retrieval Augmented Generation (RAG) · Cloudflare Reference Architecture docs
  head_html: <title>Retrieval Augmented Generation (RAG) · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="RAG combines retrieval with generative models for better text. It uses external knowledge to create factual, relevant responses, improving coherence and accuracy in NLP tasks like chatbots."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-rag/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-rag/index.md"><meta property="og:title" content="Retrieval Augmented Generation (RAG) · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="RAG combines retrieval with generative models for better text. It uses external knowledge to create factual, relevant responses, improving coherence and accuracy in NLP tasks like chatbots."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-rag/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture diagram"><meta name="algolia_content_type" content="Reference architecture diagram"><meta name="pcx_additional_products" content="AI Search,D1,Queues,Vectorize,Workers,Workers AI"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-rag/#page","headline":"Retrieval Augmented Generation (RAG) \u00b7 Cloudflare Reference Architecture docs","description":"RAG combines retrieval with generative models for better text. It uses external knowledge to create factual, relevant responses, improving coherence and accuracy in NLP tasks like chatbots.","url":"https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-rag/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/diagrams/ai/ai-rag/
  schema: 1
---
<p>Retrieval-Augmented Generation (RAG) is an innovative approach in natural language processing that integrates retrieval mechanisms with generative models to enhance text generation.</p>
<p>By incorporating external knowledge from pre-existing sources, RAG addresses the challenge of generating contextually relevant and informative text. This integration enables RAG to overcome the limitations of traditional generative models by ensuring that the generated text is grounded in factual information and context. RAG aims to solve the problem of information overload by efficiently retrieving and incorporating only the most relevant information into the generated text, leading to improved coherence and accuracy. Overall, RAG represents a significant advancement in NLP, offering a more robust and contextually aware approach to text generation.</p>
<p>Examples for application of these technique includes for instance customer service chat bots that use a knowledge base to answer support requests.</p>
<p>In the context of Retrieval-Augmented Generation (RAG), knowledge seeding involves incorporating external information from pre-existing sources into the generative process, while querying refers to the mechanism of retrieving relevant knowledge from these sources to inform the generation of coherent and contextually accurate text. Both are shown below.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-a-managed-option">Looking for a managed option?</h3>
@markup("md", "content/.markup/bodies/12730.md")
</aside>
<h2 id="knowledge-seeding">Knowledge Seeding</h2>
<p><img src="/assets/upstream/images/reference-architecture/rag-ref-architecture-diagrams/rag-architecture-seeding.svg" alt="Figure 1: Knowledge seeding" title="Figure 1: Knowledge seeding" /></p>
<ol>
<li><strong>Client upload</strong>: Send POST request with documents to API endpoint.</li>
<li><strong>Input processing</strong>: Process incoming request using <a href="/workers/">Workers</a> and send messages to <a href="/queues/">Queues</a> to add processing backlog.</li>
<li><strong>Batch processing</strong>: Use <a href="/queues/">Queues</a> to trigger a <a href="/queues/reference/how-queues-works/#consumers">consumer</a> that process input documents in batches to prevent downstream overload.</li>
<li><strong>Embedding generation</strong>: Generate embedding vectors by calling <a href="/workers-ai/">Workers AI</a> <a href="/workers-ai/models/">text embedding models</a> for the documents.</li>
<li><strong>Vector storage</strong>: Insert the embedding vectors to <a href="/vectorize/">Vectorize</a>.</li>
<li><strong>Document storage</strong>: Insert documents to <a href="/d1/">D1</a> for persistent storage.</li>
<li><strong>Ack/Retry mechanism</strong>: Signal success/error by using the <a href="/queues/configuration/javascript-apis/#message">Queues Runtime API</a> in the consumer for each document. <a href="/queues/">Queues</a> will schedule retries, if needed.</li>
</ol>
<h2 id="knowledge-queries">Knowledge Queries</h2>
<p><img src="/assets/upstream/images/reference-architecture/rag-ref-architecture-diagrams/rag-architecture-query.svg" alt="Figure 2: Knowledge queries" title="Figure 2: Knowledge queries" /></p>
<ol>
<li><strong>Client query</strong>: Send GET request with query to API endpoint.</li>
<li><strong>Embedding generation</strong>: Generate embedding vectors by calling <a href="/workers-ai/">Workers AI</a> <a href="/workers-ai/models/">text embedding models</a> for the incoming query.</li>
<li><strong>Vector search</strong>: Query <a href="/vectorize/">Vectorize</a> using the vector representation of the query to retrieve related vectors.</li>
<li><strong>Document lookup</strong>: Retrieve related documents from <a href="/d1/">D1</a> based on search results from <a href="/vectorize/">Vectorize</a>.</li>
<li><strong>Text generation</strong>: Pass both the original query and the retrieved documents as context to <a href="/workers-ai/">Workers AI</a> <a href="/workers-ai/models/">text generation models</a> to generate a response.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers-ai/guides/tutorials/build-a-retrieval-augmented-generation-ai/">Tutorial: Build a RAG AI</a></li>
<li><a href="/ai-search/get-started/">Get started with AI Search</a></li>
<li><a href="/workers-ai/models/">Workers AI: Text embedding models</a></li>
<li><a href="/workers-ai/models/">Workers AI: Text generation models</a></li>
</ul>
