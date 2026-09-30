---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/
  description: Reference information for Analytics overview in Zero Trust analytics.
  full_title: Analytics overview · Cloudflare One docs
  head_html: <title>Analytics overview · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Analytics overview in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/index.md"><meta property="og:title" content="Analytics overview · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Analytics overview in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/#page","headline":"Analytics overview \u00b7 Cloudflare One docs","description":"Reference information for Analytics overview in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/analytics-overview/
  schema: 1
---
<p>The Cloudflare One Analytics overview provides a dashboard that reports on how Cloudflare One is protecting your organization and networks. Use this page to monitor usage and potential security concerns within your organization.</p>
<p>To view the Analytics overview, log in to <a href="https://one.dash.cloudflare.com">Cloudflare One</a> and go to <strong>Overview</strong>.</p>
<p>The Analytics overview includes reports and insights across the following products and categories:</p>
<ul>
<li><a href="#global-status">Global status</a> of your Zero Trust Organization</li>
<li><a href="#access">Access</a></li>
<li>Gateway
<ul>
<li><a href="#proxy-traffic">HTTP traffic</a></li>
<li><a href="#gateway-network-requests">Network traffic</a></li>
<li><a href="#dns-traffic">DNS traffic</a></li>
<li><a href="#gateway-insights">Firewall policies</a></li>
</ul>
</li>
</ul>
<p>Refer to <a href="/cloudflare-one/insights/">Insights overview</a> to learn how to use Analytics dashboards together with <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> and <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for complete visibility and troubleshooting.</p>
<h2 id="global-status">Global status</h2>
<p>In <strong>Global status</strong>, you can view a report on your organization's Cloudflare One adoption that contains the following metrics:</p>
<ul>
<li>Access apps configured</li>
<li>Gateway HTTP policies</li>
<li>Gateway network policies</li>
<li>Gateway DNS policies</li>
<li>SaaS integrations</li>
<li>Data Loss Prevention (DLP) profiles</li>
</ul>
<p>You can also view a report on your <a href="/cloudflare-one/team-and-resources/users/seat-management/">seat usage</a> across your Zero Trust Organization that contains the following metrics. A seat is a billable unit consumed when a user authenticates to your Zero Trust organization.</p>
<ul>
<li>Total seats</li>
<li>Used seats</li>
<li>Unused seats</li>
</ul>
<h2 id="access">Access</h2>
<p>In <strong>Access</strong>, you can view a report on your <a href="/cloudflare-one/access-controls/">Cloudflare Access</a> configuration that contains:</p>
<p><strong>Metrics:</strong></p>
<ul>
<li>Total access attempts</li>
<li>Granted access</li>
<li>Denied (policy violation)</li>
<li>Active logins over time</li>
<li>Top applications with most logins</li>
</ul>
<p><strong>Filters:</strong></p>
<ul>
<li>Access data by country</li>
</ul>
<h2 id="gateway">Gateway</h2>
<h3 id="proxy-traffic">Proxy traffic</h3>
<p>In <strong>Proxy traffic</strong>, you can view a report on your <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> HTTP traffic that contains:</p>
<p><strong>Metrics:</strong></p>
<ul>
<li>Total requests over time</li>
<li>Allowed requests</li>
<li>Blocked requests</li>
<li>Isolated requests (served through <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a>)</li>
<li>Do not inspect requests</li>
<li>Top bandwidth consumers (GB)</li>
<li>Top denied users</li>
</ul>
<p><strong>Filters:</strong></p>
<ul>
<li>Gateway HTTP traffic data by country</li>
</ul>
<h3 id="gateway-network-requests">Gateway (network requests)</h3>
<p>In <strong>Gateway (network requests)</strong>, you can view a report on your Gateway network traffic that contains:</p>
<p><strong>Metrics:</strong></p>
<ul>
<li>Total sessions</li>
<li>Authenticated sessions</li>
<li>Blocked sessions</li>
<li>Allowed sessions</li>
<li>Override sessions</li>
<li>Top bandwidth consumers in GB</li>
<li>Top denied users</li>
</ul>
<p><strong>Filters:</strong></p>
<ul>
<li>Gateway network traffic data by country</li>
</ul>
<h3 id="dns-traffic">DNS traffic</h3>
<p>In <strong>DNS traffic</strong>, you can view a report on your Gateway DNS traffic that contains:</p>
<p><strong>Metrics:</strong></p>
<ul>
<li>Total DNS queries</li>
<li>Allowed DNS queries</li>
<li>Blocked DNS queries</li>
<li>Override DNS queries</li>
<li>Safe Search DNS queries</li>
<li>Restricted DNS queries</li>
<li>Other DNS queries</li>
</ul>
<p><strong>Filters:</strong></p>
<ul>
<li>Gateway DNS traffic by query type</li>
<li>Gateway DNS traffic by country</li>
</ul>
<h3 id="gateway-insights">Gateway insights</h3>
<p>In <strong>Gateway insights</strong>, you can view a report on your Gateway firewall policies that contains the following metrics:</p>
<ul>
<li>Top domain blocking policies</li>
<li>Most user queries</li>
<li>Top devices</li>
<li>Top countries</li>
</ul>
<h3 id="casb-metrics">CASB metrics</h3>
<p>In <strong>CASB</strong>, you can review instances of security issues — such as misconfigurations, unauthorized user activity, and shadow IT — found in your SaaS integrations by <a href="/cloudflare-one/cloud-and-saas-findings/">Cloudflare CASB</a>.</p>
<ul>
<li>Integrations by number of findings</li>
<li><a href="/cloudflare-one/data-loss-prevention/">DLP</a> findings by profile name</li>
</ul>
