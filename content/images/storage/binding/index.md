---
cp9:
  canonical: https://developers.cloudflare.com/images/storage/binding/
  description: Use the Images binding to upload, list, retrieve, update, and delete hosted images from a Worker.
  full_title: Manage hosted images with Workers · Cloudflare Images docs
  head_html: <title>Manage hosted images with Workers · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Images binding to upload, list, retrieve, update, and delete hosted images from a Worker."><link rel="canonical" href="https://developers.cloudflare.com/images/storage/binding/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/storage/binding/index.md"><meta property="og:title" content="Manage hosted images with Workers · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Images binding to upload, list, retrieve, update, and delete hosted images from a Worker."><meta property="og:url" content="https://developers.cloudflare.com/images/storage/binding/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Images,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/storage/binding/#page","headline":"Manage hosted images with Workers \u00b7 Cloudflare Images docs","description":"Use the Images binding to upload, list, retrieve, update, and delete hosted images from a Worker.","url":"https://developers.cloudflare.com/images/storage/binding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/storage/binding/
  schema: 1
---
<p>A <a href="/workers/runtime-apis/bindings/">binding</a> connects your <a href="/workers/">Worker</a> to external resources on the Developer Platform, like <a href="/images/">Images</a>, <a href="/r2/buckets/">R2 buckets</a>, or <a href="/kv/concepts/kv-namespaces/">KV namespaces</a>.</p>
<p>When managing hosted images, the Images binding lets your Worker upload, list, retrieve, update, and delete hosted images without calling the REST API directly. The <code>hosted</code> namespace exposes storage and management operations. This binding can also be used to <a href="/images/optimization/binding/">optimize hosted images</a>.</p>
<p>Bindings can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="billing">Billing</h3>
@markup("md", "content/.markup/bodies/9342.md")
</aside>
<h2 id="setup">Setup</h2>
<p>To bind Images to your Worker, add the following to your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9343.md")
</div>
<p>Within your Worker code, you can manage hosted images using the <code>env.IMAGES.hosted</code> namespace.</p>
<h2 id="methods">Methods</h2>
<p>The <code>env.IMAGES.hosted</code> namespace lets you upload and list images across your account. To manage a specific image, call <code>.image(imageId)</code> to get a handle, then call a method on it.</p>
<h3 id="upload-image-options"><code>.upload(image, options)</code></h3>
<p>Uploads a new image to your account. You can pass image bytes as a stream or an <code>ArrayBuffer</code>. Returns <a href="#imagemetadata"><code>ImageMetadata</code></a>.</p>
<p>Accepts the following options as an <code>ImageUploadOptions</code> object:</p>
<ul>
<li><code>id</code> <span class="nb-type">string</span> — A custom ID to assign to the image. If omitted, Cloudflare generates a UUID. Refer to <a href="/images/storage/upload-images/upload-custom-path/">Upload to a custom path</a>.</li>
<li><code>filename</code> <span class="nb-type">string</span> — The filename to associate with the image.</li>
<li><code>requireSignedURLs</code> <span class="nb-type">boolean</span> — Sets whether the image should require a signed URL to view. Defaults to <code>false</code>.</li>
<li><code>metadata</code> <span class="nb-type">Record&amp;lt;string, unknown&amp;gt;</span> — Arbitrary metadata to store alongside the image.</li>
<li><code>creator</code> <span class="nb-type">string</span> — A user-defined identifier for the image creator.</li>
<li><code>encoding</code> <span class="nb-type">base64</span> — Set to <code>base64</code> if the provided bytes are base64-encoded. The binding will decode them before upload.</li>
</ul>
<h3 id="createdirectupload-options"><code>.createDirectUpload(options)</code></h3>
<p>Creates a <a href="/images/storage/upload-images/direct-creator-upload/">Direct Creator Upload</a> URL that a client can upload an image to directly without exposing an API token. Returns <a href="#directuploadresult"><code>DirectUploadResult</code></a>.</p>
<p>Accepts the following options as a <code>DirectUploadOptions</code> object:</p>
<ul>
<li><code>id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span> — A custom ID to assign to the image. If omitted, then Cloudflare automatically generates a UUID. Refer to <a href="/images/storage/upload-images/upload-custom-path/">Upload to a custom path</a>.</li>
<li><code>metadata</code> <span class="nb-type">Record&amp;lt;string, unknown&amp;gt;</span> <span class="nb-metainfo">optional</span> — Arbitrary metadata to store alongside the image once it is uploaded.</li>
<li><code>requireSignedURLs</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span> — Sets whether the uploaded image should require a signed URL to view. Defaults to <code>false</code>.</li>
<li><code>creator</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span> — A user-defined identifier for the image creator.</li>
<li><code>expiresIn</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span> — How long the upload URL stays valid, in seconds. Must be between <code>120</code> and <code>21600</code>. Defaults to <code>1800</code>.</li>
</ul>
<h3 id="list-options"><code>.list(options)</code></h3>
<p>Lists images in your account with pagination. Returns <a href="#imagelist"><code>ImageList</code></a>.</p>
<p>Accepts the following options as an <code>ImageListOptions</code> object:</p>
<ul>
<li><code>limit</code> <span class="nb-type">number</span> — The maximum number of images to return in a page.</li>
<li><code>cursor</code> <span class="nb-type">string</span> — The continuation token returned by the previous <code>list()</code> call. Omit on the first page.</li>
<li><code>sortOrder</code> <span class="nb-type">asc' | 'desc</span> — The order to sort results in by <code>uploaded</code> timestamp. Defaults to <code>asc</code>.</li>
<li><code>creator</code> <span class="nb-type">string</span> — Filter results to images uploaded with this creator identifier.</li>
<li><code>filter</code> <span class="nb-type">ImageListFilter</span> — Filter results by image properties. Accepts a <code>metadata</code> field to filter by custom metadata.</li>
</ul>
<h4 id="filter-by-custom-metadata">Filter by custom metadata</h4>
<p>When you list images, you can pass <code>filter.metadata</code> to <code>.list()</code> to return images by their custom metadata fields.</p>
<p>Each entry in <code>filter.metadata</code> is a metadata field name, and its value sets the conditions that the field must meet. When you pass more than one entry, an image must match all of them to be returned.</p>
<p>Field names may contain only letters, numbers, underscores, and dots. If a metadata field name contains other characters, such as hyphens or spaces, then you cannot filter on it.</p>
<p>To filter on a nested field, separate the levels with dot notation, for example, <code>{ &quot;config.region&quot;: &quot;eu-west&quot; }</code> matches <code>{ config: { region: &quot;eu-west&quot; } }</code>. Field paths can be up to five levels deep.</p>
<p>Accepts the following operators as an <code>ImageMetadataFilterOperators</code> object:</p>
<ul>
<li><code>eq</code> <span class="nb-type">string | number | boolean</span> — Matches a field exactly.</li>
<li><code>in</code> <span class="nb-type">Array&amp;lt;string&amp;gt; | Array&amp;lt;number&amp;gt;</span> — Matches a field against any value in an array. An array accepts up to 10 values, and a string value cannot contain the pipe character (<code>|</code>).</li>
<li><code>gt</code> <span class="nb-type">number</span> — Matches a field that is greater than the value.</li>
<li><code>gte</code> <span class="nb-type">number</span> — Matches a field that is greater than or equal to the value.</li>
<li><code>lt</code> <span class="nb-type">number</span> — Matches a field that is less than the value.</li>
<li><code>lte</code> <span class="nb-type">number</span> — Matches a field that is less than or equal to the value.</li>
</ul>
<p>A plain value is shorthand for an exact match, so <code>{ status: &quot;active&quot; }</code> is equivalent to <code>{ status: { eq: &quot;active&quot; } }</code>.</p>
<p>If an entry has multiple conditions, then an image must match every condition to be returned. To match a range, combine two operators on the same entry. For example, <code>{ priority: { gte: 2, lte: 5 } }</code> returns images with a <code>priority</code> from 2 to 5.</p>
<p>A single call accepts up to five conditions. Each operator counts as one condition, so a bounded range such as <code>{ priority: { gte: 2, lte: 5 } }</code> uses two.</p>
<p>A request that references an unsupported field name, uses an unsupported operator, or exceeds five conditions fails rather than returning unfiltered results.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9344.md")
</div>
<h3 id="image-imageid"><code>.image(imageId)</code></h3>
<p>Returns a handle for a single hosted image. The <code>imageId</code> can be the Cloudflare-generated UUID or a <a href="/images/storage/upload-images/upload-custom-path/">custom ID</a>.</p>
<p>The handle itself does not make a network request, so it is cheap to construct.</p>
<h3 id="image-imageid-details"><code>.image(imageId).details()</code></h3>
<p>Gets the metadata for an image. Returns <a href="#imagemetadata"><code>ImageMetadata</code></a> or <code>null</code> if no image with the given ID exists.</p>
<h3 id="image-imageid-bytes"><code>.image(imageId).bytes()</code></h3>
<p>Gets the raw bytes of an image. Returns <code>ReadableStream&lt;Uint8Array&gt;</code> or <code>null</code> if no image with the given ID exists. This streams the original uploaded file. Pass the image bytes to <a href="/images/optimization/binding/"><code>.input()</code></a> to optimize before serving, or use the URLs returned in <a href="#imagemetadata"><code>ImageMetadata.variants</code></a> or the <a href="/images/optimization/hosted-images/serve-uploaded-images/">image delivery URL</a> to serve a predefined variant.</p>
<h3 id="image-imageid-update-options"><code>.image(imageId).update(options)</code></h3>
<p>Updates the metadata or access controls for an image. All fields are optional; only the specified fields will be changed. Returns <a href="#imagemetadata"><code>ImageMetadata</code></a> with the updated values.</p>
<p>Accepts the following options as an <code>ImageUpdateOptions</code> object:</p>
<ul>
<li><code>requireSignedURLs</code> <span class="nb-type">boolean</span> — Whether signed URLs should be required to view the image. Cannot be set to <code>true</code> on an image that was uploaded with a <a href="/images/storage/upload-images/upload-custom-path/">custom ID</a>.</li>
<li><code>metadata</code> <span class="nb-type">Record&amp;lt;string, unknown&amp;gt;</span> — Replacement metadata for the image. This replaces the existing metadata rather than merging into it.</li>
<li><code>creator</code> <span class="nb-type">string</span> — A user-defined identifier for the image creator.</li>
</ul>
<h3 id="image-imageid-delete"><code>.image(imageId).delete()</code></h3>
<p>Deletes an image. Returns <code>true</code> if the image was deleted or <code>false</code> if no image with the given ID existed.</p>
<h3 id="image-imageid-signedurl-options"><code>.image(imageId).signedUrl(options)</code></h3>
<p>Generates a signed <a href="/images/optimization/hosted-images/serve-private-images/">image delivery URL</a> for an image that <a href="/images/optimization/hosted-images/serve-private-images/">requires signed URLs</a>. Returns a <code>string</code>.</p>
<p>Returning a signed URL lets a browser fetch a private image directly without proxying the bytes through your Worker. The URL is signed on the Cloudflare side, so your Worker never handles the account signing key.</p>
<p>Accepts the following options as an <code>ImageSignedUrlOptions</code> object:</p>
<ul>
<li><code>variant</code> <span class="nb-type">string</span> — The <a href="/images/optimization/hosted-images/create-variants/">variant</a> to serve.</li>
<li><code>expiresIn</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span> — How long the URL stays valid, in seconds. If omitted, then the URL does not expire.</li>
<li><code>keyName</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span> — The name of the <a href="/images/optimization/hosted-images/serve-private-images/">signing key</a> to use. Defaults to <code>default</code>.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="upload-an-image-from-a-request-body">Upload an image from a request body</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9345.md")
</div>
<h3 id="upload-a-base64-encoded-image">Upload a base64-encoded image</h3>
<p>Set <code>encoding: &quot;base64&quot;</code> and the binding will decode the body for you before uploading.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9346.md")
</div>
<h3 id="list-images-with-pagination">List images with pagination</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9347.md")
</div>
<h3 id="get-the-details-for-a-single-image">Get the details for a single image</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9348.md")
</div>
<h3 id="stream-the-original-bytes-for-an-image">Stream the original bytes for an image</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9349.md")
</div>
<h3 id="update-image-metadata">Update image metadata</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9350.md")
</div>
<h3 id="delete-an-image">Delete an image</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9351.md")
</div>
<h3 id="generate-a-signed-url-for-a-private-image">Generate a signed URL for a private image</h3>
<p>Redirect the browser to a short-lived signed URL so it can fetch a private image directly without streaming the bytes through your Worker.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9352.md")
</div>
<h3 id="create-a-direct-creator-upload-url">Create a Direct Creator Upload URL</h3>
<p>Create a one-time upload URL and return it to a client, which can then upload an image straight to Cloudflare without your Worker handling the bytes or an API token.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9353.md")
</div>
<h3 id="ingest-a-remote-image-into-images-storage">Ingest a remote image into Images storage</h3>
<p>This example fetches an image from a remote URL, uploads it into your Images account, and returns the first variant URL.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9354.md")
</div>
<h2 id="type-definitions">Type definitions</h2>
<h3 id="imagemetadata">ImageMetadata</h3>
<p>Returned by operations that retrieve, create, or update an image.</p>
<ul>
<li><code>id</code> <span class="nb-type">string</span>
<ul>
<li>The unique identifier for the image.</li>
</ul>
</li>
<li><code>filename</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The original filename supplied at upload time.</li>
</ul>
</li>
<li><code>uploaded</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The date and time the image was uploaded, as an ISO 8601 string.</li>
</ul>
</li>
<li><code>requireSignedURLs</code> <span class="nb-type">boolean</span>
<ul>
<li>Whether signed URLs are required to access this image. Refer to <a href="/images/optimization/hosted-images/serve-private-images/">Serve private images</a>.</li>
</ul>
</li>
<li><code>meta</code> <span class="nb-type">Record&amp;lt;string, unknown&amp;gt;</span> <span class="nb-metainfo">optional</span>
<ul>
<li>User-supplied metadata associated with the image.</li>
</ul>
</li>
<li><code>variants</code> <span class="nb-type">Array&amp;lt;string&amp;gt;</span>
<ul>
<li>Fully-formed URLs for each variant configured on your account. Refer to <a href="/images/optimization/hosted-images/create-variants/">Create variants</a>.</li>
</ul>
</li>
<li><code>draft</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Whether the image is in a draft state (no bytes uploaded yet). Drafts are typically only seen on accounts using <a href="/images/storage/upload-images/direct-creator-upload/">Direct Creator Uploads</a>.</li>
</ul>
</li>
<li><code>creator</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A user-defined identifier for the image creator.</li>
</ul>
</li>
</ul>
<h3 id="imagelist">ImageList</h3>
<p>Returned by <a href="#listoptions"><code>list()</code></a>.</p>
<ul>
<li><code>images</code> <span class="nb-type">Array&amp;lt;ImageMetadata&amp;gt;</span>
<ul>
<li>The images in this page of results.</li>
</ul>
</li>
<li><code>cursor</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A continuation token to pass to the next <code>list()</code> call. Only present when there are more results.</li>
</ul>
</li>
<li><code>listComplete</code> <span class="nb-type">boolean</span>
<ul>
<li><code>true</code> when there are no further pages, <code>false</code> otherwise.</li>
</ul>
</li>
</ul>
<h3 id="directuploadresult">DirectUploadResult</h3>
<p>Returned by <a href="#createdirectuploadoptions"><code>createDirectUpload()</code></a>.</p>
<ul>
<li><code>id</code> <span class="nb-type">string</span>
<ul>
<li>The ID that the uploaded image will have.</li>
</ul>
</li>
<li><code>uploadURL</code> <span class="nb-type">string</span>
<ul>
<li>The one-time URL that a client uploads the image bytes to.</li>
</ul>
</li>
</ul>
<h2 id="error-handling">Error handling</h2>
<p>Methods that fail throw an <code>ImagesError</code> — <code>.upload()</code>, <code>.list()</code>, <code>.createDirectUpload()</code>, <code>.update()</code>, and <code>.signedUrl()</code> — with the following properties:</p>
<ul>
<li><code>code</code> <span class="nb-type">number</span>
<ul>
<li>A numeric error code that identifies the failure mode.</li>
</ul>
</li>
<li><code>message</code> <span class="nb-type">string</span>
<ul>
<li>A human-readable description of the error.</li>
</ul>
</li>
</ul>
<p>Methods that fetch a single image — <a href="#imageimageiddetails"><code>.details()</code></a>, <a href="#imageimageidbytes"><code>.bytes()</code></a>, and <a href="#imageimageiddelete"><code>.delete()</code></a> — return <code>null</code> or <code>false</code> for &quot;not found&quot; rather than throwing.</p>
<p>You may want to wrap operations that can throw in a <code>try...catch</code> block.</p>
<h2 id="local-development">Local development</h2>
<p>When you run <code>wrangler dev</code>, operations for managing hosted images are served by a local mock that stores images in an embedded KV namespace. The mock supports every method documented on this page, so you can develop and test your Worker offline.</p>
<p>The mock is only suitable for local development. To exercise the real Images service from your local environment, run <code>wrangler dev --remote</code>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/images/optimization/binding/">Optimize with Workers</a> — Use the binding to optimize images from a Worker.</li>
<li><a href="/images/storage/upload-images/methods/">Upload via the REST API</a> — The equivalent HTTP API.</li>
<li><a href="/images/storage/manage-images/">Manage hosted images</a> — Dashboard and API workflows for managing stored images.</li>
</ul>
