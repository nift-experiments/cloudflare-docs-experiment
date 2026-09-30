---
cp9:
  canonical: https://developers.cloudflare.com/bots/additional-configurations/detection-ids/scraping-detections/
  description: Detection IDs for identifying volumetric scraping attacks by ASN and fingerprint.
  full_title: Scraping detections · Cloudflare bot solutions docs
  head_html: <title>Scraping detections · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Detection IDs for identifying volumetric scraping attacks by ASN and fingerprint."><link rel="canonical" href="https://developers.cloudflare.com/bots/additional-configurations/detection-ids/scraping-detections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/additional-configurations/detection-ids/scraping-detections/index.md"><meta property="og:title" content="Scraping detections · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Detection IDs for identifying volumetric scraping attacks by ASN and fingerprint."><meta property="og:url" content="https://developers.cloudflare.com/bots/additional-configurations/detection-ids/scraping-detections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Bots"><meta name="pcx_tags" content="Scraping"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/additional-configurations/detection-ids/scraping-detections/#page","headline":"Scraping detections \u00b7 Cloudflare bot solutions docs","description":"Detection IDs for identifying volumetric scraping attacks by ASN and fingerprint.","url":"https://developers.cloudflare.com/bots/additional-configurations/detection-ids/scraping-detections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Scraping"]}</script>
  markdown: true
  noindex: false
  route: /bots/additional-configurations/detection-ids/scraping-detections/
  schema: 1
---
<p>Scraping behavioral detection IDs allow you to better protect your website from volumetric scraping attacks by identifying anomalous behavior. The detection IDs below are specifically designed to catch suspicious scraping activity at the zone level.</p>
<table>
<thead>
<tr>
<th><span style="width:100px">Detection ID</span></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>50331648</code></td>
<td>Observes patterns of requests sent to your zone, dynamically analyzing behavior by ASN.</td>
</tr>
<tr>
<td><code>50331649</code></td>
<td>Observes patterns of requests sent to your zone, dynamically analyzing behavior by JA4 fingerprint.</td>
</tr>
</tbody>
</table>
<h2 id="challenges-for-scraping-detections">Challenges for scraping detections</h2>
<p>Cloudflare's <a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">Managed Challenge</a> can limit scraping attacks on your website.</p>
<p>To access scraping detections:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3547.md")
</div>
<pre tabindex="0"><code class="language-js">&#10;(any(cf.bot_management.detection_ids[*] in {50331648 50331649}) and not cf.bot_management.verified_bot)&#10;</code></pre>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="best-practice">Best practice</h3>
@markup("md", "content/.markup/bodies/3546.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3545.md")
</aside>
