---
cp9:
  canonical: https://developers.cloudflare.com/health-checks/how-to/health-checks-notifications/
  description: Set up notifications for Health Checks status changes.
  full_title: Health Checks notifications · Cloudflare Health Checks docs
  head_html: <title>Health Checks notifications · Cloudflare Health Checks docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up notifications for Health Checks status changes."><link rel="canonical" href="https://developers.cloudflare.com/health-checks/how-to/health-checks-notifications/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/health-checks/how-to/health-checks-notifications/index.md"><meta property="og:title" content="Health Checks notifications · Cloudflare Health Checks docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up notifications for Health Checks status changes."><meta property="og:url" content="https://developers.cloudflare.com/health-checks/how-to/health-checks-notifications/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Health Checks"><meta name="algolia_product_filter" content="Health Checks"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Health Checks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/health-checks/how-to/health-checks-notifications/#page","headline":"Health Checks notifications \u00b7 Cloudflare Health Checks docs","description":"Set up notifications for Health Checks status changes.","url":"https://developers.cloudflare.com/health-checks/how-to/health-checks-notifications/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /health-checks/how-to/health-checks-notifications/
  schema: 1
---
<p>You can <a href="/health-checks/how-to/health-checks-notifications/#configure-notifications">configure notification emails</a> to be alerted when the Health Check detects that there is a change in the status of your origin server. Cloudflare will send you an email within seconds so you can take the necessary action before customers are impacted.</p>
<p>The email provides information to determine what caused the health status change. You can evaluate when the change happened, the status of the origin server, if and why it is unhealthy, the expected response code, and the received response code.</p>
<h2 id="configure-notifications">Configure notifications</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Health Checks</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Configure an alert</strong>.</li>
<li>Fill out the <strong>Notification name</strong> and <strong>Description</strong>.</li>
<li>Add a Notification email.</li>
<li>Select <strong>Next</strong>.</li>
<li>Add health checks to include in your alerts.</li>
<li>Choose the <strong>Notification trigger</strong>, which determines when you receive alerts.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9013.md")
</aside>
<p>See <a href="/health-checks/health-checks-analytics/#common-error-codes">common error codes</a> for more information regarding the cause of any changes to your Health Check.</p>
<p>Cloudflare encourages you to view your <a href="/health-checks/health-checks-analytics/#common-error-codes">Health Checks Analytics</a> to get more context about the health of your servers over time.</p>
