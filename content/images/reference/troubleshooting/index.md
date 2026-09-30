<h2 id="requests-without-resizing-enabled">Requests without resizing enabled</h2>
<p>Does the response have a <code>Cf-Resized</code> header? If not, then resizing has not been attempted. Possible causes:</p>
<ul>
<li>The feature is not enabled in the Cloudflare Dashboard.</li>
<li>There is another Worker running on the same request. Resizing is &quot;forgotten&quot; as soon as one Worker calls another. Do not use Workers scoped to the entire domain <code>/*</code>.</li>
<li>Preview in the Editor in Cloudflare Dashboard does not simulate image resizing. You must deploy the Worker and test from another browser tab instead.</li>
</ul>
<hr />
<h2 id="error-responses-from-resizing">Error responses from resizing</h2>
<p>When resizing fails, the response body contains an error message explaining the reason, as well as the <code>Cf-Resized</code> header containing <code>err=code</code>:</p>
<ul>
<li>9401 — The required arguments in <code>{cf:image{…}}</code> options are missing or are invalid. Try again. Refer to <a href="/images/optimization/features/#parameters">Fetch options</a> for supported arguments.</li>
<li>9402 — The image was too large or the connection was interrupted. Refer to <a href="/images/get-started/limits/">Supported formats and limitations</a> for more information.</li>
<li>9403 — A <a href="/images/optimization/transformations/transform-via-workers/#prevent-request-loops">request loop</a> occurred because the image was already resized or the Worker fetched its own URL. Verify your Worker path and image path on the server do not overlap.</li>
<li>9406 &amp; 9419 — The image URL is a non-HTTPS URL or the URL has spaces or unescaped Unicode. Check your URL and try again.</li>
<li>9407 — A lookup error occurred with the origin server's domain name. Check your DNS settings and try again.</li>
<li>9404 — The image does not exist on the origin server or the URL used to resize the image is wrong. Verify the image exists and check the URL.</li>
<li>9408 — The origin server returned an HTTP 4xx status code and may be denying access to the image. Confirm your image settings and try again.</li>
<li>9509 — The origin server returned an HTTP 5xx status code. This is most likely a problem with the origin server-side software, not the resizing.</li>
<li>9412 — The origin server returned a non-image, for example, an HTML page. This usually happens when an invalid URL is specified or server-side software has printed an error or presented a login page.</li>
<li>9413 — The image exceeds the maximum image area of 100 megapixels. Use a smaller image and try again.</li>
<li>9420 — The origin server redirected to an invalid URL. Confirm settings at your origin and try again.</li>
<li>9421 — The origin server redirected too many times. Confirm settings at your origin and try again.</li>
<li>9422 - The transformation request is rejected because the usage limit was reached. If you need to request more than 5,000 unique transformations, upgrade to an Images Paid plan.</li>
<li>9432 — The Images Binding is not available using legacy billing. Your account is using the legacy Image Resizing subscription. To bind Images to your Worker, you will need to update your plan to the Images subscription in the dashboard.</li>
<li>9504, 9505, &amp; 9510 — The origin server could not be contacted because the origin server may be down or overloaded. Try again later.</li>
<li>9523 — The <code>/cdn-cgi/image/</code> resizing service could not perform resizing. This may happen when an image has invalid format. Use correctly formatted image and try again.</li>
<li>9524 — The <code>/cdn-cgi/image/</code> resizing service could not perform resizing. This may happen when an image URL is intercepted by a Worker. As an alternative you can <a href="/images/optimization/transformations/transform-via-workers/">resize within the Worker</a>. This can also happen when using a <code>pages.dev</code> URL of a <a href="/pages/">Cloudflare Pages</a> project. In that case, you can use a <a href="/pages/configuration/custom-domains/">Custom Domain</a> instead.</li>
<li>9520 — The image format is not supported. Refer to <a href="/images/get-started/limits/">Supported formats and limitations</a> to learn about supported input and output formats.</li>
<li>9522 — The image exceeded the processing limit. This may happen briefly after purging an entire zone or when files with very large dimensions are requested. If the problem persists, contact support.</li>
<li>9529 - The image timed out while processing. This may happen when files with very large dimensions are requested or the server is overloaded.</li>
<li>9424, 9516, 9517, 9518 — Internal errors. Please contact support if you encounter these errors.</li>
</ul>
<hr />
<h2 id="limits">Limits</h2>
<p>These are the limits for images that are stored outside of Images:</p>
<ul>
<li>Maximum image size is 100 megapixels (for example, 10,000×10,000 pixels large). Maximum file size is 100 megabytes (MB). GIF/WebP animations are limited to 50 megapixels total (sum of sizes of all frames).</li>
<li><a href="/byoip/">Bring Your Own IP (BYOIP)</a> is not compatible with Images when optimizing remote images (transformations).</li>
<li>When <a href="/images/polish/">Polish</a> can't optimize an image the Response Header <code>Warning: cf-images 299 &quot;original is smaller&quot;</code> is returned.</li>
</ul>
<hr />
<h2 id="authorization-and-cookies-are-not-supported">Authorization and cookies are not supported</h2>
<p>Image requests to the origin will be anonymized (no cookies, no auth, no custom headers). This is because we have to have one public cache for resized images, and it would be unsafe to share images that are personalized for individual visitors.</p>
<p>However, in cases where customers agree to store such images in public cache, Cloudflare supports resizing images through Workers <a href="/images/optimization/transformations/transform-via-workers/">on authenticated origins</a>.</p>
<hr />
<h2 id="caching-and-purging">Caching and purging</h2>
<p>Changes to image dimensions or other resizing options always take effect immediately — no purging necessary.</p>
<p>Image requests consists of two parts: running Worker code, and image processing. The Worker code is always executed and uncached. Results of image processing are cached for one hour or longer if origin server's <code>Cache-Control</code> header allows. Source image is cached using regular caching rules. Resizing follows redirects internally, so the redirects are cached too.</p>
<p>Because responses from Workers themselves are not cached at the edge, purging of <em>Worker URLs</em> does nothing. Resized image variants are cached together under their source’s URL. When purging, use the (full-size) source image’s URL, rather than URLs of the Worker that requested resizing.</p>
<p>If the origin server sends an <code>Etag</code> HTTP header, the resized images will have an <code>Etag</code> HTTP header that has a format <code>cf-&lt;gibberish&gt;:&lt;etag of the original image&gt;</code>. You can compare the second part with the <code>Etag</code> header of the source image URL to check if the resized image is up to date.</p>
