<p>Responsive design scales media elements to fit the screen they are displayed on.</p>
<p>Without it, images can overflow their container and break the layout on small screens, look blurry on high-density displays, and waste bandwidth by forcing every device to download the same oversized file.</p>
<p>You can use Images to automatically resize images for optimal display on every device. Cloudflare supports two ways to serve responsive images on request:</p>
<table>
<thead>
<tr>
<th>Approach</th>
<th>How it works</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#using-the-srcset-attribute">HTML <code>srcset</code></a></td>
<td>List multiple sizes in markup and let the browser pick the best match based on viewport size and display density.</td>
<td>Full control over which sizes are available. Works in all browsers.</td>
</tr>
<tr>
<td><a href="#using-widthauto"><code>width=auto</code></a></td>
<td>Cloudflare automatically selects the best width from a single URL — no markup changes required.</td>
<td>Simplest implementation, especially when you don't have control over HTML.</td>
</tr>
</tbody>
</table>
<h2 id="optimize-for-high-dpi-displays">Optimize for high-DPI displays</h2>
<p>A screen displays images using physical pixels (the individual dots that you see), while the browser uses CSS pixels (an abstract unit used for layout).</p>
<p>On a standard display, these map 1:1. On high-density displays (for example, Retina, 4K), each CSS pixel is rendered using multiple physical pixels — for example, 4 physical pixels on a 2x display, 9 on a 3x display.</p>
<p>This ratio — the device pixel ratio (DPR) — determines how sharp an image will appear. When you serve a 960px image on a 2x display, the browser stretches it across 1920 physical pixels, making it appear blurry.</p>
<p>To keep images sharp, you can provide a separate, higher-resolution version for high-DPI screens using the <a href="/images/optimization/features/#dpr"><code>dpr</code></a> parameter:</p>
<table style="width:100%; table-layout:fixed; text-align:center; border:none">
<tr style="border:none; background:none">
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/dpr-1.jpg" alt="dpr=1 output" style="width:100%; height:auto" />
</td>
<td style="width:50%; border:none; vertical-align:bottom">
<img src="/assets/upstream/images/images/examples/dpr-2.jpg" alt="dpr=2 output" style="width:100%; height:auto" />
</td>
</tr>
<tr style="border:none; background:none">
<td style="border:none;">
			<code>width=300,height=200,dpr=1</code>
</td>
<td style="border:none;">
			<code>width=300,height=200,dpr=2</code>
</td>
</tr>
</table>
<h2 id="use-the-srcset-attribute">Use the <code>srcset</code> attribute</h2>
<p>When you embed an image using an <code>&lt;img&gt;</code> element, you can use its <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#srcset"><code>srcset</code></a> attribute to give the browser a list of the same image at different sizes.</p>
<p>The browser evaluates screen size, pixel density, and network conditions, then selects the single best match.</p>
<p>The snippet below shows how <code>srcset</code> can be used within an <code>&lt;img&gt;</code> tag to serve one of two possible sizes, depending on the user's device pixel ratio:</p>
<pre><code class="language-html">&lt;img&#10;	src=&quot;portrait-800w.jpg&quot;&#10;	srcset=&quot;&#10;		portrait-1600.jpg 2x,&#10;	&quot;&#10;/&gt;&#10;</code></pre>
<p>Instead of pre-generating each size, use Images to point every <code>srcset</code> entry at the same source image with a different <code>width</code> parameter and pixel density descriptor (for example, <code>2x</code>). Once the browser selects the right width for the user's device pixel ratio, Cloudflare dynamically generates the resized version on request:</p>
<pre><code class="language-html">&lt;img&#10;	src=&quot;/cdn-cgi/image/fit=contain,width=960/assets/product.jpg&quot;&#10;	srcset=&quot;/cdn-cgi/image/fit=contain,width=1920/assets/product.jpg 2x&quot;&#10;/&gt;&#10;</code></pre>
<p>In the example above, the <code>src</code> attribute contains the image for 1x displays (for example, HD/1080p monitors). The <code>srcset</code> attribute adds a larger, high-DPI image for 2x displays (for example, most mobile devices, 4K desktop displays). Use high-resolution source images, as scaling a low-resolution image increases file size without improving quality.</p>
<h3 id="create-responsive-layouts">Create responsive layouts</h3>
<p>Pixel density descriptors are used when the image has a fixed CSS size (e.g. a 960px product photo) and the viewport width doesn't matter. Here, you know exactly how many CSS pixels the image will be, and you want to provide higher-resolution versions for high-DPI screens.</p>
<p>However, if the image scales with the viewport — that is, its CSS size changes based on the screen width (for example, <code>width: 100%</code>, <code>width: 50vw</code>) — then use the width descriptor (<code>w</code>) instead to provide a range of widths:</p>
<pre><code class="language-html">&lt;img&#10;	width=&quot;100%&quot;&#10;	srcset=&quot;&#10;		/cdn-cgi/image/fit=contain,width=320/assets/hero.jpg   320w,&#10;		/cdn-cgi/image/fit=contain,width=640/assets/hero.jpg   640w,&#10;		/cdn-cgi/image/fit=contain,width=960/assets/hero.jpg   960w,&#10;		/cdn-cgi/image/fit=contain,width=1280/assets/hero.jpg 1280w,&#10;		/cdn-cgi/image/fit=contain,width=2560/assets/hero.jpg 2560w&#10;	&quot;&#10;	src=&quot;/cdn-cgi/image/width=960/assets/hero.jpg&quot;&#10;/&gt;&#10;</code></pre>
<p>The <code>w</code> values tell the browser the pixel width of each option. The browser factors in both viewport width and display density to choose the best match.</p>
<h4 id="use-the-sizes-attribute">Use the <code>sizes</code> attribute</h4>
<p>By default, the browser assumes the image fills the full viewport. If the image only occupies part of the screen, then you can use <code>sizes</code> to tell the browser how wide it actually is:</p>
<pre><code class="language-html">&lt;!-- Image fills 50% of the viewport --&gt;&#10;&lt;img style=&quot;width: 50vw&quot; srcset=&quot;...&quot; sizes=&quot;50vw&quot; /&gt;&#10;</code></pre>
<p>If the image can have a different size depending on media queries or other CSS properties (for example, <code>max-width</code>), then specify all the conditions in the <code>sizes</code> attribute:</p>
<pre><code class="language-html">&lt;img&#10;	style=&quot;max-width: 640px&quot;&#10;	srcset=&quot;&#10;		/cdn-cgi/image/fit=contain,width=320/assets/hero.jpg   320w,&#10;		/cdn-cgi/image/fit=contain,width=480/assets/hero.jpg   480w,&#10;		/cdn-cgi/image/fit=contain,width=640/assets/hero.jpg   640w,&#10;		/cdn-cgi/image/fit=contain,width=1280/assets/hero.jpg 1280w&#10;	&quot;&#10;	sizes=&quot;(max-width: 640px) 100vw, 640px&quot;&#10;/&gt;&#10;</code></pre>
<p>In the example above:</p>
<ul>
<li>If the screen size is below 640px, then the image fills the entire viewport.</li>
<li>If the screen size is above 640px, then the image scales with the viewport and caps at 640px.</li>
<li>On a 2x display above 640px, the browser needs 1280 physical pixels to fill the 640px layout width, so it selects the 1280w entry.</li>
</ul>
<h2 id="use-width-auto">Use <code>width=auto</code></h2>
<p>With <code>srcset</code>, you control exactly which sizes are available, which requires updating your HTML for every image.</p>
<p>On the other hand, <code>width=auto</code> takes a different approach, where Cloudflare determines the right width for each request from a single URL:</p>
<pre><code class="language-html">/cdn-cgi/image/width=auto/assets/hero.jpg&#10;</code></pre>
<p>This is especially useful when optimizing remote images with <a href="/images/optimization/transformations/flows/">transformation flows</a>, where you can apply <code>width=auto</code> across your entire zone without modifying any markup.</p>
<p>When a request includes <code>width=auto</code>, Cloudflare determines the width based on screen size using client hints, if sent, or user-agent detection as a fallback.</p>
<h3 id="client-hints-preferred">Client hints (preferred)</h3>
<p>Browsers that support client hints (Chrome, Edge, Opera) send the viewport width in a request header. Then, Cloudflare reads this value and selects the right image size.</p>
<p>Rather than generating a unique image for every possible viewport width, Cloudflare snaps to the smallest breakpoint that is equal to or greater than the detected screen width.</p>
<p>The default breakpoints for client hints are: <code>320</code>, <code>768</code>, <code>960</code>, and <code>1200</code> pixels.</p>
<p>The following table shows the widths that Cloudflare will pick based on the default breakpoints. If the detected viewport width exceeds the largest breakpoint, the image is served at that largest breakpoint.</p>
<table>
<thead>
<tr>
<th>Detected viewport width</th>
<th>Served image width</th>
</tr>
</thead>
<tbody>
<tr>
<td>280px</td>
<td>320px</td>
</tr>
<tr>
<td>500px</td>
<td>768px</td>
</tr>
<tr>
<td>960px</td>
<td>960px</td>
</tr>
<tr>
<td>1500px</td>
<td>1200px</td>
</tr>
</tbody>
</table>
<p>You can override the default breakpoints using the <a href="/images/optimization/features/#width"><code>wbreakpoints</code></a> sub-parameter, which accepts positive integers separated by semicolons.</p>
<h4 id="enabling-client-hints">Enabling client hints</h4>
<p>Client hints give Cloudflare the most accurate information, but require opt-in from your site. Without them, <code>width=auto</code> falls back to user-agent detection.</p>
<p>You can enable client hints using one of the following methods:</p>
<p><strong>HTML <code>&lt;meta&gt;</code> tag</strong></p>
<p>Add the following in the <code>&lt;head&gt;</code> of your page before any other elements:</p>
<pre><code class="language-html">&lt;meta&#10;	http-equiv=&quot;Delegate-CH&quot;&#10;	content=&quot;sec-ch-dpr {ZONE}; sec-ch-viewport-width {ZONE}&quot;&#10;/&gt;&#10;</code></pre>
<p><strong>HTTP response headers</strong></p>
<p>Add these headers to your HTML response:</p>
<pre><code class="language-txt">critical-ch: sec-ch-viewport-width, sec-ch-dpr&#10;permissions-policy: ch-dpr=(&quot;{ZONE}&quot;), ch-viewport-width=(&quot;{ZONE}&quot;)&#10;</code></pre>
<h3 id="user-agent-detection-fallback">User-agent detection (fallback)</h3>
<p>When client hints are not available, Cloudflare classifies the device as mobile or desktop based on the user-agent string and selects the corresponding size.</p>
<p>The default sizes for user-agent detection are:</p>
<table>
<thead>
<tr>
<th>Device type</th>
<th>Default size</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mobile (<code>iPhone</code> or <code>Android</code> in user-agent)</td>
<td>768px</td>
</tr>
<tr>
<td>Desktop (all other user-agents)</td>
<td>1200px</td>
</tr>
</tbody>
</table>
<p>You can override the default sizes using the <a href="/images/optimization/features/#width"><code>wmobile</code> and <code>wdesktop</code></a> sub-parameters, which accept positive integers.</p>
