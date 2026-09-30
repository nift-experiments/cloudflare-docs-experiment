---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/pruna/p-video-replace/
  description: pruna/p-video-replace
  full_title: P-Video-Replace · Cloudflare AI docs
  head_html: <title>P-Video-Replace · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="pruna/p-video-replace"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/pruna/p-video-replace/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="P-Video-Replace · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="pruna/p-video-replace"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/pruna/p-video-replace/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/pruna/p-video-replace/#page","headline":"P-Video-Replace \u00b7 Cloudflare AI docs","description":"pruna/p-video-replace","url":"https://developers.cloudflare.com/ai/models/pruna/p-video-replace/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/pruna/p-video-replace/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Pruna logo" width="48" height="48">

<h1 id="p-video-replace">P-Video-Replace</h1>

<p><code>pruna/p-video-replace</code></p>

Pruna's P-Video-Replace takes a source video and one or more identity reference images, then places the referenced person or people into the video while preserving the source motion and audio.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Image-to-Video</td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.03, @720p (per second): 0.03, @1080p (per second): 0.06</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Replace the person in a source video with an identity reference image, preserving motion and audio.

<section class="model-example"><strong>Character Swap</strong>
<p>Replace the person in a source video with an identity reference image, preserving motion and audio.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;video&quot;: &quot;https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4&quot;,
    &quot;images&quot;: [
      &quot;https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg&quot;
    ],
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;target_fps&quot;: &quot;original&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/pruna/p-video-replace/character-swap.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/pruna/p-video-replace/character-swap.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pruna/p-video-replace&#x27;,
  {
    video: &#x27;https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4&#x27;,
    images: [&#x27;https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg&#x27;],
    resolution: &#x27;720p&#x27;,
    target_fps: &#x27;original&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pruna/p-video-replace&quot;,
  &quot;input&quot;: {
    &quot;video&quot;: &quot;https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4&quot;,
    &quot;images&quot;: [
      &quot;https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg&quot;
    ],
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;target_fps&quot;: &quot;original&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. Source RGB video (.mp4) used as the motion and audio source. HTTP(S) URL or data URI.</td></tr><tr><td><code>images</code></td><td>array</td><td>Required. Identity reference image(s), 1 to 3, to place into the video. Each entry is an HTTP(S) URL or a data URI.</td></tr><tr><td><code>turbo</code></td><td>boolean</td><td>Required. Turbo mode: faster generation for slightly lower quality. Default: False</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Target resolution. Default: 720p; Values: 720p, 1080p</td></tr><tr><td><code>save_audio</code></td><td>boolean</td><td>Required. Save the video with audio. Default: True</td></tr><tr><td><code>ignore_audio</code></td><td>boolean</td><td>Required. Ignore source audio during generation. Default: False</td></tr><tr><td><code>target_fps</code></td><td>string</td><td>Required. Target FPS for the working video. Default: original; Values: 24, 48, original</td></tr><tr><td><code>instruction_prompt</code></td><td>string</td><td>Required. Further instruction on how to place people from the reference images into the scene. Default:</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducible generation. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>disable_safety_checker</code></td><td>boolean</td><td>Required. Disable safety checker for generated videos. Default: False</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. Presigned URL for the replacement video.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/pruna/p-video-replace/schema-input.json)
- [Output schema](/ai/models/pruna/p-video-replace/schema-output.json)

