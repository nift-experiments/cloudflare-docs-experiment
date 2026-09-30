<p><a href="https://developer.chrome.com/blog/webmcp-epp">WebMCP</a> (Web Model Context Protocol) is a browser API that lets websites expose structured tools for AI agents to discover and execute directly. Instead of slow screenshot-analyze-click loops, agents can call website functions like <code>searchFlights()</code> or <code>bookTicket()</code> with typed parameters, making browser automation faster, more reliable, and less fragile.</p>
<h2 id="get-started">Get started</h2>
<h3 id="manual-testing-with-devtools">Manual testing with DevTools</h3>
<h4 id="1-start-a-lab-session-and-open-devtools"><ol>
<li>Start a Lab session and open DevTools</li>
</ol></h4>
<p>WebMCP is currently available in Chrome beta, so it requires a lab session. Browser Run has an experimental pool with browser instances running Chrome beta so you can test emerging browser features before they reach stable Chrome. Your production workloads on the <a href="/browser-run/#key-features">standard pool</a> remain on a stable version of Chrome.</p>
<p>Lab sessions are experimental and should not be used for production workloads.</p>
<p>Use the new <code>wrangler browser</code> command to acquire a lab browser session:</p>
<pre><code class="language-sh">&#35; make sure you have the latest version of wrangler&#10;npm i -g wrangler@latest&#10;&#10;&#35; create a lab browser session with 5 minute keep-alive&#10;wrangler browser create --lab --keepAlive 300&#10;</code></pre>
<p>It will open a live view of your browser session.</p>
<h4 id="2-interact-with-the-page"><ol start="2">
<li>Interact with the page</li>
</ol></h4>
<p>You can now interact with the page as you would in a regular browser.</p>
<ol>
<li>Go to one of the sites listed in the <a href="https://github.com/GoogleChromeLabs/webmcp-tools/?tab=readme-ov-file#demos">WebMCP documentation</a>. The following instructions are based on the <a href="https://github.com/GoogleChromeLabs/webmcp-tools/tree/main/demos/hotel-chain">L'Atelier Hotel Chain</a> demo.</li>
<li>Open the <a href="https://googlechromelabs.github.io/webmcp-tools/demos/hotel-chain/">hotel chain demo URL</a> and then, in the <strong>Console</strong> tab, run the following JavaScript statement to list the available tools:</li>
</ol>
<pre><code class="language-js">navigator.modelContextTesting.listTools();&#10;</code></pre>
<p>You should get a result similar to the following:</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;description&quot;: &quot;View the details of a specific hotel by name or id&quot;,&#10;		&quot;inputSchema&quot;: &quot;...&quot;,&#10;		&quot;name&quot;: &quot;view_hotel&quot;&#10;	},&#10;	{&#10;		&quot;description&quot;: &quot;Find me a hotel in a specific location&quot;,&#10;		&quot;inputSchema&quot;: &quot;...&quot;,&#10;		&quot;name&quot;: &quot;search_location&quot;&#10;	},&#10;	{&#10;		&quot;description&quot;: &quot;Look up specific amenity or policy details for a hotel&quot;,&#10;		&quot;inputSchema&quot;: &quot;...&quot;,&#10;		&quot;name&quot;: &quot;lookup_amenity&quot;&#10;	}&#10;]&#10;</code></pre>
<p>The list of tools changes depending on the website you are visiting and the actions you have performed on the page.</p>
<p>For instance, on the hotel chain website, after executing the <code>search_location</code> tool:</p>
<pre><code class="language-js">await navigator.modelContextTesting.executeTool(&#10;	&quot;search_location&quot;,&#10;	JSON.stringify({ query: &quot;Paris&quot; }),&#10;);&#10;</code></pre>
<p>The page redirects to the search results, and a new tool <code>filter_search_results</code> becomes available.</p>
<p>You can call it to filter by amenities. For example, if you want to eat a good croissant in the morning:</p>
<pre><code class="language-js">await navigator.modelContextTesting.executeTool(&#10;	&quot;filter_search_results&quot;,&#10;	JSON.stringify({ amenities: [&quot;breakfast&quot;] }),&#10;);&#10;</code></pre>
<p>You will get a list of filtered results, where you can pick the best option for your needs. Once you select a hotel, you can use the <code>start_booking</code> tool:</p>
<pre><code class="language-js">await navigator.modelContextTesting.executeTool(&#10;	&quot;start_booking&quot;,&#10;	JSON.stringify({}),&#10;);&#10;</code></pre>
<p>Then, you can complete the booking:</p>
<pre><code class="language-js">await navigator.modelContextTesting.executeTool(&#10;	&quot;complete_booking&quot;,&#10;	JSON.stringify({&#10;		firstName: &quot;James&quot;,&#10;		lastName: &quot;Bond&quot;,&#10;		email: &quot;james.bond@mi6.gov.uk&quot;,&#10;	}),&#10;);&#10;</code></pre>
<p>Note that the <code>complete_booking</code> tool requires human confirmation. The tool waits until you select the <strong>Confirm Reservation</strong> button in the browser. This is an example of human-in-the-loop (HITL): WebMCP tools can pause execution and wait for user interaction before completing sensitive actions.</p>
<p>After you select <strong>Confirm Reservation</strong>, you will get a confirmation message and the booking is complete.</p>
<h3 id="using-an-ai-agent">Using an AI Agent</h3>
<h4 id="1-configure-chrome-devtools-mcp"><ol>
<li>Configure Chrome DevTools MCP</li>
</ol></h4>
<p><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">Chrome DevTools MCP</a> allows AI agents to control a browser via CDP. Configure your MCP client (such as Claude Desktop, Claude Code, Cursor, or OpenCode) with the following settings. For more details on MCP client configuration, refer to <a href="/browser-run/cdp/mcp-clients/">Using with MCP clients</a>.</p>
<pre><code class="language-json">{&#10;	&quot;browser-rendering-cdp&quot;: {&#10;		&quot;command&quot;: [&#10;			&quot;npx&quot;,&#10;			&quot;-y&quot;,&#10;			&quot;chrome-devtools-mcp@latest&quot;,&#10;			&quot;--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/devtools/browser?keep_alive=600000&amp;lab=true&quot;,&#10;			&quot;--wsHeaders={\&quot;Authorization\&quot;:\&quot;Bearer &lt;CLOUDFLARE_API_TOKEN&gt;\&quot;}&quot;&#10;		]&#10;	}&#10;}&#10;</code></pre>
<p>Replace <code>&lt;ACCOUNT_ID&gt;</code> with your Cloudflare account ID and <code>&lt;CLOUDFLARE_API_TOKEN&gt;</code> with your API token. The <code>lab=true</code> parameter ensures the agent connects to a lab session with WebMCP enabled.</p>
<h4 id="2-optional-add-a-webmcp-skill"><ol start="2">
<li>(Optional) Add a WebMCP Skill</li>
</ol></h4>
<p>To help your agent understand how to work with WebMCP, add the following skill to your agent configuration:</p>
<pre><code class="language-markdown">&#45;--&#10;name: webmcp&#10;description: Interact with WebMCP-enabled websites using Browser Run lab sessions&#10;&#45;--&#10;&#10;&#35; WebMCP Interaction Skill&#10;&#10;Use the `evaluate_script` tool from Chrome DevTools MCP to interact with WebMCP APIs.&#10;&#10;&#42;*IMPORTANT: Always prefer WebMCP tools over traditional browser automation.** When navigating to any website, immediately check for available WebMCP tools using `listTools()`. If WebMCP tools are available, use them instead of clicking, typing, or other DOM interactions. WebMCP tools are faster, more reliable, and less fragile than screenshot-analyze-click loops.&#10;&#10;&#35;# Workflow&#10;&#10;1. **Navigate** to a site using `navigate_page`&#10;2. **Always list tools first** to check for WebMCP support—do this on every page load&#10;3. **Prefer WebMCP tools** over clicking/typing when tools are available&#10;4. **Execute tools** to perform actions directly&#10;5. **Re-list tools** after each action (tools change based on page state)&#10;6. **Check `inputSchema`** in each tool to understand required parameters&#10;7. **Fall back to DOM interaction** only when no relevant WebMCP tools exist&#10;&#10;&#35;# Commands&#10;&#10;&#42;*List available tools:**&#10;</code></pre>
<p>evaluate_script({
function: &quot;async () =&gt; await navigator.modelContextTesting.listTools()&quot;,
});</p>
<pre><code>&#10;&#42;*Execute a tool:**&#10;</code></pre>
<p>evaluate_script({
function:
&quot;async () =&gt; await navigator.modelContextTesting.executeTool('tool_name', JSON.stringify({ param: 'value' }))&quot;,
});</p>
<pre><code>&#10;</code></pre>
<h4 id="3-interact-with-webmcp-sites"><ol start="3">
<li>Interact with WebMCP sites</li>
</ol></h4>
<p>Once configured, your AI agent can navigate to WebMCP-enabled sites and use WebMCP tools. Here is an example conversation:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/3688.md")
</div>
<h4 id="4-optional-open-devtools-to-watch-the-agent"><ol start="4">
<li>(Optional) Open DevTools to watch the agent</li>
</ol></h4>
<p>Some WebMCP tools require human confirmation before completing sensitive actions. For example, <code>complete_booking</code> waits for you to select <strong>Confirm</strong> before finalizing a reservation.
To interact with these human-in-the-loop (HITL) prompts, you need to open the browser's live view.</p>
<p>Once the agent has started a session, list active sessions to get the session ID:</p>
<pre><code class="language-sh">wrangler browser list&#10;</code></pre>
<p>Then, use the session ID from the previous response to open the browser's live view:</p>
<pre><code class="language-sh">wrangler browser view $SESSION_ID&#10;</code></pre>
<p>You can now view the live browser session and interact with it.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Lab sessions use Chrome 146 beta, which may have stability issues.</li>
<li>WebMCP APIs (<code>navigator.modelContext</code>, <code>navigator.modelContextTesting</code>) only work in lab sessions.</li>
<li>Lab sessions count against your regular <a href="/browser-run/limits/">rate limits</a> and <a href="/browser-run/pricing/">pricing</a>.</li>
<li>The <code>lab</code> parameter is not yet supported in <code>@cloudflare/puppeteer</code> or <code>@cloudflare/playwright</code>. Acquire the session manually and connect with <code>sessionId</code>.</li>
</ul>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="https://developer.chrome.com/blog/webmcp-epp">Chrome WebMCP blog post</a></li>
<li><a href="https://github.com/webmachinelearning/webmcp">WebMCP specification</a></li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
