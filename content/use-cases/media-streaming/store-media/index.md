---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/media-streaming/store-media/
  description: Store media files with zero egress fees using R2.
  full_title: Store media at scale · Cloudflare use cases
  head_html: <title>Store media at scale · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Store media files with zero egress fees using R2."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/media-streaming/store-media/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/media-streaming/store-media/index.md"><meta property="og:title" content="Store media at scale · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Store media files with zero egress fees using R2."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/media-streaming/store-media/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,R2,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/media-streaming/store-media/#page","headline":"Store media at scale \u00b7 Cloudflare use cases","description":"Store media files with zero egress fees using R2.","url":"https://developers.cloudflare.com/use-cases/media-streaming/store-media/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/media-streaming/store-media/
  schema: 1
---
<p>Media files are large, and egress fees from traditional cloud storage can be significant at scale. Cloudflare R2 provides S3-compatible object storage with zero egress fees, and Workers lets you build custom processing pipelines for validation, transformation, and routing.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="r2">R2</h3>
<p>S3-compatible object storage with zero egress fees. <a href="/r2/">Learn more about R2</a>.</p>
<ul>
<li><strong>Zero egress fees</strong> - No charges for data transferred out, regardless of volume</li>
<li><strong>S3 compatibility</strong> - Use any S3-compatible tool, SDK, or library without code changes</li>
<li><strong>Direct uploads</strong> - Issue presigned URLs so clients upload directly to R2 without routing through your servers</li>
</ul>
<h3 id="workers">Workers</h3>
<p>Build and deploy serverless applications on Cloudflare's global network. <a href="/workers/">Learn more about Workers</a>.</p>
<ul>
<li><strong>Custom processing pipelines</strong> - Build media transformation, validation, and routing logic that runs at the edge</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/r2/get-started/">R2 get started</a></li>
<li><a href="/r2/api/s3/presigned-urls/">Generate presigned URLs</a></li>
<li><a href="/workers/get-started/">Workers get started</a></li>
</ol>
