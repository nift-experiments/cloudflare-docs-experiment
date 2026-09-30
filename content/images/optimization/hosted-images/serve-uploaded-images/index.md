---
cp9:
  canonical: https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/
  description: Construct delivery URLs to serve images uploaded to Cloudflare Images using your account hash, image ID, and variant name.
  full_title: Serve uploaded images · Cloudflare Images docs
  head_html: <title>Serve uploaded images · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Construct delivery URLs to serve images uploaded to Cloudflare Images using your account hash, image ID, and variant name."><link rel="canonical" href="https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/index.md"><meta property="og:title" content="Serve uploaded images · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Construct delivery URLs to serve images uploaded to Cloudflare Images using your account hash, image ID, and variant name."><meta property="og:url" content="https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/#page","headline":"Serve uploaded images \u00b7 Cloudflare Images docs","description":"Construct delivery URLs to serve images uploaded to Cloudflare Images using your account hash, image ID, and variant name.","url":"https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/optimization/hosted-images/serve-uploaded-images/
  schema: 1
---
<p>To serve images uploaded to Cloudflare Images, you must have:</p>
<ul>
<li>Your Images account hash</li>
<li>Image ID</li>
<li>Variant or flexible variant name</li>
</ul>
<p>Assuming you have at least one image uploaded to Images, you will find the basic URL format from the Images dashboard under Developer Resources.</p>
<p><img src="/assets/upstream/images/images/image-delivery-url.png" alt="Developer Resources section within the Images product form the Cloudflare Dashboard." /></p>
<p>A typical image delivery URL looks similar to the example below.</p>
<p><code>https://imagedelivery.net/&lt;ACCOUNT_HASH&gt;/&lt;IMAGE_ID&gt;/&lt;VARIANT_NAME&gt;</code></p>
<p>In the example, you need to replace <code>&lt;ACCOUNT_HASH&gt;</code> with your Images account hash, along with the <code>&lt;IMAGE_ID&gt;</code> and <code>&lt;VARIANT_NAME&gt;</code>, to begin serving images.</p>
<p>You can select <strong>Preview</strong> next to the image you want to serve to preview the image with an Image URL you can copy. The link will have a fully formed <strong>Images URL</strong> and will look similar to the example below.</p>
<p>In this example:</p>
<ul>
<li><code>ZWd9g1K7eljCn_KDTu_MWA</code> is the Images account hash.</li>
<li><code>083eb7b2-5392-4565-b69e-aff66acddd00</code> is the image ID. You can also use Custom IDs instead of the generated ID.</li>
<li><code>public</code> is the variant name.</li>
</ul>
<p>When a user requests an image, Cloudflare Images chooses the optimal format, which is determined by client headers and the image type.</p>
<h2 id="optimize-format">Optimize format</h2>
<p>Cloudflare Images automatically transcodes uploaded PNG, JPEG and GIF files to the more efficient AVIF and WebP formats. This happens whenever the customer browser supports them. If the browser does not support AVIF, Cloudflare Images will fall back to WebP. If there is no support for WebP, then Cloudflare Images will serve compressed files in the original format.</p>
<p>Uploaded SVG files are served as <a href="/images/get-started/limits/#svg">sanitized SVGs</a>.</p>
