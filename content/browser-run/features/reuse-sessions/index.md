<p>By default, each Browser Sessions request launches a new browser instance. Reusing sessions eliminates cold-start time and improves performance by reconnecting to an existing browser instead of launching a new one.</p>
<p>This feature applies to Browser Sessions (<a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, and <a href="/browser-run/cdp/">CDP</a>). <a href="/browser-run/quick-actions/">Quick Actions</a> handle session lifecycle automatically.</p>
<p>There are two approaches to reusing sessions:</p>
<ul>
<li><strong>Disconnect and reconnect</strong> (covered in this page): Use <code>browser.disconnect()</code> instead of <code>browser.close()</code> to keep the browser alive, then reconnect to it on the next request. Best for stateless workloads where any available browser session will do.</li>
<li><strong><a href="/browser-run/how-to/browser-run-with-do/">Durable Objects</a></strong>: Persist a long-running browser inside a Durable Object for stateful session management. Best when you need to maintain state across requests or route specific users to specific browser instances.</li>
</ul>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p><a href="/workers/">Cloudflare Workers</a> provides a serverless execution environment that allows you to create new applications or augment existing ones without configuring or maintaining infrastructure. Your Worker application is a container to interact with a headless browser to do actions, such as taking screenshots.</p>
<p>Create a new Worker project named <code>browser-worker</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- browser-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare browser-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest browser-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<h2 id="2-install-puppeteer"><ol start="2">
<li>Install Puppeteer</li>
</ol></h2>
<p>In your <code>browser-worker</code> directory, install Cloudflare's <a href="/browser-run/puppeteer/">fork of Puppeteer</a>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-configure-the-wrangler-configuration-file-workers-wrangler-configuration"><ol start="3">
<li>Configure the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3695.md")
</aside>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3696.md")
</div>
<h2 id="4-code"><ol start="4">
<li>Code</li>
</ol></h2>
<p>The script below starts by fetching the current running sessions. If there are any that do not already have a worker connection, it picks a random session ID and attempts to connect (<code>puppeteer.connect(..)</code>) to it. If that fails or there were no running sessions to start with, it launches a new browser session (<code>puppeteer.launch(..)</code>). Then, it goes to the website and fetches the dom. Once that is done, it disconnects (<code>browser.disconnect()</code>), making the connection available to other workers.</p>
<p>Take into account that if the browser is idle, i.e. does not get any command, for more than the current <a href="/browser-run/limits/">limit</a>, it will close automatically, so you must have enough requests per minute to keep it alive.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3697.md")
</div>
<p>Besides <code>puppeteer.sessions()</code>, we have added other methods to facilitate <a href="/browser-run/puppeteer/#session-management">Session Management</a>.</p>
<h2 id="5-test"><ol start="5">
<li>Test</li>
</ol></h2>
<p>Run <code>npx wrangler dev</code> to test your Worker locally.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="use-real-headless-browser-during-local-development">Use real headless browser during local development</h3>
@markup("md", "content/.markup/bodies/3694.md")
</aside>
<p>To test go to the following URL:</p>
<pre><code>&lt;LOCAL_HOST_URL&gt;/?url=https://example.com&#10;</code></pre>
<h2 id="6-deploy"><ol start="6">
<li>Deploy</li>
</ol></h2>
<p>Run <code>npx wrangler deploy</code> to deploy your Worker to the Cloudflare global network and then to go to the following URL:</p>
<pre><code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/?url=https://example.com&#10;</code></pre>
