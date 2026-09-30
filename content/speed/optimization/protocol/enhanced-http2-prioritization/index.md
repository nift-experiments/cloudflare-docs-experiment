---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/
  description: Improve page load order with Enhanced HTTP/2 Prioritization.
  full_title: Enhanced HTTP/2 Prioritization · Cloudflare Speed docs
  head_html: <title>Enhanced HTTP/2 Prioritization · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Improve page load order with Enhanced HTTP/2 Prioritization."><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/index.md"><meta property="og:title" content="Enhanced HTTP/2 Prioritization · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Improve page load order with Enhanced HTTP/2 Prioritization."><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/#page","headline":"Enhanced HTTP/2 Prioritization \u00b7 Cloudflare Speed docs","description":"Improve page load order with Enhanced HTTP/2 Prioritization.","url":"https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/protocol/enhanced-http2-prioritization/
  schema: 1
---
<p>With Enhanced HTTP/2 Prioritization, Cloudflare delivers resources in the optimal order for the fastest experience across all browsers. It also supports control of content delivery when used in conjunction with <a href="/workers/">Workers</a>.</p>
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
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="how-it-works">How it works</h2>
<p>The speed of loading web content, from the user’s perspective, is dependent on the order in which the resources load. With HTTP/2, by default, Cloudflare will follow the order requested by the browser. This ordering varies from browser to browser, causing a significant difference in performance.</p>
<p>With Enhanced HTTP/2 Prioritization, Cloudflare overrides the default browser behavior to optimize the order of resource delivery, independent of the browser. The greatest improvements will be experienced by visitors using Safari and Edge browsers.</p>
<p>For more details, refer to <a href="https://blog.cloudflare.com/better-http-2-prioritization-for-a-faster-web/">the introductory blog post</a>.</p>
<h2 id="enable-enhanced-http-2-prioritization">Enable Enhanced HTTP/2 Prioritization</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13920.md")
</div></div>
