---
cp9:
  canonical: https://developers.cloudflare.com/images/get-started/key-concepts/
  description: Definitions of core Cloudflare Images terms including transformations, variants, hosted images, and origins.
  full_title: Key concepts · Cloudflare Images docs
  head_html: <title>Key concepts · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Definitions of core Cloudflare Images terms including transformations, variants, hosted images, and origins."><link rel="canonical" href="https://developers.cloudflare.com/images/get-started/key-concepts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/get-started/key-concepts/index.md"><meta property="og:title" content="Key concepts · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Definitions of core Cloudflare Images terms including transformations, variants, hosted images, and origins."><meta property="og:url" content="https://developers.cloudflare.com/images/get-started/key-concepts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/get-started/key-concepts/#page","headline":"Key concepts \u00b7 Cloudflare Images docs","description":"Definitions of core Cloudflare Images terms including transformations, variants, hosted images, and origins.","url":"https://developers.cloudflare.com/images/get-started/key-concepts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/get-started/key-concepts/
  schema: 1
---
<p>Here is a summary of the key terms that we use throughout our guides.</p>
<table>
<thead>
<tr>
<th>Term</th>
<th>What this means</th>
</tr>
</thead>
<tbody>
<tr>
<td>Remote image</td>
<td>An image that is stored outside of Images storage, including images in <a href="/r2/">R2</a>.</td>
</tr>
<tr>
<td>Transformation</td>
<td>A request to optimize a remote image that is stored outside of Images.</td>
</tr>
<tr>
<td>Origin</td>
<td><p>The location where your image is stored.</p><p>When you optimize a remote image, Cloudflare will pull the original image from the origin and store it in cache.</p></td>
</tr>
<tr>
<td>Hosted image</td>
<td><p>An image that is stored in Images.</p><p>Cloudflare dynamically serves copies of your original image, optimized based on your requirements.</p></td>
</tr>
<tr>
<td>Parameter / Option</td>
<td><p>A parameter is a type of optimization that you can perform on an image.</p><p>An option is the value for the parameter.</p><p>For example, you can set the <code>width</code> parameter to a value of <code>100</code> to resize an image to a width of 100.</p></td>
</tr>
<tr>
<td>Variant</td>
<td><p>A predefined way to specify how a hosted image should be resized.</p><p>For example, you can create a variant called &quot;thumbnail&quot; that sets image dimensions to 100x100.</p><p>When you serve images with this variant, Cloudflare will serve a version of the original image that is resized to 100x100.</p><p>Predefined variants specify a limited set of parameters: <code>width</code>, <code>height</code>, <code>fit</code>, and <code>blur</code>.</p></td>
</tr>
</tbody>
</table>
