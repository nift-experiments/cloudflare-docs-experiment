---
cp9:
  canonical: https://developers.cloudflare.com/stream/edit-videos/applying-watermarks/
  description: Create watermark profiles and apply them to Cloudflare Stream video uploads via the API.
  full_title: Apply watermarks · Cloudflare Stream docs
  head_html: <title>Apply watermarks · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Create watermark profiles and apply them to Cloudflare Stream video uploads via the API."><link rel="canonical" href="https://developers.cloudflare.com/stream/edit-videos/applying-watermarks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/edit-videos/applying-watermarks/index.md"><meta property="og:title" content="Apply watermarks · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create watermark profiles and apply them to Cloudflare Stream video uploads via the API."><meta property="og:url" content="https://developers.cloudflare.com/stream/edit-videos/applying-watermarks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/edit-videos/applying-watermarks/#page","headline":"Apply watermarks \u00b7 Cloudflare Stream docs","description":"Create watermark profiles and apply them to Cloudflare Stream video uploads via the API.","url":"https://developers.cloudflare.com/stream/edit-videos/applying-watermarks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/edit-videos/applying-watermarks/
  schema: 1
---
<p>You can add watermarks to videos uploaded using the Stream API.</p>
<p>To add watermarks to your videos, first create a watermark profile. A watermark profile describes the image you would like to be used as a watermark and the position of that image. Once you have a watermark profile, you can use it as an option when uploading videos.</p>
<h2 id="quick-start">Quick start</h2>
<p>Watermark profile has many customizable options. However, the default parameters generally work for most cases. Please see &quot;Profiles&quot; below for more details.</p>
<h3 id="step-1-create-a-profile">Step 1: Create a profile</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14479.md")
</div></div>
<h3 id="step-2-specify-the-profile-uid-at-upload">Step 2: Specify the profile UID at upload</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14488.md")
</div></div>
<h3 id="step-3-done">Step 3: Done</h3>
<p><img src="/assets/upstream/images/stream/cat.png" alt="Screenshot of a video with Cloudflare watermark at top right" /></p>
<h2 id="profiles">Profiles</h2>
<p>To create, list, delete, or get information about the profile, you will need your
<a href="https://www.cloudflare.com/a/account/my-account">Cloudflare API token</a>.</p>
<h3 id="optional-parameters">Optional parameters</h3>
<ul>
<li>
<p><code>name</code> string default: <em>empty string</em></p>
<ul>
<li>A short description for the profile. For example, &quot;marketing videos.&quot;</li>
</ul>
</li>
<li>
<p><code>opacity</code> float default: 1.0</p>
<ul>
<li>Translucency of the watermark. 0.0 means completely transparent, and 1.0 means completely opaque. Note that if the watermark is already semi-transparent, setting this to 1.0 will not make it completely opaque.</li>
</ul>
</li>
<li>
<p><code>padding</code> float default: 0.05</p>
<ul>
<li>
<p>Blank space between the adjacent edges (determined by position) of the video and the watermark. 0.0 means no padding, and 1.0 means padded full video width or length.</p>
</li>
<li>
<p>Stream will make sure that the watermark will be at about the same position across videos with different dimensions.</p>
</li>
</ul>
</li>
<li>
<p><code>scale</code> float default: 0.15</p>
<ul>
<li>
<p>The size of the watermark relative to the overall size of the video. This parameter will adapt to horizontal and vertical videos automatically. 0.0 means no scaling (use the size of the watermark as-is), and 1.0 fills the entire video.</p>
</li>
<li>
<p>The algorithm will make sure that the watermark will look about the same size across videos with different dimensions.</p>
</li>
</ul>
</li>
<li>
<p><code>position</code> string (enum) default: &quot;upperRight&quot;</p>
<ul>
<li>Location of the watermark. Valid positions are: <code>upperRight</code>, <code>upperLeft</code>, <code>lowerLeft</code>, <code>lowerRight</code>, and <code>center</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14470.md")
</aside>
<h2 id="creating-a-watermark-profile">Creating a Watermark profile</h2>
<h3 id="use-case-1-upload-a-local-image-file-directly">Use Case 1: Upload a local image file directly</h3>
<p>To upload the image directly, please send a POST request using <code>multipart/form-data</code> as the content-type and specify the file under the <code>file</code> key. All other fields are optional.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14497.md")
</div></div>
<h3 id="use-case-2-pass-a-url-to-an-image">Use Case 2: Pass a URL to an image</h3>
<p>To specify a URL for upload, please send a POST request using <code>application/json</code> as the content-type and specify the file location using the <code>url</code> key. All other fields are optional.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14506.md")
</div></div>
<h4 id="example-response-to-creating-a-watermark-profile">Example response to creating a watermark profile</h4>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;uid&quot;: &quot;d6373709b7681caa6c48ef2d8c73690d&quot;,&#10;    &quot;size&quot;: 11248,&#10;    &quot;height&quot;: 240,&#10;    &quot;width&quot;: 720,&#10;    &quot;created&quot;: &quot;2020-07-29T00:16:55.719265Z&quot;,&#10;    &quot;downloadedFrom&quot;: null,&#10;    &quot;name&quot;: &quot;marketing videos&quot;,&#10;    &quot;opacity&quot;: 1.0,&#10;    &quot;padding&quot;: 0.05,&#10;    &quot;scale&quot;: 0.15,&#10;    &quot;position&quot;: &quot;upperRight&quot;&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<p><code>downloadedFrom</code> will be populated if the profile was created via downloading from URL.</p>
<h2 id="using-a-watermark-profile-on-a-video">Using a watermark profile on a video</h2>
<p>Once you created a watermark profile, you can now use the profile at upload time for watermarking videos.</p>
<h3 id="basic-uploads">Basic uploads</h3>
<p>Unfortunately, Stream does not currently support specifying watermark profile at upload time for Basic Uploads.</p>
<h3 id="upload-video-with-a-link">Upload video with a link</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14515.md")
</div></div>
<h4 id="example-response-to-upload-video-with-a-link">Example response to upload video with a link</h4>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;uid&quot;: &quot;8d3a5b80e7437047a0fb2761e0f7a645&quot;,&#10;    &quot;thumbnail&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.jpg&quot;,&#10;&#10;    &quot;playback&quot;: {&#10;      &quot;hls&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.m3u8&quot;,&#10;      &quot;dash&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.mpd&quot;&#10;    },&#10;    &quot;watermark&quot;: {&#10;      &quot;uid&quot;: &quot;d6373709b7681caa6c48ef2d8c73690d&quot;,&#10;      &quot;size&quot;: 11248,&#10;      &quot;height&quot;: 240,&#10;      &quot;width&quot;: 720,&#10;      &quot;created&quot;: &quot;2020-07-29T00:16:55.719265Z&quot;,&#10;      &quot;downloadedFrom&quot;: null,&#10;      &quot;name&quot;: &quot;marketing videos&quot;,&#10;      &quot;opacity&quot;: 1.0,&#10;      &quot;padding&quot;: 0.05,&#10;      &quot;scale&quot;: 0.15,&#10;      &quot;position&quot;: &quot;upperRight&quot;&#10;    }&#10;&#10;}&#10;</code></pre>
<h3 id="upload-video-with-tus">Upload video with tus</h3>
<pre tabindex="0"><code class="language-bash">tus-upload --chunk-size 5242880 \&#10;&#45;-header Authentication &#x27;Bearer &lt;API_TOKEN&gt;&#x27; \&#10;&#45;-metadata watermark &lt;WATERMARK_UID&gt; \&#10;&lt;PATH_TO_VIDEO&gt; https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream&#10;</code></pre>
<h3 id="direct-creator-uploads">Direct creator uploads</h3>
<p>The video uploaded with the generated unique one-time URL will be watermarked with the profile specified.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14524.md")
</div></div>
<h4 id="example-response-to-direct-user-uploads">Example response to direct user uploads</h4>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;uploadURL&quot;: &quot;https://upload.videodelivery.net/c32d98dd671e4046a33183cd5b93682b&quot;,&#10;    &quot;uid&quot;: &quot;c32d98dd671e4046a33183cd5b93682b&quot;,&#10;    &quot;watermark&quot;: {&#10;      &quot;uid&quot;: &quot;d6373709b7681caa6c48ef2d8c73690d&quot;,&#10;      &quot;size&quot;: 11248,&#10;      &quot;height&quot;: 240,&#10;      &quot;width&quot;: 720,&#10;      &quot;created&quot;: &quot;2020-07-29T00:16:55.719265Z&quot;,&#10;      &quot;downloadedFrom&quot;: null,&#10;      &quot;name&quot;: &quot;marketing videos&quot;,&#10;      &quot;opacity&quot;: 1.0,&#10;      &quot;padding&quot;: 0.05,&#10;      &quot;scale&quot;: 0.15,&#10;      &quot;position&quot;: &quot;upperRight&quot;&#10;    }&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<p><code>watermark</code> will be <code>null</code> if no watermark was specified.</p>
<h2 id="get-a-watermark-profile">Get a watermark profile</h2>
<p>To view a watermark profile that you created:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14533.md")
</div></div>
<h3 id="example-response-to-get-a-watermark-profile">Example response to get a watermark profile</h3>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;uid&quot;: &quot;d6373709b7681caa6c48ef2d8c73690d&quot;,&#10;    &quot;size&quot;: 11248,&#10;    &quot;height&quot;: 240,&#10;    &quot;width&quot;: 720,&#10;    &quot;created&quot;: &quot;2020-07-29T00:16:55.719265Z&quot;,&#10;    &quot;downloadedFrom&quot;: null,&#10;    &quot;name&quot;: &quot;marketing videos&quot;,&#10;    &quot;opacity&quot;: 1.0,&#10;    &quot;padding&quot;: 0.05,&#10;    &quot;scale&quot;: 0.15,&#10;    &quot;position&quot;: &quot;center&quot;&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="list-watermark-profiles">List watermark profiles</h2>
<p>To list watermark profiles that you created:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14542.md")
</div></div>
<h3 id="example-response-to-list-watermark-profiles">Example response to list watermark profiles</h3>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;uid&quot;: &quot;9de16afa676d64faaa7c6c4d5047e637&quot;,&#10;      &quot;size&quot;: 207710,&#10;      &quot;height&quot;: 626,&#10;      &quot;width&quot;: 1108,&#10;      &quot;created&quot;: &quot;2020-07-29T00:23:35.918472Z&quot;,&#10;      &quot;downloadedFrom&quot;: null,&#10;      &quot;name&quot;: &quot;marketing videos&quot;,&#10;      &quot;opacity&quot;: 1.0,&#10;      &quot;padding&quot;: 0.05,&#10;      &quot;scale&quot;: 0.15,&#10;      &quot;position&quot;: &quot;upperLeft&quot;&#10;    },&#10;    {&#10;      &quot;uid&quot;: &quot;9c50cff5ab16c4aec0bcb03c44e28119&quot;,&#10;      &quot;size&quot;: 207710,&#10;      &quot;height&quot;: 626,&#10;      &quot;width&quot;: 1108,&#10;      &quot;created&quot;: &quot;2020-07-29T00:16:46.735377Z&quot;,&#10;      &quot;downloadedFrom&quot;: &quot;https://company.com/logo.png&quot;,&#10;      &quot;name&quot;: &quot;internal training videos&quot;,&#10;      &quot;opacity&quot;: 1.0,&#10;      &quot;padding&quot;: 0.05,&#10;      &quot;scale&quot;: 0.15,&#10;      &quot;position&quot;: &quot;center&quot;&#10;    }&#10;  ],&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="delete-a-watermark-profile">Delete a  watermark profile</h2>
<p>To delete a watermark profile that you created:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14551.md")
</div></div>
<p>If the operation was successful, it will return a success response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: &quot;&quot;,&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Once the watermark profile is created, you cannot change its parameters. If you need to edit your watermark profile, please delete it and create a new one.</li>
<li>Once the watermark is applied to a video, you cannot change the watermark without re-uploading the video to apply a different profile.</li>
<li>Once the watermark is applied to a video, deleting the watermark profile will not also remove the watermark from the video.</li>
<li>The maximum file size is 2MiB (2097152 bytes), and only PNG files are supported.</li>
</ul>
