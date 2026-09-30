---
cp9:
  canonical: https://developers.cloudflare.com/smart-shield/configuration/health-checks/setup/
  description: Create, configure, and manage health checks for your origin servers.
  full_title: Manage Health Checks · Cloudflare Smart Shield docs
  head_html: <title>Manage Health Checks · Cloudflare Smart Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, configure, and manage health checks for your origin servers."><link rel="canonical" href="https://developers.cloudflare.com/smart-shield/configuration/health-checks/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/smart-shield/configuration/health-checks/setup/index.md"><meta property="og:title" content="Manage Health Checks · Cloudflare Smart Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, configure, and manage health checks for your origin servers."><meta property="og:url" content="https://developers.cloudflare.com/smart-shield/configuration/health-checks/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Smart Shield"><meta name="algolia_product_filter" content="Smart Shield"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Smart Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/smart-shield/configuration/health-checks/setup/#page","headline":"Manage Health Checks \u00b7 Cloudflare Smart Shield docs","description":"Create, configure, and manage health checks for your origin servers.","url":"https://developers.cloudflare.com/smart-shield/configuration/health-checks/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /smart-shield/configuration/health-checks/setup/
  schema: 1
---
<p>Refer to the section below to learn how to manage your Smart Shield health checks.</p>
<h2 id="create-and-edit-health-checks">Create and edit health checks</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Speed</strong> &gt; <strong>Smart Shield</strong>.</li>
<li>For Health Checks, select <strong>Manage</strong>.</li>
<li>Select <strong>Create</strong> or find an existing health check and select <strong>Edit</strong>.</li>
<li>Fill out the form or edit existing values, paying special attention to:
<ul>
<li>The values for <strong>Interval</strong> and <strong>Check regions</strong>, because decreasing the <strong>Interval</strong> and increasing <strong>Check regions</strong> may increase the load on your origin server.</li>
<li><strong>Retries</strong>, which specify the number of retries to attempt in case of a timeout before marking the origin as unhealthy.</li>
</ul>
</li>
<li>Select <strong>Save and Deploy</strong>.</li>
</ol>
<h2 id="configure-alerts">Configure alerts</h2>
<p>You can configure <a href="/notifications/get-started/">notification emails</a> to be alerted when the health check detects that there is a change in the status of your origin server. Cloudflare will send you an email within seconds so you can take the necessary action before customers are impacted.</p>
<p>The email provides information to determine what caused the health status change. You can evaluate when the change happened, the status of the origin server, if and why it is unhealthy, the expected response code, and the received response code. Refer to <a href="/smart-shield/configuration/health-checks/analytics/#common-error-codes">common error codes</a> for further guidance.</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Speed</strong> &gt; <strong>Smart Shield</strong>.</li>
<li>For Health Checks, select <strong>Manage</strong> and then <strong>Configure an alert</strong>.</li>
<li>Fill out the <strong>Notification name</strong> and <strong>Description</strong>.</li>
<li>Add a Notification email.</li>
<li>Select <strong>Next</strong>.</li>
<li>Add health checks to include in your alerts.</li>
<li>Choose the <strong>Notification trigger</strong>, which determines when you receive alerts.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
