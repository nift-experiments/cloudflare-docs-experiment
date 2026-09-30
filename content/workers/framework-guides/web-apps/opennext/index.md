---
cp9:
  canonical: https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/
  description: Deploy a Next.js application to Cloudflare Workers with the OpenNext adapter.
  full_title: OpenNext adapter · Cloudflare Workers docs
  head_html: <title>OpenNext adapter · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy a Next.js application to Cloudflare Workers with the OpenNext adapter."><link rel="canonical" href="https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/index.md"><meta property="og:title" content="OpenNext adapter · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy a Next.js application to Cloudflare Workers with the OpenNext adapter."><meta property="og:url" content="https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="full-stack"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/#page","headline":"OpenNext adapter \u00b7 Cloudflare Workers docs","description":"Deploy a Next.js application to Cloudflare Workers with the OpenNext adapter.","url":"https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["full-stack"]}</script>
  markdown: true
  noindex: false
  route: /workers/framework-guides/web-apps/opennext/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="recommended-path">Recommended path</h3>
@markup("md", "content/.markup/bodies/16945.md")
</aside>
<p>Use this guide to maintain an existing OpenNext application. Migrate to vinext when compatibility allows.</p>
<p><a href="https://opennext.js.org/">OpenNext</a> adapts the output of <code>next build</code> so it can run on different platforms, including Cloudflare Workers.</p>
<h2 id="supported-features">Supported features</h2>
<p>Most Next.js features are supported by the Cloudflare OpenNext adapter:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Cloudflare OpenNext adapter</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>App Router</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Pages Router</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Route Handlers</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>React Server Components</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Static Site Generation (SSG)</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Server-Side Rendering (SSR)</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Incremental Static Regeneration (ISR)</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Server Actions</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Response streaming</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Asynchronous work with <code>next/after</code></td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Middleware</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Image optimization</td>
<td>Supported</td>
<td>Supported through <a href="/images/">Cloudflare Images</a>.</td>
</tr>
<tr>
<td>Partial Prerendering (PPR)</td>
<td>Supported</td>
<td>PPR is experimental in Next.js.</td>
</tr>
<tr>
<td>Composable Caching (<code>&quot;use cache&quot;</code>)</td>
<td>Supported</td>
<td>Composable Caching is experimental in Next.js.</td>
</tr>
<tr>
<td>Node.js in Middleware</td>
<td>Not yet supported</td>
<td>Node.js middleware introduced in Next.js 15.2 is not yet supported.</td>
</tr>
</tbody>
</table>
<p>For detailed OpenNext documentation, refer to <a href="https://opennext.js.org/cloudflare">OpenNext for Cloudflare</a>.</p>
<h2 id="configure-opennext-manually">Configure OpenNext manually</h2>
<p>Wrangler automatic configuration uses vinext for Next.js projects. To use OpenNext, configure the adapter manually.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16948.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-builds">Workers Builds</h3>
@markup("md", "content/.markup/bodies/16943.md")
</aside>
