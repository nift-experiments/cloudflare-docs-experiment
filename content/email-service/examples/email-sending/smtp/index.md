---
cp9:
  canonical: https://developers.cloudflare.com/email-service/examples/email-sending/smtp/
  description: Send transactional emails through Cloudflare Email Service authenticated SMTP from curl, Node.js, Python, or PHP.
  full_title: Send email over SMTP · Cloudflare Email Service docs
  head_html: <title>Send email over SMTP · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Send transactional emails through Cloudflare Email Service authenticated SMTP from curl, Node.js, Python, or PHP."><link rel="canonical" href="https://developers.cloudflare.com/email-service/examples/email-sending/smtp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/examples/email-sending/smtp/index.md"><meta property="og:title" content="Send email over SMTP · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send transactional emails through Cloudflare Email Service authenticated SMTP from curl, Node.js, Python, or PHP."><meta property="og:url" content="https://developers.cloudflare.com/email-service/examples/email-sending/smtp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/examples/email-sending/smtp/#page","headline":"Send email over SMTP \u00b7 Cloudflare Email Service docs","description":"Send transactional emails through Cloudflare Email Service authenticated SMTP from curl, Node.js, Python, or PHP.","url":"https://developers.cloudflare.com/email-service/examples/email-sending/smtp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/examples/email-sending/smtp/
  schema: 1
---
<p class="article-summary">Send transactional emails over Cloudflare Email Service SMTP using curl, Nodemailer, Python smtplib, or PHPMailer.</p>
<p>Send transactional emails over Cloudflare Email Service <a href="/email-service/api/send-emails/smtp/">authenticated SMTP</a> (<code>smtp.mx.cloudflare.net:465</code>) from any SMTP-capable language or client.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A domain onboarded for <a href="/email-service/configuration/domains/">Email Sending</a>.</li>
<li>A <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with the <strong>Email Sending: Edit</strong> permission. Set it as <code>CF_API_TOKEN</code> in your environment. The token is used as the SMTP password; the username is the literal string <code>api_token</code>.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="smtp-language"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8670.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/api/send-emails/smtp/">SMTP reference</a> — connection details, authentication, response codes, and troubleshooting.</li>
<li><a href="/email-service/examples/email-sending/recipients/">Specify recipients</a> — multiple recipients, CC and BCC, and named addresses.</li>
<li><a href="/email-service/platform/limits/">Limits</a> — account, message, and session limits.</li>
</ul>
