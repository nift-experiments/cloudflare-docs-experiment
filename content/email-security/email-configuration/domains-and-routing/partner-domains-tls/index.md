---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/domains-and-routing/partner-domains-tls/
  description: Enforce TLS requirements for emails from specific partner domains in Email security.
  full_title: Partner Domains TLS · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Partner Domains TLS · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Enforce TLS requirements for emails from specific partner domains in Email security."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/domains-and-routing/partner-domains-tls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/domains-and-routing/partner-domains-tls/index.md"><meta property="og:title" content="Partner Domains TLS · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enforce TLS requirements for emails from specific partner domains in Email security."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/domains-and-routing/partner-domains-tls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/domains-and-routing/partner-domains-tls/
  schema: 1
---
<p>To add additional TLS requirements for emails coming from certain domains, you can enforce higher levels of SSL/TLS inspection. If TLS is required, mail without TLS from the specified domain will be dropped.</p>
<h2 id="add-a-domain">Add a domain</h2>
<p>To require that email from a specific domain passes SSL/TLS inspection:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>On <strong>Email Configuration</strong>, go to <strong>Domains &amp; Routing</strong> &gt; <strong>Partner Domains TLS</strong>.</li>
<li>Select <strong>New Partner Domain</strong>.</li>
<li>Enter a <strong>Domain</strong> and any <strong>Notes</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="exempt-tls-inspection">Exempt TLS inspection</h2>
<p>If you decide to exempt a domain from TLS inspection - by toggling <strong>Require TLS Inbound</strong> to <strong>Off</strong> - this will not turn off enforcement against legacy standards like SSLv1, SSLv2, and TLSv1, which is generally considered insecure.</p>
