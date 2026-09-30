---
cp9:
  canonical: https://developers.cloudflare.com/analytics/account-and-zone-analytics/account-analytics/
  description: View aggregated metrics across all account domains.
  full_title: Account analytics (beta) · Cloudflare Analytics docs
  head_html: <title>Account analytics (beta) · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="View aggregated metrics across all account domains."><link rel="canonical" href="https://developers.cloudflare.com/analytics/account-and-zone-analytics/account-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/account-and-zone-analytics/account-analytics/index.md"><meta property="og:title" content="Account analytics (beta) · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View aggregated metrics across all account domains."><meta property="og:url" content="https://developers.cloudflare.com/analytics/account-and-zone-analytics/account-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/account-and-zone-analytics/account-analytics/#page","headline":"Account analytics (beta) \u00b7 Cloudflare Analytics docs","description":"View aggregated metrics across all account domains.","url":"https://developers.cloudflare.com/analytics/account-and-zone-analytics/account-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/account-and-zone-analytics/account-analytics/
  schema: 1
---
<p>Cloudflare account analytics lets you access a wide range of aggregated metrics from all the sites under a specific Cloudflare account.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3149.md")
</aside>
<hr />
<h2 id="view-your-account-analytics">View your account analytics</h2>
<p>To view metrics for your site, in the Cloudflare dashboard, go to the <strong>Account Analytics</strong> page.</p>
<div class="nb-dash-button"></div>
<p>Once it loads, the Account Analytics app displays a collection of categorized charts with aggregated metrics for your account. To understand the various metrics available, refer to <em>Review your account metrics</em> below.</p>
<hr />
<h2 id="review-your-account-metrics">Review your account metrics</h2>
<p>This section outlines the aggregated metrics under each category. Before reviewing your metrics, let's define a couple of concepts used in some panels:</p>
<ul>
<li><em>Rate</em> -  Reflects the ratio between the amount for a specific data category and the total.</li>
<li><em>Bandwidth</em> - Refers to the number of bytes sent from the Cloudflare edge network to the requesting client.</li>
</ul>
<p>Also, note that:</p>
<ul>
<li>To filter metrics for a specific time period, use the dropdown in the top right.</li>
<li>Most metrics are grouped into panels representing different aspects of the underlying data.</li>
</ul>
<h3 id="summary-of-metrics">Summary of metrics</h3>
<p>Below is a brief description of the major elements comprising the metrics available.</p>
<h4 id="http-traffic">HTTP Traffic</h4>
<p>These charts aggregate data for HTTP traffic, and include:</p>
<p><img src="/assets/upstream/images/support/hc-dash-account-analytics-map.png" alt="Chart showing last week's data for HTTP traffic" /></p>
<ul>
<li>Spark lines for <em>Requests</em>, <em>Bandwidth</em>, <em>Page views</em>, and <em>Visitors</em> (<em>Unique IPs)</em></li>
<li>An interactive map that breaks down the number of requests by country</li>
<li>A table combining numerical and spark line data, sorted by total number of requests per country</li>
</ul>
<h4 id="security">Security</h4>
<p><img src="/assets/upstream/images/support/hc-dash-account-analytics_security_panel.png" alt="Panel displaying lines highlighting encryption metrics: requests, requests rate, bandwidth, and bandwidth rate" /></p>
<p>This panel features spark lines highlighting various encryption metrics, including: <em>requests</em>, <em>requests rate</em>, <em>bandwidth</em>, and <em>bandwidth rate</em>.  These also include a comparative percentage change based on the previous period.</p>
<h4 id="cache">Cache</h4>
<p><img src="/assets/upstream/images/support/hc-dash-account-analytics_cache_card.png" alt="Panel displaying lines for caching metrics: requests, requests rate, bandwidth, and bandwidth rate" /></p>
<p>This panel features spark lines for various caching metrics, including: <em>requests</em>, <em>requests rate</em>, <em>bandwidth</em>, and <em>bandwidth rate</em>.  These also include a comparative percentage change based on the previous equivalent period.  For example, if you selected <em>Last week</em> as your time period, the previous period refers to the <em>week</em> before.</p>
<h4 id="errors">Errors</h4>
<p><img src="/assets/upstream/images/support/hc-account-analytics_errors_card.png" alt="Panel displaying lines for 4xx and 5xx error rates" /></p>
<p>This panel displays spark lines for 4xx and 5xx error rates, respectively. Learn more about <a href="/support/troubleshooting/http-status-codes/">HTTP Status Codes</a>. </p>
<h4 id="network">Network</h4>
<p><img src="/assets/upstream/images/support/hc-dash-account-analytics_network_card.png" alt="Statistics showing the percentage of requests that use a specific version of HTTP" /></p>
<h4 id="client-http-version-used">Client HTTP Version Used</h4>
<p>These statistics show the percentage of requests that use a specific version of HTTP.</p>
<h4 id="traffic-served-over-ssl">Traffic Served Over SSL</h4>
<p>These statistics show the percentage of traffic that is encrypted using a specific version of SSL or TLS.</p>
<h4 id="content-type-breakdown">Content Type Breakdown</h4>
<p>These statistics show the number of requests based on the resource content type.</p>
