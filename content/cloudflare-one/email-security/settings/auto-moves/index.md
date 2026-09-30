---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/settings/auto-moves/
  description: Auto-move events in Email Security.
  full_title: Auto-move events · Cloudflare One docs
  head_html: <title>Auto-move events · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Auto-move events in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/auto-moves/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/auto-moves/index.md"><meta property="og:title" content="Auto-move events · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Auto-move events in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/settings/auto-moves/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/auto-moves/#page","headline":"Auto-move events \u00b7 Cloudflare One docs","description":"Auto-move events in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/auto-moves/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/settings/auto-moves/
  schema: 1
---
<p>Auto-moves allow you to automatically move emails out of your inbox based on a <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">disposition</a> that Email security assigns to each message (for example, malicious, spam, or spoof).</p>
<p>Use auto-moves to enforce email security policy without relying on end users to identify and act on threats themselves. After you configure auto-moves, Email security handles flagged messages according to the action you choose for each disposition.</p>
<p>To configure auto-move events:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>.</li>
<li>Select <strong>Moves</strong>.</li>
<li>Under <strong>Auto-moves</strong>, select <strong>Configure</strong>.</li>
<li>For each disposition (malicious, spam, bulk, suspicious, spoof), choose what happens to matching emails:
<ul>
<li><strong>Soft delete - user recoverable</strong>: Moves the message to the user's <strong>Recoverable Items - Deleted</strong> folder. The user can still find and restore the message. This option is only available for Microsoft 365 customers. Refer to <a href="https://learn.microsoft.com/en-us/compliance/assurance/assurance-exchange-online-data-deletion">Microsoft 365 Exchange data deletion</a> for more information.</li>
<li><strong>Hard delete - admin recoverable</strong>: Removes the message from the user's inbox entirely. Only an administrator can recover it.</li>
<li><strong>Move to trash</strong>: Moves the message to the user's trash or deleted items folder. This option is only available for Google Workspace users.</li>
<li><strong>Move to junk</strong>: Moves the message to the user's junk or spam folder.</li>
<li><strong>No action</strong>: Leaves the message where it is. Email security still records the disposition, but does not move the message.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
