---
cp9:
  canonical: https://developers.cloudflare.com/spectrum/reference/logs/
  description: Access Spectrum connection lifecycle logs through Logpush.
  full_title: Event logs · Cloudflare Spectrum docs
  head_html: <title>Event logs · Cloudflare Spectrum docs</title><meta name="generator" content="Nift"><meta name="description" content="Access Spectrum connection lifecycle logs through Logpush."><link rel="canonical" href="https://developers.cloudflare.com/spectrum/reference/logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/spectrum/reference/logs/index.md"><meta property="og:title" content="Event logs · Cloudflare Spectrum docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access Spectrum connection lifecycle logs through Logpush."><meta property="og:url" content="https://developers.cloudflare.com/spectrum/reference/logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Spectrum"><meta name="algolia_product_filter" content="Spectrum"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Spectrum"><meta name="pcx_tags" content="Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/spectrum/reference/logs/#page","headline":"Event logs \u00b7 Cloudflare Spectrum docs","description":"Access Spectrum connection lifecycle logs through Logpush.","url":"https://developers.cloudflare.com/spectrum/reference/logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging"]}</script>
  markdown: true
  noindex: false
  route: /spectrum/reference/logs/
  schema: 1
---
<p>Spectrum logs the entire lifecycle of every client that connects through it. These event logs are available through Logpush as a separate category (dataset type <code>spectrum_events</code>); they are not part of HTTP log events.</p>
<p>For each connection, Spectrum logs a connect event and either a disconnect or error event. Details on status codes can be found below.</p>
<h2 id="configure-logpush">Configure Logpush</h2>
<p>Spectrum <a href="/logs/logpush/logpush-job/datasets/">log events</a> can be configured through the dashboard or API, depending on your preferred <a href="/logs/logpush/logpush-job/enable-destinations/">destination</a>.</p>
<h2 id="status-codes">Status Codes</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="spectrum-status-codes-are-not-http-status-codes">Spectrum status codes are not HTTP status codes</h3>
@markup("md", "content/.markup/bodies/13864.md")
</aside>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>Connection was opened successfully.</td>
</tr>
<tr>
<td>200</td>
<td>Normal connection closure.</td>
</tr>
<tr>
<td>400</td>
<td>The TLS client hello sent during the client/edge TLS handshake contained an invalid SNI.</td>
</tr>
<tr>
<td>403</td>
<td>Connection closed because the client IP matched a firewall rule with deny action.</td>
</tr>
<tr>
<td>443</td>
<td>The client TLS handshake failed.</td>
</tr>
<tr>
<td>444</td>
<td>The origin closed the connection by sending a reset (RST) packet. Not all data may have been sent.</td>
</tr>
<tr>
<td>445</td>
<td>A timeout event (ETIMEDOUT) occurred on an established connection to origin.</td>
</tr>
<tr>
<td>446</td>
<td>Origin keepalive expired (EHOSTUNREACH).</td>
</tr>
<tr>
<td>447</td>
<td>Error while reading from or writing to an established origin connection (ECONNREFUSED).</td>
</tr>
<tr>
<td>448</td>
<td>Origin connection closed due to a broken pipe (EPIPE).</td>
</tr>
<tr>
<td>490</td>
<td>Client TLS error on established connection.</td>
</tr>
<tr>
<td>495</td>
<td>Client connection received an error (ECONNREFUSED).</td>
</tr>
<tr>
<td>496</td>
<td>Client host is unreachable (EHOSTUNREACH).</td>
</tr>
<tr>
<td>497</td>
<td>A timeout event (ETIMEDOUT) occurred on an established connection to client.</td>
</tr>
<tr>
<td>498</td>
<td>Established client connection closed due to broken pipe (EPIPE).</td>
</tr>
<tr>
<td>499</td>
<td>The client closed the connection by sending a reset (RST) packet. Not all data may have been sent.</td>
</tr>
<tr>
<td>500</td>
<td>Internal Cloudflare error.</td>
</tr>
<tr>
<td>503</td>
<td>Error related to performing the TLS handshake with keyless SSL.</td>
</tr>
<tr>
<td>520</td>
<td>Unknown origin connection error.</td>
</tr>
<tr>
<td>521</td>
<td>Origin refused to open the connection (ECONNREFUSED).</td>
</tr>
<tr>
<td>522</td>
<td>Opening a connection to origin failed: ETIMEDOUT</td>
</tr>
<tr>
<td>523</td>
<td>Opening a connection to origin failed: ENETUNREACH</td>
</tr>
<tr>
<td>524</td>
<td>Opening a connection to origin failed due to an internal system error.</td>
</tr>
<tr>
<td>530</td>
<td>Internal error while resolving origin to an IP.</td>
</tr>
<tr>
<td>531</td>
<td>Could not resolve origin to an IP.</td>
</tr>
<tr>
<td>532</td>
<td>The origin connection was not opened because the origin IP is blocked.</td>
</tr>
<tr>
<td>533</td>
<td>Internal error while resolving origin to an IP.</td>
</tr>
<tr>
<td>540</td>
<td>The client/edge TLS handshake failed due to an invalid configuration.</td>
</tr>
<tr>
<td>999</td>
<td>Unknown connection error.</td>
</tr>
</tbody>
</table>
