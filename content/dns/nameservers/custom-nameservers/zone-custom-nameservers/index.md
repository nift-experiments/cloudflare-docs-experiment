---
cp9:
  canonical: https://developers.cloudflare.com/dns/nameservers/custom-nameservers/zone-custom-nameservers/
  description: With zone-level custom nameservers, each custom nameserver name must be a subdomain of the zone where the custom nameservers are configured. These custom nameservers can only be used within the respective zone.
  full_title: Zone custom nameservers · Cloudflare DNS docs
  head_html: <title>Zone custom nameservers · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="With zone-level custom nameservers, each custom nameserver name must be a subdomain of the zone where the custom nameservers are configured. These custom nameservers can only be used within the respective zone."><link rel="canonical" href="https://developers.cloudflare.com/dns/nameservers/custom-nameservers/zone-custom-nameservers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/nameservers/custom-nameservers/zone-custom-nameservers/index.md"><meta property="og:title" content="Zone custom nameservers · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="With zone-level custom nameservers, each custom nameserver name must be a subdomain of the zone where the custom nameservers are configured. These custom nameservers can only be used within the respective zone."><meta property="og:url" content="https://developers.cloudflare.com/dns/nameservers/custom-nameservers/zone-custom-nameservers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/nameservers/custom-nameservers/zone-custom-nameservers/#page","headline":"Zone custom nameservers \u00b7 Cloudflare DNS docs","description":"With zone-level custom nameservers, each custom nameserver name must be a subdomain of the zone where the custom nameservers are configured. These custom nameservers can only be used within the respective zone.","url":"https://developers.cloudflare.com/dns/nameservers/custom-nameservers/zone-custom-nameservers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/nameservers/custom-nameservers/zone-custom-nameservers/
  schema: 1
---
<p>With zone custom nameservers (ZCNS), each custom nameserver name must be a subdomain of the zone where the custom nameservers are configured.</p>
<p>For example, for a zone <code>domain.test</code>, the ZCNS can be <code>ns1.domain.test</code> and <code>ns2.domain.test</code> but they cannot use a different TLD (<code>ns1.domain.org</code>) nor a different domain (<code>ns1.example.com</code>).</p>
<h2 id="availability">Availability</h2>
<p>Zone custom nameservers are available for zones on Business or Enterprise plans. Via API or on the dashboard.</p>
<h2 id="use-zone-custom-nameservers">Use zone custom nameservers</h2>
<h3 id="primary-zones-full-setup">Primary zones (full setup)</h3>
<p>To create zone custom nameservers:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7864.md")
</div></div>
<p>Cloudflare will assign an IPv4 and an IPv6 address to each ZCNS name and automatically create the associated <code>A</code> or <code>AAAA</code> records.</p>
<p>The next step depends on whether you are using <a href="/registrar/">Cloudflare Registrar</a> for your domain:</p>
<ul>
<li>If you are using Cloudflare Registrar for your domain, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> to add the custom nameservers and IP addresses as glue records to the domain.</li>
<li>If you are not using Cloudflare Registrar for your domain, add the zone custom nameservers at your registrar as your authoritative nameservers and as glue (A and AAAA) records (<a href="https://www.rfc-editor.org/rfc/rfc1912.html">RFC 1912</a>). If you do not add these records, DNS lookups for your domain will fail.</li>
</ul>
<h3 id="secondary-zones">Secondary zones</h3>
<p>If you are using <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Cloudflare as a secondary DNS provider</a>, you can still set up zone custom nameservers. After following the <a href="/dns/nameservers/custom-nameservers/zone-custom-nameservers/#primary-zones-full-setup">steps above</a> to create zone custom nameservers, do the following:</p>
<ol>
<li>Get the ZCNS IPs. You can find them on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page or you can use the <a href="/api/resources/zones/methods/get/">Zone details endpoint</a> to get the <code>vanity_name_servers_ips</code>.</li>
<li>At your primary DNS provider, add <a href="/dns/manage-dns-records/reference/dns-record-types/#ns"><code>NS</code> records</a> and, on the subdomains that you used as ZCNS names, add <code>A/AAAA</code> records.</li>
<li>At your registrar, add the zone custom nameservers as your authoritative nameservers and as glue (A and AAAA) records (<a href="https://www.rfc-editor.org/rfc/rfc1912.html">RFC 1912</a>).</li>
</ol>
<h2 id="remove-zone-custom-nameservers">Remove zone custom nameservers</h2>
<p>To remove zone custom nameservers (and their associated, read-only DNS records):</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7867.md")
</div></div>
<p>Cloudflare will remove your ZCNS and their associated read-only <code>A</code> or <code>AAAA</code> records.</p>
<p>If you are not using Cloudflare Registrar for your domain, make sure to adjust your nameservers at the registrar, parent zone, or Primary DNS provider accordingly.</p>
