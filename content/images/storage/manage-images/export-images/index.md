---
cp9:
  canonical: https://developers.cloudflare.com/images/storage/manage-images/export-images/
  description: Download the original version of images stored in Cloudflare Images via the dashboard or API.
  full_title: Export images · Cloudflare Images docs
  head_html: <title>Export images · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Download the original version of images stored in Cloudflare Images via the dashboard or API."><link rel="canonical" href="https://developers.cloudflare.com/images/storage/manage-images/export-images/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/storage/manage-images/export-images/index.md"><meta property="og:title" content="Export images · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Download the original version of images stored in Cloudflare Images via the dashboard or API."><meta property="og:url" content="https://developers.cloudflare.com/images/storage/manage-images/export-images/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/storage/manage-images/export-images/#page","headline":"Export images \u00b7 Cloudflare Images docs","description":"Download the original version of images stored in Cloudflare Images via the dashboard or API.","url":"https://developers.cloudflare.com/images/storage/manage-images/export-images/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/storage/manage-images/export-images/
  schema: 1
---
<p>Cloudflare Images supports image exports via the Cloudflare dashboard and API which allows you to get the original version of your image.</p>
<h2 id="export-images-via-the-cloudflare-dashboard">Export images via the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the image or images you want to export.</li>
<li>To export a single image, select <strong>Export</strong> from its menu. To export several images, select the checkbox next to each image and then select <strong>Export selected</strong>.</li>
</ol>
<p>Your images are downloaded to your machine.</p>
<h2 id="export-images-via-the-api">Export images via the API</h2>
<p>Make a <code>GET</code> request as shown in the example below. <code>&lt;IMAGE_ID&gt;</code> must be fully URL encoded in the API call URL.</p>
<p><code>GET accounts/&lt;ACCOUNT_ID&gt;/images/v1/&lt;IMAGE_ID&gt;/blob</code></p>
