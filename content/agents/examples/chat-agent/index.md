---
cp9:
  canonical: https://developers.cloudflare.com/agents/examples/chat-agent/
  description: Build a streaming AI chat agent with tools using Workers AI — no API keys required.
  full_title: Chat agent · Cloudflare Agents docs
  head_html: <title>Chat agent · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Build a streaming AI chat agent with tools using Workers AI — no API keys required."><link rel="canonical" href="https://developers.cloudflare.com/agents/examples/chat-agent/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/examples/chat-agent/index.md"><meta property="og:title" content="Chat agent · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build a streaming AI chat agent with tools using Workers AI — no API keys required."><meta property="og:url" content="https://developers.cloudflare.com/agents/examples/chat-agent/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/examples/chat-agent/#page","headline":"Chat agent \u00b7 Cloudflare Agents docs","description":"Build a streaming AI chat agent with tools using Workers AI \u2014 no API keys required.","url":"https://developers.cloudflare.com/agents/examples/chat-agent/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/examples/chat-agent/
  schema: 1
---
<p>Build a chat agent that streams AI responses, calls server-side tools, executes client-side tools in the browser, and asks for user approval before sensitive actions.</p>
<p><strong>What you will build:</strong> A chat agent powered by Workers AI with three tool types — automatic, client-side, and approval-gated.</p>
<p><strong>Time:</strong> ~15 minutes</p>
<p>This tutorial starts from a minimal Hello World Worker so you can see each moving part. If you want a complete starter app with the same core pieces already wired together, start with the <a href="/agents/getting-started/quick-start/">quick start</a> and then return here to understand how the chat pieces fit together.</p>
<p><strong>Prerequisites:</strong></p>
<ul>
<li>Node.js 18+</li>
<li>A Cloudflare account (free tier works)</li>
</ul>
<h2 id="1-create-the-project"><ol>
<li>Create the project</li>
</ol></h2>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest chat-agent&#10;</code></pre>
<p>Select <strong>&quot;Hello World&quot; Worker</strong> when prompted. Then install the dependencies:</p>
<pre tabindex="0"><code class="language-sh">cd chat-agent&#10;npm install agents @cloudflare/ai-chat ai workers-ai-provider zod&#10;</code></pre>
<h2 id="2-configure-wrangler"><ol start="2">
<li>Configure Wrangler</li>
</ol></h2>
<p>Replace your <code>wrangler.jsonc</code> with:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1926.md")
</div>
<p>Key settings:</p>
<ul>
<li><code>ai</code> binds Workers AI — no API key needed</li>
<li><code>durable_objects</code> registers your chat agent class</li>
<li><code>new_sqlite_classes</code> enables SQLite storage for message persistence</li>
</ul>
<h2 id="3-write-the-server"><ol start="3">
<li>Write the server</li>
</ol></h2>
<p>Create <code>src/server.ts</code>. This is where your agent lives:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1927.md")
</div>
<h3 id="what-each-tool-type-does">What each tool type does</h3>
<table>
<thead>
<tr>
<th>Tool</th>
<th><code>execute</code>?</th>
<th><code>needsApproval</code>?</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>getWeather</code></td>
<td>Yes</td>
<td>No</td>
<td>Runs on the server automatically</td>
</tr>
<tr>
<td><code>getUserTimezone</code></td>
<td>No</td>
<td>No</td>
<td>Sent to the client; browser provides the result</td>
</tr>
<tr>
<td><code>calculate</code></td>
<td>Yes</td>
<td>Yes (large numbers)</td>
<td>Pauses for user approval, then runs on server</td>
</tr>
</tbody>
</table>
<h2 id="4-write-the-client"><ol start="4">
<li>Write the client</li>
</ol></h2>
<p>Create <code>src/client.tsx</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1928.md")
</div>
<h3 id="key-client-concepts">Key client concepts</h3>
<ul>
<li><strong><code>useAgent</code></strong> connects to your <code>ChatAgent</code> over WebSocket</li>
<li><strong><code>useAgentChat</code></strong> manages the chat lifecycle (messages, streaming, tools)</li>
<li><strong><code>onToolCall</code></strong> handles client-side tools — when the LLM calls <code>getUserTimezone</code>, the browser provides the result and the conversation auto-continues</li>
<li><strong><code>addToolApprovalResponse</code></strong> approves or rejects tools that have <code>needsApproval</code></li>
<li>Messages, streaming, and resumption are all handled automatically</li>
</ul>
<h2 id="5-run-locally"><ol start="5">
<li>Run locally</li>
</ol></h2>
<p>Generate types and start the dev server:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler types&#10;npm run dev&#10;</code></pre>
<p>Try these prompts:</p>
<ul>
<li><strong>&quot;What is the weather in Tokyo?&quot;</strong> — calls the server-side <code>getWeather</code> tool</li>
<li><strong>&quot;What timezone am I in?&quot;</strong> — calls the client-side <code>getUserTimezone</code> tool (the browser provides the answer)</li>
<li><strong>&quot;What is 5000 times 3?&quot;</strong> — triggers the approval UI before executing (numbers over 1000)</li>
</ul>
<h2 id="6-deploy"><ol start="6">
<li>Deploy</li>
</ol></h2>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your agent is now live on Cloudflare's global network. Messages persist in SQLite, streams resume on disconnect, and the agent hibernates when idle to save resources.</p>
<h2 id="what-you-built">What you built</h2>
<p>Your chat agent has:</p>
<ul>
<li><strong>Streaming AI responses</strong> via Workers AI (no API keys)</li>
<li><strong>Message persistence</strong> in SQLite — conversations survive restarts</li>
<li><strong>Server-side tools</strong> that execute automatically</li>
<li><strong>Client-side tools</strong> that run in the browser and feed results back to the LLM</li>
<li><strong>Human-in-the-loop approval</strong> for sensitive operations</li>
<li><strong>Resumable streaming</strong> — if a client disconnects mid-stream, it picks up where it left off</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-chat-agents-api-reference-agents-communication-channels-chat-chat-agents"><a href="/agents/communication-channels/chat/chat-agents/">Chat agents API reference</a></h3><p>Full reference for AIChatAgent and useAgentChat — providers, storage, advanced patterns.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-store-and-sync-state-agents-runtime-lifecycle-state"><a href="/agents/runtime/lifecycle/state/">Store and sync state</a></h3><p>Add real-time state beyond chat messages.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-callable-methods-agents-runtime-lifecycle-callable-methods"><a href="/agents/runtime/lifecycle/callable-methods/">Callable methods</a></h3><p>Expose agent methods as typed RPC for your client.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-human-in-the-loop-agents-concepts-agentic-patterns-human-in-the-loop"><a href="/agents/concepts/agentic-patterns/human-in-the-loop/">Human-in-the-loop</a></h3><p>Deeper patterns for approval flows and manual intervention.</p></div>
