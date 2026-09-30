<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 11, 2026</time><h2 id="post-title">Improved React Server Components support in the Cloudflare Vite plugin</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The Cloudflare Vite plugin now integrates seamlessly <a href="https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc">@vitejs/plugin-rsc</a>, the official Vite plugin for <a href="https://react.dev/reference/rsc/server-components">React Server Components</a>.</p>
<p>A <code>childEnvironments</code> option has been added to the plugin config to enable using multiple environments within a single Worker.
The parent environment can then import modules from a child environment in order to access a separate module graph.
For a typical RSC use case, the plugin might be configured as in the following example:</p>
<pre><code class="language-ts">export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			viteEnvironment: {&#10;				name: &quot;rsc&quot;,&#10;				childEnvironments: [&quot;ssr&quot;],&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p><code>@vitejs/plugin-rsc</code> provides the lower level functionality that frameworks, such as <a href="https://reactrouter.com/how-to/react-server-components">React Router</a>, build upon.
The GitHub repository includes a <a href="https://github.com/vitejs/vite-plugin-react/tree/f066114c3e6bf18f5209ff3d3ef6bf1ab46d3866/packages/plugin-rsc/examples/starter-cf-single">basic Cloudflare example</a>.</p>
</div></article></div>
