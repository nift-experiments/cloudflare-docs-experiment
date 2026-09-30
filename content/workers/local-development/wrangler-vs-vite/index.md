---
cp9:
  canonical: https://developers.cloudflare.com/workers/local-development/wrangler-vs-vite/
  description: Choose between Wrangler and the Cloudflare Vite plugin for local development.
  full_title: Choosing between Wrangler & Vite · Cloudflare Workers docs
  head_html: <title>Choosing between Wrangler &amp; Vite · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Choose between Wrangler and the Cloudflare Vite plugin for local development."><link rel="canonical" href="https://developers.cloudflare.com/workers/local-development/wrangler-vs-vite/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/local-development/wrangler-vs-vite/index.md"><meta property="og:title" content="Choosing between Wrangler &amp; Vite · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Choose between Wrangler and the Cloudflare Vite plugin for local development."><meta property="og:url" content="https://developers.cloudflare.com/workers/local-development/wrangler-vs-vite/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/local-development/wrangler-vs-vite/#page","headline":"Choosing between Wrangler & Vite \u00b7 Cloudflare Workers docs","description":"Choose between Wrangler and the Cloudflare Vite plugin for local development.","url":"https://developers.cloudflare.com/workers/local-development/wrangler-vs-vite/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/local-development/wrangler-vs-vite/
  schema: 1
---
<p>Wrangler and the Cloudflare Vite plugin both provide local development environments for Workers. Both support backend Workers, local and remote bindings, and multi-Worker applications.</p>
<p>Choose based on the build tools your project uses. You can also use the Vite plugin for development and builds while using Wrangler for deployment and other Workers commands.</p>
<h2 id="compare-wrangler-and-vite">Compare Wrangler and Vite</h2>
<table>
<thead>
<tr>
<th>Capability or workflow</th>
<th>Wrangler</th>
<th>Cloudflare Vite plugin</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standalone JavaScript or TypeScript Workers</td>
<td>Supported</td>
<td>Supported</td>
</tr>
<tr>
<td>Full-stack and backend Workers</td>
<td>Supported</td>
<td>Supported</td>
</tr>
<tr>
<td>Local binding simulations via <a href="/workers/testing/miniflare/">Miniflare</a></td>
<td>Supported</td>
<td>Supported</td>
</tr>
<tr>
<td><a href="/workers/local-development/">Remote bindings</a></td>
<td>Supported</td>
<td>Supported</td>
</tr>
<tr>
<td>Multi-Worker development</td>
<td>Supported</td>
<td>Supported</td>
</tr>
<tr>
<td>Frontend and server-side rendering frameworks</td>
<td>Use the framework build output</td>
<td>Integrates with Vite-powered frameworks</td>
</tr>
<tr>
<td>Build pipeline</td>
<td>Uses Wrangler's bundler or a custom build</td>
<td>Uses Vite transformations, Hot Module Replacement, and plugins</td>
</tr>
<tr>
<td>Deployment and resource management</td>
<td>Supported</td>
<td>Use Wrangler after <code>vite build</code></td>
</tr>
<tr>
<td><a href="/workers/languages/rust/">Rust Workers</a></td>
<td>Supported</td>
<td>Not supported</td>
</tr>
<tr>
<td><a href="/workers/languages/python/">Python Workers</a></td>
<td>Use <a href="/workers/languages/python/"><code>pywrangler</code></a> instead of <code>wrangler</code></td>
<td>Not supported</td>
</tr>
</tbody>
</table>
<p>Use the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> when your project already uses Vite or would benefit from its build pipeline. Vite is valid for standalone backend Workers, not only frontend applications.</p>
<p>Use <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> when your project does not use Vite or you want a direct command-line workflow. Wrangler also provides deployment and resource management commands.</p>
<p>For local development that requires deployed resources, both tools support <a href="/workers/local-development/#remote-bindings">remote bindings</a>. Your Worker runs locally while selected bindings connect to deployed Cloudflare resources.</p>
<p>For configuration differences when moving an existing project, refer to <a href="/workers/vite-plugin/reference/migrating-from-wrangler-dev/">Migrating from wrangler dev</a>.</p>
