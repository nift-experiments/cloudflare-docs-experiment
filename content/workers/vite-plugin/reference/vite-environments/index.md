---
cp9:
  canonical: https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/
  description: Vite environments and the Vite plugin
  full_title: Vite Environments · Cloudflare Workers docs
  head_html: <title>Vite Environments · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Vite environments and the Vite plugin"><link rel="canonical" href="https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/index.md"><meta property="og:title" content="Vite Environments · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Vite environments and the Vite plugin"><meta property="og:url" content="https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/#page","headline":"Vite Environments \u00b7 Cloudflare Workers docs","description":"Vite environments and the Vite plugin","url":"https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/vite-plugin/reference/vite-environments/
  schema: 1
---
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
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	environments: {&#10;		my_worker: {&#10;			define: {&#10;				__APP_VERSION__: JSON.stringify(&quot;v1.0.0&quot;),&#10;			},&#10;		},&#10;	},&#10;	plugins: [cloudflare()],&#10;});&#10;</code></pre>
<p>For more information about Vite's configuration options, see <a href="https://vite.dev/config/">Configuring Vite</a>.</p>
<p>The default behavior of using the Worker name as the environment name is appropriate when you have a standalone Worker, such as an API that is accessed from your front-end application, or an <a href="/workers/vite-plugin/reference/api/#interface-pluginconfig">auxiliary Worker</a> that is accessed via service bindings.</p>
<h2 id="full-stack-frameworks">Full-stack frameworks</h2>
<p>If you are using the Cloudflare Vite plugin with <a href="https://tanstack.com/start/">TanStack Start</a> or <a href="https://reactrouter.com/">React Router v8</a>, then your Worker is used for server-side rendering and tightly integrated with the framework.
To support this, you should assign it to the <code>ssr</code> environment by setting <code>viteEnvironment.name</code> in the plugin config.</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;import { reactRouter } from &quot;@react-router/dev/vite&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [cloudflare({ viteEnvironment: { name: &quot;ssr&quot; } }), reactRouter()],&#10;});&#10;</code></pre>
<p>This merges the Worker's environment configuration with the framework's SSR configuration and ensures that the Worker is included as part of the framework's build output.</p>
