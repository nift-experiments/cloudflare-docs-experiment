---
cp9:
  canonical: https://developers.cloudflare.com/images/get-started/introduction/
  description: Cloudflare Images provides a platform for optimizing, storing, and serving images at scale.
  full_title: Introduction · Cloudflare Images docs
  head_html: <title>Introduction · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare Images provides a platform for optimizing, storing, and serving images at scale."><link rel="canonical" href="https://developers.cloudflare.com/images/get-started/introduction/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/get-started/introduction/index.md"><meta property="og:title" content="Introduction · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare Images provides a platform for optimizing, storing, and serving images at scale."><meta property="og:url" content="https://developers.cloudflare.com/images/get-started/introduction/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/get-started/introduction/#page","headline":"Introduction \u00b7 Cloudflare Images docs","description":"Cloudflare Images provides a platform for optimizing, storing, and serving images at scale.","url":"https://developers.cloudflare.com/images/get-started/introduction/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/get-started/introduction/
  schema: 1
---
<p>Cloudflare provides a platform for building and scaling media applications with Images. On this page, we'll answer the following questions:</p>
<ul>
<li>Why optimize images?</li>
<li>How do I get started with Images?</li>
<li>Should I store with Images or R2?</li>
</ul>
<hr />
<h2 id="why-optimize-images">Why optimize images?</h2>
<p>Loading images in their original resolution and format quickly becomes a bottleneck for app performance — especially on mobile.</p>
<p>Meanwhile, creating and storing multiple versions of the same image adds complexity and overhead, along with storage costs.</p>
<p>When you serve large amounts of media, image optimization provides:</p>
<ul>
<li><strong>Streamlined infrastructure</strong> — Simplify your workflow and reduce infrastructure costs by dynamically generating optimized versions on request.</li>
<li><strong>Smaller file sizes</strong> — Automatically deliver images in modern formats like AVIF and WebP, which improves page speed and lowers bandwidth.</li>
<li><strong>Responsive sizing</strong> — Crop and resize for any use case, from square thumbnails to landscape banners, using the same original image in storage.</li>
<li><strong>Visual effects</strong> — Apply blur, overlays, background fills, and more at the edge.</li>
</ul>
<h2 id="how-do-i-get-started-with-images">How do I get started with Images?</h2>
<p>There are two ways to use Images, depending on where your images are stored:</p>
<h3 id="optimize-remote-images">Optimize remote images</h3>
<p>Keep your images on your own origin, in <a href="/r2">R2</a>, or with any storage provider. Cloudflare pulls the original image, applies optimizations at the edge, and caches the optimized image.</p>
<p>You can define an <a href="/images/optimization/transformations/sources/">origin allowlist</a> to control which source images can be transformed on your zone.</p>
<p>To start, <a href="/images/optimization/transformations/overview/">enable transformations on your zone</a>.</p>
<h3 id="upload-and-deliver-with-images">Upload and deliver with Images</h3>
<p>Store, optimize, and deliver images globally with zero infrastructure management.</p>
<p>If your app centers around user-uploaded content, then you can use the <a href="/images/storage/upload-images/direct-creator-upload/">Direct Creator Upload API</a> to securely accept images directly from your users.</p>
<p>To start, set up <a href="/images/optimization/hosted-images/create-variants/">predefined variants</a> to configure how hosted images should be served.</p>
<h2 id="should-i-store-with-images-or-r2">Should I store with Images or R2?</h2>
<p><strong>Store in <a href="/r2/">R2</a> and use Images for transformations</strong> if you want to build your own custom image pipeline or need fine-grained control over storage, such as <a href="/r2/buckets/">bucket-level access management</a> or <a href="/r2/buckets/object-lifecycles/">object lifecycle rules</a>. This is typically the most cost-effective approach for image optimization.</p>
<p><strong>Store in Images</strong> if you want a fully managed solution with the least configuration. Our built-in features include a <a href="/images/optimization/hosted-images/serve-uploaded-images/">shared delivery domain</a>, <a href="/images/optimization/hosted-images/create-variants/">predefined variants</a>, and automatic cache invalidation when you update original images in storage.</p>
<p>Each use case has a separate pricing model. To learn more, refer to <a href="/images/pricing/">Pricing</a>.</p>
