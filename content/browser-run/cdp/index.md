<p>The <code>/devtools</code> endpoints provide session management capabilities that follow the <a href="https://chromedevtools.github.io/devtools-protocol/">Chrome DevTools Protocol (CDP)</a>. These endpoints allow you to create persistent browser sessions, manage multiple tabs, and interact with browsers using CDP commands. This is useful for advanced automation, debugging, and remote browser control.</p>
<p>CDP endpoints can be accessed from any environment that supports WebSocket connections, including local development machines, external servers, and CI/CD pipelines. This means you can connect to Browser Run from Node.js scripts, Puppeteer, Playwright, or any CDP-compatible client.</p>
<p>Before you begin, <a href="/fundamentals/api/get-started/create-token/">create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</p>
<h2 id="what-is-cdp">What is CDP?</h2>
<p>The Chrome DevTools Protocol (CDP) is a remote debugging protocol that allows you to instrument, inspect, debug, and profile Chromium-based browsers. It is the same protocol used by Chrome DevTools to control and monitor the browser. Popular browser automation libraries like Puppeteer and Playwright provide high-level APIs over the Chrome DevTools Protocol, making it easier to automate common tasks.</p>
<h2 id="use-cases">Use cases</h2>
<p>The browser sessions endpoints enable you to:</p>
<ul>
<li><strong>Create and manage persistent browser sessions</strong> — Launch browser instances that remain active for extended periods</li>
<li><strong>Open, close, and list browser tabs (targets)</strong> — Manage multiple debuggable targets (pages, iframes, etc.) within a single browser instance</li>
<li><strong>Connect via WebSocket to send CDP commands</strong> — Automate browser actions programmatically</li>
<li><strong>View live browser sessions using Chrome DevTools UI</strong> — Debug and inspect remote browser sessions visually</li>
<li><strong>Integrate with existing CDP clients</strong> — Use standard CDP clients like Puppeteer or custom WebSocket implementations</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>Once you acquire a browser session, you can interact with it in two ways:</p>
<h3 id="cdp-over-websocket">CDP over WebSocket</h3>
<p>Connect to the WebSocket endpoint <code>/devtools/browser</code> to acquire a session and send <a href="https://chromedevtools.github.io/devtools-protocol/">CDP commands</a> directly over the connection. This is the standard way to use CDP and works with any CDP client, including <a href="/browser-run/cdp/puppeteer/">Puppeteer</a>, <a href="/browser-run/cdp/playwright/">Playwright</a>, and <a href="/browser-run/cdp/mcp-clients/">MCP clients</a>.</p>
<h3 id="http-api">HTTP API</h3>
<p>HTTP endpoints are also available to manage the browser lifecycle without using WebSockets. These follow the standard <a href="https://chromedevtools.github.io/devtools-protocol/#endpoints">CDP HTTP endpoints</a>:</p>
<ol>
<li><strong>Create session</strong> — <code>POST /devtools/browser</code></li>
<li><strong>List tabs</strong> — <code>GET /devtools/browser/{session_id}/json/list</code></li>
<li><strong>Create tab</strong> — <code>PUT /devtools/browser/{session_id}/json/new</code></li>
<li><strong>Close tab</strong> — <code>DELETE /devtools/browser/{session_id}/json/close/{target_id}</code></li>
<li><strong>Close session</strong> — <code>DELETE /devtools/browser/{session_id}</code></li>
</ol>
<p>Check the <a href="/api/resources/browser_rendering/">API reference</a> for the full list of endpoints.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
