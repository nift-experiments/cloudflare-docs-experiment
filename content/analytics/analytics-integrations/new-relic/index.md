---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-integrations/new-relic/
  description: This tutorial explains how to analyze Cloudflare metrics using the New Relic One Cloudflare Quickstart.
  full_title: New Relic · Cloudflare Analytics docs
  head_html: <title>New Relic · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial explains how to analyze Cloudflare metrics using the New Relic One Cloudflare Quickstart."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-integrations/new-relic/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-integrations/new-relic/index.md"><meta property="og:title" content="New Relic · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial explains how to analyze Cloudflare metrics using the New Relic One Cloudflare Quickstart."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-integrations/new-relic/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Analytics,Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-integrations/new-relic/#page","headline":"New Relic \u00b7 Cloudflare Analytics docs","description":"This tutorial explains how to analyze Cloudflare metrics using the New Relic One Cloudflare Quickstart.","url":"https://developers.cloudflare.com/analytics/analytics-integrations/new-relic/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-integrations/new-relic/
  schema: 1
---
<p>This tutorial explains how to analyze Cloudflare metrics using the <a href="https://newrelic.com/instant-observability/cloudflare/fc2bb0ac-6622-43c6-8c1f-6a4c26ab5434">New Relic One Cloudflare Quickstart</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before sending your Cloudflare log data to New Relic, make sure that you:</p>
<ul>
<li>Have a Cloudflare Enterprise account with Cloudflare Logs enabled.</li>
<li>Have a New Relic account.</li>
<li>Configure <a href="/logs/logpush/logpush-job/enable-destinations/new-relic/">Logpush to New Relic</a>.</li>
</ul>
<h2 id="task-1-install-the-cloudflare-network-logs-quickstart">Task 1 - Install the Cloudflare Network Logs quickstart</h2>
<ol>
<li>Log in to New Relic.</li>
<li>Click the Instant Observability button (top right).</li>
<li>Search for <strong>Cloudflare Network Logs</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/fundamentals/new-relic/screenshots/cloudflare-network-logs.png" alt="Cloudflare Network Logs install screen" /></p>
<ol start="4">
<li>Click <strong>Install this quickstart</strong>.</li>
<li>Follow the steps to deploy.</li>
</ol>
<h2 id="task-2-view-the-cloudflare-dashboards">Task 2 - View the Cloudflare Dashboards</h2>
<p>You can view your dashboards on the New Relic dashboard page. The dashboards include the following information:</p>
<h3 id="overview">Overview</h3>
<p>Get a quick overview of the most important metrics from your websites and applications on the Cloudflare network.</p>
<p><img src="/assets/upstream/images/fundamentals/new-relic/dashboard/dash-1.png" alt="Cloudflare Network Logs install screen" /></p>
<h3 id="security">Security</h3>
<p>Get insights on threats to your websites and applications, including number of threats taken action on by the Web Application Firewall (WAF), threats over time, top threat countries, and more.</p>
<p><img src="/assets/upstream/images/fundamentals/new-relic/dashboard/dash-2.png" alt="Cloudflare Network security metrics screen" /></p>
<h3 id="performance">Performance</h3>
<p>Identify and address performance issues and caching misconfigurations. Metrics include total requests, total versus cached requests, total versus origin requests.</p>
<p><img src="/assets/upstream/images/fundamentals/new-relic/dashboard/dash-3.png" alt="Cloudflare Network Logs performance metrics screen" /></p>
<h3 id="reliability">Reliability</h3>
<p>Get insights on the availability of your websites and Applications. Metrics include, edge response status over time, percentage of <code>3xx</code>/<code>4xx</code>/<code>5xx</code> errors over time, and more.</p>
<p><img src="/assets/upstream/images/fundamentals/new-relic/dashboard/dash-4.png" alt="Cloudflare Network Logs reliability metrics screen" /></p>
