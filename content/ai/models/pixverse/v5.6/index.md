---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/pixverse/v5.6/
  description: pixverse/v5.6
  full_title: Pixverse v5.6 · Cloudflare AI docs
  head_html: <title>Pixverse v5.6 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="pixverse/v5.6"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/pixverse/v5.6/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Pixverse v5.6 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="pixverse/v5.6"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/pixverse/v5.6/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/pixverse/v5.6/#page","headline":"Pixverse v5.6 \u00b7 Cloudflare AI docs","description":"pixverse/v5.6","url":"https://developers.cloudflare.com/ai/models/pixverse/v5.6/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/pixverse/v5.6/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/pixverse.svg" alt="Pixverse logo" width="48" height="48">

<h1 id="pixverse-v5-6">Pixverse v5.6</h1>

<p><code>pixverse/v5.6</code></p>

Pixverse v5.6 is a video generation model supporting text-to-video and image-to-video with audio generation, customizable aspect ratios, and up to 1080p output.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://pixverse.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.08, 5s @360p: 0.175, 5s @360p w/ audio: 0.4, 8s @360p: 0.35, 8s @360p w/ audio: 0.575, 10s @360p: 0.385, 10s @360p w/ audio: 0.61, 5s @540p: 0.175, 5s @540p w/ audio: 0.45, 8s @540p: 0.35, 8s @540p w/ audio: 0.575, 10s @540p: 0.385, 10s @540p w/ audio: 0.61, 5s @720p: 0.225, 5s @720p w/ audio: 0.4, 8s @720p: 0.45, 8s @720p w/ audio: 0.675, 10s @720p: 0.495, 10s @720p w/ audio: 0.72, 5s @1080p: 0.375, 5s @1080p w/ audio: 0.75, 8s @1080p: 0.75, 8s @1080p w/ audio: 0.975</td></tr>
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
    &quot;generate_audio&quot;: true,
    &quot;quality&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/pixverse__v5.6/simple-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://media.pixverse.ai/pixverse%2Fmp4%2Fmedia%2Fweb%2Fori%2F83ca9c7f-6387-4a2c-8d92-bb90a3d519e7_seed1453814635.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pixverse/v5.6&#x27;,
  {
    prompt: &#x27;A golden retriever running through a field of sunflowers on a sunny day&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 5,
    generate_audio: true,
    quality: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pixverse/v5.6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever running through a field of sunflowers on a sunny day&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;generate_audio&quot;: true,
    &quot;quality&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Cinematic Scene with Audio</strong>
<p>Dramatic cinematic video with audio generation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A dramatic aerial shot flying over misty mountain peaks at sunrise, cinematic lighting with volumetric fog&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 8,
    &quot;generate_audio&quot;: true,
    &quot;quality&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/pixverse__v5.6/cinematic-scene-with-audio.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://media.pixverse.ai/pixverse%2Fmp4%2Fmedia%2Fweb%2Fori%2F77e1e5bd-4be9-4b7b-961a-36328e90d7e0_seed735995758.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pixverse/v5.6&#x27;,
  {
    prompt:
      &#x27;A dramatic aerial shot flying over misty mountain peaks at sunrise, cinematic lighting with volumetric fog&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 8,
    generate_audio: true,
    quality: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pixverse/v5.6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A dramatic aerial shot flying over misty mountain peaks at sunrise, cinematic lighting with volumetric fog&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 8,
    &quot;generate_audio&quot;: true,
    &quot;quality&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Portrait Video</strong>
<p>Vertical video for social media</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A barista pouring latte art in a cozy coffee shop, close-up with shallow depth of field&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;generate_audio&quot;: true,
    &quot;quality&quot;: &quot;540p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/pixverse__v5.6/portrait-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://media.pixverse.ai/pixverse%2Fmp4%2Fmedia%2Fweb%2Fori%2Fa95971bd-798d-431e-8c78-8062b839742c_seed1048220235.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pixverse/v5.6&#x27;,
  {
    prompt: &#x27;A barista pouring latte art in a cozy coffee shop, close-up with shallow depth of field&#x27;,
    aspect_ratio: &#x27;9:16&#x27;,
    duration: 5,
    generate_audio: true,
    quality: &#x27;540p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pixverse/v5.6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A barista pouring latte art in a cozy coffee shop, close-up with shallow depth of field&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;generate_audio&quot;: true,
    &quot;quality&quot;: &quot;540p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>High Quality Video</strong>
<p>High quality 1080p video with custom seed</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Abstract ink drops spreading through water, vivid colors mixing in slow motion&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;duration&quot;: 5,
    &quot;generate_audio&quot;: true,
    &quot;negative_prompt&quot;: &quot;blurry, low quality&quot;,
    &quot;quality&quot;: &quot;1080p&quot;,
    &quot;seed&quot;: 12345
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/pixverse__v5.6/high-quality-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://media.pixverse.ai/pixverse%2Fmp4%2Fmedia%2Fweb%2Fori%2F557c18df-6c50-409c-a5e5-291bb2086d3f_seed12345.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pixverse/v5.6&#x27;,
  {
    prompt: &#x27;Abstract ink drops spreading through water, vivid colors mixing in slow motion&#x27;,
    aspect_ratio: &#x27;1:1&#x27;,
    duration: 5,
    generate_audio: true,
    negative_prompt: &#x27;blurry, low quality&#x27;,
    quality: &#x27;1080p&#x27;,
    seed: 12345,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pixverse/v5.6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Abstract ink drops spreading through water, vivid colors mixing in slow motion&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;duration&quot;: 5,
    &quot;generate_audio&quot;: true,
    &quot;negative_prompt&quot;: &quot;blurry, low quality&quot;,
    &quot;quality&quot;: &quot;1080p&quot;,
    &quot;seed&quot;: 12345
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the video to generate</td></tr><tr><td><code>negative_prompt</code></td><td>string</td><td>Negative text prompt</td></tr><tr><td><code>image_input</code></td><td>string</td><td>Base64-encoded reference image for image-to-video generation (data:image/...;base64,...). The image will be uploaded to Pixverse automatically.</td></tr><tr><td><code>duration</code></td><td>number</td><td>Required. Video duration in seconds Default: 5</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Required. Video aspect ratio Default: 16:9; Values: 16:9, 4:3, 1:1, 3:4, 9:16, 2:3, 3:2, 21:9</td></tr><tr><td><code>quality</code></td><td>string</td><td>Required. Video quality Default: 720p; Values: 360p, 540p, 720p, 1080p</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducibility Minimum: 0; Maximum: 2147483647</td></tr><tr><td><code>motion_mode</code></td><td>string</td><td>Motion mode (fast only available when duration=5; 1080p does not support fast) Values: normal, fast</td></tr><tr><td><code>generate_audio</code></td><td>boolean</td><td>Required. Whether to generate audio with the video Default: True</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the generated video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/pixverse/v5.6/schema-input.json)
- [Output schema](/ai/models/pixverse/v5.6/schema-output.json)

