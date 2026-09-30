---
cp9:
  canonical: https://developers.cloudflare.com/email-service/configuration/send-bindings/
  description: Restrict which senders and recipients a Workers send_email binding can use with Email Service.
  full_title: Configure send bindings · Cloudflare Email Service docs
  head_html: <title>Configure send bindings · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Restrict which senders and recipients a Workers send_email binding can use with Email Service."><link rel="canonical" href="https://developers.cloudflare.com/email-service/configuration/send-bindings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/configuration/send-bindings/index.md"><meta property="og:title" content="Configure send bindings · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Restrict which senders and recipients a Workers send_email binding can use with Email Service."><meta property="og:url" content="https://developers.cloudflare.com/email-service/configuration/send-bindings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/configuration/send-bindings/#page","headline":"Configure send bindings \u00b7 Cloudflare Email Service docs","description":"Restrict which senders and recipients a Workers sendemail binding can use with Email Service.","url":"https://developers.cloudflare.com/email-service/configuration/send-bindings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/configuration/send-bindings/
  schema: 1
---
<p>When you add a <code>send_email</code> binding to a Worker, you can restrict which addresses it may send from and to. Configure these restrictions in your Wrangler configuration file. For the binding API itself, refer to the <a href="/email-service/api/send-emails/workers-api/">Workers API</a>.</p>
<h2 id="binding-types">Binding types</h2>
<p>Each entry in <code>send_email</code> can be configured to restrict what the binding can do. The sender address must always belong to a domain you have onboarded to Email Service.</p>
<ul>
<li><strong>No restriction attribute</strong>: The binding can send to any verified destination address in your account.</li>
<li><strong><code>destination_address</code></strong>: The binding can only send to the single destination address configured here. If you call <code>send()</code> with <code>to</code> set to <code>null</code> or <code>undefined</code>, the configured address is used.</li>
<li><strong><code>allowed_destination_addresses</code></strong>: The binding can only send to addresses listed in this allowlist.</li>
<li><strong><code>allowed_sender_addresses</code></strong>: The binding can only send from the addresses listed in this allowlist.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8615.md")
</div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/api/send-emails/workers-api/">Workers API</a> — send emails from a Worker using the binding.</li>
<li><a href="/email-service/configuration/domains/">Domain configuration</a> — onboard the domains you send from.</li>
</ul>
