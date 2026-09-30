<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="lucid-origin">lucid-origin</h1>

<p><code>@cf/leonardo/lucid-origin</code></p>

Lucid Origin from Leonardo.AI is their most adaptable and prompt-responsive model to date. Whether you're generating images with sharp graphic design, stunning full-HD renders, or highly specific creative direction, it adheres closely to your prompts, renders text with accuracy, and supports a wide array of visual styles and aesthetics – from stylized concept art to crisp product mockups.


<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://leonardo.ai/terms-of-service/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.007 per 512 by 512 tile, USD 0.000132 per step</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/leonardo/lucid-origin&quot;, { text_to_image: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/leonardo/lucid-origin -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. A text description of the image you want to generate. Minimum length: 1</td></tr><tr><td><code>guidance</code></td><td>number</td><td>Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt Default: 4.5; Minimum: 0; Maximum: 10</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducibility of the image generation Minimum: 0</td></tr><tr><td><code>height</code></td><td>integer</td><td>The height of the generated image in pixels Default: 1120; Minimum: 0; Maximum: 2500</td></tr><tr><td><code>width</code></td><td>integer</td><td>The width of the generated image in pixels Default: 1120; Minimum: 0; Maximum: 2500</td></tr><tr><td><code>num_steps</code></td><td>integer</td><td>The number of diffusion steps; higher values can improve quality but take longer Minimum: 1; Maximum: 40</td></tr><tr><td><code>steps</code></td><td>integer</td><td>The number of diffusion steps; higher values can improve quality but take longer Minimum: 1; Maximum: 40</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>The generated image in Base64 format.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/lucid-origin/schema-input.json)
- [Output schema](/workers-ai/models/lucid-origin/schema-output.json)

