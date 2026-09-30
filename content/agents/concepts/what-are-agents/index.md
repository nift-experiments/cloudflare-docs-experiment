---
cp9:
  canonical: https://developers.cloudflare.com/agents/concepts/what-are-agents/
  description: Understand what Agents are, how they differ from workflows and co-pilots, and when to use them.
  full_title: What are agents? · Cloudflare Agents docs
  head_html: <title>What are agents? · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand what Agents are, how they differ from workflows and co-pilots, and when to use them."><link rel="canonical" href="https://developers.cloudflare.com/agents/concepts/what-are-agents/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/concepts/what-are-agents/index.md"><meta property="og:title" content="What are agents? · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand what Agents are, how they differ from workflows and co-pilots, and when to use them."><meta property="og:url" content="https://developers.cloudflare.com/agents/concepts/what-are-agents/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI,LLM"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/concepts/what-are-agents/#page","headline":"What are agents? \u00b7 Cloudflare Agents docs","description":"Understand what Agents are, how they differ from workflows and co-pilots, and when to use them.","url":"https://developers.cloudflare.com/agents/concepts/what-are-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI","LLM"]}</script>
  markdown: true
  noindex: false
  route: /agents/concepts/what-are-agents/
  schema: 1
---
<p>An agent is an AI system that can autonomously execute tasks by making decisions about tool usage and process flow. Unlike traditional automation that follows predefined paths, agents can dynamically adapt their approach based on context and intermediate results. Agents are also distinct from co-pilots (such as traditional chat applications) in that they can fully automate a task, as opposed to simply augmenting and extending human input.</p>
<ul>
<li><strong>Agents</strong> → non-linear, non-deterministic (can change from run to run)</li>
<li><strong>Workflows</strong> → linear, deterministic execution paths</li>
<li><strong>Co-pilots</strong> → augmentative AI assistance requiring human intervention</li>
</ul>
<h2 id="example-booking-vacations">Example: Booking vacations</h2>
<p>If this is your first time working with or interacting with agents, this example illustrates how an agent works within a context like booking a vacation.</p>
<p>Imagine you are trying to book a vacation. You need to research flights, find hotels, check restaurant reviews, and keep track of your budget.</p>
<h3 id="traditional-workflow-automation">Traditional workflow automation</h3>
<p>A traditional automation system follows a predetermined sequence:</p>
<ul>
<li>Takes specific inputs (dates, location, budget)</li>
<li>Calls predefined API endpoints in a fixed order</li>
<li>Returns results based on hardcoded criteria</li>
<li>Cannot adapt if unexpected situations arise</li>
</ul>
<p><img src="/assets/upstream/images/agents/workflow-automation.svg" alt="Traditional workflow automation diagram" /></p>
<h3 id="ai-co-pilot">AI Co-pilot</h3>
<p>A co-pilot acts as an intelligent assistant that:</p>
<ul>
<li>Provides hotel and itinerary recommendations based on your preferences</li>
<li>Can understand and respond to natural language queries</li>
<li>Offers guidance and suggestions</li>
<li>Requires human decision-making and action for execution</li>
</ul>
<p><img src="/assets/upstream/images/agents/co-pilot.svg" alt="A co-pilot diagram" /></p>
<h3 id="agent">Agent</h3>
<p>An agent combines AI's ability to make judgments and call the relevant tools to execute the task. An agent's output will be nondeterministic given:</p>
<ul>
<li>Real-time availability and pricing changes</li>
<li>Dynamic prioritization of constraints</li>
<li>Ability to recover from failures</li>
<li>Adaptive decision-making based on intermediate results</li>
</ul>
<p><img src="/assets/upstream/images/agents/agent-workflow.svg" alt="An agent diagram" /></p>
<p>An agent can dynamically generate an itinerary and execute on booking reservations, similarly to what you would expect from a travel agent.</p>
<h2 id="components-of-agent-systems">Components of agent systems</h2>
<p>Agent systems typically have three primary components:</p>
<ul>
<li><strong>Decision Engine</strong>: Usually an LLM (Large Language Model) that determines action steps</li>
<li><strong>Tool Integration</strong>: APIs, functions, and services the agent can utilize — often via <a href="/agents/model-context-protocol/">MCP</a></li>
<li><strong>Memory System</strong>: Maintains context and tracks task progress</li>
</ul>
<h3 id="how-agents-work">How agents work</h3>
<p>Agents operate in a continuous loop of:</p>
<ol>
<li><strong>Observing</strong> the current state or task</li>
<li><strong>Planning</strong> what actions to take, using AI for reasoning</li>
<li><strong>Executing</strong> those actions using available tools</li>
<li><strong>Learning</strong> from the results (storing results in memory, updating task progress, and preparing for next iteration)</li>
</ol>
<h2 id="building-agents-on-cloudflare">Building agents on Cloudflare</h2>
<p>The Cloudflare Agents SDK provides the infrastructure for building production agents:</p>
<ul>
<li><strong>Persistent state</strong> — Each agent instance has its own SQLite database for storing context and memory</li>
<li><strong>Real-time sync</strong> — State changes automatically broadcast to all connected clients via WebSockets</li>
<li><strong>Hibernation</strong> — Agents sleep when idle and wake on demand, so you only pay for what you use</li>
<li><strong>Global edge deployment</strong> — Agents run close to your users on Cloudflare's network</li>
<li><strong>Built-in capabilities</strong> — Scheduling, task queues, workflows, email handling, and more</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-quick-start-agents-getting-started-quick-start"><a href="/agents/getting-started/quick-start/">Quick start</a></h3><p>Build your first agent in 10 minutes.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-agents-api-agents-runtime-agents-api"><a href="/agents/runtime/agents-api/">Agents API</a></h3><p>Complete API reference for the Agents SDK.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-using-ai-models-agents-runtime-operations-using-ai-models"><a href="/agents/runtime/operations/using-ai-models/">Using AI models</a></h3><p>Integrate OpenAI, Anthropic, and other providers.</p></div>
