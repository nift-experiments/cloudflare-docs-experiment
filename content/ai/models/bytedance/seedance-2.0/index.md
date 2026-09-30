---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/
  description: bytedance/seedance-2.0
  full_title: Seedance 2.0 · Cloudflare AI docs
  head_html: <title>Seedance 2.0 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="bytedance/seedance-2.0"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Seedance 2.0 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="bytedance/seedance-2.0"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/#page","headline":"Seedance 2.0 \u00b7 Cloudflare AI docs","description":"bytedance/seedance-2.0","url":"https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/bytedance/seedance-2.0/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/bytedance.svg" alt="Bytedance logo" width="48" height="48">

<h1 id="seedance-2-0">Seedance 2.0</h1>

<p><code>bytedance/seedance-2.0</code></p>

ByteDance's next-generation video model with a unified multimodal architecture. Generates high-quality video with synchronized audio from text, images, video clips, and audio inputs. Supports multimodal references (up to 9 images, 3 videos, 3 audio files), native audio generation, video editing, video extension, intelligent duration, and adaptive aspect ratio.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.15, @480p video input (per second): 0.172, @720p video input (per second): 0.372, @1080p video input (per second): 0.914, @4k video input (per second): 1.866, @480p non-video input (per second): 0.07, @720p non-video input (per second): 0.15, @1080p non-video input (per second): 0.37, @4k non-video input (per second): 0.78</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-video with default settings

<section class="model-example"><strong>Simple Video</strong>
<p>Basic text-to-video with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever running through a field of sunflowers on a sunny day&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/simple-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/simple-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.0&#x27;,
  {
    prompt: &#x27;A golden retriever running through a field of sunflowers on a sunny day&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever running through a field of sunflowers on a sunny day&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Resolution Cinematic</strong>
<p>Cinematic video in 1080p</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A dramatic drone shot flying through misty mountain peaks at sunrise, cinematic lighting with volumetric fog&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 10,
    &quot;resolution&quot;: &quot;1080p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/high-resolution-cinematic.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/high-resolution-cinematic.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.0&#x27;,
  {
    prompt:
      &#x27;A dramatic drone shot flying through misty mountain peaks at sunrise, cinematic lighting with volumetric fog&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 10,
    resolution: &#x27;1080p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A dramatic drone shot flying through misty mountain peaks at sunrise, cinematic lighting with volumetric fog&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 10,
    &quot;resolution&quot;: &quot;1080p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Image to Video</strong>
<p>Generate video from a reference image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;image&quot;: &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&quot;,
    &quot;prompt&quot;: &quot;The character begins walking forward through the scene&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/image-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/image-to-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.0&#x27;,
  {
    image:
      &#x27;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&#x27;,
    prompt: &#x27;The character begins walking forward through the scene&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.0&quot;,
  &quot;input&quot;: {
    &quot;image&quot;: &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&quot;,
    &quot;prompt&quot;: &quot;The character begins walking forward through the scene&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Portrait Video</strong>
<p>Vertical video for social media</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Abstract ink drops spreading through water, vivid colors mixing in slow motion&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/portrait-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/portrait-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.0&#x27;,
  {
    prompt: &#x27;Abstract ink drops spreading through water, vivid colors mixing in slow motion&#x27;,
    aspect_ratio: &#x27;9:16&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Abstract ink drops spreading through water, vivid colors mixing in slow motion&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>4K Cinematic Video</strong>
<p>Generate a detailed cinematic video in 4K</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sweeping cinematic shot of a futuristic city skyline at dusk, flying past glass towers with neon reflections and dramatic clouds&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;4k&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/4k-cinematic-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/4k-cinematic-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.0&#x27;,
  {
    prompt:
      &#x27;A sweeping cinematic shot of a futuristic city skyline at dusk, flying past glass towers with neon reflections and dramatic clouds&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 5,
    resolution: &#x27;4k&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sweeping cinematic shot of a futuristic city skyline at dusk, flying past glass towers with neon reflections and dramatic clouds&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;4k&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Virtual Avatar Reference</strong>
<p>Use a virtual character avatar from the trusted asset library</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&quot;,
    &quot;prompt&quot;: &quot;The scene gently animates with subtle motion&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;use_virtual_avatar&quot;: true
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/virtual-avatar-reference.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0/virtual-avatar-reference.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.0&#x27;,
  {
    image: &#x27;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&#x27;,
    prompt: &#x27;The scene gently animates with subtle motion&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
    use_virtual_avatar: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.0&quot;,
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&quot;,
    &quot;prompt&quot;: &quot;The scene gently animates with subtle motion&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;use_virtual_avatar&quot;: true
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the video to generate</td></tr><tr><td><code>image</code></td><td>string</td><td>Reference image (HTTP(S) URL or base64 data URI) for image-to-video</td></tr><tr><td><code>reference_video</code></td><td>string</td><td>Reference video (HTTP(S) URL or base64 data URI) for style/motion guidance</td></tr><tr><td><code>last_frame_image</code></td><td>string</td><td>Reference image (HTTP(S) URL or base64 data URI) for last-frame guidance. Only works if an image start frame is also given.</td></tr><tr><td><code>reference_images</code></td><td>array</td><td>Reference images (1-4, HTTP(S) URLs or base64 data URIs) to guide video generation for characters, avatars, clothing, or environments. Cannot be used with 1080p resolution or first/last frame images.</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Required. Video duration in seconds Default: 5; Minimum: 4; Maximum: 12</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Video resolution Default: 720p; Values: 480p, 720p, 1080p, 4k</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Required. Video aspect ratio. Ignored if an image is used. Default: 16:9; Values: 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, 9:21</td></tr><tr><td><code>fps</code></td><td>number</td><td>Required. Frame rate (frames per second) Default: 24</td></tr><tr><td><code>camera_fixed</code></td><td>boolean</td><td>Required. Whether to fix camera position Default: False</td></tr><tr><td><code>generate_audio</code></td><td>boolean</td><td>Whether to generate audio with the video</td></tr><tr><td><code>watermark</code></td><td>boolean</td><td>Required. Whether to add a watermark to the output video Default: False</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducible generation Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>use_virtual_avatar</code></td><td>boolean</td><td>Required. Route image reference inputs (image, reference_images, last_frame_image) through ByteDance's trusted virtual avatar asset library before generation. Intended for AI-generated/virtual character avatars that would otherwise be blocked by face or deepfake detection Default: False</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the generated video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/bytedance/seedance-2.0/schema-input.json)
- [Output schema](/ai/models/bytedance/seedance-2.0/schema-output.json)

