---
cp9:
  canonical: https://developers.cloudflare.com/privacy-proxy/reference/http-headers/
  description: HTTP headers used by Privacy Proxy for authentication, geolocation, and observability, including request and response formats.
  full_title: HTTP headers · Cloudflare Privacy Proxy docs
  head_html: <title>HTTP headers · Cloudflare Privacy Proxy docs</title><meta name="generator" content="Nift"><meta name="description" content="HTTP headers used by Privacy Proxy for authentication, geolocation, and observability, including request and response formats."><link rel="canonical" href="https://developers.cloudflare.com/privacy-proxy/reference/http-headers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-proxy/reference/http-headers/index.md"><meta property="og:title" content="HTTP headers · Cloudflare Privacy Proxy docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="HTTP headers used by Privacy Proxy for authentication, geolocation, and observability, including request and response formats."><meta property="og:url" content="https://developers.cloudflare.com/privacy-proxy/reference/http-headers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Proxy"><meta name="algolia_product_filter" content="Privacy Proxy"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Privacy Proxy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/privacy-proxy/reference/http-headers/#page","headline":"HTTP headers \u00b7 Cloudflare Privacy Proxy docs","description":"HTTP headers used by Privacy Proxy for authentication, geolocation, and observability, including request and response formats.","url":"https://developers.cloudflare.com/privacy-proxy/reference/http-headers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-proxy/reference/http-headers/
  schema: 1
---
<p>This page documents the HTTP headers used by Privacy Proxy for authentication, geolocation, and observability. For full observability details, refer to <a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a> and <a href="/privacy-proxy/reference/metrics/opentelemetry/">OpenTelemetry</a>.</p>
<h2 id="request-headers">Request headers</h2>
<p>Clients include the following headers when connecting to Privacy Proxy.</p>
<h3 id="proxy-authorization"><code>Proxy-Authorization</code></h3>
<p>Authenticates the client to the proxy. Required for all requests.</p>
<p>Pre-shared key format:</p>
<pre tabindex="0"><code class="language-http">Proxy-Authorization: Preshared &lt;key&gt;&#10;</code></pre>
<p>Privacy Pass token format:</p>
<pre tabindex="0"><code class="language-http">Proxy-Authorization: PrivateToken token=&lt;base64-encoded-token&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;key&gt;</code></td>
<td>The pre-shared key provided by Cloudflare</td>
</tr>
<tr>
<td><code>&lt;base64-encoded-token&gt;</code></td>
<td>A base64-encoded Privacy Pass token</td>
</tr>
</tbody>
</table>
<h3 id="graphql-analytics-api-request-headers">GraphQL Analytics API request headers</h3>
<p>When querying Privacy Proxy metrics via the GraphQL Analytics API, send a <code>POST</code> request to <code>https://api.cloudflare.com/client/v4/graphql</code>. For required headers and authentication details, refer to <a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a>.</p>
<h3 id="sec-ch-geohash"><code>sec-ch-geohash</code></h3>
<p>Specifies the client's geographic location for egress IP selection. Optional but recommended for accurate geolocation.</p>
<pre tabindex="0"><code class="language-http">sec-ch-geohash: &lt;geohash&gt;-&lt;country_code&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;geohash&gt;</code></td>
<td>A <a href="https://en.wikipedia.org/wiki/Geohash">geohash</a> string (typically 4-8 characters)</td>
</tr>
<tr>
<td><code>&lt;country_code&gt;</code></td>
<td>ISO 3166-1 alpha-2 country code</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-http">sec-ch-geohash: u4pruydqqvj-GB&#10;</code></pre>
<p>This example specifies a location in the United Kingdom.</p>
<hr />
<h2 id="response-headers">Response headers</h2>
<p>Privacy Proxy includes the following headers in responses.</p>
<h3 id="server-timing"><code>Server-Timing</code></h3>
<p>Provides timing information about proxy processing. This is part of the <a href="/privacy-proxy/reference/metrics/opentelemetry/">OpenTelemetry</a> observability pipeline.</p>
<pre tabindex="0"><code class="language-http">Server-Timing: proxy;dur=&lt;milliseconds&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;milliseconds&gt;</code></td>
<td>Processing time in milliseconds introduced by the proxy</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-http">Server-Timing: proxy;dur=8.2&#10;</code></pre>
<h3 id="graphql-analytics-api-response-headers">GraphQL Analytics API response headers</h3>
<p>For response headers returned by the GraphQL API, refer to <a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a>.</p>
<hr />
<h2 id="connect-request-format"><code>CONNECT</code> request format</h2>
<p>A complete <code>CONNECT</code> request to Privacy Proxy looks like this:</p>
<pre tabindex="0"><code class="language-http">CONNECT example.com:443 HTTP/2&#10;Host: example.com&#10;Proxy-Authorization: Preshared abc123xyz&#10;sec-ch-geohash: 9q8yy-US&#10;</code></pre>
<p>The proxy responds with a status code indicating success or failure:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>200 OK</code></td>
<td>Tunnel established successfully</td>
</tr>
<tr>
<td><code>403 Forbidden</code></td>
<td>Authentication failed</td>
</tr>
<tr>
<td><code>502 Bad Gateway</code></td>
<td>Could not connect to destination</td>
</tr>
<tr>
<td><code>503 Service Unavailable</code></td>
<td>Proxy temporarily unavailable</td>
</tr>
</tbody>
</table>
