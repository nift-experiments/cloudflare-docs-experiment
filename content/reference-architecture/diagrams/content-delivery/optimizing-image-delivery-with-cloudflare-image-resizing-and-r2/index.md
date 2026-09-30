<h2 id="introduction">Introduction</h2>
<p>Optimizing image delivery for websites is crucial for enhancing user experience. Since images often represent the largest portion of a website's data, they significantly affect page load times, search engine rankings, delivery costs, and overall performance. This reference architecture diagram will guide you through a straightforward, scalable, and high-performance solution. By simply adjusting the URL string to specify image size and quality, you can cache and deliver the optimized image to any user requesting that format. Below are the Cloudflare components involved in this solution:</p>
<ul>
<li><a href="https://www.cloudflare.com/en-gb/application-services/products/cdn/">Cloudflare CDN</a> - Leverage <a href="https://www.cloudflare.com/en-gb/network/">Cloudflare’s Global Network</a> to cache your transformed images for fast and reliable delivery to your end users.</li>
<li><a href="https://www.cloudflare.com/en-gb/developer-platform/cloudflare-images/">Cloudflare Images</a> - Leverage Cloudflare Images to resize, optimize and transform your images that are stored in an object storage solution such as Cloudflare R2. Transformations are performed based on a specifically-formatted URL which requires minimal refactoring to your application to support.</li>
<li><a href="https://www.cloudflare.com/en-gb/developer-platform/r2/">Cloudflare R2 Object Storage</a> - R2 allows users to store a large amount of unstructured data, and in this use case will be used for storing our original images (best quality) for transformation.</li>
<li><a href="/rules/transform/">Cloudflare Transform Rules</a> - If you’re migrating from another solution to Cloudflare, Transform Rules allows you to Rewrite the URL from another solutions syntax to a Cloudflare specific syntax, which reduces the complexity of migration.</li>
</ul>
<h2 id="image-delivery-with-cloudflare-image-resizing-and-r2">Image Delivery with Cloudflare Image Resizing and R2</h2>
<p><img src="/assets/upstream/images/reference-architecture/optimizing-image-delivery-with-cloudflare-image-resizing-and-r2-diagrams/optimizing-image-delivery-with-cloudflare-image-resizing-and-r2-diagram.svg" alt="Figure 1: Cloudflare Image Resizing and R2" title="Figure 1: Cloudflare Image Resizing and R2" /></p>
<ol>
<li><strong>User Request</strong>: The user sends an HTTP request for an image (image.jpg), specifying transformations like width and quality directly in the URL as a comma-separated list of options.</li>
<li><strong>Cache Hit</strong>: Cloudflare processes the request at the point of presence closest to the user. It first checks if the requested image transformation is already in Cloudflare’s Cache. If so, the image is immediately returned to the user, eliminating the need for further processing. If not, the request moves to the next step.</li>
<li><a href="/rules/transform/">Transform Rules</a> (optional): If you’re migrating from another images solution it may be necessary to rewrite the URL path and query string with a rewrite so that you can avoid any complex refactoring at the application level to assist with the migration. Both Dynamic and Static rewrites are supported, with dynamic rewrites supporting complex expressions to support a multitude of URL rewrites.</li>
<li><strong>Cache MISS - R2</strong>: If the requested image is not available in Cloudflare’s Cache, then the request is sent to the origin, which in this scenario is <a href="/r2/">Cloudflare’s R2 Object Storage</a> platform. Only the original images are stored in R2, no resized variants are stored in the R2 bucket, which makes operating R2 without object lifecycle rules less onerous.</li>
<li><strong>Transform Image</strong>: Based on the URL syntax sent in step 1 or transformed in step 3, <a href="/images/">Cloudflare Images</a> transforms the image and sends it to the Cache before serving back to the end user with the requested image.</li>
</ol>
<h2 id="image-resizing-url-syntax-reference">Image Resizing URL Syntax Reference</h2>
<p>You can easily convert and resize images by requesting them through a specifically-formatted URL. This section explains the URL structure for image transformation, referring back to the diagram and detailing each URL component:</p>
<ul>
<li><strong>Part 1</strong> - Your specific domain name on Cloudflare, this is the Zone you onboarded to Cloudflare and where your website or images are served from. e.g. <a href="https://www.mywebsite.com/">https://www.mywebsite.com/</a></li>
<li><strong>Part 2</strong> - A fixed prefix that identifies this is a special path handled by Cloudflare’s built-in Worker.</li>
<li><strong>Part 3</strong> - A comma-separated list of options for the image, such as width=80,quality=75</li>
<li><strong>Part 4</strong> - Absolute path on the origin server. For example: /uploads/image.jpg</li>
</ul>
<p>The final URL used in the request would look like this:</p>
<pre><code class="language-plain">https://www.mywebsite.com/cdn-cgi/image/width=80,quality=75/uploads/image.jpg&#10;</code></pre>
<h2 id="related-resources">Related Resources</h2>
<ul>
<li><a href="/images/optimization/transformations/overview/">Image Resizing Documentation</a></li>
<li><a href="/r2/">Cloudflare R2 Developer Docs</a></li>
<li><a href="/rules/transform/url-rewrite/">URL Rewrite Rules</a></li>
<li><a href="/reference-architecture/diagrams/serverless/serverless-image-content-management/">Serverless image content management platform</a></li>
</ul>
