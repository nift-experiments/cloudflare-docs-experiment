---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/how-to/human-in-the-loop-knowledge-base/
  description: Build an agent that searches a knowledge base and proposes updates to it, with a human approving and able to roll back each write.
  full_title: Human-in-the-loop knowledge base updates · Cloudflare AI Search docs
  head_html: <title>Human-in-the-loop knowledge base updates · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Build an agent that searches a knowledge base and proposes updates to it, with a human approving and able to roll back each write."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/how-to/human-in-the-loop-knowledge-base/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/how-to/human-in-the-loop-knowledge-base/index.md"><meta property="og:title" content="Human-in-the-loop knowledge base updates · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build an agent that searches a knowledge base and proposes updates to it, with a human approving and able to roll back each write."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/how-to/human-in-the-loop-knowledge-base/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/how-to/human-in-the-loop-knowledge-base/#page","headline":"Human-in-the-loop knowledge base updates \u00b7 Cloudflare AI Search docs","description":"Build an agent that searches a knowledge base and proposes updates to it, with a human approving and able to roll back each write.","url":"https://developers.cloudflare.com/ai-search/how-to/human-in-the-loop-knowledge-base/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/how-to/human-in-the-loop-knowledge-base/
  schema: 1
---
<p>This tutorial builds an agent that searches a knowledge base and adds to it, with a human approving every write. Letting an agent modify your data is risky, so each save pauses for approval before it runs, and you can roll back a save that turned out wrong.</p>
<h2 id="what-you-will-build">What you will build</h2>
<p>A Cloudflare Agent that searches an AI Search instance, proposes new documents to index, waits for you to approve each one, and can undo an approved save.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3020.md")
</div></details>
<p>You do not need anything else. The agent provisions its own AI Search instance the first time it runs.</p>
<h2 id="how-it-works">How it works</h2>
<p>The agent uses <a href="/agents/tools/codemode/">Code Mode</a>, a tool-use pattern where the model writes a small program that calls your tools instead of requesting each call separately. A <strong>durable runtime</strong> records every call the program makes, pauses before sensitive calls so a human can approve them, and can compensate applied calls by running a <code>revert</code>. That durable state lives in the Agent's Durable Object, so an approval can wait across requests and hibernation.</p>
<p>You expose AI Search to the runtime through a <strong>connector</strong>: a plain class that turns AI Search operations into methods the model can call. This tutorial gives the model a read-only <code>search</code> method and a <code>saveDocument</code> method that requires approval.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3019.md")
</aside>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>kb-agent</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- kb-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- kb-agent" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare kb-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare kb-agent" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest kb-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest kb-agent" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your application directory:</p>
<pre tabindex="0"><code class="language-sh">cd kb-agent&#10;</code></pre>
<p>Install the dependencies. The <code>ai</code> and <code>zod</code> versions are pinned to the ranges the Agents SDK expects as peer dependencies:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/codemode @cloudflare/ai-chat agents ai@6 workers-ai-provider zod@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/codemode @cloudflare/ai-chat agents ai@6 workers-ai-provider zod@4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/codemode @cloudflare/ai-chat agents ai@6 workers-ai-provider zod@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/codemode @cloudflare/ai-chat agents ai@6 workers-ai-provider zod@4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/codemode @cloudflare/ai-chat agents ai@6 workers-ai-provider zod@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/codemode @cloudflare/ai-chat agents ai@6 workers-ai-provider zod@4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/codemode @cloudflare/ai-chat agents ai@6 workers-ai-provider zod@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/codemode @cloudflare/ai-chat agents ai@6 workers-ai-provider zod@4" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This tutorial uses the AI Search and Worker Loader bindings, which require Wrangler v4. If <code>create-cloudflare</code> set up your project with an earlier version, upgrade it:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i wrangler@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i wrangler@4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add wrangler@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add wrangler@4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add wrangler@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add wrangler@4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add wrangler@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add wrangler@4" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="2-configure-wrangler"><ol start="2">
<li>Configure Wrangler</li>
</ol></h2>
<p>Replace your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> with the following. This adds the AI Search binding, a Workers AI binding for the model, a Worker Loader binding that runs the model's code in an isolated Worker, and the Durable Object that stores the agent's chat history and durable runtime state.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3021.md")
</div>
<p>AI Search has no local emulator, so the binding always talks to the remote service (<code>remote = true</code>). Because of this, you exercise the agent by deploying it rather than with <code>wrangler dev</code>. <code>AIChatAgent</code> persists messages to SQLite, so its class must be listed in <code>new_sqlite_classes</code>.</p>
<h2 id="3-create-the-ai-search-connector"><ol start="3">
<li>Create the AI Search connector</li>
</ol></h2>
<p>Create <code>src/ai-search-connector.ts</code>. The connector calls the AI Search binding directly, so requests stay in-process and no public endpoint is required.</p>
<p>Give the model a read-only <code>search</code> method and a <code>saveDocument</code> method. Because <code>saveDocument</code> writes content, mark it <code>requiresApproval</code> and add a <code>revert</code> so the runtime can roll it back.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3022.md")
</div>
<p>The <code>name()</code> result (<code>aiSearch</code>) becomes the global the model's code calls, so the methods are available as <code>aiSearch.search()</code> and <code>aiSearch.saveDocument()</code>.</p>
<h2 id="4-build-the-agent"><ol start="4">
<li>Build the agent</li>
</ol></h2>
<p>Create <code>src/server.ts</code>. The agent provisions an AI Search instance with <a href="/ai-search/configuration/indexing/hybrid-search/">hybrid search</a> enabled the first time it runs, then creates the Code Mode runtime with the connector and exposes it to the model as a single <code>codemode</code> tool. The <code>@callable()</code> methods let your client list pending approvals and approve, reject, or roll back a write.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3023.md")
</div>
<p>Generate types:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler types&#10;</code></pre>
<h2 id="5-deploy"><ol start="5">
<li>Deploy</li>
</ol></h2>
<p>Because AI Search runs remotely, you deploy the Worker to run the agent.</p>
<p>Log in with your Cloudflare account:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login&#10;</code></pre>
<p>Deploy your Worker to make it accessible on the Internet:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Wrangler prints your Worker's URL, for example <code>https://kb-agent.&lt;your-subdomain&gt;.workers.dev</code>. You use it in the next step.</p>
<h2 id="6-try-the-approval-and-rollback-flow"><ol start="6">
<li>Try the approval and rollback flow</li>
</ol></h2>
<p>The model receives one <code>codemode</code> tool. When you ask it to find and save content, it writes a short program that calls the connector methods:</p>
<pre tabindex="0"><code class="language-js">// The model writes this program. It runs inside the Code Mode sandbox.&#10;async () =&gt; {&#10;	// The read-only search runs immediately.&#10;	const existing = await aiSearch.search({ query: &quot;onboarding steps&quot; });&#10;&#10;	// Only save when the knowledge base has no matching content yet.&#10;	if (existing.chunks.length === 0) {&#10;		// saveDocument requires approval, so this call pauses the program here.&#10;		await aiSearch.saveDocument({&#10;			name: &quot;onboarding.md&quot;,&#10;			content: &quot;# Onboarding\nStep 1: create an account.&quot;,&#10;		});&#10;	}&#10;&#10;	return existing.chunks.length;&#10;};&#10;</code></pre>
<p><code>aiSearch.search()</code> runs immediately. When the program reaches <code>aiSearch.saveDocument()</code>, the runtime records the call as pending and pauses the execution before the upload runs.</p>
<p>Your client sends the chat message that starts the run, then drives the approval with the <code>@callable()</code> methods. The following script uses the <a href="/agents/communication-channels/chat/client-sdk/">Agents SDK client</a> to do both. Save it as <code>client.mjs</code>, set <code>HOST</code> to your deployed Worker, and run it with <code>node client.mjs</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3024.md")
</div>
<p>Each <code>PendingAction</code> from <code>pendingApprovals()</code> includes the <code>executionId</code>, a <code>seq</code> number, and the method and arguments, so you can show the pending document to the user before deciding. The approval methods behave as follows:</p>
<ul>
<li><code>approveExecution(executionId)</code> replays the program and runs the approved <code>saveDocument</code>. The document is queued for indexing and becomes searchable a few seconds later.</li>
<li><code>rejectExecution(executionId, seq)</code> ends the execution without saving.</li>
<li><code>rollbackExecution(executionId)</code> undoes an applied write by running the connector's <code>revert</code>, which deletes the uploaded document.</li>
</ul>
<h2 id="what-you-built">What you built</h2>
<p>Your agent can now:</p>
<ul>
<li>Search the knowledge base with a read-only tool.</li>
<li>Propose new documents through a write tool that pauses for human approval.</li>
<li>Resume the same program after approval, without re-running completed work.</li>
<li>Roll back an approved save by deleting the indexed document.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-create-a-durable-code-mode-runtime-agents-tools-codemode-durable-runtime"><a href="/agents/tools/codemode/durable-runtime/">Create a durable Code Mode runtime</a></h3><p>The full runtime API: rejection, execution history, and reusable snippets.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-ai-search-as-an-agent-tool-agents-tools-ai-search"><a href="/agents/tools/ai-search/">AI Search as an agent tool</a></h3><p>Give a Cloudflare Agent retrieval with AI Search.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-hybrid-search-ai-search-configuration-indexing-hybrid-search"><a href="/ai-search/configuration/indexing/hybrid-search/">Hybrid search</a></h3><p>Combine vector and keyword search with configurable fusion.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-items-workers-binding-ai-search-api-items-workers-binding"><a href="/ai-search/api/items/workers-binding/">Items Workers binding</a></h3><p>Full reference for uploading, listing, and deleting documents.</p></div>
