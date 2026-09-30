<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-workers-static-assets-instead">Use Workers Static Assets Instead</h3>
@markup("md", "content/.markup/bodies/16806.md")
</aside>
<p>Workers Sites require <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler">Wrangler</a> — make sure to use the <a href="/workers/wrangler/install-and-update/#update-wrangler">latest version</a>.</p>
<p>To deploy a pre-existing static site project, start with a pre-generated site. Workers Sites works with all static site generators, for example:</p>
<ul>
<li><a href="https://gohugo.io/getting-started/quick-start/">Hugo</a></li>
<li><a href="https://www.gatsbyjs.org/docs/quick-start/">Gatsby</a>, requires Node</li>
<li><a href="https://jekyllrb.com/docs/">Jekyll</a>, requires Ruby</li>
<li><a href="https://www.11ty.io/#quick-start">Eleventy</a>, requires Node</li>
<li><a href="https://wordpress.org">WordPress</a> (refer to the tutorial on <a href="/pages/how-to/deploy-a-wordpress-site/">deploying static WordPress sites with Pages</a>)</li>
</ul>
<h2 id="getting-started">Getting started</h2>
<ol>
<li>Run the <code>wrangler init</code> command in the root of your project's directory to generate a basic Worker:</li>
</ol>
<pre><code class="language-sh">wrangler init -y&#10;</code></pre>
<p>This command adds/update the following files:</p>
<ul>
<li><code>wrangler.jsonc</code>: The file containing project configuration.</li>
<li><code>package.json</code>: Wrangler <code>devDependencies</code> are added.</li>
<li><code>tsconfig.json</code>: Added if not already there to support writing the Worker in TypeScript.</li>
<li><code>src/index.ts</code>: A basic Cloudflare Worker, written in TypeScript.</li>
</ul>
<ol start="2">
<li>Add your site's build/output directory to the Wrangler file:</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16807.md")
</div>
<p>The default directories for the most popular static site generators are listed below:</p>
<ul>
<li>Hugo: <code>public</code></li>
<li>Gatsby: <code>public</code></li>
<li>Jekyll: <code>_site</code></li>
<li>Eleventy: <code>_site</code></li>
</ul>
<ol start="3">
<li>Install the <code>@cloudflare/kv-asset-handler</code> package in your project:</li>
</ol>
<pre><code class="language-sh">npm i -D @cloudflare/kv-asset-handler&#10;</code></pre>
<ol start="4">
<li>Replace the contents of <code>src/index.ts</code> with the following code snippet:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16810.md")
</div></div>
<ol start="5">
<li>Run <code>wrangler dev</code> or <code>npx wrangler deploy</code> to preview or deploy your site on Cloudflare.
Wrangler will automatically upload the assets found in the configured directory.</li>
</ol>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<ol start="6">
<li>Deploy your site to a <a href="/workers/configuration/routing/custom-domains/">custom domain</a> that you own and have already attached as a Cloudflare zone. Add a <code>route</code> property to the Wrangler file.</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16811.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16804.md")
</aside>
<p>Learn more about <a href="/workers/wrangler/configuration/">configuring your project</a>.</p>
