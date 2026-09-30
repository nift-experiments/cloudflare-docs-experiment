<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Pruna logo" width="48" height="48">

<h1 id="p-video-animate">P-Video-Animate</h1>

<p><code>pruna/p-video-animate</code></p>

Pruna's P-Video-Animate takes a source video and a subject reference image, then animates the referenced subject using the motion and audio from the source video.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Image-to-Video</td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.03, @720p (per second): 0.03, @1080p (per second): 0.06</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Animate a reference subject using the motion from a source video.

<section class="model-example"><strong>Motion Transfer</strong>
<p>Animate a reference subject using the motion from a source video.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;video&quot;: &quot;https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4&quot;,
    &quot;image&quot;: &quot;https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg&quot;,
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;target_fps&quot;: &quot;original&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/pruna/p-video-animate/motion-transfer.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/pruna/p-video-animate/motion-transfer.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;pruna/p-video-animate&#x27;,
  {
    video: &#x27;https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4&#x27;,
    image: &#x27;https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg&#x27;,
    resolution: &#x27;720p&#x27;,
    target_fps: &#x27;original&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;pruna/p-video-animate&quot;,
  &quot;input&quot;: {
    &quot;video&quot;: &quot;https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4&quot;,
    &quot;image&quot;: &quot;https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg&quot;,
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;target_fps&quot;: &quot;original&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. Source RGB video (.mp4) used as the motion and audio source. HTTP(S) URL or data URI.</td></tr><tr><td><code>image</code></td><td>string</td><td>Required. Reference image of the subject to animate. HTTP(S) URL or data URI.</td></tr><tr><td><code>turbo</code></td><td>boolean</td><td>Required. Turbo mode: faster generation for slightly lower quality. Default: False</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Target resolution. Default: 720p; Values: 720p, 1080p</td></tr><tr><td><code>save_audio</code></td><td>boolean</td><td>Required. Save the video with audio. Default: True</td></tr><tr><td><code>ignore_audio</code></td><td>boolean</td><td>Required. Ignore source audio during generation. Default: False</td></tr><tr><td><code>target_fps</code></td><td>string</td><td>Required. Target FPS for the working video. Default: original; Values: 24, 48, original</td></tr><tr><td><code>instruction_prompt</code></td><td>string</td><td>Required. Further instruction on how the reference subject should be animated. Default:</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducible generation. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>disable_safety_checker</code></td><td>boolean</td><td>Required. Disable safety checker for generated videos. Default: False</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. Presigned URL for the animated video.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/pruna/p-video-animate/schema-input.json)
- [Output schema](/ai/models/pruna/p-video-animate/schema-output.json)

