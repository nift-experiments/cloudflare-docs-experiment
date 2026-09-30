---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/pixverse/v6/
  description: pixverse/v6
  full_title: Pixverse v6 · Cloudflare AI docs
  head_html: <title>Pixverse v6 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="pixverse/v6"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/pixverse/v6/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Pixverse v6 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="pixverse/v6"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/pixverse/v6/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/pixverse/v6/#page","headline":"Pixverse v6 \u00b7 Cloudflare AI docs","description":"pixverse/v6","url":"https://developers.cloudflare.com/ai/models/pixverse/v6/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/pixverse/v6/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/pixverse.svg" alt="Pixverse logo" width="48" height="48">

<h1 id="pixverse-v6">Pixverse v6</h1>

<p><code>pixverse/v6</code></p>

Pixverse v6 is the latest Pixverse video model with support for up to 15-second videos, customizable duration from 1 to 15 seconds, and audio generation.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://pixverse.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.06, @360p (per second): 0.025, @540p (per second): 0.035, @720p (per second): 0.045, @1080p (per second): 0.09, @360p w/ audio (per second): 0.035, @540p w/ audio (per second): 0.045, @720p w/ audio (per second): 0.06, @1080p w/ audio (per second): 0.115</td></tr>
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
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/pixverse__v6/simple-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://media.pixverse.ai/pixverse%2Fmp4%2Fmedia%2Fweb%2Fori%2Fda2a0d44-a700-4c6b-a36b-fff6951fd1d4_seed1150795460.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pixverse/v6&#x27;,
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
  &quot;model&quot;: &quot;pixverse/v6&quot;,
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

<section class="model-example"><strong>Long Duration Video</strong>
<p>Extended 15-second video with audio (v6 supports 1-15 seconds)</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A time-lapse of a bustling city street from dawn to dusk, showing the flow of people and vehicles&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 15,
    &quot;generate_audio&quot;: true,
    &quot;quality&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/pixverse__v6/long-duration-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://media.pixverse.ai/pixverse%2Fmp4%2Fmedia%2Fweb%2Fori%2F46e3adfb-a95f-4c03-bdad-a6d7131a98b8_seed61570270.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pixverse/v6&#x27;,
  {
    prompt:
      &#x27;A time-lapse of a bustling city street from dawn to dusk, showing the flow of people and vehicles&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 15,
    generate_audio: true,
    quality: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pixverse/v6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A time-lapse of a bustling city street from dawn to dusk, showing the flow of people and vehicles&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 15,
    &quot;generate_audio&quot;: true,
    &quot;quality&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Ultra-wide Cinematic</strong>
<p>Cinematic 21:9 aspect ratio video</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A dramatic aerial shot flying over misty mountain peaks at sunrise, cinematic lighting with volumetric fog&quot;,
    &quot;aspect_ratio&quot;: &quot;21:9&quot;,
    &quot;duration&quot;: 10,
    &quot;generate_audio&quot;: true,
    &quot;quality&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/pixverse__v6/ultra-wide-cinematic.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://media.pixverse.ai/pixverse%2Fmp4%2Fmedia%2Fweb%2Fori%2F54327d38-e03a-44de-9a21-2052356779e5_seed286185598.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pixverse/v6&#x27;,
  {
    prompt:
      &#x27;A dramatic aerial shot flying over misty mountain peaks at sunrise, cinematic lighting with volumetric fog&#x27;,
    aspect_ratio: &#x27;21:9&#x27;,
    duration: 10,
    generate_audio: true,
    quality: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pixverse/v6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A dramatic aerial shot flying over misty mountain peaks at sunrise, cinematic lighting with volumetric fog&quot;,
    &quot;aspect_ratio&quot;: &quot;21:9&quot;,
    &quot;duration&quot;: 10,
    &quot;generate_audio&quot;: true,
    &quot;quality&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Silent Video</strong>
<p>Video without audio generation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Abstract ink drops spreading through water, vivid colors mixing in slow motion&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;duration&quot;: 3,
    &quot;generate_audio&quot;: false,
    &quot;negative_prompt&quot;: &quot;blurry, low quality&quot;,
    &quot;quality&quot;: &quot;540p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/pixverse__v6/silent-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://media.pixverse.ai/pixverse%2Fmp4%2Fmedia%2Fweb%2Fori%2F06c27c41-cadd-44c5-b418-a78b96555479_seed1048443720.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pixverse/v6&#x27;,
  {
    prompt: &#x27;Abstract ink drops spreading through water, vivid colors mixing in slow motion&#x27;,
    aspect_ratio: &#x27;1:1&#x27;,
    duration: 3,
    generate_audio: false,
    negative_prompt: &#x27;blurry, low quality&#x27;,
    quality: &#x27;540p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pixverse/v6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Abstract ink drops spreading through water, vivid colors mixing in slow motion&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;duration&quot;: 3,
    &quot;generate_audio&quot;: false,
    &quot;negative_prompt&quot;: &quot;blurry, low quality&quot;,
    &quot;quality&quot;: &quot;540p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the video to generate</td></tr><tr><td><code>negative_prompt</code></td><td>string</td><td>Negative text prompt</td></tr><tr><td><code>image_input</code></td><td>string</td><td>Base64-encoded reference image for image-to-video generation (data:image/...;base64,...). The image will be uploaded to Pixverse automatically.</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Required. Video duration in seconds (1 to 15) Default: 5; Minimum: 1; Maximum: 15</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Required. Video aspect ratio Default: 16:9; Values: 16:9, 4:3, 1:1, 3:4, 9:16, 2:3, 3:2, 21:9</td></tr><tr><td><code>quality</code></td><td>string</td><td>Required. Video quality Default: 720p; Values: 360p, 540p, 720p, 1080p</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducibility Minimum: 0; Maximum: 2147483647</td></tr><tr><td><code>generate_audio</code></td><td>boolean</td><td>Required. Whether to generate audio with the video Default: True</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the generated video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/pixverse/v6/schema-input.json)
- [Output schema](/ai/models/pixverse/v6/schema-output.json)

