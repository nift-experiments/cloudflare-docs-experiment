<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16028.md")
</aside>
<h2 id="start-with-a-basic-package-json">Start with a basic <code>package.json</code></h2>
<pre><code class="language-json">{&#10;	&quot;name&quot;: &quot;cloudflare-vite-get-started&quot;,&#10;	&quot;private&quot;: true,&#10;	&quot;version&quot;: &quot;0.0.0&quot;,&#10;	&quot;type&quot;: &quot;module&quot;,&#10;	&quot;scripts&quot;: {&#10;		&quot;dev&quot;: &quot;vite dev&quot;,&#10;		&quot;build&quot;: &quot;vite build&quot;,&#10;		&quot;preview&quot;: &quot;npm run build &amp;&amp; vite preview&quot;,&#10;		&quot;deploy&quot;: &quot;npm run build &amp;&amp; wrangler deploy&quot;&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16027.md")
</aside>
<h2 id="install-the-dependencies">Install the dependencies</h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i vite @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i vite @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add vite @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add vite @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add vite @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add vite @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add vite @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add vite @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="create-your-vite-config-file-and-include-the-cloudflare-plugin">Create your Vite config file and include the Cloudflare plugin</h2>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [cloudflare()],&#10;});&#10;</code></pre>
<p>The Cloudflare Vite plugin doesn't require any configuration by default and will look for a <code>wrangler.jsonc</code>, <code>wrangler.json</code> or <code>wrangler.toml</code> in the root of your application.</p>
<p>Refer to the <a href="/workers/vite-plugin/reference/api/">API reference</a> for configuration options.</p>
<h2 id="create-your-worker-config-file">Create your Worker config file</h2>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16029.md")
</div>
<p>The <code>name</code> field specifies the name of your Worker.
By default, this is also used as the name of the Worker's Vite Environment (see <a href="/workers/vite-plugin/reference/vite-environments/">Vite Environments</a> for more information).
The <code>main</code> field specifies the entry file for your Worker code.</p>
<p>For more information about the Worker configuration, see <a href="/workers/wrangler/configuration/">Configuration</a>.</p>
<h2 id="create-your-worker-entry-file">Create your Worker entry file</h2>
<pre><code class="language-ts">export default {&#10;	fetch() {&#10;		return new Response(`Running in ${navigator.userAgent}!`);&#10;	},&#10;};&#10;</code></pre>
<p>A request to this Worker will return <strong>'Running in Cloudflare-Workers!'</strong>, demonstrating that the code is running inside the Workers runtime.</p>
<h2 id="dev-build-preview-and-deploy">Dev, build, preview and deploy</h2>
<p>You can now start the Vite development server (<code>npm run dev</code>), build the application (<code>npm run build</code>), preview the built application (<code>npm run preview</code>), and deploy to Cloudflare (<code>npm run deploy</code>).</p>
