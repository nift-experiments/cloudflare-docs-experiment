<p>The <a href="https://vite.dev/guide/api-environment">Vite Environment API</a>, released in Vite 6, is the key feature that enables the Cloudflare Vite plugin to integrate Vite directly with the Workers runtime.
It is not necessary to understand all the intricacies of the Environment API as an end user, but it is useful to have a high-level understanding.</p>
<h2 id="default-behavior">Default behavior</h2>
<p>Vite creates two environments by default: <code>client</code> and <code>ssr</code>.
A front-end only application uses the <code>client</code> environment, whereas a full-stack application created with a framework typically uses the <code>client</code> environment for front-end code and the <code>ssr</code> environment for server-side rendering.</p>
<p>By default, when you add a Worker using the Cloudflare Vite plugin, an additional environment is created.
Its name is derived from the Worker name, with any dashes replaced with underscores.
This name can be used to reference the environment in your Vite config in order to apply environment specific configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17381.md")
</aside>
<h2 id="environment-configuration">Environment configuration</h2>
<p>In the following example we have a Worker named <code>my-worker</code> that is associated with a Vite environment named <code>my_worker</code>.
We use the Vite config to set global constant replacements for this environment:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17382.md")
</div>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	environments: {&#10;		my_worker: {&#10;			define: {&#10;				__APP_VERSION__: JSON.stringify(&quot;v1.0.0&quot;),&#10;			},&#10;		},&#10;	},&#10;	plugins: [cloudflare()],&#10;});&#10;</code></pre>
<p>For more information about Vite's configuration options, see <a href="https://vite.dev/config/">Configuring Vite</a>.</p>
<p>The default behavior of using the Worker name as the environment name is appropriate when you have a standalone Worker, such as an API that is accessed from your front-end application, or an <a href="/workers/vite-plugin/reference/api/#interface-pluginconfig">auxiliary Worker</a> that is accessed via service bindings.</p>
<h2 id="full-stack-frameworks">Full-stack frameworks</h2>
<p>If you are using the Cloudflare Vite plugin with <a href="https://tanstack.com/start/">TanStack Start</a> or <a href="https://reactrouter.com/">React Router v8</a>, then your Worker is used for server-side rendering and tightly integrated with the framework.
To support this, you should assign it to the <code>ssr</code> environment by setting <code>viteEnvironment.name</code> in the plugin config.</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;import { reactRouter } from &quot;@react-router/dev/vite&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [cloudflare({ viteEnvironment: { name: &quot;ssr&quot; } }), reactRouter()],&#10;});&#10;</code></pre>
<p>This merges the Worker's environment configuration with the framework's SSR configuration and ensures that the Worker is included as part of the framework's build output.</p>
