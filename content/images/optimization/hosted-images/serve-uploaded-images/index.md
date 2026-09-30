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
