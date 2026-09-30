---
cp9:
  canonical: https://developers.cloudflare.com/health-checks/get-started/
  description: Create and configure Health Checks to monitor your origin servers.
  full_title: Get started · Cloudflare Health Checks docs
  head_html: <title>Get started · Cloudflare Health Checks docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and configure Health Checks to monitor your origin servers."><link rel="canonical" href="https://developers.cloudflare.com/health-checks/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/health-checks/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Health Checks docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and configure Health Checks to monitor your origin servers."><meta property="og:url" content="https://developers.cloudflare.com/health-checks/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Health Checks"><meta name="algolia_product_filter" content="Health Checks"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Health Checks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/health-checks/get-started/#page","headline":"Get started \u00b7 Cloudflare Health Checks docs","description":"Create and configure Health Checks to monitor your origin servers.","url":"https://developers.cloudflare.com/health-checks/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /health-checks/get-started/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="smart-shield">Smart Shield</h3>
@markup("md", "content/.markup/bodies/996.md")
</aside>
<p>This guide will get you started with creating and managing configured Health Checks.</p>
<h2 id="create-a-health-check">Create a Health Check</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Health Checks</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create</strong> and fill out the form, paying special attention to:
<ul>
<li>The values for <strong>Interval</strong> and <strong>Check regions</strong>, because decreasing the <strong>Interval</strong> and increasing <strong>Check regions</strong> may increase the load on your origin server.</li>
<li><strong>Retries</strong>, which specify the number of retries to attempt in case of a timeout before marking the origin as unhealthy.</li>
<li><strong>Response body</strong>, which specifies a substring that must be present in the first 10 KB of the response body for the check to succeed.</li>
</ul>
</li>
<li>Select <strong>Save and Deploy</strong>.</li>
</ol>
<h2 id="manage-health-checks">Manage Health Checks</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Traffic</strong> &gt; <strong>Health Checks</strong>.</li>
<li>Navigate to your health check and select <strong>Edit</strong>.</li>
<li>Edit your Health Check.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/995.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/994.md")
</aside>
