---
cp9:
  canonical: https://developers.cloudflare.com/images/optimization/features/
  description: Available Cloudflare Images optimization parameters for resizing, cropping, format conversion, and visual effects.
  full_title: Features · Cloudflare Images docs
  head_html: <title>Features · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Available Cloudflare Images optimization parameters for resizing, cropping, format conversion, and visual effects."><link rel="canonical" href="https://developers.cloudflare.com/images/optimization/features/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/optimization/features/index.md"><meta property="og:title" content="Features · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available Cloudflare Images optimization parameters for resizing, cropping, format conversion, and visual effects."><meta property="og:url" content="https://developers.cloudflare.com/images/optimization/features/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/optimization/features/#page","headline":"Features \u00b7 Cloudflare Images docs","description":"Available Cloudflare Images optimization parameters for resizing, cropping, format conversion, and visual effects.","url":"https://developers.cloudflare.com/images/optimization/features/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/optimization/features/
  schema: 1
---
<p>Cloudflare enables developers to optimize images at scale by dynamically generating different versions in real time.</p>
<p>The guide describes all of the parameters that can be used to resize, crop, manipulate, and apply visual effects to images.</p>
<h2 id="how-to-apply-optimization">How to apply optimization</h2>
<p>Use Cloudflare's image optimization capabilities through:</p>
<ul>
<li><strong>URL interface</strong> — Apply parameters directly in the image URL to specify how images should be optimized when served to the browser.</li>
<li><strong>Workers</strong> — Bind the Images API directly to your Worker or set the <code>cf.image</code> options on a <code>fetch</code> subrequest to build programmatic image workflows.</li>
</ul>
<h3 id="url-interface">URL interface</h3>
<p>Cloudflare uses a different URL structure depending on whether you are optimizing a <a href="/images/optimization/transformations/overview/">remote</a> or a <a href="/images/optimization/hosted-images/serve-uploaded-images/">hosted</a> image:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9367.md")
</div></div>
<h3 id="workers">Workers</h3>
<p>When using <a href="/images/optimization/transformations/transform-via-workers/">Images with Workers</a>, you can:</p>
<ul>
<li>Apply custom logic to set the order for optimization operations. For example, by default, Images will apply <code>flip</code> before <code>rotate</code>; instead, you can use the Images binding to customize your optimization workflow to rotate the image before flipping it.</li>
<li>Use a custom URL scheme instead of the default URL structure.</li>
<li>Implement content negotiation to dynamically adapt image size, format, and quality based on the device and network condition.</li>
</ul>
<hr />
<h2 id="parameters">Parameters</h2>
<h3 id="anim"><code>anim</code></h3>
<p>Specifies whether to preserve animation frames from input files.</p>
<ul>
<li><code>true</code> (default) — Outputs the animated image with all frames.</li>
<li><code>false</code> — Converts the first frame of an animated input to a still image.</li>
</ul>
<p>This setting is recommended when enlarging images or processing arbitrary user-uploaded content, as animated GIFs can have large file sizes and increase page load times. When using <code>format=json</code>, it is also useful to set <code>anim=false</code> to get a quicker response without the number of frames.</p>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none"> 
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/anim.gif" alt="Original animation" style="width:100%; height:auto" />
</td>
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/anim.png" alt="anim=false output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
      <code>anim=false</code>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9370.md")
</div></div>
<h3 id="background"><code>background</code></h3>
<p>Specifies an opaque or transparent color to fill blank or transparent pixels in the image. The default is <code>%23FFFFFF</code> (white).</p>
<p>Accepts the following properties:</p>
<ul>
<li>A HEX color code, formatted as <code>%23RRGGBB</code>.</li>
<li>A CSS color name, e.g. <code>white</code> or <code>red</code>.</li>
<li>An <code>rgb()</code> or <code>rgba()</code> CSS color function, e.g. <code>rgba(250,40,145,0.5)</code>.</li>
</ul>
<p>The background color is visible in images with transparent pixels, including images that are resized with <code>fit=pad</code>.</p>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/original.jpg" alt="Original image" style="width:100%; height:auto" />
</td>
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/background-red.jpg" alt="background=red output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong><br />
      1080 x 720
</td>
<td style="border:none;">
      <strong>Output</strong><br />
      1080 x 900
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9373.md")
</div></div>
<h3 id="blur"><code>blur</code></h3>
<p>Applies a blur radius to the image. Accepts an integer from <code>0</code> (no blur) to <code>250</code> (maximum blur). The default is <code>0</code>.</p>
<p>This parameter should not be used to reliably obscure image content when optimizing via URL, as the URL can be modified to remove the blur parameter. Instead, you can <a href="/images/optimization/transformations/transform-via-workers/">restrict access to the original image</a> through Workers.</p>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/original.jpg" alt="Original image" style="width:100%; height:auto" />
</td>
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/blur-50.jpg" alt="blur=50 output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;blur=50&lt;/code&gt;&#10;</code></pre>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9376.md")
</div></div>
<h3 id="border"><code>border</code></h3>
<p>Adds a border around the image.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9362.md")
</aside>
<p>Accepts the following properties:</p>
<ul>
<li><code>color</code> — Sets the color of the border. Accepts any valid CSS color value, for example <code>#FF0000</code>, <code>rgb(0,0,0)</code>, or <code>red</code>.</li>
<li><code>width</code> — Sets the uniform border, in pixels, on all four sides.</li>
<li><code>top</code>, <code>right</code>, <code>bottom</code>, <code>left</code> — Sets the border width, in pixels, for individual sides.</li>
</ul>
<p>The border is applied after the image has been resized. The border width automatically scales with the <a href="/images/optimization/features#dpr"><code>dpr</code></a> parameter to ensure sharpness on high-resolution screens.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9378.md")
</div></div>
<h3 id="brightness"><code>brightness</code></h3>
<p>Adjusts the image's overall luminance using a multiplier.</p>
<ul>
<li><code>1</code> (default) — No change to the original brightness.</li>
<li><code>&lt; 1.0</code> — Darkens the image, e.g. <code>0.5</code> is half as bright.</li>
<li><code>&gt; 1.0</code> — Lightens the image, e.g. <code>2</code> is twice as bright.</li>
</ul>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/original.jpg" alt="Original image" style="width:100%; height:auto" />
</td>
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/brightness-0.5.jpg" alt="brightness=0.5 output" style="width:100%; height:auto" />
</td>
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/brightness-2.jpg" alt="brightness=2 output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;brightness=0.5&lt;/code&gt;&#10;</code></pre>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;brightness=2&lt;/code&gt;&#10;</code></pre>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9381.md")
</div></div>
<h3 id="compression"><code>compression</code></h3>
<p>Selects the output format that is quickest to compress. Accepts <code>fast</code>. The default is none.</p>
<p>The <code>compression=fast</code> option prioritizes encoding speed over output quality and file size, and will usually override the <code>format</code> parameter to choose JPEG over more efficient formats like AVIF or WebP. This slightly reduces latency on a cache miss, but may result in increased file size and lower image quality.</p>
<p>This option is not recommended, except in unusual circumstances like resizing uncacheable, dynamically-generated images.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9384.md")
</div></div>
<h3 id="contrast"><code>contrast</code></h3>
<p>Adjusts the image's overall difference between the darkest and lightest parts using a multiplier.</p>
<ul>
<li><code>1</code> (default) — No change to the original contrast.</li>
<li><code>&lt; 1.0</code> — Decreases contrast, which makes shadows lighter and highlights darker.</li>
<li><code>&gt; 1.0</code> — Increases contrast, which pushes shadows toward black and highlights toward white.</li>
</ul>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/original.jpg" alt="Original image" style="width:100%; height:auto" />
</td>
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/contrast-0.5.jpg" alt="contrast=0.5 output" style="width:100%; height:auto" />
</td>
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/contrast-2.jpg" alt="contrast=2 output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;contrast=0.5&lt;/code&gt;&#10;</code></pre>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;contrast=2&lt;/code&gt;&#10;</code></pre>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9387.md")
</div></div>
<h3 id="dpr"><code>dpr</code></h3>
<p>Scales the output resolution by a multiplier to match a user's specific screen density (for example, Retina or 4K). The default is <code>1</code>, which delivers the image at the exact width and height requested. The maximum supported value is <code>2</code>.</p>
<p>Modern devices have more physical pixels than CSS pixels. If you serve a 300px image in a 300px container on a high-DPR smartphone, then it will look blurry. Using <code>dpr=2</code> tells Cloudflare to send a 600px image for the same 300px container, which results in a clearer, crisper image.</p>
<p>The <code>dpr</code> parameter can be used with <code>srcset</code> to <a href="/images/optimization/make-responsive-images/">serve responsive images</a>.</p>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/dpr-1.jpg" alt="dpr=1 output" style="width:100%; height:auto" />
</td>
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/dpr-2.jpg" alt="dpr=2 output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;width=300,height=200,dpr=1&lt;/code&gt;&#10;</code></pre>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;width=300,height=200,dpr=2&lt;/code&gt;&#10;</code></pre>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9390.md")
</div></div>
<h3 id="fit"><code>fit</code></h3>
<p>Specifies how the image is fit to the target area.</p>
<p>Fit is performed after setting the <a href="#width"><code>width</code></a> and <a href="#height"><code>height</code></a> dimensions of the image.</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Result</th>
<th>Match original aspect ratio</th>
<th>Upscales</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>scale-down</code> (default)</td>
<td>Show entire image without cropping or upscaling</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td><code>contain</code></td>
<td>Show entire image without cropping</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td><code>cover</code></td>
<td>Fill the entire requested area, cropping if needed</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td><code>crop</code></td>
<td>Fill the entire requested area, but never upscales</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<td><code>aspect-crop</code></td>
<td>Crop to match the target aspect ratio, but never upscales</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<td><code>pad</code></td>
<td>Fit within the target area, adding space for remaining area</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td><code>squeeze</code></td>
<td>Scale to exact dimensions, distorting if needed</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td><code>scale-up</code></td>
<td>Upscales while showing the entire image, but never downscales</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9393.md")
</div></div>
<h4 id="scale-down"><code>scale-down</code></h4>
Resizes the image to fit within the specified dimensions while preserving its original aspect ratio, but never upscales the image. This is the default `fit` behavior.
<p>When the original image is smaller than the target area, it is returned at its original dimensions. For example, a request to serve a 1080x720 image at 2000x2000 will return the image at 1080x720.</p>
<p>When larger, it downscales the image to fit the target area while matching the original aspect ratio.</p>
<p>In the example below, the 1080x720 image is resized to fit within the target 500x500 area. Since <code>scale-down</code> preserves the original aspect ratio (3:2), the final dimensions of the output image are 500x333.</p>
<table style="width:100%; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="border:none; width:51.9%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-landscape.jpg" alt="original image" style="width:100%; height:auto" />
</td>
<td style="border:none; width:24%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/1296x1296.png" alt="target area" style="width:100%; height:auto" />
</td>
<td style="border:none; width:24%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-contain.png" alt="fit=scale-down output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong><br />
      1080 x 720 (3:2)
</td>
<td style="border:none;">
      <strong>Requested</strong><br />
      500 x 500 (1:1)
</td>
<td style="border:none;">
      <strong>Output</strong><br />
      500 x 333 (3:2)
</td>
</tr>
</table>
<h4 id="contain"><code>contain</code></h4>
Resizes the image to be as large as possible within the target `width` and `height` dimensions while preserving its original aspect ratio.
<p>When the original image is larger than the target area, it downscales to fit the target area (like <code>scale-down</code>).</p>
<p>When smaller, it upscales instead (like <code>scale-up</code>). Works with the <a href="#upscale"><code>upscale</code></a> parameter to control the algorithm for enlarging an image. To avoid upscaling, use <code>scale-down</code>.</p>
<h4 id="cover"><code>cover</code></h4>
Fills the entire target area, shrinking or enlarging the image if needed. The output area always matches the requested `width` and `height` dimensions exactly.
<p>When the original and target aspect ratios differ, the image is resized to cover the full target area and any overflow is cropped. Use the <a href="#gravity"><code>gravity</code></a> parameter to control which part of the image is preserved during cropping.</p>
<p>Works with the <a href="#upscale"><code>upscale</code></a> parameter to control the algorithm for enlarging an image.</p>
<p>In the example below, the 1080×720 image is first resized to 750×500 (matching the requested height) to fit the target area, then cropped from the left and right edges to its final 500x500 dimensions.</p>
<table style="width:100%; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="border:none; width:51.9%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-landscape.jpg" alt="original image" style="width:100%; height:auto" />
</td>
<td style="border:none; width:24%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/1296x1296.png" alt="target area" style="width:100%; height:auto" />
</td>
<td style="border:none; width:24%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-cover.png" alt="fit=cover output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong><br />
      1080 x 720 (3:2)
</td>
<td style="border:none;">
      <strong>Requested</strong><br />
      500 x 500 (1:1)
</td>
<td style="border:none;">
      <strong>Output</strong><br />
      500 x 500 (1:1)
</td>
</tr>
</table>
<p>When the original image is smaller than the target area, it upscales instead. To avoid upscaling, use <code>crop</code>.</p>
<h4 id="crop"><code>crop</code></h4>
Resizes the image to fill the target area without upscaling.
<p>When the original image is smaller than the target area, it keeps its original size and aspect ratio (like <code>scale-down</code>).</p>
<p>In the example below, the original image (1080x720) is smaller than the target area (1296x1296), so it preserves its original size and aspect ratio.</p>
<table style="width:100%; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="border:none; width:31.25%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-landscape.jpg" alt="original image" style="width:100%; height:auto" />
</td>
<td style="border:none; width:37.5%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/1296x1296.png" alt="target area" style="width:100%; height:auto" />
</td>
<td style="border:none; width:31.25%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-landscape.jpg" alt="fit=crop output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong><br />
      1080 x 720 (3:2)
</td>
<td style="border:none;">
      <strong>Requested</strong><br />
      1296 x 1296 (1:1)
</td>
<td style="border:none;">
      <strong>Output</strong><br />
      1080 x 720 (3:2)
</td>
</tr>
</table>
<p>When the original image is larger than the target area, it behaves like <code>cover</code> (fills the target area and crops the rest) instead.</p>
<h4 id="aspect-crop"><code>aspect-crop</code></h4>
Crops the image to match the target aspect ratio, scaling down if needed but never upscaling.
<p>When the original image is larger than the target area, it downscales to the smallest size that still fills the target dimensions, then is cropped to match the target aspect ratio (like <code>cover</code>).</p>
<p>When the original image is smaller than the target area, it keeps its original size but is cropped to match the target aspect ratio. Unlike <code>crop</code>, which preserves the original size and dimensions of smaller images, <code>aspect-crop</code> always enforces the target aspect ratio.</p>
<p>For example, a 612x613 image requested at 1920x1120 will not be upscaled. Instead, it stays at its original size and is cropped to 612x357, matching the 1920:1120 aspect ratio. Use the <a href="#gravity"><code>gravity</code></a> parameter to control which part of the image is preserved during cropping.</p>
<h4 id="pad"><code>pad</code></h4>
Resizes the image to be as large as possible within the dimensions. If applicable, the output area will be expanded to match the `width` and `height` dimensions exactly.
<p>Works with the <code>background</code> parameter to fill any blank or transparent pixels. However, for web apps, you can often achieve the same visual result using the <code>contain</code> option with the CSS <code>object-fit: contain</code> property, which avoids encoding padding pixels into the image itself.</p>
<p>In the example below, the original image (1080x720) is smaller than the target area (1080x1080), so it creates space for the remaining pixels.</p>
<table style="width:100%; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-landscape.jpg" alt="original image" style="width:100%; height:auto" />
</td>
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/1296x1296.png" alt="target area" style="width:100%; height:auto" />
</td>
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-pad.png" alt="fit=pad output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong><br />
      1080 x 720 (3:2)
</td>
<td style="border:none;">
      <strong>Requested</strong><br />
      1080 x 1080 (1:1)
</td>
<td style="border:none;">
      <strong>Output</strong><br />
      1080 x 1080 (1:1)
</td>
</tr>
</table>
<h4 id="squeeze"><code>squeeze</code></h4>
Resizes the image to exactly match the requested width and height, without cropping the edges or constraining the portions.
<p>When the original and target aspect ratios differ, the image will be distorted to fit the target area.</p>
<table style="width:100%; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="border:none; width:31.25%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-landscape.jpg" alt="original image" style="width:100%; height:auto" />
</td>
<td style="border:none; width:31.25%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-squeeze.jpg" alt="fit=squeeze output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong><br />
      1080 x 720
</td>
<td style="border:none;">
      <strong>Output</strong><br />
      1080 x 540
</td>
</tr>
</table>
<table style="width:100%; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="border:none; width:31.25%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/abstract.jpg" alt="original image" style="width:100%; height:auto" />
</td>
<td style="border:none; width:31.25%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/abstract-squeeze.jpg" alt="fit=squeeze output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong><br />
      1080 x 1080
</td>
<td style="border:none;">
      <strong>Output</strong><br />
      1080 x 540
</td>
</tr>
</table>
<h4 id="scale-up"><code>scale-up</code></h4>
Resizes the image to fit within the specified dimensions while preserving its original aspect ratio, but never downscales the image. This is the inverse of `scale-down`.
<p>When the original image is larger than the target area, it is returned at its original dimensions.</p>
<p>When the original image is smaller than the target area, it is enlarged to fit within the target dimensions. Use the <a href="#upscale"><code>upscale</code></a> parameter to control the algorithm used for upscaling images — set <code>upscale=generate</code> for AI-powered upscaling or <code>upscale=interpolate</code> (default) for bicubic interpolation.</p>
<h3 id="flip"><code>flip</code></h3>
<p>Flips the image horizontally, vertically, or both.</p>
<p>Accepts the following values:</p>
<ul>
<li><code>h</code> — Flips the image horizontally.</li>
<li><code>v</code> — Flips the image vertically.</li>
<li><code>hv</code> — Flips the image both horizontally and vertically.</li>
</ul>
<p>Flip can be used with the <code>rotate</code> parameter to set the orientation of the image. Flip is performed before rotation. For example, if you apply <code>flip=h,rotate=90</code>, then the image will be flipped horizontally, then rotated by 90 degrees.</p>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/original.jpg" alt="Original image" style="width:100%; height:auto" />
</td>
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/flip-h.jpg" alt="flip=h output" style="width:100%; height:auto" />
</td>
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/flip-v.jpg" alt="flip=v output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;flip=h&lt;/code&gt;&#10;</code></pre>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;flip=v&lt;/code&gt;&#10;</code></pre>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9396.md")
</div></div>
<p><a id="format"></a></p>
<h3 id="format-f"><code>format</code> | <code>f</code></h3>
<p>Specifies the output format for the image.</p>
<p>Accepts the following values:</p>
<ul>
<li><code>auto</code> — Automatically serves the most efficient format that the requesting browser supports. When you serve a <a href="/images/optimization/hosted-images/create-variants/">hosted image</a>, this is the default <code>format</code> option.</li>
<li><code>avif</code> — Transcodes the image to AVIF, if possible. AVIF encoding can be an order of magnitude slower than encoding to other formats. If the image is too large to be quickly encoded to AVIF, then Cloudflare will fall back to WebP or JPEG.</li>
<li><code>webp</code> — Transcodes the image to Google WebP format. Use <code>quality=100</code> to return the WebP lossless format.</li>
<li><code>jpeg</code> — Transcodes the image in interlaced progressive JPEG format, in which data is compressed in multiple passes of progressively higher detail.</li>
<li><code>baseline-jpeg</code> — Transcode the image in baseline sequential JPEG format. It should be used in cases when target devices do not support progressive JPEG or other modern file formats.</li>
<li><code>json</code> — Outputs information about the image as a JSON object. This contains data such as image size (before and after resizing), the source image's MIME type, and file size.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9399.md")
</div></div>
<p>To use <code>format=auto</code> with a custom Worker, you need to parse the <code>Accept</code> header. Refer to <a href="/images/optimization/transformations/transform-via-workers/#an-example-worker">this example Worker</a> for a complete overview of how to set up an image transformation Worker.</p>
<pre tabindex="0"><code class="language-js">const accept = request.headers.get(&quot;accept&quot;);&#10;let image = {};&#10;&#10;if (/image\/avif/.test(accept)) {&#10;	image.format = &quot;avif&quot;;&#10;} else if (/image\/webp/.test(accept)) {&#10;	image.format = &quot;webp&quot;;&#10;}&#10;&#10;return fetch(url, { cf: { image } });&#10;</code></pre>
<h3 id="gamma"><code>gamma</code></h3>
<p>Adjusts the exposure of an image using a multiplier. Gamma controls the midtone brightness without affecting the darkest or lightest parts of the image.</p>
<ul>
<li><code>0</code> and <code>1</code> (default) — No change to the original gamma.</li>
<li><code>&lt; 1.0</code> — Increases midtone brightness, making the image appear lighter overall.</li>
<li><code>&gt; 1.0</code> — Decreases midtone brightness, making the image appear darker overall.</li>
</ul>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/original.jpg" alt="Original image" style="width:100%; height:auto" />
</td>
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/gamma-0.5.jpg" alt="gamma=0.5 output" style="width:100%; height:auto" />
</td>
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/gamma-2.jpg" alt="gamma=2 output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;gamma=0.5&lt;/code&gt;&#10;</code></pre>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;gamma=2&lt;/code&gt;&#10;</code></pre>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9402.md")
</div></div>
<p><a id="gravity"></a></p>
<h3 id="gravity-g"><code>gravity</code> | <code>g</code></h3>
<p>Specifies how the image should be cropped when used with <code>fit=cover</code> and <code>fit=crop</code>. By default, Cloudflare will crop toward the center point of the original image.</p>
<p>Accepts <code>auto</code>, <code>face</code>, a side (<code>left</code>, <code>right</code>, <code>top</code>, <code>bottom</code>), and relative coordinates (<code>XxY</code>).</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9405.md")
</div></div>
<h4 id="auto"><code>auto</code></h4>
Automatically sets the focal point by using a saliency algorithm to detect the most visually interesting pixels.
<p>This is useful when you don't know the contents of the image ahead of time, such as with user-generated content. For large image libraries such as e-commerce product galleries, this feature eliminates the need to manually set a focal point for each image.</p>
<table style="width:100%; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/gravity/coffee-base.jpg" alt="original image" />
</td>
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/gravity/coffee-crop.jpg" alt="output without gravity=auto" />
</td>
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/gravity/coffee-auto.jpg" alt="output with gravity=auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
      <strong>Default crop</strong>
</td>
<td style="border:none;">
      `gravity=auto`
</td>
</tr>
</table>
<h4 id="face"><code>face</code></h4>
Automatically sets the focal point based on faces in the image.
<p>This can be combined with the <a href="/images/optimization/features#zoom"><code>zoom</code></a> parameter to specify how closely the image should be cropped toward the face.</p>
<table style="width:100%; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/gravity/suad-kamardeen.jpeg" alt="original image" />
</td>
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/gravity/suad-kamardeen-crop.jpeg" alt="output without gravity=face" />
</td>
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/gravity/suad-kamardeen-face.jpeg" alt="output with gravity=face" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
      <strong>Default crop</strong>
</td>
<td style="border:none;">
      `gravity=face`
</td>
</tr>
</table>
<p><em>Photograph by <a href="https://unsplash.com/photos/woman-in-black-cardigan-standing-beside-pink-flowers-UO-82DJ3rcc">Suad Kamardeen (@suadkamardeen) on Unsplash</a></em></p>
<style>{`
  .gravity-xxy-table img {
    height: 180px !important;
    width: auto !important;
    max-width: none !important;
    margin: 0 !important;
  }
`}</style>
<h4 id="left-right-top-bottom"><code>left</code>, <code>right</code>, <code>top</code>, <code>bottom</code></h4>
Sets the side of the image that should not be cropped.
<p>In the example below, the 1080x720 image is cropped to a 1080x400 area, starting from its bottom edge:</p>
<table style="width:100%; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/fit/pete-landscape.jpg" alt="original image" />
</td>
<td style="border:none; width:33%; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/gravity/pete-bottom.jpg" alt="output without gravity=auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
      `gravity=bottom`
</td>
</tr>
</table>
<h4 id="xxy"><code>XxY</code></h4>
Sets the focal point (X,Y) so that the relative coordinates of the output image are positioned at the relative coordinates of the original image. Accepts a coordinate pair formatted as `XxY`, where X and Y are decimal values between `0.0` and `1.0`.
<p><img src="/assets/upstream/images/images/examples/gravity/xxy.png" alt="Change the focal point using the relative coordinates" /></p>
<ul>
<li><strong>Horizontal value (X)</strong> — <code>0.0</code> is the left edge and <code>1.0</code> is the right edge of the image.</li>
<li><strong>Vertical value (Y)</strong> — <code>0.0</code> is the top edge and <code>1.0</code> is the bottom edge of the image.</li>
</ul>
<p>The example below crops a 900x900 image to 300x900 using a 0.33x0.5 gravity point:</p>
<ul>
<li>Both the original image and target area will have gravity points set at 1/3 of the width from the left edge and 1/2 of the height from the top edge.</li>
<li>The relative coordinates of the output gravity point are positioned at the relative coordinates of the original image. That is, the target area is positioned so that its gravity point sits at the same relative position in the original image (0.33, 0.5).</li>
<li>The darkened parts of the image show the area outside of the requested output, which will be cropped.</li>
<li>The final cropped result captures the 300x900 content that is around the gravity point (0.33, 0.5).</li>
</ul>
<table class="gravity-xxy-table" style="text-align:center; border:none">
<tr style="border:none; background:none">
<td style="border:none; vertical-align:middle">
<img src="/assets/upstream/images/images/examples/gravity/base.png" alt="original image" />
</td>
<td style="border:none; vertical-align:middle">
<img src="/assets/upstream/images/images/examples/gravity/rel-points.png" alt="align gravity points on original and target area" />
</td>
<td style="border:none; vertical-align:middle">
<img src="/assets/upstream/images/images/examples/gravity/rel-alignment.png" alt="crop using new gravity point" />
</td>
<td style="border:none; vertical-align:middle">
<img src="/assets/upstream/images/images/examples/gravity/rel-output.png" alt="final output" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong><br />
</td>
<td style="border:none;">
      <strong>Align</strong><br />
</td>
<td style="border:none;">
      <strong>Crop</strong><br />
</td>
<td style="border:none;">
      <strong>Output</strong><br />
</td>
</tr>
</table>
<p>When optimizing through Workers, use an object <code>{x, y}</code> to specify coordinates. For example, <code>{fit: &quot;cover&quot;, gravity: {x:0.5, y:0.2}}</code> will crop each side to preserve as much as possible around a point at 20% of the height of the original image.</p>
<p><a id="height"></a></p>
<h3 id="height-h"><code>height</code> | <code>h</code></h3>
<p>Sets the height of the output image in pixels using a positive integer value. By default, Cloudflare uses the original height of the input image.</p>
<p>When <code>height</code> is set, the exact behavior depends on the <code>fit</code> parameter.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9408.md")
</div></div>
<h3 id="metadata"><code>metadata</code></h3>
<p>Controls the amount of invisible metadata (EXIF) that should be preserved for a JPEG image. For all other output formats (e.g. WebP or PNG), all metadata will always be discarded.</p>
<p>Color profiles and EXIF rotation are applied to the image even if the metadata is discarded.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9361.md")
</aside>
<p>Accepts the following values:</p>
<ul>
<li><code>copyright</code> (default) — Discards all metadata except EXIF copyright tag.</li>
<li><code>keep</code> — Preserves most of EXIF metadata, including GPS location, if present.</li>
<li><code>none</code> — Discards all invisible EXIF metadata.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9411.md")
</div></div>
<h3 id="onerror"><code>onerror</code></h3>
<p>Redirects the end-user to the URL of the original source image when a fatal error prevents the image from being transformed. Accepts <code>redirect</code>. The default is none.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9360.md")
</aside>
<p>This option works only if the image is in the same zone (subdomains are accepted). If the original image is from a different zone, then the option does not have any effect.</p>
<p>This may be useful in cases where an image requires user authentication and the image cannot be fetched anonymously via Workers. However, this option is not recommended if the source image is very large.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9413.md")
</div></div>
<p><a id="quality"></a></p>
<h3 id="quality-q"><code>quality</code> | <code>q</code></h3>
<p>Specifies the output quality of an image for JPEG, WebP, and AVIF formats, expressed as a fixed value or perceptual quality level. The default is <code>85</code>.</p>
<ul>
<li><strong>Fixed quality</strong> — Accepts a positive integer from <code>1</code> (low quality, small file size) to <code>100</code> (high quality, large file size).</li>
<li><strong>Perceptual quality</strong> — Accepts <code>high</code>, <code>medium-high</code>, <code>medium-low</code>, and <code>low</code>.</li>
</ul>
<p>When the output format is PNG, an explicit <code>quality</code> setting allows the use of PNG8 (palette) variant of the format.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9416.md")
</div></div>
<h3 id="rotate"><code>rotate</code></h3>
<p>Rotates an image by a number of degrees. Accepts <code>90</code>, <code>180</code>, or <code>270</code>. The default is <code>0</code> (no rotation).</p>
<p>Rotation is performed before resizing; <code>width</code> and <code>height</code> options will refer to the axes after the image is rotated.</p>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/original.jpg" alt="Original image" style="width:100%; height:auto" />
</td>
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/rotate-180.jpg" alt="rotate=180 output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;rotate=180&lt;/code&gt;&#10;</code></pre>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9419.md")
</div></div>
<h3 id="saturation"><code>saturation</code></h3>
<p>Adjusts the color saturation of an image using a multiplier.</p>
<ul>
<li><code>0</code> — Completely desaturates the image (grayscale).</li>
<li><code>&lt; 1.0</code> — Reduces color intensity. For example, <code>0.5</code> is half as saturated.</li>
<li><code>1</code> (default) — No change to the original saturation.</li>
<li><code>&gt; 1.0</code> — Increases color intensity. For example, <code>2</code> is twice as saturated.</li>
</ul>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/original.jpg" alt="Original image" style="width:100%; height:auto" />
</td>
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/saturation-0.jpg" alt="saturation=0 output" style="width:100%; height:auto" />
</td>
<td style="width:33%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/saturation-2.jpg" alt="saturation=2 output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;saturation=0&lt;/code&gt;&#10;</code></pre>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;saturation=2&lt;/code&gt;&#10;</code></pre>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9422.md")
</div></div>
<h3 id="segment"><code>segment</code></h3>
<p>Automatically isolates the subject of an image by replacing the background with transparent pixels. Accepts <code>foreground</code>. The default is none.</p>
<p>This feature uses an open-source model called BiRefNet through <a href="/workers-ai/">Workers AI</a>. Read more about Cloudflare's <a href="https://www.cloudflare.com/trust-hub/responsible-ai/">approach to responsible AI</a>.</p>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/original.jpg" alt="Original image" style="width:100%; height:auto" />
</td>
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/segment-foreground.png" alt="segment=foreground output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;segment=foreground&lt;/code&gt;&#10;</code></pre>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9425.md")
</div></div>
<h3 id="sharpen"><code>sharpen</code></h3>
<p>Applies a sharpening filter to enhance edge definition in an image. Accepts a decimal value from <code>0</code> (no sharpening) to <code>10</code> (maximum sharpening). The default is <code>0</code>. The recommended value for downscaled images is <code>1</code>.</p>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/original.jpg" alt="Original image" style="width:100%; height:auto" />
</td>
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/sharpen-5.jpg" alt="sharpen=5 output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
      <strong>Original</strong>
</td>
<td style="border:none;">
<pre tabindex="0"><code>  &lt;code&gt;sharpen=5&lt;/code&gt;&#10;</code></pre>
</td>
</tr>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9428.md")
</div></div>
<p><a id="slow-connection-quality"></a></p>
<h3 id="slow-connection-quality-scq"><code>slow-connection-quality</code> | <code>scq</code></h3>
<p>Overrides the <code>quality</code> value whenever a slow connection is detected. Accepts the same fixed or perceptual settings as <a href="#quality">quality</a>. The default is none.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9359.md")
</aside>
<p>To detect slow connections, enable any of the following client hints via HTTP in a header:</p>
<pre tabindex="0"><code class="language-txt">accept-ch: rtt, save-data, ect, downlink&#10;</code></pre>
<p><code>slow-connection-quality</code> applies when the client hint is present and any of the following conditions are met:</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/RTT">rtt</a>: Greater than 150ms.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Save-Data">save-data</a>: Value is &quot;on&quot;.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/ECT">ect</a>: Value is one of <code>slow-2g|2g|3g</code>.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Downlink">downlink</a>: Less than 5Mbps.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9430.md")
</div></div>
<h3 id="trim"><code>trim</code></h3>
<p>Removes pixels around the sides of an image.</p>
<p>This feature can be used to trim an image by its border colors or by a specified number of pixels from its side(s).</p>
<p>Trim takes into account the <a href="#dpr"><code>dpr</code></a> parameter and is performed before resizing and rotation.</p>
<h4 id="border-1"><code>border</code></h4>
<p>Automatically trims the sides of the image based on its border color.</p>
<p>The <code>trim=border</code> option can be further adjusted using the following parameters:</p>
<ul>
<li><code>trim.border.color</code> — Selects the border color to trim. Accepts any CSS color using CSS4 modern syntax. If omitted, the color is detected automatically.</li>
<li><code>trim.border.tolerance</code> — Sets how closely the detected pixels must match in color. Accepts an integer between <code>0</code> (doesn't need to match) and 255 (must match exactly).</li>
<li><code>trim.border.keep</code> — Specifies the number of pixels of the original border to leave untrimmed.</li>
</ul>
<h4 id="top-right-bottom-left"><code>top;right;bottom;left</code></h4>
<p>Specifies the number of pixels to remove from the sides of an image. Accepts four values, separated by a semicolon, to set the trim on all four sides of an image at once.</p>
<p>All trim values accept either an integer (pixel count) or a decimal between <code>0</code> and <code>1</code> representing a fraction of the image dimension. For example, <code>0.25</code> trims 25% from that side.</p>
<p>Trim can also be applied to a specific side using the following parameters:</p>
<ul>
<li><code>trim.top</code> — Removes pixels from the top of the image.</li>
<li><code>trim.left</code> — Removes pixels from the left of the image.</li>
<li><code>trim.height</code> — Sets the height of the image from the top edge, then trims everything below.</li>
<li><code>trim.width</code> — Sets the width of the image from the left edge, then trims everything to the right.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9433.md")
</div></div>
<h3 id="upscale"><code>upscale</code></h3>
<p>Controls the algorithm used when an image needs to be enlarged. This parameter works with any <a href="#fit"><code>fit</code></a> mode that upscales, such as <a href="#contain"><code>contain</code></a>, <a href="#cover"><code>cover</code></a>, and <a href="#scale-up"><code>scale-up</code></a>. It has no effect when <code>fit=scale-down</code> or when the target dimensions are smaller than the source.</p>
<p>Accepts the following values:</p>
<ul>
<li><code>interpolate</code> (default) — Uses bicubic interpolation, which may reduce image quality. This is the default behavior when <code>upscale</code> is not specified.</li>
<li><code>generate</code> — Uses AI upscaling (<a href="https://github.com/xinntao/ESRGAN">ESRGAN</a>) to produce sharper, more detailed results when enlarging images.</li>
</ul>
<p>When <code>upscale=generate</code> is specified, the AI model runs a single pass at the nearest supported scale (2x or 4x), then adjusts to the exact target dimensions. Scale factors beyond 4x are handled with AI upscaling to 4x, then bicubic interpolation for the remainder.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9358.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9436.md")
</div></div>
<p><a id="width"></a></p>
<h3 id="width-w"><code>width</code> | <code>w</code></h3>
<p>Sets the width of the output image in pixels using a positive integer value. By default, Cloudflare uses the original width of the input image.</p>
<p>When <code>width</code> is set, the exact behavior depends on the <code>fit</code> parameter.</p>
<p>Accepts the following values:</p>
<ul>
<li>A number in pixels (for example, <code>250</code>).</li>
<li><code>auto</code> — Automatically serves the image in the most optimal width based on available information about the browser and device. Accepts <code>wbreakpoints</code> (client hints), <code>wmobile</code> (user-agent detection), and <code>wdesktop</code> (user-agent detection) as sub-parameters.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9439.md")
</div></div>
<h4 id="width-auto-sub-parameters"><code>width=auto</code> sub-parameters</h4>
<p>When <code>width=auto</code> is specified, Cloudflare resizes the image using information from client hints (sent by the browser) or by user-agent detection as a fallback.</p>
<p>You can customize the <code>width=auto</code> behavior with the following sub-parameters:</p>
<table>
<thead>
<tr>
<th>Sub-parameter</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wbreakpoints</code></td>
<td>Override default breakpoint widths, in pixels (client hints)</td>
<td><code>320;768;960;1200</code></td>
</tr>
<tr>
<td><code>wmobile</code></td>
<td>Override default width, in pixels, for mobile devices (user-agent detection)</td>
<td><code>768</code></td>
</tr>
<tr>
<td><code>wdesktop</code></td>
<td>Override default width, in pixels, for desktop devices (user-agent detection)</td>
<td><code>1200</code></td>
</tr>
</tbody>
</table>
<p>When optimizing remote images with <code>width=auto</code>, each unique width counts as a separate <a href="/images/pricing/#images-transformed">billable transformation</a>.</p>
<p>To learn how <code>width=auto</code> works, refer to our guide on <a href="/images/optimization/make-responsive-images/">serving responsive images</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9442.md")
</div></div>
<p><a id="zoom"></a></p>
<h3 id="zoom-face-zoom"><code>zoom</code> | <code>face-zoom</code></h3>
<p>Specifies how closely the image is cropped toward detected faces when combined with the <code>gravity=face</code> option. Accepts a valid range between <code>0.0</code> (includes as much of the background as possible) and <code>1.0</code> (crops the image as closely to the face as possible). The default is <code>0</code>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9445.md")
</div></div>
<h2 id="recommended-image-sizes">Recommended image sizes</h2>
<p>Ideally, image sizes should match the exact size that they are displayed on the page. If the page contains thumbnails with markup such as <code>&lt;img width=&quot;200&quot; …&gt;</code>, then images should be resized to <code>width=200</code>.</p>
<p>To <a href="/images/optimization/make-responsive-images/">serve responsive images</a>, you can use the HTML <code>srcset</code> attribute to let the provider pick the most optimal size. If you can't use the <code>&lt;img srcset&gt;</code> markup and have to hardcode specific maximum sizes, Cloudflare recommends the following sizes:</p>
<ul>
<li>Maximum of 1920 pixels for desktop browsers.</li>
<li>Maximum of 960 pixels for tablets.</li>
<li>Maximum of 640 pixels for mobile phones.</li>
</ul>
<p>For example, <code>fit=scale-down,width=1920</code> sets a maximum size of 1920px and ensures that the image will not be enlarged unnecessarily.</p>
<p>You can detect device type by enabling the <code>CF-Device-Type</code> header <a href="/cache/how-to/cache-rules/examples/cache-device-type/">via Cache Rule</a>.</p>
<h2 id="caching">Caching</h2>
<p>When you optimize with Images, the original image will be fetched from the origin server and cached — following the usual rules of HTTP caching, <code>Cache-Control</code> header, etc.. Requests for multiple different image sizes are likely to reuse the cached original image without causing extra transfers from the origin server.</p>
<p>If <a href="/cache/how-to/cache-keys/">Custom Cache Keys</a> are used for the origin image, the origin image might not be cached and might result in more calls to the origin.</p>
<p>Optimized images follow the same caching rules as the original image they were resized from, except the minimum cache time is one hour. If you need images to be updated more frequently, add <code>must-revalidate</code> to the <code>Cache-Control</code> header. The Images service supports cache revalidation, so we recommend serving images with the <code>Etag</code> header. Refer to the <a href="/cache/concepts/cache-control/#revalidation">Cache docs for more information</a>.</p>
<p>Cloudflare does not support purging optimized images individually. URLs starting with <code>/cdn-cgi/</code> cannot be purged. However, purging of the original image's URL will also purge all of its optimized versions.</p>
