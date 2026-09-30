---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/bcc-microsoft-exchange/
  description: Integrate Microsoft Exchange BCC setup with Email Security.
  full_title: Setup phishing risk assessment for Microsoft Exchange with Email Security · Cloudflare One docs
  head_html: <title>Setup phishing risk assessment for Microsoft Exchange with Email Security · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Microsoft Exchange BCC setup with Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/bcc-microsoft-exchange/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/bcc-microsoft-exchange/index.md"><meta property="og:title" content="Setup phishing risk assessment for Microsoft Exchange with Email Security · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Microsoft Exchange BCC setup with Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/bcc-microsoft-exchange/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/bcc-microsoft-exchange/#page","headline":"Setup phishing risk assessment for Microsoft Exchange with Email Security \u00b7 Cloudflare One docs","description":"Integrate Microsoft Exchange BCC setup with Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/bcc-microsoft-exchange/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/bcc-microsoft-exchange/
  schema: 1
---
<p>For customers using Microsoft Exchange, setting up Email security via BCC is quick and easy. You need to configure an inbound rule to send emails to Email security via BCC for processing and detection of potential <span class="nb-glossary-tooltip" title="phishing">phishing</span> attacks. The following email flow shows how this works:</p>
<p><img src="/assets/upstream/email-security/Microsoft_Exchange_365.png" alt="Email flow when setting up a phishing assessment risk for Microsoft Exchange with Email security." /></p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="auto-moves-for-microsoft-exchange-customers">Auto-moves for Microsoft Exchange customers</h3>
@markup("md", "content/.markup/bodies/4950.md")
</aside>
<h2 id="configure-inbound-rule">Configure Inbound Rule</h2>
<ol>
<li>Access Exchange's <strong>Management Console</strong>, and go to <strong>Organization Configuration</strong> &gt; <strong>Hub Transport</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/exchange/step1.png" alt="Access Hub transport" /></p>
<ol start="2">
<li>
<p>On the <strong>Actions</strong> pane, select <strong>New Transport Rule</strong>.</p>
</li>
<li>
<p>Give the transport rule a name and a description and select <strong>Next</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/exchange/step3.png" alt="Give transport rule a name and description" /></p>
<ol start="4">
<li>In the <strong>Condition</strong> configuration panel, select the option <strong>from users that are inside or outside the organization</strong> option. In the dropdown that opens, select <strong>Outside the organization</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/exchange/step4.png" alt="Select scope of transport rule" /></p>
<ol start="5">
<li>Still in the same <strong>Condition</strong> configuration panel, add a second condition to the transport rule. Select <strong>sent to users that are inside or outside the organization, or partners</strong>. Keep the default value of <strong>Inside the organization</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/exchange/step5.png" alt="Select where to send emails" /></p>
<ol start="6">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In the <strong>Action</strong> configuration panel, select <strong>Blind carbon copy (Bcc) the message to addresses</strong>. Edit the <strong>addresses</strong> variable to add the addresses you want to copy as BCC.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/exchange/step7.png" alt="Select BCC and edit email addresses" /></p>
<ol start="8">
<li>In <strong>Specify Recipient</strong>, select the <strong>down arrow</strong> next to the <strong>Add</strong> button &gt; <strong>External E-Mail Address</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/exchange/step8.png" alt="Select external e-mail address" /></p>
<ol start="9">
<li>Enter the BCC address provided by Email security. This address is specific to your account.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/exchange/step9.png" alt="Enter the BCC address provided by Email security" /></p>
<ol start="10">
<li>
<p>Select <strong>OK</strong> &gt; <strong>OK</strong> to return to the main configuration page of the transport rule.</p>
</li>
<li>
<p>At the main configuration page of the transport rule, select <strong>Next</strong> to continue to the Exception configuration panel.</p>
</li>
<li>
<p>You do not need to configure an exception rule. Select <strong>Next</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/exchange/step12.png" alt="You do not need to configure an exception rule" /></p>
<ol start="13">
<li>In <strong>Create Rule</strong>, select the <strong>New</strong> button.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/exchange/step13.png" alt="Select the new button" /></p>
<ol start="14">
<li>Select <strong>Finish</strong> to close the transport rule configuration panel. This will return you to the Exchange Management Console.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/exchange/step14.png" alt="Select finish" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4949.md")
</aside>
<h2 id="email-processing-and-reports">Email processing and reports</h2>
<p>In BCC mode, all emails are put through automated phishing detections by Email security. Emails that trigger phishing detections are logged for reporting via product portal, email and Slack. Emails that do not trigger any detections are deleted.</p>
<h2 id="next-steps">Next steps</h2>
<p><a href="/cloudflare-one/insights/logs/logpush/email-security-logs/">Enable logs</a> to send detection data to an endpoint of your choice.</p>
