---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/privacy-proxy/
  description: '2026-04-15'
  full_title: privacy-proxy changelog | Cloudflare Docs
  head_html: <title>privacy-proxy changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-04-15"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/privacy-proxy/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="privacy-proxy changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-04-15"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/privacy-proxy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/privacy-proxy/#page","headline":"privacy-proxy changelog | Cloudflare Docs","description":"2026-04-15","url":"https://developers.cloudflare.com/changelog/product/privacy-proxy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/privacy-proxy/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="privacy-proxy-metrics-now-available-via-graphql-analytics-api"><a href="/changelog/post/2026-04-15-graphql-analytics-api/">Privacy Proxy metrics now available via GraphQL Analytics API</a></h2>
<p><em>2026-04-15</em></p>
<p>Privacy Proxy metrics are now queryable through Cloudflare's <a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a>, the new default method for accessing Privacy Proxy observability data. All metrics are available through a single endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/graphql \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;query&quot;: &quot;{ viewer { accounts(filter: { accountTag: $accountTag }) { privacyProxyRequestMetricsAdaptiveGroups(filter: { date_geq: $startDate, date_leq: $endDate }, limit: 10000, orderBy: [date_ASC]) { count dimensions { date } } } } }&quot;,&#10;    &quot;variables&quot;: {&#10;      &quot;accountTag&quot;: &quot;&lt;YOUR_ACCOUNT_TAG&gt;&quot;,&#10;      &quot;startDate&quot;: &quot;2026-04-04&quot;,&#10;      &quot;endDate&quot;: &quot;2026-04-06&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-04-15-graphql-analytics-api-available-nodes">Available nodes</h4>
<p>Four GraphQL nodes are now live, providing aggregate metrics across all key dimensions of your Privacy Proxy deployment:</p>
<ul>
<li><strong><code>privacyProxyRequestMetricsAdaptiveGroups</code></strong> — Request volume, error rates, status codes, and proxy status breakdowns.</li>
<li><strong><code>privacyProxyIngressConnMetricsAdaptiveGroups</code></strong> — Client-to-proxy connection counts, bytes transferred, and latency percentiles.</li>
<li><strong><code>privacyProxyEgressConnMetricsAdaptiveGroups</code></strong> — Proxy-to-origin connection counts, bytes transferred, and latency percentiles.</li>
<li><strong><code>privacyProxyAuthMetricsAdaptiveGroups</code></strong> — Authentication attempt counts by method and result.</li>
</ul>
<p>All nodes support filtering by time, data center (<code>coloCode</code>), and endpoint, with additional node-specific dimensions such as transport protocol and authentication method.</p>
<h4 id="2026-04-15-graphql-analytics-api-what-this-means-for-existing-opentelemetry-users">What this means for existing OpenTelemetry users</h4>
<p>OpenTelemetry-based metrics export remains available. The GraphQL Analytics API is now the recommended default method — a plug-and-play method that requires no collector infrastructure, saving engineering overhead.</p>
<h4 id="2026-04-15-graphql-analytics-api-learn-more">Learn more</h4>
<ul>
<li><a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API for Privacy Proxy</a></li>
<li><a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API — getting started</a></li>
</ul>



