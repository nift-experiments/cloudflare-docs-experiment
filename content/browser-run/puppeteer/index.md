<p><a href="https://pptr.dev/">Puppeteer</a> is one of the most popular libraries that abstract the lower-level DevTools protocol from developers and provides a high-level API that you can use to easily instrument Chrome/Chromium and automate browsing sessions. Puppeteer is used for tasks like creating screenshots, crawling pages, and testing web applications.</p>
<p>Puppeteer typically connects to a local Chrome or Chromium browser using the DevTools port. Refer to the <a href="https://pptr.dev/api/puppeteer.puppeteer.connect">Puppeteer API documentation on the <code>Puppeteer.connect()</code> method</a> for more information.</p>
<p>The Workers team forked a version of Puppeteer and patched it to connect to the Workers Browser Run API instead. After connecting, the developers can then use the full <a href="https://github.com/cloudflare/puppeteer/blob/main/docs/api/index.md">Puppeteer API</a> as they would on a standard setup.</p>
<p>Our version is open sourced and can be found in <a href="https://github.com/cloudflare/puppeteer">Cloudflare's fork of Puppeteer</a>. The npm can be installed from <a href="https://www.npmjs.com/">npmjs</a> as <a href="https://www.npmjs.com/package/@cloudflare/puppeteer">@cloudflare/puppeteer</a>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1407.md")
</aside>
<h2 id="use-puppeteer-in-a-worker">Use Puppeteer in a Worker</h2>
<p>Once the <a href="/browser-run/reference/wrangler/#bindings">browser binding</a> is configured and the <code>@cloudflare/puppeteer</code> library is installed, Puppeteer can be used in a Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1408.md")
</div>
<p>This script <a href="https://pptr.dev/api/puppeteer.puppeteernode.launch">launches</a> the <code>env.MYBROWSER</code> browser, opens a <a href="https://pptr.dev/api/puppeteer.browser.newpage">new page</a>, <a href="https://pptr.dev/api/puppeteer.page.goto">goes to</a> <a href="https://example.com/">https://example.com/</a>, gets the page load <a href="https://pptr.dev/api/puppeteer.page.metrics">metrics</a>, <a href="https://pptr.dev/api/puppeteer.browser.close">closes</a> the browser and prints metrics in JSON.</p>
<h3 id="keep-alive">Keep Alive</h3>
<p>If users omit the <code>browser.close()</code> statement, it will stay open, ready to be connected to again and <a href="/browser-run/features/reuse-sessions/">re-used</a> but it will, by default, close automatically after 1 minute of inactivity. Users can optionally extend this idle time up to 10 minutes, by using the <code>keep_alive</code> option, set in milliseconds:</p>
<pre><code class="language-js">const browser = await puppeteer.launch(env.MYBROWSER, { keep_alive: 600000 });&#10;</code></pre>
<p>Using the above, the browser will stay open for up to 10 minutes, even if inactive.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1406.md")
</aside>
<h3 id="set-a-custom-user-agent">Set a custom user agent</h3>
<p>To specify a custom user agent in Puppeteer, use the <code>page.setUserAgent()</code> method. This is useful if the target website serves different content based on the user agent.</p>
<pre><code class="language-js">await page.setUserAgent(&#10;	&quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36&quot;,&#10;);&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1405.md")
</aside>
<h2 id="local-debugging-with-headful-mode-experimental">Local debugging with headful mode (experimental)</h2>
<p>When developing locally with <code>wrangler dev</code> or <code>vite dev</code>, Chrome runs in headless mode by default. To launch Chrome in visible (headful) mode, set the <code>X_BROWSER_HEADFUL</code> environment variable:</p>
<pre><code class="language-sh">X_BROWSER_HEADFUL=true npx wrangler dev&#10;</code></pre>
<p>Or with the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>:</p>
<pre><code class="language-sh">X_BROWSER_HEADFUL=true npx vite dev&#10;</code></pre>
<p>This opens a browser window so you can watch your Puppeteer automation in real time, making it easier to debug navigation, element selection, and page interactions.</p>
<h2 id="element-selection">Element selection</h2>
<p>Puppeteer provides multiple methods for selecting elements on a page. While CSS selectors work as expected, XPath selectors are not supported due to security constraints in the Workers runtime.</p>
<p>Instead of using Xpath selectors, you can use CSS selectors or <code>page.evaluate()</code> to run XPath queries in the browser context:</p>
<pre><code class="language-ts">const innerHtml = await page.evaluate(() =&gt; {&#10;	return (&#10;		// @ts-ignore this runs on browser context&#10;		new XPathEvaluator()&#10;			.createExpression(&quot;/html/body/div/h1&quot;)&#10;			// @ts-ignore this runs on browser context&#10;			.evaluate(document, XPathResult.FIRST_ORDERED_NODE_TYPE).singleNodeValue&#10;			.innerHTML&#10;	);&#10;});&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1404.md")
</aside>
<h2 id="session-management">Session management</h2>
<p>In order to facilitate browser session management, we've added new methods to <code>puppeteer</code>:</p>
<h3 id="list-open-sessions">List open sessions</h3>
<p><code>puppeteer.sessions()</code> lists the current running sessions. It will return an output similar to this:</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;connectionId&quot;: &quot;2a2246fa-e234-4dc1-8433-87e6cee80145&quot;,&#10;		&quot;connectionStartTime&quot;: 1711621704607,&#10;		&quot;sessionId&quot;: &quot;478f4d7d-e943-40f6-a414-837d3736a1dc&quot;,&#10;		&quot;startTime&quot;: 1711621703708&#10;	},&#10;	{&#10;		&quot;sessionId&quot;: &quot;565e05fb-4d2a-402b-869b-5b65b1381db7&quot;,&#10;		&quot;startTime&quot;: 1711621703808&#10;	}&#10;]&#10;</code></pre>
<p>Notice that the session <code>478f4d7d-e943-40f6-a414-837d3736a1dc</code> has an active worker connection (<code>connectionId=2a2246fa-e234-4dc1-8433-87e6cee80145</code>), while session <code>565e05fb-4d2a-402b-869b-5b65b1381db7</code> is free. While a connection is active, no other workers may connect to that session.</p>
<h3 id="list-recent-sessions">List recent sessions</h3>
<p><code>puppeteer.history()</code> lists recent sessions, both open and closed. It's useful to get a sense of your current usage.</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;closeReason&quot;: 2,&#10;		&quot;closeReasonText&quot;: &quot;BrowserIdle&quot;,&#10;		&quot;endTime&quot;: 1711621769485,&#10;		&quot;sessionId&quot;: &quot;478f4d7d-e943-40f6-a414-837d3736a1dc&quot;,&#10;		&quot;startTime&quot;: 1711621703708&#10;	},&#10;	{&#10;		&quot;closeReason&quot;: 1,&#10;		&quot;closeReasonText&quot;: &quot;NormalClosure&quot;,&#10;		&quot;endTime&quot;: 1711123501771,&#10;		&quot;sessionId&quot;: &quot;2be00a21-9fb6-4bb2-9861-8cd48e40e771&quot;,&#10;		&quot;startTime&quot;: 1711123430918&#10;	}&#10;]&#10;</code></pre>
<p>Session <code>2be00a21-9fb6-4bb2-9861-8cd48e40e771</code> was closed explicitly with <code>browser.close()</code> by the client, while session <code>478f4d7d-e943-40f6-a414-837d3736a1dc</code> was closed due to reaching the maximum idle time (check <a href="/browser-run/limits/">limits</a>).</p>
<p>You should also be able to access this information in the dashboard, albeit with a slight delay.</p>
<h3 id="active-limits">Active limits</h3>
<p><code>puppeteer.limits()</code> lists your active limits:</p>
<pre><code class="language-json">{&#10;	&quot;activeSessions&quot;: [&#10;		{ &quot;id&quot;: &quot;478f4d7d-e943-40f6-a414-837d3736a1dc&quot; },&#10;		{ &quot;id&quot;: &quot;565e05fb-4d2a-402b-869b-5b65b1381db7&quot; }&#10;	],&#10;	&quot;allowedBrowserAcquisitions&quot;: 1,&#10;	&quot;maxConcurrentSessions&quot;: 2,&#10;	&quot;timeUntilNextAllowedBrowserAcquisition&quot;: 0&#10;}&#10;</code></pre>
<ul>
<li><code>activeSessions</code> lists the IDs of the current open sessions</li>
<li><code>maxConcurrentSessions</code> defines how many browsers can be open at the same time</li>
<li><code>allowedBrowserAcquisitions</code> specifies if a new browser session can be opened according to the rate <a href="/browser-run/limits/">limits</a> in place</li>
<li><code>timeUntilNextAllowedBrowserAcquisition</code> defines the waiting period before a new browser can be launched.</li>
</ul>
<h2 id="puppeteer-api">Puppeteer API</h2>
<p>The full Puppeteer API can be found in the <a href="https://github.com/cloudflare/puppeteer/blob/main/docs/api/index.md">Cloudflare's fork of Puppeteer</a>.</p>
