---
cp9:
  canonical: https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/
  description: How to configure a HTML handling and trailing slashes for the static assets of your Worker.
  full_title: HTML handling · Cloudflare Workers docs
  head_html: <title>HTML handling · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="How to configure a HTML handling and trailing slashes for the static assets of your Worker."><link rel="canonical" href="https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/index.md"><meta property="og:title" content="HTML handling · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How to configure a HTML handling and trailing slashes for the static assets of your Worker."><meta property="og:url" content="https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/#page","headline":"HTML handling \u00b7 Cloudflare Workers docs","description":"How to configure a HTML handling and trailing slashes for the static assets of your Worker.","url":"https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/static-assets/routing/advanced/html-handling/
  schema: 1
---
<p>Forcing or dropping trailing slashes on request paths (for example, <code>example.com/page/</code> vs. <code>example.com/page</code>) is often something that developers wish to control for cosmetic reasons. Additionally, it can impact SEO because search engines often treat URLs with and without trailing slashes as different, separate pages. This distinction can lead to duplicate content issues, indexing problems, and overall confusion about the correct canonical version of a page.</p>
<p>The <a href="/workers/wrangler/configuration/#assets"><code>assets.html_handling</code> configuration</a> determines the redirects and rewrites of requests for HTML content. It is used to specify the pattern for canonical URLs, thus where Cloudflare serves HTML content from, and additionally, where Cloudflare redirects non-canonical URLs to.</p>
<p>Take the following directory structure:</p>
<pre tabindex="0" class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/17311.md")&#10;&#10;&#10;</pre>
<h2 id="automatic-trailing-slashes-default">Automatic trailing slashes (default)</h2>
<p>This will usually give you the desired behavior automatically: individual files (e.g. <code>foo.html</code>) will be served <em>without</em> a trailing slash and folder index files (e.g. <code>foo/index.html</code>) will be served <em>with</em> a trailing slash.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17312.md")
</div>
<p>Based on the incoming requests, the following assets would be served:</p>
<table>
<thead>
<tr>
<th>Incoming Request</th>
<th>Response</th>
<th>Asset Served</th>
</tr>
</thead>
<tbody>
<tr>
<td>/file</td>
<td>200</td>
<td>/dist/file.html</td>
</tr>
<tr>
<td>/file.html</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/index</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/index.html</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/folder</td>
<td>307 to /folder/</td>
<td>-</td>
</tr>
<tr>
<td>/folder.html</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
<tr>
<td>/folder/</td>
<td>200</td>
<td>/dist/folder/index.html</td>
</tr>
<tr>
<td>/folder/index</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
<tr>
<td>/folder/index.html</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
</tbody>
</table>
<h2 id="force-trailing-slashes">Force trailing slashes</h2>
<p>Alternatively, you can force trailing slashes (<code>force-trailing-slash</code>).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17313.md")
</div>
<p>Based on the incoming requests, the following assets would be served:</p>
<table>
<thead>
<tr>
<th>Incoming Request</th>
<th>Response</th>
<th>Asset Served</th>
</tr>
</thead>
<tbody>
<tr>
<td>/file</td>
<td>307 to /file/</td>
<td>-</td>
</tr>
<tr>
<td>/file.html</td>
<td>307 to /file/</td>
<td>-</td>
</tr>
<tr>
<td>/file/</td>
<td>200</td>
<td>/dist/file.html</td>
</tr>
<tr>
<td>/file/index</td>
<td>307 to /file/</td>
<td>-</td>
</tr>
<tr>
<td>/file/index.html</td>
<td>307 to /file/</td>
<td>-</td>
</tr>
<tr>
<td>/folder</td>
<td>307 to /folder/</td>
<td>-</td>
</tr>
<tr>
<td>/folder.html</td>
<td>307 to /folder/</td>
<td>-</td>
</tr>
<tr>
<td>/folder/</td>
<td>200</td>
<td>/dist/folder/index.html</td>
</tr>
<tr>
<td>/folder/index</td>
<td>307 to /folder/</td>
<td>-</td>
</tr>
<tr>
<td>/folder/index.html</td>
<td>307 to /folder/</td>
<td>-</td>
</tr>
</tbody>
</table>
<h2 id="drop-trailing-slashes">Drop trailing slashes</h2>
<p>Or you can drop trailing slashes (<code>drop-trailing-slash</code>).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17314.md")
</div>
<p>Based on the incoming requests, the following assets would be served:</p>
<table>
<thead>
<tr>
<th>Incoming Request</th>
<th>Response</th>
<th>Asset Served</th>
</tr>
</thead>
<tbody>
<tr>
<td>/file</td>
<td>200</td>
<td>/dist/file.html</td>
</tr>
<tr>
<td>/file.html</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/index</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/index.html</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/folder</td>
<td>200</td>
<td>/dist/folder/index.html</td>
</tr>
<tr>
<td>/folder.html</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
<tr>
<td>/folder/</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
<tr>
<td>/folder/index</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
<tr>
<td>/folder/index.html</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
</tbody>
</table>
<h2 id="disable-html-handling">Disable HTML handling</h2>
<p>Alternatively, if you have bespoke needs, you can disable the built-in HTML handling entirely (<code>none</code>).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17315.md")
</div>
<p>Based on the incoming requests, the following assets would be served:</p>
<table>
<thead>
<tr>
<th>Incoming Request</th>
<th>Response</th>
<th>Asset Served</th>
</tr>
</thead>
<tbody>
<tr>
<td>/file</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/file.html</td>
<td>200</td>
<td>/dist/file.html</td>
</tr>
<tr>
<td>/file/</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/file/index</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/file/index.html</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/folder</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/folder.html</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/folder/</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/folder/index</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/folder/index.html</td>
<td>200</td>
<td>/dist/folder/index.html</td>
</tr>
</tbody>
</table>
