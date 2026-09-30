---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/partial-setup/
  description: Use Cloudflare with your existing DNS provider via CNAME setup.
  full_title: CNAME setup (Partial) · Cloudflare DNS docs
  head_html: <title>CNAME setup (Partial) · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Cloudflare with your existing DNS provider via CNAME setup."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/partial-setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/partial-setup/index.md"><meta property="og:title" content="CNAME setup (Partial) · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Cloudflare with your existing DNS provider via CNAME setup."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/partial-setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/partial-setup/#page","headline":"CNAME setup (Partial) \u00b7 Cloudflare DNS docs","description":"Use Cloudflare with your existing DNS provider via CNAME setup.","url":"https://developers.cloudflare.com/dns/zone-setups/partial-setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/partial-setup/
  schema: 1
---
<p>A CNAME setup (also known as partial setup) allows you to use <a href="/fundamentals/concepts/how-cloudflare-works/">Cloudflare's reverse proxy</a> while maintaining your primary and authoritative DNS provider.</p>
<p>Use this option to <span class="nb-glossary-tooltip" title="proxy status">proxy</span> only individual subdomains through Cloudflare when you cannot change your authoritative DNS provider. You will be able to create A, AAAA, and CNAME records, which are the DNS record types that can be <a href="/dns/proxy-status/">proxied</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/7936.md")
</aside>
<p>Once you are on a CNAME setup (partial), the actual resolution of your records to Cloudflare depends on CNAME records <a href="/dns/zone-setups/partial-setup/setup/#3-add-dns-records">added at your authoritative DNS provider</a>. Check your authoritative DNS provider to know which records are pointing to <code>{your-hostname}.cdn.cloudflare.net</code>.</p>
<h2 id="how-to">How to</h2>
<ul>
<li><a href="/dns/zone-setups/partial-setup/setup/">Set up a partial zone (CNAME setup)</a></li>
<li><a href="/dns/zone-setups/conversions/convert-partial-to-full/">Convert a CNAME setup (partial) to a primary setup (full)</a></li>
<li><a href="/dns/zone-setups/conversions/convert-partial-to-secondary/">Convert a CNAME setup (partial) to a secondary setup</a></li>
<li><a href="/dns/zone-setups/partial-setup/setup/#other-record-types">Create DNS records of other types</a></li>
</ul>
<h2 id="availability-1">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="reference">Reference</h2>
<h3 id="dns-resolution">DNS resolution</h3>
<p>When you have a partial zone (<span class="nb-glossary-tooltip" title="CNAME setup">CNAME setup</span>), Cloudflare resolves <a href="/dns/zone-setups/partial-setup/dns-resolution/">DNS records differently</a> than for primary zones (full setup).</p>
<h3 id="cname-flattening">CNAME flattening</h3>
<p>A CNAME setup (partial) requires the proxied hostname to be pointed to Cloudflare via a CNAME record. Since <a href="https://datatracker.ietf.org/doc/html/rfc1912#section-2.4">CNAME records are not allowed on the zone apex</a> (<code>example.com</code>), you can only proxy your zone apex to Cloudflare if your authoritative DNS provider supports <a href="https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/">CNAME Flattening</a>.</p>
<p>If your authoritative DNS provider does not support CNAME Flattening, redirect its traffic — for example, with an <code>.htaccess</code> file — to a subdomain proxied to Cloudflare. Alternatively, you can use <a href="/fundamentals/concepts/cloudflare-ip-addresses/#customize-cloudflare-ip-addresses">static IPs or BYOIPs</a>.</p>
<h3 id="ddos-protection">DDoS protection</h3>
<p><a href="/ddos-protection/">DDoS protection</a> for attacks against DNS infrastructure is only available for domains on <a href="/dns/zone-setups/full-setup/">primary setup (full)</a>. Domains on the CNAME setup (partial) are not using Cloudflare authoritative nameservers.</p>
<h3 id="domain-ownership">Domain ownership</h3>
<p>Enterprise customers can use <a href="/fundamentals/account/account-security/zone-holds/">zone holds</a> to prevent other teams in the organization from adding zones that are already active in another Cloudflare account. For CNAME setups (partial), if the same zone is added to different accounts, the last account to complete the setup will gain ownership.</p>
