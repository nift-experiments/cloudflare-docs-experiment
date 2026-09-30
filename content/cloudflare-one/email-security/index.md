---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/
  description: Overview of Email security in Email Security.
  full_title: Email security · Cloudflare One docs
  head_html: <title>Email security · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Overview of Email security in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/index.md"><meta property="og:title" content="Email security · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Overview of Email security in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/#page","headline":"Email security \u00b7 Cloudflare One docs","description":"Overview of Email security in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/4507.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4506.md")
</aside>
<div class="nb-description">
@markup("md", "content/.markup/bodies/4508.md")
</div>
<p>Cloudflare Email Security uses AI, threat intelligence, and security rules to analyze every incoming email, protecting your organization from phishing, malware, <a href="https://www.cloudflare.com/en-gb/learning/email-security/business-email-compromise-bec/">Business Email Compromise</a> (where attackers impersonate executives or authority figures to commit fraud), vendor email fraud, and spam.</p>
<p>It integrates with your existing email provider (such as Outlook or Gmail) and can be deployed via <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/">API</a>, <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/gmail-bcc-setup/">BCC</a>/<a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/m365-journaling/">Journaling</a>, or <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/">MX/Inline</a>.</p>
<p>When you complete the <a href="/cloudflare-one/email-security/setup/">setup process</a>, the Cloudflare dashboard will display the Email security overview page.</p>
<p>The Email security overview provides you with:</p>
<ul>
<li><strong>Quick actions</strong>, where you can:
<ul>
<li>View <a href="/cloudflare-one/email-security/submissions/">submissions</a></li>
<li>Manage detection settings: manage <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policies</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">blocked senders</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">trusted domains</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">impersonation registry</a> and <a href="/cloudflare-one/email-security/settings/detection-settings/additional-detections/">additional detections</a>.</li>
<li><a href="/cloudflare-one/email-security/investigation/search-email/#screen-criteria">Run screens</a>: Search, filter, reclassify, and bulk-move emails</li>
</ul>
</li>
<li><strong>Recommendations</strong>: Suggested next steps to improve your configuration. For example, submitting misclassified emails for reclassification, creating policies, or protecting users at risk of <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">impersonation</a>.</li>
<li><strong>Email security metrics</strong>: Activity from the last seven days.</li>
<li><strong>Recently modified policies</strong>: A list of recently changed policies.</li>
<li><strong>Education and resources</strong>: Links to <a href="/cloudflare-one/implementation-guides/">implementation guides</a>, <a href="/cloudflare-one/changelog/email-security/">Email security changelogs</a>, and <a href="https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/methods/get/">API documentation</a></li>
</ul>
<p>To access the Email security overview:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Go to <strong>Email security</strong> &gt; <strong>Overview</strong>.</li>
</ol>
<hr />
<h2 id="troubleshooting">Troubleshooting</h2>
<p>For help resolving common issues with Email Security, refer to <a href="/cloudflare-one/email-security/troubleshooting/">Troubleshoot Email Security</a>.</p>
