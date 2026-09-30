<h1 id="changelog">Changelog</h1>

<h2 id="new-in-images-text-rasterization-and-updates-to-the-binding"><a href="/changelog/post/2026-09-02-images-binding-updates/">New in Images: text rasterization and updates to the binding</a></h2>
<p><em>2026-09-02</em></p>
<p>We've added more ways to manage and manipulate images with the <a href="/images/optimization/binding/">Images binding</a>. Here's what's new:</p>
<p><strong>Render text into an image.</strong> Output a string of text into its own image or draw it over another image.</p>
<ul>
<li>Use the <a href="/images/optimization/binding/#textcontent-options"><code>.text()</code></a> method to rasterize text with the Images binding.</li>
<li>Style content using the <code>font</code>, <code>size</code>, and <code>color</code> options.</li>
<li>The <a href="/images/optimization/draw-overlays/#draw-with-cfimage"><code>draw</code></a> array in <code>cf.image</code> now accepts a <code>text</code> key.</li>
</ul>
<p><strong>Manage hosted images without an API token.</strong></p>
<ul>
<li><strong>Metadata filtering:</strong> Pass <code>filter.metadata</code> to <a href="/images/storage/binding/#listoptions"><code>.list()</code></a> to return images by custom metadata. Match a bounded range by setting two operators in one condition, for example, <code>priority: { gte: 2, lte: 5 }</code>.</li>
<li><strong>Server-side signing:</strong> Get a signed URL for a private image with <a href="/images/storage/binding/#imageimageidsignedurloptions"><code>.signedUrl()</code></a>.</li>
<li><strong>User uploads:</strong> Create a Direct Creator Upload link with <a href="/images/storage/binding/#createdirectuploadoptions"><code>.createDirectUpload()</code></a> so that a client can upload an image to your storage.</li>
</ul>
<p><strong>Set headers in a single call.</strong></p>
<ul>
<li>Pass a <code>headers</code> option to <a href="/images/optimization/binding/#responseoptions"><code>.response()</code></a> to set headers without rebuilding the <code>Response</code>.</li>
<li><code>Content-Type</code> is always taken from the optimized image and can't be overridden by a specified header.</li>
<li>Set <code>Cache-Control</code> with <a href="/workers/cache/">Workers Cache</a> to cache your optimized image at the edge.</li>
</ul>
<p>For more information, refer to <a href="/images/optimization/binding/">Optimize with Workers</a>, <a href="/images/optimization/draw-overlays/">Draw overlays and watermarks</a>, and <a href="/images/storage/binding/">Manage hosted images with Workers</a>.</p>


<h2 id="images-binding-is-now-billed-per-unique-transformation"><a href="/changelog/post/2026-07-01-binding-unique-transformations/">Images binding is now billed per unique transformation</a></h2>
<p><em>2026-07-01</em></p>
<p>The <a href="/images/optimization/binding/">Images binding</a> is now billed per unique transformation, matching the model already used for URL-based transformations. Repeat requests for the same combination of source image and parameters within the same calendar month are counted only once.</p>
<p>Previously, every call to the binding counted as a separate transformation regardless of whether the image or parameters were unique. With this change, you can call the binding on hot paths without paying for each individual request.</p>
<p>Calls to <a href="/images/optimization/binding/#infostream"><code>.info()</code></a> are no longer billed.</p>
<p>For more information, refer to <a href="/images/pricing/#images-transformed">Images pricing</a> and the <a href="/images/optimization/binding/">Images binding documentation</a>.</p>


<h2 id="new-optimization-features-in-images"><a href="/changelog/post/2026-06-16-new-optimization-features/">New optimization features in Images</a></h2>
<p><em>2026-06-16</em></p>
<p>These updates introduce new features for optimizing and manipulating with Images:</p>
<ul>
<li><strong>New <code>composite</code> option:</strong> Control how <a href="/images/optimization/draw-overlays/#composite">overlays are blended</a> with the base image.</li>
<li><strong>Percentage widths:</strong> Set the dimensions of an overlay as <a href="/images/optimization/draw-overlays/#width-and-height">a fraction of the dimensions</a> of the base image.</li>
<li><strong>New <code>fit</code> modes:</strong> Use <a href="/images/optimization/features/#aspect-crop"><code>aspect-crop</code></a> to always preserve the target aspect ratio or <a href="/images/optimization/features/#scale-up"><code>scale-up</code></a> to always enlarge images.</li>
<li><strong>New <code>upscale</code> parameter:</strong> Apply <a href="/images/optimization/features/#upscale">AI upscaling</a> to produce sharper, more detailed results when enlarging images.</li>
</ul>


<h2 id="manage-hosted-images-with-the-images-binding"><a href="/changelog/post/2026-06-10-hosted-images-binding/">Manage hosted images with the Images binding</a></h2>
<p><em>2026-06-10</em></p>
<p>Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests.</p>
<p>The <code>env.IMAGES.hosted</code> namespace supports the following storage and management operations:</p>
<ul>
<li><a href="/images/storage/binding/#uploadimage-options"><code>.upload(image, options)</code></a> — Upload a new image to your account.</li>
<li><a href="/images/storage/binding/#listoptions"><code>.list(options)</code></a> — List images with pagination.</li>
<li><a href="/images/storage/binding/#imageimageiddetails"><code>.image(imageId).details()</code></a> — Get image metadata.</li>
<li><a href="/images/storage/binding/#imageimageidbytes"><code>.image(imageId).bytes()</code></a> — Stream the original image bytes.</li>
<li><a href="/images/storage/binding/#imageimageidupdateoptions"><code>.image(imageId).update(options)</code></a> — Update metadata or access controls.</li>
<li><a href="/images/storage/binding/#imageimageiddelete"><code>.image(imageId).delete()</code></a> — Delete an image.</li>
</ul>
<p>For example, you can upload an image from a request body and return its metadata:</p>
<pre><code class="language-ts">const image = await env.IMAGES.hosted.upload(request.body, {&#10;	filename: &quot;upload.jpg&quot;,&#10;	metadata: { source: &quot;worker&quot; },&#10;});&#10;&#10;return Response.json(image);&#10;</code></pre>
<p>Or retrieve and serve the original bytes of a hosted image:</p>
<pre><code class="language-ts">const bytes = await env.IMAGES.hosted.image(&quot;IMAGE_ID&quot;).bytes();&#10;return new Response(bytes);&#10;</code></pre>
<p>For more information, refer to the <a href="/images/storage/binding/">Images binding</a>.</p>


<h2 id="transformation-flows-in-images"><a href="/changelog/post/2026-05-27-transformation-flows/">Transformation flows in Images</a></h2>
<p><em>2026-05-27</em></p>
<p><img src="/assets/upstream/images/images/custom-flow.png" alt="Custom flow configuration panel" /></p>
<p>Flows are automated rules that pair conditions (such as file extension, URL path, or query parameter) with parameters. Set up a flow to automatically apply image optimization to matching requests on your zone without writing code or changing URLs.</p>
<p>There are two modes for transformation flows:</p>
<ul>
<li><strong><a href="/images/optimization/transformations/flows/#set-up-a-provider-flow">Provider flows</a></strong> — Migrate from another image optimization service. Your existing URLs continue to work while Cloudflare rewrites provider-specific parameters to their Cloudflare equivalents. Currently, Cloudflare supports provider flows for Fastly Image Optimizer.</li>
<li><strong><a href="/images/optimization/transformations/flows/#set-up-a-custom-flow">Custom flows</a></strong> — Define your own conditions and actions for use cases like automatic format conversion, <a href="/images/optimization/make-responsive-images/#using-widthauto">responsive sizing</a> with <code>width=auto</code>, or directory-based optimization.</li>
</ul>
<p>To get started, go to <strong>Images</strong> &gt; <strong>Transformations</strong> &gt; <strong>Automation</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/images/transformations">Cloudflare dashboard</a>.</p>
<p>Learn more about <a href="/images/optimization/transformations/flows/">transformation flows</a>.</p>


<h2 id="heic-support-in-cloudflare-images"><a href="/changelog/post/heic-support/">HEIC support in Cloudflare Images</a></h2>
<p><em>2025-07-08</em></p>
<p>You can use Images to ingest HEIC images and serve them in supported output formats like AVIF, WebP, JPEG, and PNG.</p>
<p>When inputting a HEIC image, dimension and sizing limits may still apply. Refer to our documentation to see limits for <a href="/images/storage/upload-images/methods/">uploading to Images</a> or <a href="/images/optimization/transformations/overview/">transforming a remote image</a>.</p>


<h2 id="bind-the-images-api-to-your-worker"><a href="/changelog/post/2025-02-21-images-bindings-in-workers/">Bind the Images API to your Worker</a></h2>
<p><em>2025-02-24</em></p>
<p>You can now <a href="/images/optimization/binding/">interact with the Images API</a> directly in your Worker.</p>
<p>This allows more fine-grained control over transformation request flows and cache behavior. For example, you can resize, manipulate, and overlay images without requiring them to be accessible through a URL.</p>
<p>The Images binding can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17735.md")</div>
<p>Within your Worker code, you can interact with this binding by using <code>env.IMAGES</code>.</p>
<p>Here's how you can rotate, resize, and blur an image, then output the image as AVIF:</p>
<pre><code class="language-ts">const info = await env.IMAGES.info(stream);&#10;// stream contains a valid image, and width/height is available on the info object&#10;&#10;const response = (&#10;	await env.IMAGES.input(stream)&#10;		.transform({ rotate: 90 })&#10;		.transform({ width: 128 })&#10;		.transform({ blur: 20 })&#10;		.output({ format: &quot;image/avif&quot; })&#10;).response();&#10;&#10;return response;&#10;</code></pre>
<p>For more information, refer to <a href="/images/optimization/binding/">Images Bindings</a>.</p>



