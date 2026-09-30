---
cp9:
  canonical: https://developers.cloudflare.com/email-service/examples/email-sending/recipients/
  description: Send to multiple recipients, CC and BCC, and named addresses using the Workers binding, REST API, or SMTP.
  full_title: Specify recipients · Cloudflare Email Service docs
  head_html: <title>Specify recipients · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Send to multiple recipients, CC and BCC, and named addresses using the Workers binding, REST API, or SMTP."><link rel="canonical" href="https://developers.cloudflare.com/email-service/examples/email-sending/recipients/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/examples/email-sending/recipients/index.md"><meta property="og:title" content="Specify recipients · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send to multiple recipients, CC and BCC, and named addresses using the Workers binding, REST API, or SMTP."><meta property="og:url" content="https://developers.cloudflare.com/email-service/examples/email-sending/recipients/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/examples/email-sending/recipients/#page","headline":"Specify recipients \u00b7 Cloudflare Email Service docs","description":"Send to multiple recipients, CC and BCC, and named addresses using the Workers binding, REST API, or SMTP.","url":"https://developers.cloudflare.com/email-service/examples/email-sending/recipients/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/examples/email-sending/recipients/
  schema: 1
---
<p class="article-summary">Specify multiple recipients, CC and BCC, and named addresses when sending with Email Service.</p>
<p>Email Service lets you specify recipients in several ways — multiple recipients, CC and BCC, and named addresses — using the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a>, the <a href="/email-service/api/send-emails/rest-api/">REST API</a>, or <a href="/email-service/api/send-emails/smtp/">SMTP</a>. The combined number of addresses across <code>to</code>, <code>cc</code>, and <code>bcc</code> must not exceed 50. See <a href="/email-service/platform/limits/">Limits</a>.</p>
<h2 id="multiple-recipients">Multiple recipients</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="send-method"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8675.md")
</div></div>
<h2 id="cc-and-bcc">CC and BCC</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="send-method"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8679.md")
</div></div>
<h2 id="named-recipients">Named recipients</h2>
<p>Provide a display name alongside the address for the sender and recipients.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="send-method"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8683.md")
</div></div>
<h2 id="mixed-plain-and-named-recipients">Mixed plain and named recipients</h2>
<p>Combine plain addresses and named addresses in the same <code>to</code> field.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="send-method"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8687.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/api/send-emails/workers-api/">Workers API</a> — full <code>send()</code> reference.</li>
<li><a href="/email-service/api/send-emails/rest-api/">REST API</a> — send over HTTPS.</li>
<li><a href="/email-service/api/send-emails/smtp/">SMTP</a> — send from any SMTP-capable client.</li>
<li><a href="/email-service/examples/email-sending/email-attachments/">Email attachments</a> — send PDFs, inline images, and uploads.</li>
</ul>
