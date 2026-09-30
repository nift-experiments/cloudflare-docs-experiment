<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 19, 2025</time><h2 id="post-title">Static prerendering support for TanStack Start</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="https://tanstack.com/start/">TanStack Start</a> apps can now prerender routes to static HTML at build time with access to build time environment variables
and bindings,  and serve them as <a href="/workers/static-assets/">static assets</a>. To enable prerendering, configure the <code>prerender</code> option of the TanStack Start plugin in your Vite config:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;&#10;export default defineConfig({&#10;  plugins: [&#10;    cloudflare({ viteEnvironment: { name: &quot;ssr&quot; } }),&#10;    tanstackStart({&#10;      prerender: {&#10;        enabled: true,&#10;      },&#10;    }),&#10;  ],&#10;});&#10;</code></pre>
<p>This feature requires <code>@tanstack/react-start</code> v1.138.0 or later. See the <a href="/workers/framework-guides/web-apps/tanstack-start/#static-prerendering">TanStack Start framework guide</a> for more details.</p>
</div></article></div>
