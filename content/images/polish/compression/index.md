<p>With Lossless and Lossy modes, Cloudflare attempts to strip as much metadata as possible. However, Cloudflare cannot guarantee stripping all metadata because other factors, such as caching status, might affect which metadata is finally sent in the response.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/9355.md")
</aside>
<h2 id="compression-options">Compression options</h2>
<h3 id="off">Off</h3>
<p>Polish is disabled and no compression is applied. Disabling Polish does not revert previously polished images to original, until they expire or are purged from the cache.</p>
<h3 id="lossless">Lossless</h3>
<p>The Lossless option attempts to reduce file sizes without changing any of the image pixels, keeping images identical to the original. It removes most metadata, like EXIF data, and losslessly recompresses image data. JPEG images may be converted to progressive format. On average, lossless compression reduces file sizes by 21 percent compared to unoptimized image files.</p>
<p>The Lossless option prevents conversion of JPEG to WebP, because this is always a lossy operation.</p>
<h3 id="lossy">Lossy</h3>
<p>The Lossy option applies significantly better compression to images than the Lossless option, at a cost of small quality loss. When uncompressed, some of the redundant information from the original image is lost. On average, using Lossy mode reduces file sizes by 48 percent.</p>
<p>This option also removes metadata from images. The Lossy option mainly affects JPEG images, but PNG images may also be compressed in a lossy way, or converted to JPEG when this improves compression.</p>
<h3 id="webp">WebP</h3>
<p>When enabled, in addition to other optimizations, Polish creates versions of images converted to the WebP format.</p>
<p>WebP compression is quite effective on PNG images, reducing file sizes by approximately 26 percent.
It may reduce file sizes of JPEG images by around 17 percent, but this <a href="/images/polish/no-webp/">depends on several factors</a>.
WebP is supported in all browsers except for Internet Explorer and KaiOS. You can learn more in our <a href="https://blog.cloudflare.com/a-very-webp-new-year-from-cloudflare/">blog post</a>.</p>
<p>The WebP version is served only when the <code>Accept</code> header from the browser includes WebP, and the WebP image is significantly smaller than the lossy or lossless recompression of the original format:</p>
<pre><code class="language-txt">Accept: image/avif,image/webp,image/*,*/*;q=0.8&#10;</code></pre>
<p>Polish only converts standard image formats <em>to</em> the WebP format. If the origin server serves WebP images, Polish will not convert them, and will not optimize them.</p>
<h4 id="file-size-image-quality-and-webp">File size, image quality, and WebP</h4>
<p>Lossy formats like JPEG and WebP are able to generate files of any size, and every image could theoretically be made smaller. However, reduction in file size comes at a cost of reduction in image quality. Reduction of file sizes below each format's optimal size limit causes disproportionally large losses in quality. Re-encoding of files that are already optimized reduces their quality more than it reduces their file size.</p>
<p>Cloudflare will not convert from JPEG to WebP when the conversion would make the file bigger, or would reduce image quality by more than it would save in file size.</p>
<p>If you choose the Lossless Polish setting, then WebP will be used very rarely. This is due to the fact that, in this mode, WebP is only adequate for PNG images, and cannot improve compression for JPEG images.</p>
<p>Although WebP compresses better than JPEG on average, there are exceptions, and in some occasions JPEG compresses better than WebP. Cloudflare tries to detect these cases and keep the JPEG format.</p>
<p>If you serve low-quality JPEG images at the origin (quality setting 60 or lower), it may not be beneficial to convert them to WebP. This is because low-quality JPEG images have blocky edges and noise caused by compression, and these distortions increase file size of WebP images. We recommend serving high-quality JPEG images (quality setting between 80 and 90) at your origin server to avoid this issue.</p>
<p>If your server or Content Management System (CMS) has a built-in image converter or optimizer, it may interfere with Polish. It does not make sense to apply lossy optimizations twice to images, because quality degradation will be larger than the savings in file size.</p>
<h2 id="polish-interaction-with-image-optimization">Polish interaction with Image optimization</h2>
<p>Polish will not be applied to URLs using image transformations. Resized images already have lossy compression applied where possible, so they do not need the optimizations provided by Polish. Use the <code>format=auto</code> option to allow use of WebP and AVIF formats.</p>
