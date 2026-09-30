---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-secondary/
  description: If you initially configured a full setup you can later convert your zone to use incoming zone transfers (Cloudflare as secondary).
  full_title: Convert full setup to secondary setup · Cloudflare DNS docs
  head_html: <title>Convert full setup to secondary setup · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="If you initially configured a full setup you can later convert your zone to use incoming zone transfers (Cloudflare as secondary)."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-secondary/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-secondary/index.md"><meta property="og:title" content="Convert full setup to secondary setup · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="If you initially configured a full setup you can later convert your zone to use incoming zone transfers (Cloudflare as secondary)."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-secondary/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-secondary/#page","headline":"Convert full setup to secondary setup \u00b7 Cloudflare DNS docs","description":"If you initially configured a full setup you can later convert your zone to use incoming zone transfers (Cloudflare as secondary).","url":"https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-secondary/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/conversions/convert-full-to-secondary/
  schema: 1
---
<p>If you initially configured a <a href="/dns/zone-setups/full-setup/">primary setup (full)</a>, you can later convert your zone to use <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/">incoming zone transfers (Cloudflare as secondary)</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="subdomain-setup">Subdomain setup</h3>
@markup("md", "content/.markup/bodies/7989.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-dns-conversion-subdomain-setup-callout-mdx-1">Meaning you have one or more subdomains (`sub.example.com`) added to Cloudflare as their own zone, separate from your apex domain (`example.com`).</li></ol></section>
<p>Follow the steps below to achieve this conversion.</p>
<h2 id="1-prepare-dns-records"><ol>
<li>Prepare DNS records</li>
</ol></h2>
<ol>
<li><a href="/dns/manage-dns-records/how-to/import-and-export/#export-records">Export a zone file</a>.</li>
<li>Import the zone file into your new primary DNS provider.</li>
<li>At your Cloudflare zone, use the <a href="/api/resources/dns/subresources/settings/subresources/zone/methods/edit/">Update DNS Settings</a> endpoint to enable <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">secondary DNS overrides</a>. Set the value for <code>secondary_overrides</code> to <code>true</code>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7988.md")
</aside>
<h2 id="2-prepare-the-zone-transfers"><ol start="2">
<li>Prepare the zone transfers</li>
</ol></h2>
<ol>
<li>Make adjustments to DNSSEC according to your option for <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/">DNSSEC with secondary setup</a>.</li>
<li>(Optional) Create a Transaction Signature (TSIG).</li>
</ol>
<p>A Transaction Signature (TSIG) authenticates communication between a primary and secondary DNS server.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7986.md")
</aside>
<p>While optional, this step is highly recommended.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7992.md")
</div></div>
<ol start="3">
<li>Create a peer server.</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7995.md")
</div></div>
<h2 id="3-convert-the-zone-and-initiate-zone-transfers"><ol start="3">
<li>Convert the zone and initiate zone transfers</li>
</ol></h2>
<ol>
<li>Use the <a href="/api/resources/zones/methods/edit/">Edit Zone endpoint</a> with <code>type</code> set to <code>secondary</code> to convert the zone type. The existing records will remain in place.</li>
<li>In the Cloudflare dashboard, go to the <strong>DNS Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select <strong>Manage linked peers</strong> under <strong>DNS Zone Transfers</strong>.</li>
<li>Link the peer server you created in the previous steps and select <strong>Save</strong>.</li>
<li>Back on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page, select <strong>Initiate zone transfer</strong>.</li>
<li>Confirm the DNS records are transferring as expected.</li>
<li>Go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page and take note of your new <strong>Cloudflare Nameservers</strong>.</li>
<li>At your domain registrar (or parent zone), <a href="/dns/nameservers/update-nameservers/">update your nameservers</a> to include the <code>secondary.cloudflare.com</code> nameservers.</li>
</ol>
