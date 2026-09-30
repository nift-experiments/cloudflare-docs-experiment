---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/browser/
  description: Give Agents full Chrome DevTools Protocol access to inspect pages, scrape data, and capture screenshots with Browser Run.
  full_title: Browser · Cloudflare Agents docs
  head_html: <title>Browser · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Give Agents full Chrome DevTools Protocol access to inspect pages, scrape data, and capture screenshots with Browser Run."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/browser/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/browser/index.md"><meta property="og:title" content="Browser · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Give Agents full Chrome DevTools Protocol access to inspect pages, scrape data, and capture screenshots with Browser Run."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/browser/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/browser/#page","headline":"Browser \u00b7 Cloudflare Agents docs","description":"Give Agents full Chrome DevTools Protocol access to inspect pages, scrape data, and capture screenshots with Browser Run.","url":"https://developers.cloudflare.com/agents/tools/browser/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/browser/
  schema: 1
---
<p>Agents can use <a href="/browser-run/">Browser Run</a> to inspect and interact with web pages through the <a href="/browser-run/cdp/">Chrome DevTools Protocol (CDP)</a>. <span class="nb-badge">Beta</span> Browser tools are useful when an agent needs to understand rendered pages, capture screenshots, debug frontend behavior, or extract information that is only available after JavaScript runs.</p>
<p>Instead of a fixed set of browser actions (click, screenshot, navigate), the model writes code that runs CDP commands against a live browser session through the <code>cdp</code> connector — accessing all domains, commands, events, and types in the protocol. Executions use the <a href="/agents/tools/codemode/how-it-works/">durable Code Mode runtime</a>, so a run can pause for approval and resume with its browser session intact.</p>
<p>Use browser tools when you want an agent to:</p>
<ul>
<li>Open and inspect live web pages.</li>
<li>Capture screenshots or page state.</li>
<li>Scrape rendered content that is not present in static HTML.</li>
<li>Debug frontend issues using CDP commands.</li>
<li>Combine page inspection with other tools, such as RAG or Sandbox.</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>Browser Run provides isolated browser sessions that agents can control with CDP. The agent can navigate pages, evaluate JavaScript, read DOM state, capture screenshots, and inspect network or console output.</p>
<p>Because browser sessions run outside the Worker isolate, use them for work that needs a real browser environment rather than lightweight HTTP fetches.</p>
<h2 id="basic-pattern">Basic pattern</h2>
<p>Create browser tools with the Browser Run and Worker Loader bindings, then pass those tools to your model call.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1846.md")
</div>
<p>Browser tools must be created from inside a Durable Object (such as an Agent) — the durable runtime facet and the session store live on its <code>ctx</code>. The helper exposes one durable CDP tool plus stateless Quick Action tools when a <code>browser</code> binding is present:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>browser_execute</code></td>
<td>Run sandboxed code against a live browser over CDP — screenshots, DOM reads, JavaScript evaluation, and more.</td>
</tr>
<tr>
<td><code>browser_markdown</code></td>
<td>Read a page or raw HTML as Markdown.</td>
</tr>
<tr>
<td><code>browser_extract</code></td>
<td>Extract structured data from a page with AI.</td>
</tr>
<tr>
<td><code>browser_links</code></td>
<td>List links on a page.</td>
</tr>
<tr>
<td><code>browser_scrape</code></td>
<td>Scrape specific elements by CSS selector.</td>
</tr>
</tbody>
</table>
<p>To discover protocol surface, the model calls <code>cdp.spec()</code> (the live, normalized CDP protocol description) or the runtime's built-in <a href="/agents/tools/codemode/api-reference/#sandbox-codemode-api"><code>codemode.search()</code> and <code>codemode.describe()</code></a>.</p>
<h2 id="configuration">Configuration</h2>
<p>Add the Browser Run and Worker Loader bindings to <code>wrangler.jsonc</code>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1847.md")
</div>
<p>The durable runtime behind the tool lives in a Durable Object facet, so your Worker entry must export it (the <code>@cloudflare/codemode/vite</code> plugin does this automatically):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1848.md")
</div>
<p><code>agents/browser</code> re-exports the Code Mode runtime for browser tool setups. Code Mode-specific examples can also import <code>CodemodeRuntime</code> from <code>@cloudflare/codemode</code>.</p>
<h2 id="session-lifecycle">Session lifecycle</h2>
<p>By default each execution gets a fresh browser session, torn down when the run ends (<code>one-shot</code>). Pass a <code>session</code> option for two more modes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1849.md")
</div>
<ul>
<li><strong><code>one-shot</code></strong> (default) — fresh session per execution; deterministic cleanup when the execution reaches a terminal status.</li>
<li><strong><code>reuse</code></strong> — a named shared session that persists across executions until explicitly closed or swept.</li>
<li><strong><code>dynamic</code></strong> — starts one-shot; the model can promote the session with <code>cdp.startSession()</code> (for example, after logging in to a page) so later executions continue in the same browser.</li>
</ul>
<p>In <code>reuse</code> and <code>dynamic</code> modes the sandbox additionally gets <code>cdp.startSession()</code>, <code>cdp.sessionInfo()</code>, <code>cdp.closeSession()</code>, and <code>cdp.resetSession()</code>.</p>
<p>Sessions are tracked durably in the Durable Object's storage, so they survive hibernation and approval pauses — a run that pauses for human approval resumes with its browser session, tabs, and cookies intact. If Browser Run expires the session while a pause waits, the resume surfaces a clear error and the model starts over.</p>
<p>For host-side wiring (session inspection, cleanup, reclaiming stale pauses), use <code>createBrowserRuntime</code>, which returns <code>{ runtime, connector, tools }</code>. Call <code>connector.sweep()</code> from a scheduled task to reclaim expired or stale sessions, and <code>runtime.expirePaused()</code> to reject stale never-approved pauses.</p>
<h2 id="quick-actions">Quick actions</h2>
<p>Use <code>browser_execute</code> for interactive, multi-step automation. For one-shot browsing tasks, use <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a>. Quick Actions need only the <code>browser</code> binding, so they do not need a Worker Loader or sandbox.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1850.md")
</div>
<p>By default, <code>createBrowserTools</code> and <code>createBrowserRuntime</code> include Quick Action tools whenever a <code>browser</code> binding is present. Pass <code>quickActions: false</code> to keep only <code>browser_execute</code>, or pass <code>quickActions: { actions, maxChars, options }</code> to configure the stateless tools.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1851.md")
</div>
<p>Every Quick Action result is bounded to <code>maxChars</code> to protect the model context window while preserving the result shape. Host-supplied request options, such as <code>cookies</code>, <code>authenticate</code>, <code>gotoOptions</code>, and <code>viewport</code>, are passed once through <code>options</code> and are not exposed to the model.</p>
<p>Quick Actions require a Worker <code>compatibility_date</code> of <code>2026-03-24</code> or later and <code>remote: true</code> on the browser binding for local <code>wrangler dev</code>.</p>
<h2 id="live-view-and-human-in-the-loop">Live View and human-in-the-loop</h2>
<p><a href="/browser-run/features/live-view/">Live View</a> lets a human watch or control a running browser session in real time. Use it for human-in-the-loop steps such as login, MFA, CAPTCHA, or sensitive input.</p>
<p>Because the Code Mode runtime can pause a run with the browser session intact, a handoff follows this pattern:</p>
<ol>
<li>The model calls <code>cdp.getLiveViewUrl()</code> to get a link to the current tab.</li>
<li>The agent surfaces the link to the user.</li>
<li>The model makes an approval-gated call, so the run pauses durably.</li>
<li>After approval, the run resumes against the same session.</li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1852.md")
</div>
<p>Pass <code>mode: &quot;tab&quot;</code> for an interactive page view, or <code>mode: &quot;devtools&quot;</code> for the full DevTools inspector. The URL is valid for about five minutes. Call <code>cdp.getLiveViewUrl()</code> again to create a fresh URL.</p>
<p>From the host side, <code>connector.liveView()</code> returns Live View URLs for the shared session's tabs. Each tab includes its current <code>pageUrl</code>, so an agent UI can label tabs and skip blank or internal pages.</p>
<h2 id="session-recording">Session recording</h2>
<p><a href="/browser-run/features/session-recording/">Session recording</a> captures a Browser Run session as structured rrweb events. Use recordings to audit or debug what an autonomous browser run did after the session closes.</p>
<p>Opt in per session with <code>recording: true</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1853.md")
</div>
<p>A recording is finalized after the session closes. Capture the session ID while the session is alive, then fetch the recording from the Browser Rendering REST API:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1854.md")
</div>
<p>Recordings are retained for 30 days and capped at two hours per session. Be deliberate with recording on shared <code>reuse</code> and <code>dynamic</code> sessions because the recording spans the full session lifetime.</p>
<h2 id="cdp-connector-api">CDP connector API</h2>
<p>Inside <code>browser_execute</code>, the <code>cdp</code> namespace provides the following methods. All methods take a single object argument:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cdp.send({ method, params?, sessionId?, timeoutMs? })</code></td>
<td>Send a CDP command and wait for the response.</td>
</tr>
<tr>
<td><code>cdp.attachToTarget({ targetId, timeoutMs? })</code></td>
<td>Attach to a target; returns <code>{ sessionId }</code> for page-scoped <code>send</code> calls.</td>
</tr>
<tr>
<td><code>cdp.spec()</code></td>
<td>The searchable, normalized CDP protocol spec.</td>
</tr>
<tr>
<td><code>cdp.getDebugLog({ limit? })</code></td>
<td>Recent CDP traffic (sends, receives, warnings) for this execution's connection.</td>
</tr>
<tr>
<td><code>cdp.clearDebugLog()</code></td>
<td>Clear the debug log buffer.</td>
</tr>
<tr>
<td><code>cdp.getLiveViewUrl({ targetId?, mode? })</code></td>
<td>Create a Live View URL for a tab.</td>
</tr>
<tr>
<td><code>cdp.startSession()</code> <em>(reuse/dynamic)</em></td>
<td>Promote or ensure the shared session; returns its info.</td>
</tr>
<tr>
<td><code>cdp.sessionInfo()</code> <em>(reuse/dynamic)</em></td>
<td>Shared session info, or <code>null</code>.</td>
</tr>
<tr>
<td><code>cdp.closeSession()</code> <em>(reuse/dynamic)</em></td>
<td>Close the shared session.</td>
</tr>
<tr>
<td><code>cdp.resetSession()</code> <em>(reuse/dynamic)</em></td>
<td>Close and replace the shared session.</td>
</tr>
</tbody>
</table>
<p>Every <code>cdp.*</code> call is recorded in the runtime's durable log. If a run pauses (for approval) or the sandbox aborts, resuming replays the log and continues — so connector calls must be sequential and deterministic. Model code must not <code>Promise.all</code> CDP calls (the tool instructions enforce this), and the returned <code>sessionId</code> is a stable session handle that stays valid across pause/resume reconnects.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1845.md")
</aside>
<h2 id="build-a-browser-agent">Build a browser agent</h2>
<p>For a complete walkthrough, including Browser Run setup, tool definitions, and screenshot capture, use the browser agent example.</p>
<div class="nb-card nb-link-card"><h3 id="card-browser-agent-agents-examples-browser-agent"><a href="/agents/examples/browser-agent/">Browser agent</a></h3><p>Build an agent that can browse the web, inspect pages, capture screenshots, and debug frontend issues.</p></div>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-browser-run-browser-run"><a href="/browser-run/">Browser Run</a></h3><p>Run browser automation on Cloudflare.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-chrome-devtools-protocol-browser-run-cdp"><a href="/browser-run/cdp/">Chrome DevTools Protocol</a></h3><p>Use CDP commands, events, and types with Browser Run.</p></div>
