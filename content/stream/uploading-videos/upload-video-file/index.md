---
cp9:
  canonical: https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/
  description: Upload video files under 200 MB to Cloudflare Stream using the dashboard or API.
  full_title: Basic video uploads · Cloudflare Stream docs
  head_html: <title>Basic video uploads · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Upload video files under 200 MB to Cloudflare Stream using the dashboard or API."><link rel="canonical" href="https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/index.md"><meta property="og:title" content="Basic video uploads · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upload video files under 200 MB to Cloudflare Stream using the dashboard or API."><meta property="og:url" content="https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/#page","headline":"Basic video uploads \u00b7 Cloudflare Stream docs","description":"Upload video files under 200 MB to Cloudflare Stream using the dashboard or API.","url":"https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/uploading-videos/upload-video-file/
  schema: 1
---
<h2 id="basic-uploads">Basic Uploads</h2>
<p>For files smaller than 200 MB, you can use simple form-based uploads.</p>
<h2 id="upload-through-the-cloudflare-dashboard">Upload through the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Stream</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Drag and drop your video into the <strong>Quick upload</strong> area. You can also click to browse for the file on your machine.</li>
</ol>
<p>After the video finishes uploading, the video appears in the list.</p>
<h2 id="upload-with-the-stream-api">Upload with the Stream API</h2>
<p>Make a <code>POST</code> request with the <code>content-type</code> header set to <code>multipart/form-data</code> and include the media as an input with the name set to <code>file</code>.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-form file=@/Users/user_name/Desktop/my-video.mp4 \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14369.md")
</aside>
