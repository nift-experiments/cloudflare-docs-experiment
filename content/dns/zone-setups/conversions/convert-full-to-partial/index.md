---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-partial/
  description: Convert a full DNS setup to a partial CNAME setup.
  full_title: Convert full setup to partial setup · Cloudflare DNS docs
  head_html: <title>Convert full setup to partial setup · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Convert a full DNS setup to a partial CNAME setup."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-partial/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-partial/index.md"><meta property="og:title" content="Convert full setup to partial setup · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Convert a full DNS setup to a partial CNAME setup."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-partial/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-partial/#page","headline":"Convert full setup to partial setup \u00b7 Cloudflare DNS docs","description":"Convert a full DNS setup to a partial CNAME setup.","url":"https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-partial/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/conversions/convert-full-to-partial/
  schema: 1
---
<p>If you initially configured a <a href="/dns/zone-setups/full-setup/">primary setup (full)</a>, you can later convert your zone to use a CNAME setup (also known as partial setup). This guide assumes your zone is already in an <a href="/dns/zone-setups/reference/domain-status/#active">active status</a>.</p>
<p>A CNAME setup allows you to use <a href="/fundamentals/concepts/how-cloudflare-works/">Cloudflare's reverse proxy</a> on individual subdomains while using a different authoritative DNS provider.</p>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<h3 id="consider-cname-setup-limitations">Consider CNAME setup limitations</h3>
<ul>
<li>A CNAME setup requires a CNAME record for each proxied hostname but, following <a href="https://datatracker.ietf.org/doc/html/rfc1912#section-2.4">RFC 1912</a>, CNAME records are not allowed on the zone apex (<code>example.com</code>). With a CNAME setup, you can only proxy the zone apex if your authoritative DNS provider supports <a href="https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/">CNAME flattening</a> (or an equivalent like ALIAS/ANAME records), or if you create A/AAAA records pointing the apex directly to Cloudflare <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IP addresses</a>. Otherwise, you can only proxy subdomains.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7998.md")
</aside>
<ul>
<li>Once your zone is using CNAME setup, on the dashboard, you will only be able to create A, AAAA, and CNAME records, which are the DNS record types that can be <a href="/dns/proxy-status/">proxied</a>.</li>
</ul>
<h3 id="plan-for-ssl-tls-certificates">Plan for SSL/TLS certificates</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="universal-ssl-deletion">Universal SSL deletion</h3>
@markup("md", "content/.markup/bodies/7997.md")
</aside>
<p>New Universal SSL certificates will be <a href="/ssl/edge-certificates/universal-ssl/enable-universal-ssl/#partial-dns-setup">provisioned</a> for your proxied subdomains only after each CNAME record pointing to <code>{your-hostname}.cdn.cloudflare.net</code> is in place, and domain ownership is verified with the TXT record, as <a href="#2-convert-the-zone">explained below</a>.</p>
<p>To avoid downtime, replace your Universal SSL certificates with an <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificate</a>, which will persist during the transition. After the conversion, you can optionally configure <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/#setup">delegated DCV</a>.</p>
<hr />
<h2 id="1-prepare-new-dns-provider"><ol>
<li>Prepare new DNS provider</li>
</ol></h2>
<ol>
<li>Export a zone file</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8001.md")
</div></div>
<ol start="2">
<li>
<p>Import the zone file into your new primary DNS provider.</p>
</li>
<li>
<p>At your new authoritative DNS provider, create or update records so that you have CNAME records pointing to <code>{your-hostname}.cdn.cloudflare.net</code> for every hostname you wish to proxy through Cloudflare.</p>
<details class="nb-details"><summary>Example CNAME record at authoritative DNS provider</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/8002.md")
</div></details>
<h2 id="2-convert-the-zone"><ol start="2">
<li>Convert the zone</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8007.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7996.md")
</aside>
<h2 id="3-update-your-nameservers"><ol start="3">
<li>Update your nameservers</li>
</ol></h2>
<p>Update the nameservers at your domain registrar to point to your new authoritative DNS provider. Make sure to remove the Cloudflare nameservers.</p>
<h2 id="4-clean-up-dns-records-on-cloudflare"><ol start="4">
<li>Clean up DNS records on Cloudflare</li>
</ol></h2>
<p>In Cloudflare, remove all records that are not of type A, AAAA, or CNAME, and also remove any A, AAAA, or CNAME records for hostnames you do not want to proxy after the conversion. After this cleanup, only the A, AAAA, or CNAME records for hostnames you want to proxy should remain in Cloudflare, and those same hostnames should have CNAME records pointing to <code>{your-hostname}.cdn.cloudflare.net</code> at your new authoritative DNS provider.</p>
