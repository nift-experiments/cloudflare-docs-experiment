---
cp9:
  canonical: https://developers.cloudflare.com/network/ip-geolocation/
  description: Add visitor country information via the CF-IPCountry header.
  full_title: IP geolocation · Cloudflare Network settings docs
  head_html: <title>IP geolocation · Cloudflare Network settings docs</title><meta name="generator" content="Nift"><meta name="description" content="Add visitor country information via the CF-IPCountry header."><link rel="canonical" href="https://developers.cloudflare.com/network/ip-geolocation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network/ip-geolocation/index.md"><meta property="og:title" content="IP geolocation · Cloudflare Network settings docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add visitor country information via the CF-IPCountry header."><meta property="og:url" content="https://developers.cloudflare.com/network/ip-geolocation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network"><meta name="algolia_product_filter" content="Network"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Network"><meta name="pcx_tags" content="Geolocation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network/ip-geolocation/#page","headline":"IP geolocation \u00b7 Cloudflare Network settings docs","description":"Add visitor country information via the CF-IPCountry header.","url":"https://developers.cloudflare.com/network/ip-geolocation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Geolocation"]}</script>
  markdown: true
  noindex: false
  route: /network/ip-geolocation/
  schema: 1
---
<p>IP geolocation adds the <a href="/fundamentals/reference/http-headers/#cf-ipcountry"><code>CF-IPCountry</code> header</a> to all requests to your origin server.</p>
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
<h2 id="add-ip-geolocation-information">Add IP geolocation information</h2>
<p>The recommended procedure to enable IP geolocation information is to <a href="/rules/transform/managed-transforms/reference/#add-visitor-location-headers">enable the <strong>Add visitor location headers</strong> Managed Transform</a>. This Managed Transform adds HTTP request headers with location information for the visitor's IP address, such as city, country, continent, longitude, and latitude.</p>
<p>If you only want the request header for the visitor's country, you can enable <strong>IP Geolocation</strong>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/685.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/682.md")
</aside>
<hr />
<h2 id="accuracy-and-limitations">Accuracy and limitations</h2>
<p>IP geolocation is an estimate, not an exact science. There is nothing that inherently binds an IP address to a physical location or country. Because IP addresses rotate and ownership can change, the data is dynamic and may shift over time.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/681.md")
</aside>
<p>Here is what you can expect regarding data accuracy and updates:</p>
<ul>
<li><strong>Update frequency</strong>: Cloudflare automatically updates its IP geolocation database multiple times per week.</li>
<li><strong>Processing time</strong>: Cloudflare reviews correction requests, which may or may not result in a change. Confirmed changes generally take effect within a few business days.</li>
<li><strong>Accuracy</strong>: Due to the dynamic nature of IP address allocation, Cloudflare cannot guarantee that its IP geolocation will align with other providers. Cloudflare does not provide SLAs for IP geolocation accuracy or the timing of updates.</li>
</ul>
<hr />
<h2 id="report-an-incorrect-ip-location">Report an incorrect IP location</h2>
<p>If you find an IP address with a location that you believe is incorrect, fill in the <a href="https://www.cloudflare.com/lp/ip-corrections/">data correction form</a> with the relevant IP address range(s) along with the correct information as applicable (country, state/province, city name, and ZIP code).</p>
<p>If the data is confirmed, Cloudflare will make the necessary changes, generally within a few business days.</p>
<p>If Cloudflare cannot confirm the submitted location, the correction does not result in a change.</p>
<p>If an end user's IP address rotates frequently, for example on mobile or CGNAT networks, the address may change again before the correction completes.</p>
