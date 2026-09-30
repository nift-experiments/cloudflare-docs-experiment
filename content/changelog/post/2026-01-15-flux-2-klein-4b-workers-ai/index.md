<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 15, 2026</time><h2 id="post-title">Launching FLUX.2 [klein] 4B on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We've partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 4B model to Workers AI! This distilled model offers faster generation and cost-effective pricing, while maintaining great output quality. With a fixed 4-step inference process, Klein 4B is ideal for rapid prototyping and real-time applications where speed matters.</p>
<p>Read the <a href="https://bfl.ai/blog">BFL blog</a> to learn more about the model itself, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-klein-4b/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="workers-ai-platform-specifics">Workers AI Platform specifics</h4>
<p>The model hosted on Workers AI is optimized for speed with a <strong>fixed 4-step inference process</strong> and supports up to 4 image inputs. Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev], this image model uses multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre><code class="language-javascript">const form = new FormData();&#10;form.append(&quot;prompt&quot;, &quot;a sunset with a dog&quot;);&#10;form.append(&quot;width&quot;, &quot;1024&quot;);&#10;form.append(&quot;height&quot;, &quot;1024&quot;);&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, {&#10;	multipart: {&#10;		body: formStream,&#10;		contentType: formContentType,&#10;	},&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
<p><strong>Note:</strong> Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted.</p>
</details>
<pre><code>&#10;&#35;# Multi-Reference Images&#10;&#10;The FLUX.2 klein-4b model supports generating images based on reference images, just like FLUX.2 [dev]. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.&#10;&#10;For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.&#10;&#10;Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2`, `input_image_3` for it to work correctly. All input images must be smaller than 512x512.&#10;</code></pre>
<p>curl --request POST <br />
--url '<a href="https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT%7D/ai/run/@cf/black-forest-labs/flux-2-klein-4b">https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b</a>' <br />
--header 'Authorization: Bearer {TOKEN}' <br />
--header 'Content-Type: multipart/form-data' <br />
--form 'prompt=take the subject of image 1 and style it like image 0' <br />
--form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png <br />
--form input_image_1=@/Users/johndoe/Desktop/me.png <br />
--form width=1024 <br />
--form height=1024</p>
<pre><code>&#10;Through Workers AI Binding:&#10;</code></pre>
<p>//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
const reader = stream.getReader();
const chunks = [];</p>
<p>while (true) {
const { done, value } = await reader.read();
if (done) break;
chunks.push(value);
}</p>
<p>return new Blob(chunks, { type: contentType });
}</p>
<p>const image0 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const image1 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const form = new FormData();</p>
<p>const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);
const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1 and style it like image 0')</p>
<p>// FormData doesn't expose its serialized body or boundary. Passing it to a
// Request (or Response) constructor serializes it and generates the Content-Type
// header with the boundary, which is required for the server to parse the multipart fields.
const formResponse = new Response(form);
const formStream = formResponse.body;
const formContentType = formResponse.headers.get('content-type');</p>
<p>const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, {
multipart: {
body: formStream,
contentType: formContentType
}
})</p>
<pre><code></code></pre>
</div></article></div>
