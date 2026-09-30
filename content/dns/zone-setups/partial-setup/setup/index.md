---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/
  description: A CNAME setup (also known as partial) allows you to use Cloudflare's reverse proxy while maintaining your primary and authoritative DNS provider.
  full_title: Set up a partial zone (CNAME setup) · Cloudflare DNS docs
  head_html: <title>Set up a partial zone (CNAME setup) · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="A CNAME setup (also known as partial) allows you to use Cloudflare&#x27;s reverse proxy while maintaining your primary and authoritative DNS provider."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/index.md"><meta property="og:title" content="Set up a partial zone (CNAME setup) · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A CNAME setup (also known as partial) allows you to use Cloudflare&#x27;s reverse proxy while maintaining your primary and authoritative DNS provider."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/#page","headline":"Set up a partial zone (CNAME setup) \u00b7 Cloudflare DNS docs","description":"A CNAME setup (also known as partial) allows you to use Cloudflare's reverse proxy while maintaining your primary and authoritative DNS provider.","url":"https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/partial-setup/setup/
  schema: 1
---
<p>A CNAME setup (also known as partial setup) allows you to use <a href="/fundamentals/concepts/how-cloudflare-works/">Cloudflare's reverse proxy</a> while maintaining your primary and authoritative DNS provider.</p>
<p>Use this option to <span class="nb-glossary-tooltip" title="proxy status">proxy</span> only individual subdomains through Cloudflare when you cannot change your authoritative DNS provider. You will be able to create A, AAAA, and CNAME records, which are the DNS record types that can be <a href="/dns/proxy-status/">proxied</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/7926.md")
</aside>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7928.md")
</div>
<h2 id="1-convert-your-zone-and-review-dns-records"><ol>
<li>Convert your zone and review DNS records</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7932.md")
</div></div>
<h2 id="2-verify-ownership-for-your-domain"><ol start="2">
<li>Verify ownership for your domain</li>
</ol></h2>
<p>Add the <strong>Verification TXT Record</strong> at your authoritative DNS provider. Cloudflare will verify the TXT record and send a confirmation email. This can take up to a few hours.</p>
<details class="nb-details"><summary>Example verification record</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7933.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7924.md")
</aside>
<p>The verification record must remain in place for as long as your domain is active on a CNAME setup on Cloudflare.</p>
<p>If your organization has multiple Cloudflare accounts, also consider using zone holds to have more control over <a href="/dns/zone-setups/partial-setup/#domain-ownership">domain ownership</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7923.md")
</aside>
<h2 id="3-add-dns-records"><ol start="3">
<li>Add DNS records</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7935.md")
</div>
<hr />
<h2 id="other-record-types">Other record types</h2>
<p>If you are preparing a conversion from CNAME setup (partial) to primary setup (full), or if you have a more specific use case, you can use the <a href="/api/resources/dns/subresources/records/methods/create/">Create DNS Record</a> API endpoint to create DNS records of any supported type.</p>
