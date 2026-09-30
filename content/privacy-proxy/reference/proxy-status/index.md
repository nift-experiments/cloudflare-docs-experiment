---
cp9:
  canonical: https://developers.cloudflare.com/privacy-proxy/reference/proxy-status/
  description: All possible proxyStatus values for Privacy Proxy error classification in GraphQL Analytics and OpenTelemetry metrics.
  full_title: Proxy status reference · Cloudflare Privacy Proxy docs
  head_html: <title>Proxy status reference · Cloudflare Privacy Proxy docs</title><meta name="generator" content="Nift"><meta name="description" content="All possible proxyStatus values for Privacy Proxy error classification in GraphQL Analytics and OpenTelemetry metrics."><link rel="canonical" href="https://developers.cloudflare.com/privacy-proxy/reference/proxy-status/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-proxy/reference/proxy-status/index.md"><meta property="og:title" content="Proxy status reference · Cloudflare Privacy Proxy docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="All possible proxyStatus values for Privacy Proxy error classification in GraphQL Analytics and OpenTelemetry metrics."><meta property="og:url" content="https://developers.cloudflare.com/privacy-proxy/reference/proxy-status/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Proxy"><meta name="algolia_product_filter" content="Privacy Proxy"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Privacy Proxy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/privacy-proxy/reference/proxy-status/#page","headline":"Proxy status reference \u00b7 Cloudflare Privacy Proxy docs","description":"All possible proxyStatus values for Privacy Proxy error classification in GraphQL Analytics and OpenTelemetry metrics.","url":"https://developers.cloudflare.com/privacy-proxy/reference/proxy-status/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-proxy/reference/proxy-status/
  schema: 1
---
<p>The <code>proxyStatus</code> dimension provides proxy-level error classification. This field is available in both <a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a> and <a href="/privacy-proxy/reference/metrics/opentelemetry/">OpenTelemetry</a> metrics. The value is an empty string when no proxy-level error occurred.</p>
<hr />
<h2 id="proxystatus-values"><code>proxyStatus</code> values</h2>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>dns_error</code></td>
<td>The proxy encountered a DNS error when resolving the next hop hostname.</td>
</tr>
<tr>
<td><code>dns_timeout</code></td>
<td>The proxy timed out while resolving the next hop hostname.</td>
</tr>
<tr>
<td><code>destination_not_found</code></td>
<td>The proxy cannot determine the appropriate next hop for this request.</td>
</tr>
<tr>
<td><code>destination_unavailable</code></td>
<td>The proxy considers the next hop unavailable (for example, recent failures or health check is down).</td>
</tr>
<tr>
<td><code>destination_ip_prohibited</code></td>
<td>The proxy is configured to prohibit connections to the next hop IP address.</td>
</tr>
<tr>
<td><code>destination_ip_unroutable</code></td>
<td>The proxy cannot find a route to the next hop IP address.</td>
</tr>
<tr>
<td><code>connection_refused</code></td>
<td>The proxy's connection to the next hop was refused.</td>
</tr>
<tr>
<td><code>connection_terminated</code></td>
<td>The proxy's connection to the next hop was closed before any response was received.</td>
</tr>
<tr>
<td><code>connection_timeout</code></td>
<td>The proxy's attempt to open a connection to the next hop timed out.</td>
</tr>
<tr>
<td><code>connection_read_timeout</code></td>
<td>The proxy was expecting data on a connection but received none within the configured time limit.</td>
</tr>
<tr>
<td><code>connection_write_timeout</code></td>
<td>The proxy was attempting to write data to a connection but was unable to.</td>
</tr>
<tr>
<td><code>connection_limit_reached</code></td>
<td>The proxy's configured connection limit to the next hop has been exceeded.</td>
</tr>
<tr>
<td><code>source_addr_in_use</code></td>
<td>The proxy cannot assign a source address when connecting to the next hop.</td>
</tr>
<tr>
<td><code>source_addr_not_available</code></td>
<td>The proxy cannot assign a source address (bind failure or source host resolution failure).</td>
</tr>
<tr>
<td><code>tls_protocol_error</code></td>
<td>The proxy encountered a TLS error when communicating with the next hop.</td>
</tr>
<tr>
<td><code>tls_certificate_error</code></td>
<td>The proxy encountered an error verifying the certificate presented by the next hop.</td>
</tr>
<tr>
<td><code>http_request_error</code></td>
<td>The proxy is generating a client (4xx) response on the origin's behalf.</td>
</tr>
<tr>
<td><code>http_upgrade_failed</code></td>
<td>The HTTP Upgrade between the proxy and the next hop failed.</td>
</tr>
<tr>
<td><code>http_request_denied</code></td>
<td>The proxy rejected the HTTP request based on its configuration or policy.</td>
</tr>
<tr>
<td><code>proxy_internal_error</code></td>
<td>The proxy encountered an internal error unrelated to the origin.</td>
</tr>
<tr>
<td><code>proxy_loop_detected</code></td>
<td>The proxy tried to forward the request to itself.</td>
</tr>
<tr>
<td><code>http_protocol_error</code></td>
<td>The proxy encountered an HTTP protocol error when communicating with the next hop.</td>
</tr>
<tr>
<td><code>http_response_incomplete</code></td>
<td>The proxy received an incomplete response from the next hop.</td>
</tr>
<tr>
<td><code>rate_limited</code></td>
<td>The client has reached the maximum number of connections per second to a single origin.</td>
</tr>
</tbody>
</table>
