<p>A <a href="/workers/runtime-apis/bindings/">binding</a> connects your <a href="/workers/">Worker</a> to external resources on the Developer Platform, like <a href="/stream/">Stream</a>, <a href="/r2/buckets/">R2 buckets</a>, or <a href="/kv/concepts/kv-namespaces/">KV namespaces</a>.</p>
<p>For example, when you use Stream within Workers, you can:</p>
<ul>
<li>Upload videos from a URL and manage their lifecycle</li>
<li>Create direct uploads for client-side uploads without having to expose API keys</li>
<li>List and search videos</li>
<li>Manage captions and downloads for videos</li>
<li>Create and manage watermark profiles</li>
</ul>
<h2 id="setup">Setup</h2>
<p>The Stream binding is enabled on a per-Worker basis.</p>
<p>To bind Stream to your Worker, add the following to the end of your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/14446.md")
</div>
<p>For more detailed information on configuring your Worker, refer to the <a href="/workers/wrangler/configuration/">Wrangler Configuration documentation</a>.</p>
<h2 id="methods">Methods</h2>
<h3 id="binding-level-methods">Binding-level methods</h3>
<p>The following methods are available on the <code>env.STREAM</code> binding directly.</p>
<h4 id="upload-url-params"><code>upload(url, params?)</code></h4>
<p>Upload a video from a URL. Returns <code>Promise&lt;</code><a href="#streamvideo"><code>StreamVideo</code></a><code>&gt;</code>.</p>
<ul>
<li><code>url</code> (required): The URL of the video to upload.</li>
<li><code>params</code> (optional): A <a href="#streamurluploadparams"><code>StreamUrlUploadParams</code></a> object with the following properties:
<ul>
<li><code>allowedOrigins</code>: Array of allowed origins for the video.</li>
<li><code>creator</code>: Creator identifier.</li>
<li><code>meta</code>: Arbitrary metadata object.</li>
<li><code>requireSignedURLs</code>: Whether signed URLs are required.</li>
<li><code>scheduledDeletion</code>: ISO 8601 timestamp for scheduled deletion.</li>
<li><code>thumbnailTimestampPct</code>: Thumbnail timestamp as a percentage (0.0 to 1.0).</li>
<li><code>watermarkId</code>: ID of a watermark profile to apply.</li>
</ul>
</li>
</ul>
<p>Throws: <code>BadRequestError</code>, <code>QuotaReachedError</code>, <code>MaxFileSizeError</code>, <code>RateLimitedError</code>, <code>AlreadyUploadedError</code>, <code>InternalError</code>.</p>
<h4 id="createdirectupload-params"><code>createDirectUpload(params)</code></h4>
<p>Create a basic direct upload URL for client-side uploads without an API key. Returns <code>Promise&lt;</code><a href="#streamdirectupload"><code>StreamDirectUpload</code></a><code>&gt;</code> with <code>uploadURL</code> and <code>id</code>.</p>
<p><em>This method does not currently support files over 200MB.</em> For larger direct uploads, refer to the <a href="http://localhost:1111/stream/uploading-videos/direct-creator-uploads/#direct-creator-uploads-with-tus-protocol">API request for provisioning a TUS endpoint</a>._</p>
<ul>
<li><code>params</code> (required): A <a href="#streamdirectuploadcreateparams"><code>StreamDirectUploadCreateParams</code></a> object with the following properties:
<ul>
<li><code>maxDurationSeconds</code> (required): Maximum duration of the uploaded video in seconds.</li>
<li><code>expiry</code> (optional): ISO 8601 timestamp when the upload URL expires.</li>
<li><code>creator</code> (optional): Creator identifier.</li>
<li><code>meta</code> (optional): Arbitrary metadata object.</li>
<li><code>allowedOrigins</code> (optional): Array of allowed origins for the video.</li>
<li><code>requireSignedURLs</code> (optional): Whether signed URLs are required.</li>
<li><code>thumbnailTimestampPct</code> (optional): Thumbnail timestamp as a percentage (0.0 to 1.0).</li>
<li><code>scheduledDeletion</code> (optional): ISO 8601 timestamp for scheduled deletion.</li>
<li><code>watermark</code> (optional): ID of a watermark profile to apply.</li>
</ul>
</li>
</ul>
<h4 id="videos-list-params"><code>videos.list(params?)</code></h4>
<p>List all videos in the account. Returns <code>Promise&lt;</code><a href="#streamvideo"><code>StreamVideo</code></a><code>[]&gt;</code>.</p>
<ul>
<li><code>params</code> (optional): A <a href="#streamvideoslistparams"><code>StreamVideosListParams</code></a> object with the following properties:
<ul>
<li><code>limit</code>: Maximum number of videos to return.</li>
<li><code>before</code>: Return videos created before this ISO 8601 timestamp.</li>
<li><code>beforeComp</code>: Comparison operator for <code>before</code> — <code>eq</code>, <code>gt</code>, <code>gte</code>, <code>lt</code>, or <code>lte</code>.</li>
<li><code>after</code>: Return videos created after this ISO 8601 timestamp.</li>
<li><code>afterComp</code>: Comparison operator for <code>after</code> — <code>eq</code>, <code>gt</code>, <code>gte</code>, <code>lt</code>, or <code>lte</code>.</li>
</ul>
</li>
</ul>
<h3 id="video-scoped-methods">Video-scoped methods</h3>
<p>Calling <code>env.STREAM.video(id)</code> returns a handle scoped to a single video, with the following methods.</p>
<h4 id="details"><code>details()</code></h4>
<p>Get full video details. Returns <code>Promise&lt;</code><a href="#streamvideo"><code>StreamVideo</code></a><code>&gt;</code>.</p>
<h4 id="update-params"><code>update(params)</code></h4>
<p>Update video metadata. Returns <code>Promise&lt;</code><a href="#streamvideo"><code>StreamVideo</code></a><code>&gt;</code>.</p>
<ul>
<li><code>params</code> (required): A <a href="#streamupdatevideoparams"><code>StreamUpdateVideoParams</code></a> object with the following properties:
<ul>
<li><code>allowedOrigins</code>: Array of allowed origins for the video.</li>
<li><code>creator</code>: Creator identifier.</li>
<li><code>maxDurationSeconds</code>: Maximum duration in seconds.</li>
<li><code>meta</code>: Arbitrary metadata object.</li>
<li><code>requireSignedURLs</code>: Whether signed URLs are required.</li>
<li><code>scheduledDeletion</code>: ISO 8601 timestamp for scheduled deletion.</li>
<li><code>thumbnailTimestampPct</code>: Thumbnail timestamp as a percentage (0.0 to 1.0).</li>
</ul>
</li>
</ul>
<h4 id="delete"><code>delete()</code></h4>
<p>Delete a video and its copies. Returns <code>Promise&lt;void&gt;</code>.</p>
<h4 id="generatetoken"><code>generateToken()</code></h4>
<p>Create a signed URL token for a video. Returns <code>Promise&lt;string&gt;</code>.</p>
<h4 id="downloads"><code>downloads</code></h4>
<p>Namespace for download operations on a video.</p>
<ul>
<li><code>generate(downloadType?)</code>: Generate a download. <code>downloadType</code> is a <a href="#streamdownloadtype"><code>StreamDownloadType</code></a> of <code>default</code> or <code>audio</code>. Defaults to <code>default</code>. Returns <code>Promise&lt;</code><a href="#streamdownloadgetresponse"><code>StreamDownloadGetResponse</code></a><code>&gt;</code>.</li>
<li><code>get()</code>: List existing downloads. Returns <code>Promise&lt;</code><a href="#streamdownloadgetresponse"><code>StreamDownloadGetResponse</code></a><code>&gt;</code>.</li>
<li><code>delete(downloadType?)</code>: Delete downloads. <code>downloadType</code> is <code>default</code> or <code>audio</code>.</li>
</ul>
<h4 id="captions"><code>captions</code></h4>
<p>Namespace for caption operations on a video.</p>
<ul>
<li><code>upload(language, input)</code>: Upload a caption file for a BCP 47 language tag. <code>input</code> is a <code>ReadableStream</code>. Returns <code>Promise&lt;</code><a href="#streamcaption"><code>StreamCaption</code></a><code>&gt;</code>.</li>
<li><code>generate(language)</code>: Generate captions via AI for a BCP 47 language tag. Returns <code>Promise&lt;</code><a href="#streamcaption"><code>StreamCaption</code></a><code>&gt;</code>.</li>
<li><code>list(language?)</code>: List captions, optionally filtered by language. Returns <code>Promise&lt;</code><a href="#streamcaption"><code>StreamCaption</code></a><code>[]&gt;</code>.</li>
<li><code>delete(language)</code>: Delete captions for a language. Returns <code>Promise&lt;void&gt;</code>.</li>
</ul>
<h3 id="watermark-methods">Watermark methods</h3>
<p>The following methods are available on the <code>env.STREAM.watermarks</code> namespace.</p>
<h4 id="watermarks-generate-input-params"><code>watermarks.generate(input, params)</code></h4>
<p>Create a watermark profile. Accepts either a <code>ReadableStream</code> or a URL string. Returns <code>Promise&lt;</code><a href="#streamwatermark"><code>StreamWatermark</code></a><code>&gt;</code>.</p>
<ul>
<li><code>input</code> (required): A <code>ReadableStream</code> or URL string of the watermark image.</li>
<li><code>params</code> (optional): A <a href="#streamwatermarkcreateparams"><code>StreamWatermarkCreateParams</code></a> object with the following properties:
<ul>
<li><code>name</code>: Name of the watermark profile.</li>
<li><code>opacity</code>: Opacity of the watermark (0.0 to 1.0).</li>
<li><code>padding</code>: Padding around the watermark as a proportion of the video resolution.</li>
<li><code>scale</code>: Scale of the watermark as a proportion of the video resolution.</li>
<li><code>position</code>: Position of the watermark — <code>upperRight</code>, <code>upperLeft</code>, <code>lowerLeft</code>, <code>lowerRight</code>, or <code>center</code>.</li>
</ul>
</li>
</ul>
<h4 id="watermarks-list"><code>watermarks.list()</code></h4>
<p>List all watermark profiles. Returns <code>Promise&lt;</code><a href="#streamwatermark"><code>StreamWatermark</code></a><code>[]&gt;</code>.</p>
<h4 id="watermarks-get-watermarkid"><code>watermarks.get(watermarkId)</code></h4>
<p>Get a single watermark profile. Returns <code>Promise&lt;</code><a href="#streamwatermark"><code>StreamWatermark</code></a><code>&gt;</code>.</p>
<ul>
<li><code>watermarkId</code> (required): The ID of the watermark profile.</li>
</ul>
<h4 id="watermarks-delete-watermarkid"><code>watermarks.delete(watermarkId)</code></h4>
<p>Delete a watermark profile. Returns <code>Promise&lt;void&gt;</code>.</p>
<ul>
<li><code>watermarkId</code> (required): The ID of the watermark profile.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="upload-a-video-from-a-url">Upload a video from a URL</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14447.md")
</div>
<h3 id="create-a-direct-upload">Create a direct upload</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14448.md")
</div>
<h3 id="list-videos">List videos</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14449.md")
</div>
<h3 id="get-video-details">Get video details</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14450.md")
</div>
<h3 id="update-video-metadata">Update video metadata</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14451.md")
</div>
<h3 id="delete-a-video">Delete a video</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14452.md")
</div>
<h3 id="generate-a-signed-url-token">Generate a signed URL token</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14453.md")
</div>
<h3 id="upload-captions">Upload captions</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14454.md")
</div>
<h3 id="generate-ai-captions">Generate AI captions</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14455.md")
</div>
<h3 id="list-and-delete-captions">List and delete captions</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14456.md")
</div>
<h3 id="generate-and-list-downloads">Generate and list downloads</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14457.md")
</div>
<h3 id="create-a-watermark-profile">Create a watermark profile</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14458.md")
</div>
<h3 id="list-and-delete-watermark-profiles">List and delete watermark profiles</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14459.md")
</div>
<h2 id="type-definitions">Type definitions</h2>
<h3 id="streamvideo">StreamVideo</h3>
<p><code>StreamVideo</code> is returned by operations that retrieve or create a video. It contains the full metadata for a video.</p>
<ul>
<li>
<p><code>id</code> <span class="nb-type">string</span></p>
<ul>
<li>The unique identifier for the video.</li>
</ul>
</li>
<li>
<p><code>creator</code> <span class="nb-type">string | null</span></p>
<ul>
<li>A user-defined identifier for the media creator.</li>
</ul>
</li>
<li>
<p><code>thumbnail</code> <span class="nb-type">string</span></p>
<ul>
<li>The thumbnail URL for the video.</li>
</ul>
</li>
<li>
<p><code>thumbnailTimestampPct</code> <span class="nb-type">number</span></p>
<ul>
<li>The thumbnail timestamp percentage.</li>
</ul>
</li>
<li>
<p><code>readyToStream</code> <span class="nb-type">boolean</span></p>
<ul>
<li>Indicates whether the video is ready to stream.</li>
</ul>
</li>
<li>
<p><code>readyToStreamAt</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The date and time the video became ready to stream.</li>
</ul>
</li>
<li>
<p><code>status</code> <span class="nb-type">StreamVideoStatus</span></p>
<ul>
<li>Processing status information. Refer to <a href="#streamvideostatus">StreamVideoStatus</a>.</li>
</ul>
</li>
<li>
<p><code>meta</code> <span class="nb-type">Record&amp;lt;string, string&amp;gt;</span></p>
<ul>
<li>A user modifiable key-value store.</li>
</ul>
</li>
<li>
<p><code>created</code> <span class="nb-type">string</span></p>
<ul>
<li>The date and time the video was created.</li>
</ul>
</li>
<li>
<p><code>modified</code> <span class="nb-type">string</span></p>
<ul>
<li>The date and time the video was last modified.</li>
</ul>
</li>
<li>
<p><code>scheduledDeletion</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The date and time at which the video will be deleted.</li>
</ul>
</li>
<li>
<p><code>size</code> <span class="nb-type">number</span></p>
<ul>
<li>The size of the video in bytes.</li>
</ul>
</li>
<li>
<p><code>preview</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The preview URL for the video.</li>
</ul>
</li>
<li>
<p><code>allowedOrigins</code> <span class="nb-type">Array&amp;lt;string&amp;gt;</span></p>
<ul>
<li>Origins allowed to display the video.</li>
</ul>
</li>
<li>
<p><code>requireSignedURLs</code> <span class="nb-type">boolean | null</span></p>
<ul>
<li>Indicates whether signed URLs are required.</li>
</ul>
</li>
<li>
<p><code>uploaded</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The date and time the video was uploaded.</li>
</ul>
</li>
<li>
<p><code>uploadExpiry</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The date and time when the upload URL expires.</li>
</ul>
</li>
<li>
<p><code>maxSizeBytes</code> <span class="nb-type">number | null</span></p>
<ul>
<li>The maximum size in bytes for direct uploads.</li>
</ul>
</li>
<li>
<p><code>maxDurationSeconds</code> <span class="nb-type">number | null</span></p>
<ul>
<li>The maximum duration in seconds for direct uploads.</li>
</ul>
</li>
<li>
<p><code>duration</code> <span class="nb-type">number</span></p>
<ul>
<li>The video duration in seconds. <code>-1</code> indicates unknown.</li>
</ul>
</li>
<li>
<p><code>input</code> <span class="nb-type">StreamVideoInput</span></p>
<ul>
<li>Input metadata for the original upload. Refer to <a href="#streamvideoinput">StreamVideoInput</a>.</li>
</ul>
</li>
<li>
<p><code>hlsPlaybackUrl</code> <span class="nb-type">string</span></p>
<ul>
<li>The HLS playback URL for the video.</li>
</ul>
</li>
<li>
<p><code>dashPlaybackUrl</code> <span class="nb-type">string</span></p>
<ul>
<li>The DASH playback URL for the video.</li>
</ul>
</li>
<li>
<p><code>watermark</code> <span class="nb-type">StreamWatermark | null</span></p>
<ul>
<li>The watermark applied to the video, if any. Refer to <a href="#streamwatermark">StreamWatermark</a>.</li>
</ul>
</li>
<li>
<p><code>liveInputId</code> <span class="nb-type">string | null</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The live input ID associated with the video, if any.</li>
</ul>
</li>
<li>
<p><code>clippedFromId</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The source video ID if this is a clip.</li>
</ul>
</li>
<li>
<p><code>publicDetails</code> <span class="nb-type">StreamPublicDetails | null</span></p>
<ul>
<li>Public details associated with the video. Refer to <a href="#streampublicdetails">StreamPublicDetails</a>.</li>
</ul>
</li>
</ul>
<h3 id="streamvideostatus">StreamVideoStatus</h3>
<p>Processing status information for a video.</p>
<ul>
<li>
<p><code>state</code> <span class="nb-type">string</span></p>
<ul>
<li>The current processing state.</li>
</ul>
</li>
<li>
<p><code>step</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The current processing step.</li>
</ul>
</li>
<li>
<p><code>pctComplete</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The percent complete as a string.</li>
</ul>
</li>
<li>
<p><code>errorReasonCode</code> <span class="nb-type">string</span></p>
<ul>
<li>An error reason code, if applicable.</li>
</ul>
</li>
<li>
<p><code>errorReasonText</code> <span class="nb-type">string</span></p>
<ul>
<li>An error reason text, if applicable.</li>
</ul>
</li>
</ul>
<h3 id="streamvideoinput">StreamVideoInput</h3>
<p>Input metadata for the original upload.</p>
<ul>
<li>
<p><code>width</code> <span class="nb-type">number</span></p>
<ul>
<li>The input width in pixels.</li>
</ul>
</li>
<li>
<p><code>height</code> <span class="nb-type">number</span></p>
<ul>
<li>The input height in pixels.</li>
</ul>
</li>
</ul>
<h3 id="streampublicdetails">StreamPublicDetails</h3>
<p>Public details associated with a video.</p>
<ul>
<li>
<p><code>title</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The public title for the video.</li>
</ul>
</li>
<li>
<p><code>share_link</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The public share link.</li>
</ul>
</li>
<li>
<p><code>channel_link</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The public channel link.</li>
</ul>
</li>
<li>
<p><code>logo</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The public logo URL.</li>
</ul>
</li>
</ul>
<h3 id="streamdirectupload">StreamDirectUpload</h3>
<p>Returned by <code>createDirectUpload()</code>. Contains the upload URL and video identifier for a direct upload.</p>
<ul>
<li>
<p><code>uploadURL</code> <span class="nb-type">string</span></p>
<ul>
<li>The URL an unauthenticated upload can use for a single multipart request.</li>
</ul>
</li>
<li>
<p><code>id</code> <span class="nb-type">string</span></p>
<ul>
<li>A Cloudflare-generated unique identifier for a media item.</li>
</ul>
</li>
<li>
<p><code>watermark</code> <span class="nb-type">StreamWatermark | null</span></p>
<ul>
<li>The watermark profile applied to the upload. Refer to <a href="#streamwatermark">StreamWatermark</a>.</li>
</ul>
</li>
<li>
<p><code>scheduledDeletion</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The scheduled deletion time, if any.</li>
</ul>
</li>
</ul>
<h3 id="streamcaption">StreamCaption</h3>
<p>Represents a caption or subtitle track for a video.</p>
<ul>
<li>
<p><code>generated</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Whether the caption was generated via AI.</li>
</ul>
</li>
<li>
<p><code>label</code> <span class="nb-type">string</span></p>
<ul>
<li>The language label displayed in the native language to users.</li>
</ul>
</li>
<li>
<p><code>language</code> <span class="nb-type">string</span></p>
<ul>
<li>The language tag in BCP 47 format.</li>
</ul>
</li>
<li>
<p><code>status</code> <span class="nb-type">ready' | 'inprogress' | 'error</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The status of a generated caption.</li>
</ul>
</li>
</ul>
<h3 id="streamdownloadgetresponse">StreamDownloadGetResponse</h3>
<p>An object with download type keys. Each key is optional and only present if that download type has been created.</p>
<ul>
<li>
<p><code>default</code> <span class="nb-type">StreamDownload</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The default video download. Only present if this download type has been created. Refer to <a href="#streamdownload">StreamDownload</a>.</li>
</ul>
</li>
<li>
<p><code>audio</code> <span class="nb-type">StreamDownload</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The audio-only download. Only present if this download type has been created. Refer to <a href="#streamdownload">StreamDownload</a>.</li>
</ul>
</li>
</ul>
<h3 id="streamdownload">StreamDownload</h3>
<p>Represents a generated download for a video.</p>
<ul>
<li>
<p><code>percentComplete</code> <span class="nb-type">number</span></p>
<ul>
<li>Indicates the progress as a percentage between 0 and 100.</li>
</ul>
</li>
<li>
<p><code>status</code> <span class="nb-type">StreamDownloadStatus</span></p>
<ul>
<li>The status of a generated download.</li>
</ul>
</li>
<li>
<p><code>url</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The URL to access the generated download.</li>
</ul>
</li>
</ul>
<h3 id="streamwatermark">StreamWatermark</h3>
<p>Represents a watermark profile.</p>
<ul>
<li>
<p><code>id</code> <span class="nb-type">string</span></p>
<ul>
<li>The unique identifier for a watermark profile.</li>
</ul>
</li>
<li>
<p><code>name</code> <span class="nb-type">string</span></p>
<ul>
<li>A short description of the watermark profile.</li>
</ul>
</li>
<li>
<p><code>opacity</code> <span class="nb-type">number</span></p>
<ul>
<li>The translucency of the image. A value of <code>0.0</code> makes the image completely transparent, and <code>1.0</code> makes the image completely opaque. Note that if the image is already semi-transparent, setting this to <code>1.0</code> will not make the image completely opaque.</li>
</ul>
</li>
<li>
<p><code>padding</code> <span class="nb-type">number</span></p>
<ul>
<li>The whitespace between the adjacent edges (determined by position) of the video and the image. <code>0.0</code> indicates no padding, and <code>1.0</code> indicates a fully padded video width or length.</li>
</ul>
</li>
<li>
<p><code>scale</code> <span class="nb-type">number</span></p>
<ul>
<li>The size of the image relative to the overall size of the video. <code>0.0</code> indicates no scaling, and <code>1.0</code> fills the entire video.</li>
</ul>
</li>
<li>
<p><code>position</code> <span class="nb-type">StreamWatermarkPosition</span></p>
<ul>
<li>The location of the image. Refer to <a href="#streamwatermarkposition">StreamWatermarkPosition</a>.</li>
</ul>
</li>
<li>
<p><code>size</code> <span class="nb-type">number</span></p>
<ul>
<li>The size of the image in bytes.</li>
</ul>
</li>
<li>
<p><code>height</code> <span class="nb-type">number</span></p>
<ul>
<li>The height of the image in pixels.</li>
</ul>
</li>
<li>
<p><code>width</code> <span class="nb-type">number</span></p>
<ul>
<li>The width of the image in pixels.</li>
</ul>
</li>
<li>
<p><code>created</code> <span class="nb-type">string</span></p>
<ul>
<li>The date and time a watermark profile was created.</li>
</ul>
</li>
<li>
<p><code>downloadedFrom</code> <span class="nb-type">string | null</span></p>
<ul>
<li>The source URL for a downloaded image. If the watermark profile was created via direct upload, this field is <code>null</code>.</li>
</ul>
</li>
</ul>
<h3 id="streamwatermarkposition">StreamWatermarkPosition</h3>
<p>The position of a watermark on a video.</p>
<p><span class="nb-type">upperRight' | 'upperLeft' | 'lowerLeft' | 'lowerRight' | 'center</span></p>
<ul>
<li><code>upperRight</code> — Top-right corner of the video.</li>
<li><code>upperLeft</code> — Top-left corner of the video.</li>
<li><code>lowerLeft</code> — Bottom-left corner of the video.</li>
<li><code>lowerRight</code> — Bottom-right corner of the video.</li>
<li><code>center</code> — Center of the video. Note that <code>center</code> ignores the <code>padding</code> parameter.</li>
</ul>
<h3 id="streamdownloadstatus">StreamDownloadStatus</h3>
<p>The status of a generated download.</p>
<p><span class="nb-type">ready' | 'inprogress' | 'error</span></p>
<ul>
<li><code>ready</code> — The download is ready.</li>
<li><code>inprogress</code> — The download is being generated.</li>
<li><code>error</code> — An error occurred during generation.</li>
</ul>
<h3 id="streamdownloadtype">StreamDownloadType</h3>
<p>The type of download to generate.</p>
<p><span class="nb-type">default' | 'audio</span></p>
<ul>
<li><code>default</code> — A video download.</li>
<li><code>audio</code> — An audio-only download.</li>
</ul>
<h3 id="streamurluploadparams">StreamUrlUploadParams</h3>
<p>Parameters for uploading a video from a URL.</p>
<ul>
<li>
<p><code>allowedOrigins</code> <span class="nb-type">Array&amp;lt;string&amp;gt;</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Lists the origins allowed to display the video. Enter allowed origin domains in an array and use <code>*</code> for wildcard subdomains. Empty arrays allow the video to be viewed on any origin.</li>
</ul>
</li>
<li>
<p><code>creator</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A user-defined identifier for the media creator.</li>
</ul>
</li>
<li>
<p><code>meta</code> <span class="nb-type">Record&amp;lt;string, string&amp;gt;</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A user modifiable key-value store used to reference other systems of record for managing videos.</li>
</ul>
</li>
<li>
<p><code>requireSignedURLs</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Indicates whether the video can be accessed using the ID. When set to <code>true</code>, a signed token must be generated with a signing key to view the video.</li>
</ul>
</li>
<li>
<p><code>scheduledDeletion</code> <span class="nb-type">string | null</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Indicates the date and time at which the video will be deleted. Omit the field to indicate no change, or include with a <code>null</code> value to remove an existing scheduled deletion. If specified, must be at least 30 days from upload time.</li>
</ul>
</li>
<li>
<p><code>thumbnailTimestampPct</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The timestamp for a thumbnail image calculated as a percentage value of the video's duration. To convert from a second-wise timestamp to a percentage, divide the desired timestamp by the total duration of the video. If this value is not set, the default thumbnail image is taken from 0s of the video.</li>
</ul>
</li>
<li>
<p><code>watermarkId</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The identifier for the watermark profile.</li>
</ul>
</li>
</ul>
<h3 id="streamdirectuploadcreateparams">StreamDirectUploadCreateParams</h3>
<p>Parameters for creating a direct upload.</p>
<ul>
<li>
<p><code>maxDurationSeconds</code> <span class="nb-type">number</span></p>
<ul>
<li>The maximum duration in seconds for a video upload.</li>
</ul>
</li>
<li>
<p><code>expiry</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The date and time after upload when videos will not be accepted.</li>
</ul>
</li>
<li>
<p><code>creator</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A user-defined identifier for the media creator.</li>
</ul>
</li>
<li>
<p><code>meta</code> <span class="nb-type">Record&amp;lt;string, string&amp;gt;</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A user modifiable key-value store used to reference other systems of record for managing videos.</li>
</ul>
</li>
<li>
<p><code>allowedOrigins</code> <span class="nb-type">Array&amp;lt;string&amp;gt;</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Lists the origins allowed to display the video.</li>
</ul>
</li>
<li>
<p><code>requireSignedURLs</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Indicates whether the video can be accessed using the ID. When set to <code>true</code>, a signed token must be generated with a signing key to view the video.</li>
</ul>
</li>
<li>
<p><code>thumbnailTimestampPct</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The timestamp for a thumbnail image calculated as a percentage value of the video's duration.</li>
</ul>
</li>
<li>
<p><code>scheduledDeletion</code> <span class="nb-type">string | null</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The date and time at which the video will be deleted. Include <code>null</code> to remove a scheduled deletion.</li>
</ul>
</li>
<li>
<p><code>watermark</code> <span class="nb-type">StreamDirectUploadWatermark</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The watermark profile to apply. Refer to <a href="#streamdirectuploadwatermark">StreamDirectUploadWatermark</a>.</li>
</ul>
</li>
</ul>
<h3 id="streamdirectuploadwatermark">StreamDirectUploadWatermark</h3>
<p>Watermark configuration for a direct upload.</p>
<ul>
<li>
<p><code>id</code> <span class="nb-type">string</span></p>
<ul>
<li>The unique identifier for the watermark profile.</li>
</ul>
</li>
</ul>
<h3 id="streamupdatevideoparams">StreamUpdateVideoParams</h3>
<p>Parameters for updating a video.</p>
<ul>
<li>
<p><code>allowedOrigins</code> <span class="nb-type">Array&amp;lt;string&amp;gt;</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Lists the origins allowed to display the video. Enter allowed origin domains in an array and use <code>*</code> for wildcard subdomains. Empty arrays allow the video to be viewed on any origin.</li>
</ul>
</li>
<li>
<p><code>creator</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A user-defined identifier for the media creator.</li>
</ul>
</li>
<li>
<p><code>maxDurationSeconds</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The maximum duration in seconds for a video upload. Can be set for a video that is not yet uploaded to limit its duration. Uploads that exceed the specified duration will fail during processing. A value of <code>-1</code> means the value is unknown.</li>
</ul>
</li>
<li>
<p><code>meta</code> <span class="nb-type">Record&amp;lt;string, string&amp;gt;</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A user modifiable key-value store used to reference other systems of record for managing videos.</li>
</ul>
</li>
<li>
<p><code>requireSignedURLs</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Indicates whether the video can be accessed using the ID. When set to <code>true</code>, a signed token must be generated with a signing key to view the video.</li>
</ul>
</li>
<li>
<p><code>scheduledDeletion</code> <span class="nb-type">string | null</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Indicates the date and time at which the video will be deleted. Omit the field to indicate no change, or include with a <code>null</code> value to remove an existing scheduled deletion. If specified, must be at least 30 days from upload time.</li>
</ul>
</li>
<li>
<p><code>thumbnailTimestampPct</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The timestamp for a thumbnail image calculated as a percentage value of the video's duration. To convert from a second-wise timestamp to a percentage, divide the desired timestamp by the total duration of the video. If this value is not set, the default thumbnail image is taken from 0s of the video.</li>
</ul>
</li>
</ul>
<h3 id="streamvideoslistparams">StreamVideosListParams</h3>
<p>Parameters for listing videos.</p>
<ul>
<li>
<p><code>limit</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The maximum number of videos to return.</li>
</ul>
</li>
<li>
<p><code>before</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Return videos created before this timestamp (RFC3339/RFC3339Nano).</li>
</ul>
</li>
<li>
<p><code>beforeComp</code> <span class="nb-type">StreamPaginationComparison</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Comparison operator for the <code>before</code> field. Defaults to <code>lt</code>. Refer to <a href="#streampaginationcomparison">StreamPaginationComparison</a>.</li>
</ul>
</li>
<li>
<p><code>after</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Return videos created after this timestamp (RFC3339/RFC3339Nano).</li>
</ul>
</li>
<li>
<p><code>afterComp</code> <span class="nb-type">StreamPaginationComparison</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Comparison operator for the <code>after</code> field. Defaults to <code>gte</code>. Refer to <a href="#streampaginationcomparison">StreamPaginationComparison</a>.</li>
</ul>
</li>
</ul>
<h3 id="streampaginationcomparison">StreamPaginationComparison</h3>
<p>Comparison operators for pagination queries.</p>
<p><span class="nb-type">eq' | 'gt' | 'gte' | 'lt' | 'lte</span></p>
<ul>
<li><code>eq</code> — Equal to</li>
<li><code>gt</code> — Greater than</li>
<li><code>gte</code> — Greater than or equal to</li>
<li><code>lt</code> — Less than</li>
<li><code>lte</code> — Less than or equal to</li>
</ul>
<h3 id="streamwatermarkcreateparams">StreamWatermarkCreateParams</h3>
<p>Parameters for creating a watermark profile.</p>
<ul>
<li>
<p><code>name</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A short description of the watermark profile.</li>
</ul>
</li>
<li>
<p><code>opacity</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The translucency of the image. A value of <code>0.0</code> makes the image completely transparent, and <code>1.0</code> makes the image completely opaque. Note that if the image is already semi-transparent, setting this to <code>1.0</code> will not make the image completely opaque.</li>
</ul>
</li>
<li>
<p><code>padding</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The whitespace between the adjacent edges (determined by position) of the video and the image. <code>0.0</code> indicates no padding, and <code>1.0</code> indicates a fully padded video width or length.</li>
</ul>
</li>
<li>
<p><code>scale</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The size of the image relative to the overall size of the video. <code>0.0</code> indicates no scaling, and <code>1.0</code> fills the entire video.</li>
</ul>
</li>
<li>
<p><code>position</code> <span class="nb-type">StreamWatermarkPosition</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The location of the image. Refer to <a href="#streamwatermarkposition">StreamWatermarkPosition</a>.</li>
</ul>
</li>
</ul>
<h2 id="error-handling">Error handling</h2>
<p>Errors throw a <code>StreamError</code>, which extends the standard <code>Error</code> interface with additional information:</p>
<ul>
<li><code>code</code>: A numeric error code.</li>
<li><code>statusCode</code>: An HTTP status code.</li>
<li><code>message</code>: A description of the error.</li>
<li><code>stack</code>: Optional stack trace.</li>
</ul>
<p>The following error subtypes may be thrown:</p>
<table>
<thead>
<tr>
<th>Error type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>InternalError</code></td>
<td>An internal server error occurred.</td>
</tr>
<tr>
<td><code>BadRequestError</code></td>
<td>The request was malformed or contained invalid parameters.</td>
</tr>
<tr>
<td><code>NotFoundError</code></td>
<td>The requested resource was not found.</td>
</tr>
<tr>
<td><code>ForbiddenError</code></td>
<td>The request was not authorized.</td>
</tr>
<tr>
<td><code>RateLimitedError</code></td>
<td>The request was rate limited.</td>
</tr>
<tr>
<td><code>QuotaReachedError</code></td>
<td>The account has reached its video quota.</td>
</tr>
<tr>
<td><code>MaxFileSizeError</code></td>
<td>The uploaded file exceeds the maximum allowed size.</td>
</tr>
<tr>
<td><code>InvalidURLError</code></td>
<td>The provided URL is invalid or unreachable.</td>
</tr>
<tr>
<td><code>AlreadyUploadedError</code></td>
<td>The video has already been uploaded.</td>
</tr>
<tr>
<td><code>TooManyWatermarksError</code></td>
<td>The account has reached the watermark profile limit.</td>
</tr>
</tbody>
</table>
<p>Use a <code>try...catch</code> block to handle errors:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14460.md")
</div>
