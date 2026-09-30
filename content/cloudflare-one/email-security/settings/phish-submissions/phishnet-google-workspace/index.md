---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/phishnet-google-workspace/
  description: PhishNet for Google Workspace in Email Security.
  full_title: PhishNet for Google Workspace · Cloudflare One docs
  head_html: <title>PhishNet for Google Workspace · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="PhishNet for Google Workspace in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/phishnet-google-workspace/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/phishnet-google-workspace/index.md"><meta property="og:title" content="PhishNet for Google Workspace · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="PhishNet for Google Workspace in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/phishnet-google-workspace/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Google"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/phishnet-google-workspace/#page","headline":"PhishNet for Google Workspace \u00b7 Cloudflare One docs","description":"PhishNet for Google Workspace in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/phishnet-google-workspace/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Google"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/settings/phish-submissions/phishnet-google-workspace/
  schema: 1
---
<p>To set up PhishNet with Google Workspace you need admin access to your Google Workspace account.</p>
<h2 id="set-up-phishnet-for-google-workspace">Set up PhishNet for Google Workspace</h2>
<ol>
<li>Log in to <a href="https://workspace.google.com/marketplace/app/cloudflare_phishnet/11369379045">Google Workspace Marketplace apps</a> using this direct link and an administrator account.</li>
<li>Select <strong>Admin install</strong> to install Cloudflare PhishNet. Read the warning, and select <strong>Continue</strong>.</li>
<li>You will be redirected to the <strong>Allow data access</strong> page, where you can choose to install Cloudflare PhishNet for <strong>Everyone at your organization</strong>, or <strong>Certain groups or organizational units</strong>. If you choose the latter option, you will have to select the users in the next step.</li>
<li>After choosing the groups you want to install PhishNet for, agree with Google's terms of service, and select <strong>Finish</strong>.</li>
<li>Cloudflare PhishNet has been installed. Select <strong>DONE</strong>.</li>
</ol>
<p>You have now successfully installed Cloudflare PhishNet.</p>
<h2 id="submit-phish-with-phishnet">Submit phish with PhishNet</h2>
<ol>
<li>In your Gmail web client, open the message you would like to flag as either spam or phish.</li>
<li>Select the PhishNet logo on the side panel.</li>
<li>Under <strong>Select Submission Type</strong>, select <strong>Spam</strong> or <strong>Phish</strong>.</li>
<li>Select <strong>Submit Report</strong>.</li>
</ol>
