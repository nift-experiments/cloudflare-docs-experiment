---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/pruna/p-video/
  description: pruna/p-video
  full_title: P-Video · Cloudflare AI docs
  head_html: <title>P-Video · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="pruna/p-video"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/pruna/p-video/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="P-Video · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="pruna/p-video"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/pruna/p-video/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/pruna/p-video/#page","headline":"P-Video \u00b7 Cloudflare AI docs","description":"pruna/p-video","url":"https://developers.cloudflare.com/ai/models/pruna/p-video/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/pruna/p-video/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Pruna logo" width="48" height="48">

<h1 id="p-video">P-Video</h1>

<p><code>pruna/p-video</code></p>

Pruna's P-Video is a premium video generation model supporting text-to-video, image-to-video, and audio-conditioned generation up to 1080p at 24 or 48 fps, with configurable duration up to 20 seconds.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.02, @720p (per second): 0.02, @1080p (per second): 0.04, @720p draft (per second): 0.005, @1080p draft (per second): 0.01</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a short cinematic clip from a text prompt in draft mode for fast, low-cost previews.

<section class="model-example"><strong>Neon City Drift</strong>
<p>Generate a short cinematic clip from a text prompt in draft mode for fast, low-cost previews.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sports car drifting through a neon-lit city at night, cinematic aerial shot&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;draft&quot;: true
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/pruna/p-video/neon-city-drift.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/pruna/p-video/neon-city-drift.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pruna/p-video&#x27;,
  {
    prompt: &#x27;A sports car drifting through a neon-lit city at night, cinematic aerial shot&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    draft: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pruna/p-video&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sports car drifting through a neon-lit city at night, cinematic aerial shot&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;draft&quot;: true
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt for video generation.</td></tr><tr><td><code>image</code></td><td>string</td><td>Input image to generate video from (image-to-video). HTTP(S) URL or data URI. Supports jpg, jpeg, png, webp. When provided, aspect_ratio is ignored.</td></tr><tr><td><code>audio</code></td><td>string</td><td>Input audio to condition video generation. HTTP(S) URL or data URI. Supports flac, mp3, wav. When provided, duration is ignored.</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Required. Duration of the video in seconds (1-20). Ignored when audio is provided. Default: 5; Minimum: 1; Maximum: 20</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Video resolution. Default: 720p; Values: 720p, 1080p</td></tr><tr><td><code>fps</code></td><td>number</td><td>Required. Frames per second: 24 or 48. Default: 24</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Required. Aspect ratio of the video. Ignored when an input image is provided. Default: 16:9; Values: 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 1:1</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducible generation. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>draft</code></td><td>boolean</td><td>Required. Draft mode. Generates a lower-quality preview of the video. Default: False</td></tr><tr><td><code>save_audio</code></td><td>boolean</td><td>Required. Save the video with audio. Default: True</td></tr><tr><td><code>last_frame_image</code></td><td>string</td><td>Reference image for the last frame of the video. HTTP(S) URL or data URI.</td></tr><tr><td><code>prompt_upsampling</code></td><td>boolean</td><td>Required. Use prompt upsampling to enhance the prompt. Default: True</td></tr><tr><td><code>disable_safety_filter</code></td><td>boolean</td><td>Required. Disable safety filter for prompts and input images. Default: True</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. Presigned URL for the generated video.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/pruna/p-video/schema-input.json)
- [Output schema](/ai/models/pruna/p-video/schema-output.json)

