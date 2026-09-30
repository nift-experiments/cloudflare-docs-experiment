---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/set-additional-detections/
  description: Enable extra email threat detection rules.
  full_title: Set additional detections · Cloudflare Learning Paths
  head_html: <title>Set additional detections · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Enable extra email threat detection rules."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/set-additional-detections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/set-additional-detections/index.md"><meta property="og:title" content="Set additional detections · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable extra email threat detection rules."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/set-additional-detections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/set-additional-detections/#page","headline":"Set additional detections \u00b7 Cloudflare Learning Paths","description":"Enable extra email threat detection rules.","url":"https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/set-additional-detections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-your-email/configure-email-security/set-additional-detections/
  schema: 1
---
<p>Email security allows you to configure the following additional detections:</p>
<ul>
<li><a href="/cloudflare-one/email-security/settings/detection-settings/additional-detections/#configure-domain-age">Domain age</a></li>
<li><a href="/cloudflare-one/email-security/settings/detection-settings/additional-detections/#configure-blank-email-detection">Blank email detection</a></li>
<li><a href="/cloudflare-one/email-security/settings/detection-settings/additional-detections/#configure-ach-change-from-free-email-detection">Automated Clearing House (ACH)</a> change from free email detection.</li>
<li><a href="/cloudflare-one/email-security/settings/detection-settings/additional-detections/#configure-html-attachment-email-detection">HTML attachment email detection</a></li>
</ul>
<p>To configure additional detections:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>.</li>
<li>On the Settings page, go to <strong>Detection settings</strong> &gt; <strong>Additional detections</strong>, and select <strong>Edit</strong>.</li>
</ol>
<h2 id="configure-domain-age">Configure domain age</h2>
<p>The domain age is the time since the domain has been registered.</p>
<p>To configure a domain age:</p>
<ol>
<li>On the <strong>Edit additional detections</strong> page:
<ul>
<li>Select <strong>Malicious domain age</strong>: Controls the threshold for a malicious disposition. Maximum of 100 days.</li>
<li>Select <strong>Suspicious domain age</strong>: Controls the threshold for a suspicious disposition. Maximum of 100 days.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="configure-blank-email-detection">Configure blank email detection</h2>
<p>Blank email detection detects emails with blank bodies and assigns a default disposition. You can choose between <strong>Malicious</strong> and <strong>Suspicious</strong> as dispositions.</p>
<p>To enable blank email detection:</p>
<ol>
<li>On the <strong>Edit additional detections</strong> page, enable <strong>Blank email detection</strong>.</li>
<li>Choose between <strong>Malicious</strong> and <strong>Suspicious</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="configure-ach-change-from-free-email-detection">Configure ACH change from free email detection</h2>
<p><a href="https://en.wikipedia.org/wiki/Automated_clearing_house">Automated Clearing House (ACH)</a> is a banking term related to direct deposits. ACH change from free email detection detects payroll inquiries or change requests from free email domains and assigns a default disposition. You can choose between <strong>Malicious</strong> and <strong>Suspicious</strong> as dispositions.</p>
<p>To enable ACH change from free email detection:</p>
<ol>
<li>On the <strong>Edit additional detections</strong> page, enable <strong>ACH change from free email detection</strong>.</li>
<li>Choose between <strong>Malicious</strong> and <strong>Suspicious</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="configure-html-attachment-email-detection">Configure HTML Attachment Email Detection</h2>
<p>HTML attachment email detection detects HTM and HTML attachments in emails and assigns a default disposition.</p>
<p>To enable HTML attachment email detection:</p>
<ol>
<li>On the <strong>Edit additional detections</strong> page, enable <strong>HTML attachment email detection</strong>.</li>
<li>Choose between <strong>Malicious</strong> and <strong>Suspicious</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
