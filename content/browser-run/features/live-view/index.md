<p>Live View lets you see and interact with a remote Browser Run session in real time. This is useful for debugging automation scripts, monitoring what a browser is doing, or manually stepping in when a task requires human intervention (see <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>).</p>
<p>Live View is available for any <a href="/browser-run/#integration-methods">Browser Session</a>, including sessions created with <a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, or the <a href="/browser-run/cdp/">Chrome DevTools Protocol (CDP)</a> endpoints.</p>
<p>A browser session is one remote Chrome instance. A session can contain multiple tabs. CDP calls each debuggable item a target, and a page target usually represents one browser tab. Live View connects to a page target.</p>
<h2 id="access-live-view">Access Live View</h2>
<p>Open Live View from the Cloudflare dashboard or with a generated <code>devtoolsFrontendUrl</code>. A generated URL opens Cloudflare's hosted interface in any browser. Chrome users can instead open the connection in Chrome DevTools.</p>
<h3 id="cloudflare-dashboard">Cloudflare dashboard</h3>
<p>In the Cloudflare dashboard, go to the <strong>Browser Run</strong> page and select the <strong>Live Sessions</strong> tab. This shows all active browser sessions in your account. Expand a session to see its tabs, then select <strong>Open</strong> to open the Live View for that tab.</p>
<div class="nb-dash-button"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3701.md")
</aside>
<h3 id="generated-url-any-browser">Generated URL (any browser)</h3>
<p>When you create a session with <code>targets=true</code> or list a session's targets, the API response includes a <code>devtoolsFrontendUrl</code> for each page target. Open this URL in any browser to watch or control that tab through Cloudflare's hosted interface. The generated URL uses <code>live.browser.run</code>; you do not visit that hostname directly.</p>
<p>The hosted UI supports three viewing modes, controlled by the <code>mode</code> parameter in the URL:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>URL pattern</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>tab</code></td>
<td><code>https://live.browser.run/ui/view?mode=tab&amp;wss=...</code></td>
<td>Shows and controls one selected page without DevTools panels</td>
</tr>
<tr>
<td><code>full</code></td>
<td><code>https://live.browser.run/ui/view?mode=full&amp;wss=...</code></td>
<td>Shows the browser interface and its open page tabs</td>
</tr>
<tr>
<td><code>devtools</code></td>
<td><code>https://live.browser.run/ui/view?mode=devtools&amp;wss=...</code></td>
<td>Opens DevTools panels for one page, including Elements and the Console</td>
</tr>
</tbody>
</table>
<h3 id="native-chrome-devtools-chrome-only">Native Chrome DevTools (Chrome only)</h3>
<p>Browser Run supports CDP, the protocol that powers Chrome DevTools. If a generated <code>devtoolsFrontendUrl</code> starts with <code>https://live.browser.run/ui/inspector?wss=</code>, replace that prefix with <code>devtools://devtools/bundled/inspector.html?wss=</code>:</p>
<pre><code class="language-txt">devtools://devtools/bundled/inspector.html?wss=live.browser.run/api/devtools/browser/SESSION_ID/page/TARGET_ID?jwt=...&#10;</code></pre>
<p>Paste the updated URL into Chrome's address bar. Chrome opens its built-in DevTools interface for the remote tab. The <code>devtools://</code> protocol works only in Chrome and supports only the <code>devtools</code> viewing mode.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="url-validity">URL validity</h3>
@markup("md", "content/.markup/bodies/3700.md")
</aside>
<p>The API examples in the following sections assume <code>$ACCOUNT_ID</code> is set and <code>$CLOUDFLARE_API_TOKEN</code> has Browser Rendering Write permission.</p>
<h2 id="view-a-new-session">View a new session</h2>
<ol>
<li>Create a browser session with <code>targets=true</code> to include its current page targets and generated Live View URLs in the response:</li>
</ol>
<pre><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-rendering/devtools/browser</code></pre>
<pre><code class="language-json">{&#10;	&quot;sessionId&quot;: &quot;1909cef7-23e8-4394-bc31-27404bf4348f&quot;,&#10;	&quot;targets&quot;: [&#10;		{&#10;			&quot;description&quot;: &quot;&quot;,&#10;			&quot;devtoolsFrontendUrl&quot;: &quot;https://live.browser.run/ui/inspector?wss=live.browser.run/api/devtools/browser/1909cef7-.../page/8E598E99...?jwt=...&quot;,&#10;			&quot;id&quot;: &quot;8E598E996530FB09E46A22B8B7754F7F&quot;,&#10;			&quot;title&quot;: &quot;about:blank&quot;,&#10;			&quot;type&quot;: &quot;page&quot;,&#10;			&quot;url&quot;: &quot;about:blank&quot;,&#10;			&quot;webSocketDebuggerUrl&quot;: &quot;wss://live.browser.run/api/devtools/browser/1909cef7-.../page/8E598E99...?jwt=...&quot;&#10;		}&#10;	],&#10;	&quot;webSocketDebuggerUrl&quot;: &quot;wss://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/devtools/browser/1909cef7-...&quot;&#10;}&#10;</code></pre>
<p>The <code>targets[].devtoolsFrontendUrl</code> opens the hosted interface for a page. The <code>targets[].webSocketDebuggerUrl</code> connects a CDP client to that page. The top-level <code>webSocketDebuggerUrl</code> connects a CDP client to the browser session.</p>
<ol start="2">
<li>Find the page target you want by its <code>title</code> or <code>url</code>. Copy its <code>devtoolsFrontendUrl</code> and open it in your browser. A new session initially contains an <code>about:blank</code> page.</li>
</ol>
<h2 id="view-an-existing-session">View an existing session</h2>
<p>If you have a running session and want to connect to it:</p>
<ol>
<li>
<p>List your active sessions and copy the ID of the session you want to view:</p>
<pre><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-rendering/devtools/session</code></pre>
</li>
<li>
<p>Using the session ID, list the targets in that session:</p>
<pre><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-rendering/devtools/browser/$SESSION_ID/json/list</code></pre>
</li>
</ol>
<pre><code class="language-json">[&#10;	{&#10;		&quot;id&quot;: &quot;110850A800BDB8B593CDDA30676635CF&quot;,&#10;		&quot;type&quot;: &quot;page&quot;,&#10;		&quot;url&quot;: &quot;https://example.com&quot;,&#10;		&quot;title&quot;: &quot;Example Domain&quot;,&#10;		&quot;description&quot;: &quot;&quot;,&#10;		&quot;devtoolsFrontendUrl&quot;: &quot;https://live.browser.run/ui/view?wss=live.browser.run/api/devtools/browser/28d75446-.../page/110850A8...?jwt=...&quot;,&#10;		&quot;webSocketDebuggerUrl&quot;: &quot;wss://live.browser.run/api/devtools/browser/28d75446-.../page/110850A8...?jwt=...&quot;&#10;	}&#10;]&#10;</code></pre>
<ol start="3">
<li>Copy the <code>devtoolsFrontendUrl</code> and open it in your browser.</li>
</ol>
<h2 id="generate-a-live-view-url">Generate a Live View URL</h2>
<p>Listing targets returns a default <code>devtoolsFrontendUrl</code> for every page target. Generate a custom URL to change its viewing mode, connection deadline, or viewer permissions.</p>
<h3 id="set-parameters">Set parameters</h3>
<p>The following optional parameters configure generated links:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>mode</code></td>
<td><code>string</code></td>
<td><code>devtools</code></td>
<td>Viewing mode: <code>devtools</code>, <code>tab</code>, or <code>full</code></td>
</tr>
<tr>
<td><code>expiresInMs</code></td>
<td><code>number</code></td>
<td><code>300,000</code> (five minutes)</td>
<td>Deadline for starting a connection, in milliseconds. Minimum <code>60,000</code> and maximum <code>3,600,000</code></td>
</tr>
<tr>
<td><code>targetId</code></td>
<td><code>string</code></td>
<td>Current CDP target or first page target</td>
<td>Page target to view</td>
</tr>
<tr>
<td><code>guardrails</code></td>
<td><code>object</code></td>
<td>—</td>
<td>REST API only. Viewer restrictions for this connection. Set <code>{ &quot;mode&quot;: &quot;readonly&quot; }</code> to block interaction</td>
</tr>
</tbody>
</table>
<p>The REST API response includes <code>id</code>, <code>options</code>, <code>devtoolsFrontendUrl</code>, and <code>webSocketDebuggerUrl</code>. Open the frontend URL in a browser or use the WebSocket URL with a CDP client. The <code>Cloudflare.getLiveView</code> CDP command returns <code>devtoolsFrontendUrl</code>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="treat-live-view-urls-as-credentials">Treat Live View URLs as credentials</h3>
@markup("md", "content/.markup/bodies/3699.md")
</aside>
<p>A read-only Live View guardrail applies only to the generated connection. Other connections and automation scripts can still control the session. Session <a href="/browser-run/features/guardrails/">guardrails</a> restrict HTTP and HTTPS destinations for the entire session and remain active for every Live View connection.</p>
<h3 id="rest-api">REST API</h3>
<p>Use the <a href="/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/live_view/methods/create/">Live View endpoint</a> to generate a URL:</p>
<pre><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-rendering/devtools/browser/$SESSION_ID/live_view</code></pre>
<h4 id="share-a-view-only-link">Share a view-only link</h4>
<p>To block viewer interaction, set <code>guardrails</code> to <code>{ &quot;mode&quot;: &quot;readonly&quot; }</code>:</p>
<pre><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-rendering/devtools/browser/$SESSION_ID/live_view</code></pre>
<p>The link streams the session but blocks navigation, input, and JavaScript evaluation. The tab title starts with <code>READ ONLY - </code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3698.md")
</aside>
<h3 id="cdp">CDP</h3>
<p>CDP is Chrome's remote debugging protocol. <code>Cloudflare.getLiveView</code> is a Cloudflare extension that generates a Live View URL over an existing CDP connection. This Puppeteer example generates a URL for the current page:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3702.md")
</div>
<p>To use Live View for a human operator handoff, refer to the <a href="/browser-run/features/human-in-the-loop/#cloudflaregetliveview">Human in the Loop workflow</a>.</p>
