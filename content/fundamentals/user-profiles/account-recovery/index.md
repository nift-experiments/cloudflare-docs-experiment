---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/user-profiles/account-recovery/
  description: Regain access to your Cloudflare account when you have lost your 2FA device and backup codes.
  full_title: Account recovery · Cloudflare Fundamentals docs
  head_html: <title>Account recovery · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Regain access to your Cloudflare account when you have lost your 2FA device and backup codes."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/user-profiles/account-recovery/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/user-profiles/account-recovery/index.md"><meta property="og:title" content="Account recovery · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Regain access to your Cloudflare account when you have lost your 2FA device and backup codes."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/user-profiles/account-recovery/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/user-profiles/account-recovery/#page","headline":"Account recovery \u00b7 Cloudflare Fundamentals docs","description":"Regain access to your Cloudflare account when you have lost your 2FA device and backup codes.","url":"https://developers.cloudflare.com/fundamentals/user-profiles/account-recovery/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/user-profiles/account-recovery/
  schema: 1
---
<p>If you do not have access to your 2FA account or backup codes and cannot currently generate a 2FA code, use a verified device that you have logged in from before to request a temporary access code.</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>On the <strong>Two-Factor Authentication</strong> page, select <strong>Try recovery</strong> on <strong>Lost all 2FA devices and backup codes?</strong>.</li>
<li>Select <strong>Begin recovery</strong>.</li>
<li>An access code will be sent to the email address associated with your Cloudflare account.</li>
<li>Enter the temporary access code into the Cloudflare Dashboard and select <strong>Verify email</strong>.</li>
<li>Select <strong>Verify device</strong>. This checks whether you are using a device that has previously logged into your account.</li>
</ol>
<p>If you see <strong>Device verified</strong>, you will receive an email within 3-5 days with instructions to regain access to your account. It is important to note this process cannot be expedited, so you will need to wait until that email arrives before you can proceed.</p>
<p>If you see <strong>Device verification failed</strong>, you may be able to try again considering the following:</p>
<ul>
<li>If you clear your cookies often or are logging in from a different IP address, you have wiped Cloudflare's memory of your device and will need to use a different device to verify.</li>
<li>Your browser may be set to clear cookies on exit or after browser or OS upgrades. This interferes with the device verification process.</li>
<li>You may be using anti-malware or other software that automatically clears your browser cookies and makes your device unregognizable by Cloudflare's Dashboard.</li>
</ul>
<p>If you are still unable to verify your device, follow the instructions to <em>Request manual verification</em> on the <strong>Device verification failed</strong> page.</p>
