---
cp9:
  canonical: https://developers.cloudflare.com/byoip/
  description: Get Cloudflare's security and performance while using your own IPs.
  full_title: Bringing Your Own IPs to Cloudflare · Cloudflare BYOIP docs
  head_html: <title>Bringing Your Own IPs to Cloudflare · Cloudflare BYOIP docs</title><meta name="generator" content="Nift"><meta name="description" content="Get Cloudflare&#x27;s security and performance while using your own IPs."><link rel="canonical" href="https://developers.cloudflare.com/byoip/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/byoip/index.md"><meta property="og:title" content="Bringing Your Own IPs to Cloudflare · Cloudflare BYOIP docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Get Cloudflare&#x27;s security and performance while using your own IPs."><meta property="og:url" content="https://developers.cloudflare.com/byoip/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="BYOIP"><meta name="algolia_product_filter" content="BYOIP"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="BYOIP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/byoip/#page","headline":"Bringing Your Own IPs to Cloudflare \u00b7 Cloudflare BYOIP docs","description":"Get Cloudflare's security and performance while using your own IPs.","url":"https://developers.cloudflare.com/byoip/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /byoip/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/1378.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p>When you use Cloudflare as a <a href="/fundamentals/concepts/how-cloudflare-works/">reverse proxy</a>, Cloudflare responds to DNS queries for proxied records with Cloudflare-owned IP addresses<sup><a href="#footnote-1">1</a></sup>. For some organizations, it is important to keep their website or application associated with IP addresses they already own rather than using Cloudflare's.</p>
<p>With Bring Your Own IP (BYOIP), Cloudflare announces your IP prefixes in all our locations. Use your IPs with <a href="/magic-transit/">Magic Transit</a>, <a href="/spectrum/">Spectrum</a>, <a href="/cache/">CDN services</a>, or Gateway <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a>.</p>
<p>Learn how to <a href="/byoip/get-started/">get started</a>.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1379.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1380.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/1383.md")
</div>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Without BYOIP, when your domain's records are `proxied`, Cloudflare responds with a Cloudflare-owned [anycast IP address](/fundamentals/concepts/cloudflare-ip-addresses/).</li></ol></section>
