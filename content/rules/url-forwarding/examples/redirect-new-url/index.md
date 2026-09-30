---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/
  description: Create a redirect rule to redirect visitors from `/contact-us/` to the page's new path `/contacts/`.
  full_title: Redirect visitors to a new page URL · Cloudflare Rules docs
  head_html: <title>Redirect visitors to a new page URL · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a redirect rule to redirect visitors from `/contact-us/` to the page&#x27;s new path `/contacts/`."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/index.md"><meta property="og:title" content="Redirect visitors to a new page URL · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a redirect rule to redirect visitors from `/contact-us/` to the page&#x27;s new path `/contacts/`."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Redirect Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/#page","headline":"Redirect visitors to a new page URL \u00b7 Cloudflare Rules docs","description":"Create a redirect rule to redirect visitors from /contact-us/ to the page's new path /contacts/.","url":"https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/examples/redirect-new-url/
  schema: 1
---
<p class="article-summary">Create a redirect rule to redirect visitors from `/contact-us/` to the page&#x27;s new path `/contacts/`.</p>
<p>This example static redirect for zone <code>example.com</code> will redirect visitors requesting the <code>/contact-us/</code> page to the new page URL <code>/contacts/</code>.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13199.md")
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
<td><code>example.com/contact-us/</code></td>
<td><code>example.com/contacts/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>example.com/contact-us/?state=TX</code></td>
<td><code>example.com/contacts/?state=TX</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>example.com/team/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
