---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/dex/notifications/
  description: Reference information for Notifications in Zero Trust analytics.
  full_title: DEX notifications · Cloudflare One docs
  head_html: <title>DEX notifications · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Notifications in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/notifications/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/notifications/index.md"><meta property="og:title" content="DEX notifications · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Notifications in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/dex/notifications/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/dex/notifications/#page","headline":"DEX notifications \u00b7 Cloudflare One docs","description":"Reference information for Notifications in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/dex/notifications/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/dex/notifications/
  schema: 1
---
<p>Administrators can receive alerts when Cloudflare detects connectivity issues with the Cloudflare One Client or degraded application performance. Notifications can be delivered via email, webhook, and third-party services.</p>
<h2 id="manage-notifications">Manage notifications</h2>
<p>DEX notifications are configured on the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>. For more information, refer to <a href="/notifications/get-started/#create-a-notification">Create a notification</a>.</p>
<h2 id="available-notifications">Available notifications</h2>
<details><summary>Device connectivity anomaly</summary><strong>Who is it for?</strong><p>Zero Trust customers who want to be notified when Cloudflare detects a spike or drop in the number of devices connected to the WARP client.</p>
<strong>Other options / filters</strong><ul>
<li><strong>Alert configuration</strong>: Choose when to trigger a notification. Available options are <em>Connectivity spike</em>, <em>Connectivity drop</em>, and <em>Connectivity spike or drop</em>.</li>
<li>Filters:
<ul>
<li><strong>Colo</strong>: Cloudflare data center that the device is connected to.</li>
<li><strong>Platform</strong>: Operating system of the device.</li>
<li><strong>Version</strong>: WARP client version (for example, <code>2024.3.409.0</code>).</li>
<li><strong>Mode</strong>: <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">WARP mode</a> deployed on the device.</li>
</ul>
</li>
</ul>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>Review your <a href="/cloudflare-one/insights/dex/fleet-status/">fleet status</a> to investigate why the spike or drop occurred and which devices are impacted.</p>
<strong>Additional information</strong><p>To learn more about the alert logic, refer to <a href="/cloudflare-one/insights/dex/notifications/#z-score">Z-score</a>.</p>
</details><details><summary>DEX test latency</summary><strong>Who is it for?</strong><p>Zero Trust customers who wish to receive alerts when there is a spike or drop in application latency, as measured by the HTTP test <a href="/cloudflare-one/insights/dex/tests/http/#test-results">Resource Fetch time</a> or Traceroute test <a href="/cloudflare-one/insights/dex/tests/traceroute/#test-results">Round trip time</a>. Requires setting up a <a href="/cloudflare-one/insights/dex/tests/">DEX test</a>.</p>
<strong>Other options / filters</strong><ul>
<li><strong>Alert configuration</strong>: Choose when to trigger a notification. Available options are <em>Latency spike</em>, <em>Latency drop</em>, and <em>Latency spike or drop</em>.</li>
<li>Filters:
<ul>
<li><strong>Colo</strong>: Cloudflare data center that the device is connected to.</li>
<li><strong>Platform</strong>: Operating system of the device.</li>
<li><strong>Version</strong>: WARP client version (for example, <code>2024.3.409.0</code>).</li>
<li><strong>Test name</strong>: Choose which DEX test the alert should monitor. You will receive individual notifications for each test.</li>
</ul>
</li>
</ul>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>View your <a href="/cloudflare-one/insights/dex/tests/view-results/">test results</a> to investigate why the spike occurred.</p>
<strong>Additional information</strong><p>To learn more about the alert logic, refer to <a href="/cloudflare-one/insights/dex/notifications/#z-score">Z-score</a>.</p>
</details><details><summary>DEX test low availability</summary><strong>Who is it for?</strong><p>Zero Trust customers who wish to receive alerts when the percentage of successful HTTP or traceroute requests to an application drops below the selected service-level objective (SLO). Requires setting up a <a href="/cloudflare-one/insights/dex/tests/">DEX test</a>.</p>
<strong>Other options / filters</strong><ul>
<li><strong>Service Level Objective (SLO)</strong>: Specify the availability threshold that will trigger an alert. Enter a percentage in <code>xx.x</code> format (for example, <code>98.0</code>).</li>
<li>Filters:
<ul>
<li><strong>Colo</strong>: Cloudflare data center that the device is connected to.</li>
<li><strong>Platform</strong>: Operating system of the device.</li>
<li><strong>Version</strong>: WARP client version (for example, <code>2024.3.409.0</code>).</li>
<li><strong>Test name</strong>: Choose which DEX test the alert should monitor. You will receive individual notifications for each test.</li>
</ul>
</li>
</ul>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>View your <a href="/cloudflare-one/insights/dex/tests/view-results/">test results</a> to investigate why the degradation occurred.</p>
<strong>Additional information</strong><p>To learn more about the alert logic, refer to <a href="/cloudflare-one/insights/dex/notifications/#slo">SLO</a>.</p>
</details>
<h2 id="alert-logic">Alert logic</h2>
<h3 id="z-score">Z-score</h3>
<p>Cloudflare uses a z-score to detect unusual traffic spikes or drops. A <a href="https://en.wikipedia.org/wiki/Standard_score">z-score</a> is the number of standard deviations the current value is from the mean. Cloudflare calculates the mean and standard deviation by comparing the current five minutes to the past four hours. This is measured every five minutes.</p>
<p>To trigger an alert, the z-score value must be above 3.5 or below -3.5, which indicates the current value is significantly different from the recent baseline.</p>
<h3 id="slo">SLO</h3>
<p>A service-level objective (SLO) measures the percentage of valid events that succeeded. It is defined as (good events / valid events) * 100, where valid events are those that could be measured in a given time period. DEX notifications evaluate both a short window (five minutes) and a long window (one hour) and trigger an alert if availability falls below the SLO threshold in either window.</p>
