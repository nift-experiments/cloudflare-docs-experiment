---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/protocol/http3/
  description: Serve content over HTTP/3 with QUIC for faster connections.
  full_title: HTTP/3 (with QUIC) · Cloudflare Speed docs
  head_html: <title>HTTP/3 (with QUIC) · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Serve content over HTTP/3 with QUIC for faster connections."><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/protocol/http3/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/protocol/http3/index.md"><meta property="og:title" content="HTTP/3 (with QUIC) · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Serve content over HTTP/3 with QUIC for faster connections."><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/protocol/http3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Speed"><meta name="pcx_tags" content="QUIC"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/optimization/protocol/http3/#page","headline":"HTTP/3 (with QUIC) \u00b7 Cloudflare Speed docs","description":"Serve content over HTTP/3 with QUIC for faster connections.","url":"https://developers.cloudflare.com/speed/optimization/protocol/http3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["QUIC"]}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/protocol/http3/
  schema: 1
---
<p>HTTP/3 uses QUIC, which is a secure-by-default transport protocol. HTTP/3 improves page load times in a similar way to HTTP/2. However, the QUIC transport protocol solves TCP's head-of-line blocking problem, meaning that performance over lossy networks can be better.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13906.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13905.md")
</aside>
<h2 id="availability">Availability</h2>
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
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="enable-http-3">Enable HTTP/3</h2>
<p>HTTP/3 is available to all plans (though it does require an <a href="/ssl/get-started/">SSL certificate at Cloudflare’s edge network</a>).</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13909.md")
</div></div>
