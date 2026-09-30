---
cp9:
  canonical: https://developers.cloudflare.com/images/polish/
  description: Cloudflare Polish automatically optimizes images by stripping metadata and applying lossy or lossless compression.
  full_title: Cloudflare Polish · Cloudflare Images docs
  head_html: <title>Cloudflare Polish · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare Polish automatically optimizes images by stripping metadata and applying lossy or lossless compression."><link rel="canonical" href="https://developers.cloudflare.com/images/polish/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/polish/index.md"><meta property="og:title" content="Cloudflare Polish · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare Polish automatically optimizes images by stripping metadata and applying lossy or lossless compression."><meta property="og:url" content="https://developers.cloudflare.com/images/polish/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/polish/#page","headline":"Cloudflare Polish \u00b7 Cloudflare Images docs","description":"Cloudflare Polish automatically optimizes images by stripping metadata and applying lossy or lossless compression.","url":"https://developers.cloudflare.com/images/polish/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/polish/
  schema: 1
---
<p>Cloudflare Polish is a one-click image optimization product that automatically optimizes images in your site. Polish strips metadata from images and reduces image size through lossy or lossless compression to accelerate the speed of image downloads.</p>
<p>When an image is fetched from your origin, our systems automatically optimize it in Cloudflare's cache. Subsequent requests for the same image will get the smaller, faster, optimized version of the image, improving the speed of your website.</p>
<p><img src="/assets/upstream/images/images/polish.png" alt="Example of Polish compression's quality." /></p>
<h2 id="comparison">Comparison</h2>
<ul>
<li><b>Polish</b> automatically optimizes all images served from your origin
server. It keeps the same image URLs, and does not require changing markup of
your pages.</li>
<li><b>Cloudflare Images</b> API allows you to create new images with resizing,
cropping, watermarks, and other processing applied. These images get their own
new URLs, and you need to embed them on your pages to take advantage of this
service. Images created this way are already optimized, and there is no need
to apply Polish to them.</li>
</ul>
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
