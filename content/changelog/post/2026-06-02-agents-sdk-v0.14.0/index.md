---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-02-agents-sdk-v0.14.0/
  description: New updates and improvements at Cloudflare.
  full_title: 'Agents SDK v0.14.0: Agent Skills, messengers, scheduled tasks, Workflows, and hardened chat recovery · Changelog'
  head_html: '<title>Agents SDK v0.14.0: Agent Skills, messengers, scheduled tasks, Workflows, and hardened chat recovery · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-02-agents-sdk-v0.14.0/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Agents SDK v0.14.0: Agent Skills, messengers, scheduled tasks, Workflows, and hardened chat recovery · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-02-agents-sdk-v0.14.0/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-02-agents-sdk-v0.14.0/#page","headline":"Agents SDK v0.14.0: Agent Skills, messengers, scheduled tasks, Workflows, and hardened chat recovery \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-02-agents-sdk-v0.14.0/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-02-agents-sdk-v0.14.0/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 2, 2026</time><h2 id="post-title">Agents SDK v0.14.0: Agent Skills, messengers, scheduled tasks, Workflows, and hardened chat recovery</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> adds four new ways to build with <code>@cloudflare/think</code>: on-demand Agent Skills, chat messengers (starting with Telegram), declarative scheduled tasks, and durable reasoning steps inside Workflows. This release also significantly hardens durable chat recovery, so turns reliably ride through deploys, evictions, and stalled model streams in production.</p>
<h4 id="agent-skills-experimental">Agent Skills (experimental)</h4>
<p>Give an agent a catalog of on-demand instructions, resources, and scripts. A skill source adds a catalog to the system prompt, and the model activates a skill only when a task matches — so a large library of capabilities does not bloat every prompt.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17667.md")</div>
<p>The <code>agents:skills</code> import bundles a local <code>./skills</code> directory through the Agents Vite plugin (one directory per skill, each with a <code>SKILL.md</code>). Skills can also load from R2 or a manifest. When skills are available, Think exposes <code>activate_skill</code>, <code>read_skill_resource</code>, and an optional <code>run_skill_script</code> tool. Skill loading is resilient: a duplicate or failing source is skipped with a warning instead of breaking the agent.</p>
<p>Agent Skills are <strong>experimental</strong>, and script execution in particular is early. The API may change in a future release. We would love your feedback — tell us what you are building and what is missing in the <a href="https://github.com/cloudflare/agents/discussions">Agents repository</a>.</p>
<h4 id="messengers">Messengers</h4>
<p>Connect a Think agent directly to a chat platform. Think owns the webhook route, conversation routing, durable reply fiber, and streamed delivery back to the provider. Telegram ships as the first provider.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17668.md")</div>
<p>Each Chat SDK thread maps to its own Think sub-agent by default, so group chats and direct messages do not share memory. Multiple bots, custom conversation routing, and custom providers are all supported.</p>
<h4 id="scheduled-tasks">Scheduled tasks</h4>
<p>Declare recurring, timezone-aware prompts and handlers with a typed domain-specific language (DSL). Think reconciles the declarations on startup and re-arms the next occurrence after each run, backed by durable idempotent submissions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17669.md")</div>
<h4 id="think-workflows">Think Workflows</h4>
<p>Run a model-driven reasoning step inside a Cloudflare Workflow with <code>ThinkWorkflow</code> and <code>step.prompt()</code>, with durable typed structured output, long waits, and approval gates.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17670.md")</div>
<h4 id="production-hardening-for-durable-chat-recovery">Production hardening for durable chat recovery</h4>
<p>Durable chat turns have always been designed to survive a mid-turn deploy or Durable Object eviction. This release is a major hardening pass on that machinery for production.</p>
<ul>
<li><strong>Better recovery during deploys.</strong> Turns now ride through continuous deploys and evictions without losing completed work or re-running tools that already ran.</li>
<li><strong>A live &quot;recovering…&quot; signal.</strong> <code>useAgentChat</code> exposes a new <code>isRecovering</code> flag, so a recovering turn shows progress instead of looking frozen. Most UIs render <code>isStreaming || isRecovering</code> as &quot;busy&quot;.</li>
<li><strong>Stalled streams recover.</strong> Set <code>chatStreamStallTimeoutMs</code> to route a hung provider stream into the same recovery path instead of leaving an infinite spinner.</li>
<li><strong>Sub-agents re-attach.</strong> On parent recovery, an in-flight <code>agentTool()</code> child is re-attached to its result rather than abandoned and re-run, so long-running children no longer lose work under deploys.</li>
</ul>
<h4 id="mcp-transport-improvements">MCP transport improvements</h4>
<ul>
<li><strong>Resumable streams</strong> — In-flight tool calls over Server-Sent Events (SSE) survive a dropped connection. Clients reconnect with <code>Last-Event-ID</code> and replay anything they missed.</li>
<li><strong>Readable server IDs</strong> — <code>addMcpServer</code> accepts an optional <code>id</code>, so tools surface as readable keys (for example <code>tool_github_create_pull_request</code>) instead of opaque connection IDs.</li>
<li><strong>Better handling of concurrent requests</strong> — Overlapping JSON-RPC requests are now correctly correlated to their responses across the HTTP and RPC transports.</li>
</ul>
<h4 id="other-improvements">Other improvements</h4>
<ul>
<li><strong>Compaction</strong> — A <code>Session</code>'s <code>tokenCounter</code> now also drives the compaction boundary decision (&quot;what to compress&quot;), not just the fire/no-fire trigger.</li>
<li><strong><code>@cloudflare/worker-bundler</code></strong> — Adds a <code>virtualModules</code> option to <code>createWorker</code> to provide in-memory module source during bundling.</li>
<li><strong>Client-tool continuations</strong> — Parallel tool results now coalesce into a single continuation, immediate resume requests attach to the pending continuation, and server-side <code>needsApproval</code> continuations resume reliably after approval.</li>
</ul>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/runtime/">Agents API reference</a> and <a href="/agents/communication-channels/chat/chat-agents/">Chat agents documentation</a> for more information.</p>
</div></article></div>
