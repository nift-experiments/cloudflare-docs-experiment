---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/
  description: Troubleshoot domain verification failures caused by proxied CNAME records, CNAME flattening, or NS record conflicts.
  full_title: Cannot verify a domain with CNAME · Cloudflare DNS docs
  head_html: <title>Cannot verify a domain with CNAME · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot domain verification failures caused by proxied CNAME records, CNAME flattening, or NS record conflicts."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/index.md"><meta property="og:title" content="Cannot verify a domain with CNAME · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot domain verification failures caused by proxied CNAME records, CNAME flattening, or NS record conflicts."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/#page","headline":"Cannot verify a domain with CNAME \u00b7 Cloudflare DNS docs","description":"Troubleshoot domain verification failures caused by proxied CNAME records, CNAME flattening, or NS record conflicts.","url":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/troubleshooting/cname-domain-verification/
  schema: 1
---
<p>When configuring services from external providers - such as email services, for example - it is possible that they require you to verify your domain by placing a CNAME record at your zone, similar to the following:</p>
<pre tabindex="0"><code class="language-txt">&lt;value&gt;._domainkey.example.com CNAME &lt;hostname&gt;.&lt;service provider domain&gt;&#10;</code></pre>
<p>Consider the sections below if this is not working correctly for you.</p>
<h2 id="causes">Causes</h2>
<p>You may find issues if you have one of the following:</p>
<ul>
<li>The CNAME record you created for domain verification is set to <a href="/dns/proxy-status/"><strong>Proxied</strong></a>.</li>
<li>The CNAME record is correctly set to DNS only (not proxied) but, in your <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings">zone settings</a>, <a href="/dns/cname-flattening/set-up-cname-flattening/#for-all-cname-records"><strong>CNAME flattening for all CNAME records</strong></a> is on.</li>
<li>The CNAME record is correctly set to DNS only (not proxied) but CNAME flattening is set <a href="/dns/cname-flattening/set-up-cname-flattening/#per-record">for that record specifically</a>.</li>
<li>An <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/">NS record</a> exists, causing a different DNS provider to be authoritative for the subdomain.</li>
</ul>
<h2 id="solution">Solution</h2>
<p>Make sure that:</p>
<ul>
<li>In your zone DNS settings: <a href="/dns/cname-flattening/"><strong>CNAME flattening for all CNAME records</strong></a> is turned off.</li>
<li>On the DNS records table: you have filled in the CNAME record fields correctly, proxy status is set to <strong>DNS only</strong>, and <strong>Flatten</strong> is turned off.</li>
<li>You have the correct NS configuration, and either:
<ul>
<li>Make sure that the CNAME record is set as expected with the DNS provider that the NS record points to.</li>
<li>Review your configuration for other DNS records that may be affected by the NS record. Once you are aware of any consequences or have made any necessary adjustments, remove the NS record so that the CNAME is resolved to the target you configured on Cloudflare.</li>
</ul>
</li>
</ul>
