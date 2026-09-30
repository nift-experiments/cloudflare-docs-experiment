---
cp9:
  canonical: https://developers.cloudflare.com/pages/functions/source-maps/
  description: Adding source maps and generating stack traces for Pages.
  full_title: Source maps and stack traces · Cloudflare Pages docs
  head_html: <title>Source maps and stack traces · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Adding source maps and generating stack traces for Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/functions/source-maps/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/functions/source-maps/index.md"><meta property="og:title" content="Source maps and stack traces · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Adding source maps and generating stack traces for Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/functions/source-maps/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/functions/source-maps/#page","headline":"Source maps and stack traces \u00b7 Cloudflare Pages docs","description":"Adding source maps and generating stack traces for Pages.","url":"https://developers.cloudflare.com/pages/functions/source-maps/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/functions/source-maps/
  schema: 1
---
<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack">Stack traces</a> help with debugging your code when your application encounters an unhandled exception. Stack traces show you the specific functions that were called, in what order, from which line and file, and with what arguments.</p>
<p>Most JavaScript code is first bundled, often transpiled, and then minified before being deployed to production. This process creates smaller bundles to optimize performance and converts code from TypeScript to Javascript if needed.</p>
<p>Source maps translate compiled and minified code back to the original code that you wrote. Source maps are combined with the stack trace returned by the JavaScript runtime to present you with a stack trace.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10939.md")
</aside>
<h2 id="source-maps">Source Maps</h2>
<p>To enable source maps, provide the <code>--upload-source-maps</code> flag to <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler pages deploy</code></a> or add the following to your Pages application's <a href="/pages/functions/wrangler-configuration/">Wrangler configuration file</a> if you are using the Pages build environment:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/10940.md")
</div>
<p>When uploading source maps is enabled, Wrangler will automatically generate and upload source map files when you run <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler pages deploy</code></a>.</p>
<h2 id="stack-traces">Stack traces</h2>
<p>​​
When your application throws an uncaught exception, we fetch the source map and use it to map the stack trace of the exception back to lines of your application’s original source code.</p>
<p>You can then view the stack trace when streaming <a href="/pages/functions/debugging-and-logging/">real-time logs</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10938.md")
</aside>
<h2 id="limits">Limits</h2>
<table>
<thead>
<tr>
<th>Description</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum Source Map Size</td>
<td>15 MB gzipped</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/pages/functions/debugging-and-logging/">Real-time logs</a> - Learn how to capture Pages logs in real-time.</li>
</ul>
