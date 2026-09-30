---
cp9:
  canonical: https://developers.cloudflare.com/network/true-client-ip-header/
  description: Send the visitor's IP to your origin via True-Client-IP header.
  full_title: Understanding the True-Client-IP Header · Cloudflare Network settings docs
  head_html: <title>Understanding the True-Client-IP Header · Cloudflare Network settings docs</title><meta name="generator" content="Nift"><meta name="description" content="Send the visitor&#x27;s IP to your origin via True-Client-IP header."><link rel="canonical" href="https://developers.cloudflare.com/network/true-client-ip-header/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network/true-client-ip-header/index.md"><meta property="og:title" content="Understanding the True-Client-IP Header · Cloudflare Network settings docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send the visitor&#x27;s IP to your origin via True-Client-IP header."><meta property="og:url" content="https://developers.cloudflare.com/network/true-client-ip-header/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network"><meta name="algolia_product_filter" content="Network"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Network"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network/true-client-ip-header/#page","headline":"Understanding the True-Client-IP Header \u00b7 Cloudflare Network settings docs","description":"Send the visitor's IP to your origin via True-Client-IP header.","url":"https://developers.cloudflare.com/network/true-client-ip-header/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network/true-client-ip-header/
  schema: 1
---
<p>Enabling the True-Client-IP Header adds the <a href="/fundamentals/reference/http-headers/#true-client-ip-enterprise-plan-only"><code>True-Client-IP</code> header</a> to all requests to your origin server, which includes the end user's IP address.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="add-true-client-ip-header">Add True-Client-IP Header</h2>
<p>The recommended procedure to access client IP information is to <a href="/rules/transform/managed-transforms/reference/#add-true-client-ip-header">enable the <strong>Add &quot;True-Client-IP&quot; header</strong> Managed Transform</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/665.md")
</aside>
<h2 id="additional-resources">Additional resources</h2>
<p>For additional guidance on using True-Client-IP Header with Cloudflare, refer to the following resources:</p>
<ul>
<li><a href="/rules/transform/managed-transforms/reference/#add-true-client-ip-header">Available Managed Transforms</a></li>
<li><a href="/fundamentals/reference/http-headers/#true-client-ip-enterprise-plan-only">Cloudflare HTTP headers</a></li>
<li><a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">Restoring original visitor IPs</a></li>
</ul>
