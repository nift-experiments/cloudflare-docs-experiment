---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/
  description: Cloud and SaaS findings in Cloudflare One.
  full_title: Cloud and SaaS findings · Cloudflare One docs
  head_html: <title>Cloud and SaaS findings · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloud and SaaS findings in Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/index.md"><meta property="og:title" content="Cloud and SaaS findings · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloud and SaaS findings in Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/#page","headline":"Cloud and SaaS findings \u00b7 Cloudflare One docs","description":"Cloud and SaaS findings in Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Compliance"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/cloud-and-saas-findings/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/4530.md")
</aside>
<p>Cloudflare's <a href="https://www.cloudflare.com/learning/access-management/what-is-a-casb/">Cloud Access Security Broker</a> (CASB) connects to SaaS application and cloud environment APIs to scan for security issues that can occur after a user has successfully logged in. These include misconfigurations (such as overly permissive sharing settings), unauthorized user activity, <span class="nb-glossary-tooltip" title="shadow IT">shadow IT</span>, and other data security issues.</p>
<p>For a list of available findings, refer to <a href="/cloudflare-one/integrations/cloud-and-saas/">Cloud and SaaS integrations</a>. You can also send posture finding instances to external systems with <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">CASB webhooks</a>.</p>
<h2 id="manage-casb-integrations">Manage CASB integrations</h2>
<p>When you integrate a third-party SaaS application or cloud environment with Cloudflare CASB, you allow CASB to make API calls to its endpoint and read relevant data on your behalf. The CASB integration permissions are read-only and follow the least privileged model. In other words, only the minimum access required to perform a scan is granted.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before you can integrate a SaaS application or cloud environment with CASB, your account with that integration must meet certain requirements. Refer to the SaaS application or cloud environment's <a href="/cloudflare-one/integrations/cloud-and-saas/">integration guide</a> to learn more about the prerequisites and permissions.</p>
<h3 id="add-an-integration">Add an integration</h3>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Select <strong>Connect an integration</strong> or <strong>Add integration</strong>.</li>
<li>Browse the available integrations and select the application you would like to add.</li>
<li>Follow the step-by-step integration instructions in the UI.</li>
<li>To run your first scan, select <strong>Save integration</strong>.</li>
</ol>
<p>After the first scan, CASB will automatically scan your SaaS application or cloud environment on a frequent basis to keep up with any changes. Scan intervals will vary due to each application having their own set of requirements, but the frequency is typically between every 1 hour and every 24 hours.</p>
<p>Once CASB detects at least one finding, you can <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/">view and manage your findings</a>.</p>
<h3 id="pause-an-integration">Pause an integration</h3>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find the integration you would like to pause and select <strong>Configure</strong>.</li>
<li>To stop scanning the application, turn off <strong>Scan for findings</strong>.</li>
<li>Select <strong>Save integration</strong>.</li>
</ol>
<p>You can resume CASB scanning at any time by turning on <strong>Scan for findings</strong>.</p>
<h3 id="delete-an-integration">Delete an integration</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4529.md")
</aside>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find the integration you would like to delete and select <strong>Configure</strong>.</li>
<li>Select <strong>Disenroll</strong>.</li>
</ol>
<p>To resume scanning the integration for findings, you will need to <a href="#add-an-integration">add the integration</a> again.</p>
