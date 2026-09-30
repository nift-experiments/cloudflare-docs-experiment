<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 20, 2026</time><h2 id="post-title">Use auxiliary Workers alongside full-stack frameworks</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Auxiliary Workers are now fully supported when using full-stack frameworks, such as <a href="/workers/framework-guides/web-apps/react-router/">React Router</a> and <a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start</a>, that integrate with the <a href="/workers/vite-plugin/reference/api/">Cloudflare Vite plugin</a>.
They are included alongside the framework's build output in the build output directory.
Note that this feature requires Vite 7 or above.</p>
<p>Auxiliary Workers are additional Workers that can be called via <a href="/workers/runtime-apis/bindings/service-bindings/">service bindings</a> from your main (entry) Worker.
They are defined in the plugin config, as in the example below:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		tanstackStart(),&#10;		cloudflare({&#10;			viteEnvironment: { name: &quot;ssr&quot; },&#10;			auxiliaryWorkers: [{ configPath: &quot;./wrangler.aux.jsonc&quot; }],&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>See the Vite plugin <a href="/workers/vite-plugin/reference/api/">API docs</a> for more info.</p>
</div></article></div>
