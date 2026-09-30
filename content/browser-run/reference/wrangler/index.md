<p><a href="/workers/wrangler/">Wrangler</a> is a command-line tool for building with Cloudflare developer products.</p>
<p>Use Wrangler to deploy projects that use the Workers Browser Run API.</p>
<h2 id="install">Install</h2>
<p>To install Wrangler, refer to <a href="/workers/wrangler/install-and-update/">Install and Update Wrangler</a>.</p>
<h2 id="bindings">Bindings</h2>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to interact with resources on the Cloudflare developer platform. A browser binding will provide your Worker with an authenticated endpoint to interact with a dedicated Chromium browser instance.</p>
<p>To deploy a Browser Run Worker, you must declare a <a href="/workers/runtime-apis/bindings/">browser binding</a> in your Worker's Wrangler configuration file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3581.md")
</aside>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3582.md")
</div>
<p>After the binding is declared, access the DevTools endpoint using <code>env.MYBROWSER</code> in your Worker code:</p>
<pre><code class="language-javascript">const browser = await puppeteer.launch(env.MYBROWSER);&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="quick-actions-compatibility">Quick Actions compatibility</h3>
@markup("md", "content/.markup/bodies/3580.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="quick-actions-require-remote-mode-for-local-development">Quick Actions require remote mode for local development</h3>
@markup("md", "content/.markup/bodies/3579.md")
</aside>
<p>For Puppeteer, Playwright, or CDP-based Workers, run <code>npx wrangler dev</code> to test locally. For Quick Actions via <code>.quickAction()</code>, use <code>npx wrangler dev --remote</code> as noted above.</p>
<h3 id="headful-mode-experimental">Headful mode (experimental)</h3>
<p>By default, local development runs Chrome in headless mode. To launch Chrome in visible (headful) mode for debugging, set the <code>X_BROWSER_HEADFUL</code> environment variable:</p>
<pre><code class="language-sh">X_BROWSER_HEADFUL=true npx wrangler dev&#10;</code></pre>
<p>This opens a browser window on screen so you can watch navigations, interactions, and rendering in real time. Headful mode is for local development only and does not affect deployed Workers. This feature is experimental and may change without notice.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3578.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="use-real-headless-browser-during-local-development">Use real headless browser during local development</h3>
@markup("md", "content/.markup/bodies/3577.md")
</aside>
