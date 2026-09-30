---
cp9:
  canonical: https://developers.cloudflare.com/email-service/platform/pricing/
  description: Email Service pricing for outbound sending and inbound routing across Workers Free and Paid plans.
  full_title: Pricing · Cloudflare Email Service docs
  head_html: <title>Pricing · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Email Service pricing for outbound sending and inbound routing across Workers Free and Paid plans."><link rel="canonical" href="https://developers.cloudflare.com/email-service/platform/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/platform/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Email Service pricing for outbound sending and inbound routing across Workers Free and Paid plans."><meta property="og:url" content="https://developers.cloudflare.com/email-service/platform/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/platform/pricing/#page","headline":"Pricing \u00b7 Cloudflare Email Service docs","description":"Email Service pricing for outbound sending and inbound routing across Workers Free and Paid plans.","url":"https://developers.cloudflare.com/email-service/platform/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/platform/pricing/
  schema: 1
---
<p>Cloudflare Email Service pricing is based on your Cloudflare plan and email usage.</p>
<h2 id="plan-pricing">Plan pricing</h2>
<p>Email Routing is available on both the Workers Free and Workers Paid plans. Sending to arbitrary recipients requires the Workers Paid plan. Sending to <a href="/email-service/configuration/email-routing-addresses/#destination-addresses">verified destination addresses</a> in your account is free on all plans, including when only Email Routing is configured.</p>
<table>
<thead>
<tr>
<th></th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Outbound emails (Email Sending)</strong></td>
<td>Not available</td>
<td>3,000 included per month, then $0.35 per 1,000 emails</td>
</tr>
<tr>
<td><strong>Inbound emails (Email Routing)</strong></td>
<td>Unlimited</td>
<td>Unlimited</td>
</tr>
</tbody>
</table>
<p>The 3,000 included emails apply per account, per month, aligned with your Cloudflare subscription billing cycle. Emails that hard-bounce or are otherwise accepted by Email Service count toward the quota. Emails rejected at the API boundary, including sends blocked by the <a href="/email-service/concepts/suppressions/">suppression list</a>, do not count toward the quota.</p>
<p>Sends to verified destination addresses are free and do not count toward the included quota.</p>
<p>Email Routing Workers is billed according to <a href="/workers/platform/pricing/">Workers pricing</a>.</p>
