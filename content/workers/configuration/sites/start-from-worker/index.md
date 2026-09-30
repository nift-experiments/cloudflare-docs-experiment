<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-workers-static-assets-instead">Use Workers Static Assets Instead</h3>
@markup("md", "content/.markup/bodies/16794.md")
</aside>
<p>Workers Sites require <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler">Wrangler</a> — make sure to use the <a href="/workers/wrangler/install-and-update/#update-wrangler">latest version</a>.</p>
<p>If you have a pre-existing Worker project, you can use Workers Sites to serve static assets to the Worker.</p>
<h2 id="getting-started">Getting started</h2>
<ol>
<li>
<p>Create a directory that will contain the assets in the root of your project (for example, <code>./public</code>)</p>
</li>
<li>
<p>Add configuration to your Wrangler file to point to it.</p>
</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16795.md")
</div>
<ol start="3">
<li>Install the <code>@cloudflare/kv-asset-handler</code> package in your project:</li>
</ol>
<pre><code class="language-sh">npm i -D @cloudflare/kv-asset-handler&#10;</code></pre>
<ol start="4">
<li>Import the <code>getAssetFromKV()</code> function into your Worker entry point and use it to respond with static assets.</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16798.md")
</div></div>
<p>For more information on the configurable options of <code>getAssetFromKV()</code> refer to <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/kv-asset-handler">kv-asset-handler docs</a>.</p>
<ol start="5">
<li>Run <code>wrangler deploy</code> or <code>npx wrangler deploy</code> as you would normally with your Worker project.
Wrangler will automatically upload the assets found in the configured directory.</li>
</ol>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
