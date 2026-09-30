<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 24, 2025</time><h2 id="post-title">Build TanStack Start apps with the Cloudflare Vite plugin</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> now supports <a href="https://tanstack.com/start/">TanStack Start</a> apps.
Get started with new or existing projects.</p>
<h4 id="new-projects">New projects</h4>
<p>Create a new TanStack Start project that uses the Cloudflare Vite plugin via the <code>create-cloudflare</code> CLI:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="existing-projects">Existing projects</h4>
<p>Migrate an existing TanStack Start project to use the Cloudflare Vite plugin:</p>
<ol>
<li>Install <code>@cloudflare/vite-plugin</code> and <code>wrangler</code></li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="2">
<li>Add the Cloudflare plugin to your Vite config</li>
</ol>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;import viteReact from &quot;@vitejs/plugin-react&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({ viteEnvironment: { name: &quot;ssr&quot; } }),&#10;		tanstackStart(),&#10;		viteReact(),&#10;	],&#10;});&#10;</code></pre>
<ol start="3">
<li>Add your Worker config file</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17789.md")</div>
<ol start="4">
<li>Modify the scripts in your <code>package.json</code></li>
</ol>
<pre><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;dev&quot;: &quot;vite dev&quot;,&#10;		&quot;build&quot;: &quot;vite build &amp;&amp; tsc --noEmit&quot;,&#10;		&quot;start&quot;: &quot;node .output/server/index.mjs&quot;,&#10;		&quot;preview&quot;: &quot;vite preview&quot;,&#10;		&quot;deploy&quot;: &quot;npm run build &amp;&amp; wrangler deploy&quot;,&#10;		&quot;cf-typegen&quot;: &quot;wrangler types&quot;&#10;	}&#10;}&#10;</code></pre>
<p>See the <a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start framework guide</a> for more info.</p>
</div></article></div>
