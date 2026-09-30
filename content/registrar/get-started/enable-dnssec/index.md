---
cp9:
  canonical: https://developers.cloudflare.com/registrar/get-started/enable-dnssec/
  description: Enable DNSSEC for your registered domain.
  full_title: Domain Name System Security Extensions (DNSSEC) · Cloudflare Registrar docs
  head_html: <title>Domain Name System Security Extensions (DNSSEC) · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable DNSSEC for your registered domain."><link rel="canonical" href="https://developers.cloudflare.com/registrar/get-started/enable-dnssec/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/get-started/enable-dnssec/index.md"><meta property="og:title" content="Domain Name System Security Extensions (DNSSEC) · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable DNSSEC for your registered domain."><meta property="og:url" content="https://developers.cloudflare.com/registrar/get-started/enable-dnssec/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/get-started/enable-dnssec/#page","headline":"Domain Name System Security Extensions (DNSSEC) \u00b7 Cloudflare Registrar docs","description":"Enable DNSSEC for your registered domain.","url":"https://developers.cloudflare.com/registrar/get-started/enable-dnssec/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/get-started/enable-dnssec/
  schema: 1
---
<p>The domain name system (DNS) translates domain names into numeric Internet addresses. However, DNS is a fundamentally insecure protocol. It does not guarantee where DNS records come from and accepts any requests given to it.</p>
<p><a href="/dns/dnssec/">DNSSEC</a> creates a secure layer to the domain name system by adding cryptographic signatures to DNS records. By doing so, your request can check the signature to verify that the record you need comes from the authoritative nameserver and was not altered along the way.</p>
<h2 id="enable-or-disable-dnssec">Enable or disable DNSSEC</h2>
<p>Cloudflare Registrar offers one-click DNSSEC activation for free to all customers:</p>
<ol>
<li>In Cloudflare dashboard, go to the <strong>Manage Domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the domain that you want to activate DNSSEC and select <strong>Manage</strong>.</li>
<li>Select <strong>Configuration</strong> &gt; <strong>Enable DNSSEC</strong>. If DNSSEC was previously activated, select <strong>Disable DNSSEC</strong> to disable it.</li>
</ol>
<p>Cloudflare publishes delegation signer (DS) records in the form of <a href="https://www.cloudflare.com/dns/dnssec/how-dnssec-works/">CDS and CDNSKEY records</a> for a domain delegated to Cloudflare. Cloudflare Registrar scans those records at regular intervals, gathers those details and sends them to your domain's registry.</p>
<p>This process can take one to two days after you first enable DNSSEC.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12755.md")
</aside>
<h2 id="confirming-dnssec">Confirming DNSSEC</h2>
<p>When DNSSEC has been successfully applied to your domain, Cloudflare shows you a confirmed status. Go to <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS</strong> &gt; <strong>Settings</strong></a> in the Cloudflare dashboard, and scroll down to <strong>DNSSEC</strong>.</p>
<p>You can also confirm this by reviewing the <a href="https://lookup.icann.org/">WHOIS information</a> for your domain. Domains with DNSSEC will read <code>signedDelegation</code> in the DNSSEC field.</p>
