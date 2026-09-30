<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Krea logo" width="48" height="48">

<h1 id="krea-2-medium">Krea 2 Medium</h1>

<p><code>krea/krea-2-medium</code></p>

Smaller, faster, more cost-efficient. Extensive post-training makes outputs especially stable and consistent across generations. Strongest on illustration, anime, painting, and other expressive or artistic styles.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://www.krea.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.03, Per image: 0.03</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Official Krea 2 Medium example from https://docs.krea.ai/api-reference/krea/krea-2-medium.

<section class="model-example"><strong>Default</strong>
<p>Official Krea 2 Medium example from https://docs.krea.ai/api-reference/krea/krea-2-medium.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An igloo village glowing with Aurora&#x27;s colors.&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;resolution&quot;: &quot;1K&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/krea/krea-2-medium/default.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/krea/krea-2-medium/default.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;krea/krea-2-medium&#x27;,
  {
    prompt: &quot;An igloo village glowing with Aurora&#x27;s colors.&quot;,
    aspect_ratio: &#x27;1:1&#x27;,
    resolution: &#x27;1K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;krea/krea-2-medium&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An igloo village glowing with Aurora&#x27;\&#x27;&#x27;s colors.&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;resolution&quot;: &quot;1K&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/krea/krea-2-medium/default.png" alt="Default">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the image to generate.</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Required. Aspect ratio of the generated image. Values: 1:1, 4:3, 3:2, 16:9, 2.35:1, 4:5, 2:3, 9:16</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Resolution scale. Values: 1K</td></tr><tr><td><code>seed</code></td><td>['number', 'null']</td><td>Random seed for reproducible generations. Pass null or omit for a random seed.</td></tr><tr><td><code>styles</code></td><td>array</td><td>Styles (typically LoRAs) to apply to the generation.</td></tr><tr><td><code>styles[].id</code></td><td>string</td><td>Required. Style (typically LoRA) identifier.</td></tr><tr><td><code>styles[].strength</code></td><td>number</td><td>Required. Style strength, between -2 and 2. Minimum: -2; Maximum: 2</td></tr><tr><td><code>image_style_references</code></td><td>array</td><td>Reference images to drive the visual style (up to 10).</td></tr><tr><td><code>image_style_references[].url</code></td><td>string</td><td>Required. URL of the reference image (max 1024 chars).</td></tr><tr><td><code>image_style_references[].strength</code></td><td>number</td><td>Style influence (0 = no influence, 1 = maximum). Default 0.5. Default: 0.5; Minimum: 0; Maximum: 1</td></tr><tr><td><code>creativity</code></td><td>string</td><td>Prompt expansion mode. `raw` disables expansion; `low`, `medium`, `high` control strength. Does not affect the K2 Intensity, Complexity, or Movement slider LoRAs. Default: low; Values: raw, low, medium, high</td></tr><tr><td><code>intensity</code></td><td>integer</td><td>K2 Intensity slider (-100 to 100). 0 disables the slider LoRA. Default: 0; Minimum: -100; Maximum: 100</td></tr><tr><td><code>complexity</code></td><td>integer</td><td>K2 Complexity slider (-100 to 100). 0 disables the slider LoRA. Default: 0; Minimum: -100; Maximum: 100</td></tr><tr><td><code>movement</code></td><td>integer</td><td>K2 Movement slider (-100 to 100). 0 disables the slider LoRA. Default: 0; Minimum: -100; Maximum: 100</td></tr><tr><td><code>moodboards</code></td><td>array</td><td>Moodboard references (currently limited to one).</td></tr><tr><td><code>moodboards[].id</code></td><td>string</td><td>Required. Moodboard identifier.</td></tr><tr><td><code>moodboards[].strength</code></td><td>number</td><td>Moodboard influence (0 = no influence, 1 = maximum). Default 0.23. Default: 0.23; Minimum: 0; Maximum: 1</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. Presigned URL for the generated image.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/krea/krea-2-medium/schema-input.json)
- [Output schema](/ai/models/krea/krea-2-medium/schema-output.json)

