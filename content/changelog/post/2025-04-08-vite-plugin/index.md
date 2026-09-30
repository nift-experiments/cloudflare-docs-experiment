<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 8, 2025</time><h2 id="post-title">The Cloudflare Vite plugin is now Generally Available</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> has <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">reached v1.0</a> and is now Generally Available (&quot;GA&quot;).</p>
<p>When you use <code>@cloudflare/vite-plugin</code>, you can use Vite's local development server and build tooling, while ensuring that while developing, your code runs in <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>, the open-source Workers runtime.</p>
<p>This lets you get the best of both worlds for a full-stack app — you can use <a href="https://vite.dev/guide/features.html#hot-module-replacement">Hot Module Replacement</a> from Vite right alongside <a href="/durable-objects/">Durable Objects</a> and other runtime APIs and bindings that are unique to Cloudflare Workers.</p>
<p><code>@cloudflare/vite-plugin</code> is made possible by the new <a href="https://vite.dev/guide/api-environment">environment API</a> in Vite, and was built <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">in partnership with the Vite team</a>.</p>
<h4 id="framework-support">Framework support</h4>
<p>You can build any type of application with <code>@cloudflare/vite-plugin</code>, using any rendering mode, from single page applications (SPA) and static sites to server-side rendered (SSR) pages and API routes.</p>
<p><a href="/workers/framework-guides/web-apps/react-router/">React Router v7 (Remix)</a> is the first full-stack framework to provide full support for Cloudflare Vite plugin, allowing you to use all parts of Cloudflare's developer platform, without additional build steps.</p>
<p>You can also build complete full-stack apps on Workers <strong>without a framework</strong> — <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">&quot;just use Vite&quot;</a> and React together, and build a back-end API in the same Worker. Follow our <a href="/workers/vite-plugin/tutorial/">React SPA with an API tutorial</a> to learn how.</p>
<h4 id="configuration">Configuration</h4>
<p>If you're already using <a href="https://vite.dev/">Vite</a> in your build and development toolchain, you can start using our plugin with minimal changes to your <code>vite.config.ts</code>:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [cloudflare()],&#10;});&#10;</code></pre>
<p>Take a look at the <a href="/workers/vite-plugin/">documentation for our Cloudflare Vite plugin</a> for more information!</p>
</div></article></div>
