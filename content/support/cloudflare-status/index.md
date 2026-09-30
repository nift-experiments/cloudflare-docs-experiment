---
cp9:
  canonical: https://developers.cloudflare.com/support/cloudflare-status/
  description: Check Cloudflare service status and configure notifications.
  full_title: Cloudflare Status · Cloudflare Support docs
  head_html: <title>Cloudflare Status · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Check Cloudflare service status and configure notifications."><link rel="canonical" href="https://developers.cloudflare.com/support/cloudflare-status/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/cloudflare-status/index.md"><meta property="og:title" content="Cloudflare Status · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Check Cloudflare service status and configure notifications."><meta property="og:url" content="https://developers.cloudflare.com/support/cloudflare-status/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/cloudflare-status/#page","headline":"Cloudflare Status \u00b7 Cloudflare Support docs","description":"Check Cloudflare service status and configure notifications.","url":"https://developers.cloudflare.com/support/cloudflare-status/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/cloudflare-status/
  schema: 1
---
<p>Cloudflare provides updates on the status of our services and network on the <a href="https://www.cloudflarestatus.com/">Cloudflare Status page</a>, which you should check if you notice unexpected behavior with Cloudflare.</p>
<p>Beyond looking at the page itself, there are programmatic ways to consume this information.</p>
<h2 id="configure-notifications">Configure notifications</h2>
<p>There are two ways to be notified about Cloudflare incidents and maintenance.</p>
<h3 id="status-page-notifications">Status page notifications</h3>
<p>The status page has its own notification system, delivered independently of Cloudflare infrastructure, so these notifications fire even if Cloudflare itself is down. You can subscribe by email, webhook, Slack, Discord, or Google Chat.</p>
<p>For more information, refer to <a href="https://www.cloudflarestatus.com/docs/notifications">status page notifications</a>.</p>
<h3 id="cloudflare-notifications">Cloudflare Notifications</h3>
<p>Cloudflare offers a dedicated notification called <strong>Incident Alerts</strong>, which lets you know when Cloudflare is experiencing an incident. Because it runs on your account, it delivers to the destinations you have already configured and can be filtered to the impact levels and components you care about.</p>
<p>You can configure this notification to send via <a href="/notifications/get-started/">email</a>, <a href="/notifications/get-started/configure-webhooks/">Webhooks</a>, or <a href="/notifications/get-started/configure-pagerduty/">PagerDuty</a>.</p>
<p>A separate <strong>Maintenance Notification</strong> covers planned maintenance. For more information, refer to <a href="/support/disruptive-maintenance/">Disruptive Maintenance</a>.</p>
<h2 id="check-location-status">Check location status</h2>
<p>The <a href="https://www.cloudflarestatus.com/locations">locations view</a> lists the status of each Cloudflare data center as <strong>Operational</strong>, <strong>Re-routed</strong>, or <strong>Partially Re-routed</strong>. A location that has been removed from the network for planned or unplanned maintenance is listed as <strong>Re-routed</strong>.</p>
<h2 id="use-the-api">Use the API</h2>
<p>Cloudflare also provides status information through the <a href="https://www.cloudflarestatus.com/api">Cloudflare Status API</a>.</p>
<p>Incidents and maintenance are published as separate feeds, each available in RSS and Atom:</p>
<table>
<thead>
<tr>
<th>Feed</th>
<th>RSS</th>
<th>Atom</th>
</tr>
</thead>
<tbody>
<tr>
<td>Incidents</td>
<td><code>https://www.cloudflarestatus.com/api/v3/incidents.rss</code></td>
<td><code>https://www.cloudflarestatus.com/api/v3/incidents.atom</code></td>
</tr>
<tr>
<td>Maintenance</td>
<td><code>https://www.cloudflarestatus.com/api/v3/maintenance.rss</code></td>
<td><code>https://www.cloudflarestatus.com/api/v3/maintenance.atom</code></td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/fundamentals/new-features/available-rss-feeds/">Available RSS feeds</a> (for the <a href="/changelog/">Cloudflare changelog</a>)</li>
<li><a href="/fundamentals/api/reference/deprecations/">API deprecations</a></li>
<li><a href="/support/disruptive-maintenance/">Planned maintenance windows</a></li>
</ul>
