---
cp9:
  canonical: https://developers.cloudflare.com/registrar/get-started/transfer-domain-to-cloudflare/
  description: Transfer a domain to Cloudflare Registrar from another registrar.
  full_title: Transfer your domain to Cloudflare · Cloudflare Registrar docs
  head_html: <title>Transfer your domain to Cloudflare · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Transfer a domain to Cloudflare Registrar from another registrar."><link rel="canonical" href="https://developers.cloudflare.com/registrar/get-started/transfer-domain-to-cloudflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/get-started/transfer-domain-to-cloudflare/index.md"><meta property="og:title" content="Transfer your domain to Cloudflare · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Transfer a domain to Cloudflare Registrar from another registrar."><meta property="og:url" content="https://developers.cloudflare.com/registrar/get-started/transfer-domain-to-cloudflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/get-started/transfer-domain-to-cloudflare/#page","headline":"Transfer your domain to Cloudflare \u00b7 Cloudflare Registrar docs","description":"Transfer a domain to Cloudflare Registrar from another registrar.","url":"https://developers.cloudflare.com/registrar/get-started/transfer-domain-to-cloudflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/get-started/transfer-domain-to-cloudflare/
  schema: 1
---
<p>Transferring a domain moves your registration from your current registrar to Cloudflare.</p>
<ul>
<li><strong>Active work:</strong> About 30 minutes.</li>
<li><strong>Total time:</strong> Up to 10 days, depending on your registrar.</li>
<li><strong>Cost:</strong> Cloudflare domains are at-cost with no markup fees. Most transfers include a one-year extension from your current expiration date. Some country-code domains (such as <code>.uk</code>) have no transfer fee.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12745.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12744.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12743.md")
</aside>
<hr />
<details class="nb-details"><summary>Before you begin</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/12746.md")
</div></details>
<hr />
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/3c7f20b8e49ea737d6d013d2918c4520/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fpub-d9bf66e086fb4b639107aa52105b49dd.r2.dev%2FTransfer%2520your%2520domain%2520%2520to%2520Cloudflare_%2520%2520before%2520you%2520begin.png" title="Transfer your domain to Cloudflare: before you begin" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="1-add-your-domain-to-cloudflare"><ol>
<li>Add your domain to Cloudflare</li>
</ol></h2>
<p>Before you can transfer your registration, your domain must be <a href="/dns/zone-setups/full-setup/">active on Cloudflare</a>. This is what allows Cloudflare to protect your site with performance and security features during and after the transfer. You will not be able to enter an authorization code or proceed with the transfer until this step is complete.</p>
<h3 id="disable-dnssec">Disable DNSSEC</h3>
<p>If DNSSEC is enabled at your current registrar, disable it before you change nameservers. DNSSEC validates DNS responses using cryptographic signatures tied to your current provider. When you point nameservers to Cloudflare, those signatures will no longer match, which causes DNS resolution failures and can prevent your domain from becoming active.</p>
<p><strong>At your current registrar:</strong></p>
<ol>
<li>Check your domain settings for DNSSEC or DS records. If there are none, DNSSEC is not active and you can skip to <a href="#add-your-domain-and-update-your-nameservers">Add your domain</a>.</li>
<li>Remove or disable DNSSEC (sometimes labeled &quot;DS records&quot;).</li>
<li>Wait at least 24 hours for the change to propagate before changing nameservers.</li>
</ol>
<details class="nb-details"><summary>Provider-specific DNSSEC instructions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/12747.md")
</div></details>
<p>After your transfer completes, you can re-enable DNSSEC through Cloudflare with one click. Refer to <a href="/dns/dnssec/#1-activate-dnssec-in-cloudflare">Enable DNSSEC</a>.</p>
<h3 id="add-your-domain-and-update-your-nameservers">Add your domain and update your nameservers</h3>
<p>Follow the steps in <a href="/dns/zone-setups/full-setup/setup/">Set up Cloudflare DNS</a> to add your domain, review your DNS records, and get your assigned nameservers. Then <a href="/dns/nameservers/update-nameservers/">update the nameservers</a> at your current registrar to the ones Cloudflare assigned.</p>
<details class="nb-details"><summary>Nameserver instructions for popular registrars</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/12748.md")
</div></details>
<h3 id="wait-for-your-domain-to-become-active">Wait for your domain to become active</h3>
<p><strong>In the Cloudflare dashboard:</strong></p>
<p>Wait for your domain status to change from <strong>Pending</strong> to <strong>Active</strong>. This usually takes a few minutes but can take up to 24 hours.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12742.md")
</aside>
<p>If your zone has been pending for more than 24 hours, verify that you updated the nameservers correctly at your current registrar and that DNSSEC is disabled.</p>
<hr />
<h2 id="2-transfer-your-registration"><ol start="2">
<li>Transfer your registration</li>
</ol></h2>
<p>Once your domain is active on Cloudflare, you can transfer the registration. This moves your domain record from your current registrar to Cloudflare. You will go back and forth between your current registrar and Cloudflare during this process.</p>
<h3 id="unlock-your-domain">Unlock your domain</h3>
<p><strong>At your current registrar:</strong></p>
<p>Remove the lock on your domain so Cloudflare can process the transfer. Most registrars apply a lock by default (sometimes called registrar lock, domain lock, or transfer lock) to prevent unauthorized transfers. In WHOIS, this appears as <code>clientTransferProhibited</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12741.md")
</aside>
<h3 id="request-an-authorization-code">Request an authorization code</h3>
<p><strong>At your current registrar:</strong></p>
<p>Request an authorization code for your domain. This is also called an auth code, EPP code, authinfo code, or transfer code. Cloudflare uses this code to verify that the transfer is authorized by the domain owner.</p>
<p>Authorization codes are usually only valid for a limited period. Request the code when you are ready to enter it in the next step.</p>
<h3 id="enter-your-authorization-code-and-confirm-payment">Enter your authorization code and confirm payment</h3>
<p><strong>In the Cloudflare dashboard:</strong></p>
<div class="nb-dash-button"></div>
<p>Select your domain and enter the authorization code. For most generic TLDs (such as <code>.com</code>, <code>.net</code>, and <code>.org</code>), the transfer price includes a one-year registration extension from your current expiration date. This is an ICANN requirement for gTLD transfers. Country-code domains follow their own registry policies — for example, <code>.uk</code> transfers do not add an extra year or charge a transfer fee.</p>
<p>If you do not have a payment method on file, add one before proceeding.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12740.md")
</aside>
<p>For information about registration limits and the one-year extension, refer to <a href="/registrar/troubleshooting/#transfer-rejected-due-to-registration-limits">Transfer rejected due to registration limits</a>.</p>
<h3 id="confirm-your-contact-information">Confirm your contact information</h3>
<p><strong>In the Cloudflare dashboard:</strong></p>
<p>Enter the contact information for your registration. Cloudflare Registrar redacts this information from public WHOIS by default, but ICANN requires Cloudflare to collect accurate contact details. Providing inaccurate information may result in domain suspension.</p>
<p>You can <a href="/registrar/account-options/domain-contact-updates/">modify your contact information</a> later.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12739.md")
</aside>
<p>After entering the contact information, agree to the domain registration terms of service by selecting <strong>Confirm transfer</strong>.</p>
<h3 id="approve-the-transfer-at-your-current-registrar">Approve the transfer at your current registrar</h3>
<p>After you submit the transfer, Cloudflare will begin processing it and send a Form of Authorization (FOA) email to the registrant if the information is available in the public WHOIS database.</p>
<p>Your current registrar will email you confirming the transfer or asking for your approval. Afterwards, most registrars process it within 5 business days (but some TLDs, such as <code>.mx</code>, can take up to 10 business days).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12738.md")
</aside>
<hr />
<h2 id="transfer-from-shopify-block-or-wix">Transfer from Shopify, Block, or Wix</h2>
<p>Some commerce and site-building platforms (such as Shopify, Block, and Wix) act as both your hosting provider and domain registrar. These platforms typically do not allow you to change nameservers while the domain is registered with them. Because Cloudflare requires your nameservers to point to Cloudflare before a transfer can begin, a direct transfer is not possible.</p>
<p>The workaround is to transfer your domain to another registrar first, wait 60 days, then transfer to Cloudflare:</p>
<ol>
<li><strong>Get your authorization code from your current platform.</strong> Each platform has a different process. Refer to your platform documentation for instructions on transferring your domain away.</li>
<li><strong>Transfer to another registrar</strong> that allows nameserver changes. Enter the authorization code there and complete the transfer. This usually takes 3-5 days.</li>
<li><strong>Update nameservers to Cloudflare.</strong> Once the domain is at the new registrar, update the nameservers to Cloudflare. You can use all Cloudflare features (CDN, DNS, security) immediately after this step.</li>
<li><strong>Transfer to Cloudflare Registrar after 60 days.</strong> ICANN requires a 60-day wait between transfers. After that period, initiate the transfer to Cloudflare from the <a href="#enter-your-authorization-code-and-confirm-payment">Transfer Domains</a> page.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12737.md")
</aside>
<hr />
<h2 id="transfer-statuses">Transfer statuses</h2>
<p>You can check the status of your transfer on the <strong>Transfer Domains</strong> page in the dashboard.</p>
<ul>
<li>
<p><strong>Transfer in progress</strong>: Cloudflare has submitted the request to your current registrar. If this status persists for more than 24 hours, verify that you have unlocked the domain at your current registrar.</p>
</li>
<li>
<p><strong>Pending approval</strong>: Your current registrar has received the transfer request and can take up to five days to release the domain. To speed this up, approve the transfer through the email or dashboard of your current registrar.</p>
</li>
<li>
<p><strong>Transfer rejected</strong>: The transfer was rejected by your current registrar. This can happen if you declined the transfer request, or if the registrar determined the domain is not eligible. Select <strong>Retry</strong> to start a new transfer request.</p>
</li>
</ul>
<hr />
<h2 id="bulk-domain-transfers">Bulk domain transfers</h2>
<p>The process for transferring domains in bulk is the same as transferring a single domain. Each domain is charged individually.</p>
<hr />
<h2 id="common-transfer-issues">Common transfer issues</h2>
<p>Here are suggestions for how to handle common transfer issues:</p>
<ul>
<li><a href="/registrar/troubleshooting/#domain-is-still-locked">Domain is still locked</a></li>
<li><a href="/registrar/troubleshooting/#authorization-code-is-invalid-or-expired">Authorization code is invalid or expired</a></li>
<li><a href="/registrar/troubleshooting/#cannot-find-where-to-enter-your-authorization-code">Cannot find where to enter your authorization code</a></li>
<li><a href="/registrar/troubleshooting/#transfer-rejected">Transfer rejected</a></li>
<li><a href="/registrar/troubleshooting/#transfer-is-taking-too-long">Transfer is taking too long</a></li>
<li><a href="/registrar/troubleshooting/#payment-failed-during-transfer">Payment failed during transfer</a></li>
</ul>
<p>For a full list of issues, refer to <a href="/registrar/troubleshooting/">Troubleshoot failed domain transfers</a>.</p>
<h2 id="next-steps">Next steps</h2>
<p>As mentioned in <a href="/dns/zone-setups/full-setup/setup/#2-review-your-dns-records">Review DNS records in Cloudflare</a>, when moving your domain to Cloudflare Registrar, you might need to configure your DNS records to correctly point traffic to your web host. Cloudflare automatically scans for common records and adds them to your account's DNS page, but the scan is not guaranteed to find all existing DNS records.</p>
<p>Refer to your web host's documentation to learn what type of records you need to configure and where they should point, to avoid downtime.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/12749.md")
</div></details>
<p>You may also want to <a href="/dns/dnssec/#1-activate-dnssec-in-cloudflare">enable DNSSEC</a>.</p>
