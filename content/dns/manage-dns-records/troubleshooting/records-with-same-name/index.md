---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/records-with-same-name/
  description: Handle multiple DNS records with the same name.
  full_title: Cannot add DNS records with the same name · Cloudflare DNS docs
  head_html: <title>Cannot add DNS records with the same name · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Handle multiple DNS records with the same name."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/records-with-same-name/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/records-with-same-name/index.md"><meta property="og:title" content="Cannot add DNS records with the same name · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Handle multiple DNS records with the same name."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/records-with-same-name/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/records-with-same-name/#page","headline":"Cannot add DNS records with the same name \u00b7 Cloudflare DNS docs","description":"Handle multiple DNS records with the same name.","url":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/records-with-same-name/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/troubleshooting/records-with-same-name/
  schema: 1
---
<p>Occasionally, Cloudflare will not allow you to <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">create new DNS records</a> with the same value in the <strong>Name</strong> field.</p>
<p>This error can occur due to the special requirements of CNAME records<sup><a href="#footnote-1">1</a></sup>.</p>
<h2 id="causes">Causes</h2>
<p>You will encounter this error if you try to do one of the following:</p>
<ul>
<li>Create a CNAME record with a <strong>Name</strong> matching the name of an existing A/AAAA<sup><a href="#footnote-2">2</a></sup> or CNAME record.</li>
<li>Create an A/AAAA record with a <strong>Name</strong> matching the name of an existing CNAME record.</li>
<li>Create a <a href="/spectrum/">Spectrum</a> application for a name that already has a manually-created <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> record. Spectrum provisions and manages its own DNS record for the application, so Cloudflare does not support having both on the same name. Multiple Spectrum applications can, however, share the same name. Refer to <a href="/spectrum/reference/troubleshooting/#cannot-create-spectrum-application--dns-record-already-exists">Spectrum Troubleshooting</a> for recommended workarounds.</li>
</ul>
<p>Cloudflare prevents you from creating this combination of records because if a CNAME record is provided for a hostname DNS servers expect only that CNAME record to provide DNS information for that hostname.</p>
<p>Adding additional records would send conflicting information to DNS servers. For a technical explanation of the mechanism behind this, refer to <a href="https://www.rfc-editor.org/rfc/rfc1034">RFC 1034</a>.</p>
<h2 id="solution">Solution</h2>
<p>Review your existing DNS records to find the matching value in the <strong>Name</strong> field. Then, decide whether you want to keep the current record or delete it and make a new one.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7764.md")
</aside>
<p><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/">CNAME records</a> map a domain name to another (canonical) domain name. They can be used to resolve other record types present on the target domain name.</p>
<p><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/">A and AAAA records</a> map a domain name to one or multiple IPv4 or IPv6 address(es).</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1"></li>
<li id="footnote-2"></li></ol></section>
