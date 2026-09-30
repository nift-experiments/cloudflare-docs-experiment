---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/security/
  description: Discover, validate, and protect API endpoints with API Shield security features.
  full_title: Security · Cloudflare API Shield docs
  head_html: <title>Security · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Discover, validate, and protect API endpoints with API Shield security features."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/security/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/security/index.md"><meta property="og:title" content="Security · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Discover, validate, and protect API endpoints with API Shield security features."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/security/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/api-shield/security/#page","headline":"Security \u00b7 Cloudflare API Shield docs","description":"Discover, validate, and protect API endpoints with API Shield security features.","url":"https://developers.cloudflare.com/api-shield/security/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/security/
  schema: 1
---
<p><a href="/waf/detections/application-profiles/">Application Profiles</a> provides the shared profile detection, analytics, and mitigation model. Schema Profile is its only current profile type.</p>
<p><a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema Learning</a> learns a Schema Profile from traffic. <a href="/api-shield/security/schema-validation/">Schema Validation</a> supplies the same profile type through uploaded OpenAPI schemas.</p>
<p>API Shield provides API inventory, schema governance, OpenAPI export, and automation. Cloudflare also offers these API security features:</p>
<table>
<thead>
<tr>
<th>Discovery &amp; management</th>
<th>Posture management</th>
<th>Runtime protection</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api-shield/security/api-discovery/">API Discovery</a></td>
<td><a href="/api-shield/security/volumetric-abuse-detection/">Volumetric Abuse Detection</a></td>
<td><a href="/api-shield/security/schema-validation/">Schema validation</a></td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema learning</a></td>
<td><a href="/api-shield/security/authentication-posture/">Authentication Posture</a></td>
<td><a href="/api-shield/security/jwt-validation/">JWT validation</a></td>
</tr>
<tr>
<td><a href="/api-shield/security/sequence-analytics/">Sequence Analytics</a></td>
<td><a href="/api-shield/security/bola-vulnerability-detection/">BOLA vulnerability detection</a></td>
<td><a href="/api-shield/security/sequence-mitigation/">Sequence mitigation</a></td>
</tr>
<tr>
<td></td>
<td><a href="/api-shield/management-and-monitoring/endpoint-labels/#risk-labels">Risk labels</a></td>
<td><a href="/api-shield/security/mtls/">Mutual TLS (mTLS)</a></td>
</tr>
<tr>
<td></td>
<td><a href="/api-shield/security/vulnerability-scanner/">Vulnerability Scanner</a></td>
<td><a href="/api-shield/security/graphql-protection/">GraphQL query protection</a></td>
</tr>
</tbody>
</table>
<h2 id="example-cloudflare-solutions">Example Cloudflare solutions</h2>
<p>Cloudflare API Shield, together with other Cloudflare products, helps protect your API from the <a href="https://owasp.org/www-project-api-security/">OWASP API Security Top 10</a>. These are the most common API security risks, ranging from unauthorized data access to denial of service.</p>
<p>The following table maps each OWASP vulnerability to the Cloudflare features that address it:</p>
<table>
<thead>
<tr>
<th>OWASP issue</th>
<th>Example Cloudflare solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Broken Object Level Authorization</td>
<td><a href="/api-shield/security/bola-vulnerability-detection/">BOLA vulnerability detection</a>, [Sequence mitigation], [Schema validation], [JWT validation], [Rate Limiting], <a href="/api-shield/security/vulnerability-scanner/">Vulnerability Scanner</a></td>
</tr>
<tr>
<td>Broken Authentication</td>
<td><a href="/api-shield/security/authentication-posture/">Authentication Posture</a>, <a href="/api-shield/security/mtls/">mTLS</a>, [JWT validation], <a href="/waf/managed-rules/check-for-exposed-credentials/">Exposed Credential Checks</a>, <a href="/bots/">Bot Management</a></td>
</tr>
<tr>
<td>Broken Object Property Level Authorization</td>
<td>[Schema validation], [JWT validation]</td>
</tr>
<tr>
<td>Unrestricted Resource Consumption</td>
<td>[Rate Limiting], [Sequence mitigation], [Bot Management], [GraphQL Query Protection]</td>
</tr>
<tr>
<td>Broken Function Level Authorization</td>
<td>[Schema validation], [JWT validation]</td>
</tr>
<tr>
<td>Unrestricted Access to Sensitive Business Flows</td>
<td>[Sequence mitigation], [Bot Management], [GraphQL Query Protection]</td>
</tr>
<tr>
<td>Server Side Request Forgery</td>
<td>[Schema validation], [WAF managed rules], <a href="/waf/custom-rules/">WAF custom rules</a></td>
</tr>
<tr>
<td>Security Misconfiguration</td>
<td>[Sequence mitigation], [Schema validation], [WAF managed rules], [GraphQL Query Protection]</td>
</tr>
<tr>
<td>Improper Inventory Management</td>
<td><a href="/api-shield/security/api-discovery/">Discovery</a>, <a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema learning</a></td>
</tr>
<tr>
<td>Unsafe Consumption of APIs</td>
<td>[JWT validation], [WAF managed rules]</td>
</tr>
</tbody>
</table>
