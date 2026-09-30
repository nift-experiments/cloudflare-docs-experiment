---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/user-profiles/change-password-or-email/
  description: Learn how to change your email address or password associated with your account.
  full_title: Email address and password · Cloudflare Fundamentals docs
  head_html: <title>Email address and password · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to change your email address or password associated with your account."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/user-profiles/change-password-or-email/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/user-profiles/change-password-or-email/index.md"><meta property="og:title" content="Email address and password · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to change your email address or password associated with your account."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/user-profiles/change-password-or-email/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/user-profiles/change-password-or-email/#page","headline":"Email address and password \u00b7 Cloudflare Fundamentals docs","description":"Learn how to change your email address or password associated with your account.","url":"https://developers.cloudflare.com/fundamentals/user-profiles/change-password-or-email/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/user-profiles/change-password-or-email/
  schema: 1
---
<h2 id="change-email-address">Change email address</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8746.md")
</aside>
<p>To change the email address associated with your Cloudflare account:</p>
<ol>
<li>Go to your <a href="https://dash.cloudflare.com/?to=/:account/profile">Profile</a>.</li>
<li>Select your account.</li>
<li>In the Email Address panel, select <strong>Change Email Address</strong>.</li>
<li>In the dialog, enter your new email address in <strong>New email</strong> and <strong>Confirm email</strong>.</li>
<li>Enter your current password.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="billing-and-notification-email-addresses-must-be-updated-separately">Billing and notification email addresses must be updated separately</h3>
@markup("md", "content/.markup/bodies/8745.md")
</aside>
<h2 id="change-password">Change password</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8744.md")
</aside>
<p>To change your Cloudflare password:</p>
<ol>
<li>Go to your <a href="https://dash.cloudflare.com/?to=/:account/profile">Profile</a>.</li>
<li>Select your account.</li>
<li>Select <strong>Authentication</strong>.</li>
<li>On <strong>Password</strong>, select <strong>Change Password</strong>.</li>
<li>Change your password and select <strong>Save</strong>.</li>
</ol>
<p>For added account security, consider changing your <a href="/fundamentals/api/how-to/roll-token/">API tokens</a> as well.</p>
<h2 id="forgot-your-email-address">Forgot your email address</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8743.md")
</aside>
<p>If you forget the email address associated with your application:</p>
<ol>
<li>Go to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a> and select <strong>Forgot your email?</strong>.</li>
<li>Enter your domain name.</li>
<li>Cloudflare will send an email to the email address associated with your domain name. If you do not receive an email within 20 minutes, check your spam folder. The message will be sent from <code>no-reply@cloudflare.com</code> or <code>noreply@notify.cloudflare.com</code>.</li>
</ol>
<h2 id="forgot-your-password">Forgot your password</h2>
<p>You must be logged out of the Cloudflare dashboard to view the <strong>Forgot your password?</strong> option.</p>
<p>If you forget the password associated with your email address:</p>
<ol>
<li>Go to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a> and select <strong>Forgot your password?</strong>.</li>
<li>Enter your email address.</li>
<li>Cloudflare will send an email with instructions to reset your password. If you do not receive an email within 20 minutes, check your spam folder. The message will be sent from <code>no-reply@cloudflare.com</code> or <code>noreply@notify.cloudflare.com</code>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8742.md")
</aside>
<p>If you still cannot access the email address associated with your Cloudflare account, you may need to <a href="/fundamentals/manage-domains/move-domain/">move your domain to another account</a>.</p>
<p>Cloudflare requires these steps to prevent account hijacking.</p>
