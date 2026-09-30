<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="stable-diffusion-v1-5-inpainting">stable-diffusion-v1-5-inpainting</h1>

<p><code>@cf/runwayml/stable-diffusion-v1-5-inpainting</code></p>

Stable Diffusion Inpainting is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input, with the extra capability of inpainting the pictures by using a mask.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>More information</th><td><a href="https://huggingface.co/runwayml/stable-diffusion-inpainting">Model details</a></td></tr>
<tr><th>Terms</th><td><a href="https://github.com/runwayml/stable-diffusion/blob/main/LICENSE">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0 per step</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/runwayml/stable-diffusion-v1-5-inpainting&quot;, { text_to_image: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/runwayml/stable-diffusion-v1-5-inpainting -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. A text description of the image you want to generate Minimum length: 1</td></tr><tr><td><code>negative_prompt</code></td><td>string</td><td>Text describing elements to avoid in the generated image</td></tr><tr><td><code>height</code></td><td>integer</td><td>The height of the generated image in pixels Minimum: 256; Maximum: 2048</td></tr><tr><td><code>width</code></td><td>integer</td><td>The width of the generated image in pixels Minimum: 256; Maximum: 2048</td></tr><tr><td><code>image</code></td><td>array</td><td>For use with img2img tasks. An array of integers that represent the image data constrained to 8-bit unsigned integer values</td></tr><tr><td><code>image_b64</code></td><td>string</td><td>For use with img2img tasks. A base64-encoded string of the input image</td></tr><tr><td><code>mask</code></td><td>array</td><td>An array representing An array of integers that represent mask image data for inpainting constrained to 8-bit unsigned integer values</td></tr><tr><td><code>num_steps</code></td><td>integer</td><td>The number of diffusion steps; higher values can improve quality but take longer Default: 20; Maximum: 20</td></tr><tr><td><code>strength</code></td><td>number</td><td>A value between 0 and 1 indicating how strongly to apply the transformation during img2img tasks; lower values make the output closer to the input image Default: 1</td></tr><tr><td><code>guidance</code></td><td>number</td><td>Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt Default: 7.5</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducibility of the image generation</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<p>No parameters.</p>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/stable-diffusion-v1-5-inpainting/schema-input.json)
- [Output schema](/workers-ai/models/stable-diffusion-v1-5-inpainting/schema-output.json)

