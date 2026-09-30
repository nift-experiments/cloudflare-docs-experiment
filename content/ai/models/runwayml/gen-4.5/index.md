<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Runwayml logo" width="48" height="48">

<h1 id="runwayml-gen-4-5">RunwayML Gen-4.5</h1>

<p><code>runwayml/gen-4.5</code></p>

RunwayML's video generation model supporting both text-to-video and image-to-video with customizable duration, aspect ratio, and content moderation controls.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://runwayml.com/terms-of-use">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.12</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-video with default settings

<section class="model-example"><strong>Simple Text-to-Video</strong>
<p>Basic text-to-video with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A timelapse of the Eiffel Tower on a sunny day with clouds flying by&quot;,
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;1280:720&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/simple-text-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/fd840364-360e-4903-8500-d5787fd8ab90.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/gen-4.5&#x27;,
  {
    prompt: &#x27;A timelapse of the Eiffel Tower on a sunny day with clouds flying by&#x27;,
    duration: 5,
    ratio: &#x27;1280:720&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/gen-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A timelapse of the Eiffel Tower on a sunny day with clouds flying by&quot;,
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;1280:720&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Portrait Video</strong>
<p>Vertical video for social media</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A busy street in Tokyo at night with neon signs reflecting on wet pavement, rain falling&quot;,
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;720:1280&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/portrait-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/44f43eac-8c12-4084-ace3-6395fa67c13e.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/gen-4.5&#x27;,
  {
    prompt:
      &#x27;A busy street in Tokyo at night with neon signs reflecting on wet pavement, rain falling&#x27;,
    duration: 5,
    ratio: &#x27;720:1280&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/gen-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A busy street in Tokyo at night with neon signs reflecting on wet pavement, rain falling&quot;,
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;720:1280&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Nature Close-up</strong>
<p>Close-up wildlife shot in 16:9</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Close-up of a hummingbird feeding from a vibrant red flower, slow motion with soft bokeh background&quot;,
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;1280:720&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/nature-close-up.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/e03781eb-2544-45ae-a9a8-6148d556bf2a.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/gen-4.5&#x27;,
  {
    prompt:
      &#x27;Close-up of a hummingbird feeding from a vibrant red flower, slow motion with soft bokeh background&#x27;,
    duration: 5,
    ratio: &#x27;1280:720&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/gen-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Close-up of a hummingbird feeding from a vibrant red flower, slow motion with soft bokeh background&quot;,
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;1280:720&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Cinematic Scene</strong>
<p>Longer duration cinematic video</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Aerial drone shot flying through a misty forest at dawn, rays of sunlight breaking through the trees&quot;,
    &quot;duration&quot;: 10,
    &quot;ratio&quot;: &quot;1280:720&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/23ea177e-523d-45b4-9f8c-c4f8d7238ff0.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/gen-4.5&#x27;,
  {
    prompt:
      &#x27;Aerial drone shot flying through a misty forest at dawn, rays of sunlight breaking through the trees&#x27;,
    duration: 10,
    ratio: &#x27;1280:720&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/gen-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Aerial drone shot flying through a misty forest at dawn, rays of sunlight breaking through the trees&quot;,
    &quot;duration&quot;: 10,
    &quot;ratio&quot;: &quot;1280:720&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Image-to-Video</strong>
<p>Animate an existing image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Camera slowly pans across the scene, gentle wind blowing&quot;,
    &quot;duration&quot;: 5,
    &quot;image_input&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg&quot;,
    &quot;ratio&quot;: &quot;1280:720&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/image-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/ab424367-7431-4a0a-aa39-52604ff9150a.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/gen-4.5&#x27;,
  {
    prompt: &#x27;Camera slowly pans across the scene, gentle wind blowing&#x27;,
    duration: 5,
    image_input:
      &#x27;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg&#x27;,
    ratio: &#x27;1280:720&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/gen-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Camera slowly pans across the scene, gentle wind blowing&quot;,
    &quot;duration&quot;: 5,
    &quot;image_input&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg&quot;,
    &quot;ratio&quot;: &quot;1280:720&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Reproducible Generation</strong>
<p>Use seed for consistent results</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sailboat gliding across calm ocean waters at sunset&quot;,
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;1280:720&quot;,
    &quot;seed&quot;: 42
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/reproducible-generation.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/0bdfbec7-0823-4529-bdb5-d37bb24adb0d.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/gen-4.5&#x27;,
  {
    prompt: &#x27;A sailboat gliding across calm ocean waters at sunset&#x27;,
    duration: 5,
    ratio: &#x27;1280:720&#x27;,
    seed: 42,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/gen-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sailboat gliding across calm ocean waters at sunset&quot;,
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;1280:720&quot;,
    &quot;seed&quot;: 42
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>With Content Moderation</strong>
<p>Adjust content moderation settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A press conference with multiple speakers at podiums&quot;,
    &quot;content_moderation&quot;: {
      &quot;public_figure_threshold&quot;: &quot;low&quot;
    },
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;1280:720&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/with-content-moderation.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/75c4cb0d-20aa-4824-b1f3-32f33ab9269b.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/gen-4.5&#x27;,
  {
    prompt: &#x27;A press conference with multiple speakers at podiums&#x27;,
    content_moderation: { public_figure_threshold: &#x27;low&#x27; },
    duration: 5,
    ratio: &#x27;1280:720&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/gen-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A press conference with multiple speakers at podiums&quot;,
    &quot;content_moderation&quot;: {
      &quot;public_figure_threshold&quot;: &quot;low&quot;
    },
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;1280:720&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing what should appear in the video Minimum length: 1</td></tr><tr><td><code>image_input</code></td><td>string</td><td>HTTPS URL, Runway URI, or data URI containing an image for image-to-video</td></tr><tr><td><code>ratio</code></td><td>string</td><td>Required. Resolution/aspect ratio of the output video Default: 1280:720; Values: 1280:720, 720:1280, 1104:832, 960:960, 832:1104, 1584:672</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Required. Video duration in seconds Default: 5; Minimum: 2; Maximum: 10</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducible results Minimum: 0; Maximum: 4294967295</td></tr><tr><td><code>content_moderation</code></td><td>object</td><td>Content moderation settings</td></tr><tr><td><code>content_moderation.public_figure_threshold</code></td><td>string</td><td>Content moderation strictness for public figures Values: auto, low</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the generated video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/runwayml/gen-4.5/schema-input.json)
- [Output schema](/ai/models/runwayml/gen-4.5/schema-output.json)

