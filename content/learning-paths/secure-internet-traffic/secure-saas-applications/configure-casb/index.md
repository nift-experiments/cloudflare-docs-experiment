---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/secure-saas-applications/configure-casb/
  description: Detect SaaS misconfigurations with CASB scans.
  full_title: Scan SaaS applications with Cloudflare CASB · Cloudflare Learning Paths
  head_html: <title>Scan SaaS applications with Cloudflare CASB · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Detect SaaS misconfigurations with CASB scans."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/secure-saas-applications/configure-casb/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/secure-saas-applications/configure-casb/index.md"><meta property="og:title" content="Scan SaaS applications with Cloudflare CASB · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Detect SaaS misconfigurations with CASB scans."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/secure-saas-applications/configure-casb/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/secure-saas-applications/configure-casb/#page","headline":"Scan SaaS applications with Cloudflare CASB \u00b7 Cloudflare Learning Paths","description":"Detect SaaS misconfigurations with CASB scans.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/secure-saas-applications/configure-casb/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/secure-saas-applications/configure-casb/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10039.md")
</aside>
<div class="nb-glossary-definition"><p>Cloudflare CASB provides comprehensive visibility and control over SaaS apps to prevent data leaks and compliance violations. It helps detect insider threats, shadow IT, risky data sharing, and bad actors.</p></div>
<p>Cloudflare's API-implemented CASB addresses the final, common security concern for administrators of SaaS applications or security organizations: How can I get insights into the existing configurations of my SaaS tools and proactively address issues before there is an incident? CASB integrates with a number of leading SaaS applications and surfaces instant security insights related to misconfiguration and potential for data loss. CASB also powers <a href="/cloudflare-one/team-and-resources/users/risk-score/">risk score heuristics</a> organized by severity.</p>
<p>For more information on Cloudflare CASB, including available SaaS integrations, refer to <a href="/cloudflare-one/integrations/cloud-and-saas/">Scan SaaS applications</a>.</p>
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
@markup("md", "content/.markup/bodies/10038.md")
</aside>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find the integration you would like to delete and select <strong>Configure</strong>.</li>
<li>Select <strong>Disenroll</strong>.</li>
</ol>
<p>To resume scanning the integration for findings, you will need to <a href="#add-an-integration">add the integration</a> again.</p>
<h3 id="integrate-dlp-policies">Integrate DLP policies</h3>
<p>If you use both Cloudflare CASB and Cloudflare Data Loss Prevention (DLP), you can use DLP to discover if files stored in your SaaS application contain sensitive data. CASB integrations supported by DLP include:</p>
<ul>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/aws-s3/">Amazon Web Services (AWS) S3</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/box/">Box</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/dropbox/">Dropbox</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/gcp-cloud-storage">Google Cloud Platform (GCP) Cloud Storage</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-drive/">Google Drive</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/onedrive/">Microsoft OneDrive</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint/">Microsoft SharePoint</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/">Microsoft 365 Copilot</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/openai/">OpenAI</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/anthropic/">Anthropic</a></li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">Scan SaaS applications with DLP</a>.</p>
