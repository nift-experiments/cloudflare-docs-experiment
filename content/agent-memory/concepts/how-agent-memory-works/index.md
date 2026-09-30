---
cp9:
  canonical: https://developers.cloudflare.com/agent-memory/concepts/how-agent-memory-works/
  description: A high-level overview of how Agent Memory extracts, stores, and retrieves knowledge from conversations.
  full_title: How Agent Memory works · Cloudflare Agent Memory docs
  head_html: <title>How Agent Memory works · Cloudflare Agent Memory docs</title><meta name="generator" content="Nift"><meta name="description" content="A high-level overview of how Agent Memory extracts, stores, and retrieves knowledge from conversations."><link rel="canonical" href="https://developers.cloudflare.com/agent-memory/concepts/how-agent-memory-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agent-memory/concepts/how-agent-memory-works/index.md"><meta property="og:title" content="How Agent Memory works · Cloudflare Agent Memory docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A high-level overview of how Agent Memory extracts, stores, and retrieves knowledge from conversations."><meta property="og:url" content="https://developers.cloudflare.com/agent-memory/concepts/how-agent-memory-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agent Memory"><meta name="algolia_product_filter" content="Agent Memory"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agent Memory"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agent-memory/concepts/how-agent-memory-works/#page","headline":"How Agent Memory works \u00b7 Cloudflare Agent Memory docs","description":"A high-level overview of how Agent Memory extracts, stores, and retrieves knowledge from conversations.","url":"https://developers.cloudflare.com/agent-memory/concepts/how-agent-memory-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agent-memory/concepts/how-agent-memory-works/
  schema: 1
---
<p>Agent Memory is a managed service that gives your applications persistent, AI-powered memory. It automatically turns raw conversations into structured knowledge and retrieves the right context when you need it.</p>
<h2 id="memory-types">Memory types</h2>
<p>Agent Memory classifies every extracted memory into one of four types:</p>
<ul>
<li><strong>Facts</strong> — Stable knowledge about a person, project, or tool. Preferences, identities, relationships, and goals. Facts evolve over time through supersession: when a newer fact replaces an older one on the same topic, the old version is preserved but the latest surfaces in recall results.</li>
<li><strong>Events</strong> — Completed actions anchored to a point in time. Deployments, decisions, milestones, and observations. Events accumulate and do not conflict with each other.</li>
<li><strong>Instructions</strong> — Reusable procedures, workflows, and conventions. Like facts, instructions support supersession when updated.</li>
<li><strong>Tasks</strong> — Short-lived, session-scoped items such as active investigations and follow-ups. Tasks are deprioritized after the session ends.</li>
</ul>
<h2 id="how-ingestion-works">How ingestion works</h2>
<p>When you call <code>ingest()</code>, Agent Memory processes the conversation through several stages:</p>
<ol>
<li>
<p><strong>Extraction</strong> — AI reads the conversation and identifies discrete, memorable items. Each item is a standalone piece of knowledge with a clear summary and supporting content.</p>
</li>
<li>
<p><strong>Classification</strong> — Each extracted item is classified into a memory type (fact, event, instruction, or task) and assigned a topic key, keywords, and search queries for later retrieval.</p>
</li>
<li>
<p><strong>Deduplication</strong> — The system checks for duplicates against both the current batch and existing stored memories. Facts and instructions with the same topic key supersede older versions rather than creating duplicates.</p>
</li>
<li>
<p><strong>Storage</strong> — Memories are written to durable storage with full-text search indexes. Non-task memories are also embedded as vectors for semantic search.</p>
</li>
</ol>
<p>Raw conversation messages are always stored verbatim alongside extracted memories, preserving the original transcript for full-text search.</p>
<h2 id="how-recall-works">How recall works</h2>
<p>When you call <code>recall()</code>, Agent Memory runs multiple retrieval strategies in parallel:</p>
<ol>
<li>
<p><strong>Query analysis</strong> — AI analyzes your query to determine the best retrieval approach, generating keyword terms, topic keys, and semantic search vectors.</p>
</li>
<li>
<p><strong>Parallel retrieval</strong> — The system simultaneously searches across keyword indexes, topic key lookups, semantic vector indexes, and raw conversation messages.</p>
</li>
<li>
<p><strong>Scoring and ranking</strong> — Results from all sources are combined and ranked to surface the most relevant memories while maintaining diversity across retrieval methods.</p>
</li>
<li>
<p><strong>Synthesis</strong> — AI generates a natural language answer from the top-ranked memories, grounded in the actual stored content.</p>
</li>
</ol>
<p>If no memories match the query, <code>recall()</code> returns an empty answer rather than hallucinating a response.</p>
<h2 id="idempotency-and-deduplication">Idempotency and deduplication</h2>
<p>Agent Memory is designed for safe re-ingestion:</p>
<ul>
<li>
<p><strong>Messages are content-addressed.</strong> Each message gets a deterministic ID derived from its content and session. Sending the same message twice does not create a duplicate.</p>
</li>
<li>
<p><strong>Sessions are deterministic.</strong> If you do not provide a <code>sessionId</code>, one is derived from the message content. The same conversation always maps to the same session.</p>
</li>
<li>
<p><strong>Facts and instructions evolve.</strong> When a new memory shares a topic key with an existing one (for example, &quot;editor preference&quot;), the old memory is marked as superseded. The latest version surfaces in recall results, but the full history is preserved.</p>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-profiles-and-namespaces-agent-memory-concepts-namespaces-profiles"><a href="/agent-memory/concepts/namespaces-profiles/">Profiles and namespaces</a></h3><p>Understand the isolation model for memory storage.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-workers-api-agent-memory-api-workers-api"><a href="/agent-memory/api/workers-api/">Workers API</a></h3><p>Configure bindings and use profiles from Worker code.</p></div>
