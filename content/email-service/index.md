---
cp9:
  canonical: https://developers.cloudflare.com/email-service/
  description: Send transactional emails and route incoming emails to Workers or email addresses with Cloudflare Email Service.
  full_title: Cloudflare Email Service · Cloudflare Email Service docs
  head_html: <title>Cloudflare Email Service · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Send transactional emails and route incoming emails to Workers or email addresses with Cloudflare Email Service."><link rel="canonical" href="https://developers.cloudflare.com/email-service/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/index.md"><meta property="og:title" content="Cloudflare Email Service · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send transactional emails and route incoming emails to Workers or email addresses with Cloudflare Email Service."><meta property="og:url" content="https://developers.cloudflare.com/email-service/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/email-service/#page","headline":"Cloudflare Email Service \u00b7 Cloudflare Email Service docs","description":"Send transactional emails and route incoming emails to Workers or email addresses with Cloudflare Email Service.","url":"https://developers.cloudflare.com/email-service/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/1024.md")
</div>
<p>Cloudflare Email Service provides powerful email capabilities:</p>
<ul>
<li><strong>Email Sending</strong> <span class="nb-badge">Beta</span> for outbound transactional emails</li>
</ul>
<div class="nb-plan">
<p>Available on Workers Paid plan</p>
</div>
- **Email Routing** for handling incoming emails with Workers or routing to email addresses
<div class="nb-plan">
<p>Available on Free and Paid plans</p>
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1023.md")
</aside>
<p>Together, these two features make it possible for you to send and receive emails from your applications. For example, you can use Email Service for:</p>
<ul>
<li>Transactional emails (welcome messages, password resets, order confirmations)</li>
<li>Authentication flows (magic links, email verification, two-factor authentication)</li>
<li>Notifications and alerts</li>
<li>Custom email addresses (support@, contact@, orders@)</li>
<li>Emails as a mode of interaction for agents, such as send an email to create an issue in ticket tracking</li>
</ul>
<p>Access Email Service directly from Cloudflare Workers using <a href="/email-service/api/send-emails/workers-api/">bindings</a>, from any platform using the <a href="/email-service/api/send-emails/rest-api/">REST API</a>, or over <a href="/email-service/api/send-emails/smtp/">authenticated SMTP</a>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1028.md")
</div></div>
<p>See the full <a href="/email-service/api/send-emails/">API reference</a> for the REST API, Workers binding, and SMTP.</p>
<p><a class="nb-link-button" href="/email-service/get-started/">Get started</a></p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1030.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1031.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1032.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1033.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1034.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1035.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1036.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1037.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/1043.md")
</div>
