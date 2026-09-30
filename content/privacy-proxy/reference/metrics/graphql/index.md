---
cp9:
  canonical: https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/
  description: Query Privacy Proxy request, connection, and authentication metrics using the Cloudflare GraphQL Analytics API.
  full_title: GraphQL Analytics API · Cloudflare Privacy Proxy docs
  head_html: <title>GraphQL Analytics API · Cloudflare Privacy Proxy docs</title><meta name="generator" content="Nift"><meta name="description" content="Query Privacy Proxy request, connection, and authentication metrics using the Cloudflare GraphQL Analytics API."><link rel="canonical" href="https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/index.md"><meta property="og:title" content="GraphQL Analytics API · Cloudflare Privacy Proxy docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query Privacy Proxy request, connection, and authentication metrics using the Cloudflare GraphQL Analytics API."><meta property="og:url" content="https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Proxy"><meta name="algolia_product_filter" content="Privacy Proxy"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Privacy Proxy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/#page","headline":"GraphQL Analytics API \u00b7 Cloudflare Privacy Proxy docs","description":"Query Privacy Proxy request, connection, and authentication metrics using the Cloudflare GraphQL Analytics API.","url":"https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-proxy/reference/metrics/graphql/
  schema: 1
---
<p>Privacy Proxy exposes metrics through Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. All metrics are queryable through a single endpoint:</p>
<pre tabindex="0"><code class="language-txt">POST https://api.cloudflare.com/client/v4/graphql&#10;</code></pre>
<p>Before you begin, you will need:</p>
<ul>
<li><strong>API token</strong> — Create a token with <em>Account Analytics</em> read permissions. For more information, refer to our Analytics API token documentation: <a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">Configure an Analytics API token</a>.</li>
<li><strong>Account ID</strong> — Your Cloudflare account ID, passed as <code>accountTag</code> in queries. For more information, refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find account and zone IDs</a>.</li>
</ul>
<hr />
<h2 id="making-a-request">Making a request</h2>
<p>The following example shows how to query your Privacy Proxy metrics daily request volume using curl. Replace the placeholder values with your own.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/graphql \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;query&quot;: &quot;query DailyRequestVolume($accountTag: String!, $startDate: Date!, $endDate: Date!) { viewer { accounts(filter: { accountTag: $accountTag }) { privacyProxyRequestMetricsAdaptiveGroups(filter: { date_geq: $startDate, date_leq: $endDate }, limit: 10000, orderBy: [date_ASC]) { count dimensions { date } } } } }&quot;,&#10;    &quot;variables&quot;: {&#10;      &quot;accountTag&quot;: &quot;&lt;YOUR_ACCOUNT_TAG&gt;&quot;,&#10;      &quot;startDate&quot;: &quot;2026-04-04&quot;,&#10;      &quot;endDate&quot;: &quot;2026-04-06&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<hr />
<h2 id="available-nodes">Available nodes</h2>
<p>Four GraphQL nodes are available. All four return aggregate data only — no raw per-connection records are exposed.</p>
<ol>
<li><code>privacyProxyRequestMetricsAdaptiveGroups</code> — Query aggregate request volume and error rates, filterable by time, location, endpoint, status code, and proxy status dimensions.</li>
<li><code>privacyProxyIngressConnMetricsAdaptiveGroups</code> — Query client-to-proxy connection counts, bytes transferred, and latency percentiles, filterable by time, location, endpoint, and transport dimensions.</li>
<li><code>privacyProxyEgressConnMetricsAdaptiveGroups</code> — Query proxy-to-origin connection counts, bytes transferred, and latency percentiles, filterable by time, location, endpoint, and transport dimensions.</li>
<li><code>privacyProxyAuthMetricsAdaptiveGroups</code> — Query authentication attempt counts, filterable by time, location, endpoint, auth method, and auth result dimensions.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="adaptive-sampling">Adaptive sampling</h3>
@markup("md", "content/.markup/bodies/11117.md")
</aside>
<hr />
<h2 id="schema">Schema</h2>
<details class="nb-details"><summary>Metrics</summary><div class="nb-details-body">
@input("content/.markup/bodies/11121.md")
</div></details>
<details class="nb-details"><summary>Dimensions</summary><div class="nb-details-body">
@input("content/.markup/bodies/11127.md")
</div></details>
<details class="nb-details"><summary>Arguments</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11128.md")
</div></details>
<hr />
<h2 id="sample-queries">Sample queries</h2>
<details class="nb-details"><summary>privacyProxyRequestMetricsAdaptiveGroups node</summary><div class="nb-details-body">
@input("content/.markup/bodies/11133.md")
</div></details>
<details class="nb-details"><summary>privacyProxyIngressConnMetricsAdaptiveGroups node</summary><div class="nb-details-body">
@input("content/.markup/bodies/11137.md")
</div></details>
<details class="nb-details"><summary>privacyProxyEgressConnMetricsAdaptiveGroups node</summary><div class="nb-details-body">
@input("content/.markup/bodies/11141.md")
</div></details>
<details class="nb-details"><summary>privacyProxyAuthMetricsAdaptiveGroups node</summary><div class="nb-details-body">
@input("content/.markup/bodies/11145.md")
</div></details>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API — getting started</a></li>
<li><a href="/analytics/graphql-api/features/filtering/">GraphQL Analytics API — filtering</a></li>
<li><a href="/privacy-proxy/reference/proxy-status/">Proxy status reference</a> — All possible <code>proxyStatus</code> values and their meanings.</li>
</ul>
