---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/manage-domains/redirect-domain/
  description: Set up domain redirects in Cloudflare to forward traffic from an alias domain to your primary domain using DNS records and redirect rules.
  full_title: Redirect one domain to another · Cloudflare Fundamentals docs
  head_html: <title>Redirect one domain to another · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up domain redirects in Cloudflare to forward traffic from an alias domain to your primary domain using DNS records and redirect rules."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/manage-domains/redirect-domain/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/manage-domains/redirect-domain/index.md"><meta property="og:title" content="Redirect one domain to another · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up domain redirects in Cloudflare to forward traffic from an alias domain to your primary domain using DNS records and redirect rules."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/manage-domains/redirect-domain/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/manage-domains/redirect-domain/#page","headline":"Redirect one domain to another \u00b7 Cloudflare Fundamentals docs","description":"Set up domain redirects in Cloudflare to forward traffic from an alias domain to your primary domain using DNS records and redirect rules.","url":"https://developers.cloudflare.com/fundamentals/manage-domains/redirect-domain/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/manage-domains/redirect-domain/
  schema: 1
---
<p>If you have an alias domain that only forwards traffic to another domain (that is, the domain does not have an associated origin server of its own), you can set up redirects directly within Cloudflare.</p>
<ol>
<li>
<p><a href="/fundamentals/manage-domains/#add-a-domain-to-cloudflare">Add</a> your alias domain (for example, <code>previous.com</code>) to Cloudflare.</p>
</li>
<li>
<p>Make sure that your alias domain has a proxied <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS A or CNAME record</a> that properly resolves DNS queries. You may also want to include a subdomain DNS record for <code>www</code>.</p>
<p>Use the IP address <code>192.0.2.1</code> for the <code>A</code> record. This address does not route traffic to an origin server but allows Cloudflare to apply rules, redirects, and Workers to incoming traffic. The equivalent IP address for an <code>AAAA</code> record is <code>100::</code>.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Type</strong></th>
<th><strong>Name</strong></th>
<th><strong>IPv4 address</strong></th>
<th><strong>Proxy status</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td><code>@</code></td>
<td><code>192.0.2.1</code></td>
<td>Proxied</td>
</tr>
<tr>
<td>A</td>
<td><code>www</code></td>
<td><code>192.0.2.1</code></td>
<td>Proxied</td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Use <a href="/rules/url-forwarding/">Redirect rules</a> to forward traffic from your alias domain to your other domain.</li>
</ol>
<p>This example will redirect all requests for <code>smallshop.example.com</code> to a different hostname using HTTPS, keeping the original path and query string.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/8901.md")
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
<td><code>http://smallshop.example.com/</code></td>
<td><code>https://globalstore.example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>http://smallshop.example.com/admin/?logged_out=true</code></td>
<td><code>https://globalstore.example.net/admin/?logged_out=true</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://smallshop.example.com/?all_items=1</code></td>
<td><code>https://globalstore.example.net/?all_items=1</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>http://example.com/about/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
