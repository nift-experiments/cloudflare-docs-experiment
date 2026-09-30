---
cp9:
  canonical: https://developers.cloudflare.com/images/storage/upload-images/methods/
  description: Upload images through the dashboard, API, Workers, or S3.
  full_title: Methods · Cloudflare Images docs
  head_html: <title>Methods · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Upload images through the dashboard, API, Workers, or S3."><link rel="canonical" href="https://developers.cloudflare.com/images/storage/upload-images/methods/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/storage/upload-images/methods/index.md"><meta property="og:title" content="Methods · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upload images through the dashboard, API, Workers, or S3."><meta property="og:url" content="https://developers.cloudflare.com/images/storage/upload-images/methods/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/storage/upload-images/methods/#page","headline":"Methods \u00b7 Cloudflare Images docs","description":"Upload images through the dashboard, API, Workers, or S3.","url":"https://developers.cloudflare.com/images/storage/upload-images/methods/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/storage/upload-images/methods/
  schema: 1
---
<p>Cloudflare gives you the option to <a href="/images/optimization/transformations/overview">transform remote images</a>, or upload into Images storage.</p>
<p>If you have a <a href="/images/pricing#images-paid">paid Images plan</a>, you can upload an image using the following methods:</p>
<ul>
<li>Upload directly through the dashboard. This is primarily used for one-off uploads.</li>
<li>Upload using API endpoints.</li>
<li>Upload from a Worker using the <a href="/images/storage/binding/">Images binding</a>.</li>
<li>Import images from Amazon S3.</li>
</ul>
<hr />
<h2 id="upload-via-dashboard">Upload via dashboard</h2>
<p>To upload an image from the dashboard, follow these steps:</p>
<ol>
<li>Log in to the Cloudflare dashboard and select your account.</li>
<li>Go to the <strong>Images &amp; Stream</strong> → <strong>Hosted images</strong> tab.</li>
<li>Drag and drop your image in the <strong>Quick Upload</strong> section. Alternatively, you can browse to select your image from your local disk.</li>
<li>When your image successfully uploads, your image will appear in the list of files.</li>
</ol>
<h2 id="upload-using-api">Upload using API</h2>
<p>Upload, manage, and delete hosted images from the Images API.</p>
<p>The Images API endpoint uses the following format:</p>
<pre tabindex="0"><code class="language-txt">  https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/images/v1&#10;</code></pre>
<p>When uploading through the API, you can use the following features:</p>
<ul>
<li>Upload an image from your local machine or from <a href="/images/storage/upload-images/upload-url">a URL</a>.</li>
<li>Upload your image to a <a href="/images/storage/upload-images/upload-custom-path/">custom ID path</a> rather than the path automatically generated by our Universal Unique Identifier (UUID).</li>
<li>The <a href="/images/storage/upload-images/direct-creator-upload/">Direct Creator API</a> lets you accept image uploads from your users without exposing your API token.</li>
<li>The <a href="/images/storage/upload-images/images-batch/">Batch API</a> returns a batch token that you can use to upload, manage, and delete images while bypassing Cloudflare’s global rate limits.</li>
</ul>
<h2 id="import-from-s3">Import from S3</h2>
<p>Import from S3 lets you copy objects from an Amazon S3 bucket to your Images storage.</p>
<p>With Import from S3, you can:</p>
<ul>
<li>Define repositories of images to bulk import.</li>
<li>Reuse existing sources and import only new images, skipping any other images that were already imported.</li>
<li>Define target paths and prefixes for imported images.</li>
</ul>
<p>For more information, refer to <a href="/images/storage/upload-images/import-from-s3/">Import from S3</a>.</p>
