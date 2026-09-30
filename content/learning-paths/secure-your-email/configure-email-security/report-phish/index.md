---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/
  description: Set up PhishNet for user phish reporting.
  full_title: Report phish · Cloudflare Learning Paths
  head_html: <title>Report phish · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Set up PhishNet for user phish reporting."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/index.md"><meta property="og:title" content="Report phish · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up PhishNet for user phish reporting."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/#page","headline":"Report phish \u00b7 Cloudflare Learning Paths","description":"Set up PhishNet for user phish reporting.","url":"https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-your-email/configure-email-security/report-phish/
  schema: 1
---
<p>Before deploying Email security to production, you will have to consider reporting any phishing attacks, evaluating which disposition to assign a specific message, and using different screen criteria to search through your inbox.</p>
<p>PhishNet is an add-in button that helps users to submit phish samples missed by Email security detection.</p>
<h3 id="phishnet-for-microsoft-365">PhishNet for Microsoft 365</h3>
<p>To set up PhishNet Microsoft 365:</p>
<ol>
<li>Log in to the Microsoft admin panel. Go to <strong>Microsoft 365 admin center</strong> &gt; <strong>Settings</strong> &gt; <strong>Integrated Apps</strong>.</li>
<li>Select <strong>Upload custom apps</strong>.</li>
<li>Choose <strong>Provide link to manifest file</strong> and paste the following URL:</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://phishnet-o365.area1cloudflare-webapps.workers.dev?clientId=ODcxNDA0MjMyNDM3NTA4NjQwNDk1Mzc3MDIxNzE0OTcxNTg0Njk5NDEyOTE2NDU5ODQyNjU5NzYzNjYyNDQ3NjEwMzIxODEyMDk1NQ&#10;</code></pre>
<ol start="4">
<li>Verify and complete the wizard.</li>
</ol>
<h3 id="phishnet-for-google-workspace">PhishNet for Google Workspace</h3>
<p>To set up PhishNet for Google Workspace:</p>
<ol>
<li>Log in to the Google Workspace Marketplace using an administrator account.</li>
<li>Select <strong>Admin install</strong> to install Cloudflare PhishNet.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/email-security/settings/phish-submissions/phishnet-google-workspace/#set-up-phishnet-for-google-workspace">Set up PhishNet for Google Workspace</a> for more information.</p>
