<p>Run your Pages application locally with our Wrangler Command Line Interface (CLI).</p>
<h2 id="install-wrangler">Install Wrangler</h2>
<p>To get started with Wrangler, refer to the <a href="/workers/wrangler/install-and-update/">Install/Update Wrangler</a>.</p>
<h2 id="run-your-pages-project-locally">Run your Pages project locally</h2>
<p>The main command for local development on Pages is <code>wrangler pages dev</code>. This will let you run your Pages application locally, which includes serving static assets and running your Functions.</p>
<p>With your folder of static assets set up, run the following command to start local development:</p>
<pre><code class="language-sh">npx wrangler pages dev &lt;DIRECTORY-OF-ASSETS&gt;&#10;</code></pre>
<p>This will then start serving your Pages project. You can press <code>b</code> to open the browser on your local site, (available, by default, on <a href="http://localhost:8788">http://localhost:8788</a>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10950.md")
</aside>
<h3 id="https-support">HTTPS support</h3>
<p>To serve your local development server over HTTPS with a self-signed certificate, you can [set <code>local_protocol</code> via the <a href="/pages/functions/wrangler-configuration/#local-development-settings">Wrangler configuration file</a> or you can pass the <code>--local-protocol=https</code> argument to <a href="/workers/wrangler/commands/pages/#pages-dev"><code>wrangler pages dev</code></a>:</p>
<pre><code class="language-sh">npx wrangler pages dev --local-protocol=https &lt;DIRECTORY-OF-ASSETS&gt;&#10;</code></pre>
<h2 id="attach-bindings-to-local-development">Attach bindings to local development</h2>
<p>To attach a binding to local development, refer to <a href="/pages/functions/bindings/">Bindings</a> and find the Cloudflare Developer Platform resource you would like to work with.</p>
<h2 id="additional-wrangler-configuration">Additional Wrangler configuration</h2>
<p>If you are using a Wrangler configuration file in your project, you can set up dev server values like: <code>port</code>, <code>local protocol</code>, <code>ip</code>, and <code>port</code>. For more information, read about <a href="/pages/functions/wrangler-configuration/#local-development-settings">configuring local development settings</a>.</p>
