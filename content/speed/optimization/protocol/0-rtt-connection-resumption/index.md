---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/protocol/0-rtt-connection-resumption/
  description: Resume TLS connections faster with zero round-trip time.
  full_title: 0-RTT Connection Resumption · Cloudflare Speed docs
  head_html: <title>0-RTT Connection Resumption · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Resume TLS connections faster with zero round-trip time."><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/protocol/0-rtt-connection-resumption/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/protocol/0-rtt-connection-resumption/index.md"><meta property="og:title" content="0-RTT Connection Resumption · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resume TLS connections faster with zero round-trip time."><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/protocol/0-rtt-connection-resumption/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/optimization/protocol/0-rtt-connection-resumption/#page","headline":"0-RTT Connection Resumption \u00b7 Cloudflare Speed docs","description":"Resume TLS connections faster with zero round-trip time.","url":"https://developers.cloudflare.com/speed/optimization/protocol/0-rtt-connection-resumption/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/protocol/0-rtt-connection-resumption/
  schema: 1
---
<p>Zero round trip time resumption (0-RTT) improves performance for clients who have previously connected to your website, reducing latency for returning users. This feature is especially beneficial for those who frequently visit your application or connect over mobile networks.</p>
<p>We support 0-RTT for GET, HEAD, and OPTIONS requests, facilitating faster responses for these types of requests. Note that 0-RTT is not supported for POST requests.</p>
<p>In line with 0-RTT standards, we add the <code>Early-Data: 1</code> header to 0-RTT requests, which allows origin servers to identify when a request has used 0-RTT resumption. Customers should be able to see the <code>Early-Data: 1</code> header for any 0-RTT requests connecting to their origin.</p>
<p>For more information on 0-RTT, including its functionality and potential limitations, refer to our <a href="https://blog.cloudflare.com/even-faster-connection-establishment-with-quic-0-rtt-resumption/">blog post</a>.</p>
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
<h2 id="enable-0-rtt-connection-resumption">Enable 0-RTT Connection Resumption</h2>
<p>By default, 0-RTT Connection Resumption is not enabled on your Cloudflare application.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13924.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13921.md")
</aside>
