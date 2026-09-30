---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/google/veo-3.1/
  description: google/veo-3.1
  full_title: Veo 3.1 · Cloudflare AI docs
  head_html: <title>Veo 3.1 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="google/veo-3.1"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/google/veo-3.1/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Veo 3.1 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="google/veo-3.1"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/google/veo-3.1/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/google/veo-3.1/#page","headline":"Veo 3.1 \u00b7 Cloudflare AI docs","description":"google/veo-3.1","url":"https://developers.cloudflare.com/ai/models/google/veo-3.1/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/google/veo-3.1/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="veo-3-1">Veo 3.1</h1>

<p><code>google/veo-3.1</code></p>

Google's latest video generation model with improved quality, motion, and audio generation.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.4, @720p (per second): 0.2, @1080p (per second): 0.2, @4k (per second): 0.4, @720p w/ audio (per second): 0.4, @1080p w/ audio (per second): 0.4, @4k w/ audio (per second): 0.6</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

High quality nature footage

<section class="model-example"><strong>Nature Documentary</strong>
<p>High quality nature footage</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A majestic eagle soaring over snow-capped mountains, tracking shot following the bird as it glides through clouds&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: &quot;8s&quot;,
    &quot;generate_audio&quot;: true,
    &quot;resolution&quot;: &quot;1080p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/nature-documentary.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/nature-documentary.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/veo-3.1&#x27;,
  {
    prompt:
      &#x27;A majestic eagle soaring over snow-capped mountains, tracking shot following the bird as it glides through clouds&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: &#x27;8s&#x27;,
    generate_audio: true,
    resolution: &#x27;1080p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/veo-3.1&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A majestic eagle soaring over snow-capped mountains, tracking shot following the bird as it glides through clouds&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: &quot;8s&quot;,
    &quot;generate_audio&quot;: true,
    &quot;resolution&quot;: &quot;1080p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Urban Time-lapse</strong>
<p>City life time-lapse video</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A time-lapse of a busy city intersection at night, car lights creating streaks, people walking in fast motion&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: &quot;6s&quot;,
    &quot;generate_audio&quot;: true,
    &quot;resolution&quot;: &quot;1080p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/urban-time-lapse.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/urban-time-lapse.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/veo-3.1&#x27;,
  {
    prompt:
      &#x27;A time-lapse of a busy city intersection at night, car lights creating streaks, people walking in fast motion&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: &#x27;6s&#x27;,
    generate_audio: true,
    resolution: &#x27;1080p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/veo-3.1&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A time-lapse of a busy city intersection at night, car lights creating streaks, people walking in fast motion&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: &quot;6s&quot;,
    &quot;generate_audio&quot;: true,
    &quot;resolution&quot;: &quot;1080p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Abstract Art</strong>
<p>Abstract motion graphics</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Colorful ink drops falling into water in slow motion, creating organic swirling patterns&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: &quot;6s&quot;,
    &quot;generate_audio&quot;: false,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/abstract-art.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/abstract-art.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/veo-3.1&#x27;,
  {
    prompt:
      &#x27;Colorful ink drops falling into water in slow motion, creating organic swirling patterns&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: &#x27;6s&#x27;,
    generate_audio: false,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/veo-3.1&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Colorful ink drops falling into water in slow motion, creating organic swirling patterns&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: &quot;6s&quot;,
    &quot;generate_audio&quot;: false,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Food Video</strong>
<p>Appetizing food footage</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Melted chocolate being poured over fresh strawberries in slow motion, rich and glossy&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: &quot;4s&quot;,
    &quot;generate_audio&quot;: true,
    &quot;resolution&quot;: &quot;1080p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/food-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/food-video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/veo-3.1&#x27;,
  {
    prompt: &#x27;Melted chocolate being poured over fresh strawberries in slow motion, rich and glossy&#x27;,
    aspect_ratio: &#x27;9:16&#x27;,
    duration: &#x27;4s&#x27;,
    generate_audio: true,
    resolution: &#x27;1080p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/veo-3.1&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Melted chocolate being poured over fresh strawberries in slow motion, rich and glossy&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: &quot;4s&quot;,
    &quot;generate_audio&quot;: true,
    &quot;resolution&quot;: &quot;1080p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the video to generate</td></tr><tr><td><code>image_input</code></td><td>string</td><td>Base64-encoded reference image for i2v</td></tr><tr><td><code>duration</code></td><td>string</td><td>Required. Video duration Default: 6s; Values: 4s, 6s, 8s</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Required. Video aspect ratio Default: 16:9; Values: 16:9, 9:16, 1:1</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Video resolution Default: 720p; Values: 720p, 1080p</td></tr><tr><td><code>generate_audio</code></td><td>boolean</td><td>Required. Whether to generate audio with the video Default: True</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the generated video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/veo-3.1/schema-input.json)
- [Output schema](/ai/models/google/veo-3.1/schema-output.json)

