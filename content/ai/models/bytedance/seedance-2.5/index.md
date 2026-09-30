---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/
  description: bytedance/seedance-2.5
  full_title: Seedance 2.5 · Cloudflare AI docs
  head_html: <title>Seedance 2.5 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="bytedance/seedance-2.5"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Seedance 2.5 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="bytedance/seedance-2.5"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/#page","headline":"Seedance 2.5 \u00b7 Cloudflare AI docs","description":"bytedance/seedance-2.5","url":"https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/bytedance/seedance-2.5/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/bytedance.svg" alt="Bytedance logo" width="48" height="48">

<h1 id="seedance-2-5">Seedance 2.5</h1>

<p><code>bytedance/seedance-2.5</code></p>

ByteDance's next-generation video model with a unified multimodal reference-to-video architecture. Generates video from text, up to 30 reference images, 10 reference videos, and 10 reference audio clips — including audio-only input with no image or video required. Supports first/last-frame image-to-video, video editing, video extension, intelligent duration (including automatic selection), and adaptive aspect ratio.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.2312, @480p video input (per second): 0.4304, @720p video input (per second): 0.9676, @480p non-video input (per second): 0.1028, @720p non-video input (per second): 0.2312</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-video with default settings (adaptive aspect ratio, 720p)

<section class="model-example"><strong>Simple Video</strong>
<p>Basic text-to-video with default settings (adaptive aspect ratio, 720p)</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever running through a field of sunflowers on a sunny day&quot;,
    &quot;duration&quot;: 5,
    &quot;generate_audio&quot;: false,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.5/simple-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.5/simple-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.5&#x27;,
  {
    prompt: &#x27;A golden retriever running through a field of sunflowers on a sunny day&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever running through a field of sunflowers on a sunny day&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Cinematic Wide Shot</strong>
<p>Longer cinematic video with an explicit 16:9 aspect ratio</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A dramatic drone shot flying through misty mountain peaks at sunrise, cinematic lighting with volumetric fog&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 12,
    &quot;generate_audio&quot;: false,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.5/cinematic-wide-shot.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.5/cinematic-wide-shot.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.5&#x27;,
  {
    prompt:
      &#x27;A dramatic drone shot flying through misty mountain peaks at sunrise, cinematic lighting with volumetric fog&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 12,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A dramatic drone shot flying through misty mountain peaks at sunrise, cinematic lighting with volumetric fog&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 12,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>First and Last Frame</strong>
<p>Generate a video that transitions between a given first-frame and last-frame image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&quot;,
    &quot;last_frame_image&quot;: &quot;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic2.jpg&quot;,
    &quot;prompt&quot;: &quot;The character slowly turns to face the camera and smiles&quot;,
    &quot;duration&quot;: 5,
    &quot;generate_audio&quot;: false,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.5/first-and-last-frame.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.5/first-and-last-frame.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.5&#x27;,
  {
    image: &#x27;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&#x27;,
    last_frame_image: &#x27;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic2.jpg&#x27;,
    prompt: &#x27;The character slowly turns to face the camera and smiles&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.5&quot;,
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&quot;,
    &quot;last_frame_image&quot;: &quot;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic2.jpg&quot;,
    &quot;prompt&quot;: &quot;The character slowly turns to face the camera and smiles&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Portrait Video with MOV Output</strong>
<p>Vertical video for social media, encoded as mov for higher color fidelity</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Abstract ink drops spreading through water, vivid colors mixing in slow motion&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;generate_audio&quot;: false,
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;output_format&quot;: &quot;mov&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.5/portrait-video-with-mov-output.mov&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.5/portrait-video-with-mov-output.mov&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.5&#x27;,
  {
    prompt: &#x27;Abstract ink drops spreading through water, vivid colors mixing in slow motion&#x27;,
    aspect_ratio: &#x27;9:16&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
    output_format: &#x27;mov&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Abstract ink drops spreading through water, vivid colors mixing in slow motion&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;output_format&quot;: &quot;mov&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Text prompt describing the video to generate. Optional when at least one reference image, video, or audio clip is provided (Seedance 2.5 supports audio-only input).</td></tr><tr><td><code>image</code></td><td>string</td><td>First-frame reference image (HTTP(S) URL or base64 data URI) for image-to-video</td></tr><tr><td><code>last_frame_image</code></td><td>string</td><td>Last-frame reference image (HTTP(S) URL or base64 data URI). Requires a first-frame image to also be given.</td></tr><tr><td><code>reference_images</code></td><td>array</td><td>Reference images (0-30, HTTP(S) URLs or base64 data URIs) to guide multimodal video generation, editing, or extension.</td></tr><tr><td><code>reference_videos</code></td><td>array</td><td>Reference videos (0-10, HTTP(S) URLs or base64 data URIs) for style/motion guidance, video editing, or video extension. Total duration of all reference videos must not exceed 30 seconds.</td></tr><tr><td><code>reference_audios</code></td><td>array</td><td>Reference audio clips (0-10, HTTP(S) URLs or base64 data:audio/... URIs). Supports audio-only input (no image or video required). Total duration of all audio clips must not exceed 30 seconds.</td></tr><tr><td><code>duration</code></td><td>number or integer</td><td>Required. Generated video duration in seconds. Supported range: 4-30, or -1 for automatic selection. For multimodal reference-to-video requests that edit an input reference video, only -1 is supported and the output duration is kept close to the input. Default: 5</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Video resolution Default: 720p; Values: 480p, 720p</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Required. Video aspect ratio. "adaptive" automatically matches the aspect ratio of the provided reference image or video when applicable. First/last-frame generation always uses "adaptive"; any supplied value is overridden. Default: adaptive; Values: 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, adaptive</td></tr><tr><td><code>fps</code></td><td>number</td><td>Required. Frame rate (frames per second) Default: 24</td></tr><tr><td><code>camera_fixed</code></td><td>boolean</td><td>Required. Whether to fix camera position. Not currently supported by the provider; has no effect. Default: False</td></tr><tr><td><code>generate_audio</code></td><td>boolean</td><td>Whether to generate audio with the video</td></tr><tr><td><code>watermark</code></td><td>boolean</td><td>Required. Whether to add a watermark to the output video Default: False</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed. Passing this does not error, but reproducibility is not guaranteed and is not documented by the provider. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Required. Output video container format. "mp4" offers the best compatibility and smaller file size; "mov" preserves higher color fidelity for professional post-production workflows at the cost of a larger file. Default: mp4; Values: mp4, mov</td></tr><tr><td><code>use_virtual_avatar</code></td><td>boolean</td><td>Required. Route image reference inputs (image, reference_images, last_frame_image) through ByteDance's trusted virtual avatar asset library before generation. Intended for AI-generated/virtual character avatars that would otherwise be blocked by face or deepfake detection Default: False</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the generated video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/bytedance/seedance-2.5/schema-input.json)
- [Output schema](/ai/models/bytedance/seedance-2.5/schema-output.json)

