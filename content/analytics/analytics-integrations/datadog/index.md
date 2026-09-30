---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-integrations/datadog/
  description: This tutorial explains how to analyze Cloudflare metrics using the Cloudflare Integration tile for Datadog
  full_title: Datadog · Cloudflare Analytics docs
  head_html: <title>Datadog · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial explains how to analyze Cloudflare metrics using the Cloudflare Integration tile for Datadog"><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-integrations/datadog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-integrations/datadog/index.md"><meta property="og:title" content="Datadog · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial explains how to analyze Cloudflare metrics using the Cloudflare Integration tile for Datadog"><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-integrations/datadog/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Analytics,Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-integrations/datadog/#page","headline":"Datadog \u00b7 Cloudflare Analytics docs","description":"This tutorial explains how to analyze Cloudflare metrics using the Cloudflare Integration tile for Datadog","url":"https://developers.cloudflare.com/analytics/analytics-integrations/datadog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-integrations/datadog/
  schema: 1
---
<p>This tutorial explains how to analyze Cloudflare metrics using the <a href="https://docs.datadoghq.com/integrations/cloudflare/">Cloudflare Integration tile for Datadog</a>.</p>
<h2 id="overview">Overview</h2>
<p>Before viewing the Cloudflare dashboard in Datadog, note that this integration:</p>
<ul>
<li>Is available to all Cloudflare customer plans (Free, Pro, Business and Enterprise)</li>
<li>Is based on the Cloudflare Analytics API</li>
<li>Provides Cloudflare web traffic and DNS metrics only</li>
<li>Does not feature data coming from request logs stored in Cloudflare Logs</li>
</ul>
<h2 id="task-1-install-the-cloudflare-app">Task 1 - Install the Cloudflare App</h2>
<p>To install the Cloudflare App for Datadog:</p>
<ol>
<li>
<p>Log in to <strong>Datadog</strong>.</p>
</li>
<li>
<p>Click the <strong>Integrations</strong> tab.</p>
</li>
<li>
<p>In the <strong>search box</strong>, start typing <em>Cloudflare</em>. The app tile should appear below the search box.
<img src="/assets/upstream/images/fundamentals/datadog/screenshots/datadog-integrations.png" alt="Searching for Cloudflare App in the Datadog Integrations tab" /></p>
</li>
<li>
<p>Click the <strong>Cloudflare</strong> tile to begin the installation.</p>
</li>
<li>
<p>Next, click <strong>Configuration</strong> and then complete the following:</p>
<ul>
<li>
<p><strong>Account name</strong>: (Optional) This can be any value. It has not impact on the site data pulled from Cloudflare.</p>
</li>
<li>
<p><strong>Email</strong>: This value helps keep your account safe. We recommend creating a dedicated Cloudflare user for analytics with the <a href="/fundamentals/manage-members/roles/"><em>Analytics</em> role</a> (read-only). Note that the <em>Analytics</em> role is available to Enterprise customers only.</p>
</li>
<li>
<p><strong>API Key</strong>: Enter your Cloudflare Global API key. For details refer to <a href="/fundamentals/api/get-started/keys/">API Keys</a>.</p>
</li>
</ul>
</li>
<li>
<p>Click <strong>Install Integration</strong>.
<img src="/assets/upstream/images/fundamentals/datadog/screenshots/cloudflare-tile-datadog-fill-details.png" alt="Configuring and installing the Datadog integration" /></p>
</li>
</ol>
<p>The Cloudflare App for Datadog should be installed now and you can view the dashboard.</p>
<h2 id="task-2-view-the-dashboard">Task 2 - View the dashboard</h2>
<p>By default, the dashboard displays metrics for all sites in your Cloudflare account. Use the dashboard filters see metrics for a specific domain.</p>
<p>The dashboard displays the following metrics:</p>
<ul>
<li><strong>Threats</strong> (threats by type, threats by country)</li>
<li><strong>Requests</strong> (total requests, cached requests, uncached requests, top countries by request, requests by IP class, top content types)</li>
<li><strong>Bandwidth</strong> (total bandwidth, encrypted and unencrypted traffic cached bandwidth, uncached bandwidth)</li>
<li><strong>Caching</strong> (Cache hit rate, request caching rate over time)</li>
<li><strong>HTTP response status errors</strong></li>
<li><strong>Page views</strong></li>
<li><strong>Search Engine Bot Traffic</strong></li>
<li><strong>DNS</strong> (DNS queries, response time, top hostnames, queries by type, stale vs. uncached queries)</li>
</ul>
<p><img src="/assets/upstream/images/fundamentals/datadog/dashboards/cloudflare-dashboard-datadog.png" alt="Dashboard displaying metrics for a site on a Cloudflare account" /></p>
