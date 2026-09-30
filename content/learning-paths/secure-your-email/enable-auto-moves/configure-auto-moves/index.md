---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/configure-auto-moves/
  description: Automate moving suspicious emails to folders.
  full_title: Configure auto-moves · Cloudflare Learning Paths
  head_html: <title>Configure auto-moves · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Automate moving suspicious emails to folders."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/configure-auto-moves/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/configure-auto-moves/index.md"><meta property="og:title" content="Configure auto-moves · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Automate moving suspicious emails to folders."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/configure-auto-moves/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/configure-auto-moves/#page","headline":"Configure auto-moves \u00b7 Cloudflare Learning Paths","description":"Automate moving suspicious emails to folders.","url":"https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/configure-auto-moves/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-your-email/enable-auto-moves/configure-auto-moves/
  schema: 1
---
<p>To configure auto-move events:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>.</li>
<li>Select <strong>Moves</strong>.</li>
<li>Under <strong>Auto-moves</strong>, select <strong>Configure</strong>.</li>
<li>Assign actions based on malicious, spoof, suspicious, spam, and bulk dispositions. Select among:
<ul>
<li><strong>Soft delete - user recoverable</strong>: Moves the message to the user's <strong>Recoverable Items - Deleted</strong> folder. Messages can be recovered by the user.</li>
<li><strong>Hard delete - admin recoverable</strong>: Completely deletes messages from a user's inbox.</li>
<li><strong>Move to trash</strong>: Moves messages to the trash or deleted items email folder.</li>
<li><strong>Move to junk</strong>: Moves the message to the junk or spam folder.</li>
<li><strong>No action</strong>: Messages stay in the origin folder.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
