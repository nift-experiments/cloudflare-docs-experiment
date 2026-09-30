---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/analytics/access/
  description: Reference information for Access event analytics in Zero Trust analytics.
  full_title: Access event analytics · Cloudflare One docs
  head_html: <title>Access event analytics · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Access event analytics in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics/access/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics/access/index.md"><meta property="og:title" content="Access event analytics · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Access event analytics in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/analytics/access/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Authentication"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/analytics/access/#page","headline":"Access event analytics \u00b7 Cloudflare One docs","description":"Reference information for Access event analytics in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/analytics/access/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Authentication"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/analytics/access/
  schema: 1
---
<p>Access event analytics allows you to review login attempts to the applications you protect behind <a href="/cloudflare-one/access-controls/policies/">Access</a>. Access event analytics are powered by <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access authentication logs</a>.</p>
<p>To view Access event analytics:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong>.</li>
<li>Go to <strong>Dashboards</strong>.</li>
<li>Select <strong>Access event analytics</strong>.</li>
</ol>
<p>Access Event Analytics aggregates authentication activity based on your <a href="/cloudflare-one/access-controls/policies/policy-management/">Access policies</a>.</p>
<p>The <a href="/cloudflare-one/insights/analytics/application-access/">Application Access Report</a> dashboard offers a summary of overall Access activity, while <a href="/cloudflare-one/insights/analytics/access/">Access event analytics</a> dashboard provides a view of login events. You can export the Application Access Report to a PDF to share with stakeholders.</p>
<p>Refer to <a href="/cloudflare-one/insights/">Insights overview</a> to learn how to use Analytics dashboards together with <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> and <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for complete visibility and troubleshooting.</p>
<h2 id="available-insights">Available insights</h2>
<p>The Access event analytics dashboard includes a time-series chart of authentication events, allowing you to identify spikes in login activity over a selected period.</p>
<ul>
<li>Events are displayed on the vertical axis.</li>
<li>Time (in your local timezone) is shown along the horizontal axis.</li>
</ul>
<p>The Access event analytics dashboard also shows data on your usage patterns with metrics including:</p>
<ul>
<li>Top used applications</li>
<li>Top users</li>
<li>Top IP addresses</li>
<li>Top identities</li>
<li>Top countries</li>
<li>Top application types</li>
</ul>
<p>These insights help you detect anomalies, and optimize policy rules.</p>
