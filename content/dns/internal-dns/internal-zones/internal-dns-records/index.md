---
cp9:
  canonical: https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/
  description: Manage internal DNS records in Cloudflare. Learn about supported DNS record types and CNAME flattening.
  full_title: Manage internal DNS records · Cloudflare DNS docs
  head_html: <title>Manage internal DNS records · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage internal DNS records in Cloudflare. Learn about supported DNS record types and CNAME flattening."><link rel="canonical" href="https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/index.md"><meta property="og:title" content="Manage internal DNS records · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage internal DNS records in Cloudflare. Learn about supported DNS record types and CNAME flattening."><meta property="og:url" content="https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/#page","headline":"Manage internal DNS records \u00b7 Cloudflare DNS docs","description":"Manage internal DNS records in Cloudflare. Learn about supported DNS record types and CNAME flattening.","url":"https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /dns/internal-dns/internal-zones/internal-dns-records/
  schema: 1
---
<p>Internal zones can contain the same <a href="/dns/manage-dns-records/reference/dns-record-types/">DNS record types</a> that Cloudflare supports for public zones.</p>
<p>You can manage internal DNS records in the same way as you would manage public DNS records, with the difference that <a href="/dns/proxy-status/">proxy status</a> does not apply to internal DNS records.</p>
<p>Refer to <a href="/dns/manage-dns-records/how-to/create-dns-records/">Manage DNS records</a> or to the <a href="/api/resources/dns/subresources/records/">API documentation</a> for further guidance.</p>
<h2 id="cname-flattening-in-internal-dns">CNAME flattening in Internal DNS</h2>
<p>With <a href="/dns/cname-flattening/">CNAME flattening</a>, Cloudflare finds the final target content that a CNAME points to and then returns this content instead of a CNAME record. With Internal DNS, CNAME flattening is applied by default and cannot be turned off.</p>
<p>Cloudflare will try to flatten the CNAME record considering both the specified <a href="/dns/internal-dns/dns-views/">DNS view</a> and any existing <a href="/dns/internal-dns/internal-zones/reference-zones/">reference zones</a>. If the reference zone then has another CNAME, the record will again be considered from the perspective of the original view.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7760.md")
</div></details>
<p>If it is not possible to flatten the CNAME record, the following will happen:</p>
<ol>
<li>The CNAME record is returned to <a href="/dns/internal-dns/#architecture-overview">Gateway resolver</a> as-is.</li>
<li>Gateway resolver will process the returned record, depending on the <strong>Fallback through public DNS</strong> configuration:
<ul>
<li>On: Gateway will try to resolve the query by sending it to Cloudflare's public DNS resolver (<a href="/1.1.1.1/">1.1.1.1</a>).</li>
<li>Off: Gateway will return the response as-is to the client.</li>
</ul>
</li>
</ol>
