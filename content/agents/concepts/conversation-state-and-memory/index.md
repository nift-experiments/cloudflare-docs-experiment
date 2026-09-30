---
cp9:
  canonical: https://developers.cloudflare.com/agents/concepts/conversation-state-and-memory/
  description: How agents store and recall information, including read-only context, writable short-form memory, searchable knowledge, and on-demand skills.
  full_title: Conversation state and memory · Cloudflare Agents docs
  head_html: <title>Conversation state and memory · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="How agents store and recall information, including read-only context, writable short-form memory, searchable knowledge, and on-demand skills."><link rel="canonical" href="https://developers.cloudflare.com/agents/concepts/conversation-state-and-memory/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/concepts/conversation-state-and-memory/index.md"><meta property="og:title" content="Conversation state and memory · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How agents store and recall information, including read-only context, writable short-form memory, searchable knowledge, and on-demand skills."><meta property="og:url" content="https://developers.cloudflare.com/agents/concepts/conversation-state-and-memory/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/concepts/conversation-state-and-memory/#page","headline":"Conversation state and memory \u00b7 Cloudflare Agents docs","description":"How agents store and recall information, including read-only context, writable short-form memory, searchable knowledge, and on-demand skills.","url":"https://developers.cloudflare.com/agents/concepts/conversation-state-and-memory/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /agents/concepts/conversation-state-and-memory/
  schema: 1
---
<p>Agents need memory to be useful over time. Without it, every conversation starts from zero. The agent forgets who the user is, what it learned, and what it was doing. Memory is what turns a stateless LLM call into a persistent, context-aware agent.</p>
<p>The <a href="/agents/runtime/lifecycle/sessions/">Session API</a> provides the memory layer for agents built on the Cloudflare Agents SDK. It manages two kinds of memory: <strong>conversation history</strong> (the messages and tool calls that make up a session) and <strong>context memory</strong> (persistent blocks injected into the system prompt that the agent can read, write, search, and load).</p>
<p>Use this page when you need more than simple synced state or flat chat history. For small UI state, use <a href="/agents/runtime/lifecycle/state/">Store and sync state</a>. For basic chat persistence, <code>AIChatAgent</code> stores messages for you. For opinionated long-term memory, Think builds on Session and context blocks.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="experimental">Experimental</h3>
@markup("md", "content/.markup/bodies/1941.md")
</aside>
<h2 id="conversation-history">Conversation history</h2>
<p>The most fundamental type of memory is the conversation itself: the messages between the user and the agent, the tool calls the agent made, and the results it received. The Session stores all of this in a tree-structured message history backed by a Session Provider, defaulting to SQLite.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1942.md")
</div>
<p>Conversation history persists across Durable Object hibernation and eviction. When the agent wakes up, the full history is available in SQLite. It does not need to be replayed or reconstructed.</p>
<p>Messages are stored in a tree structure via <code>parent_id</code>, which enables branching conversations. When you <code>appendMessage</code> with a <code>parentId</code> that already has children, you create a branch, useful for features like response regeneration. <code>getHistory(leafId)</code> walks any chosen path through the tree.</p>
<p>The Session also provides full-text search across the conversation history:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1943.md")
</div>
<p>As conversations grow long, <a href="#compaction">compaction</a> summarizes older messages to keep the context window manageable without losing the underlying data.</p>
<h2 id="context-memory">Context memory</h2>
<p>Context memory is persistent information injected into the system prompt, separate from the conversation history. It gives the agent access to identity, instructions, learned facts, knowledge bases, and reference material across every turn.</p>
<p>The Session API supports four types of context memory, each suited to different kinds of information. The type is determined by the <strong>provider</strong> backing the context block. The Session detects the provider's capabilities automatically.</p>
<h3 id="read-only-context">Read-only context</h3>
<p>This is your traditional system prompt: the agent's identity, personality, and instructions. You might write it directly in your codebase, load it from a <code>SOUL.md</code> file in R2, or fetch it from an API. The content is injected into the system prompt and the agent cannot modify it.</p>
<p>A coding assistant might have a soul that defines its personality and constraints:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1944.md")
</div>
<p>Or load it from R2 so you can update the agent's personality without redeploying:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1945.md")
</div>
<p>Read-only blocks are defined by providing an object with only a <code>get()</code> method. No tools are generated. The content appears in the system prompt and the agent has no way to change it.</p>
<h3 id="writable-short-form-context">Writable short-form context</h3>
<p>Think of this as a scratchpad the agent maintains for itself, a place to jot down things it needs to remember. Like how Claude Code keeps a todo list of tasks to work through, or how a customer support agent might track what it has learned about the user during the conversation.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1946.md")
</div>
<p>When you omit the <code>provider</code> option in the builder, the Session auto-wires to a SQLite-backed writable provider. The agent gets a <code>set_context</code> tool that lets it replace or append content to these blocks. Token limits are enforced, so the agent cannot write more than the <code>maxTokens</code> budget allows.</p>
<p>The system prompt renders writable blocks with a token usage indicator so the agent knows how much space it has left:</p>
<pre tabindex="0"><code class="language-txt">══════════════════════════════════════════════&#10;MEMORY (Important facts learned during conversation) [45% — 495/1100 tokens] [writable]&#10;══════════════════════════════════════════════&#10;User prefers dark mode.&#10;User&#x27;s project uses React and TypeScript.&#10;Deployment target is Cloudflare Workers.&#10;&#10;══════════════════════════════════════════════&#10;TODOS (Task list) [12% — 240/2000 tokens] [writable]&#10;══════════════════════════════════════════════&#10;&#45; [x] Set up project scaffolding&#10;&#45; [ ] Add authentication middleware&#10;&#45; [ ] Write integration tests&#10;</code></pre>
<p>The content persists across messages and survives hibernation. It is always visible in the system prompt, so the agent sees it on every turn without needing to fetch anything.</p>
<h3 id="searchable-context">Searchable context</h3>
<p>When you have a large body of information (a knowledge base, documentation, logs, accumulated notes) you do not want to stuff it all into the system prompt. Searchable context keeps a summary in the system prompt (for example, &quot;42 entries indexed&quot;) and lets the agent retrieve specific entries when it needs them.</p>
<p>You provide a provider with a <code>search()</code> method. How that search works is entirely up to you: full-text search, vector search via <a href="/vectorize/">Vectorize</a>, a call to an external API, or anything else. The Session does not care about the implementation, only that the provider has a <code>search()</code> method.</p>
<p>The built-in <code>AgentSearchProvider</code> uses Durable Object SQLite with FTS5 as default:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1947.md")
</div>
<p>But you can implement your own provider backed by any search mechanism:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1948.md")
</div>
<p>The agent gets a <code>search_context</code> tool for querying and a <code>set_context</code> tool for indexing new entries. It decides what to search for, and you decide how the search works.</p>
<p>This is the right choice when the agent needs to find specific pieces of information from a large collection, rather than loading entire documents.</p>
<h3 id="loadable-context-skills">Loadable context (Skills)</h3>
<p>Skills are large pieces of context (complete documents, reference guides, runbooks, templates) that the agent can discover and load on demand. Think of them as reference material on a shelf: the agent sees a list of titles and descriptions, picks what is relevant to the current task, loads it, uses it, and unloads it when done.</p>
<p>Unlike searchable context where the agent retrieves small chunks from a larger collection, skills are designed to be loaded whole. When an agent loads a skill, it gets the entire document in its context window.</p>
<p>Skills are backed by the <code>SkillProvider</code> interface. A skill provider has three methods:</p>
<ul>
<li><strong><code>get()</code></strong> returns a metadata listing (titles and descriptions) that appears in the system prompt</li>
<li><strong><code>load(key)</code></strong> fetches the full content of a specific skill</li>
<li><strong><code>set(key, content, description?)</code></strong> writes or updates a skill entry (optional)</li>
</ul>
<p>The system prompt shows available skills as a listing. The <code>[loadable]</code> tag tells the LLM that these entries are not inline. It needs to use a tool to access the full content:</p>
<pre tabindex="0"><code class="language-txt">══════════════════════════════════════════════&#10;SKILLS [loadable]&#10;══════════════════════════════════════════════&#10;&#45; api-ref: API Reference documentation&#10;&#45; style-guide: Company style guide&#10;&#45; deploy-checklist: Production deployment checklist&#10;</code></pre>
<p>The agent sees the titles, decides which skill is relevant to the current task, and uses <code>load_context</code> to pull the full content into its working context. When it is done, it uses <code>unload_context</code> to free the space. When the skill provider implements <code>set()</code>, the agent can also write back, updating existing skills or creating new ones.</p>
<pre tabindex="0"><code class="language-txt">Agent sees: &quot;- deploy-checklist: Production deployment checklist&quot;&#10;User asks: &quot;Walk me through a production deployment&quot;&#10;Agent calls: load_context({ block: &quot;skills&quot;, key: &quot;deploy-checklist&quot; })&#10;→ Full checklist content is loaded into the agent&#x27;s working context&#10;</code></pre>
<h4 id="r2-backed-skills">R2-backed skills</h4>
<p>The built-in <code>R2SkillProvider</code> stores skills in a Cloudflare R2 bucket. Each skill is an R2 object with optional custom metadata for descriptions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1949.md")
</div>
<p>The <code>prefix</code> option scopes the provider to a subdirectory in the bucket. Skill keys in the metadata listing are shown without the prefix, so <code>skills/api-ref</code> becomes <code>api-ref</code> in the system prompt.</p>
<p>Use <code>keys</code> to allowlist specific prefix-relative skills for <code>get()</code> and <code>load()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1950.md")
</div>
<p>Add an R2 bucket binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1951.md")
</div>
<p>Skills are regular R2 objects. Upload them through any R2 interface (the Wrangler CLI, the dashboard, or the Workers API):</p>
<pre tabindex="0"><code class="language-sh">&#35; Upload a skill from a file&#10;wrangler r2 object put my-agent-skills/skills/style-guide --file ./docs/style-guide.md --content-type text/markdown&#10;</code></pre>
<p>To add descriptions (shown in the metadata listing), set custom metadata on the R2 object:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1952.md")
</div>
<h4 id="custom-skill-providers">Custom skill providers</h4>
<p>You can back skills with any storage by implementing the <code>SkillProvider</code> interface:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1953.md")
</div>
<p>The Session detects the <code>load()</code> method via duck-typing and generates the appropriate tools automatically.</p>
<h4 id="skills-vs-other-memory-types">Skills vs other memory types</h4>
<table>
<thead>
<tr>
<th>Aspect</th>
<th>Skills</th>
<th>Writable context</th>
<th>Searchable context</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>In system prompt</strong></td>
<td>Metadata listing only</td>
<td>Full content</td>
<td>Summary count</td>
</tr>
<tr>
<td><strong>Access pattern</strong></td>
<td>Load whole document by key</td>
<td>Always visible</td>
<td>Search by query</td>
</tr>
<tr>
<td><strong>Best for</strong></td>
<td>Large documents, reference material</td>
<td>Short notes, preferences</td>
<td>Large collections of small entries</td>
</tr>
<tr>
<td><strong>Context cost</strong></td>
<td>Low (until loaded)</td>
<td>Proportional to content</td>
<td>Low (until searched)</td>
</tr>
<tr>
<td><strong>Agent writes?</strong></td>
<td>Optional (if <code>set</code> implemented)</td>
<td>Yes (via <code>set_context</code>)</td>
<td>Yes (via <code>set_context</code>)</td>
</tr>
</tbody>
</table>
<p>The key distinction: skills are <strong>lazy</strong>. They cost nearly nothing in the system prompt until the agent decides it needs one. This makes them ideal for large reference material where only a subset is relevant to any given conversation.</p>
<h2 id="how-agents-interact-with-memory">How agents interact with memory</h2>
<p>The Session automatically generates tools based on the provider types of your context blocks. You pass these tools to your LLM alongside your own application-specific tools:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1954.md")
</div>
<h3 id="generated-tools">Generated tools</h3>
<p>The Session generates tools dynamically based on what provider types are present:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Generated when</th>
<th>What it does</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong><code>set_context</code></strong></td>
<td>Any writable, skill, or search block exists</td>
<td>Writes content to a named block. For writable blocks, replaces or appends. For skill/search blocks, writes a keyed entry.</td>
</tr>
<tr>
<td><strong><code>load_context</code></strong></td>
<td>Any skill block exists</td>
<td>Loads full content of a document by key into the agent's context.</td>
</tr>
<tr>
<td><strong><code>unload_context</code></strong></td>
<td>Any skill block exists</td>
<td>Frees context space by removing a previously loaded document. The document remains available for re-loading.</td>
</tr>
<tr>
<td><strong><code>search_context</code></strong></td>
<td>Any search block exists</td>
<td>Full-text search within a searchable block. Returns the top results ranked by relevance.</td>
</tr>
<tr>
<td><strong><code>session_search</code></strong></td>
<td>Using <code>SessionManager</code></td>
<td>Searches across all sessions (cross-conversation search).</td>
</tr>
</tbody>
</table>
<p>The tools include descriptions and parameter schemas that tell the LLM which blocks are available and what they are for. The agent decides when and how to use them based on the conversation.</p>
<p>For the full tool signatures and all Session methods, refer to the <a href="/agents/runtime/lifecycle/sessions/">Session API reference</a>.</p>
<h2 id="the-system-prompt">The system prompt</h2>
<p>Context blocks are assembled into a structured system prompt with clear headers and metadata. Each block gets a labeled section with tags indicating its type and capacity:</p>
<pre tabindex="0"><code class="language-txt">══════════════════════════════════════════════&#10;SOUL (Identity) [readonly]&#10;══════════════════════════════════════════════&#10;You are a helpful coding assistant who speaks concisely.&#10;&#10;══════════════════════════════════════════════&#10;MEMORY (Important facts) [45% — 495/1100 tokens] [writable]&#10;══════════════════════════════════════════════&#10;User prefers dark mode.&#10;User&#x27;s project uses React and TypeScript.&#10;&#10;══════════════════════════════════════════════&#10;KNOWLEDGE (Searchable knowledge base) [searchable]&#10;══════════════════════════════════════════════&#10;12 entries indexed.&#10;&#10;══════════════════════════════════════════════&#10;SKILLS [loadable]&#10;══════════════════════════════════════════════&#10;&#45; api-ref: API Reference documentation&#10;&#45; style-guide: Company style guide&#10;</code></pre>
<p>The tags (<code>[readonly]</code>, <code>[writable]</code>, <code>[searchable]</code>, <code>[loadable]</code>) tell the LLM what kind of interaction is possible with each block. Token budgets show the agent how much space remains in writable blocks, helping it manage its own memory.</p>
<h2 id="gotchas">Gotchas</h2>
<h3 id="prompt-caching">Prompt caching</h3>
<p>LLM providers (Anthropic, OpenAI, and others) cache the system prompt prefix. When consecutive requests share the same system prompt, the provider can skip re-processing that prefix, reducing both latency and cost. Breaking the cache (by changing the system prompt) throws away this benefit.</p>
<p>The Session API is designed to work with prompt caching:</p>
<ul>
<li><strong><code>freezeSystemPrompt()</code></strong> renders the system prompt from all context blocks on the first call, then returns the cached value on subsequent calls. The prompt does not change between turns, even when the agent writes to memory via <code>set_context</code>.</li>
<li><strong><code>withCachedPrompt()</code></strong> persists the frozen prompt to storage, so it survives Durable Object hibernation and eviction. When the agent wakes up, it loads the same prompt without re-fetching from all providers.</li>
</ul>
<p>When the agent uses <code>set_context</code> to update a writable block, the underlying provider is updated immediately (the data is saved), but the frozen system prompt is <strong>not</strong> re-rendered. The LLM sees the update on its next turn only if you explicitly call <code>refreshSystemPrompt()</code>, which you typically do between conversation turns, not mid-turn.</p>
<p>This means the system prompt stays stable throughout a multi-step tool-use turn, preserving the provider's prefix cache across every step.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1955.md")
</div>
<h3 id="compaction">Compaction</h3>
<p>Long conversations eventually exceed the LLM's context window. Compaction addresses this at two levels: <strong>macro-compaction</strong> summarizes ranges of older messages, and <strong>micro-compaction</strong> truncates individual messages that are too large.</p>
<h4 id="macro-compaction">Macro-compaction</h4>
<p>Macro-compaction summarizes older messages, but it never deletes the originals.</p>
<p>It uses <strong>overlays</strong>: a summary is stored in a separate table, keyed by the message range it covers. When <code>getHistory()</code> is called, overlays are applied transparently at read time. The compacted range is replaced by a synthetic summary message. The underlying messages remain in SQLite, preserving the full conversation for audit, search, and branching.</p>
<pre tabindex="0"><code class="language-txt">Messages:  [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]&#10;                    ↓ compaction ↓&#10;Overlay:   [1] [2] [SUMMARY of 3-7]           [8] [9] [10]&#10;                                                ↑ tail protected&#10;</code></pre>
<p>The key points:</p>
<ul>
<li><strong>Non-destructive</strong>, original messages are never deleted. The full conversation is always available in the database.</li>
<li><strong>Iterative</strong>, when the conversation grows again and triggers another compaction, the existing summary is passed to the LLM to update, not replaced from scratch.</li>
<li><strong>Boundary-aware</strong>, compaction boundaries are shifted to avoid splitting tool call / tool result pairs.</li>
<li><strong>Configurable</strong>, <code>protectHead</code> preserves the first N messages (usually the system context), and <code>tailTokenBudget</code> keeps the most recent messages intact.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1956.md")
</div>
<p>Auto-compaction triggers after <code>appendMessage()</code> when the estimated token count exceeds the threshold. Compaction failure is non-fatal, the message is already saved.</p>
<h4 id="micro-compaction">Micro-compaction</h4>
<p>Micro-compaction works at the individual message level rather than across ranges. It handles two problems:</p>
<p><strong>Read-time truncation</strong>: <code>truncateOlderMessages()</code> shortens tool outputs and long text in older messages before sending them to the LLM. Recent messages (last 4 by default) are kept intact. This operates on a copy, stored messages are not mutated.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1957.md")
</div>
<p><strong>Row size enforcement</strong>: when a message is persisted (typically an assistant message with large tool outputs), it is checked against the SQLite row size limit. Oversized tool outputs are replaced with a preview and a note suggesting the tool be re-run. This prevents individual messages from exceeding storage limits while preserving the conversation flow.</p>
<h2 id="related">Related</h2>
<div class="nb-card nb-link-card"><h3 id="card-session-api-reference-agents-runtime-lifecycle-sessions"><a href="/agents/runtime/lifecycle/sessions/">Session API reference</a></h3><p>Full API reference for Session, covering messages, context blocks, compaction, search, tools, and custom providers.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-store-and-sync-state-agents-runtime-lifecycle-state"><a href="/agents/runtime/lifecycle/state/">Store and sync state</a></h3><p>setState() for simpler key-value persistence and real-time sync.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-think-agents-harnesses-think"><a href="/agents/harnesses/think/">Think</a></h3><p>Opinionated chat agent with built-in Session integration via configureSession().</p></div>
