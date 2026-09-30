---
cp9:
  canonical: https://developers.cloudflare.com/registrar/account-options/domain-contact-updates/
  description: Update domain registrant contact information.
  full_title: Registrant contact updates · Cloudflare Registrar docs
  head_html: <title>Registrant contact updates · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Update domain registrant contact information."><link rel="canonical" href="https://developers.cloudflare.com/registrar/account-options/domain-contact-updates/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/account-options/domain-contact-updates/index.md"><meta property="og:title" content="Registrant contact updates · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Update domain registrant contact information."><meta property="og:url" content="https://developers.cloudflare.com/registrar/account-options/domain-contact-updates/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/account-options/domain-contact-updates/#page","headline":"Registrant contact updates \u00b7 Cloudflare Registrar docs","description":"Update domain registrant contact information.","url":"https://developers.cloudflare.com/registrar/account-options/domain-contact-updates/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/account-options/domain-contact-updates/
  schema: 1
---
<p>It is important that you keep your contact details accurate and up-to-date. <a href="https://www.icann.org/resources/pages/registrant-contact-information-wdrp-2017-08-31-en">ICANN rules state</a> that if you do not have updated contact information, your domain name registration may be suspended or even cancelled.</p>
<p>The contact information you can update includes:</p>
<ul>
<li>First name</li>
<li>Last name</li>
<li>Email</li>
<li>Organization</li>
<li>Phone</li>
<li>Address including City, State/Province, Postal code &amp; Country</li>
</ul>
<p>To update your registrant contacts:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Manage domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find <strong>Default contact</strong> and select <strong>Edit</strong>.</li>
<li>Update the relevant information, and select <strong>Save</strong>.</li>
<li>Find the domain where you want to update your contact information, and select <strong>Manage</strong>.</li>
<li>Select the <strong>Contacts</strong> tab, and edit the contact information.</li>
</ol>
<p>If you change any of the following fields, Cloudflare Registrar will require a Change of Registrant approval before the changes are finalized:</p>
<ul>
<li>First name</li>
<li>Last name</li>
<li>Organization</li>
<li>Email address</li>
</ul>
<p>If you update any of the fields mentioned above, Cloudflare Registrar will send an approval email to the current registrant's email address. The approval email contains a link to a web page where the requested change may be viewed and approved or rejected. If the pending change is not approved or rejected within seven days, the request will automatically be canceled.</p>
<p>If you do not update these fields, your contact information is updated immediately and no further action is required.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/12765.md")
</aside>
<h2 id="changing-email-contact">Changing email contact</h2>
<p>If the registrant contact update also includes a change to the email address, Cloudflare sends a second approval email to the new (requested) email address. Both the old (original) email address and the new one have to approve the change for the change to be successfully completed.</p>
<p>Only the current registrant may opt out of the transfer lock, however. The approval page for the new registrant will not include the option to opt out.</p>
<h2 id="60-day-transfer-lock">60-day transfer lock</h2>
<p>After the changes for the registrant contact are approved, the domain will be placed on a transfer lock for 60 days. This happens when you approve changes to the registrant contacts without checking the box to prevent the transfer lock.</p>
<p>This transfer lock prevents the transfer of the domain to another registrar, and the transfer to another Cloudflare account. It does not prevent additional updates to the domain name.</p>
<p>If the registrant contact is updated again while the domain is in the 60-day lock period, the lock expiration will be further extended to 60 days from the most recent update.</p>
