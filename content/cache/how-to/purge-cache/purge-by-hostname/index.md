---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/
  description: Purge all cached resources for a specific hostname.
  full_title: ​Purge cache by hostname · Cloudflare Cache (CDN) docs
  head_html: <title>​Purge cache by hostname · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Purge all cached resources for a specific hostname."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/index.md"><meta property="og:title" content="​Purge cache by hostname · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Purge all cached resources for a specific hostname."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/#page","headline":"\u200bPurge cache by hostname \u00b7 Cloudflare Cache (CDN) docs","description":"Purge all cached resources for a specific hostname.","url":"https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/purge-cache/purge-by-hostname/
  schema: 1
---
<p>Purging by hostname means that all assets at URLs with a host that matches one of the provided values will be instantly purged from the cache.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Purge Cache</strong>, select <strong>Custom Purge</strong>. The <strong>Custom Purge</strong> window appears.</li>
<li>Under <strong>Purge by</strong>, select <strong>Hostname</strong>.</li>
<li>Follow the syntax instructions:
<ul>
<li>One hostname per line.</li>
<li>Separated by commas.</li>
<li>You can purge up to 100 hostnames at a time.</li>
</ul>
</li>
<li>Enter the appropriate value(s) in the text field using the format shown in the example.</li>
<li>Select <strong>Purge</strong>.</li>
</ol>
<p>For information on rate limits, refer to the <a href="/cache/how-to/purge-cache/#availability-and-limits">Availability and limits</a> section.</p>
<h2 id="resulting-cache-status">Resulting cache status</h2>
<p>Purging by hostname deletes the resource, resulting in the <code>CF-Cache-Status</code> header being set to <a href="/cache/concepts/cache-responses/#miss"><code>MISS</code></a> for subsequent requests.</p>
<p>If <a href="/cache/how-to/tiered-cache/">tiered cache</a> is used, purging by hostname may return <code>EXPIRED</code>, as the lower tier tries to revalidate with the upper tier to reduce load on the latter.
Depending on whether the upper tier has the resource or not, and whether the end user is reaching the lower tier or the upper tier, <code>EXPIRED</code> or <code>MISS</code> are returned.</p>
