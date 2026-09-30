---
cp9:
  canonical: https://developers.cloudflare.com/dns/cname-flattening/
  description: Resolve CNAME records at the zone apex to comply with DNS standards.
  full_title: CNAME flattening · Cloudflare DNS docs
  head_html: <title>CNAME flattening · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve CNAME records at the zone apex to comply with DNS standards."><link rel="canonical" href="https://developers.cloudflare.com/dns/cname-flattening/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/cname-flattening/index.md"><meta property="og:title" content="CNAME flattening · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve CNAME records at the zone apex to comply with DNS standards."><meta property="og:url" content="https://developers.cloudflare.com/dns/cname-flattening/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/cname-flattening/#page","headline":"CNAME flattening \u00b7 Cloudflare DNS docs","description":"Resolve CNAME records at the zone apex to comply with DNS standards.","url":"https://developers.cloudflare.com/dns/cname-flattening/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/cname-flattening/
  schema: 1
---
<p>CNAME flattening speeds up CNAME resolution and allows you to use a <a href="/dns/manage-dns-records/reference/dns-record-types/#cname">CNAME record</a> at your <span class="nb-glossary-tooltip" title="zone apex">zone apex</span> (<code>example.com</code>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7718.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>With CNAME flattening, Cloudflare finds the IP address that a CNAME points to. This process could involve a single lookup or multiple (if your CNAME points to another CNAME). Cloudflare then returns the final IP address instead of a CNAME record, helping DNS queries resolve faster.</p>
<p>For more details on the steps involved in CNAME flattening, review the <a href="/dns/cname-flattening/cname-flattening-diagram/">CNAME flattening diagram</a> and refer to the <a href="https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/">Cloudflare blog post</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7717.md")
</aside>
<h2 id="aspects-to-keep-in-mind">Aspects to keep in mind</h2>
<ul>
<li>CNAME flattening happens by default in some cases. Refer to <a href="/dns/cname-flattening/set-up-cname-flattening/">Setup</a> for details.</li>
<li>CNAME to a different Cloudflare account is prohibited and will result in <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/">Error 1014: CNAME Cross-User Banned</a></li>
<li></li>
</ul>
<p>If a CNAME target is being used to verify a domain for a third-party service, turning on <a href="/dns/cname-flattening/set-up-cname-flattening/#for-all-cname-records">CNAME flattening for all CNAME records</a> may cause the verification to fail since the CNAME record itself will not be returned directly.</p>
<ul>
<li>If the final CNAME target has no A/AAAA records (a dangling CNAME), CNAME flattening returns an empty response (NODATA) because there is no IP address to flatten to. This can make it appear as if the DNS record is not propagating. Ensure your CNAME targets resolve to valid A/AAAA records.</li>
</ul>
