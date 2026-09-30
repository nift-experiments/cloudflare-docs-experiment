---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/
  description: Create a redirect rule to redirect all requests to a different domain, maintaining all functionality, except for the discontinued HTTP service (port 80).
  full_title: Redirect requests from one domain to another · Cloudflare Rules docs
  head_html: <title>Redirect requests from one domain to another · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a redirect rule to redirect all requests to a different domain, maintaining all functionality, except for the discontinued HTTP service (port 80)."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/index.md"><meta property="og:title" content="Redirect requests from one domain to another · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a redirect rule to redirect all requests to a different domain, maintaining all functionality, except for the discontinued HTTP service (port 80)."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Redirect Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/#page","headline":"Redirect requests from one domain to another \u00b7 Cloudflare Rules docs","description":"Create a redirect rule to redirect all requests to a different domain, maintaining all functionality, except for the discontinued HTTP service (port 80).","url":"https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/examples/redirect-all-another-domain/
  schema: 1
---
<p class="article-summary">Create a redirect rule to redirect all requests to a different domain, maintaining all functionality, except for the discontinued HTTP service (port 80).</p>
<p>In this example the original domain was replaced with a different domain. All functionality was maintained, except for the HTTP service (port 80) which was discontinued.</p>
<p><a href="/rules/url-forwarding/single-redirects/create-dashboard/">Create a redirect rule</a> with the following configuration:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13204.md")
</div>
<p>This configuration will perform the following redirects:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>URL after redirect</th>
<th>Status code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>http://example.com/</code></td>
<td><code>https://example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://example.com/</code></td>
<td><code>https://example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://example.com/my/path/to/page.htm</code></td>
<td><code>https://example.net/my/path/to/page.htm</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://example.com/search?q=term</code></td>
<td><code>https://example.net/search?q=term</code></td>
<td><code>301</code></td>
</tr>
</tbody>
</table>
