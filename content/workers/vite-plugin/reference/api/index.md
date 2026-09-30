---
cp9:
  canonical: https://developers.cloudflare.com/workers/vite-plugin/reference/api/
  description: Vite plugin API
  full_title: API · Cloudflare Workers docs
  head_html: <title>API · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Vite plugin API"><link rel="canonical" href="https://developers.cloudflare.com/workers/vite-plugin/reference/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/vite-plugin/reference/api/index.md"><meta property="og:title" content="API · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Vite plugin API"><meta property="og:url" content="https://developers.cloudflare.com/workers/vite-plugin/reference/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/vite-plugin/reference/api/#page","headline":"API \u00b7 Cloudflare Workers docs","description":"Vite plugin API","url":"https://developers.cloudflare.com/workers/vite-plugin/reference/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/vite-plugin/reference/api/
  schema: 1
---
<h2 id="cloudflare"><code>cloudflare()</code></h2>
<p>The <code>cloudflare</code> plugin should be included in the Vite <code>plugins</code> array:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [cloudflare()],&#10;});&#10;</code></pre>
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
