<h1 id="changelog">Changelog</h1>

<h2 id="control-which-hostnames-browser-run-sessions-can-access"><a href="/changelog/post/2026-09-14-guardrails/">Control which hostnames Browser Run sessions can access</a></h2>
<p><em>2026-09-14</em></p>
<p><a href="/browser-run/">Browser Run</a> now supports <a href="/browser-run/features/guardrails/">guardrails</a>, which limit a browser session's HTTP and HTTPS requests to permitted hostnames.</p>
<p>Use guardrails when you need to:</p>
<ul>
<li>Keep a browser workflow limited to a specific website and its subdomains.</li>
<li>Load only known third-party APIs, scripts, images, and fonts.</li>
<li>Generate a screenshot or PDF from HTML you provide while preventing it from loading external content.</li>
</ul>
<p>Set guardrails when starting a session with Puppeteer, Playwright, or the REST API. With a browser binding named <code>MYBROWSER</code>, pass <code>guardrails</code> when launching Puppeteer:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17700.md")</div>
<p>In addition to session guardrails, Browser Run now supports a read-only mode for <a href="/browser-run/features/live-view/">Live View</a>. Live View lets you watch and interact with an active Browser Run session in real time. A read-only link lets someone watch without clicking, typing, navigating, or running JavaScript.</p>
<p>To create a read-only link, set <code>{ mode: &quot;readonly&quot; }</code> when generating the Live View URL. This setting affects only the person using that link. The session's hostname restrictions remain unchanged.</p>
<p>Refer to the <a href="/browser-run/features/guardrails/">guardrails documentation</a> for more information.</p>


<h2 id="crawl-endpoint-now-respects-the-content-signals-use-directive"><a href="/changelog/post/2026-08-31-crawl-content-use/">Crawl endpoint now respects the Content Signals `use` directive</a></h2>
<p><em>2026-08-31</em></p>
<p>The <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code></a> endpoint now respects the <code>use</code> directive of the <a href="https://contentsignals.org/">Content Signals</a> standard, letting site owners express the maximum level at which their content may be used.</p>
<p>You can declare your intended level with the new <code>contentUse</code> parameter. Allowed values, from least to most permissive, are <code>reference</code> and <code>full</code>, and the default is <code>full</code>. If a target site's <code>robots.txt</code> sets a <code>use</code> level that is more restrictive than your declared <code>contentUse</code>, the crawl request is rejected with a <code>400</code> error.</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;contentUse&quot;: &quot;reference&quot;,&#10;    &quot;formats&quot;: [&quot;markdown&quot;]&#10;  }&#x27;&#10;</code></pre>
<p>For more information, refer to <a href="/browser-run/quick-actions/crawl-endpoint/#content-signals">Content Signals</a> in the <code>/crawl</code> endpoint documentation.</p>


<h2 id="run-more-headless-browsers-concurrently-with-browser-run"><a href="/changelog/post/2026-08-20-limits-increase/">Run more headless browsers concurrently with Browser Run</a></h2>
<p><em>2026-08-20</em></p>
<p><a href="/browser-run/">Browser Run</a> lets you automate headless browsers on Cloudflare's global network. Run full browser sessions for interactive workflows, or use <a href="/browser-run/quick-actions/">Quick Actions</a> for one-request tasks such as screenshots, PDFs, and capturing page content.</p>
<p>If you are on the <a href="/workers/platform/pricing/">Workers Paid plan</a>, your default <a href="/browser-run/limits/#workers-paid">limits</a> are now higher:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous</th>
<th>New</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concurrent browsers</td>
<td>120</td>
<td><strong>200</strong></td>
</tr>
<tr>
<td>New browser instances / second</td>
<td>1</td>
<td><strong>3</strong></td>
</tr>
<tr>
<td>Quick Actions requests / second</td>
<td>10</td>
<td><strong>30</strong></td>
</tr>
</tbody>
</table>
<p>You can now run hundreds of browser sessions in parallel, launch new browsers faster, and process three times as many <a href="/browser-run/quick-actions/">Quick Actions</a> per second. These published limits are defaults, not maximums. If your workload needs more more concurrent browsers, <a href="https://forms.gle/CdueDKvb26mTaepa9">request higher limits</a>.</p>


<h2 id="introducing-kitesurf-an-agent-first-browser-on-browser-run"><a href="/changelog/post/2026-08-06-kitesurf/">Introducing Kitesurf, an agent-first browser on Browser Run</a></h2>
<p><em>2026-08-06</em></p>
<p><a href="/browser-run/kitesurf/">Kitesurf</a> is Cloudflare's new stateless, highly scalable browser that runs entirely on top of <a href="/workers/">Workers</a> and is designed for AI agents. It is available for free while in beta.</p>
<p>Compared to Chromium, Kitesurf uses 3–7× less CPU and memory for common agentic tasks like screenshots and HTML extraction, so you can run more sessions and scale better for bursty, AI-driven workloads.</p>
<p>Your existing clients already work. To opt in, add the <code>browser=kitesurf</code> parameter to any Browser Run <a href="/browser-run/cdp/">CDP</a> or <a href="/browser-run/quick-actions/">Quick Action</a> endpoint:</p>
<pre><code class="language-sh">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-run/screenshot?browser=kitesurf&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.png&quot;&#10;</code></pre>
<p>You can also explore Kitesurf without writing any code in the <a href="https://kitesurf.cloudflare.app/">public playground</a>.</p>
<p>For more information, refer to the <a href="/browser-run/kitesurf/">Kitesurf documentation</a> and the <a href="https://blog.cloudflare.com/kitesurf">blog announcement</a>.</p>


<h2 id="browser-run-adds-a-playground-to-the-cloudflare-dashboard"><a href="/changelog/post/2026-07-31-br-dashboard-playground/">Browser Run adds a Playground to the Cloudflare dashboard</a></h2>
<p><em>2026-07-31</em></p>
<p><a href="/browser-run/">Browser Run</a> now includes a Playground in the Cloudflare dashboard. Use it to try Quick Actions against a live browser without creating a Worker, installing an SDK, or deploying code first.</p>
<p>The Playground helps you test a target URL or raw HTML input, tune viewport and page-load settings, preview the output, and copy working code for the same request.</p>
<p><img src="/images/browser-run/playground.png" alt="Browser Run Playground in the Cloudflare dashboard showing a generated screenshot preview and output settings" /></p>
<p>With the Playground, you can:</p>
<ul>
<li>Capture visuals as <a href="/browser-run/quick-actions/screenshot-endpoint/">screenshots</a> or <a href="/browser-run/quick-actions/pdf-endpoint/">PDFs</a>.</li>
<li>Generate multiple output formats in one request with the <a href="/browser-run/quick-actions/snapshot/">snapshot endpoint</a>.</li>
<li>Extract <a href="/browser-run/quick-actions/content-endpoint/">HTML</a>, <a href="/browser-run/quick-actions/markdown-endpoint/">Markdown</a>, <a href="/browser-run/quick-actions/links-endpoint/">links</a>, or <a href="/browser-run/quick-actions/scrape-endpoint/">scraped data</a>.</li>
<li>Extract <a href="/browser-run/quick-actions/json-endpoint/">structured data with AI</a> using a prompt and optional JSON Schema.</li>
</ul>
<p>You can also configure desktop, laptop, tablet, mobile, or custom viewport sizes, set browser scale, choose page-load conditions, set timeouts, and wait for selectors before running a request.</p>
<p>Select <strong>Show Code</strong> to generate the same request as cURL, TypeScript SDK, Python, or Workers Binding code. For example, a screenshot request can be copied as a Workers Binding call:</p>
<pre><code class="language-ts">interface Env {&#10;	BROWSER: BrowserRun;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env): Promise&lt;Response&gt; {&#10;		return await env.BROWSER.quickAction(&quot;screenshot&quot;, {&#10;			url: &quot;https://developers.cloudflare.com&quot;,&#10;			viewport: {&#10;				width: 1920,&#10;				height: 1080,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Requests made in the Playground incur <a href="/browser-run/pricing/">Browser Run charges</a>. AI extraction also incurs Workers AI charges.</p>
<p>To try the Playground, go to <strong>Browser Run</strong> in the Cloudflare dashboard and select <strong>Playground</strong>.</p>
<div class="nb-dash-button"></div>
<p>For more information, refer to the <a href="/browser-run/quick-actions/">Quick Actions documentation</a>.</p>


<h2 id="browser-run-adds-structured-handoff-for-human-in-the-loop"><a href="/changelog/post/2026-07-28-human-in-the-loop/">Browser Run adds structured handoff for Human in the Loop</a></h2>
<p><em>2026-07-28</em></p>
<p><a href="/browser-run/">Browser Run</a> now supports structured handoff for <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a> workflows. Using Cloudflare-specific <a href="/browser-run/features/human-in-the-loop/#cloudflare-cdp-commands">CDP commands</a>, your agent can signal that it needs help, a human steps in through <a href="/browser-run/features/live-view/">Live View</a> to handle the task, and the agent resumes once the work is done.</p>
<p>For agents running multi-step browser workflows, a single login wall or unexpected prompt can fail the entire run. Previously, scripts had to manage human intervention manually by sharing a Live View URL and polling for completion. Structured handoff replaces this with a formal pause-and-resume flow.</p>
<p>The following example requests human intervention for a login page and waits for the human to finish before continuing:</p>
<pre><code class="language-js">const cdp = await page.createCDPSession();&#10;&#10;// Get Live View URL for the human operator&#10;const { devtoolsFrontendUrl } = await cdp.send(&quot;Cloudflare.getLiveView&quot;, {&#10;	mode: &quot;tab&quot;,&#10;});&#10;console.log(`Human input needed: ${devtoolsFrontendUrl}`);&#10;&#10;// Request human intervention and wait for completion&#10;const handoffComplete = new Promise((resolve) =&gt; {&#10;	cdp.once(&quot;Cloudflare.handoffComplete&quot;, resolve);&#10;});&#10;&#10;await cdp.send(&quot;Cloudflare.handoff&quot;, {&#10;	instructions: &quot;Please log in with your credentials&quot;,&#10;	timeout: 600000,&#10;});&#10;&#10;const result = await handoffComplete;&#10;console.log(result.success ? &quot;Handoff complete&quot; : `Failed: ${result.reason}`);&#10;</code></pre>
<p>Refer to the <a href="/browser-run/features/human-in-the-loop/">Human in the Loop documentation</a> for the full API reference, examples, and best practices.</p>


<h2 id="new-browser-run-endpoint-for-accessibility-trees"><a href="/changelog/post/2026-07-07-browser-run-accessibility-tree-endpoint/">New Browser Run endpoint for accessibility trees</a></h2>
<p><em>2026-07-07</em></p>
<p><a href="/browser-run/">Browser Run</a> now supports a standalone <code>/accessibilityTree</code> endpoint, giving agent and automation workflows direct access to the browser's accessibility tree for a rendered webpage.</p>
<p>An accessibility tree is the browser's structured view of a rendered page: roles, names, states, values, and hierarchy. It is useful for accessibility tooling, but also for AI agents and automation workflows that need page structure without the noise of raw HTML or the cost of screenshots.</p>
<p>For AI agents, this means less inference from pixels and less parsing HTML. You can provide the page structure directly, helping agents identify available elements and determine which actions they can take.</p>
<p>With the new <code>/accessibilityTree</code> endpoint, you can request the accessibility tree directly when you only need the semantic structure of a page. If you need multiple page formats in a single API call, you can use the <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code></a> endpoint, which also returns Markdown, HTML, and screenshots.</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-run/accessibilityTree&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;accessibilityTree&quot;: {&#10;			&quot;role&quot;: &quot;RootWebArea&quot;,&#10;			&quot;name&quot;: &quot;Example Domain&quot;,&#10;			&quot;children&quot;: [&#10;				{&#10;					&quot;role&quot;: &quot;heading&quot;,&#10;					&quot;name&quot;: &quot;Example Domain&quot;,&#10;					&quot;level&quot;: 1&#10;				},&#10;				{&#10;					&quot;role&quot;: &quot;link&quot;,&#10;					&quot;name&quot;: &quot;Learn more&quot;&#10;				}&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use <code>interestingOnly</code> to return only semantically meaningful nodes, or <code>root</code> to capture the accessibility tree for a specific subtree.</p>
<p>Refer to the <a href="/browser-run/quick-actions/accessibility-tree-endpoint/"><code>/accessibilityTree</code> documentation</a> for usage examples and supported parameters.</p>


<h2 id="new-formats-parameter-for-the-browser-run-snapshot-endpoint"><a href="/changelog/post/2026-06-11-browser-run-snapshot-formats/">New formats parameter for the Browser Run /snapshot endpoint</a></h2>
<p><em>2026-06-11</em></p>
<p><a href="/browser-run/">Browser Run</a>'s <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code> endpoint</a> now supports a <code>formats</code> parameter that lets you return multiple page formats in a single API call. Previously, <code>/snapshot</code> returned only HTML content and a screenshot. You can now also include Markdown and the accessibility tree in the same response.</p>
<p>These formats are particularly useful for AI agent workflows:</p>
<ul>
<li>Markdown provides a token-efficient representation of page content that LLMs can process directly, without parsing HTML markup.</li>
<li>The accessibility tree provides a structured representation of a page's elements, including roles, labels, and hierarchy, helping LLMs understand page structure and navigate its contents.</li>
</ul>
<p>The following example returns a screenshot, Markdown, and the accessibility tree in one call:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17699.md")
</div></div>
<p>You must request at least two formats. If you only need one, use the respective single-format endpoint such as <a href="/browser-run/quick-actions/screenshot-endpoint/"><code>/screenshot</code></a> or <a href="/browser-run/quick-actions/markdown-endpoint/"><code>/markdown</code></a>.</p>
<p>Refer to the <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code> documentation</a> for the full list of accepted values.</p>


<h2 id="use-browser-run-quick-actions-directly-from-workers"><a href="/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/">Use Browser Run Quick Actions directly from Workers</a></h2>
<p><em>2026-05-28</em></p>
<p>You can now call <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a> directly from a <a href="/workers/">Cloudflare Worker</a> using the <code>quickAction()</code> method on the browser binding. This simplifies how Workers interact with Browser Run by removing the need for API tokens or external HTTP requests. Your Worker communicates with Browser Run directly over Cloudflare's network, resulting in simpler code and lower latency.</p>
<p>With the <code>quickAction()</code> method you can:</p>
<ul>
<li><a href="/browser-run/quick-actions/screenshot-endpoint/">Capture screenshots</a> from URLs or HTML</li>
<li><a href="/browser-run/quick-actions/pdf-endpoint/">Generate PDFs</a> with custom styling, headers, and footers</li>
<li><a href="/browser-run/quick-actions/content-endpoint/">Extract HTML content</a> from fully rendered pages</li>
<li><a href="/browser-run/quick-actions/markdown-endpoint/">Convert pages to Markdown</a></li>
<li><a href="/browser-run/quick-actions/json-endpoint/">Extract structured JSON</a> using AI</li>
<li><a href="/browser-run/quick-actions/scrape-endpoint/">Scrape elements</a> with CSS selectors</li>
<li><a href="/browser-run/quick-actions/links-endpoint/">Get all links</a> from a page</li>
<li><a href="/browser-run/quick-actions/snapshot/">Capture snapshots</a> (HTML + screenshot in one request)</li>
</ul>
<p>To get started, add a browser binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17694.md")</div>
<p>Then call any Quick Action directly from your Worker. For example, to capture a screenshot:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17695.md")</div>
<p>The <code>quickAction()</code> method requires a compatibility date of <code>2026-03-24</code> or later.</p>
<p>For setup instructions and the full list of available actions, refer to <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a>.</p>


<h2 id="browser-rendering-is-now-browser-run"><a href="/changelog/post/2026-04-15-br-rename/">Browser Rendering is now Browser Run</a></h2>
<p><em>2026-04-15T12:00:00+00:00</em></p>
<p>We are renaming Browser Rendering to <strong><a href="/browser-run/">Browser Run</a></strong>. The name Browser Rendering never fully captured what the product does. Browser Run lets you run full browser sessions on Cloudflare's global network, drive them with code or AI, record and replay sessions, crawl pages for content, debug in real time, and let humans intervene when your agent needs help.</p>
<p>Along with the rename, we have increased limits for Workers Paid plans and redesigned the Browser Run dashboard.</p>
<p>We have 4x-ed concurrency limits for Workers Paid plan users:</p>
<ul>
<li><strong>Concurrent browsers per account</strong>: 30 → <strong>120 per account</strong></li>
<li><strong>New browser instances</strong>: 30 per minute → <strong>1 per second</strong></li>
<li><strong>REST API rate limits</strong>: recently increased from <a href="/changelog/post/2026-03-04-br-rest-api-limit-increase/">3 to 10 requests per second</a></li>
</ul>
<p>Rate limits across the <a href="/browser-run/limits/">limits page</a> are now expressed in per-second terms, matching how they are enforced. No action is needed to benefit from the higher limits.</p>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/workers/browser-run">redesigned dashboard</a> now shows every request in a single Runs tab, not just browser sessions but also quick actions like screenshots, PDFs, markdown, and crawls. Filter by endpoint, view target URLs, status, and duration, and expand any row for more detail.</p>
<p><img src="/images/browser-run/BRdashboardredesign.png" alt="Browser Run dashboard Runs tab with browser sessions and quick actions visible in one list, and an expanded crawl job showing its progress" /></p>
<p>We are also shipping several new features:</p>
<ul>
<li><strong><a href="/changelog/post/2026-04-15-br-observability/">Live View, Human in the Loop, and Session Recordings</a></strong> - See what your agent is doing in real time, let humans step in when automation hits a wall, and replay any session after it ends.</li>
<li><strong><a href="/changelog/post/2026-04-15-br-webmcp/">WebMCP</a></strong> - Websites can expose structured tools for AI agents to discover and call directly, replacing slow screenshot-analyze-click loops.</li>
</ul>
<p>For the full story, read our Agents Week blog <a href="https://blog.cloudflare.com/browser-run-for-ai-agents">Browser Run: Give your agents a browser</a>.</p>


<h2 id="browser-run-adds-live-view-human-in-the-loop-and-session-recordings"><a href="/changelog/post/2026-04-15-br-observability/">Browser Run adds Live View, Human in the Loop, and Session Recordings</a></h2>
<p><em>2026-04-15T11:00:00+00:00</em></p>
<p>When browser automation fails or behaves unexpectedly, it can be hard to understand what happened. We are shipping three new features in <a href="/browser-run/">Browser Run</a> (formerly Browser Rendering) to help:</p>
<ul>
<li><strong><a href="/browser-run/features/live-view/">Live View</a></strong> for real-time visibility</li>
<li><strong><a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a></strong> for human intervention</li>
<li><strong><a href="/browser-run/features/session-recording/">Session Recordings</a></strong> for replaying sessions after they end</li>
</ul>
<h4 id="2026-04-15-br-observability-live-view">Live View</h4>
<p><a href="/browser-run/features/live-view/">Live View</a> lets you see what your agent is doing in real time. The page, DOM, console, and network requests are all visible for any active browser session. Access Live View from the Cloudflare dashboard, via the hosted UI at <code>live.browser.run</code>, or using native Chrome DevTools.</p>
<h4 id="2026-04-15-br-observability-human-in-the-loop">Human in the Loop</h4>
<p>When your agent hits a snag like a login page or unexpected edge case, it can hand off to a human instead of failing. With <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>, a human steps into the live browser session through Live View, resolves the issue, and hands control back to the script.</p>
<p>Today, you can step in by opening the Live View URL for any active session. Next, we are adding a handoff flow where the agent can signal that it needs help, notify a human to step in, then hand control back to the agent once the issue is resolved.</p>
<p><img src="/images/browser-run/liveview.gif" alt="Browser Run Human in the Loop demo where an AI agent searches Amazon, selects a product, and requests human help when authentication is needed to buy" /></p>
<h4 id="2026-04-15-br-observability-session-recordings">Session Recordings</h4>
<p><a href="/browser-run/features/session-recording/">Session Recordings</a> records DOM state so you can replay any session after it ends. Enable recordings by passing <code>recording: true</code> when launching a browser. After the session closes, view the recording in the Cloudflare dashboard under <strong>Browser Run</strong> &gt; <strong>Runs</strong>, or retrieve via API using the session ID. Next, we are adding the ability to inspect DOM state and console output at any point during the recording.</p>
<p><img src="/images/browser-run/sessionrecording.gif" alt="Browser Run session recording showing an automated browser navigating the Sentry Shop and adding a bomber jacket to the cart" /></p>
<p>To get started, refer to the documentation for <a href="/browser-run/features/live-view/">Live View</a>, <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>, and <a href="/browser-run/features/session-recording/">Session Recording</a>.</p>


<h2 id="browser-run-adds-webmcp-support"><a href="/changelog/post/2026-04-15-br-webmcp/">Browser Run adds WebMCP support</a></h2>
<p><em>2026-04-15T10:00:00+00:00</em></p>
<p><a href="/browser-run/">Browser Run</a> (formerly Browser Rendering) now supports <a href="https://webmachinelearning.github.io/webmcp/">WebMCP</a> (Web Model Context Protocol), a new browser API from the Google Chrome team.</p>
<p>The Internet was built for humans, so navigating as an AI agent today is unreliable. WebMCP lets websites expose structured tools for AI agents to discover and call directly. Instead of slow screenshot-analyze-click loops, agents can call website functions like <code>searchFlights()</code> or <code>bookTicket()</code> with typed parameters, making browser automation faster, more reliable, and less fragile.</p>
<p><img src="/images/browser-run/webMCP.gif" alt="Browser Run lab session showing WebMCP tools being discovered and executed in the Chrome DevTools console to book a hotel" /></p>
<p>With WebMCP, you can:</p>
<ul>
<li><strong>Discover website tools</strong> - Use <code>navigator.modelContextTesting.listTools()</code> to see available actions on any WebMCP-enabled site</li>
<li><strong>Execute tools directly</strong> - Call <code>navigator.modelContextTesting.executeTool()</code> with typed parameters</li>
<li><strong>Handle human-in-the-loop interactions</strong> - Some tools pause for user confirmation before completing sensitive actions</li>
</ul>
<p>WebMCP requires Chrome beta features. We have an experimental pool with browser instances running Chrome beta so you can test emerging browser features before they reach stable Chrome. To start a WebMCP session, add <code>lab=true</code> to your <code>/devtools/browser</code> request:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/devtools/browser?lab=true&amp;keep_alive=300000&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot;&#10;</code></pre>
<p>Combined with the recently launched <a href="/browser-run/cdp/">CDP endpoint</a>, AI agents can also use WebMCP. Connect an <a href="/browser-run/cdp/mcp-clients/">MCP client</a> to Browser Run via CDP, and your agent can discover and call website tools directly. Here's the same hotel booking demo, this time driven by an AI agent through OpenCode:</p>
<p><img src="/images/browser-run/webMCPagent.gif" alt="Browser Run Live View showing an AI agent navigating a hotel booking site in real time" /></p>
<p>For a step-by-step guide, refer to the <a href="/browser-run/features/webmcp/">WebMCP documentation</a>.</p>


<h2 id="manage-browser-rendering-sessions-with-wrangler-cli"><a href="/changelog/post/2026-04-14-browser-wrangler-commands/">Manage Browser Rendering sessions with Wrangler CLI</a></h2>
<p><em>2026-04-14</em></p>
<p><a href="/browser-run/">Browser Rendering</a> now supports <code>wrangler browser</code> commands, letting you create, manage, and view browser sessions directly from your terminal, streamlining your workflow. Since Wrangler handles authentication, you do not need to pass API tokens in your commands.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler browser create</code></td>
<td>Create a new browser session</td>
</tr>
<tr>
<td><code>wrangler browser close</code></td>
<td>Close a session</td>
</tr>
<tr>
<td><code>wrangler browser list</code></td>
<td>List active sessions</td>
</tr>
<tr>
<td><code>wrangler browser view</code></td>
<td>View a live browser session</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command spins up a browser instance on Cloudflare's network and returns a session URL. Once created, you can connect to the session using any <a href="/browser-run/cdp/">CDP</a>-compatible client like <a href="/browser-run/cdp/puppeteer/">Puppeteer</a>, <a href="/browser-run/cdp/playwright/">Playwright</a>, or <a href="/browser-run/cdp/mcp-clients/">MCP clients</a> to automate browsing, scrape content, or debug remotely.</p>
<pre><code class="language-sh">wrangler browser create&#10;</code></pre>
<p>Use <code>--keepAlive</code> to set the session keep-alive duration (60-600 seconds):</p>
<pre><code class="language-sh">wrangler browser create --keepAlive 300&#10;</code></pre>
<p>The <code>view</code> command auto-selects when only one session exists, or prompts for selection when multiple sessions are available.</p>
<p>All commands support <code>--json</code> for structured output, and because these are CLI commands, you can incorporate them into scripts to automate session management.</p>
<p>For full usage details, refer to the <a href="/browser-run/reference/wrangler-commands/">Wrangler commands documentation</a>.</p>


<h2 id="browser-rendering-adds-chrome-devtools-protocol-cdp-and-mcp-client-support"><a href="/changelog/post/2026-04-10-browser-rendering-cdp-endpoint/">Browser Rendering adds Chrome DevTools Protocol (CDP) and MCP client support</a></h2>
<p><em>2026-04-10</em></p>
<p><a href="/browser-run/">Browser Rendering</a> now exposes the <a href="/browser-run/cdp/">Chrome DevTools Protocol (CDP)</a>, the low-level protocol that powers browser automation. The growing ecosystem of CDP-based agent tools, along with existing CDP automation scripts, can now use Browser Rendering directly.</p>
<p>Any CDP-compatible client, including <a href="/browser-run/cdp/puppeteer/">Puppeteer</a> and <a href="/browser-run/cdp/playwright/">Playwright</a>, can connect from any environment, whether that is <a href="/workers/">Cloudflare Workers</a>, your local machine, or a cloud environment. All you need is your Cloudflare API key.</p>
<p>For any existing CDP script, switching to Browser Rendering is a one-line change:</p>
<pre><code class="language-js">const puppeteer = require(&quot;puppeteer-core&quot;);&#10;&#10;const browser = await puppeteer.connect({&#10;	browserWSEndpoint: `wss://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/browser-rendering/devtools/browser?keep_alive=600000`,&#10;	headers: { Authorization: `Bearer ${API_TOKEN}` },&#10;});&#10;&#10;const page = await browser.newPage();&#10;await page.goto(&quot;https://example.com&quot;);&#10;console.log(await page.title());&#10;await browser.close();&#10;</code></pre>
<p>Additionally, MCP clients like Claude Desktop, Claude Code, Cursor, and OpenCode can now use Browser Rendering as their remote browser via the <a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">chrome-devtools-mcp</a> package.</p>
<p>Here is an example of how to configure Browser Rendering for Claude Desktop:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;browser-rendering&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;chrome-devtools-mcp@latest&quot;,&#10;				&quot;--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/devtools/browser?keep_alive=600000&quot;,&#10;				&quot;--wsHeaders={\&quot;Authorization\&quot;:\&quot;Bearer &lt;API_TOKEN&gt;\&quot;}&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To get started, refer to the <a href="/browser-run/cdp/">CDP documentation</a>.</p>


<h2 id="crawl-entire-websites-with-a-single-api-call-using-browser-rendering"><a href="/changelog/post/2026-03-10-br-crawl-endpoint/">Crawl entire websites with a single API call using Browser Rendering</a></h2>
<p><em>2026-03-10</em></p>
<p><em>Edit: this post has been edited to clarify crawling behavior with respect to site guidance.</em></p>
<p>You can now crawl an entire website with a single API call using <a href="/browser-run/">Browser Rendering</a>'s new <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a>, available in open beta. Submit a starting URL, and pages are automatically discovered, rendered in a headless browser, and returned in multiple formats, including HTML, Markdown, and structured JSON. The endpoint is a <a href="/bots/concepts/bot/verified-bots/">verified bot (intermediary agent)</a> that respects robots.txt and <a href="https://www.cloudflare.com/ai-crawl-control/">AI Crawl Control</a> by default, making it easy for developers to comply with website rules, and making it less likely for crawlers to ignore web-owner guidance. This is great for training models, building RAG pipelines, and researching or monitoring content across a site.</p>
<p>Crawl jobs run asynchronously. You submit a URL, receive a job ID, and check back for results as pages are processed.</p>
<pre><code class="language-sh">&#35; Initiate a crawl&#10;curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://blog.cloudflare.com/&quot;&#10;  }&#x27;&#10;&#10;&#35; Check results&#10;curl -X GET &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/{job_id}&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27;&#10;</code></pre>
<p>Key features:</p>
<ul>
<li><strong>Multiple output formats</strong> - Return crawled content as HTML, Markdown, and structured JSON (powered by <a href="/workers-ai/">Workers AI</a>)</li>
<li><strong>Crawl scope controls</strong> - Configure crawl depth, page limits, and wildcard patterns to include or exclude specific URL paths</li>
<li><strong>Automatic page discovery</strong> - Discovers URLs from sitemaps, page links, or both</li>
<li><strong>Incremental crawling</strong> - Use <code>modifiedSince</code> and <code>maxAge</code> to skip pages that haven't changed or were recently fetched, saving time and cost on repeated crawls</li>
<li><strong>Static mode</strong> - Set <code>render: false</code> to fetch static HTML without spinning up a browser, for faster crawling of static sites</li>
<li><strong>Well-behaved bot</strong> - Honors <code>robots.txt</code> directives, including <code>crawl-delay</code></li>
</ul>
<p>Available on both the Workers Free and Paid plans.</p>
<p><strong>Note</strong>: the /crawl endpoint cannot bypass Cloudflare bot detection or captchas, and self-identifies as a bot.</p>
<p>To get started, refer to the <a href="/browser-run/quick-actions/crawl-endpoint/">crawl endpoint documentation</a>.
If you are setting up your own site to be crawled, review the <a href="/browser-run/reference/robots-txt/">robots.txt and sitemaps best practices</a>.</p>


<h2 id="browser-rendering-3x-higher-rest-api-request-rate"><a href="/changelog/post/2026-03-04-br-rest-api-limit-increase/">Browser Rendering: 3x higher REST API request rate</a></h2>
<p><em>2026-03-04</em></p>
<p><a href="/browser-run/">Browser Rendering</a> REST API rate limits for Workers Paid plans have been increased from 3 requests per second (180/min) to <strong>10 requests per second (600/min)</strong>. No action is needed to benefit from the higher limit.</p>
<p><img src="/assets/upstream/images/changelog/browser-run/rest-api-limit-increase.png" alt="Browser Rendering REST API rate limit increased from 3 to 10 requests per second" /></p>
<p>The <a href="/browser-run/quick-actions/">REST API</a> lets you perform common browser tasks with a single API call, and you can now do it at a higher rate.</p>
<ul>
<li><a href="/browser-run/quick-actions/content-endpoint/">/content - Fetch HTML</a></li>
<li><a href="/browser-run/quick-actions/screenshot-endpoint/">/screenshot - Capture screenshot</a></li>
<li><a href="/browser-run/quick-actions/pdf-endpoint/">/pdf - Render PDF</a></li>
<li><a href="/browser-run/quick-actions/markdown-endpoint/">/markdown - Extract Markdown from a webpage</a></li>
<li><a href="/browser-run/quick-actions/snapshot/">/snapshot - Take a webpage snapshot</a></li>
<li><a href="/browser-run/quick-actions/scrape-endpoint/">/scrape - Scrape HTML elements</a></li>
<li><a href="/browser-run/quick-actions/json-endpoint/">/json - Capture structured data using AI</a></li>
<li><a href="/browser-run/quick-actions/links-endpoint/">/links - Retrieve links from a webpage</a></li>
</ul>
<p>If you use the <a href="/browser-run/#integration-methods">Browser Sessions</a> method, increases to concurrent browser and new browser limits are coming soon. Stay tuned.</p>
<p>For full details, refer to the <a href="/browser-run/limits/">Browser Rendering limits page</a>.</p>


<h2 id="workers-websocket-message-size-limit-increased-from-1-mib-to-32-mib"><a href="/changelog/post/2025-10-31-increased-websocket-message-size-limit/">Workers WebSocket message size limit increased from 1 MiB to 32 MiB</a></h2>
<p><em>2025-10-31</em></p>
<p>Workers, including those using <a href="/durable-objects/">Durable Objects</a> and <a href="/browser-run/">Browser Rendering</a>, may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.</p>
<p>This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.</p>
<p>For more information, please see the <a href="/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits">Durable Objects startup limits</a>.</p>


<h2 id="browser-rendering-playwright-ga-stagehand-support-beta-and-higher-limits"><a href="/changelog/post/2025-09-25-br-playwright-ga-stagehand-limits/">Browser Rendering Playwright GA, Stagehand support (Beta), and higher limits</a></h2>
<p><em>2025-09-25T12:00:00+00:00</em></p>
<p>We’re shipping three updates to Browser Rendering:</p>
<ul>
<li>Playwright support is now Generally Available and synced with <a href="https://playwright.dev/docs/release-notes#version-155">Playwright v1.55</a>, giving you a stable foundation for critical automation and AI-agent workflows.</li>
<li>We’re also adding <a href="/browser-run/stagehand/">Stagehand support (Beta)</a> so you can combine code with natural language instructions to build more resilient automations.</li>
<li>Finally, we’ve tripled <a href="/browser-run/limits/#workers-paid">limits</a> for paid plans across both the <a href="/browser-run/quick-actions/">REST API</a> and <a href="/browser-run/#integration-methods">Browser Sessions</a> to help you scale.</li>
</ul>
<p>To get started with Stagehand, refer to the <a href="/browser-run/stagehand/">Stagehand</a> example that uses Stagehand and <a href="/workers-ai/">Workers AI</a> to search for a movie on this <a href="https://demo.playwright.dev/movies">example movie directory</a>, extract its details using natural language (title, year, rating, duration, and genre), and return the information along with a screenshot of the webpage.</p>
<pre><code class="language-ts">const stagehand = new Stagehand({&#10;	env: &quot;LOCAL&quot;,&#10;	localBrowserLaunchOptions: { cdpUrl: endpointURLString(env.BROWSER) },&#10;	llmClient: new WorkersAIClient(env.AI),&#10;	verbose: 1,&#10;});&#10;&#10;await stagehand.init();&#10;const page = stagehand.page;&#10;&#10;await page.goto(&quot;https://demo.playwright.dev/movies&quot;);&#10;&#10;// if search is a multi-step action, stagehand will return an array of actions it needs to act on&#10;const actions = await page.observe(&#x27;Search for &quot;Furiosa&quot;&#x27;);&#10;for (const action of actions) await page.act(action);&#10;&#10;await page.act(&quot;Click the search result&quot;);&#10;&#10;// normal playwright functions work as expected&#10;await page.waitForSelector(&quot;.info-wrapper .cast&quot;);&#10;&#10;let movieInfo = await page.extract({&#10;	instruction: &quot;Extract movie information&quot;,&#10;	schema: z.object({&#10;		title: z.string(),&#10;		year: z.number(),&#10;		rating: z.number(),&#10;		genres: z.array(z.string()),&#10;		duration: z.number().describe(&quot;Duration in minutes&quot;),&#10;	}),&#10;});&#10;&#10;await stagehand.close();&#10;</code></pre>
<p><img src="/images/browser-run/speedystagehand.gif" alt="Stagehand video" /></p>


<h2 id="introducing-pricing-for-the-browser-rendering-api-0-09-per-browser-hour"><a href="/changelog/post/2025-07-28-br-pricing/">Introducing pricing for the Browser Rendering API — $0.09 per browser hour</a></h2>
<p><em>2025-07-28T12:00:00+00:00</em></p>
<p>We’ve launched pricing for <a href="/browser-run/">Browser Rendering</a>, including a free tier and a pay-as-you-go model that scales with your needs. Starting <strong>August 20, 2025</strong>, Cloudflare will begin billing for Browser Rendering.</p>
<p>There are two ways to use Browser Rendering. Depending on the method you use, here’s how billing will work:</p>
<ul>
<li><a href="/browser-run/quick-actions/"><strong>REST API</strong></a>: Charged for <strong>Duration</strong> only ($/browser hour)</li>
<li><a href="/browser-run/#integration-methods"><strong>Browser Sessions</strong></a>: Charged for both <strong>Duration</strong> and <strong>Concurrency</strong> ($/browser hour and # of concurrent browsers)</li>
</ul>
<p>Included usage and pricing by plan</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Included duration</th>
<th>Included concurrency</th>
<th>Price (beyond included)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers Free</strong></td>
<td>10 minutes per day</td>
<td>3 concurrent browsers</td>
<td>N/A</td>
</tr>
<tr>
<td><strong>Workers Paid</strong></td>
<td>10 hours per month</td>
<td>10 concurrent browsers (averaged monthly)</td>
<td><strong>1. REST API</strong>: $0.09 per additional browser hour <br /><strong>2. Workers Bindings</strong>: $0.09 per additional browser hour <br /> $2.00 per additional concurrent browser</td>
</tr>
</tbody>
</table>
<p>What you need to know:</p>
<ul>
<li><strong>Workers Free Plan:</strong> 10 minutes of browser usage per day with 3 concurrent browsers at no charge.</li>
<li><strong>Workers Paid Plan:</strong> 10 hours of browser usage per month with 10 concurrent browsers (averaged monthly) at no charge. Additional usage is charged as shown above.</li>
</ul>
<p>You can monitor usage via the <a href="https://dash.cloudflare.com/?to=/:account/workers/browser-run">Cloudflare dashboard</a>. Go to <strong>Compute</strong> &gt; <strong>Browser Run</strong>.</p>
<p><img src="/assets/upstream/images/browser-run/dashboard.png" alt="Browser Rendering dashboard" /></p>
<p>If you've been using Browser Rendering and do not wish to incur charges, ensure your usage stays within your plan's <a href="/browser-run/pricing/">included usage</a>. To estimate costs, take a look at these <a href="/browser-run/pricing/#examples-of-workers-paid-pricing">example pricing scenarios</a>.</p>


<h2 id="browser-rendering-now-supports-local-development"><a href="/changelog/post/2025-07-22-br-local-dev/">Browser Rendering now supports local development</a></h2>
<p><em>2025-07-22T11:00:00+00:00</em></p>
<p>You can now run your Browser Rendering locally using <code>npx wrangler dev</code>, which spins up a browser directly on your machine before deploying to Cloudflare's global network. By running tests locally, you can quickly develop, debug, and test changes without needing to deploy or worry about usage costs.</p>
<p>Get started with this <a href="/browser-run/how-to/deploy-worker/">example guide</a> that shows how to use Cloudflare's <a href="/browser-run/puppeteer/">fork of Puppeteer</a> (you can also use <a href="/browser-run/playwright/">Playwright</a>) to take screenshots of webpages and store the results in <a href="/kv/">Workers KV</a>.</p>


<h2 id="playwright-mcp-server-is-now-compatible-with-browser-rendering"><a href="/changelog/post/2025-05-28-playwright-mcp/">Playwright MCP server is now compatible with Browser Rendering</a></h2>
<p><em>2025-05-28</em></p>
<p>We're excited to share that you can now use the <a href="https://github.com/cloudflare/playwright-mcp">Playwright MCP</a> server with Browser Rendering.</p>
<p>Once you <a href="/browser-run/playwright/playwright-mcp/#deploying">deploy the server</a>, you can use any MCP client with it to interact with Browser Rendering. This allows you to run AI models that can automate browser tasks, such as taking screenshots, filling out forms, or scraping data.</p>
<p><img src="/assets/upstream/images/browser-run/playground-ai-screenshot.png" alt="Access Analytics" /></p>
<p>Playwright MCP is available as an npm package at <a href="https://www.npmjs.com/package/@cloudflare/playwright-mcp"><code>@cloudflare/playwright-mcp</code></a>. To install it, type:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Deploying the server is then as easy as:</p>
<pre><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { createMcpAgent } from &quot;@cloudflare/playwright-mcp&quot;;&#10;&#10;export const PlaywrightMCP = createMcpAgent(env.BROWSER);&#10;export default PlaywrightMCP.mount(&quot;/sse&quot;);&#10;</code></pre>
<p>Check out the full code at <a href="https://github.com/cloudflare/playwright-mcp">GitHub</a>.</p>
<p>Learn more about Playwright MCP in our <a href="/browser-run/playwright/playwright-mcp/">documentation</a>.</p>


<h2 id="browser-rendering-rest-api-is-generally-available-with-new-endpoints-and-a-free-tier"><a href="/changelog/post/2025-04-07-br-free-ga-playwright/">Browser Rendering REST API is Generally Available, with new endpoints and a free tier</a></h2>
<p><em>2025-04-07</em></p>
<p>We’re excited to announce Browser Rendering is now available on the <a href="https://www.cloudflare.com/plans/developer-platform/">Workers Free plan</a>, making it even easier to prototype and experiment with web search and headless browser use-cases when building applications on Workers.</p>
<p>The Browser Rendering <strong><a href="/browser-run/quick-actions/">REST API</a> is now Generally Available</strong>, allowing you to control browser instances from outside of Workers applications. We've added three new endpoints to help automate more browser tasks:</p>
<ul>
<li><strong>Extract structured data</strong> – Use <code>/json</code> to retrieve structured data from a webpage.</li>
<li><strong>Retrieve links</strong> – Use <code>/links</code> to pull all links from a webpage.</li>
<li><strong>Convert to Markdown</strong> – Use <code>/markdown</code> to convert webpage content into Markdown format.</li>
</ul>
<p>For example, to fetch the Markdown representation of a webpage:</p>
<pre><code class="language-bash">curl -X &#x27;POST&#x27; &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27;&#10;</code></pre>
<p>For the full list of endpoints, check out our <a href="/browser-run/quick-actions/">REST API documentation</a>. You can also interact with Browser Rendering via the <a href="https://github.com/cloudflare/cloudflare-typescript">Cloudflare TypeScript SDK</a>.</p>
<p>We also recently landed support for <a href="/browser-run/playwright/">Playwright</a> in Browser Rendering for browser automation from Cloudflare <a href="/workers/">Workers</a>, in addition to <a href="/browser-run/puppeteer/">Puppeteer</a>, giving you more flexibility to test across different browser environments.</p>
<p>Visit the <a href="/browser-run/">Browser Rendering docs</a> to learn more about how to use headless browsers in your applications.</p>


<h2 id="playwright-for-browser-rendering-now-available"><a href="/changelog/post/2025-04-04-playwright-beta/">Playwright for Browser Rendering now available</a></h2>
<p><em>2025-04-04</em></p>
<p>We're excited to share that you can now use Playwright's browser automation <a href="https://playwright.dev/docs/api/class-playwright">capabilities</a> from Cloudflare <a href="/workers/">Workers</a>.</p>
<p><a href="https://playwright.dev/">Playwright</a> is an open-source package developed by Microsoft that can do browser automation tasks; it's commonly used to write software tests, debug applications, create screenshots, and crawl pages. Like <a href="/browser-run/puppeteer/">Puppeteer</a>, we <a href="https://github.com/cloudflare/playwright">forked</a> Playwright and modified it to be compatible with Cloudflare Workers and <a href="/browser-run/">Browser Rendering</a>.</p>
<p>Below is an example of how to use Playwright with Browser Rendering to test a TODO application using assertions:</p>
<pre><code class="language-ts">import { launch, type BrowserWorker } from &quot;@cloudflare/playwright&quot;;&#10;import { expect } from &quot;@cloudflare/playwright/test&quot;;&#10;&#10;interface Env {&#10;	MYBROWSER: BrowserWorker;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const browser = await launch(env.MYBROWSER);&#10;		const page = await browser.newPage();&#10;&#10;		await page.goto(&quot;https://demo.playwright.dev/todomvc&quot;);&#10;&#10;		const TODO_ITEMS = [&#10;			&quot;buy some cheese&quot;,&#10;			&quot;feed the cat&quot;,&#10;			&quot;book a doctors appointment&quot;,&#10;		];&#10;&#10;		const newTodo = page.getByPlaceholder(&quot;What needs to be done?&quot;);&#10;		for (const item of TODO_ITEMS) {&#10;			await newTodo.fill(item);&#10;			await newTodo.press(&quot;Enter&quot;);&#10;		}&#10;&#10;		await expect(page.getByTestId(&quot;todo-title&quot;)).toHaveCount(TODO_ITEMS.length);&#10;&#10;		await Promise.all(&#10;			TODO_ITEMS.map((value, index) =&gt;&#10;				expect(page.getByTestId(&quot;todo-title&quot;).nth(index)).toHaveText(value),&#10;			),&#10;		);&#10;	},&#10;};&#10;</code></pre>
<p>Playwright is available as an npm package at <a href="https://www.npmjs.com/package/@cloudflare/playwright"><code>@cloudflare/playwright</code></a> and the code is at <a href="https://github.com/cloudflare/playwright">GitHub</a>.</p>
<p>Learn more in our <a href="/browser-run/playwright/">documentation</a>.</p>


<h2 id="new-rest-api-is-in-open-beta"><a href="/changelog/post/2025-02-27-br-rest-api-beta/">New REST API is in open beta!</a></h2>
<p><em>2025-02-27</em></p>
<p>We've released a new REST API for <a href="/browser-run/">Browser Rendering</a> in open beta, making interacting with browsers easier than ever. This new API provides endpoints for common browser actions, with more to be added in the future.</p>
<p>With the <strong>REST API</strong> you can:</p>
<ul>
<li><strong>Capture screenshots</strong> – Use <code>/screenshot</code> to take a screenshot of a webpage from provided URL or HTML.</li>
<li><strong>Generate PDFs</strong> – Use <code>/pdf</code> to convert web pages into PDFs.</li>
<li><strong>Extract HTML content</strong> – Use <code>/content</code> to retrieve the full HTML from a page.
<strong>Snapshot (HTML + Screenshot)</strong> – Use <code>/snapshot</code> to capture both the page's HTML and a screenshot in one request</li>
<li><strong>Scrape Web Elements</strong> – Use <code>/scrape</code> to extract specific elements from a page.</li>
</ul>
<p>For example, to capture a screenshot:</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;html&quot;: &quot;Hello World!&quot;,&#10;    &quot;screenshotOptions&quot;: {&#10;      &quot;type&quot;: &quot;webp&quot;,&#10;      &quot;omitBackground&quot;: true&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.webp&quot;&#10;</code></pre>
<p>Learn more in our <a href="/browser-run/quick-actions/">documentation</a>.</p>


<h2 id="increased-browser-rendering-limits"><a href="/changelog/post/2025-01-30-browser-rendering-more-instances/">Increased Browser Rendering limits!</a></h2>
<p><em>2025-01-30</em></p>
<p><a href="/browser-run/">Browser Rendering</a> now supports 10 concurrent browser instances per account <em>and</em> 10 new instances per minute, up from the previous limits of 2.</p>
<p>This allows you to launch more browser tasks from <a href="/workers">Cloudflare Workers</a>.</p>
<p>To manage concurrent browser sessions, you can use <a href="/queues/">Queues</a> or <a href="/workflows/">Workflows</a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17693.md")</div>



