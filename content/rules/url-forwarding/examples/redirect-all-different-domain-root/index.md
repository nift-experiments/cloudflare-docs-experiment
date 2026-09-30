---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/
  description: Create a redirect rule to redirect all URLs for a domain to point to the root of a new domain, including any subdomains of the old domain.
  full_title: Redirect requests for a domain to a new domain · Cloudflare Rules docs
  head_html: <title>Redirect requests for a domain to a new domain · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a redirect rule to redirect all URLs for a domain to point to the root of a new domain, including any subdomains of the old domain."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/index.md"><meta property="og:title" content="Redirect requests for a domain to a new domain · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a redirect rule to redirect all URLs for a domain to point to the root of a new domain, including any subdomains of the old domain."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Redirect Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/#page","headline":"Redirect requests for a domain to a new domain \u00b7 Cloudflare Rules docs","description":"Create a redirect rule to redirect all URLs for a domain to point to the root of a new domain, including any subdomains of the old domain.","url":"https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/examples/redirect-all-different-domain-root/
  schema: 1
---
<p class="article-summary">Create a redirect rule to redirect all URLs for a domain to point to the root of a new domain, including any subdomains of the old domain.</p>
<p>In this example, an old website was discontinued and replaced by a new one in a different domain. The functionality is different, and all URLs should now point to the root of the new domain. The same applies to any subdomains of the old domain.</p>
<p><a href="/rules/url-forwarding/single-redirects/create-dashboard/">Create a redirect rule</a> with the following configuration:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13202.md")
</div>
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
<td><code>https://subdomain.example.com/</code></td>
<td><code>https://example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://example.com/my/path/to/page.htm</code></td>
<td><code>https://example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://example.com/search?q=term</code></td>
<td><code>https://example.net/</code></td>
<td><code>301</code></td>
</tr>
</tbody>
</table>
