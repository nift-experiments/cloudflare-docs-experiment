---
cp9:
  canonical: https://developers.cloudflare.com/agent-memory/api/workers-api/
  description: Configure the Agent Memory binding and use memory profiles from Worker code.
  full_title: Workers API · Cloudflare Agent Memory docs
  head_html: <title>Workers API · Cloudflare Agent Memory docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure the Agent Memory binding and use memory profiles from Worker code."><link rel="canonical" href="https://developers.cloudflare.com/agent-memory/api/workers-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agent-memory/api/workers-api/index.md"><meta property="og:title" content="Workers API · Cloudflare Agent Memory docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure the Agent Memory binding and use memory profiles from Worker code."><meta property="og:url" content="https://developers.cloudflare.com/agent-memory/api/workers-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agent Memory"><meta name="algolia_product_filter" content="Agent Memory"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agent Memory"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agent-memory/api/workers-api/#page","headline":"Workers API \u00b7 Cloudflare Agent Memory docs","description":"Configure the Agent Memory binding and use memory profiles from Worker code.","url":"https://developers.cloudflare.com/agent-memory/api/workers-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agent-memory/api/workers-api/
  schema: 1
---
<p>Use the Workers API to access Agent Memory from your <a href="/workers/">Worker</a>. The binding connects your Worker to a <a href="/agent-memory/concepts/namespaces-profiles/">namespace</a> containing profiles, which are isolated memory stores for your agent.</p>
<h2 id="configure-the-binding">Configure the binding</h2>
<p>Add an <code>agent_memory</code> entry to your Wrangler configuration. The <code>binding</code> field is the variable name you use in Worker code, and the <code>namespace</code> field is the Agent Memory namespace to bind to.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1823.md")
</div>
<p>To bind multiple namespaces, add multiple entries to the <code>agent_memory</code> array.</p>
<h2 id="generated-types">Generated types</h2>
<p>Run <code>npx wrangler types</code> to generate the binding type in <code>worker-configuration.d.ts</code>:</p>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;	MEMORY: AgentMemoryNamespace;&#10;}&#10;</code></pre>
<h2 id="namespace-methods">Namespace methods</h2>
<p>Use namespace methods on the binding to access and manage memory profiles.</p>
<h3 id="getprofile-profilename"><code>getProfile(profileName)</code></h3>
<p>Gets a memory profile by name. If the profile does not exist, Agent Memory creates it.</p>
<ul>
<li><code>profileName</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>: Name of the profile to access. Maximum 100 characters.</li>
<li>Returns <span class="nb-type">Promise&lt;AgentMemoryProfile&gt;</span></li>
</ul>
<p>The first <code>getProfile()</code> call for a new profile may take longer while Agent Memory creates the profile.</p>
<h3 id="deleteprofile-profilename"><code>deleteProfile(profileName)</code></h3>
<p>Marks a profile and all its memories and messages for deletion.</p>
<ul>
<li><code>profileName</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>: Name of the profile to delete. Maximum 100 characters.</li>
<li>Returns <span class="nb-type">Promise&lt;void&gt;</span></li>
</ul>
<h2 id="profile-methods">Profile methods</h2>
<p>Call profile methods after you get a profile from the binding.</p>
<pre tabindex="0"><code class="language-ts">type AgentMemoryMemory = {&#10;	id: string;&#10;	type: &quot;fact&quot; | &quot;event&quot; | &quot;instruction&quot; | &quot;task&quot;;&#10;	summary: string;&#10;	content: string;&#10;	sessionId: string | null;&#10;	createdAt: Date;&#10;	updatedAt: Date;&#10;};&#10;</code></pre>
<h3 id="ingest-messages-options"><code>ingest(messages, options?)</code></h3>
<p>Processes a conversation and extracts structured memories from it. Agent Memory identifies facts, events, instructions, and tasks automatically, so you do not need to specify what to remember.</p>
<ul>
<li><code>messages</code> <span class="nb-type">Iterable&lt;AgentMemoryMessage&gt;</span> <span class="nb-metainfo">required</span>: Conversation messages to process.</li>
<li><code>options.sessionId</code> <span class="nb-type">string | null</span> <span class="nb-metainfo">optional</span>: Identifier for the conversation session. Maximum 64 characters. If omitted, Agent Memory derives one from the message content.</li>
<li>Returns <span class="nb-type">Promise&lt;void&gt;</span></li>
</ul>
<pre tabindex="0"><code class="language-ts">type AgentMemoryMessage = {&#10;	role: &quot;system&quot; | &quot;user&quot; | &quot;assistant&quot;;&#10;	content: string; // Max 32 KB&#10;	timestamp?: Date;&#10;};&#10;</code></pre>
<p><code>ingest()</code> is idempotent. Re-ingesting the same conversation does not create duplicate memories.</p>
<h3 id="remember-memory"><code>remember(memory)</code></h3>
<p>Stores a single memory explicitly. Use <code>remember()</code> when your application or agent already knows what should be stored, instead of passing a conversation to <code>ingest()</code> for extraction.</p>
<ul>
<li><code>memory.content</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>: Memory content to store. The service classifies and summarizes automatically.</li>
<li><code>memory.sessionId</code> <span class="nb-type">string | null</span> <span class="nb-metainfo">optional</span>: Identifier for the related conversation session.</li>
<li>Returns <span class="nb-type">Promise&lt;AgentMemoryMemory&gt;</span></li>
</ul>
<h3 id="recall-query-options"><code>recall(query, options?)</code></h3>
<p>Searches stored memories in the profile and returns a synthesized answer grounded in the stored content.</p>
<ul>
<li><code>query</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>: Natural language question or search query. Maximum 1 KB (1,024 bytes UTF-8).</li>
<li><code>options.thinkingLevel</code> <span class="nb-type">low&quot; | &quot;medium&quot; | &quot;high</span> <span class="nb-metainfo">optional (default: &quot;low&quot;)</span>: Controls retrieval breadth. Higher levels search more candidates but take longer.</li>
<li><code>options.responseLength</code> <span class="nb-type">short&quot; | &quot;medium&quot; | &quot;long</span> <span class="nb-metainfo">optional (default: &quot;medium&quot;)</span>: Controls the verbosity of the synthesized answer.</li>
<li><code>options.referenceDate</code> <span class="nb-type">Date | string</span> <span class="nb-metainfo">optional</span>: Temporal anchor for date-relative queries.</li>
<li>Returns <span class="nb-type">Promise&lt;AgentMemoryRecallResult&gt;</span></li>
</ul>
<pre tabindex="0"><code class="language-ts">type AgentMemoryRecallResult = {&#10;	count: number;&#10;	answer: string;&#10;	candidates: AgentMemoryScoredCandidate[];&#10;};&#10;&#10;type AgentMemoryScoredCandidate = {&#10;	id: string;&#10;	summary: string;&#10;	sessionId: string | null;&#10;	score: number;&#10;};&#10;</code></pre>
<p>If no memories match the query, <code>recall()</code> returns an empty answer.</p>
<h3 id="list-options"><code>list(options?)</code></h3>
<p>Lists memories stored in the profile. Returns a paginated, filterable view of stored memories. Use the returned <code>cursor</code> (when present) to fetch the next page.</p>
<ul>
<li><code>options.limit</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional (default: 20, max: 500)</span>: Maximum number of memories to return.</li>
<li><code>options.cursor</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>: Opaque cursor from a previous page.</li>
<li><code>options.sessionId</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>: Exact-match session filter.</li>
<li><code>options.type</code> <span class="nb-type">fact&quot; | &quot;event&quot; | &quot;instruction&quot; | &quot;task</span> <span class="nb-metainfo">optional</span>: Exact-match memory-type filter.</li>
<li>Returns <span class="nb-type">Promise&lt;AgentMemoryListMemoriesResult&gt;</span></li>
</ul>
<pre tabindex="0"><code class="language-ts">type AgentMemoryMemoryListEntry = Omit&lt;AgentMemoryMemory, &quot;content&quot;&gt;;&#10;&#10;type AgentMemoryListMemoriesResult = {&#10;	memories: AgentMemoryMemoryListEntry[];&#10;	cursor?: string;&#10;};&#10;</code></pre>
<p>List entries omit <code>content</code>. Use <code>get(memoryId)</code> to retrieve the full memory.</p>
<h3 id="get-memoryid"><code>get(memoryId)</code></h3>
<p>Retrieves a memory by ID.</p>
<ul>
<li><code>memoryId</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>: Memory ID.</li>
<li>Returns <span class="nb-type">Promise&lt;AgentMemoryMemory&gt;</span></li>
</ul>
<p>Throws an error if the memory does not exist.</p>
<h3 id="delete-memoryid"><code>delete(memoryId)</code></h3>
<p>Deletes a memory by ID. Removes the memory and any source messages linked to it. Returns the deleted memory.</p>
<ul>
<li><code>memoryId</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>: Memory ID.</li>
<li>Returns <span class="nb-type">Promise&lt;AgentMemoryMemory&gt;</span></li>
</ul>
<p>Throws an error if the memory does not exist.</p>
<h3 id="deletesession-sessionid"><code>deleteSession(sessionId)</code></h3>
<p>Marks all memories and messages in the profile that are tagged with the given session ID for deletion. Rows from other sessions in the same profile are untouched. Idempotent: deleting a session ID that has no rows is a no-op.</p>
<ul>
<li><code>sessionId</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>: Session ID to delete. Maximum 64 characters.</li>
<li>Returns <span class="nb-type">Promise&lt;void&gt;</span></li>
</ul>
<h3 id="getsummary-options"><code>getSummary(options?)</code></h3>
<p>Generates a structured Markdown summary of everything stored in a memory profile. Use it to inspect what Agent Memory remembers about a profile.</p>
<ul>
<li><code>options.sessionId</code> <span class="nb-type">string | null</span> <span class="nb-metainfo">optional</span>: Session ID to scope the &quot;Last Session&quot; section of the summary. If omitted, Agent Memory uses the most recent session.</li>
<li>Returns <span class="nb-type">Promise&lt;AgentMemoryGetSummaryResponse&gt;</span></li>
</ul>
<pre tabindex="0"><code class="language-ts">type AgentMemoryGetSummaryResponse = {&#10;	summary: string;&#10;};&#10;</code></pre>
<h2 id="limits">Limits</h2>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Messages per <code>ingest()</code> call</td>
<td>500</td>
</tr>
<tr>
<td>Message content size</td>
<td>32 KB (32,768 bytes UTF-8)</td>
</tr>
<tr>
<td>Session ID length</td>
<td>64 characters</td>
</tr>
<tr>
<td><code>recall()</code> query size</td>
<td>1 KB (1,024 bytes UTF-8)</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/agent-memory/platform/limits/">Limits</a> for the complete list of constraints.</p>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-http-api-agent-memory-api-http-api"><a href="/agent-memory/api/http-api/">HTTP API</a></h3><p>Use Agent Memory from services that call the Cloudflare API directly.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-get-started-agent-memory-get-started"><a href="/agent-memory/get-started/">Get started</a></h3><p>Add durable memory recall and ingestion to an agent.</p></div>
