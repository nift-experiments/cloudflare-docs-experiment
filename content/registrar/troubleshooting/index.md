---
cp9:
  canonical: https://developers.cloudflare.com/registrar/troubleshooting/
  description: Fix common domain transfer issues.
  full_title: Troubleshoot failed domain transfers · Cloudflare Registrar docs
  head_html: <title>Troubleshoot failed domain transfers · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Fix common domain transfer issues."><link rel="canonical" href="https://developers.cloudflare.com/registrar/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/troubleshooting/index.md"><meta property="og:title" content="Troubleshoot failed domain transfers · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fix common domain transfer issues."><meta property="og:url" content="https://developers.cloudflare.com/registrar/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/troubleshooting/#page","headline":"Troubleshoot failed domain transfers \u00b7 Cloudflare Registrar docs","description":"Fix common domain transfer issues.","url":"https://developers.cloudflare.com/registrar/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/troubleshooting/
  schema: 1
---
<p>After you start the transfer process to Cloudflare Registrar, your previous registrar has five days to release the domain after a successful transfer request. If your transfer has not been completed within that time frame, something has likely gone wrong.</p>
<p>Most issues with a stalled transfer can be solved by checking the following details and <a href="#restart-your-transfer">restarting the transfer</a>.</p>
<h2 id="domain-is-still-locked">Domain is still locked</h2>
<p>If <code>clientTransferProhibited</code> appears in your domain WHOIS or RDAP output, the domain is still locked. Unlock it at your current registrar. If you reapplied the registrar lock after requesting the transfer, you will need to remove it again to restart the transfer process.</p>
<p>If you already unlocked the domain but WHOIS still shows it as locked, allow up to 5 hours for the change to propagate. Some registrars may take up to 24 hours. Some registrars have multiple lock types (domain lock, transfer lock, privacy lock) that must each be disabled separately. If your registrar dashboard shows unlocked but WHOIS disagrees, contact your current registrar directly.</p>
<h2 id="dnssec-is-still-active">DNSSEC is still active</h2>
<p>Active DNSSEC at your current registrar will block the transfer. Disable DNSSEC and wait for the DS record TTL to expire (usually 24 hours) before retrying. Refer to <a href="/registrar/get-started/transfer-domain-to-cloudflare/#disable-dnssec">Disable DNSSEC</a> for detailed steps.</p>
<h2 id="authorization-code-is-invalid-or-expired">Authorization code is invalid or expired</h2>
<p>Authorization codes are usually only valid for a limited period. If your code is rejected, request a fresh one from your current registrar. Check for trailing spaces or line breaks when copy-pasting the code.</p>
<h2 id="cannot-find-where-to-enter-your-authorization-code">Cannot find where to enter your authorization code</h2>
<p>Unlike some registrars, Cloudflare does not allow you to submit an authorization code upfront. Cloudflare requires your domain to be active on its network first so that your site benefits from Cloudflare performance and security features from the moment the transfer begins. You must first <a href="/fundamentals/manage-domains/add-site/">add your domain</a> to Cloudflare, <a href="/dns/nameservers/update-nameservers/">update your nameservers</a>, and wait for the zone to show <strong>Active</strong> status in the Cloudflare dashboard. Only then will the <a href="https://dash.cloudflare.com/?to=/:account/registrar/transfer">Transfer Domains</a> page allow you to enter your code.</p>
<p>If your zone is still <strong>Pending</strong>, verify that you updated nameservers correctly at your current registrar and wait up to 24 hours. If you already have an authorization code, keep in mind that most codes are only valid for a limited period. If your code expires while you wait for the zone to activate, request a new one from your current registrar before proceeding.</p>
<h2 id="transfer-rejected">Transfer rejected</h2>
<p>Your transfer has been rejected by your previous registrar. There are several reasons for this to happen:</p>
<ul>
<li>You actively rejected the transfer request in the email you received from your registrar or on your registrar interface.</li>
<li>Your registrar determined the domain is not eligible for transfer.</li>
<li>Some registrars allow customers to enable a setting to reject all transfer requests.</li>
<li>If you are transferring from GoDaddy, make sure Domain Privacy and Domain Protection are fully disabled. GoDaddy may reject the transfer if either is still active.</li>
<li>In some instances, registrars may reject the transfer if they suspect malicious behavior.</li>
</ul>
<p>You will need to restart the transfer and approve the request or contact your current registrar to resolve this issue.</p>
<h2 id="transfer-rejected-due-to-registration-limits">Transfer rejected due to registration limits</h2>
<p>Domain registries enforce maximum registration periods. Because every transfer adds one year to your registration, a transfer can be rejected if the extra year would exceed the limit.</p>
<p><strong>Maximum registration periods:</strong></p>
<ul>
<li>Most TLDs (such as <code>.com</code>, <code>.net</code>, <code>.org</code>) allow up to <strong>10 years</strong> of registration.</li>
<li><code>.co</code> domains have a maximum of <strong>5 years</strong>.</li>
</ul>
<p><strong>Common reasons for rejection:</strong></p>
<ul>
<li>Your domain already has 9 or more years of registration remaining. Adding one year would exceed the 10-year limit (or 5-year limit for <code>.co</code>).</li>
<li>Your domain was renewed after expiring and then transferred within 45 days of the original expiration date. In this case, the registry may not add the extra year. For example, if <code>example.com</code> expires on December 10, you renew it on December 20 (extending it to December 20 of the following year), and then transfer to Cloudflare on December 30 — the transfer is within 45 days of the original expiration, so the registry may not add an additional year. Your expiration date would remain December 20 of the following year, meaning you effectively paid twice for the same year. If this happens, you are entitled to request a refund from your previous registrar under ICANN rules.</li>
<li>Your domain does not meet a TLD-specific minimum. For example, <code>.ai</code> domains require a minimum 2-year registration for transfers.</li>
<li><code>.uk</code> domains do not receive an additional year when transferred.</li>
</ul>
<p><strong>What you can do:</strong></p>
<ul>
<li>If your domain has too many years remaining, wait until the total registration period (current time remaining plus the one year added by the transfer) would not exceed the maximum — 10 years for most TLDs, or 5 years for <code>.co</code>. For example, a <code>.com</code> domain with 9 years and 6 months remaining cannot be transferred until at least 6 months have passed.</li>
<li>If your domain is close to expiration, renew it at your current registrar first. Once the renewal is confirmed, initiate the transfer.</li>
<li>If your domain is a TLD with special requirements (such as <code>.ai</code>), verify that you meet the minimum registration period before transferring.</li>
</ul>
<h2 id="domain-was-recently-registered-or-transferred">Domain was recently registered or transferred</h2>
<p>ICANN rules prohibit transfers within 60 days of registration or a previous transfer. Check the domain creation date and last transfer date in WHOIS.</p>
<h2 id="domain-is-in-a-restricted-status">Domain is in a restricted status</h2>
<p>Domains with certain WHOIS statuses cannot be transferred:</p>
<ul>
<li><code>clientHold</code> or <code>serverHold</code> — the domain is suspended, usually due to non-payment, failed verification, or a dispute. Contact your current registrar to find out why the hold was applied and how to remove it.</li>
<li><code>redemptionPeriod</code> — the domain has expired and passed the grace period. You must restore and renew it at your current registrar before it can be transferred.</li>
<li><code>pendingDelete</code> — the domain is scheduled for deletion by the registry and cannot be transferred or recovered. After deletion, the domain becomes available for anyone to register.</li>
</ul>
<p>Other common WHOIS or RDAP statuses include:</p>
<ul>
<li><code>clientTransferProhibited</code> — the domain is locked at the registrar.</li>
<li><code>serverTransferProhibited</code> — the registry has applied a transfer restriction.</li>
<li><code>addPeriod</code> — the domain is within the post-registration lock window.</li>
<li><code>pendingTransfer</code> — the domain is already in an active transfer.</li>
<li><code>clientDeleteProhibited</code> or <code>serverDeleteProhibited</code> — deletion is restricted.</li>
</ul>
<h2 id="whois-privacy-is-blocking-the-transfer">WHOIS privacy is blocking the transfer</h2>
<p>Most domains can be transferred with WHOIS privacy enabled. However, some registrars may prohibit transfer requests if you have WHOIS privacy services enabled. If your transfer is failing, check with your current registrar to confirm WHOIS privacy is not blocking it.</p>
<h2 id="payment-failed-during-transfer">Payment failed during transfer</h2>
<p>If your payment method was declined after submitting the authorization code, the transfer may be in a partially started state. Update your payment method in your Cloudflare billing settings and check the <a href="https://dash.cloudflare.com/?to=/:account/registrar/transfer">Transfer Domains</a> page for the current status.</p>
<h2 id="transfer-is-taking-too-long">Transfer is taking too long</h2>
<p>Domain transfers typically take 3-5 business days. Some TLDs (such as <code>.mx</code>) can take up to 10 days. You can speed up the process by approving the transfer at your current registrar when you receive the confirmation email. If the transfer has been stuck beyond these timeframes with no identifiable issue, contact your current registrar to confirm there are no holds or restrictions on their end.</p>
<h2 id="domain-not-available-for-transfer">Domain not available for transfer</h2>
<p>Your domain may not appear on the <a href="https://dash.cloudflare.com/?to=/:account/registrar/transfer">Transfer Domains</a> page if:</p>
<ul>
<li>You have not <a href="/fundamentals/manage-domains/add-site/">added your domain</a> to your Cloudflare account, or it is still in <strong>Pending</strong> status. Your domain must be <strong>Active</strong> before you can transfer it.</li>
<li>The domain was registered or previously transferred in the last 60 days (ICANN requirement).</li>
<li>Cloudflare does not support the TLD.</li>
<li>The domain has a status that blocks transfers (such as <code>serverHold</code> or <code>pendingDelete</code>). Refer to <a href="#domain-is-in-a-restricted-status">Domain is in a restricted status</a> for details.</li>
</ul>
<h2 id="cannot-update-nameservers-at-your-current-registrar">Cannot update nameservers at your current registrar</h2>
<p>Some commerce and site-building platforms (such as Shopify, Block, and Wix) do not allow you to change nameservers while the domain is registered with them. Because Cloudflare requires your nameservers to point to Cloudflare before a transfer can begin, a direct transfer from these platforms is not possible. For the recommended workaround, refer to <a href="/registrar/get-started/transfer-domain-to-cloudflare/#transfer-from-shopify-block-or-wix">Transfer from Shopify, Block, or Wix</a>.</p>
<h2 id="email-verification-required">Email verification required</h2>
<p>Cloudflare may send a verification email to your registrant contact email address when you register or transfer a domain, or when you update your registrant email. Per ICANN requirements, if the registrant email is not verified within 15 days, a hold is placed on the domain and nameservers are replaced with a parking server until verification is complete. After successful verification, nameservers are automatically restored.</p>
<p>Verification is triggered when your registrant contact email differs from your verified Cloudflare account email.</p>
<p>Some TLDs — including <code>.mx</code>, <code>.nz</code>, and <code>.ca</code> — may send verification through a third-party service. In these cases, the verification email will come from <code>noreply@emailverification.info</code> rather than Cloudflare. Check your spam folder if you do not receive it.</p>
<p>For these TLDs, if verification is not completed in time, the registry may temporarily replace your nameservers with <code>ns1.emailverification.info</code> and related hostnames until the registrant email is verified.</p>
<h2 id="uk-transfer-uses-an-ips-tag-not-an-auth-code"><code>.uk</code> transfer uses an IPS tag, not an auth code</h2>
<p><code>.uk</code>, <code>.co.uk</code>, and <code>.org.uk</code> domains do not use the standard auth-code transfer flow.</p>
<p>Instead, the losing registrar changes the domain's IPS tag to the gaining registrar. If you are transferring a <code>.uk</code> family domain to Cloudflare and cannot find an auth-code field, this behavior is expected.</p>
<p>If the transfer does not proceed, contact the current registrar and confirm that they have updated the IPS tag correctly.</p>
<h2 id="restart-your-transfer">Restart your transfer</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/444.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Manage Domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the correct domain and select <strong>Manage</strong>.</li>
<li>Select <strong>Cancel Transfer and Retry</strong>. After you initiate the retry, you must re-enter your auth code and confirm your WHOIS information.</li>
</ol>
