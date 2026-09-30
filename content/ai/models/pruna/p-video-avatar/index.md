<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Pruna logo" width="48" height="48">

<h1 id="p-video-avatar">P-Video-Avatar</h1>

<p><code>pruna/p-video-avatar</code></p>

Pruna's P-Video-Avatar generates talking-head videos from a single portrait image driven by a text script or audio file, with multiple voices, languages, and output resolutions.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Image-to-Video</td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.025, @720p (per second): 0.025, @1080p (per second): 0.045</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a talking-head video from a portrait and a short voice script.

<section class="model-example"><strong>Product Demo Greeting</strong>
<p>Generate a talking-head video from a portrait and a short voice script.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg&quot;,
    &quot;voice_script&quot;: &quot;Hello, welcome to our product demo!&quot;,
    &quot;voice&quot;: &quot;Zephyr (Female)&quot;,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/pruna/p-video-avatar/product-demo-greeting.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/pruna/p-video-avatar/product-demo-greeting.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pruna/p-video-avatar&#x27;,
  {
    image: &#x27;https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg&#x27;,
    voice_script: &#x27;Hello, welcome to our product demo!&#x27;,
    voice: &#x27;Zephyr (Female)&#x27;,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pruna/p-video-avatar&quot;,
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg&quot;,
    &quot;voice_script&quot;: &quot;Hello, welcome to our product demo!&quot;,
    &quot;voice&quot;: &quot;Zephyr (Female)&quot;,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. Input portrait image (first frame). HTTP(S) URL or data URI. Supports jpg, jpeg, png, webp.</td></tr><tr><td><code>audio</code></td><td>string</td><td>URL of uploaded audio to drive speech. HTTP(S) URL or data URI. If both audio and voice_script are provided, audio takes priority.</td></tr><tr><td><code>voice</code></td><td>string</td><td>Required. Voice for generated speech. Default: Zephyr (Female); Values: Zephyr (Female), Puck (Male), Charon (Male), Kore (Female), Fenrir (Male), Leda (Female), Orus (Male), Aoede (Female), Callirrhoe (Female), Autonoe (Female), Enceladus (Male), Iapetus (Male), Umbriel (Male), Algenib (Male), Despina (Female), Erinome (Female), Laomedeia (Female), Achernar (Female), Algieba (Male), Schedar (Male), Gacrux (Female), Pulcherrima (Female), Achird (Male), Zubenelgenubi (Male), Vindemiatrix (Female), Sadachbia (Male), Sadaltager (Male), Sulafat (Female), Alnilam (Male), Rasalgethi (Male)</td></tr><tr><td><code>voice_script</code></td><td>string</td><td>Required. Script for the person to say when no audio is uploaded. Default:</td></tr><tr><td><code>voice_language</code></td><td>string</td><td>Required. Output language. Default: English (US); Values: English (US), English (UK), Spanish, French, German, Italian, Portuguese (Brazil), Japanese, Korean, Hindi</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Resolution of the video. Default: 720p; Values: 720p, 1080p</td></tr><tr><td><code>video_prompt</code></td><td>string</td><td>Required. Optional prompt for the video. Default: The person is talking.</td></tr><tr><td><code>voice_prompt</code></td><td>string</td><td>Required. Optional speaking style, tone, pacing or emotion instructions. Default: Say the following.</td></tr><tr><td><code>negative_prompt</code></td><td>string</td><td>Required. Mention what you do NOT want in the video. Disabled if empty. Default:</td></tr><tr><td><code>strength_negative_prompt</code></td><td>number</td><td>Required. Strength of the negative prompt (0-4). Default: 0.5; Minimum: 0; Maximum: 4</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducible generation. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>disable_safety_filter</code></td><td>boolean</td><td>Required. Disable safety filter for prompts and input image. Default: True</td></tr><tr><td><code>disable_prompt_upsampling</code></td><td>boolean</td><td>Required. When true, skip the prompt upsampler and pass the raw user prompt. Default: False</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. Presigned URL for the generated avatar video.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/pruna/p-video-avatar/schema-input.json)
- [Output schema](/ai/models/pruna/p-video-avatar/schema-output.json)

