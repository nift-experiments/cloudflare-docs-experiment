---
cp9:
  canonical: https://developers.cloudflare.com/images/get-started/limits/
  description: Supported file formats, size limits, and dimension constraints for Cloudflare Images.
  full_title: Limits and formats · Cloudflare Images docs
  head_html: <title>Limits and formats · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Supported file formats, size limits, and dimension constraints for Cloudflare Images."><link rel="canonical" href="https://developers.cloudflare.com/images/get-started/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/get-started/limits/index.md"><meta property="og:title" content="Limits and formats · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Supported file formats, size limits, and dimension constraints for Cloudflare Images."><meta property="og:url" content="https://developers.cloudflare.com/images/get-started/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/get-started/limits/#page","headline":"Limits and formats \u00b7 Cloudflare Images docs","description":"Supported file formats, size limits, and dimension constraints for Cloudflare Images.","url":"https://developers.cloudflare.com/images/get-started/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/get-started/limits/
  schema: 1
---
<p>This section covers limits and supported formats for Images.</p>
<hr />
<h2 id="limits">Limits</h2>
<p>Here are limits to keep in mind when optimizing with Images.</p>
<p>On an Enterprise plan, you can reach out to our account team to ensure that the limits align with your needs.</p>
<h3 id="remote-images">Remote images</h3>
<p>The following limits apply when transforming a remote image stored outside of Images:</p>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Image file size</td>
<td>100 MB</td>
</tr>
<tr>
<td>Image area, excluding animated GIFs</td>
<td>100 MP (e.g. 10,000x10,000 pixels)</td>
</tr>
<tr>
<td>Image area for animated GIFs</td>
<td>100 MP*</td>
</tr>
<tr>
<td>Image dimension, excluding WebP and AVIF</td>
<td>12,000 pixels</td>
</tr>
<tr>
<td>Image dimension, AVIF</td>
<td>1,200 pixels</td>
</tr>
</tbody>
</table>
<h3 id="hosted-images">Hosted images</h3>
<p>The following limits apply when uploading to your Images storage:</p>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Image file size</td>
<td>10 MB</td>
</tr>
<tr>
<td>Image area, excluding animated GIFs</td>
<td>100 MP (e.g. 10,000x10,000 pixels)</td>
</tr>
<tr>
<td>Image area, animated GIFs</td>
<td>100 MP*</td>
</tr>
<tr>
<td>Image dimension, excluding WebP and AVIF</td>
<td>12,000 pixels</td>
</tr>
<tr>
<td>Image dimension, AVIF</td>
<td>1,200 pixels</td>
</tr>
<tr>
<td>Image metadata</td>
<td>1024 bytes</td>
</tr>
</tbody>
</table>
<h3 id="limits-for-animated-images">Limits for animated images</h3>
<p>GIF/WebP animations are limited to the total megapixels across all frames, or the sum of areas of all frames. For example, a GIF with 500x500 dimensions and 10 frames has an image area of 2,500,000 pixels or 2.5 megapixels.</p>
<p>The limit to deliver an animated GIF/WebP animation is 100 megapixels. However, any animations over 50 megapixels will be delivered without applying any transformations.</p>
<p>When serving animations, we recommend using video formats like MP4 and WebM for best performance. As the GIF format has inefficient compression, high resolution animations typically have larger file sizes and take longer to compress.</p>
<p>To optimize remote videos, you can use <a href="https://developers.cloudflare.com/stream/transform-videos/">media transformations</a>.</p>
<h3 id="limits-for-the-images-binding">Limits for the Images binding</h3>
<p>When optimizing with the <a href="/images/optimization/binding/">Images binding</a>, the maximum input size for <code>.input()</code> is 20 MB.</p>
<h2 id="supported-formats">Supported formats</h2>
<h3 id="input-formats">Input formats</h3>
<p>Images supports a wide range of input formats for both remote and hosted images:</p>
<ul>
<li>PNG</li>
<li>JPEG</li>
<li>GIF (including animations)</li>
<li>WebP (including animations)</li>
<li>SVG</li>
<li>AVIF*</li>
<li>HEIC</li>
</ul>
<p>*Available on an Enterprise plan.</p>
<h3 id="output-formats">Output formats</h3>
<p>You can serve images in the following output formats:</p>
<ul>
<li>PNG</li>
<li>JPEG</li>
<li>GIF (including animations)</li>
<li>WebP (including animations)</li>
<li>SVG</li>
<li>AVIF</li>
</ul>
<p>When detecting the most optimal output format for the requesting browser, Cloudflare balances the time to generate an image with the time to serve the image to the browser.</p>
<p>In particular, AVIF encoding can be an order of magnitude slower than encoding to other formats. If the image is too large to be quickly encoded to AVIF, then Cloudflare will fall back to WebP or JPEG.</p>
<h3 id="progressive-jpeg">Progressive JPEG</h3>
<p>When transcoding to JPEG, Cloudflare generates images in an interlaced progressive JPEG format.</p>
<p>You can use the <a href="/images/optimization/features/#format"><code>format</code></a> parameter to specify whether progressive or baseline JPEG should be used.</p>
<p>However, we will always fall back to the baseline JPEG format — even when progressive JPEG is specified — if either:</p>
<ul>
<li>The output image area dimensions are less than 50x50.</li>
<li>The output image area dimensions are greater than 3000x3000.</li>
</ul>
<h3 id="svg">SVG</h3>
<p>Cloudflare does not resize SVG files and will ignore any optimization parameters.</p>
<p>If you store in Images, then you can use any predefined variant as a placeholder to deliver a sanitized SVG. For example, applying the default public variant allows the SVG to be delivered without resizing or cropping:</p>
<p><code>imagedelivery.net/account_hash/svg_id/public</code></p>
<p>Similarly, you can use Images to serve a sanitized SVG that is stored in your own origin, like in <a href="/r2/">R2</a>.</p>
<p>When SVG files are served, they are sanitized using <a href="https://github.com/cloudflare/svg-hush"><code>svg-hush</code></a>, an open-source tool developed by Cloudflare to make SVGs as safe as possible. It streams the files without buffering, enabling us to quickly filter them on the fly. SVG files are XML documents and can contain links or Javascript features that may pose a security concern.</p>
<p>The <code>svg-hush</code> tool filters SVGs and removes potentially risky features, such as:</p>
<ul>
<li><strong>Scripting.</strong> We prevent SVGs from being used for cross-site scripting attacks. Although browsers do not allow scripts in <code>&lt;img&gt;</code> tags, they do allow scripting when SVGs are opened directly as a top-level document.</li>
<li><strong>Hyperlinks to other documents.</strong> Removing hyperlinking makes
SVG files less attractive for SEO spam and phishing.</li>
<li><strong>References to cross-origin resources.</strong> We stop third parties
from tracking who is viewing the image.</li>
</ul>
