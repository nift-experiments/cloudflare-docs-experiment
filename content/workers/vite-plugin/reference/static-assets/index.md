<p>This guide focuses on the areas of working with static assets that are unique to the Vite plugin.
For more general documentation, see <a href="/workers/static-assets/">Static Assets</a>.</p>
<h2 id="configuration">Configuration</h2>
<p>The Vite plugin does not require that you provide the <code>assets</code> field in order to enable assets and instead determines whether assets should be included based on whether the <code>client</code> environment has been built. By default, the <code>client</code> environment is built if any of the following conditions are met:</p>
<ul>
<li>There is an <code>index.html</code> file in the root of your project</li>
<li><code>build.rollupOptions.input</code> or <code>environments.client.build.rollupOptions.input</code> is specified in your Vite config</li>
<li>You have a non-empty <a href="https://vite.dev/guide/assets#the-public-directory"><code>public</code> directory</a></li>
<li>Your Worker <a href="https://vite.dev/guide/assets#importing-asset-as-url">imports assets as URLs</a></li>
</ul>
<p>On running <code>vite build</code>, an output <code>wrangler.json</code> configuration file is generated as part of the build output.
The <code>assets.directory</code> field in this file is automatically populated with the path to your <code>client</code> build output.
It is therefore not necessary to provide the <code>assets.directory</code> field in your input Worker configuration.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cloudflare-access-context">Cloudflare Access context</h3>
@markup("md", "content/.markup/bodies/17384.md")
</aside>
<p>The <code>assets</code> configuration should be used, however, if you wish to set <a href="/workers/static-assets/routing/">routing configuration</a> or enable the <a href="/workers/static-assets/binding/#binding">assets binding</a>.
The following example configures the <code>not_found_handling</code> for a single-page application so that the fallback will always be the root <code>index.html</code> file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17385.md")
</div>
<h2 id="features">Features</h2>
<p>The Vite plugin ensures that all of Vite's <a href="https://vite.dev/guide/assets">static asset handling</a> features are supported in your Worker as well as in your frontend.
These include importing assets as URLs, importing as strings and importing from the <code>public</code> directory as well as inlining assets.</p>
<p>Assets <a href="https://vite.dev/guide/assets#importing-asset-as-url">imported as URLs</a> can be fetched via the <a href="/workers/static-assets/binding/#binding">assets binding</a>.
As the binding's <code>fetch</code> method requires a full URL, we recommend using the request URL as the <code>base</code>.
This is demonstrated in the following example:</p>
<pre><code class="language-ts">import myImage from &quot;./my-image.png&quot;;&#10;&#10;export default {&#10;	fetch(request, env) {&#10;		return env.ASSETS.fetch(new URL(myImage, request.url));&#10;	},&#10;};&#10;</code></pre>
<p>Assets imported as URLs in your Worker will automatically be moved to the client build output.
When running <code>vite build</code> the paths of any moved assets will be displayed in the console.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17383.md")
</aside>
<h2 id="headers-and-redirects">Headers and redirects</h2>
<p>Custom <a href="/workers/static-assets/headers/">headers</a> and <a href="/workers/static-assets/redirects/">redirects</a> are supported at build, preview and deploy time by adding <code>_headers</code> and <code>_redirects</code> files to your <a href="https://vite.dev/guide/assets#the-public-directory"><code>public</code> directory</a>.
The paths in these files should reflect the structure of your client build output.
For example, generated assets are typically located in an <a href="https://vite.dev/config/build-options#build-assetsdir">assets subdirectory</a>.</p>
