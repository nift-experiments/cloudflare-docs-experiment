---
cp9:
  canonical: https://developers.cloudflare.com/stream/transform-videos/bindings/
  description: Bind the Media Transformations API to a Cloudflare Worker to transform videos programmatically.
  full_title: Bind to Workers API · Cloudflare Stream docs
  head_html: <title>Bind to Workers API · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Bind the Media Transformations API to a Cloudflare Worker to transform videos programmatically."><link rel="canonical" href="https://developers.cloudflare.com/stream/transform-videos/bindings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/transform-videos/bindings/index.md"><meta property="og:title" content="Bind to Workers API · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bind the Media Transformations API to a Cloudflare Worker to transform videos programmatically."><meta property="og:url" content="https://developers.cloudflare.com/stream/transform-videos/bindings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/transform-videos/bindings/#page","headline":"Bind to Workers API \u00b7 Cloudflare Stream docs","description":"Bind the Media Transformations API to a Cloudflare Worker to transform videos programmatically.","url":"https://developers.cloudflare.com/stream/transform-videos/bindings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/transform-videos/bindings/
  schema: 1
---
<p>A <a href="/workers/runtime-apis/bindings/">binding</a> connects your <a href="/workers/">Worker</a> to external resources on the Developer Platform, like <a href="/stream/transform-videos/">Media Transformations</a>, <a href="/r2/buckets/">R2 buckets</a>, or <a href="/kv/concepts/kv-namespaces/">KV namespaces</a>.</p>
<p>You can bind the Media Transformations API to your Worker to transform, resize, and extract content from videos without requiring them to be accessible through a URL.</p>
<p>For example, when you use Media Transformations within Workers, you can:</p>
<ul>
<li>Transform a video stored in a private R2 bucket or other protected source</li>
<li>Optimize videos and store the output directly back in R2 without serving it to the browser</li>
<li>Extract still frames and spritesheets for videos and use them for classification or description with <a href="/workers-ai/">Workers AI</a></li>
<li>Extract audio tracks from video files for dynamic transcription using Workers AI</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="beta-restrictions">Beta restrictions</h3>
@markup("md", "content/.markup/bodies/14394.md")
</aside>
<h2 id="setup">Setup</h2>
<p>The Media binding is enabled on a per-Worker basis.</p>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project directory.</p>
<p>To bind Media Transformations to your Worker, add the following to the end of your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/14395.md")
</div>
<p>Within your Worker code, you can interact with this binding by using <code>env.MEDIA.input()</code> to build an object that can manipulate the video (passed as a <code>ReadableStream</code>).</p>
<h2 id="methods">Methods</h2>
<p>The Media Transformations binding is similar to the <a href="/images/optimization/binding/">Images binding</a>, except the method chain order is fixed and the result of an <code>input()</code> cannot be reused across multiple transformations.</p>
<h3 id="input"><code>.input()</code></h3>
<p>The starting point for the Media binding, which accepts raw content.</p>
<ul>
<li>Accepts a <code>ReadableStream&lt;Uint8Array&gt;</code> containing the video bytes.</li>
</ul>
<h3 id="transform-optional"><code>.transform()</code> (optional)</h3>
<p>Defines how the video input should be transformed by resizing or cropping. This method is optional — if you do not need to resize or crop, you can call <code>.output()</code> directly on the result of <code>.input()</code>.</p>
<ul>
<li>Accepts the following parameters (all optional):
<ul>
<li><code>width</code>: Target width in pixels (10-2000).</li>
<li><code>height</code>: Target height in pixels (10-2000).</li>
<li><code>fit</code>: How to resize the video to fit the specified dimensions.
<ul>
<li><code>contain</code>: Scales the video to fit entirely within the output dimensions while respecting aspect ratio.</li>
<li><code>cover</code>: Scales the video to entirely cover the output dimensions with a center-weighted crop.</li>
<li><code>scale-down</code>: Same as <code>contain</code>, but only scales down. Does not upscale.</li>
</ul>
</li>
</ul>
</li>
<li>Refer to <a href="/stream/transform-videos/#options">Transform videos options</a> for more details.</li>
</ul>
<h3 id="output"><code>.output()</code></h3>
<p>Defines what to extract from the video and how the output will be formatted. Refer to <a href="/stream/transform-videos/#source-video-requirements">source video requirements</a> and <a href="/stream/transform-videos/#limitations">limitations</a> for input and output constraints.</p>
<ul>
<li>Accepts the following parameters:
<ul>
<li><code>mode</code>: The type of output to generate.
<ul>
<li><code>video</code>: Outputs an H.264/AAC optimized MP4 file.</li>
<li><code>frame</code>: Outputs a still image (JPEG or PNG).</li>
<li><code>spritesheet</code>: Outputs a JPEG containing multiple frames.</li>
<li><code>audio</code>: Outputs an AAC encoded M4A file.</li>
</ul>
</li>
<li><code>time</code>: Start timestamp for extraction (for example, <code>&quot;2s&quot;</code>, <code>&quot;1m&quot;</code>). Default: <code>&quot;0s&quot;</code>.</li>
<li><code>duration</code>: Duration of the output for <code>video</code>, <code>audio</code>, or <code>spritesheet</code> modes (for example, <code>&quot;5s&quot;</code>).</li>
<li><code>imageCount</code>: Number of frames to include in a spritesheet.</li>
<li><code>format</code>: Output format for <code>frame</code> mode (<code>jpg</code>, <code>png</code>) or <code>audio</code> mode (<code>m4a</code>).</li>
<li><code>audio</code>: Boolean to include or exclude audio in <code>video</code> mode. Default: <code>true</code>.</li>
</ul>
</li>
</ul>
<h3 id="result-methods">Result methods</h3>
<p>Finally, after configuring the output, three methods are available to receive results. These methods return Promises and must be awaited:</p>
<ul>
<li><code>.response()</code>: Returns a <code>Promise&lt;Response&gt;</code> — the transformed media as an HTTP Response object, ready to return to the client or store in cache.</li>
<li><code>.media()</code>: Returns a <code>Promise&lt;ReadableStream&lt;Uint8Array&gt;&gt;</code> — the transformed media as a byte stream.</li>
<li><code>.contentType()</code>: Returns a <code>Promise&lt;string&gt;</code> — the MIME type of the output (for example, <code>video/mp4</code>, <code>image/jpeg</code>, <code>audio/mp4</code>).</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="generate-an-optimized-video-clip">Generate an optimized video clip</h3>
<p>Resize a video and extract a five-second clip:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request, env) {&#10;		const video = await env.R2_BUCKET.get(&quot;input.mp4&quot;);&#10;&#10;		const result = env.MEDIA.input(video.body)&#10;			.transform({ width: 480, height: 270 })&#10;			.output({ mode: &quot;video&quot;, time: &quot;0s&quot;, duration: &quot;5s&quot; });&#10;&#10;		return await result.response();&#10;	},&#10;};&#10;</code></pre>
<h3 id="extract-a-still-frame">Extract a still frame</h3>
<p>Extract a single frame as a JPEG thumbnail:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request, env) {&#10;		const video = await env.R2_BUCKET.get(&quot;input.mp4&quot;);&#10;&#10;		const result = env.MEDIA.input(video.body)&#10;			.transform({ width: 640, height: 360 })&#10;			.output({ mode: &quot;frame&quot;, time: &quot;2s&quot;, format: &quot;jpg&quot; });&#10;&#10;		return await result.response();&#10;	},&#10;};&#10;</code></pre>
<h4 id="identify-content-with-media-transformations-and-workers-ai">Identify content with Media Transformations and Workers AI</h4>
<p>Extract a frame (still image) from a video, then use a model like <a href="/workers-ai/models/uform-gen2-qwen-500m/">UForm-Gen on Workers AI</a> to generate a caption.</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request, env) {&#10;		// First, load the video file from a source like R2 (or a fetch)&#10;&#10;		// Loading from R2&#10;		const video = await env.R2_BUCKET.get(&quot;input.mp4&quot;);&#10;&#10;		// Or using a fetch:&#10;		// const video = await fetch(&#x27;https://example.com/video.mp4&#x27;);&#10;&#10;		// Isolate a frame (still image)&#10;		const frame = await env.MEDIA.input(video.body)&#10;			.transform({ width: 720 })&#10;			.output({&#10;				mode: &#x27;frame&#x27;,&#10;				time: &#x27;3s&#x27;,&#10;			})&#10;			.response();&#10;&#10;		// Set up the payload for Workers AI&#10;		const payload = {&#10;			image: [...new Uint8Array(await frame.arrayBuffer())],&#10;			prompt: &quot;Generate a caption for this image&quot;,&#10;			max_tokens: 512,&#10;		};&#10;		const response = await env.AI.run(&#10;			&quot;@cf/unum/uform-gen2-qwen-500m&quot;,&#10;			payload&#10;		);&#10;		return new Response(JSON.stringify(response));&#10;	}&#10;}&#10;</code></pre>
<h3 id="extract-audio">Extract audio</h3>
<p>Extract the audio track from a video as an M4A file. This example demonstrates skipping <code>.transform()</code> since no resizing is needed:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request, env) {&#10;		const video = await env.R2_BUCKET.get(&quot;input.mp4&quot;);&#10;&#10;		const result = env.MEDIA.input(video.body).output({&#10;			mode: &quot;audio&quot;,&#10;			time: &quot;0s&quot;,&#10;			duration: &quot;30s&quot;,&#10;		});&#10;&#10;		return await result.response();&#10;	},&#10;};&#10;</code></pre>
<h4 id="transcribe-audio-with-media-transformations-and-workers-ai">Transcribe audio with Media Transformations and Workers AI</h4>
<p>Extract audio, then transcribe using <a href="/workers-ai/models/whisper/">Whisper on Workers AI</a>.</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request, env) {&#10;		// First, load the video file from a source like R2 (or a fetch)&#10;&#10;		// Loading from R2&#10;		const video = await env.R2_BUCKET.get(&quot;input.mp4&quot;);&#10;&#10;		// Or using a fetch:&#10;		// const video = await fetch(&#x27;https://example.com/video.mp4&#x27;);&#10;&#10;		// Extract audio using the media transformations binding:&#10;		const audio = await env.MEDIA.input(video.body)&#10;			.transform()&#10;			.output({&#10;				mode: &#x27;audio&#x27;,&#10;				})&#10;			.response();&#10;&#10;		// Prepare and run Workers AI inference&#10;		const payload = {&#10;			audio: [...new Uint8Array(await audio.arrayBuffer())],&#10;		};&#10;		const response = await env.AI.run(&#10;			&quot;@cf/openai/whisper&quot;,&#10;			payload&#10;		);&#10;&#10;		// response will have props {text, word_count, vtt, words}&#10;		return new Response(&#10;			JSON.stringify(response, null, 2),&#10;			{&#10;				headers: {&#x27;Content-Type&#x27;: &#x27;application/json&#x27;}&#10;			}&#10;		);&#10;	}&#10;}&#10;</code></pre>
<h3 id="store-transformed-output-in-r2">Store transformed output in R2</h3>
<p>Transform a video and store the result directly in R2:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request, env) {&#10;		const video = await env.R2_BUCKET.get(&quot;input.mp4&quot;);&#10;&#10;		const result = env.MEDIA.input(video.body)&#10;			.transform({ width: 480, height: 270, fit: &quot;contain&quot; })&#10;			.output({ mode: &quot;video&quot;, time: &quot;0s&quot;, duration: &quot;10s&quot;, audio: false });&#10;&#10;		// Store the transformed video directly in R2&#10;		await env.R2_BUCKET.put(&quot;output-480p.mp4&quot;, await result.media(), {&#10;			httpMetadata: { contentType: await result.contentType() },&#10;		});&#10;&#10;		return new Response(&quot;Video transformed and stored&quot;, { status: 200 });&#10;	},&#10;};&#10;</code></pre>
<h2 id="error-handling">Error handling</h2>
<p>Errors can be thrown at different points in the method chain:</p>
<ul>
<li><code>.input()</code> can throw errors related to account limits (free tier or subscription) or service disruptions.</li>
<li><code>.output()</code> can throw errors related to the transformation operation itself, such as invalid parameters or unsupported input formats.</li>
</ul>
<p>Errors throw a <code>MediaError</code>, which extends the standard <code>Error</code> interface with additional information:</p>
<ul>
<li><code>code</code>: A numeric error code.</li>
<li><code>message</code>: A description of the error.</li>
<li><code>stack</code>: Optional stack trace.</li>
</ul>
<p>Use a <code>try...catch</code> block to handle errors:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request, env) {&#10;		const video = await env.R2_BUCKET.get(&quot;input.mp4&quot;);&#10;&#10;		try {&#10;			const result = env.MEDIA.input(video.body)&#10;				.transform({ width: 480, height: 270 })&#10;				.output({ mode: &quot;video&quot;, time: &quot;0s&quot;, duration: &quot;5s&quot; });&#10;&#10;			return await result.response();&#10;		} catch (e) {&#10;			if (e instanceof Error &amp;&amp; &quot;code&quot; in e) {&#10;				// Handle MediaError&#10;				return new Response(`Transformation failed: ${e.message}`, {&#10;					status: 500,&#10;				});&#10;			}&#10;			throw e;&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h2 id="caching">Caching</h2>
<p>Unlike transformations via URL, responses from the Media binding are <em>not</em> automatically cached. Workers lets you interact directly with the <a href="/workers/runtime-apis/cache/">Cache API</a> to customize cache behavior. You can implement logic in your script to store transformations in Cloudflare's cache or R2 storage.</p>
<h2 id="billing">Billing</h2>
<p>Refer to Stream's <a href="/stream/pricing/">Pricing</a> information for costs. Transformations executed via the binding are billed on a per-operation basis, not based on request uniqueness. For best cost and performance optimization, cache or store outputs for reuse.</p>
<h2 id="local-development">Local development</h2>
<p>The Media Transformations API is available <em>in remote mode</em> for local development through <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the command-line interface for Workers. Transformations operations will be performed using a remote resource and are subject to usage charges beyond the included free tier.</p>
<p>To enable usage in local development, add <code>remote</code> to the binding configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/14396.md")
</div>
<p>Then run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14393.md")
</aside>
