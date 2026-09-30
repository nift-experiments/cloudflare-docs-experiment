---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/
  description: Create a redirect rule to redirect all website visitors from the United Kingdom to a different domain, maintaining the current functionality in the same paths.
  full_title: Redirect requests from one country to a domain · Cloudflare Rules docs
  head_html: <title>Redirect requests from one country to a domain · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a redirect rule to redirect all website visitors from the United Kingdom to a different domain, maintaining the current functionality in the same paths."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/index.md"><meta property="og:title" content="Redirect requests from one country to a domain · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a redirect rule to redirect all website visitors from the United Kingdom to a different domain, maintaining the current functionality in the same paths."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Redirect Rules"><meta name="pcx_tags" content="Redirects,Geolocation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/#page","headline":"Redirect requests from one country to a domain \u00b7 Cloudflare Rules docs","description":"Create a redirect rule to redirect all website visitors from the United Kingdom to a different domain, maintaining the current functionality in the same paths.","url":"https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects","Geolocation"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/examples/redirect-all-country/
  schema: 1
---
<p class="article-summary">Create a redirect rule to redirect all website visitors from the United Kingdom to a different domain, maintaining the current functionality in the same paths.</p>
<p>In this example, all website visitors from the United Kingdom will be redirected to a different domain, but maintaining current functionality in the same paths.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13203.md")
</div>
<p>This configuration will perform the following redirects for UK visitors:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>URL after redirect</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://example.com/</code></td>
<td><code>https://example.co.uk/</code></td>
</tr>
<tr>
<td><code>https://example.com/my/path/to/page.htm</code></td>
<td><code>https://example.co.uk/my/path/to/page.htm</code></td>
</tr>
<tr>
<td><code>https://example.com/search?q=term</code></td>
<td><code>https://example.co.uk/search?q=term</code></td>
</tr>
</tbody>
</table>
