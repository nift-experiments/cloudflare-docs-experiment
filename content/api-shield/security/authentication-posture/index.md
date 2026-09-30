---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/security/authentication-posture/
  description: Identify authentication misconfigurations for API endpoints with Authentication Posture.
  full_title: Authentication Posture · Cloudflare API Shield docs
  head_html: <title>Authentication Posture · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Identify authentication misconfigurations for API endpoints with Authentication Posture."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/security/authentication-posture/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/security/authentication-posture/index.md"><meta property="og:title" content="Authentication Posture · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Identify authentication misconfigurations for API endpoints with Authentication Posture."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/security/authentication-posture/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="API Shield"><meta name="pcx_tags" content="Authentication"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/security/authentication-posture/#page","headline":"Authentication Posture \u00b7 Cloudflare API Shield docs","description":"Identify authentication misconfigurations for API endpoints with Authentication Posture.","url":"https://developers.cloudflare.com/api-shield/security/authentication-posture/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Authentication"]}</script>
  markdown: true
  noindex: false
  route: /api-shield/security/authentication-posture/
  schema: 1
---
<p>Authentication Posture detects API endpoints with missing or inconsistent authentication and alerts you to potential misconfigurations.</p>
<p>For example, a security team member may expect that their API endpoints <code>/api/v1/users</code> and <code>/api/v1/orders</code> require authentication. However, bugs in origin API authentication policies can create broken authentication vulnerabilities — allowing unauthenticated access to protected resources. Authentication Posture details the authentication status of successful requests to your API endpoints, alerting to potential misconfigurations.</p>
<p>Consider a typical e-commerce application. Users can browse items and prices without logging in. However, to retrieve order details via <code>GET /api/v1/orders/{order_id}</code>, users must log in and pass an Authorization HTTP header with all requests. Cloudflare alerts you via <a href="/security/security-insights/">Security Center Insights</a> and <a href="/api-shield/management-and-monitoring/endpoint-labels/">Endpoint labels</a> if successful requests reach this endpoint or any other endpoint without authentication when <span class="nb-glossary-tooltip" title="session identifier">session identifiers</span> are configured.</p>
<h2 id="process">Process</h2>
<p>After configuring <a href="/api-shield/get-started/#session-identifiers">session identifiers</a>, API Shield continuously scans your traffic for successful requests without authentication and labels your endpoints on a daily basis. Refer to the table below for the labeling methodology.</p>
<table>
<thead>
<tr>
<th>Description</th>
<th>2xx response codes</th>
<th>4xx, 5xx response codes</th>
</tr>
</thead>
<tbody>
<tr>
<td>If all requests are missing authentication, Cloudflare will apply the label:</td>
<td><code>cf-missing-auth</code></td>
<td>Without successful responses, no label will be added.</td>
</tr>
<tr>
<td>If only some requests are missing authentication, Cloudflare will apply the label:</td>
<td><code>cf-mixed-auth</code></td>
<td>Without successful responses, no label will be added.</td>
</tr>
</tbody>
</table>
<h3 id="examine-an-endpoint-s-authentication-details">Examine an endpoint's authentication details</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3199.md")
</div>
<p>The main authentication widget displays how many successful requests over the last seven days had session identifiers included with them, and which identifiers were included with the traffic.</p>
<p>The authentication-over-time chart shows a detailed breakdown over time of how clients successfully interacted with your API and which identifiers were used. A large increase in unauthenticated traffic may signal a security incident. Similarly, any successful unauthenticated traffic on an endpoint that is expected to be 100% authenticated can be a cause for concern.</p>
<p>Work with your development team to understand which authentication policies may need to be corrected on your API to stop unauthenticated traffic.</p>
<h3 id="stop-unauthenticated-traffic-with-cloudflare">Stop unauthenticated traffic with Cloudflare</h3>
<p>To block unauthenticated requests, create a <a href="/waf/custom-rules/">custom rule</a> using the <code>cf.api_gateway.auth_id_present</code> field. This field evaluates to <code>true</code> when the configured API Shield session identifiers are present on a request. You can also match on absence to detect unauthenticated traffic. Add a host and path match to scope the rule to specific endpoints.</p>
<h2 id="limitations">Limitations</h2>
<p>Authentication Posture can only apply when customers accurately set up session identifiers in API Shield. Session identifiers must uniquely identify authenticated users of your API. If you are unsure of your API's session identifier, consult with your development team.</p>
<h2 id="availability">Availability</h2>
<p>Authentication Posture is available for all Enterprise customers with an API Shield subscription.</p>
