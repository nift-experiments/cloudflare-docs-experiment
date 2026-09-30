<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 25, 2025</time><h2 id="post-title">Launching FLUX.2 [dev] on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We've partnered with Black Forest Labs (BFL) to bring their latest FLUX.2 [dev] model to Workers AI! This model excels in generating high-fidelity images with physical world grounding, multi-language support, and digital asset creation. You can also create specific super images with granular controls like JSON prompting.</p>
<p>Read the <a href="https://bfl.ai/flux2">BFL blog</a> to learn more about the model itself. Read our <a href="https://blog.cloudflare.com/flux-2-workers-ai">Cloudflare blog</a> to see the model in action, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-dev/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>. Note, we expect to drop pricing in the next few days after iterating on the model performance.</p>
<h4 id="workers-ai-platform-specifics">Workers AI Platform specifics</h4>
<p>The model hosted on Workers AI is able to support up to 4 image inputs (512x512 per input image). Note, this image model is one of the most powerful in the catalog and is expected to be slower than the other image models we currently support. One catch to look out for is that this model takes multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form steps=25&#10;  &#45;-form width=1024&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre><code class="language-javascript">&#10;const form = new FormData();&#10;form.append(&#x27;prompt&#x27;, &#x27;a sunset with a dog&#x27;);&#10;form.append(&#x27;width&#x27;, &#x27;1024&#x27;);&#10;form.append(&#x27;height&#x27;, &#x27;1024&#x27;);&#10;&#10;//this dummy request is temporary hack&#10;//we&#x27;re pushing a change to address this soon&#10;const formRequest = new Request(&#x27;http://dummy&#x27;, {&#10;  method: &#x27;POST&#x27;,&#10;  body: form&#10;});&#10;const formStream = formRequest.body;&#10;const formContentType = formRequest.headers.get(&#x27;content-type&#x27;) || &#x27;multipart/form-data&#x27;;&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-dev&quot;, {&#10;  multipart: {&#10;    body: formStream,&#10;    contentType: formContentType&#10;  }&#10;});&#10;</code></pre>
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
<li><code>steps</code> (integer) - Number of inference steps. Higher values may improve quality but increase generation time</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
</details>
<pre><code>&#10;&#35;# Multi-Reference Images&#10;&#10;The FLUX.2 model is great at generating images based on reference images. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generate images. You would use it with the same multipart form data structure, with the input images in binary.&#10;&#10;For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.&#10;&#10;Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2` for it to work correctly. All input images must be smaller than 512x512.&#10;</code></pre>
<p>curl --request POST <br />
--url '<a href="https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT%7D/ai/run/@cf/black-forest-labs/flux-2-dev">https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev</a>' <br />
--header 'Authorization: Bearer {TOKEN}' <br />
--header 'Content-Type: multipart/form-data' <br />
--form 'prompt=take the subject of image 1 and style it like image 0' <br />
--form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png <br />
--form input_image_1=@/Users/johndoe/Desktop/me.png <br />
--form steps=25
--form width=1024
--form height=1024</p>
<pre><code>Through Workers AI Binding:&#10;</code></pre>
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
form.append('prompt', 'take the subject of image 1and style it like image 0')</p>
<p>//this dummy request is temporary hack
//we're pushing a change to address this soon
const formRequest = new Request('<a href="http://dummy">http://dummy</a>', {
method: 'POST',
body: form
});
const formStream = formRequest.body;
const formContentType = formRequest.headers.get('content-type') || 'multipart/form-data';</p>
<p>const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-dev&quot;, {
multipart: {
body: form,
contentType: &quot;multipart/form-data&quot;
}
})</p>
<pre><code>&#10;&#35;# JSON Prompting&#10;&#10;The model supports prompting in JSON to get more granular control over images. You would pass the JSON as the value of the &#x27;prompt&#x27; field in the multipart form data. See the JSON schema below on the base parameters you can pass to the model.&#10;&#10;&lt;details&gt;&#10;  &lt;summary&gt;JSON Prompting Schema&lt;/summary&gt;&#10;</code></pre>
<p>{
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;scene&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Overall scene setting or location&quot;
},
&quot;subjects&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;type&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Type of subject (e.g., desert nomad, blacksmith, DJ, falcon)&quot;
},
&quot;description&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Physical attributes, clothing, accessories&quot;
},
&quot;pose&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Action or stance&quot;
},
&quot;position&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;foreground&quot;, &quot;midground&quot;, &quot;background&quot;],
&quot;description&quot;: &quot;Depth placement in scene&quot;
}
},
&quot;required&quot;: [&quot;type&quot;, &quot;description&quot;, &quot;pose&quot;, &quot;position&quot;]
}
},
&quot;style&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Artistic rendering style (e.g., digital painting, photorealistic, pixel art, noir sci-fi, lifestyle photo, wabi-sabi photo)&quot;
},
&quot;color_palette&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: { &quot;type&quot;: &quot;string&quot; },
&quot;minItems&quot;: 3,
&quot;maxItems&quot;: 3,
&quot;description&quot;: &quot;Exactly 3 main colors for the scene (e.g., ['navy', 'neon yellow', 'magenta'])&quot;
},
&quot;lighting&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Lighting condition and direction (e.g., fog-filtered sun, moonlight with star glints, dappled sunlight)&quot;
},
&quot;mood&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Emotional atmosphere (e.g., harsh and determined, playful and modern, peaceful and dreamy)&quot;
},
&quot;background&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Background environment details&quot;
},
&quot;composition&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [
&quot;rule of thirds&quot;,
&quot;circular arrangement&quot;,
&quot;framed by foreground&quot;,
&quot;minimalist negative space&quot;,
&quot;S-curve&quot;,
&quot;vanishing point center&quot;,
&quot;dynamic off-center&quot;,
&quot;leading leads&quot;,
&quot;golden spiral&quot;,
&quot;diagonal energy&quot;,
&quot;strong verticals&quot;,
&quot;triangular arrangement&quot;
],
&quot;description&quot;: &quot;Compositional technique&quot;
},
&quot;camera&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;angle&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;eye level&quot;, &quot;low angle&quot;, &quot;slightly low&quot;, &quot;bird's-eye&quot;, &quot;worm's-eye&quot;, &quot;over-the-shoulder&quot;, &quot;isometric&quot;],
&quot;description&quot;: &quot;Camera perspective&quot;
},
&quot;distance&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;close-up&quot;, &quot;medium close-up&quot;, &quot;medium shot&quot;, &quot;medium wide&quot;, &quot;wide shot&quot;, &quot;extreme wide&quot;],
&quot;description&quot;: &quot;Framing distance&quot;
},
&quot;focus&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;deep focus&quot;, &quot;macro focus&quot;, &quot;selective focus&quot;, &quot;sharp on subject&quot;, &quot;soft background&quot;],
&quot;description&quot;: &quot;Focus type&quot;
},
&quot;lens&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;14mm&quot;, &quot;24mm&quot;, &quot;35mm&quot;, &quot;50mm&quot;, &quot;70mm&quot;, &quot;85mm&quot;],
&quot;description&quot;: &quot;Focal length (wide to telephoto)&quot;
},
&quot;f-number&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Aperture (e.g., f/2.8, the smaller the number the more blurry the background)&quot;
},
&quot;ISO&quot;: {
&quot;type&quot;: &quot;number&quot;,
&quot;description&quot;: &quot;Light sensitivity value (comfortable range between 100 &amp; 6400, lower = less sensitivity)&quot;
}
}
},
&quot;effects&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: { &quot;type&quot;: &quot;string&quot; },
&quot;description&quot;: &quot;Post-processing effects (e.g., 'lens flare small', 'subtle film grain', 'soft bloom', 'god rays', 'chromatic aberration mild')&quot;
}
},
&quot;required&quot;: [&quot;scene&quot;, &quot;subjects&quot;]
}</p>
<pre><code>&lt;/details&gt;&#10;&#10;&#35;# Other features to try&#10;&#10;&#45; The model also supports the most common latin and non-latin character languages&#10;&#45; You can prompt the model with specific hex codes like `#2ECC71`&#10;&#45; Try creating digital assets like landing pages, comic strips, infographics too!&#10;&#10;&#10;</code></pre>
<h4 id="json-prompting">JSON Prompting</h4><h4 id="other-features-to-try">Other features to try</h4></div></article></div>
