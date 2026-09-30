---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/
  description: Insights resources and guides for Zero Trust analytics.
  full_title: Insights · Cloudflare One docs
  head_html: <title>Insights · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Insights resources and guides for Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/index.md"><meta property="og:title" content="Insights · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Insights resources and guides for Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-one/insights/#page","headline":"Insights \u00b7 Cloudflare One docs","description":"Insights resources and guides for Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/
  schema: 1
---
<p>Cloudflare One offers observability tools to monitor and troubleshoot your environment:</p>
<ul>
<li><a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> to monitor overall Cloudflare One usage.</li>
<li><a href="/cloudflare-one/insights/analytics/">Analytics Dashboards</a> to review organizational traffic trends and policy insights.</li>
<li><a href="/cloudflare-one/insights/logs/">Logs</a> for event-level investigation.</li>
<li><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for device, network, and application performance.</li>
</ul>
<h2 id="troubleshooting-workflow-example">Troubleshooting workflow example</h2>
<p>A user reports they cannot reach an internal application behind <a href="/cloudflare-one/">Cloudflare Access</a>. To address the issue:</p>
<ol>
<li>Check the <a href="/cloudflare-one/insights/analytics-overview/">Analytics overview dashboard</a> to review if other users are experiencing similar issues.</li>
<li>Review <a href="/cloudflare-one/insights/logs/">Logs</a> to examine the user's authentication attempts and blocked requests.</li>
<li>Use <a href="/cloudflare-one/insights/dex/">DEX</a> to evaluate the user's device health and network performance.</li>
</ol>
<h2 id="how-to-use-these-tools-together">How to use these tools together</h2>
<h3 id="onboarding">Onboarding</h3>
<p>After onboarding your devices and users, use these tools to confirm everything is set up correctly and to monitor your organization's activity.</p>
<ol>
<li>Start with <a href="/cloudflare-one/insights/logs/">Logs</a> to validate initial configuration and confirm that authentication is successful.</li>
<li>Use <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> to confirm expected patterns and policy activity.</li>
</ol>
<p>If your device is experiencing connectivity issues, Cloudflare recommends starting with <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/">troubleshooting WARP</a> as WARP misconfiguration is the most common cause of connectivity issues.</p>
<h3 id="daily-monitoring">Daily monitoring</h3>
<ol>
<li>
<p>Use <a href="/cloudflare-one/insights/analytics/">Analytics Dashboards</a> to understand trends and for visualizations of your log data.</p>
<p>Administrators typically start with Analytics Dashboards because they offer:</p>
<ul>
<li>A high-level view of activity across your products, like Access, or security use cases, such as AI and shadow IT.</li>
<li>Visibility into trends, provided through time-series graphs, to track the evolution of key metrics (such as <a href="/cloudflare-one/insights/analytics/gateway/#dns-query-analytics">DNS queries</a>, <a href="/cloudflare-one/insights/analytics/gateway/#network-session-analytics">network sessions</a>, <a href="/cloudflare-one/insights/analytics/gateway/#http-request-analytics">HTTP requests</a>, and <a href="/cloudflare-one/insights/analytics/data-analytics/">CASB posture/content findings</a>) over time.</li>
</ul>
</li>
<li>
<p>Use <a href="/cloudflare-one/insights/logs/">Logs</a> as needed for event-level verification.</p>
<p>Use Logs when you need to:</p>
<ul>
<li>Investigate a specific event; for example, a user's <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">failed authentication attempt</a> when trying to log in to an application.</li>
<li>Validate identity or device details; for example, confirming which user made the request, how they authenticated, and whether their device met required <a href="/cloudflare-one/insights/logs/dashboard-logs/posture-logs/">posture conditions</a>.</li>
<li>Confirm policy matches; for example, verifying which <a href="/cloudflare-one/access-controls/policies/#rule-types">specific rule</a> allowed, blocked, or challenged a user's request and why it was applied.</li>
</ul>
</li>
</ol>
<h3 id="user-reported-issues">User-reported issues</h3>
<p>Users may report problems like slow or failing connections to internal apps.</p>
<ol>
<li>Start with <a href="/cloudflare-one/insights/analytics/">Analytics Dashboards</a> to review whether the issue impacts others.</li>
<li>Check <a href="/cloudflare-one/insights/logs/">Logs</a> for failed authentication attempts, blocked requests, or unexpected policy matches.</li>
<li>Use <a href="/cloudflare-one/insights/dex/">DEX</a> to diagnose device- or network-level causes with <a href="/cloudflare-one/insights/dex/tests/">synthetic tests</a> and <a href="/cloudflare-one/insights/dex/monitoring/">device monitoring</a>.</li>
</ol>
