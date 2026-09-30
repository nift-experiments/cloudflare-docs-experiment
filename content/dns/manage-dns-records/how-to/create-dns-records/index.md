---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/
  description: Create, edit, and delete DNS records for your zone.
  full_title: Manage DNS records · Cloudflare DNS docs
  head_html: <title>Manage DNS records · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, edit, and delete DNS records for your zone."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/index.md"><meta property="og:title" content="Manage DNS records · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, edit, and delete DNS records for your zone."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#page","headline":"Manage DNS records \u00b7 Cloudflare DNS docs","description":"Create, edit, and delete DNS records for your zone.","url":"https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/how-to/create-dns-records/
  schema: 1
---
<p>Consider the sections below for step-by-step instructions on managing DNS records at Cloudflare.</p>
<p>To better understand what DNS records are, refer to <a href="/dns/manage-dns-records/">Overview</a>. For context around common records you want to review when getting started at Cloudflare, refer to <a href="/dns/zone-setups/full-setup/setup/#2-review-your-dns-records">review DNS records</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7843.md")
</aside>
<hr />
<h2 id="basic-operations">Basic operations</h2>
<h3 id="create-dns-records">Create DNS records</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7847.md")
</div></div>
<h3 id="edit-dns-records">Edit DNS records</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7850.md")
</div></div>
<h3 id="delete-dns-records">Delete DNS records</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7853.md")
</div></div>
<hr />
<h2 id="use-cases">Use cases</h2>
<h3 id="update-an-origin-ip-address">Update an origin IP address</h3>
<p>If your hosting provider changes or your origin IP address changes, update the <strong>Content</strong> value of the relevant DNS records (usually <code>A</code> or <code>AAAA</code> records).</p>
<p>If you are not sure which IP address to use, refer to your hosting provider's documentation.</p>
<h3 id="originless-setups">Originless setups</h3>
<p>If you need a placeholder address for an originless setup (also referred to as parked domain or redirect-only), you can use the reserved IPv6 address <code>100::</code> or the reserved IPv4 address <code>192.0.2.0</code> in a <span class="nb-glossary-tooltip" title="proxy status">proxied</span> DNS record.</p>
<p>This allows you to route requests using products such as <a href="/rules/url-forwarding/">Redirect Rules</a>, <a href="/rules/page-rules/">Page Rules</a>, or <a href="/workers/">Workers</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7842.md")
</aside>
<hr />
<h2 id="further-guidance">Further guidance</h2>
<ul class="directory-listing"><li><a href="/dns/manage-dns-records/how-to/create-dns-records/">Manage DNS records</a></li><li><a href="/dns/manage-dns-records/how-to/create-zone-apex/">Create zone apex record</a></li><li><a href="/dns/manage-dns-records/how-to/create-subdomain/">Create subdomain records</a></li><li><a href="/dns/manage-dns-records/how-to/email-records/">Set up email records</a></li><li><a href="/dns/manage-dns-records/how-to/set-up-google-workspace/">Set up Google Workspace DNS records</a></li><li><a href="/dns/manage-dns-records/how-to/import-and-export/">Import and export records</a></li><li><a href="/dns/manage-dns-records/how-to/batch-record-changes/">Batch record changes</a></li><li><a href="/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/">Dynamically update DNS records</a></li><li><a href="/dns/manage-dns-records/how-to/round-robin-dns/">Round-robin DNS</a></li><li><a href="/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/">Delegate subdomains</a></li></ul>
