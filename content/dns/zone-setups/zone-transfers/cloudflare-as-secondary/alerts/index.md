---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/
  description: Set up alerts for secondary DNS zone transfer events.
  full_title: Alerts for Secondary DNS · Cloudflare DNS docs
  head_html: <title>Alerts for Secondary DNS · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up alerts for secondary DNS zone transfer events."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/index.md"><meta property="og:title" content="Alerts for Secondary DNS · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up alerts for secondary DNS zone transfer events."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/#page","headline":"Alerts for Secondary DNS \u00b7 Cloudflare DNS docs","description":"Set up alerts for secondary DNS zone transfer events.","url":"https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/
  schema: 1
---
<p>You can configure alerts to receive notifications for changes in your secondary DNS.</p>
<details><summary>Secondary DNS all Primaries Failing</summary><strong>Who is it for?</strong><p>Enterprise customers who have at least one secondary zone in their account and want to receive a notification if all of their primary nameservers are failing.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Secondary DNS</p>
<strong>What should you do if you receive one?</strong><ol>
<li>Confirm that your primary nameservers are up and running.</li>
<li>Confirm that the <a href="/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/">Access Control Lists (ACLs)</a> on your primary nameservers are configured correctly.</li>
<li>Confirm that your primary nameservers are configured correctly in your Cloudflare account (correct IP, port, TSIG).</li>
</ol>
</details><details><summary>Secondary DNS Primaries Failing</summary><strong>Who is it for?</strong><p>Enterprise customers who have at least one secondary zone and want to receive a notification if at least one of their primary nameservers is failing while transfers from at least one other primary are still successful.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Secondary DNS.</p>
<strong>What should you do if you receive one?</strong><ol>
<li>Confirm that your primary nameservers are up and running.</li>
<li>Confirm that the <a href="/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/">Access Control Lists (ACLs)</a> on your primary nameservers are configured correctly.</li>
<li>Confirm that your primary nameservers are configured correctly in your Cloudflare account (correct IP, port, TSIG).</li>
</ol>
</details><details><summary>Secondary DNS Successfully Updated</summary><strong>Who is it for?</strong><p>Enterprise customers who have at least one secondary zone in their account and want to receive a notification on successful zone transfers.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Secondary DNS.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Everything is working correctly.</p>
</details><details><summary>Secondary DNS Warning</summary><strong>Who is it for?</strong><p>Customers who are using Cloudflare for Secondary DNS and want to receive notifications about warnings issued by the transferred zone.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>Actions for failure notifications will depend on the type of failure.</p>
</details>
<p>Refer to <a href="/notifications/get-started/">Cloudflare Notifications</a> for more information on how to set up an alert.</p>
