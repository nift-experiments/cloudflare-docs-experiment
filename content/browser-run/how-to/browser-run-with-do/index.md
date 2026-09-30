<p>By following this guide, you will create a Worker that uses the Browser Run API along with <a href="/durable-objects/">Durable Objects</a> to take screenshots from web pages and store them in <a href="/r2/">R2</a>.</p>
<p>Using Durable Objects to persist browser sessions improves performance by eliminating the time that it takes to spin up a new browser session. Since Durable Objects re-uses sessions, it reduces the number of concurrent sessions needed.</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3685.md")
</div></details>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p><a href="/workers/">Cloudflare Workers</a> provides a serverless execution environment that allows you to create new applications or augment existing ones without configuring or maintaining infrastructure. Your Worker application is a container to interact with a headless browser to do actions, such as taking screenshots.</p>
<p>Create a new Worker project named <code>browser-worker</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- browser-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare browser-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest browser-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="2-install-puppeteer"><ol start="2">
<li>Install Puppeteer</li>
</ol></h2>
<p>In your <code>browser-worker</code> directory, install Cloudflare’s <a href="/browser-run/puppeteer/">fork of Puppeteer</a>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-create-a-r2-bucket"><ol start="3">
<li>Create a R2 bucket</li>
</ol></h2>
<p>Create two R2 buckets, one for production, and one for development.</p>
<p>Note that bucket names must be lowercase and can only contain dashes.</p>
<pre><code class="language-sh">wrangler r2 bucket create screenshots&#10;wrangler r2 bucket create screenshots-test&#10;</code></pre>
<p>To check that your buckets were created, run:</p>
<pre><code class="language-sh">wrangler r2 bucket list&#10;</code></pre>
<p>After running the <code>list</code> command, you will see all bucket names, including the ones you have just created.</p>
<h2 id="4-configure-your-wrangler-configuration-file"><ol start="4">
<li>Configure your Wrangler configuration file</li>
</ol></h2>
<p>Configure your <code>browser-worker</code> project's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> by adding a browser <a href="/workers/runtime-apis/bindings/">binding</a> and a <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">Node.js compatibility flag</a>. Browser bindings allow for communication between a Worker and a headless browser which allows you to do actions such as taking a screenshot, generating a PDF and more.</p>
<p>Update your Wrangler configuration file with the Browser Run API binding, the R2 bucket you created and a Durable Object:</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3684.md")
</aside>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3686.md")
</div>
<h2 id="5-code"><ol start="5">
<li>Code</li>
</ol></h2>
<p>The code below uses Durable Object to instantiate a browser using Puppeteer. It then opens a series of web pages with different resolutions, takes a screenshot of each, and uploads it to R2.</p>
<p>The Durable Object keeps a browser session open for 60 seconds after last use. If a browser session is open, any requests will re-use the existing session rather than creating a new one. Update your Worker code by copy and pasting the following:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3687.md")
</div>
<h2 id="6-test"><ol start="6">
<li>Test</li>
</ol></h2>
<p>Run <code>npx wrangler dev</code> to test your Worker locally.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="use-real-headless-browser-during-local-development">Use real headless browser during local development</h3>
@markup("md", "content/.markup/bodies/3683.md")
</aside>
<h2 id="7-deploy"><ol start="7">
<li>Deploy</li>
</ol></h2>
<p>Run <a href="/workers/wrangler/commands/workers/#deploy"><code>npx wrangler deploy</code></a> to deploy your Worker to the Cloudflare global network.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Other <a href="https://github.com/cloudflare/puppeteer/tree/main/examples">Puppeteer examples</a></li>
<li>Get started with <a href="/durable-objects/get-started/">Durable Objects</a></li>
<li><a href="/r2/api/workers/workers-api-usage/">Using R2 from Workers</a></li>
</ul>
