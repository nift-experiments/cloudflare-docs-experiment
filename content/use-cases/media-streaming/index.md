<p>Deliver video, images, and rich media at scale with encoding, optimization, and global distribution. Cloudflare Stream handles video upload, encoding, and adaptive bitrate delivery. Images transforms and optimizes images on-the-fly. R2 stores media files with zero egress fees. Cache serves content from 300+ edge locations. Hotlink Protection and signed URLs secure media from unauthorized access.</p>
<ul class="directory-listing"><li><a href="/use-cases/media-streaming/video-delivery/">Upload, encode, and deliver videos</a></li><li><a href="/use-cases/media-streaming/image-optimization/">Optimize and transform images for the web</a></li><li><a href="/use-cases/media-streaming/store-media/">Store media at scale</a></li><li><a href="/use-cases/media-streaming/cache-delivery/">Cache and accelerate media delivery</a></li><li><a href="/use-cases/media-streaming/secure-content/">Secure your content</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="video-platform">Video platform</h3>
<p>Build a complete video hosting and delivery solution:</p>
<ul>
<li><strong>Stream</strong> handles upload, encoding, and adaptive bitrate delivery</li>
<li><strong>Stream Live</strong> enables live streaming with automatic recording</li>
<li><strong>Signed URLs</strong> protect content with token authentication</li>
</ul>
<h3 id="image-optimization-pipeline">Image optimization pipeline</h3>
<p>Serve optimized images without pre-generating variants:</p>
<ol>
<li><strong>R2</strong> stores original high-resolution images</li>
<li><strong>Images</strong> transforms images on-the-fly based on URL parameters</li>
<li><strong>Workers</strong> applies custom logic for format selection and caching</li>
</ol>
<h3 id="user-generated-content">User-generated content</h3>
<p>Handle media uploads from users at scale:</p>
<ol>
<li><strong>R2</strong> receives uploads directly via presigned URLs</li>
<li><strong>Workers</strong> validates and processes uploaded content</li>
<li><strong>Stream</strong> or <strong>Images</strong> optimizes media for delivery</li>
</ol>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="create-a-new-application">Create a new application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>. Stream and R2 are account-level offerings. You do not need a domain added to Cloudflare to upload, encode, or store media.</li>
<li>For Image Transformations: enable the feature per domain from the <a href="https://dash.cloudflare.com/?to=/:account/images/transformations">Transformations page</a> in the dashboard. Refer to <a href="/images/optimization/transformations/overview/">Image Transformations</a>.</li>
</ul>
<h3 id="use-an-existing-application">Use an existing application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> with DNS records proxied through Cloudflare. This is required for CDN caching, image optimization (Polish), and cache rules.</li>
<li>For Image Transformations on an existing domain: enable the feature from the <a href="https://dash.cloudflare.com/?to=/:account/images/transformations">Transformations page</a> in the dashboard. Refer to <a href="/images/optimization/transformations/overview/">Image Transformations</a>.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15232.md")
</div>
