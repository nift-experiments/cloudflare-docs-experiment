---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-413/
  description: Troubleshoot HTTP 413 error responses.
  full_title: Error 413 · Cloudflare Support docs
  head_html: <title>Error 413 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 413 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-413/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-413/index.md"><meta property="og:title" content="Error 413 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 413 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-413/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-413/#page","headline":"Error 413 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 413 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-413/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/4xx-client-error/error-413/
  schema: 1
---
<h2 id="413-payload-too-large">413 Payload Too Large</h2>
<p>The <code>413 Payload Too Large</code> status code indicates that the server refuses to process the request because the payload sent by the client exceeds the server's acceptable size limit. The server may optionally close the connection. If this refusal would only happen temporarily, then the server should send a <code>Retry-After</code> header to specify when the client should try the request again.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>The <code>413 Payload Too Large</code> status code often occurs when clients attempt to upload large files, such as videos or images, or send oversized request bodies, like JSON or XML payloads, that exceed the server's size limits. This can also happen during file transfers or API requests involving large datasets, prompting the server to reject the request.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>The upload limit for the Cloudflare API depends on your plan. If you exceed this limit, your API call will receive a <code>413 Request Entity Too Large</code> error.</p>
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
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Max upload size</td>
<td>100 MB</td>
<td>100 MB</td>
<td>200 MB</td>
<td>Up to 5 GB</td>
</tr>
</tbody>
</table>
<p>Keep in mind, customers can adjust the <strong>Maximum Upload Size</strong> from the zone's <strong>Network</strong> page. Enterprise customers can self-serve any value up to 5 GB; uploads larger than 5 GB require additional configuration — contact your account team. Setting the limit below the size of an incoming request causes a <code>413</code>.</p>
<p>If you require a larger upload, break up requests into smaller chunks, change your DNS record to <a href="/dns/proxy-status/#dns-only-records">DNS-only</a>, or <a href="/billing/manage/change-plan/">upgrade your plan</a>.</p>
