---
cp9:
  canonical: https://developers.cloudflare.com/rules/snippets/examples/route-and-rewrite/
  description: Route requests to a different origin, prepend a directory to the URL path, and remove specific segments.
  full_title: Change origin and modify paths · Cloudflare Rules docs
  head_html: <title>Change origin and modify paths · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Route requests to a different origin, prepend a directory to the URL path, and remove specific segments."><link rel="canonical" href="https://developers.cloudflare.com/rules/snippets/examples/route-and-rewrite/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/snippets/examples/route-and-rewrite/index.md"><meta property="og:title" content="Change origin and modify paths · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route requests to a different origin, prepend a directory to the URL path, and remove specific segments."><meta property="og:url" content="https://developers.cloudflare.com/rules/snippets/examples/route-and-rewrite/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Snippets"><meta name="pcx_tags" content="URL rewrite"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/snippets/examples/route-and-rewrite/#page","headline":"Change origin and modify paths \u00b7 Cloudflare Rules docs","description":"Route requests to a different origin, prepend a directory to the URL path, and remove specific segments.","url":"https://developers.cloudflare.com/rules/snippets/examples/route-and-rewrite/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["URL rewrite"]}</script>
  markdown: true
  noindex: false
  route: /rules/snippets/examples/route-and-rewrite/
  schema: 1
---
<p class="article-summary">Reroute a request to a different origin and modify the URL path.</p>
<p>This example demonstrates how to use Cloudflare Snippets to:</p>
<ul>
<li>Reroute incoming requests to a different origin.</li>
<li>Prepend a directory to the URL path.</li>
<li>Remove specific segments from the URL path.</li>
</ul>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request) {&#10;		// Clone the original request to create a new request object&#10;		const newRequest = new Request(request);&#10;&#10;		// Add a header to identify a rerouted request at the new origin&#10;		newRequest.headers.set(&quot;X-Rerouted&quot;, &quot;1&quot;);&#10;&#10;		// Clone and parse the original URL&#10;		const url = new URL(request.url);&#10;&#10;		// Step 1: Reroute to a different origin&#10;		url.hostname = &quot;example.com&quot;; // Change the hostname to the new origin&#10;&#10;		// Step 2: Append a directory to the path&#10;		url.pathname = `/new-path${url.pathname}`; // Prepend &quot;/new-path&quot; to the current path&#10;&#10;		// Step 3: Remove a specific segment from the path&#10;		url.pathname = url.pathname.replace(&quot;/remove-me&quot;, &quot;&quot;); // Rewrite `/remove-me/something` to `/something`&#10;&#10;		// Fetch the modified request from the updated URL&#10;		return await fetch(url, newRequest);&#10;	},&#10;};&#10;</code></pre>
<p>This configuration will perform the following rewrites:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>URL after rewrite</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://subdomain.example.com/foo</code></td>
<td><code>https://example.com/new-path/foo</code></td>
</tr>
<tr>
<td><code>https://example.com/remove-me/bar</code></td>
<td><code>https://example.com/new-path/bar</code></td>
</tr>
<tr>
<td><code>https://example.net/remove-me</code></td>
<td><code>https://example.com/new-path</code></td>
</tr>
</tbody>
</table>
