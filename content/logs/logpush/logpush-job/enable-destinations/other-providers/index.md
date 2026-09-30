---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/
  description: Learn about enable other providers in Cloudflare Logs.
  full_title: Enable Logpush to other providers · Cloudflare Logs docs
  head_html: <title>Enable Logpush to other providers · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about enable other providers in Cloudflare Logs."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/index.md"><meta property="og:title" content="Enable Logpush to other providers · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about enable other providers in Cloudflare Logs."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/#page","headline":"Enable Logpush to other providers \u00b7 Cloudflare Logs docs","description":"Learn about enable other providers in Cloudflare Logs.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/other-providers/
  schema: 1
---
<p>Cloudflare Logpush supports pushing logs to a limited set of services providers. However, you can configure Logpush via API.</p>
<h2 id="manage-via-the-cloudflare-dashboard">Manage via the Cloudflare dashboard</h2>
<p>Refer to <a href="/logs/logpush/logpush-job/enable-destinations/">Enable destinations</a> for the list of services you can configure to use with Logpush through the Cloudflare dashboard. Interested in a different service? Take this <a href="https://docs.google.com/forms/d/e/1FAIpQLScwOSabROywVajpMX2ZYCVl3saYs11cP4NIC8QR-wmOAnxOtA/viewform">survey</a>.</p>
<h2 id="manage-via-api">Manage via API</h2>
<p>The Cloudflare Logpush API allows you to configure and manage jobs via create, retrieve, update, and delete operations (CRUD).</p>
<p>With Logpush, you can create a job to upload logs of the metadata Cloudflare collects in batches as soon as possible to your cloud service provider. The default number of jobs that you can setup per dataset per domain is four, but you can setup more jobs depending on your plan and subscriptions.</p>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.
<br /></p>
<p>To get started:</p>
<ol>
<li>
<p>Set up a storage provider and grant Cloudflare access. Your storage provider may request your Cloudflare API credentials and other information including:</p>
<ul>
<li>Email address</li>
<li>Cloudflare API key</li>
<li>Zone ID</li>
<li>Destination access details for your cloud service provider</li>
</ul>
</li>
<li>
<p>Configure your Logpush job. For more information on how to configure a Logpush job, refer to <a href="/logs/logpush/logpush-job/api-configuration/">API configuration</a>.</p>
</li>
</ol>
