---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/
  description: Learn how to troubleshoot issues with a primary setup (full)
  full_title: Troubleshooting primary setup (full) · Cloudflare DNS docs
  head_html: <title>Troubleshooting primary setup (full) · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to troubleshoot issues with a primary setup (full)"><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting primary setup (full) · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to troubleshoot issues with a primary setup (full)"><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/#page","headline":"Troubleshooting primary setup (full) \u00b7 Cloudflare DNS docs","description":"Learn how to troubleshoot issues with a primary setup (full)","url":"https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/full-setup/troubleshooting/
  schema: 1
---
<p>If you see unexpected results when <a href="/dns/zone-setups/full-setup/setup/">changing your nameservers</a>, review the following troubleshooting questions.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7940.md")
</aside>
<h2 id="is-a-ds-record-present-at-your-registrar">Is a DS record present at your registrar?</h2>
<p>You need to remove any pre-Cloudflare <strong>DS</strong> records at your registrar to update your authoritative nameservers. This will disable DNSSEC and allow Cloudflare to resolve your domain name.</p>
<p>You can then <a href="/dns/zone-setups/full-setup/setup/#4-re-enable-dnssec">re-enable DNSSEC</a> in Cloudflare and at your registrar after you have changed your nameservers.</p>
<h2 id="do-the-nameservers-at-your-registrar-exactly-match-the-values-provided-by-cloudflare">Do the nameservers at your registrar exactly match the values provided by Cloudflare?</h2>
<p>If the nameservers in your registrar do not exactly match those provided by Cloudflare, your domain will not resolve correctly.</p>
<h2 id="are-additional-nameservers-listed-at-your-registrar">Are additional nameservers listed at your registrar?</h2>
<p>If so, you should remove these nameservers.</p>
<p>You should have only Cloudflare nameservers listed at your registrar.</p>
<h2 id="have-you-waited-longer-than-24-hours">Have you waited longer than 24 hours?</h2>
<p>For some registrars, you will need to wait up to 24 hours for updates to your nameservers.</p>
