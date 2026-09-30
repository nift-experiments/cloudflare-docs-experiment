<h2 id="introduction">Introduction</h2>
<p>In this reference architecture diagram, we reveal how to leverage various components of Cloudflare’s ecosystem to construct a scalable image management solution. This solution integrates moderation principles via Cloudflare's Workers AI platform and performs image classification through inference at the edge. The storage of images is handled by Cloudflare's R2 product, an S3 API-like object storage system, while metadata is stored in a key/value store to enable content augmentation.</p>
<p>The servicing of images to requesting clients is secured by link signature, resizing based on device type or requested transformations and leveraging Cloudflare’s native security and performance features.</p>
<p><img src="/assets/upstream/images/reference-architecture/serverless_image_content_management/diagram.svg" alt="Figure 1: Serverless image content management" title="Figure 1: Serverless image content management reference architecture diagram" /></p>
<h3 id="products-included-in-the-recipe">Products included in the recipe</h3>
<table>
<thead>
<tr>
<th>Product</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.cloudflare.com/application-services/products/bot-management/">DDoS</a></td>
<td>Volumetric attack protection</td>
</tr>
<tr>
<td><a href="https://www.cloudflare.com/ddos/">Bot Management</a></td>
<td>Protection against scraping and general sophisticated automated abuse</td>
</tr>
<tr>
<td><a href="https://www.cloudflare.com/application-services/products/waf/">Web Application Firewall</a></td>
<td>Protection against web threats</td>
</tr>
<tr>
<td><a href="https://www.cloudflare.com/application-services/products/cdn/">CDN</a></td>
<td>Cache spreading of the images</td>
</tr>
<tr>
<td><a href="https://www.cloudflare.com/application-services/products/website-optimization/">Optimization</a></td>
<td>Compression and acceleration of the image delivery</td>
</tr>
<tr>
<td><a href="https://workers.cloudflare.com/">Workers</a></td>
<td>Compute of the several serverless micro services</td>
</tr>
<tr>
<td><a href="https://ai.cloudflare.com/">AI</a></td>
<td>Image classification</td>
</tr>
<tr>
<td><a href="https://www.cloudflare.com/developer-platform/r2/">R2</a></td>
<td>S3-type object-storage platform</td>
</tr>
<tr>
<td><a href="/kv/">KV</a></td>
<td>Image metadata storage</td>
</tr>
</tbody>
</table>
<h2 id="getting-started">Getting started</h2>
<p>This reference architecture diagram reveals how to harness the power of the Cloudflare platform to construct a fully serverless image and content management system. This implementation leverages various components of the Cloudflare stack, including edge compute with Cloudflare Workers, KV, and R2 object storage; application performance optimization and caching; application security features such as rate limiting and DDoS mitigation; and artificial intelligence with Workers AI.</p>
<p>The ultimate goal is to create a scalable and accessible platform for storing and serving images globally. This reference architecture will walk you through the key features and mechanisms that you can use with Cloudflare’s native capabilities as well as those that can be built with Cloudflare’s robust computing capabilities.</p>
<h3 id="1-image-servicing"><ol>
<li>Image servicing</li>
</ol></h3>
<p>Clients request images with <a href="/workers/examples/signing-requests/">HMAC signatures</a> and any necessary transformations. Transformation parameters can be included in the <a href="/images/optimization/make-responsive-images/#srcset-for-high-dpi-displays">src-set</a> for HTML content or directly sent alongside <a href="/images/optimization/features/">HTTP requests</a>.</p>
<h3 id="2-volumetric-protection"><ol start="2">
<li>Volumetric protection</li>
</ol></h3>
<p>Cloudflare's Application Security stack takes a comprehensive approach to shielding the image servicing from malicious activities. By implementing volumetric protection <a href="/waf/rate-limiting-rules/">rate limiting controls</a>, we effectively mitigate the risk of abuse and <a href="/ddos-protection/">DDoS</a> attacks, ensuring uninterrupted service delivery.</p>
<h3 id="3-signature-validation"><ol start="3">
<li>Signature validation</li>
</ol></h3>
<p>A <a href="/workers/">Cloudflare worker</a> function validates <a href="/workers/examples/signing-requests/">incoming signatures</a> to ensure the authenticity and integrity of requests. This security measure helps prevent content evasion and abuse of the service by verifying that the signature accompanying the request is legitimate. The application responsible for generating content and associated signatures can also set expiration dates for links, further guarding against tampering or man-in-the-middle attacks. HMAC (Hash-based Message Authentication Code) is commonly used as the signature mechanism of choice for this purpose.</p>
<h3 id="4-image-optimization-and-caching"><ol start="4">
<li>Image optimization and caching</li>
</ol></h3>
<p>Images are retrieved from <a href="/cache/">cache</a> when available or stored on the server for the first time and delivered to clients upon request. We optimize image delivery by serving the most suitable format for each device, such as <a href="/images/polish/">WebP or AVIF</a>, while also applying compression to reduce file size. This ensures a smooth and seamless visual experience for users.</p>
<h3 id="4-image-transformations"><ol start="4">
<li>Image transformations</li>
</ol></h3>
<p>Cloudflare's <a href="/images/">image resizing</a> feature will resize the original images requested for transformation, completing the process entirely at the edge from any of our global locations. This fast and efficient process offers a wide range of transformation options.</p>
<h3 id="5-content-moderation-and-storage"><ol start="5">
<li>Content moderation and storage</li>
</ol></h3>
<p>A <a href="/workers/">Cloudflare Worker</a> script meticulously analyzes incoming images, leveraging their <a href="/workers-ai/models/">classification metadata</a> to ensure compliance with established policy of use. <a href="/r2/">Cloudflare R2</a> serves as an S3-like object storage solution, storing images and their associated metadata (such as image classification) in a globally accessible and scalable manner. With lightning-fast delivery capabilities and the ability to scale from 0, Cloudflare R2 is an ideal solution for storing and managing large collections of images.</p>
<h3 id="6-image-classification"><ol start="6">
<li>Image classification</li>
</ol></h3>
<p>With <a href="https://ai.cloudflare.com/">Cloudflare AI</a> at its core, our <a href="/workers-ai/models/">image classification</a> inference model will rapidly inspect each incoming image, classifying them in real-time. This cutting-edge technology allows us to streamline the process of moderating content, significantly reducing the need for a dedicated team to sift through and review every submission.</p>
