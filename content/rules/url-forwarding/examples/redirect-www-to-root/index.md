---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/
  description: Create a redirect rule to forward HTTPS requests from the WWW subdomain to the root (also known as the “apex” or “naked” domain).
  full_title: Redirect from WWW to root · Cloudflare Rules docs
  head_html: <title>Redirect from WWW to root · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a redirect rule to forward HTTPS requests from the WWW subdomain to the root (also known as the “apex” or “naked” domain)."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/index.md"><meta property="og:title" content="Redirect from WWW to root · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a redirect rule to forward HTTPS requests from the WWW subdomain to the root (also known as the “apex” or “naked” domain)."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Redirect Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/#page","headline":"Redirect from WWW to root \u00b7 Cloudflare Rules docs","description":"Create a redirect rule to forward HTTPS requests from the WWW subdomain to the root (also known as the \u201capex\u201d or \u201cnaked\u201d domain).","url":"https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/examples/redirect-www-to-root/
  schema: 1
---
<p class="article-summary">Create a redirect rule to forward HTTPS requests from the WWW subdomain to the root (also known as the “apex” or “naked” domain).</p>
<p>This example creates a redirect rule that forwards HTTPS requests from the WWW subdomain (<code>www.example.com</code>) to the root domain (<code>example.com</code>), while retaining the original path and query string.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13197.md")
</div>
<p>This rule ensures that only HTTPS requests from <code>www.</code> subdomains are redirected to the root domain, leaving other requests (such as HTTP or non-WWW) unchanged.</p>
<p>For example, the redirect rule would perform the following redirects:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>Target URL</th>
<th>Status code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://www.example.com/products/</code></td>
<td><code>https://example.com/products/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://www.store.example.com/products/</code></td>
<td><code>https://store.example.com/products/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://store.example.com/products/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
<tr>
<td><code>https://www.example.com/admin/?logged_out=true</code></td>
<td><code>https://example.com/admin/?logged_out=true</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>http://www.example.com/?all_items=true</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
<tr>
<td><code>http://example.com/admin/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
