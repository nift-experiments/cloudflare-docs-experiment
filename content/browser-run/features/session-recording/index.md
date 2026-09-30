<p><span class="nb-badge">Beta</span></p>
<p>When browser automation fails or behaves unexpectedly, it can be difficult to understand what happened. Session recording captures DOM changes, mouse and keyboard events, and page navigation as structured JSON events — not a video — so it is lightweight and easy to inspect. Recordings are powered by <a href="https://github.com/rrweb-io/rrweb">rrweb</a> and are opt-in per session.</p>
<h2 id="enable-session-recording">Enable session recording</h2>
<p>Session recording must be enabled during the initial session acquisition. You cannot enable recording when reconnecting to an existing session.</p>
<p>Pass <code>recording: true</code> to <code>puppeteer.launch()</code> or <code>playwright.launch()</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3693.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3690.md")
</aside>
<h2 id="enable-with-cdp-endpoint">Enable with CDP endpoint</h2>
<p>When connecting to Browser Run from any environment using the <a href="/browser-run/cdp/">CDP endpoint</a>, add <code>recording=true</code> as a query parameter to the WebSocket URL:</p>
<pre><code class="language-txt">wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/devtools/browser?recording=true&amp;keep_alive=600000&#10;</code></pre>
<p>For example, to enable session recording in an MCP client, add <code>recording=true</code> to the <code>--wsEndpoint</code> URL in your client configuration:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;browser-rendering&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;chrome-devtools-mcp@latest&quot;,&#10;				&quot;--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/devtools/browser?recording=true&amp;keep_alive=600000&quot;,&#10;				&quot;--wsHeaders={\&quot;Authorization\&quot;:\&quot;Bearer &lt;API_TOKEN&gt;\&quot;}&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>For other MCP clients and CDP usage with Puppeteer or Playwright, refer to the <a href="/browser-run/cdp/">CDP documentation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3689.md")
</aside>
<h2 id="view-recordings">View recordings</h2>
<p>After a session closes, its recording is available in the Cloudflare dashboard under <strong>Browser Run</strong> &gt; <strong>Runs</strong>. Select the recording icon next to a session to open the recording viewer, where you can scrub through the timeline and replay what happened during the session.</p>
<p>If a session opened multiple tabs, the recording viewer shows a tab selector dropdown in the top-right corner of the replay area. Use it to switch between the recorded tabs and view the activity for each one individually.</p>
<div class="nb-dash-button"></div>
<h2 id="retrieve-a-recording-via-api">Retrieve a recording via API</h2>
<p>You can also retrieve a recording programmatically using the session ID. Use <code>browser.sessionId()</code> to capture the session ID before closing the browser, then pass it to the recordings endpoint.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/recording/&lt;SESSION_ID&gt; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>A successful response looks similar to the following:</p>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;sessionId&quot;: &quot;e26d4660-5b78-4761-b82f-c6b5bad5a925&quot;,&#10;		&quot;duration&quot;: 4380,&#10;		&quot;events&quot;: {&#10;			&quot;target-1&quot;: [],&#10;			&quot;target-2&quot;: []&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>After a recorded session closes, the recording may still be finalizing. The endpoint can briefly return <code>404</code> during this period. Callers can retry the request until finalization completes.</p>
<p>The event arrays are available under <code>result.events</code>. The keys in <code>result.events</code> (such as <code>target-1</code>, <code>target-2</code>) are <a href="https://chromedevtools.github.io/devtools-protocol/tot/Target/">CDP targets</a>. In the context of session recording, each target typically corresponds to a browser tab. A session that opened multiple tabs will have one target per tab, and each target's value is an independent rrweb event array for that tab.</p>
<h2 id="replay-a-recording">Replay a recording</h2>
<p>Each value in <code>result.events</code> is a standard rrweb event array and can be passed directly to <a href="https://github.com/rrweb-io/rrweb/tree/master/packages/rrweb-player"><code>rrweb-player</code></a> to self-host a replay UI with a timeline scrubber and playback controls.</p>
<p>Tabs replay independently — to replay a multi-tab session, render one player per target, or build a UI that lets the user switch between targets (similar to the tab selector in the dashboard recording viewer).</p>
<h2 id="limits">Limits</h2>
<ul>
<li>Recordings are retained for 30 days after the session ends and automatically deleted.</li>
<li>Recording is opt-in. It is not enabled by default.</li>
<li>Session recording is available with Browser Sessions via <code>launch()</code> and the <a href="/browser-run/cdp/">CDP endpoint</a>. It is not available with Quick Actions.</li>
<li>The minimum recording duration is 1 second. Sessions shorter than 1 second will not produce a viewable recording.</li>
<li>The maximum recording duration is 2 hours.</li>
</ul>
<h2 id="rrweb-limitations">rrweb limitations</h2>
<p>Session recording uses <a href="https://github.com/rrweb-io/rrweb">rrweb</a>, which records DOM state and events rather than pixels. This approach is lightweight but has the following limitations:</p>
<ul>
<li><strong>Canvas elements</strong> — The content of <code>&lt;canvas&gt;</code> elements is not captured. The element itself appears in the recording as a blank placeholder.</li>
<li><strong>Cross-origin iframes</strong> — Content inside cross-origin <code>&lt;iframe&gt;</code> elements is not recorded. Same-origin iframes are recorded normally.</li>
<li><strong>Video and audio</strong> — The DOM structure of <code>&lt;video&gt;</code> and <code>&lt;audio&gt;</code> elements is captured, but media playback state and content are not.</li>
<li><strong>WebGL</strong> — WebGL rendering is not captured.</li>
<li><strong>Input fields</strong> — The content of all input fields is masked by default and will not be visible in the replay.</li>
<li><strong>Large or complex pages</strong> — Pages with frequent DOM mutations (for example, pages with real-time data feeds or heavy animations) can generate a high volume of events, which increases the size of the recording.</li>
</ul>
