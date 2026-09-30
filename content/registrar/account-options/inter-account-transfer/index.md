---
cp9:
  canonical: https://developers.cloudflare.com/registrar/account-options/inter-account-transfer/
  description: Transfer domain registration between Cloudflare accounts.
  full_title: Move a Cloudflare Registrar domain registration between accounts · Cloudflare Registrar docs
  head_html: <title>Move a Cloudflare Registrar domain registration between accounts · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Transfer domain registration between Cloudflare accounts."><link rel="canonical" href="https://developers.cloudflare.com/registrar/account-options/inter-account-transfer/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/account-options/inter-account-transfer/index.md"><meta property="og:title" content="Move a Cloudflare Registrar domain registration between accounts · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Transfer domain registration between Cloudflare accounts."><meta property="og:url" content="https://developers.cloudflare.com/registrar/account-options/inter-account-transfer/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/account-options/inter-account-transfer/#page","headline":"Move a Cloudflare Registrar domain registration between accounts \u00b7 Cloudflare Registrar docs","description":"Transfer domain registration between Cloudflare accounts.","url":"https://developers.cloudflare.com/registrar/account-options/inter-account-transfer/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/account-options/inter-account-transfer/
  schema: 1
---
<p>Cloudflare supports the move (transfer) of domain registrations between Cloudflare accounts when the source and target account both confirm the move. The move will result in the loss of all configurations and settings for the domain in the source account.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/12760.md")
</aside>
<p>Before proceeding, please be aware of the following:</p>
<ul>
<li>WHOIS contact information will be moved as is.</li>
<li>No other configuration will be moved.</li>
<li>After successful move, the registration will be transfer-locked for 30 days.</li>
<li>The target account will become responsible for domain renewals going forward.</li>
</ul>
<h2 id="1-prepare-for-the-move"><ol>
<li>Prepare for the move</li>
</ol></h2>
<p>Before you request the move, you will need to do the following:</p>
<ul>
<li>Obtain the <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> of the new account.</li>
<li>Add the domain as a website to the new account and select a plan.</li>
<li><a href="/dns/dnssec/#disable-dnssec">Disable DNSSEC</a> for the domain and ensure it is set up and ready in the new dashboard account you intend to move it to.</li>
</ul>
<p>The following pre-conditions must be met before the domain can be moved:</p>
<ul>
<li>The domain must have been registered more than 10 days ago.</li>
<li>The domain must be added to the new account as a website and a plan must be selected.</li>
<li>The domain must not be administratively locked, such as being locked due to a dispute or court order.</li>
<li>The domain must not have any of the following registry statuses: <code>pendingDelete</code>, <code>redemptionPeriod</code>, or <code>pendingTransfer</code>.</li>
<li>The registrant email address must be verified.</li>
<li>A pending Change of Registrant request cannot be present. If there is a pending request, it should be completed before initiating the move request.</li>
<li>DNSSEC must be turned off. It can be re-enabled on the new zone once the move completes.</li>
<li>If the current zone is locked, the lock must be released.</li>
</ul>
<h2 id="2-submit-the-move-request"><ol start="2">
<li>Submit the move request</li>
</ol></h2>
<p>You can now submit the move request under the <strong>Configuration</strong> tab of the <strong>Manage Domain</strong> page. Begin the submission process by selecting the <strong>Start</strong> button and follow the instructions.</p>
<p><strong>Important</strong>: Review the pre-conditions described above. If those conditions have not been met, the domain move will not be completed.</p>
<p>Once the move request has been submitted, the gaining account will receive an email notifying them of the request and will provide instructions for how to approve the request.</p>
<p>The gaining account must log into their account and go to <strong>Manage Domains</strong> (under Domain Registration). A message will appear at the top of the page stating that there are domains requiring action to be taken.</p>
<p>Select <strong>View Actions</strong> to display the domains with a pending move along and choose to accept or reject the request. Action must be taken within five days of the request.</p>
<p>If no action is taken within the five days, the request will be automatically canceled.</p>
