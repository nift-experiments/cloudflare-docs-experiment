---
cp9:
  canonical: https://developers.cloudflare.com/agents/concepts/calling-llms/
  description: Call large language models from within a stateful Cloudflare Agent with persistent context and autonomous scheduling.
  full_title: Calling LLMs · Cloudflare Agents docs
  head_html: <title>Calling LLMs · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Call large language models from within a stateful Cloudflare Agent with persistent context and autonomous scheduling."><link rel="canonical" href="https://developers.cloudflare.com/agents/concepts/calling-llms/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/concepts/calling-llms/index.md"><meta property="og:title" content="Calling LLMs · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Call large language models from within a stateful Cloudflare Agent with persistent context and autonomous scheduling."><meta property="og:url" content="https://developers.cloudflare.com/agents/concepts/calling-llms/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/concepts/calling-llms/#page","headline":"Calling LLMs \u00b7 Cloudflare Agents docs","description":"Call large language models from within a stateful Cloudflare Agent with persistent context and autonomous scheduling.","url":"https://developers.cloudflare.com/agents/concepts/calling-llms/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /agents/concepts/calling-llms/
  schema: 1
---
<p>Agents change how you work with LLMs. In a stateless Worker, every request starts from scratch — you reconstruct context, call a model, return the response, and forget everything. An Agent keeps state between calls, stays connected to clients over WebSocket, and can call models on its own schedule without a user present.</p>
<p>This page covers the patterns that become possible when your LLM calls happen inside a stateful Agent. For provider setup and code examples, refer to <a href="/agents/runtime/operations/using-ai-models/">Using AI Models</a>.</p>
<h2 id="state-as-context">State as context</h2>
<p>Every Agent has a built-in <a href="/agents/runtime/lifecycle/state/">SQL database</a> and key-value state. Instead of passing an entire conversation history from the client on every request, the Agent stores it and builds prompts from its own storage.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1958.md")
</div>
<p>This means the client does not need to send the full conversation on every message. The Agent owns the history, can prune it, enrich it with retrieved documents, or summarize older turns before sending to the model.</p>
<h2 id="surviving-disconnections">Surviving disconnections</h2>
<p>Reasoning models like DeepSeek R1 or GLM-4 can take 30 seconds to several minutes to respond. In a stateless request-response architecture, the client must stay connected the entire time. If the connection drops, the response is lost.</p>
<p>An Agent keeps running after the client disconnects. When the response arrives, the Agent can persist it to state and deliver it when the client reconnects — even hours or days later.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1959.md")
</div>
<p>With <a href="/agents/communication-channels/chat/chat-agents/"><code>AIChatAgent</code></a>, this is handled automatically — messages are persisted to SQLite and streams resume on reconnect.</p>
<h2 id="autonomous-model-calls">Autonomous model calls</h2>
<p>Agents do not need a user request to call a model. You can schedule model calls to run in the background — for nightly summarization, periodic classification, monitoring, or any task that should happen without human interaction.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1960.md")
</div>
<h2 id="multi-model-pipelines">Multi-model pipelines</h2>
<p>Because an Agent maintains state across calls, you can chain multiple models in a single method — using a fast model for classification, a reasoning model for planning, and an embedding model for retrieval — without losing context between steps.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1961.md")
</div>
<p>Each intermediate result stays in the Agent's memory for the duration of the method, and the final result is persisted to SQL for future reference.</p>
<h2 id="caching-and-cost-control">Caching and cost control</h2>
<p>Persistent storage means you can cache model responses and avoid redundant calls. This is especially useful for expensive operations like embeddings or long reasoning chains.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1962.md")
</div>
<p>For provider-level caching and rate limit management across multiple agents, use <a href="/ai-gateway/">AI Gateway</a>.</p>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-using-ai-models-agents-runtime-operations-using-ai-models"><a href="/agents/runtime/operations/using-ai-models/">Using AI Models</a></h3><p>Provider setup, streaming, and code examples for Workers AI, OpenAI, Anthropic, and more.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-chat-agents-agents-communication-channels-chat-chat-agents"><a href="/agents/communication-channels/chat/chat-agents/">Chat agents</a></h3><p>AIChatAgent handles message persistence, resumable streaming, and tools automatically.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-store-and-sync-state-agents-runtime-lifecycle-state"><a href="/agents/runtime/lifecycle/state/">Store and sync state</a></h3><p>SQL database and key-value state APIs for building context and caching.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-schedule-tasks-agents-runtime-execution-schedule-tasks"><a href="/agents/runtime/execution/schedule-tasks/">Schedule tasks</a></h3><p>Run autonomous model calls on a delay, schedule, or cron.</p></div>
