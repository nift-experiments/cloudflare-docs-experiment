---
cp9:
  canonical: https://developers.cloudflare.com/agents/harnesses/think/configuration/
  description: Configuration overrides, dynamic runtime configuration, Session integration, and package exports for the Think chat agent framework.
  full_title: Configuration · Cloudflare Agents docs
  head_html: <title>Configuration · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Configuration overrides, dynamic runtime configuration, Session integration, and package exports for the Think chat agent framework."><link rel="canonical" href="https://developers.cloudflare.com/agents/harnesses/think/configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/harnesses/think/configuration/index.md"><meta property="og:title" content="Configuration · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configuration overrides, dynamic runtime configuration, Session integration, and package exports for the Think chat agent framework."><meta property="og:url" content="https://developers.cloudflare.com/agents/harnesses/think/configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/harnesses/think/configuration/#page","headline":"Configuration \u00b7 Cloudflare Agents docs","description":"Configuration overrides, dynamic runtime configuration, Session integration, and package exports for the Think chat agent framework.","url":"https://developers.cloudflare.com/agents/harnesses/think/configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/harnesses/think/configuration/
  schema: 1
---
<p>Think is configured by overriding methods and properties on your <code>Think</code> subclass. Most agents only override <code>getModel()</code>.</p>
<h2 id="configuration-overrides">Configuration overrides</h2>
<table>
<thead>
<tr>
<th>Method / Property</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>getModel()</code></td>
<td>throws</td>
<td>Return the <code>LanguageModel</code> to use</td>
</tr>
<tr>
<td><code>getSystemPrompt()</code></td>
<td><code>&quot;You are a helpful assistant.&quot;</code></td>
<td>System prompt (fallback when no context blocks)</td>
</tr>
<tr>
<td><code>getTools()</code></td>
<td><code>{}</code></td>
<td>AI SDK <code>ToolSet</code> for the agentic loop</td>
</tr>
<tr>
<td><code>getScheduledTasks()</code></td>
<td><code>{}</code></td>
<td>Code-declared recurring prompts or handlers — refer to <a href="/agents/harnesses/think/scheduled-tasks/">Scheduled tasks</a></td>
</tr>
<tr>
<td><code>getDefaultTimezone()</code></td>
<td><code>undefined</code></td>
<td>Default timezone for wall-clock scheduled tasks</td>
</tr>
<tr>
<td><code>getMessengers()</code></td>
<td><code>{}</code></td>
<td>Messenger ingress and delivery declarations — refer to <a href="/agents/harnesses/think/messengers/">Messengers</a></td>
</tr>
<tr>
<td><code>maxSteps</code></td>
<td><code>10</code></td>
<td>Max tool-call rounds per turn</td>
</tr>
<tr>
<td><code>sendReasoning</code></td>
<td><code>true</code></td>
<td>Send reasoning chunks to chat clients</td>
</tr>
<tr>
<td><code>configureSession()</code></td>
<td>identity</td>
<td>Add context blocks, compaction, search, skills — refer to <a href="/agents/runtime/lifecycle/sessions/">Sessions</a></td>
</tr>
<tr>
<td><code>getSkills()</code></td>
<td><code>[]</code></td>
<td>Return Agent Skills sources for on-demand skill activation — refer to <a href="/agents/runtime/execution/agent-skills/">Agent Skills</a></td>
</tr>
<tr>
<td><code>getSkillScriptRunner()</code></td>
<td><code>null</code></td>
<td>Enable the optional <code>run_skill_script</code> tool</td>
</tr>
<tr>
<td><code>workspaceBash</code></td>
<td><code>true</code></td>
<td>Include or configure the default workspace <code>bash</code> tool — refer to <a href="/agents/harnesses/think/tools/">Tools</a></td>
</tr>
<tr>
<td><code>messageConcurrency</code></td>
<td><code>&quot;queue&quot;</code></td>
<td>How overlapping submits behave — refer to <a href="/agents/harnesses/think/client-tools/#message-concurrency">Client tools</a></td>
</tr>
<tr>
<td><code>includeMcpTools</code></td>
<td><code>true</code></td>
<td>Convert connected MCP tools to AI SDK tools and add them to model turns. Refer to <a href="/agents/harnesses/think/tools/#mcp-tools">MCP tools</a></td>
</tr>
<tr>
<td><code>waitForMcpConnections</code></td>
<td><code>false</code></td>
<td>Wait for MCP servers before inference</td>
</tr>
<tr>
<td><code>chatRecovery</code></td>
<td>Always on</td>
<td>Durable recovery configuration. Refer to <a href="/agents/harnesses/think/recovery/">Durable recovery</a> for all options and defaults</td>
</tr>
<tr>
<td><code>chatStreamStallTimeoutMs</code></td>
<td><code>0</code> (off)</td>
<td>Opt-in inactivity watchdog: abort a turn whose model stream produces no chunk for this long (measures the gap between chunks, including tool execution). A stall routes into bounded recovery</td>
</tr>
<tr>
<td><code>contextOverflow</code></td>
<td><code>undefined</code></td>
<td>Opt-in mid-turn context-overflow handling with <code>reactive</code>, <code>maxRetries</code>, and <code>proactive</code> options. Requires <code>classifyChatError</code> plus a session compaction function — refer to <a href="/agents/harnesses/think/recovery/#context-window-overflow-recovery">Context-window overflow recovery</a></td>
</tr>
</tbody>
</table>
<p>For <code>chatRecovery</code> and <code>chatStreamStallTimeoutMs</code> behavior, refer to <a href="/agents/harnesses/think/recovery/">Durable recovery</a>.</p>
<h2 id="dynamic-configuration">Dynamic configuration</h2>
<p>Think's class generics match <code>Agent&lt;Env, State, Props&gt;</code>. Persisted runtime configuration is typed at the <code>configure&lt;T&gt;()</code> and <code>getConfig&lt;T&gt;()</code> call sites, stored in SQLite, and survives hibernation and restarts.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2168.md")
</div>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>configure&lt;T&gt;(config: T)</code></td>
<td>Persist a typed configuration object</td>
</tr>
<tr>
<td><code>getConfig&lt;T&gt;(): T | null</code></td>
<td>Read the persisted configuration, or null if never configured</td>
</tr>
</tbody>
</table>
<p>Expose configuration to the client via <code>@callable</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2169.md")
</div>
<h2 id="session-integration">Session integration</h2>
<p>Think stores conversations in a <a href="/agents/runtime/lifecycle/sessions/">Session</a> — the storage layer that holds your messages and gives the model writable memory. Two concepts come up here: <strong>context blocks</strong> are labelled sections of the system prompt the model can read and update (for example, a <code>memory</code> block of facts about the user), and <strong>compaction</strong> summarizes older messages so long conversations stay within the model's context window. Override <code>configureSession</code> to add persistent memory, compaction, search, and skills:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2170.md")
</div>
<p>When <code>configureSession</code> adds context blocks, Think builds the system prompt from those blocks instead of using <code>getSystemPrompt()</code>. Think's <code>this.messages</code> getter reads directly from Session's tree-structured storage.</p>
<p>For the full Session API — context blocks, compaction, search, skills, and multi-session support — refer to the <a href="/agents/runtime/lifecycle/sessions/">Sessions documentation</a>.</p>
<h2 id="package-exports">Package exports</h2>
<table>
<thead>
<tr>
<th>Export</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cloudflare/think</code></td>
<td><code>Think</code>, <code>Session</code>, <code>Workspace</code>, <code>skills</code> namespace</td>
</tr>
<tr>
<td><code>@cloudflare/think/messengers</code></td>
<td>Messenger contracts, Chat SDK bridge, state agent, delivery</td>
</tr>
<tr>
<td><code>@cloudflare/think/messengers/telegram</code></td>
<td>Telegram messenger provider and delivery helpers</td>
</tr>
<tr>
<td><code>@cloudflare/think/workflows</code></td>
<td><code>ThinkWorkflow</code>, <code>step.prompt()</code> — Workflow prompts</td>
</tr>
<tr>
<td><code>@cloudflare/think/tools/workspace</code></td>
<td><code>createWorkspaceTools()</code> — for custom storage backends</td>
</tr>
<tr>
<td><code>@cloudflare/think/tools/execute</code></td>
<td><code>createExecuteTool()</code> — sandboxed code execution via Code Mode</td>
</tr>
<tr>
<td><code>@cloudflare/think/tools/browser</code></td>
<td><code>createBrowserTools()</code> — Chrome DevTools Protocol tools</td>
</tr>
<tr>
<td><code>@cloudflare/think/tools/extensions</code></td>
<td><code>createExtensionTools()</code> — LLM-driven extension loading</td>
</tr>
<tr>
<td><code>@cloudflare/think/extensions</code></td>
<td><code>ExtensionManager</code>, <code>HostBridgeLoopback</code> — extension runtime</td>
</tr>
</tbody>
</table>
<h2 id="dependencies">Dependencies</h2>
<p>Peer dependencies you provide:</p>
<table>
<thead>
<tr>
<th>Package</th>
<th>Required</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agents</code></td>
<td>yes</td>
<td>Cloudflare Agents SDK</td>
</tr>
<tr>
<td><code>ai</code></td>
<td>yes</td>
<td>AI SDK v6</td>
</tr>
<tr>
<td><code>zod</code></td>
<td>yes</td>
<td>Schema validation (v4)</td>
</tr>
<tr>
<td><code>@chat-adapter/telegram</code></td>
<td>optional</td>
<td>Required for Telegram messengers</td>
</tr>
</tbody>
</table>
<p>Bundled with <code>@cloudflare/think</code>:</p>
<table>
<thead>
<tr>
<th>Package</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cloudflare/shell</code></td>
<td><code>Workspace</code> filesystem</td>
</tr>
<tr>
<td><code>@cloudflare/codemode</code></td>
<td>Code execution for <code>createExecuteTool()</code></td>
</tr>
<tr>
<td><code>just-bash</code></td>
<td>Sandboxed shell for the default workspace <code>bash</code> tool</td>
</tr>
</tbody>
</table>
<p>The Agent Skills engine and its script runner live in <a href="/agents/runtime/execution/agent-skills/"><code>agents/skills</code></a>, so skill scripts pull <code>@cloudflare/worker-bundler</code> and <code>just-bash</code> through <code>agents</code>, not Think.</p>
