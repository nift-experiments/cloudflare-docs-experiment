---
cp9:
  canonical: https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/
  description: Upload large or resumable video files to Cloudflare Stream using the tus protocol.
  full_title: Resumable and large files (tus) · Cloudflare Stream docs
  head_html: <title>Resumable and large files (tus) · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Upload large or resumable video files to Cloudflare Stream using the tus protocol."><link rel="canonical" href="https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/index.md"><meta property="og:title" content="Resumable and large files (tus) · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upload large or resumable video files to Cloudflare Stream using the tus protocol."><meta property="og:url" content="https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/#page","headline":"Resumable and large files (tus) \u00b7 Cloudflare Stream docs","description":"Upload large or resumable video files to Cloudflare Stream using the tus protocol.","url":"https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/uploading-videos/resumable-uploads/
  schema: 1
---
<p>If you need to upload a video that is over 200 MB, you must use the <a href="https://tus.io/">tus protocol</a>. Even if the video is under 200 MB, if your connection is potentially unreliable, Cloudflare recommends using the tus protocol because it is resumable. A resumable upload ensures that the upload can be interrupted and resumed without uploading the previous data again.</p>
<p>To use the tus protocol with end user videos, refer to <a href="/stream/uploading-videos/direct-creator-uploads/#direct-creator-uploads-with-tus-protocol">Direct Creator Uploads with tus</a>.</p>
<p>If your video is under 200 MB and your connection is reliable, you can use a basic <code>POST</code> request instead. For direct API uploads using your API token, refer to <a href="/stream/uploading-videos/upload-video-file/">Upload via link</a>. For end user uploads, refer to <a href="/stream/uploading-videos/direct-creator-uploads/#basic-post-request">Basic POST request for Direct Creator Uploads</a>.</p>
<h2 id="requirements">Requirements</h2>
<ul>
<li>Resumable uploads require a minimum chunk size of 5,242,880 bytes unless the entire file is less than this amount. For better performance when the client connection is expected to be reliable, increase the chunk size to 52,428,800 bytes.</li>
<li>Maximum chunk size is 209,715,200 bytes.</li>
<li>Chunk size must be divisible by 256 KiB (256x1024 bytes). Round your chunk size to the nearest multiple of 256 KiB. Note that the final chunk of an upload that fits within a single chunk is exempt from this requirement.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you can upload a video using tus, you will need to download a tus client.</p>
<p>For more information, refer to the <a href="https://github.com/tus/tus-py-client">tus Python client</a> which is available through pip, Python's package manager.</p>
<pre tabindex="0"><code class="language-python">pip install -U tus.py&#10;</code></pre>
<h2 id="upload-a-video-using-tus">Upload a video using tus</h2>
<pre tabindex="0"><code class="language-sh">tus-upload --chunk-size 52428800 --header \&#10;Authorization &quot;Bearer &lt;API_TOKEN&gt;&quot;&#10;&lt;PATH_TO_VIDEO&gt; https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">INFO Creating file endpoint&#10;INFO Created: https://api.cloudflare.com/client/v4/accounts/d467d4f0fcbcd9791b613bc3a9599cdc/stream/dd5d531a12de0c724bd1275a3b2bc9c6&#10;...&#10;</code></pre>
<h3 id="golang-example">Golang example</h3>
<p>Before you begin, import a tus client such as <a href="https://github.com/eventials/go-tus">go-tus</a> to upload from your Go applications.</p>
<p>The <code>go-tus</code> library does not return the response headers to the calling function, which makes it difficult to read the video ID from the <code>stream-media-id</code> header. As a workaround, create a <a href="/stream/uploading-videos/direct-creator-uploads/">Direct Creator Upload</a> link. That API response will include the TUS endpoint as well as the video ID. Setting a Creator ID is not required.</p>
<pre tabindex="0"><code class="language-go">package main&#10;&#10;import (&#10;	&quot;net/http&quot;&#10;	&quot;os&quot;&#10;&#10;	tus &quot;github.com/eventials/go-tus&quot;&#10;)&#10;&#10;func main() {&#10;	accountID := &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;&#10;	f, err := os.Open(&quot;videofile.mp4&quot;)&#10;&#10;	if err != nil {&#10;		panic(err)&#10;	}&#10;&#10;	defer f.Close()&#10;&#10;	headers := make(http.Header)&#10;	headers.Add(&quot;Authorization&quot;, &quot;Bearer &lt;API_TOKEN&gt;&quot;)&#10;&#10;	config := &amp;tus.Config{&#10;		ChunkSize:           50 * 1024 * 1024, // Required a minimum chunk size of 5 MB, here we use 50 MB.&#10;		Resume:              false,&#10;		OverridePatchMethod: false,&#10;		Store:               nil,&#10;		Header:              headers,&#10;		HttpClient:          nil,&#10;	}&#10;&#10;	client, _ := tus.NewClient(&quot;https://api.cloudflare.com/client/v4/accounts/&quot;+ accountID +&quot;/stream&quot;, config)&#10;&#10;	upload, _ := tus.NewUploadFromFile(f)&#10;&#10;	uploader, _ := client.CreateUpload(upload)&#10;&#10;	uploader.Upload()&#10;}&#10;</code></pre>
<p>You can also get the progress of the upload if you are running the upload in a goroutine.</p>
<pre tabindex="0"><code class="language-go">// returns the progress percentage.&#10;upload.Progress()&#10;&#10;// returns whether or not the upload is complete.&#10;upload.Finished()&#10;</code></pre>
<p>Refer to <a href="https://github.com/eventials/go-tus">go-tus</a> for functionality such as resuming uploads.</p>
<h3 id="node-js-example">Node.js example</h3>
<p>Before you begin, install the tus-js-client.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i tus-js-client</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i tus-js-client" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add tus-js-client</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add tus-js-client" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add tus-js-client</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add tus-js-client" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add tus-js-client</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add tus-js-client" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Create an <code>index.js</code> file and configure:</p>
<ul>
<li>The API endpoint with your Cloudflare Account ID.</li>
<li>The request headers to include an API token.</li>
</ul>
<pre tabindex="0"><code class="language-js">var fs = require(&quot;fs&quot;);&#10;var tus = require(&quot;tus-js-client&quot;);&#10;&#10;// Specify location of file you would like to upload below&#10;var path = __dirname + &quot;/test.mp4&quot;;&#10;var file = fs.createReadStream(path);&#10;var size = fs.statSync(path).size;&#10;var mediaId = &quot;&quot;;&#10;&#10;var options = {&#10;	endpoint: &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream&quot;,&#10;	headers: {&#10;		Authorization: &quot;Bearer &lt;API_TOKEN&gt;&quot;,&#10;	},&#10;	chunkSize: 50 * 1024 * 1024, // Required a minimum chunk size of 5 MB. Here we use 50 MB.&#10;	retryDelays: [0, 3000, 5000, 10000, 20000], // Indicates to tus-js-client the delays after which it will retry if the upload fails.&#10;	metadata: {&#10;		name: &quot;test.mp4&quot;,&#10;		filetype: &quot;video/mp4&quot;,&#10;		// Optional if you want to include a watermark&#10;		// watermark: &#x27;&lt;WATERMARK_UID&gt;&#x27;,&#10;	},&#10;	uploadSize: size,&#10;	onError: function (error) {&#10;		throw error;&#10;	},&#10;	onProgress: function (bytesUploaded, bytesTotal) {&#10;		var percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2);&#10;		console.log(bytesUploaded, bytesTotal, percentage + &quot;%&quot;);&#10;	},&#10;	onSuccess: function () {&#10;		console.log(&quot;Upload finished&quot;);&#10;	},&#10;	onAfterResponse: function (req, res) {&#10;		return new Promise((resolve) =&gt; {&#10;			var mediaIdHeader = res.getHeader(&quot;stream-media-id&quot;);&#10;			if (mediaIdHeader) {&#10;				mediaId = mediaIdHeader;&#10;			}&#10;			resolve();&#10;		});&#10;	},&#10;};&#10;&#10;var upload = new tus.Upload(file, options);&#10;upload.start();&#10;</code></pre>
<h2 id="specify-upload-options">Specify upload options</h2>
<p>The tus protocol allows you to add optional parameters in the <a href="https://tus.io/protocols/resumable-upload.html#upload-metadata"><code>Upload-Metadata</code> header</a>.</p>
<h3 id="supported-options-in-upload-metadata">Supported options in <code>Upload-Metadata</code></h3>
<p>Setting arbitrary metadata values in the <code>Upload-Metadata</code> header sets values in the <a href="/api/resources/stream/methods/list/">meta key in Stream API</a>.</p>
<ul>
<li>
<p><code>name</code></p>
<ul>
<li>Setting this key will set <code>meta.name</code> in the API and display the value as the name of the video in the dashboard.</li>
</ul>
</li>
<li>
<p><code>requiresignedurls</code></p>
<ul>
<li>If this key is present, the video playback for this video will be required to use signed URLs after upload.</li>
</ul>
</li>
<li>
<p><code>scheduleddeletion</code></p>
<ul>
<li>Specifies a date and time when a video will be deleted. After a video is deleted, it is no longer viewable and no longer counts towards storage for billing. The specified date and time cannot be earlier than 30 days or later than 1,096 days from the video's created timestamp.</li>
</ul>
</li>
<li>
<p><code>allowedorigins</code></p>
<ul>
<li>An array of strings listing origins allowed to display the video. This will set the <a href="/stream/viewing-videos/securing-your-stream/#security-considerations">allowed origins setting</a> for the video.</li>
</ul>
</li>
<li>
<p><code>thumbnailtimestamppct</code></p>
<ul>
<li>Specify the default thumbnail <a href="/stream/viewing-videos/displaying-thumbnails/">timestamp percentage</a>. Note that percentage is a floating point value between 0.0 and 1.0.</li>
</ul>
</li>
<li>
<p><code>watermark</code></p>
<ul>
<li>The watermark profile UID.</li>
</ul>
</li>
</ul>
<h2 id="set-creator-property">Set creator property</h2>
<p>Setting a creator value in the <code>Upload-Creator</code> header can be used to identify the creator of the video content, linking the way you identify your users or creators to videos in your Stream account.</p>
<p>For examples of how to set and modify the creator ID, refer to <a href="/stream/manage-video-library/creator-id/">Associate videos with creators</a>.</p>
<h2 id="get-the-video-id-when-using-tus">Get the video ID when using tus</h2>
<p>When an initial tus request is made, Stream responds with a URL in the <code>Location</code> header. While this URL may contain the video ID, it is not recommend to parse this URL to get the ID.</p>
<p>Instead, you should use the <code>stream-media-id</code> HTTP header in the response to retrieve the video ID.</p>
<p>For example, a request made to <code>https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream</code> with the tus protocol will contain a HTTP header like the following:</p>
<pre tabindex="0"><code>stream-media-id: cab807e0c477d01baq20f66c3d1dfc26cf&#10;</code></pre>
