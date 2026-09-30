---
cp9:
  canonical: https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/
  description: Configure CNAME flattening for your zone.
  full_title: Set up CNAME flattening · Cloudflare DNS docs
  head_html: <title>Set up CNAME flattening · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure CNAME flattening for your zone."><link rel="canonical" href="https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/index.md"><meta property="og:title" content="Set up CNAME flattening · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure CNAME flattening for your zone."><meta property="og:url" content="https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/#page","headline":"Set up CNAME flattening \u00b7 Cloudflare DNS docs","description":"Configure CNAME flattening for your zone.","url":"https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/cname-flattening/set-up-cname-flattening/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7709.md")
</aside>
<h2 id="for-your-zone-apex">For your zone apex</h2>
<p>CNAME flattening occurs by default for all plans when your domain uses a CNAME record for its zone apex (<code>example.com</code>, meaning the record <strong>Name</strong> is set to <code>@</code>).</p>
<h2 id="for-all-cname-records">For all CNAME records</h2>
<p>For zones on paid plans, you can choose to flatten all CNAME records. This option is useful for <span class="nb-glossary-tooltip" title="proxy status">DNS-only (unproxied)</span> CNAME records. <a href="/dns/proxy-status/">Proxied records</a> are flattened by default as they return Cloudflare anycast IPs.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7713.md")
</div></div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7708.md")
</aside>
<h2 id="per-record">Per record</h2>
<p>Paid zones also have the option of flattening specific CNAME records.</p>
<p>If you use this option, a special <a href="/dns/manage-dns-records/reference/record-attributes/">tag</a> <code>cf-flatten-cname</code> will be added to the respective flattened CNAME records in your zone file, allowing you to <a href="/dns/manage-dns-records/how-to/import-and-export/">export and import records</a> without losing this configuration.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7716.md")
</div></div>
