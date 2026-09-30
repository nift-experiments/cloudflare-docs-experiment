---
cp9:
  canonical: https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/
  description: Create a rate limiting rule for your zone in the Cloudflare dashboard.
  full_title: Create a rate limiting rule in the dashboard · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Create a rate limiting rule in the dashboard · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a rate limiting rule for your zone in the Cloudflare dashboard."><link rel="canonical" href="https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/index.md"><meta property="og:title" content="Create a rate limiting rule in the dashboard · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a rate limiting rule for your zone in the Cloudflare dashboard."><meta property="og:url" content="https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Rate limiting"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/#page","headline":"Create a rate limiting rule in the dashboard \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Create a rate limiting rule for your zone in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/rate-limiting-rules/create-zone-dashboard/
  schema: 1
---
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15371.md")
</div>
<h2 id="configure-a-custom-response-for-blocked-requests">Configure a custom response for blocked requests</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15370.md")
</aside>
<p>When you select the <em>Block</em> action in a rule you can optionally define a custom response.</p>
<p>The custom response has three settings:</p>
<ul>
<li><strong>With response type</strong>: Choose a content type or the default rate limiting response from the list. The available custom response types are the following:</li>
</ul>
<table>
<thead>
<tr>
<th>Dashboard value</th>
<th>API value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Custom HTML</td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
<tr>
<td>Custom Text</td>
<td><code>&quot;text/plain&quot;</code></td>
</tr>
<tr>
<td>Custom JSON</td>
<td><code>&quot;application/json&quot;</code></td>
</tr>
<tr>
<td>Custom XML</td>
<td><code>&quot;text/xml&quot;</code></td>
</tr>
</tbody>
</table>
<ul>
<li>
<p><strong>With response code</strong>: Choose an HTTP status code for the response, in the range 400-499. The default response code is 429.</p>
</li>
<li>
<p><strong>Response body</strong>: The body of the response. Configure a valid body according to the response type you selected. The maximum field size is 30 KB.</p>
</li>
</ul>
