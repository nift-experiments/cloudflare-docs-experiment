---
cp9:
  canonical: https://developers.cloudflare.com/workers/local-development/bindings-per-env/
  description: Supported bindings per development mode
  full_title: Supported bindings per development mode · Cloudflare Workers docs
  head_html: <title>Supported bindings per development mode · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Supported bindings per development mode"><link rel="canonical" href="https://developers.cloudflare.com/workers/local-development/bindings-per-env/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/local-development/bindings-per-env/index.md"><meta property="og:title" content="Supported bindings per development mode · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Supported bindings per development mode"><meta property="og:url" content="https://developers.cloudflare.com/workers/local-development/bindings-per-env/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/local-development/bindings-per-env/#page","headline":"Supported bindings per development mode \u00b7 Cloudflare Workers docs","description":"Supported bindings per development mode","url":"https://developers.cloudflare.com/workers/local-development/bindings-per-env/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/local-development/bindings-per-env/
  schema: 1
---
<h2 id="local-development">Local development</h2>
<p><strong>Local simulations</strong>: During local development, your Worker code always executes locally and bindings connect to locally simulated resources <a href="/workers/local-development/#remote-bindings">by default</a>. This is supported in <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> and the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<p><strong>Remote binding connections:</strong>: Allows you to connect to remote resources on a <a href="/workers/local-development/#remote-bindings">per-binding basis</a>. This is supported in <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> and the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<table>
<thead>
<tr>
<th>Binding</th>
<th align="center">Local simulations</th>
<th align="center">Remote binding connections</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>AI</strong></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Assets</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Analytics Engine</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Browser Run</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>D1</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Durable Objects</strong></td>
<td align="center">✅</td>
<td align="center">❌ <sup><a href="#footnote-workers-bindings-per-env-mdx-1">1</a></sup></td>
</tr>
<tr>
<td><strong>Containers</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Email Bindings</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Hyperdrive</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Images</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>KV</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Media Transformations</strong></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>mTLS</strong></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Queues</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>R2</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Rate Limiting</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Service Bindings (multiple Workers)</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Vectorize</strong></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Workflows</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
</tbody>
</table>
<h2 id="remote-development">Remote development</h2>
<p>During remote development, all of your Worker code is uploaded and executed on Cloudflare's infrastructure, and bindings always connect to remote resources. <strong>We recommend using local development with remote binding connections instead</strong> for faster iteration and debugging.</p>
<p>Supported only in <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev --remote</code></a> - there is <strong>no Vite plugin equivalent</strong>.</p>
<table>
<thead>
<tr>
<th>Binding</th>
<th align="center">Remote development</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>AI</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Assets</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Analytics Engine</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Browser Run</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>D1</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Durable Objects</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Containers</strong></td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Email Bindings</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Hyperdrive</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Images</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>KV</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Media Transformations</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>mTLS</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Queues</strong></td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>R2</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Rate Limiting</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Service Bindings (multiple Workers)</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Vectorize</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Workflows</strong></td>
<td align="center">❌</td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-workers-bindings-per-env-mdx-1">Refer to [Using remote resources with Durable Objects and Workflows](/workers/local-development/#using-remote-resources-with-durable-objects-and-workflows) for recommended workarounds.</li></ol></section>
