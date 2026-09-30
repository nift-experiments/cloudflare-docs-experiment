---
cp9:
  canonical: https://developers.cloudflare.com/network-error-logging/how-to/
  description: NEL reports show you why a request failed, the country a request failed from, and last mile network a request failed from, and the likely intended Cloudflare data center.
  full_title: View Reports · Cloudflare Network Error Logging docs
  head_html: <title>View Reports · Cloudflare Network Error Logging docs</title><meta name="generator" content="Nift"><meta name="description" content="NEL reports show you why a request failed, the country a request failed from, and last mile network a request failed from, and the likely intended Cloudflare data center."><link rel="canonical" href="https://developers.cloudflare.com/network-error-logging/how-to/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-error-logging/how-to/index.md"><meta property="og:title" content="View Reports · Cloudflare Network Error Logging docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="NEL reports show you why a request failed, the country a request failed from, and last mile network a request failed from, and the likely intended Cloudflare data center."><meta property="og:url" content="https://developers.cloudflare.com/network-error-logging/how-to/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Error Logging"><meta name="algolia_product_filter" content="Network Error Logging"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Network Error Logging"><meta name="pcx_tags" content="Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-error-logging/how-to/#page","headline":"View Reports \u00b7 Cloudflare Network Error Logging docs","description":"NEL reports show you why a request failed, the country a request failed from, and last mile network a request failed from, and the likely intended Cloudflare data center.","url":"https://developers.cloudflare.com/network-error-logging/how-to/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging"]}</script>
  markdown: true
  noindex: false
  route: /network-error-logging/how-to/
  schema: 1
---
<p>Use NEL reports to view information such as:</p>
<ul>
<li>Why a request failed</li>
<li>The country a request failed from</li>
<li>The last mile network a request failed from</li>
<li>The Cloudflare data center the request was most likely meant for</li>
</ul>
<ol>
<li>Log in to your Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Analytics &amp; Logs</strong> &gt; <strong>Edge Reachability</strong>.</li>
</ol>
<p>Click a tab under <strong>Reachability summary</strong> to view specific information related to your Origin ASN, Origin, IP, or data center. Hover over a location on the map to view the number of reachable requests.</p>
<p>Under <strong>Reachability by data center</strong>, click a location under Data Centers to filter reachability by a specific location.</p>
<p>To view the log fields available for NEL, refer to <a href="/logs/logpush/logpush-job/datasets/zone/nel_reports/">NEL reports</a>.</p>
