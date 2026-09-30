---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/
  description: Enable DNSSEC for a subdomain zone.
  full_title: Enable DNSSEC - subdomain setup · Cloudflare DNS docs
  head_html: <title>Enable DNSSEC - subdomain setup · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable DNSSEC for a subdomain zone."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/index.md"><meta property="og:title" content="Enable DNSSEC - subdomain setup · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable DNSSEC for a subdomain zone."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/#page","headline":"Enable DNSSEC - subdomain setup \u00b7 Cloudflare DNS docs","description":"Enable DNSSEC for a subdomain zone.","url":"https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/subdomain-setup/dnssec/
  schema: 1
---
<p>As opposed to the <a href="/dns/dnssec/">normal process</a> for enabling DNSSEC, DNSSEC with a subdomain setup requires a few additional steps.</p>
<h2 id="requirements">Requirements</h2>
<p>To use DNSSEC for a subdomain setup, DNSSEC must be enabled on the parent zone. After enabling DNSSEC on the parent zone, you should wait the minimum <span class="nb-glossary-tooltip" title="time-to-live (TTL)">TTL</span> value (specified in the <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/">SOA record</a> of the parent zone) to ensure DNS resolvers provide the same DNS query responses.</p>
<h2 id="setup">Setup</h2>
<ol>
<li>
<p><a href="/dns/zone-setups/subdomain-setup/setup/#how-to">Create</a> the child zone.</p>
</li>
<li>
<p>Make sure the child zone is <a href="/dns/zone-setups/reference/domain-status/">active</a> on Cloudflare and that DNS resolution is working properly for your subdomain.</p>
</li>
<li>
<p><a href="/dns/dnssec/">Enable DNSSEC</a> for the child zone and save the information provided within the DS record output.</p>
</li>
<li>
<p>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page of the parent zone, <a href="/dns/manage-dns-records/how-to/create-dns-records/">add the DS record</a> from the previous step.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/dns/ds-record-example.png" alt="Screenshot showing how to add a DS record within Cloudflare" /></p>
<ol start="5">
<li>
<p>Add an A record to the child zone to validate DNS resolution.</p>
</li>
<li>
<p>Wait two to six hours. Then, <a href="/dns/dnssec/troubleshooting/#test-dnssec-with-dig">test the A record</a> added in the previous step using multiple DNS resolvers with DNSSEC validation (<code>1.1.1.1</code>, <code>8.8.8.8</code>, and <code>9.9.9.9</code>). For example, if the A record is for <code>test.child.example.com</code>: <code>dig test.child.example.com +dnssec @1.1.1.1</code>.</p>
</li>
</ol>
