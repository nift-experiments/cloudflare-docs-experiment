<h2 id="cloudflare"><code>cloudflare()</code></h2>
<p>The <code>cloudflare</code> plugin should be included in the Vite <code>plugins</code> array:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [cloudflare()],&#10;});&#10;</code></pre>
<p>It accepts an optional <code>PluginConfig</code> parameter.</p>
<h2 id="interface-pluginconfig"><code>interface PluginConfig</code></h2>
<ul>
<li>
<p><code>configPath</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>An optional path to your entry Worker config file.</p>
<p>For the entry Worker, the plugin resolves the config path in this order:</p>
<ol>
<li><code>configPath</code></li>
<li><code>CLOUDFLARE_VITE_WRANGLER_CONFIG_PATH</code> (typically set by a framework or other external tool)</li>
<li><code>wrangler.jsonc</code>, <code>wrangler.json</code>, or <code>wrangler.toml</code> in the root of your application</li>
</ol>
<p>This applies in <code>vite dev</code> and <code>vite build</code>.</p>
<p>For more information about the Worker configuration, see <a href="/workers/wrangler/configuration/">Configuration</a>.</p>
</li>
<li>
<p><code>config</code> <span class="nb-type">WorkerConfigCustomizer&lt;true&gt;</span> <span class="nb-metainfo">optional</span></p>
<p>Customize or override Worker configuration programmatically.
Accepts a partial configuration object or a function that receives the current config.</p>
<p>Applied after any config file loads. Use it to override values, modify the existing config, or define Workers entirely in code.</p>
<p>See <a href="/workers/vite-plugin/reference/programmatic-configuration/">Programmatic configuration</a> for details.</p>
</li>
<li>
<p><code>viteEnvironment</code> <span class="nb-type">{ name?: string; childEnvironments?: string[] }</span> <span class="nb-metainfo">optional</span></p>
<p>Optional Vite environment options.
By default, the environment name is the Worker name with <code>-</code> characters replaced with <code>_</code>.
Setting the name here will override this.
A typical use case is setting <code>viteEnvironment: { name: &quot;ssr&quot; }</code> to apply the Worker to the SSR environment.</p>
<p>The <code>childEnvironments</code> option is for supporting React Server Components via <a href="https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc">@vitejs/plugin-rsc</a> and frameworks that build on top of it.
This enables embedding additional environments with separate module graphs inside a single Worker.</p>
<p>See <a href="/workers/vite-plugin/reference/vite-environments/">Vite Environments</a> for more information.</p>
</li>
<li>
<p><code>persistState</code> <span class="nb-type">boolean | { path: string }</span> <span class="nb-metainfo">optional</span></p>
<p>An optional override for state persistence.
By default, state is persisted to <code>.wrangler/state</code>.
A custom <code>path</code> can be provided or, alternatively, persistence can be disabled by setting the value to <code>false</code>.</p>
</li>
<li>
<p><code>inspectorPort</code> <span class="nb-type">number | false</span> <span class="nb-metainfo">optional</span></p>
<p>An optional override for debugging your Workers.
By default, the debugging inspector is enabled and listens on port <code>9229</code>.
A custom port can be provided or, alternatively, setting this to <code>false</code> will disable the debugging inspector.</p>
<p>See <a href="/workers/vite-plugin/reference/debugging/">Debugging</a> for more information.</p>
</li>
<li>
<p><code>tunnel</code> <span class="nb-type">boolean | { name?: string; autoStart?: boolean }</span> <span class="nb-metainfo">optional</span></p>
<p>Expose your local dev server over a <a href="/tunnel/">Cloudflare Tunnel</a>.</p>
<p>Provide an object to configure a named tunnel or control whether the tunnel starts automatically. Press <code>t + Enter</code> to start or close the tunnel. Set <code>tunnel.autoStart</code> to <code>true</code> if you want the tunnel to open when Vite starts.</p>
</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17403.md")
</div>
<p>See <a href="/workers/local-development/local-dev-tunnels/">Share a local dev server</a> for more information.</p>
<ul>
<li>
<p><code>auxiliaryWorkers</code> <span class="nb-type">Array&lt;AuxiliaryWorkerConfig&gt;</span> <span class="nb-metainfo">optional</span></p>
<p>An optional array of auxiliary Workers.
Auxiliary Workers are additional Workers that are used as part of your application.
You can use <a href="/workers/runtime-apis/bindings/service-bindings/">service bindings</a> to call auxiliary Workers from your main (entry) Worker.
All requests are routed through your entry Worker.
During the build, each Worker is output to a separate subdirectory of <code>dist</code>.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17402.md")
</aside>
<ul>
<li>
<p><code>remoteBindings</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<p>Whether or not <a href="/workers/local-development/#remote-bindings">remote bindings</a> should be enabled. Defaults to <code>true</code>.</p>
</li>
</ul>
<h2 id="interface-auxiliaryworkerconfig"><code>interface AuxiliaryWorkerConfig</code></h2>
<p>Auxiliary Workers require a <code>configPath</code>, a <code>config</code> option, or both.
<code>CLOUDFLARE_VITE_WRANGLER_CONFIG_PATH</code> only applies to the entry Worker. Auxiliary Workers do not use this environment variable. If you use a config file for an auxiliary Worker, set <code>configPath</code> explicitly.</p>
<ul>
<li>
<p><code>configPath</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The path to your Worker config file.
This field is required unless <code>config</code> is provided.</p>
<p>For more information about the Worker configuration, see <a href="/workers/wrangler/configuration/">Configuration</a>.</p>
</li>
<li>
<p><code>config</code> <span class="nb-type">WorkerConfigCustomizer&lt;false&gt;</span> <span class="nb-metainfo">optional</span></p>
<p>Customize or override Worker configuration programmatically.
When used without <code>configPath</code>, this allows defining auxiliary Workers entirely in code.</p>
<p>See <a href="/workers/vite-plugin/reference/programmatic-configuration/">Programmatic configuration</a> for usage examples.</p>
</li>
<li>
<p><code>viteEnvironment</code> <span class="nb-type">{ name?: string; childEnvironments?: string[] }</span> <span class="nb-metainfo">optional</span></p>
<p>Optional Vite environment options.
By default, the environment name is the Worker name with <code>-</code> characters replaced with <code>_</code>.
Setting the name here will override this.</p>
<p>The <code>childEnvironments</code> option is for supporting React Server Components via <a href="https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc">@vitejs/plugin-rsc</a> and frameworks that build on top of it.
This enables embedding additional environments with separate module graphs inside a single Worker.</p>
<p>See <a href="/workers/vite-plugin/reference/vite-environments/">Vite Environments</a> for more information.</p>
</li>
</ul>
