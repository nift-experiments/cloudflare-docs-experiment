---
cp9:
  canonical: https://developers.cloudflare.com/dns/dns-firewall/
  description: Protect and accelerate authoritative nameservers with DNS-level caching and DDoS mitigation.
  full_title: DNS Firewall · Cloudflare DNS docs
  head_html: <title>DNS Firewall · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Protect and accelerate authoritative nameservers with DNS-level caching and DDoS mitigation."><link rel="canonical" href="https://developers.cloudflare.com/dns/dns-firewall/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/dns-firewall/index.md"><meta property="og:title" content="DNS Firewall · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Protect and accelerate authoritative nameservers with DNS-level caching and DDoS mitigation."><meta property="og:url" content="https://developers.cloudflare.com/dns/dns-firewall/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="DNS Firewall"><meta name="pcx_tags" content="Caching"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/dns/dns-firewall/#page","headline":"DNS Firewall \u00b7 Cloudflare DNS docs","description":"Protect and accelerate authoritative nameservers with DNS-level caching and DDoS mitigation.","url":"https://developers.cloudflare.com/dns/dns-firewall/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Caching"]}</script>
  markdown: true
  noindex: false
  route: /dns/dns-firewall/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/7702.md")
</div>
<div class="nb-plan">
<p>Enterprise-only paid add-on</p>
</div>
<p>Cloudflare DNS Firewall proxies all DNS queries to your nameservers through Cloudflare’s global network. This action protects upstream nameservers from DDoS attacks and reduces load by caching DNS responses.</p>
<p><img src="/assets/upstream/images/dns/dns-firewall-overview.png" alt="Diagram showing protection provided by DNS Firewall. For more details, read further." /></p>
<p>DNS Firewall is for customers who need to speed up and protect entire authoritative nameservers. If you need to speed up and protect individual zones, refer to Cloudflare DNS <a href="/dns/zone-setups/">Setups</a>.</p>
<hr />
<h2 id="how-dns-firewall-works">How DNS Firewall works</h2>
<p>When a DNS query for your domain takes place:</p>
<ol>
<li>Queries go to the Cloudflare data center that is closest to the website visitor. This is determined by the location of the DNS resolver.</li>
<li>Cloudflare tries to return a DNS response from cache.</li>
<li>If the response is not available in cache, Cloudflare queries the upstream authoritative nameservers.</li>
<li>After returning the response from the nameservers, Cloudflare temporarily caches it for subsequent DNS queries.</li>
</ol>
<hr />
<h2 id="benefits">Benefits</h2>
<p>DNS Firewall provides the following benefits while allowing your organization total control over your authoritative nameservers:</p>
<ul>
<li>DDoS mitigation</li>
<li>High availability</li>
<li>Global distribution</li>
<li>Enhanced performance</li>
<li>Bandwidth savings</li>
<li><a href="/dns/dns-firewall/setup/#additional-options">Rate limiting per data center</a></li>
<li>Minimum and maximum cache TTL specification</li>
<li>DNS <a href="https://datatracker.ietf.org/doc/html/rfc8482">ANY</a> query type block</li>
</ul>
