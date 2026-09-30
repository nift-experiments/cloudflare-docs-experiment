---
cp9:
  canonical: https://developers.cloudflare.com/images/optimization/binding/
  description: Use the Images binding to optimize, resize, and manipulate images directly in a Worker from any source.
  full_title: Optimize with Workers · Cloudflare Images docs
  head_html: <title>Optimize with Workers · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Images binding to optimize, resize, and manipulate images directly in a Worker from any source."><link rel="canonical" href="https://developers.cloudflare.com/images/optimization/binding/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/optimization/binding/index.md"><meta property="og:title" content="Optimize with Workers · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Images binding to optimize, resize, and manipulate images directly in a Worker from any source."><meta property="og:url" content="https://developers.cloudflare.com/images/optimization/binding/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Images,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/optimization/binding/#page","headline":"Optimize with Workers \u00b7 Cloudflare Images docs","description":"Use the Images binding to optimize, resize, and manipulate images directly in a Worker from any source.","url":"https://developers.cloudflare.com/images/optimization/binding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/optimization/binding/
  schema: 1
---
<p>A <a href="/workers/runtime-apis/bindings/">binding</a> connects your <a href="/workers/">Worker</a> to external resources on the Developer Platform, like <a href="/images/">Images</a>, <a href="/r2/buckets/">R2 buckets</a>, or <a href="/kv/concepts/kv-namespaces/">KV namespaces</a>.</p>
<p>The Images binding lets you optimize and manipulate images directly in a Worker. Unlike the <a href="/images/optimization/transformations/overview/">URL interface</a>, which requires images to be accessible through a URL, the binding works with raw image bytes. You can pass images from any source, including <a href="/images/storage/upload-images/methods/">Images</a>, <a href="/r2/">R2</a>, a <code>fetch()</code> response, or a request body.</p>
<p>With the Images binding, you can:</p>
<ul>
<li>Optimize an image stored in Images or R2 by passing the bytes directly, instead of fetching through a public URL.</li>
<li>Resize an image, overlay a watermark, then resize the combined output into a final result — all in a single chain of operations.</li>
<li>Control the order of operations for optimization parameters. When you use the URL interface, the optimization parameters follow a fixed order of operations.</li>
</ul>
<p>Bindings can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="billing">Billing</h3>
@markup("md", "content/.markup/bodies/9449.md")
</aside>
<h2 id="setup">Setup</h2>
<p>The Images binding is enabled on a per-Worker basis.</p>
<p>You can define variables in the Wrangler configuration file of your Worker project's directory. These variables are bound to external resources at runtime, and you can then interact with them through this variable.</p>
<p>To bind Images to your Worker, add the following to the end of your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9450.md")
</div>
<p>Within your Worker code, use <code>env.IMAGES.input()</code> to build an object that can manipulate the image (passed as a <code>ReadableStream</code>).</p>
<h2 id="methods">Methods</h2>
<p>An operation starts with a source method — <code>.input()</code> for an image or <code>.text()</code> for text — and ends with <code>.output()</code>. Both source methods return an optimization handle that you can use to chain <code>.transform()</code> and <code>.draw()</code> calls.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="enable-caching">Enable caching</h3>
@markup("md", "content/.markup/bodies/9448.md")
</aside>
<h3 id="input-stream"><code>.input(stream)</code></h3>
<p>Creates an optimization handle for an image. Accepts image bytes up to 20 MB from any source, including <a href="/images/storage/upload-images/methods/">Images</a>, <a href="/r2/">R2</a>, a <code>fetch()</code> response, or a request body.</p>
<p>Returns a handle that you can use to chain <code>.transform()</code>, <code>.draw()</code>, and <code>.output()</code> calls.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9451.md")
</div>
<h3 id="text-content-options"><code>.text(content, options)</code></h3>
<p>Creates an optimization handle for text. Cloudflare rasterizes <code>content</code> into an image using the <code>options</code>. The dimensions of the image are determined by the text string and its styling.</p>
<p>Returns a handle that you can use to chain <code>.transform()</code>, <code>.draw()</code>, and <code>.output()</code> calls. Pass the handle to <code>.draw()</code> to overlay the text on a base image, or call <code>.output()</code> on it directly to produce a standalone image with a transparent background.</p>
<h4 id="content"><code>content</code></h4>
<p>Sets the text string to render. This parameter is required.</p>
<h4 id="options"><code>options</code></h4>
<p>Sets the styling options for the text. These options apply to both the <code>.text()</code> method in the binding and <code>text</code> entries when drawing overlays with the <code>draw</code> array in <code>cf.image</code>.</p>
<p>Accepts the following options:</p>
<ul>
<li><code>font</code> — Sets the font for the text. Accepts an object with a <code>url</code> property that points to a custom TrueType (<code>.ttf</code>), OpenType (<code>.otf</code>), Web Open (<code>.woff</code> and <code>.woff2</code>) font file, up to 20 MB. If the font cannot be fetched or parsed, then the request returns an error.</li>
<li><code>color</code> — Sets the fill color for the text. Accepts a HEX code, a CSS color name, or a CSS color function. The default is <code>#000000</code> (black).</li>
<li><code>size</code> — Sets the font size in pixels. The default is <code>12</code>.</li>
</ul>
<p>The rendered text can be up to 1,000 characters and up to 4096 x 4096 pixels. If a text overlay exceeds these limits, then the request returns an error.</p>
<p>To draw text over an image, refer to <a href="/images/optimization/draw-overlays/">Draw overlays and watermarks</a>.</p>
<h3 id="transform-options"><code>.transform(options)</code></h3>
<p>Applies optimization parameters to the image, such as <code>width</code>, <code>height</code>, or <code>blur</code>. You can chain multiple <code>.transform()</code> calls to control the order that parameters will be applied.</p>
<p>For the full list of parameters, refer to <a href="/images/optimization/features/">Features</a>.</p>
<p>The example below shows how you can resize an image that is <a href="/images/storage/binding/">stored in Images</a> by getting the image bytes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9452.md")
</div>
<h3 id="draw-image-options"><code>.draw(image, options)</code></h3>
<p>Draws an overlay image over another image.</p>
<p>The overlay can be a stream of image bytes or another <code>.input()</code> chain. You can pass a child <code>.transform()</code> function inside this method to resize or manipulate the overlay before drawing it.</p>
<p>Accepts <code>opacity</code>, <code>repeat</code>, a side (<code>left</code>, <code>right</code>, <code>top</code>, <code>bottom</code>), and <code>composite</code>. For the full list of draw options and examples, refer to <a href="/images/optimization/draw-overlays/#options">Draw overlays and watermarks</a>.</p>
<h3 id="output-options"><code>.output(options)</code></h3>
<p>Generates the final image with the specified output options. Returns a result that you can call <a href="/images/optimization/binding/#responseoptions"><code>.response()</code></a> on to return the image from your Worker.</p>
<p>Accepts the following options:</p>
<ul>
<li><code>format</code> — Encodes the image in <a href="/images/get-started/limits/#output-formats">a supported format</a>, such as AVIF, WebP, or JPEG. This method is required — there is no default output format.</li>
<li><code>quality</code> — Specifies the output <a href="/images/optimization/features/#quality--q">quality</a> of an image for JPEG, WebP, and AVIF formats, expressed as a fixed value or perceptual quality level.</li>
<li><code>anim</code> — Specifies whether to <a href="/images/optimization/features/#anim">preserve animation frames</a> from input files. Set <code>anim:false</code> to convert animations to still images.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9453.md")
</div>
<h4 id="response-options"><code>.response(options)</code></h4>
<p>Returns a <code>Response</code> that you can return from your Worker.</p>
<p>Accepts the following options:</p>
<ul>
<li><code>headers</code> — Additional headers to set on the <code>Response</code> as a <a href="/workers/runtime-apis/response/#parameters"><code>HeadersInit</code></a>. Use this to set <code>Cache-Control</code> or other headers directly, instead of rebuilding the <code>Response</code>.</li>
</ul>
<p>The <code>Content-Type</code> is always set from the output format and cannot be overridden.</p>
<h3 id="info-stream"><code>.info(stream)</code></h3>
<p>Outputs information about the image, such as <code>format</code>, <code>fileSize</code>, <code>width</code>, and <code>height</code>.</p>
<h2 id="interact-with-your-images-binding-locally">Interact with your Images binding locally</h2>
<p>The Images API can be used in local development through <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the command-line interface for Workers. Using the Images binding in local development will not incur usage charges.</p>
<p>Wrangler supports two different versions of the Images API:</p>
<ul>
<li>A high-fidelity version that supports all features that are available through the Images API. This is the same version that Cloudflare runs globally in production.</li>
<li>A low-fidelity offline version that supports only a subset of features, such as resizing and rotation.</li>
</ul>
<p>To test the low-fidelity version of Images, you can run <code>wrangler dev</code>:</p>
<pre tabindex="0"><code class="language-txt">npx wrangler dev&#10;</code></pre>
<p>Currently, this version supports only <code>width</code>, <code>height</code>, <code>rotate</code>, and <code>format</code>.</p>
<p>To test the high-fidelity remote version of Images, you can use the <code>--remote</code> flag:</p>
<pre tabindex="0"><code class="language-txt">npx wrangler dev --remote&#10;</code></pre>
<p>When testing with the <a href="/workers/testing/vitest-integration/">Workers Vitest integration</a>, the low-fidelity offline version is used by default, to avoid hitting the Cloudflare API in tests.</p>
