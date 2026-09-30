<p>You can use <a href="https://pptr.dev/">Puppeteer</a> to connect to Browser Run sessions from any Node.js environment and automate browser tasks programmatically via CDP. This is useful for scripts running on your local machine, CI/CD pipelines, or external servers.</p>
<p>Before you begin, <a href="/fundamentals/api/get-started/create-token/">create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Node.js installed on your machine</li>
<li>A Cloudflare account with Browser Run enabled</li>
<li>A Browser Run API token with <code>Browser Rendering - Edit</code> permissions</li>
</ul>
<h2 id="install-puppeteer">Install Puppeteer</h2>
<p>Install the <code>puppeteer-core</code> package (the version without bundled Chrome):</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i puppeteer-core</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i puppeteer-core" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add puppeteer-core</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add puppeteer-core" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add puppeteer-core</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add puppeteer-core" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add puppeteer-core</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add puppeteer-core" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="connect-to-browser-run">Connect to Browser Run</h2>
<p>The following script demonstrates how to connect to a Browser Run session, navigate to a page, extract the title, and take a screenshot.</p>
<p>Create a file named <code>script.js</code>:</p>
<pre><code class="language-js">const puppeteer = require(&quot;puppeteer-core&quot;);&#10;&#10;const ACCOUNT_ID = process.env.CF_ACCOUNT_ID || &quot;&lt;ACCOUNT_ID&gt;&quot;;&#10;const API_TOKEN = process.env.CF_API_TOKEN || &quot;&lt;API_TOKEN&gt;&quot;;&#10;&#10;const browserWSEndpoint = `wss://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/browser-rendering/devtools/browser?keep_alive=600000`;&#10;&#10;async function main() {&#10;	const browser = await puppeteer.connect({&#10;		browserWSEndpoint,&#10;		headers: {&#10;			Authorization: `Bearer ${API_TOKEN}`,&#10;		},&#10;	});&#10;&#10;	const page = await browser.newPage();&#10;	await page.goto(&quot;https://developers.cloudflare.com&quot;);&#10;&#10;	const title = await page.title();&#10;	console.log(`Page title: ${title}`);&#10;&#10;	await page.screenshot({ path: &quot;screenshot.png&quot; });&#10;&#10;	await browser.close();&#10;}&#10;&#10;main().catch(console.error);&#10;</code></pre>
<p>Replace <code>ACCOUNT_ID</code> with your Cloudflare account ID and <code>API_TOKEN</code> with your Browser Run API token, or set them as environment variables:</p>
<pre><code class="language-bash">export CF_ACCOUNT_ID=&quot;&lt;ACCOUNT_ID&gt;&quot;&#10;export CF_API_TOKEN=&quot;&lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<h2 id="run-the-script">Run the script</h2>
<pre><code class="language-bash">node script.js&#10;</code></pre>
<p>You should see the page title printed to the console and a screenshot saved as <code>screenshot.png</code>.</p>
<h2 id="how-it-works">How it works</h2>
<p>The script connects directly to Browser Run via WebSocket using the CDP protocol:</p>
<ol>
<li><strong>WebSocket endpoint</strong> - The <code>browserWSEndpoint</code> URL acquires a new browser session and connects to it via WebSocket</li>
<li><strong>Authentication</strong> - The <code>Authorization</code> header with your API token authenticates the request</li>
<li><strong>Keep-alive</strong> - The <code>keep_alive</code> parameter (in milliseconds) specifies how long the session stays active</li>
<li><strong>Puppeteer API</strong> - Once connected, you use the standard Puppeteer API to control the browser</li>
</ol>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
