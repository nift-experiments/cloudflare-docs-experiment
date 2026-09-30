---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/
  description: Which records transfer when Cloudflare is primary.
  full_title: Records transfer · Cloudflare DNS docs
  head_html: <title>Records transfer · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Which records transfer when Cloudflare is primary."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/index.md"><meta property="og:title" content="Records transfer · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Which records transfer when Cloudflare is primary."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/#page","headline":"Records transfer \u00b7 Cloudflare DNS docs","description":"Which records transfer when Cloudflare is primary.","url":"https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/
  schema: 1
---
<p>Consider the sections below to understand the expected behaviors, depending on DNS record type and proxied status.</p>
<h2 id="proxied-records">Proxied records</h2>
<p>For each <a href="/dns/proxy-status/">proxied DNS record</a> in your zone, Cloudflare will transfer out two <code>A</code> and two <code>AAAA</code> records.</p>
<p>These records correspond to the <a href="https://www.cloudflare.com/ips">Cloudflare IP addresses</a> used for proxying traffic.</p>
<h2 id="dns-only-cname-records">DNS-only CNAME records</h2>
<p>As explained in <a href="/dns/manage-dns-records/reference/dns-record-types/#cname">DNS record types</a>, Cloudflare uses a process called <a href="/dns/cname-flattening/">CNAME flattening</a> to return the final IP address instead of the CNAME target. CNAME flattening improves performance and is also what allows you to set a CNAME record on the zone apex.</p>
<p>Depending on the <a href="/dns/cname-flattening/set-up-cname-flattening/">settings</a> you have, when you use DNS-only CNAME records with outgoing zone transfers, you can expect the following:</p>
<ul>
<li>For DNS-only CNAME records on the zone apex, Cloudflare will always transfer out the flattened IP addresses.</li>
<li>For DNS-only CNAME records on subdomains, Cloudflare will only transfer out flattened IP addresses if the setting <a href="/dns/cname-flattening/set-up-cname-flattening/#for-all-cname-records"><strong>CNAME flattening for all CNAME records</strong></a> is enabled.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="per-record-cname-flattening">Per-record CNAME flattening</h3>
@markup("md", "content/.markup/bodies/8058.md")
</aside>
<h2 id="records-that-are-not-transferred">Records that are not transferred</h2>
<p>The following records are not transferred out when you use Cloudflare as primary:</p>
<ul>
<li><a href="/ssl/edge-certificates/caa-records/">CAA records</a></li>
<li>TXT records used for TLS certificate validation</li>
<li>DNS-only <a href="/load-balancing/load-balancers/dns-records/">Load Balancing</a> records</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8057.md")
</aside>
