---
cp9:
  canonical: https://developers.cloudflare.com/email-service/configuration/subdomains/
  description: Configure Email Sending and Email Routing on subdomains within your zone.
  full_title: Subdomains · Cloudflare Email Service docs
  head_html: <title>Subdomains · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Email Sending and Email Routing on subdomains within your zone."><link rel="canonical" href="https://developers.cloudflare.com/email-service/configuration/subdomains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/configuration/subdomains/index.md"><meta property="og:title" content="Subdomains · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Email Sending and Email Routing on subdomains within your zone."><meta property="og:url" content="https://developers.cloudflare.com/email-service/configuration/subdomains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/configuration/subdomains/#page","headline":"Subdomains \u00b7 Cloudflare Email Service docs","description":"Configure Email Sending and Email Routing on subdomains within your zone.","url":"https://developers.cloudflare.com/email-service/configuration/subdomains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/configuration/subdomains/
  schema: 1
---
<p>Email Routing is a zone-level feature that applies to the apex domain (for example, <code>example.com</code>) by default. Email Sending treats each domain separately and is onboarded per domain. You can extend either service to subdomains of the same zone, such as <code>mail.example.com</code> or <code>corp.example.com</code>, but the onboarding flow differs between the two.</p>
<p>A zone can have up to 30 domains configured for Email Routing or Email Sending combined, including the apex domain. Refer to <a href="/email-service/platform/limits/">Limits</a> for the full list of platform limits.</p>
<h2 id="add-a-subdomain-to-email-routing">Add a subdomain to Email Routing</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select the apex domain, then open <strong>Settings</strong>.</li>
<li>Under <strong>Subdomains</strong>, enter the subdomain you want to enable in the inline form and submit it.</li>
</ol>
<p>Cloudflare adds the required DNS records to the subdomain. Once the records propagate, you can create <a href="/email-service/configuration/email-routing-addresses/">routing rules</a> on the subdomain in the same way as on the apex domain.</p>
<h2 id="add-a-subdomain-to-email-sending">Add a subdomain to Email Sending</h2>
<p>Email Sending treats a subdomain as a separate sending domain. Onboard the subdomain through the standard onboarding flow:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Sending</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select <strong>Onboard Domain</strong> and choose the subdomain you want to send from. The onboarding flow adds the <code>cf-bounce</code> MX, SPF, DKIM, and DMARC records to the subdomain.</li>
<li>Select <strong>Done</strong>.</li>
</ol>
<p>Once verified, you can send emails from addresses on the subdomain (for example, <code>notifications@mail.example.com</code>) using either the <a href="/email-service/api/send-emails/rest-api/">REST API</a> or the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a>.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/configuration/domains/">Domain configuration</a> — manage DNS records for sending and routing.</li>
<li><a href="/email-service/configuration/email-routing-addresses/">Routing rules and addresses</a> — create routing rules on subdomains.</li>
<li><a href="/email-service/concepts/deliverability/">Deliverability</a> — separate subdomains for different email types.</li>
</ul>
