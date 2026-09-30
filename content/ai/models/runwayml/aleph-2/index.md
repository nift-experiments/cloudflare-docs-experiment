<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Runwayml logo" width="48" height="48">

<h1 id="runwayml-aleph-2">RunwayML Aleph 2</h1>

<p><code>runwayml/aleph-2</code></p>

RunwayML's video editing model. Edit one frame to update your whole video, make changes across multiple shots, and work with up to 30 seconds of video. Supports keyframe-guided editing for precise control over specific moments in the clip.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://runwayml.com/terms-of-use">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.336</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Apply a text-only edit to an existing video

<section class="model-example"><strong>Simple Video Edit</strong>
<p>Apply a text-only edit to an existing video</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Transform the scene into a golden-hour sunset with warm lighting&quot;,
    &quot;video_uri&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/7449093b-e574-41a5-8308-05e4692fa652.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/7449093b-e574-41a5-8308-05e4692fa652.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/aleph-2&#x27;,
  {
    prompt: &#x27;Transform the scene into a golden-hour sunset with warm lighting&#x27;,
    video_uri: &#x27;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/aleph-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Transform the scene into a golden-hour sunset with warm lighting&quot;,
    &quot;video_uri&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Keyframe-Guided Edit</strong>
<p>Edit a video using a reference image anchored to the first frame of the output</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Edit the video to match the provided reference frame&quot;,
    &quot;video_uri&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/nature-close-up.mp4&quot;,
    &quot;prompt_images&quot;: [
      {
        &quot;uri&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg&quot;,
        &quot;position&quot;: &quot;first&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/cd7388fe-09d6-4b16-afc5-24bb315eaf14.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/cd7388fe-09d6-4b16-afc5-24bb315eaf14.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/aleph-2&#x27;,
  {
    prompt: &#x27;Edit the video to match the provided reference frame&#x27;,
    video_uri: &#x27;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/nature-close-up.mp4&#x27;,
    prompt_images: [
      {
        uri: &#x27;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg&#x27;,
        position: &#x27;first&#x27;,
      },
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/aleph-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Edit the video to match the provided reference frame&quot;,
    &quot;video_uri&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/nature-close-up.mp4&quot;,
    &quot;prompt_images&quot;: [
      {
        &quot;uri&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg&quot;,
        &quot;position&quot;: &quot;first&quot;
      }
    ]
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Timed Keyframe Edit</strong>
<p>Place a guidance image at a specific timestamp within the input video using keyframes[].seconds</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Change the background to a futuristic cityscape at night&quot;,
    &quot;video_uri&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/simple-text-to-video.mp4&quot;,
    &quot;keyframes&quot;: [
      {
        &quot;uri&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg&quot;,
        &quot;seconds&quot;: 2
      }
    ]
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/a7e054fa-1cf2-4265-a35c-518b8c4d6a1a.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/a7e054fa-1cf2-4265-a35c-518b8c4d6a1a.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/aleph-2&#x27;,
  {
    prompt: &#x27;Change the background to a futuristic cityscape at night&#x27;,
    video_uri: &#x27;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/simple-text-to-video.mp4&#x27;,
    keyframes: [
      {
        uri: &#x27;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg&#x27;,
        seconds: 2.0,
      },
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/aleph-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Change the background to a futuristic cityscape at night&quot;,
    &quot;video_uri&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/simple-text-to-video.mp4&quot;,
    &quot;keyframes&quot;: [
      {
        &quot;uri&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg&quot;,
        &quot;seconds&quot;: 2.0
      }
    ]
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Content Moderation Override</strong>
<p>Edit a video featuring public figures with relaxed content moderation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Make the background a dramatic stormy sky&quot;,
    &quot;video_uri&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4&quot;,
    &quot;content_moderation&quot;: {
      &quot;public_figure_threshold&quot;: &quot;low&quot;
    }
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/ea5b1ccd-3dd6-43c3-86e3-5ed720849e92.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://dnznrvs05pmza.cloudfront.net/ea5b1ccd-3dd6-43c3-86e3-5ed720849e92.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;runwayml/aleph-2&#x27;,
  {
    prompt: &#x27;Make the background a dramatic stormy sky&#x27;,
    video_uri: &#x27;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4&#x27;,
    content_moderation: {
      public_figure_threshold: &#x27;low&#x27;,
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;runwayml/aleph-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Make the background a dramatic stormy sky&quot;,
    &quot;video_uri&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4&quot;,
    &quot;content_moderation&quot;: {
      &quot;public_figure_threshold&quot;: &quot;low&quot;
    }
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the edit to apply to the input video Minimum length: 1</td></tr><tr><td><code>video_uri</code></td><td>string</td><td>Required. HTTPS URL, Runway URI, or data URI of the source video to edit (≤30 seconds)</td></tr><tr><td><code>keyframes</code></td><td>array</td><td>Timed guidance images placed at specific points in the input video. Each entry has a uri and either seconds (absolute timestamp) or at (fractional position). Up to 5.</td></tr><tr><td><code>keyframes[].uri</code></td><td>string</td><td>Required. HTTPS URL, Runway URI, or data URI of the guidance image</td></tr><tr><td><code>keyframes[].seconds</code></td><td>number</td><td>Required. Absolute timestamp in seconds from the start of the input video Minimum: 0; Maximum: 30</td></tr><tr><td><code>keyframes[].uri</code></td><td>string</td><td>Required. HTTPS URL, Runway URI, or data URI of the guidance image</td></tr><tr><td><code>keyframes[].at</code></td><td>number</td><td>Required. Position as a fraction [0.0, 1.0] of the input video duration Minimum: 0; Maximum: 1</td></tr><tr><td><code>prompt_images</code></td><td>array</td><td>Image keyframes for guiding the edit at specific points in the output video. Up to 5.</td></tr><tr><td><code>prompt_images[].uri</code></td><td>string</td><td>Required. HTTPS URL, Runway URI, or data URI of the keyframe image</td></tr><tr><td><code>prompt_images[].position</code></td><td>string or object</td><td>Required. Where in the output video this image applies: "first", "last", { type: "timestamp", timestampSeconds }, or { type: "position", positionPercentage }</td></tr><tr><td><code>prompt_images[].position.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>prompt_images[].position.timestampSeconds</code></td><td>number</td><td>Required. Absolute timestamp in seconds from the start of the output video Minimum: 0</td></tr><tr><td><code>prompt_images[].position.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>prompt_images[].position.positionPercentage</code></td><td>number</td><td>Required. Position as a fraction [0.0, 1.0] of the total video duration Minimum: 0; Maximum: 1</td></tr><tr><td><code>prompt_images[].position.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>prompt_images[].position.timestampSeconds</code></td><td>number</td><td>Required. Absolute timestamp in seconds from the start of the output video Minimum: 0</td></tr><tr><td><code>prompt_images[].position.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>prompt_images[].position.positionPercentage</code></td><td>number</td><td>Required. Position as a fraction [0.0, 1.0] of the total video duration Minimum: 0; Maximum: 1</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducible results Minimum: 0; Maximum: 4294967295</td></tr><tr><td><code>content_moderation</code></td><td>object</td><td>Settings that affect the behavior of the content moderation system</td></tr><tr><td><code>content_moderation.public_figure_threshold</code></td><td>string</td><td>When set to "low", content moderation is less strict about recognizable public figures Values: auto, low</td></tr><tr><td><code>duration</code></td><td>number</td><td>Duration of the source video in seconds. Used for billing only — not sent to RunwayML. Provide this so the gateway can compute per-second video cost accurately.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the edited video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/runwayml/aleph-2/schema-input.json)
- [Output schema](/ai/models/runwayml/aleph-2/schema-output.json)

