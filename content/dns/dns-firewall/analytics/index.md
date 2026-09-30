---
cp9:
  canonical: https://developers.cloudflare.com/dns/dns-firewall/analytics/
  description: Access DNS Firewall query analytics and configure Logpush for DNS logs.
  full_title: Analytics and logs · Cloudflare DNS docs
  head_html: <title>Analytics and logs · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Access DNS Firewall query analytics and configure Logpush for DNS logs."><link rel="canonical" href="https://developers.cloudflare.com/dns/dns-firewall/analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/dns-firewall/analytics/index.md"><meta property="og:title" content="Analytics and logs · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access DNS Firewall query analytics and configure Logpush for DNS logs."><meta property="og:url" content="https://developers.cloudflare.com/dns/dns-firewall/analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="DNS Firewall"><meta name="pcx_tags" content="Analytics,GraphQL,Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/dns/dns-firewall/analytics/#page","headline":"Analytics and logs \u00b7 Cloudflare DNS docs","description":"Access DNS Firewall query analytics and configure Logpush for DNS logs.","url":"https://developers.cloudflare.com/dns/dns-firewall/analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics","GraphQL","Logging"]}</script>
  markdown: true
  noindex: false
  route: /dns/dns-firewall/analytics/
  schema: 1
---
<p>Consider the sections below to learn how to access analytics and logs for your DNS Firewall.</p>
<h2 id="analytics">Analytics</h2>
<p>DNS Firewall analytics allow you to evaluate data about DNS queries to your account.</p>
<h3 id="availability-and-limits">Availability and limits</h3>
<p>The historical data available covers 62 days and the maximum time interval you can get data for is also 62 days.</p>
<h3 id="dashboard">Dashboard</h3>
<p>For a quick summary, view your DNS Firewall analytics on the dashboard. The DNS analytics dashboard contains <a href="#panels">four main panels</a>. The filters and time frame that you specify at the top of the page apply to all of them.</p>
<p>In the Cloudflare dashboard, go to the <strong>DNS Firewall Analytics</strong> page.</p>
<div class="nb-dash-button"></div>
<h4 id="available-dimensions">Available dimensions</h4>
<ul>
<li>Query name</li>
<li>Query type (same as DNS record type)</li>
<li>Cluster</li>
<li>Cluster IP</li>
<li>Response code</li>
<li>Response reason (refer to <a href="#response-reasons">descriptions</a> below)</li>
<li>Response cached (cached or uncached)</li>
<li>Response stale (stale or fresh)</li>
<li>Data center</li>
<li>Source IP</li>
<li>Upstream nameserver IP</li>
<li>Protocol (UDP or TCP)</li>
<li>IP version (IPv4 or IPv6)</li>
</ul>
<h4 id="panels">Panels</h4>
<p>The filters and time frame that you specify at the top of the page apply to all of the available panels.</p>
<ul>
<li>
<p><strong>Query summary</strong>: the number of queries and their distribution over time. This information is segmented by each of the <a href="#available-dimensions">available dimensions</a>. You can select the dimensions through the different tabs above the graph and quickly filter for or exclude a certain value from the results by hovering over it and selecting <strong>Filter</strong> or <strong>Exclude</strong>.</p>
</li>
<li>
<p><strong>Query statistics</strong>: an overview of query metrics. Namely, <strong>Total queries</strong>, <strong>Cached queries</strong>, <strong>Uncached queries</strong>, and <strong>Stale cache queries</strong>.</p>
<details class="nb-details"><summary>Processing time and response time</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/7705.md")
</div></details>
<pre tabindex="0"><code>  &lt;details class=&quot;nb-details&quot;&gt;&lt;summary&gt;90th percentile (p90)&lt;/summary&gt;&lt;div class=&quot;nb-details-body&quot;&gt;&#10;</code></pre>
@markup("md", "content/.markup/bodies/7706.md")
</div></details>
<ul>
<li><strong>DNS queries by data center</strong>: a map indicating which Cloudflare data centers have handled DNS queries to your account. You can also find a list of the top ten results and quickly filter for or exclude a certain data center from the results by hovering over it and selecting <strong>Filter</strong> or <strong>Exclude</strong>.</li>
<li><strong>Top query statistics</strong>: a breakdown of the top queries grouped by the <a href="#available-dimensions">available dimensions</a>. You can expand each card to list more results and search for specific values.</li>
</ul>
<h3 id="graphql">GraphQL</h3>
<p>Use the <a href="/analytics/graphql-api/">GraphQL API</a> to access DNS Firewall analytics. Refer to the GraphQL Analytics API documentation for guidance on how to <a href="/analytics/graphql-api/getting-started/">get started</a>.</p>
<p>The DNS Firewall analytics has two <a href="/analytics/graphql-api/getting-started/querying-basics/">schemas</a>:</p>
<ul>
<li><code>dnsFirewallAnalyticsAdaptive</code>: Retrieve information about individual DNS Firewall queries.</li>
<li><code>dnsFirewallAnalyticsAdaptiveGroups</code>: Get reports on aggregate information only.</li>
</ul>
<h3 id="api">API <span class="nb-badge">Legacy</span></h3>
<p>You can also use the DNS Firewall API <a href="/api/resources/dns_firewall/subresources/analytics/subresources/reports/">reports endpoint</a>.</p>
<hr />
<h2 id="logs">Logs</h2>
<p>You can <a href="/logs/logpush/">set up Logpush</a> to deliver <a href="/logs/logpush/logpush-job/datasets/account/dns_firewall_logs/">DNS Firewall logs</a> to a storage service, SIEM, or log management provider.</p>
<h2 id="response-reasons">Response reasons</h2>
<p>When analyzing why Cloudflare DNS Firewall responded in one way or another to a specific query, consider the <code>responseReason</code> log field.</p>
<p>The following table provides a description for each of the values that might be returned as a response reason:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>success</code></td>
<td>Response was successfully served, either from Cloudflare cache or forwarded from the upstream.</td>
</tr>
<tr>
<td><code>upstream_failure</code></td>
<td>Response could not be fetched from the upstream due to the upstream failing to respond.</td>
</tr>
<tr>
<td><code>upstream_servfail</code></td>
<td>Response could not be fetched from the upstream due to the upstream responding with <code>SERVFAIL</code>.</td>
</tr>
<tr>
<td><code>invalid_query</code></td>
<td>Query is invalid and cannot be processed.</td>
</tr>
<tr>
<td><code>any_type_blocked</code></td>
<td>Query of type <code>ANY</code> was blocked according to your <a href="/dns/dns-firewall/setup/">DNS Firewall settings</a> (<a href="https://www.rfc-editor.org/rfc/rfc8482.html">RFC 8482</a>).</td>
</tr>
<tr>
<td><code>rate_limit</code></td>
<td>Query was rate limited according to your <a href="/dns/dns-firewall/setup/">DNS Firewall settings</a>.</td>
</tr>
<tr>
<td><code>chaos_success</code></td>
<td>Response for <a href="https://en.wikipedia.org/wiki/Chaosnet">Chaos class</a> was successfully served.</td>
</tr>
<tr>
<td><code>attack_mitigation_block</code></td>
<td>Query was blocked as part of <a href="/dns/dns-firewall/random-prefix-attacks/">random prefix attack mitigation</a>.</td>
</tr>
<tr>
<td><code>unknown</code></td>
<td>There was an unknown error.</td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">the total time taken to handle a query within DNS Firewall.</li>
<li id="footnote-2">the time it takes when an answer is not cached and Cloudflare has to get the answer from your upstream nameservers.</li></ol></section>
