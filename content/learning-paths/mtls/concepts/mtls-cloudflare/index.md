---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/mtls/concepts/mtls-cloudflare/
  description: Learn about use mtls with cloudflare protected resources in this guide.
  full_title: Use mTLS with Cloudflare protected resources · Cloudflare Learning Paths
  head_html: <title>Use mTLS with Cloudflare protected resources · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about use mtls with cloudflare protected resources in this guide."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/mtls/concepts/mtls-cloudflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/mtls/concepts/mtls-cloudflare/index.md"><meta property="og:title" content="Use mTLS with Cloudflare protected resources · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about use mtls with cloudflare protected resources in this guide."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/mtls/concepts/mtls-cloudflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="SSL/TLS,Access,API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/mtls/concepts/mtls-cloudflare/#page","headline":"Use mTLS with Cloudflare protected resources \u00b7 Cloudflare Learning Paths","description":"Learn about use mtls with cloudflare protected resources in this guide.","url":"https://developers.cloudflare.com/learning-paths/mtls/concepts/mtls-cloudflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/mtls/concepts/mtls-cloudflare/
  schema: 1
---
<p>In this implementation guide we will be focusing on the L7 / Application Layer security for HTTP/S requests targeting <a href="/dns/proxy-status/">proxied</a> hostnames, including the <a href="/ssl/origin-configuration/ssl-modes/">first connection</a> between client and Cloudflare.</p>
<p>Some common mTLS use cases are:</p>
<ul>
<li>Protect and verify legitimate API traffic by verifying Client Certificates provided during TLS/SSL handshakes.</li>
<li>Check IoT devices' identity by verifying Client Certificates they provide during TLS/SSL handshakes.</li>
</ul>
<p>There are two main ways to use mTLS at Cloudflare, either by using the Application Security offering (optionally including <a href="/api-shield/">API Shield</a>) or <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>. Below is a non-exhaustive overview table of their differences:</p>
<table>
<thead>
<tr>
<th align="left">Feature</th>
<th align="left">Application Security (Client Certificate + WAF)</th>
<th align="left">Cloudflare Access (mTLS)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mainly used for</td>
<td align="left">External Authentication (that is, APIs)</td>
<td align="left">Internal Authentication (that is, employees)</td>
</tr>
<tr>
<td align="left">Availability</td>
<td align="left">By default, 100 Client Certificates per Zone are included for free. For more certificates or <a href="/api-shield/">API Shield features</a>, contact your account team.</td>
<td align="left">Zero Trust Enterprise only feature.</td>
</tr>
<tr>
<td align="left"><a href="/ssl/concepts/#certificate-authority-ca">Certificate Authority (CA)</a></td>
<td align="left">Cloudflare-managed or customer-uploaded (BYO CA). There's a soft-limit of up to <a href="/ssl/client-certificates/byo-ca/#availability">five customer-uploaded CAs</a>.</td>
<td align="left">Customer-uploaded only (BYO CA). There's a soft-limit of up to <a href="/cloudflare-one/account-limits/#access">50 CAs</a>.</td>
</tr>
<tr>
<td align="left">Client Certificate Details</td>
<td align="left">Forwarded to the origin server via <a href="/ssl/client-certificates/forward-a-client-certificate/#cloudflare-api">Cloudflare API</a>, <a href="/ssl/client-certificates/forward-a-client-certificate/#cloudflare-workers">Cloudflare Workers</a>, and <a href="/ssl/client-certificates/forward-a-client-certificate/#managed-transforms">Managed Transforms</a>.</td>
<td align="left">Forwarded to the origin server via <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#cloudflare-api">Cloudflare API</a>, <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#cloudflare-workers">Cloudflare Workers</a>, and <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#managed-transforms">Managed Transforms</a>. Client Certificate headers and <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/">Cf-Access-Jwt-Assertion</a> JWT header can be forwarded to the origin server.</td>
</tr>
<tr>
<td align="left">Client Certificates Revocation</td>
<td align="left">Use the WAF <a href="/waf/custom-rules/">Custom Rules</a> to check for <a href="/ssl/client-certificates/revoke-client-certificate/"><em>cf.tls_client_auth.cert_revoked</em></a>, which only applies to Cloudflare-managed CA. <br /><br /> For BYO CAs, it would be the same approach as with Cloudflare Access.</td>
<td align="left">Generate a <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#create-a-crl">Certificate Revocation List (CRL)</a> and enforce the revocation in a Cloudflare Worker.</td>
</tr>
</tbody>
</table>
