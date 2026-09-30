---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/
  description: lightricks/ltx-2-5-fast
  full_title: LTX-2.5 Fast · Cloudflare AI docs
  head_html: <title>LTX-2.5 Fast · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="lightricks/ltx-2-5-fast"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="LTX-2.5 Fast · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="lightricks/ltx-2-5-fast"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/#page","headline":"LTX-2.5 Fast \u00b7 Cloudflare AI docs","description":"lightricks/ltx-2-5-fast","url":"https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/lightricks/ltx-2-5-fast/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Lightricks logo" width="48" height="48">

<h1 id="ltx-2-5-fast">LTX-2.5 Fast</h1>

<p><code>lightricks/ltx-2-5-fast</code></p>

Lightricks LTX-2.5 Fast is a fast video generation model for text-to-video and image-to-video workflows, with synchronized audio, configurable duration, resolution, and frame rate.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.09, @720p (per second): 0.09, @1080p (per second): 0.15, @2k (per second): 0.19, @4k (per second): 0.37</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a cinematic video from text

<section class="model-example"><strong>Text-to-Video</strong>
<p>Generate a cinematic video from text</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cinematic aerial shot of ocean waves at sunset&quot;,
    &quot;duration&quot;: 8,
    &quot;resolution&quot;: &quot;1920x1080&quot;,
    &quot;fps&quot;: 24,
    &quot;generate_audio&quot;: true
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/lightricks/ltx-2-5-fast/text-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/lightricks/ltx-2-5-fast/text-to-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;lightricks/ltx-2-5-fast&#x27;,
  {
    prompt: &#x27;A cinematic aerial shot of ocean waves at sunset&#x27;,
    duration: 8,
    resolution: &#x27;1920x1080&#x27;,
    fps: 24,
    generate_audio: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;lightricks/ltx-2-5-fast&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cinematic aerial shot of ocean waves at sunset&quot;,
    &quot;duration&quot;: 8,
    &quot;resolution&quot;: &quot;1920x1080&quot;,
    &quot;fps&quot;: 24,
    &quot;generate_audio&quot;: true
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Image-to-Video</strong>
<p>Animate a reference image with a final frame</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;The camera moves forward while the trees sway in the wind&quot;,
    &quot;image_uri&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg&quot;,
    &quot;last_frame_uri&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg&quot;,
    &quot;duration&quot;: 8,
    &quot;resolution&quot;: &quot;1920x1080&quot;,
    &quot;fps&quot;: 24,
    &quot;generate_audio&quot;: true
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/lightricks/ltx-2-5-fast/image-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/lightricks/ltx-2-5-fast/image-to-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;lightricks/ltx-2-5-fast&#x27;,
  {
    prompt: &#x27;The camera moves forward while the trees sway in the wind&#x27;,
    image_uri:
      &#x27;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg&#x27;,
    last_frame_uri:
      &#x27;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg&#x27;,
    duration: 8,
    resolution: &#x27;1920x1080&#x27;,
    fps: 24,
    generate_audio: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;lightricks/ltx-2-5-fast&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;The camera moves forward while the trees sway in the wind&quot;,
    &quot;image_uri&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg&quot;,
    &quot;last_frame_uri&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg&quot;,
    &quot;duration&quot;: 8,
    &quot;resolution&quot;: &quot;1920x1080&quot;,
    &quot;fps&quot;: 24,
    &quot;generate_audio&quot;: true
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the video Minimum length: 1</td></tr><tr><td><code>image_uri</code></td><td>string</td><td>HTTPS URI for the first frame</td></tr><tr><td><code>last_frame_uri</code></td><td>string</td><td>HTTPS URI for the last frame</td></tr><tr><td><code>duration</code></td><td>number</td><td>Required. Video duration in seconds Default: 8</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Default: 1920x1080; Values: 1280x720, 720x1280, 1920x1080, 1080x1920, 2560x1440, 1440x2560, 3840x2160, 2160x3840</td></tr><tr><td><code>fps</code></td><td>number</td><td>Required. Default: 24</td></tr><tr><td><code>generate_audio</code></td><td>boolean</td><td>Required. Default: True</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the generated video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/lightricks/ltx-2-5-fast/schema-input.json)
- [Output schema](/ai/models/lightricks/ltx-2-5-fast/schema-output.json)

