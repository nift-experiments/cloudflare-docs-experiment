<p>Use <a href="/workers/">Workers</a> to draw text, watermarks, and logos over other images. Overlays support transparency, positioning, and compositing modes.</p>
<p>You can draw overlays in a Worker using two approaches:</p>
<ul>
<li><strong><a href="#draw-with-cfimage"><code>cf.image</code> on a fetch subrequest</a></strong> — Add a <code>draw</code> array to the image options to overlay with text or images. Overlay images must be accessible via URL. Use this approach when optimizing through the <a href="/images/optimization/features/#url-interface">URL interface</a>.</li>
<li><strong><a href="#draw-with-the-images-binding">Images binding</a></strong> — Chain <code>.draw()</code> calls to overlay images from any source, including <a href="/images/storage/binding/">hosted images</a> or <a href="/r2/">R2</a>, or to overlay text.</li>
</ul>
<h2 id="draw-with-cf-image">Draw with <code>cf.image</code></h2>
<p>To draw overlays on a <a href="/images/optimization/transformations/transform-via-workers/"><code>fetch()</code> subrequest</a> in Workers, you can add a <code>draw</code> array to your <code>cf.image</code> options.</p>
<p>Each entry draws either an image or text:</p>
<ul>
<li><strong>Image</strong> — Set <code>url</code> to the absolute URL of the image. Apply <a href="/images/optimization/features/">optimization parameters</a> like <a href="/images/optimization/features/#width--w"><code>width</code></a>, <a href="/images/optimization/features/#height--h"><code>height</code></a>, <a href="/images/optimization/features/#fit"><code>fit</code></a>, <a href="/images/optimization/features/#blur"><code>blur</code></a>, and <a href="/images/optimization/features/#rotate"><code>rotate</code></a>.</li>
<li><strong>Text</strong> — Set <code>text</code> to the string to render. Style it with the same <code>font</code>, <code>color</code>, and <code>size</code> options as the binding <code>.text()</code> method. Refer to <a href="/images/optimization/binding/#textcontent-options"><code>.text()</code></a> for the available options, defaults, and limits.</li>
</ul>
<p>Overlays are drawn in the order they appear — the last entry is the topmost layer.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request) {&#10;		const imageURL = &quot;https://example.com/image.png&quot;;&#10;&#10;		return fetch(imageURL, {&#10;			cf: {&#10;				image: {&#10;					width: 800,&#10;					height: 600,&#10;					draw: [&#10;						{&#10;							url: &quot;https://example.com/branding/logo.png&quot;,&#10;							bottom: 5,&#10;							right: 5,&#10;							fit: &quot;contain&quot;,&#10;							width: 100,&#10;							height: 50,&#10;							opacity: 0.8,&#10;						},&#10;						{&#10;							text: &quot;HELLO&quot;,&#10;							font: { url: &quot;https://example.com/font.otf&quot; },&#10;							color: &quot;#223E49&quot;,&#10;							size: 96,&#10;							top: 40,&#10;						},&#10;					],&#10;				},&#10;			},&#10;		});&#10;	},&#10;};&#10;</code></pre>
<h2 id="draw-with-the-images-binding">Draw with the Images binding</h2>
<p>The <a href="/images/optimization/binding/">Images binding</a> uses a chainable <code>.draw()</code> method to draw an overlay on top of an image. You can chain multiple <code>.draw()</code> calls for multiple overlays.</p>
<p>Pass the overlay as the first argument, then the draw options as the second. The overlay can be an image or text:</p>
<ul>
<li><strong>Image</strong> — Pass the image bytes or an <code>.input()</code> chain. To apply <a href="/images/optimization/features/">optimization parameters</a> to the overlay image, pass an <code>.input()</code> chain with <code>.transform()</code> as the first argument.</li>
<li><strong>Text</strong> — Pass a handle created with <code>.text()</code>. Set the font, color, and size in the <code>.text()</code> <code>options</code> argument. Refer to <a href="/images/optimization/binding/#textcontent-options"><code>.text()</code></a> for the available options, defaults, and limits.</li>
</ul>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const img = await fetch(&quot;https://example.com/base.png&quot;);&#10;		const watermark = await fetch(&quot;https://example.com/overlay.png&quot;);&#10;&#10;		const response = (&#10;			await env.IMAGES.input(img.body)&#10;				.draw(env.IMAGES.input(watermark.body).transform({ width: 100 }), {&#10;					bottom: 10,&#10;					right: 10,&#10;					opacity: 0.5,&#10;				})&#10;				.draw(&#10;					env.IMAGES.text(&quot;HELLO&quot;, {&#10;						font: { url: &quot;https://example.com/font.otf&quot; },&#10;						color: &quot;#223E49&quot;,&#10;						size: 96,&#10;					}),&#10;					{ top: 40 },&#10;				)&#10;				.output({ format: &quot;image/avif&quot; })&#10;		).response();&#10;&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<h2 id="options">Options</h2>
<p>The dimensions of the output image are always determined by the base image. The overlay is then drawn onto the base image's canvas.</p>
<p>The following draw-specific options can be used for positioning and blending.</p>
<h3 id="url"><code>url</code></h3>
<p>Absolute URL of the overlay image when drawing with <code>cf.image</code>. <code>url</code> applies only to image overlays. To draw text, create the overlay with a <code>text</code> entry in the <code>draw</code> array instead.</p>
<p>Accepts any <a href="/images/get-started/limits/">supported image format</a>. For watermarks or non-rectangular overlays, use PNG or WebP images.</p>
<p>When drawing an image overlay with the binding, the overlay is passed as image bytes or an <code>.input()</code> chain instead of a URL. Refer to <a href="#draw-with-the-images-binding">Draw with the Images binding</a>.</p>
<h3 id="text"><code>text</code></h3>
<p>Renders a text string as an overlay when drawing with <code>cf.image</code>. When drawing with the Images binding, create the text overlay with <code>.text()</code> instead.</p>
<p>Style the text with <code>font</code>, <code>color</code>, and <code>size</code> options. These apply to both <code>cf.image</code> text entries and the binding <code>.text()</code> method. Refer to <a href="/images/optimization/binding/#textcontent-options"><code>.text()</code></a> for the available options, defaults, and limits.</p>
<h3 id="width-and-height"><code>width</code> and <code>height</code></h3>
<p>Sets the maximum dimensions of the overlay image when drawing with <code>cf.image</code>. These options apply only to image overlays. The dimensions of a text overlay are determined by its text string and styling.</p>
<p>Accepts an integer (pixels) or a decimal between <code>0</code> and <code>1</code> representing a fraction of the base image's dimension. For example, <code>height:0.25</code> sets the overlay height to 25% of the height of the base image.</p>
<p>Use <a href="/images/optimization/features/#fit"><code>fit</code></a> and <a href="/images/optimization/features/#gravity--g"><code>gravity</code></a> to control how the overlay image is resized and cropped.</p>
<p>When drawing with the Images binding, the dimensions of the overlay image can be set using the <code>.transform()</code> method.</p>
<h3 id="repeat"><code>repeat</code></h3>
<p>Determines whether to tile the overlay across the image.</p>
<p>Accepts the following values:</p>
<ul>
<li><code>true</code> — Tiles the overlay to cover the entire area. This is useful for watermarks.</li>
<li><code>x</code> — Tiles the overlay horizontally only.</li>
<li><code>y</code> — Tiles the overlay vertically only.</li>
</ul>
<h3 id="top-left-bottom-right"><code>top</code>, <code>left</code>, <code>bottom</code>, <code>right</code></h3>
<p>Sets the position of the overlay as an offset, in pixels, to the specified edge. <code>0</code> aligns the overlay flush to the edge. If no position is specified, then the overlay is centered.</p>
<p>For example, <code>{ bottom: 0, right: 10 }</code> places the overlay at the bottom-right corner, 10 pixels inward from the right edge.</p>
<p>Setting both <code>left</code> and <code>right</code>, or both <code>top</code> and <code>bottom</code> returns an error.</p>
<h3 id="opacity"><code>opacity</code></h3>
<p>Sets the opacity of the overlay. Accepts a decimal value between <code>0.0</code> (fully transparent) and <code>1.0</code> (fully opaque). For example, <code>opacity: 0.5</code> makes the overlay semitransparent.</p>
<h3 id="composite"><code>composite</code></h3>
<p>Controls how the overlay is blended with the base image using <a href="https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feComposite">Porter-Duff compositing operations</a>. The default is <code>over</code>.</p>
<p>The composite mode only affects the area within the overlay's bounding box. The base image is always preserved outside of this area.</p>
<p>Accepts the following values:</p>
<h4 id="over"><code>over</code></h4>
<p>Draws the overlay on top of the base image. This is the default <code>composite</code> behavior.</p>
<p>The overlay covers the base where they overlap. Both images are visible where they do not overlap.</p>
<img src="/assets/upstream/images/images/examples/composite/over.png" alt="composite=over output" style="max-width:300px" />
<h4 id="in"><code>in</code></h4>
<p>Shows the overlay only where the base image is opaque. If the overlay has transparent pixels that overlap with the base image, then those areas of the base image will also become transparent.</p>
<img src="/assets/upstream/images/images/examples/composite/in.png" alt="composite=in output" style="max-width:300px" />
<h4 id="atop"><code>atop</code></h4>
<p>Draws the overlay on top of the base image, but only where the base image is opaque. This will clip the overlay to the shape of the base image.</p>
<p>If the overlay has transparent pixels that overlap with the base image, then the base image remains visible (unlike <code>in</code>).</p>
<img src="/assets/upstream/images/images/examples/composite/atop.png" alt="composite=atop output" style="max-width:300px" />
<h4 id="out"><code>out</code></h4>
<p>Shows the overlay only where the base image is transparent. Within the overlay's bounding box, opaque areas of the base image will become transparent.</p>
<img src="/assets/upstream/images/images/examples/composite/out.png" alt="composite=out output" style="max-width:300px" />
<h4 id="xor"><code>xor</code></h4>
<p>Shows the areas of each image where the other is transparent. Overlapping opaque areas will become transparent. This can be used to create <a href="/images/optimization/draw-overlays/#rounded-corners">rounded corners</a> or custom shapes.</p>
<img src="/assets/upstream/images/images/examples/composite/xor.png" alt="composite=xor output" style="max-width:300px" />
<h4 id="lighter"><code>lighter</code></h4>
<p>Adds the color values of both images, which makes the overlapping areas brighter.</p>
<img src="/assets/upstream/images/images/examples/composite/lighter.png" alt="composite=lighter output" style="max-width:300px" />
<h2 id="examples">Examples</h2>
<h3 id="watermark">Watermark</h3>
<p>Tile a semitransparent watermark across the entire image using <code>cf.image</code>.</p>
<pre><code class="language-js">fetch(imageURL, {&#10;	cf: {&#10;		image: {&#10;			draw: [&#10;				{&#10;					url: &quot;https://example.com/watermark.png&quot;,&#10;					repeat: true,&#10;					opacity: 0.2,&#10;				},&#10;			],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h3 id="logo-in-the-corner">Logo in the corner</h3>
<p>Position a logo at the bottom-right corner using <code>cf.image</code>.</p>
<pre><code class="language-js">fetch(imageURL, {&#10;	cf: {&#10;		image: {&#10;			draw: [&#10;				{&#10;					url: &quot;https://example.com/logo.png&quot;,&#10;					bottom: 5,&#10;					right: 5,&#10;				},&#10;			],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h3 id="multiple-overlays">Multiple overlays</h3>
<p>Combine multiple overlays in one request using <code>cf.image</code>. They are drawn in order — the last entry is the topmost layer.</p>
<pre><code class="language-js">fetch(imageURL, {&#10;	cf: {&#10;		image: {&#10;			draw: [&#10;				{&#10;					url: &quot;https://example.com/watermark.png&quot;,&#10;					repeat: true,&#10;					opacity: 0.2,&#10;				},&#10;				{ url: &quot;https://example.com/play-button.png&quot; },&#10;				{ url: &quot;https://example.com/logo.png&quot;, bottom: 5, right: 5 },&#10;			],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h3 id="rounded-corners">Rounded corners</h3>
<p>Cut rounded corners from an image. A corner mask is drawn at each corner and rotated to match the position. <code>xor</code> removes the overlapping pixels.</p>
<p>The example below shows how this can be done using the <a href="/images/optimization/binding/">Images binding</a>.</p>
<pre><code class="language-ts">const image = await fetch(&quot;https://example.com/photo.png&quot;);&#10;const mask = await fetch(&quot;https://example.com/corner-mask.png&quot;);&#10;&#10;let [topLeft, topRight] = mask.body.tee();&#10;let bottomLeft, bottomRight;&#10;[topLeft, bottomLeft] = topLeft.tee();&#10;[topLeft, bottomRight] = topLeft.tee();&#10;&#10;const output = await env.IMAGES.input(image.body)&#10;	.draw(env.IMAGES.input(topLeft).transform({ rotate: 0 }), {&#10;		left: 0,&#10;		top: 0,&#10;		composite: &quot;xor&quot;,&#10;	})&#10;	.draw(env.IMAGES.input(topRight).transform({ rotate: 90 }), {&#10;		right: 0,&#10;		top: 0,&#10;		composite: &quot;xor&quot;,&#10;	})&#10;	.draw(env.IMAGES.input(bottomRight).transform({ rotate: 180 }), {&#10;		bottom: 0,&#10;		right: 0,&#10;		composite: &quot;xor&quot;,&#10;	})&#10;	.draw(env.IMAGES.input(bottomLeft).transform({ rotate: 270 }), {&#10;		bottom: 0,&#10;		left: 0,&#10;		composite: &quot;xor&quot;,&#10;	})&#10;	.output({ format: &quot;image/png&quot; });&#10;&#10;return output.response();&#10;</code></pre>
