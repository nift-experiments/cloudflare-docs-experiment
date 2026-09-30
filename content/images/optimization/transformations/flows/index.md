<div class="nb-description">
@markup("md", "content/.markup/bodies/9464.md")
</div>
<p>Flows let you automatically apply image optimization to requests on your zone.</p>
<p>Each flow pairs a set of conditional triggers (for example, image is a JPEG or PNG) with optimization parameters (for example, transcode to AVIF).</p>
<p>When an image request matches a flow, Cloudflare transparently rewrites it through the Images service and serves the optimized result.</p>
<h2 id="types-of-flows">Types of flows</h2>
<p>You can use pre-built flows to handle migrations from other image optimization services (like Fastly) or create your own custom flows.</p>
<p>A <strong>provider flow</strong> is a translation layer that maps image URLs from another image optimization service to Cloudflare. Your existing URLs — including provider-specific parameters — continue to work without any changes.</p>
<p>Currently, Cloudflare supports flows for Fastly Image Optimizer. When enabled, Cloudflare automatically translates Fastly's parameters to their Cloudflare equivalents. For example:</p>
<ul>
<li>Fastly's <code>brightness</code> parameter accepts a range from <code>-100</code> to <code>100</code>, while Cloudflare's <code>brightness</code> works as a multiplier. The value is scaled accordingly.</li>
<li>Fastly's <code>orient</code> parameter is mapped to Cloudflare's <code>flip</code> and <code>rotate</code> parameters.</li>
</ul>
<p>A <strong>custom flow</strong> lets you define your own conditions and actions for image optimization.</p>
<p>This is well-suited for situations where you want to optimize your images broadly and consistently, such as:</p>
<ul>
<li><strong>Automatic format conversion</strong> — Transcode all images to modern formats like AVIF or WebP across your entire site.</li>
<li><strong>Responsive sizing</strong> — Automatically resize images based on each user's device.</li>
<li><strong>Directory-based optimization</strong> — Enforce a consistent size for all images in a particular path, such as 100x100 for images where the path contains <code>/thumbnail</code>.</li>
</ul>
<h2 id="how-flows-work">How flows work</h2>
<p>Before setting up a flow, make sure that transformations are turned on for your zone under <strong>Images</strong> &gt; <strong>Transformations</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/images/transformations">Cloudflare dashboard</a>.</p>
<p>When an image is requested on your zone, Cloudflare checks to see whether the request matches the conditions for any of your configured flows:</p>
<ul>
<li>Flows are evaluated from top to bottom in the order that they appear in the dashboard.</li>
<li>If a request matches more than one flow, only the first matching flow will run.</li>
<li>If no flow matches, then the request passes through to your origin unmodified.</li>
<li>To control priority, you can reorder flows in the dashboard.</li>
</ul>
<p>If the request matches a flow's conditions, then Cloudflare rewrites the URL to pass through the Images service with the specified parameters:</p>
<ul>
<li>A custom flow triggers only on requests for <a href="/images/get-started/limits/">supported image extensions</a>. HTML pages, CSS files, and other non-images are never affected.</li>
<li>A provider flow evaluates requests based on provider-specific optimization parameters. For example, a Fastly provider flow triggers only when the request contains parameters like <code>?width</code>, <code>?height</code>, or <code>?fit</code>. Cloudflare will ignore any unrecognized parameters.</li>
</ul>
<p>In your request lifecycle, flows are evaluated after standard HTTP <a href="/rules/url-forwarding/">redirect rules</a>:</p>
<ul>
<li>Any existing URL rewrites or redirect rules will be applied before Images evaluates the request, which may affect matching behavior.</li>
<li>Flows include built-in loop prevention. If the request is already coming from the Images service, then the flow will not re-trigger on that subrequest.</li>
</ul>
<h2 id="set-up-a-provider-flow">Set up a provider flow</h2>
<p>Currently, Cloudflare supports flows to handle migrations from Fastly Image Optimizer.</p>
<p>To add a provider flow:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Images</strong> &gt; <strong>Transformations</strong> and select your zone.</li>
<li>Select the <strong>Automation</strong> tab, then select <strong>Add provider flow</strong>.</li>
<li>Choose <strong>Fastly</strong> as the provider.</li>
<li><strong>Save</strong> your flow.</li>
</ol>
<h2 id="set-up-a-custom-flow">Set up a custom flow</h2>
<h3 id="1-create-a-new-flow"><ol>
<li>Create a new flow</li>
</ol></h3>
<p>In the Cloudflare dashboard, go to <a href="https://dash.cloudflare.com/?to=/:account/images/transformations"><strong>Images</strong> &gt; <strong>Transformations</strong></a> and select the zone where you want to set up the custom flow.</p>
<p>Go to the <strong>Automation</strong> tab and select <strong>Add custom flow</strong> to open the side panel where you can configure your flow.</p>
<p><img src="/assets/upstream/images/images/custom-flow.png" alt="Custom flow configuration panel" /></p>
<h3 id="2-configure-the-conditions"><ol start="2">
<li>Configure the conditions</li>
</ol></h3>
<p>A custom flow is triggered when an incoming request matches all of the configured conditions in the flow:</p>
<ul>
<li><strong>File extension</strong> — Match requests for all image formats or only specific file extensions, such as JPEG, PNG, or WebP.</li>
<li><strong>URL path</strong> — Match requests where the URL path matches a specified pattern, such as <code>/images/*</code> or <code>/assets/thumbnails/*</code>.</li>
<li><strong>Query parameter</strong> — Match requests where the query string contains a specified parameter, such as <code>orient</code>.</li>
</ul>
<h3 id="3-configure-the-actions"><ol start="3">
<li>Configure the actions</li>
</ol></h3>
<p>Next, define the optimization parameters that should be applied when the flow is triggered.</p>
<p>You can apply multiple actions within a single flow. For the full list of available parameters, refer to <a href="/images/optimization/features/">Features</a>.</p>
<p>The key parameters for most use cases are:</p>
<h4 id="format-f"><code>format</code> | <code>f</code></h4>
<p>Set <code>format=auto</code> to automatically serve images in the most efficient format (e.g. AVIF, WebP) for each requesting browser.</p>
<p>If the browser doesn't support AVIF, then Cloudflare will fall back to WebP or a standard format.</p>
<p>Refer to <a href="/images/optimization/features/#format"><code>format</code></a></p>
<h4 id="quality-q"><code>quality</code> | <code>q</code></h4>
<p>Control the compression quality of the output image. Accepts either:</p>
<ul>
<li>A <strong>fixed value</strong> from <code>1</code> (low quality, small file size) to <code>100</code> (high quality, large file size).</li>
<li>A <strong>perceptual quality level</strong>: <code>high</code>, <code>medium-high</code>, <code>medium-low</code>, or <code>low</code>.</li>
</ul>
<p>Refer to <a href="/images/optimization/features/#quality"><code>quality</code></a></p>
<h4 id="slow-connection-quality-scq"><code>slow-connection-quality</code> | <code>scq</code></h4>
<p>Override <code>quality</code> when a slow connection is detected via client hints. Accepts the same fixed or perceptual values as <code>quality</code>. This serves lower-quality (and smaller) images to users on slow networks without affecting users on fast connections.</p>
<p>Refer to <a href="/images/optimization/features/#slow-connection-quality"><code>slow-connection-quality</code></a></p>
<h4 id="width-w"><code>width</code> | <code>w</code></h4>
<p>Set <a href="/images/optimization/features/#width"><code>width=auto</code></a> to automatically size images based on the requesting device.</p>
<p>Cloudflare determines the optimal width using either <a href="/images/optimization/make-responsive-images/#client-hints-preferred">client hints</a> (sent by the browser) or user-agent detection as a fallback.</p>
<p>You can fine-tune the <code>width=auto</code> behavior with the following sub-parameters:</p>
<table>
<thead>
<tr>
<th>Sub-parameter</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wbreakpoints</code></td>
<td>Override default breakpoint widths, in pixels (client hints)</td>
<td><code>320;768;960;1200</code></td>
</tr>
<tr>
<td><code>wmobile</code></td>
<td>Override default width, in pixels, for mobile devices (user-agent detection)</td>
<td><code>768</code></td>
</tr>
<tr>
<td><code>wdesktop</code></td>
<td>Override default width, in pixels, for desktop devices (user-agent detection)</td>
<td><code>1200</code></td>
</tr>
</tbody>
</table>
<p>To learn how <code>width=auto</code> works, refer to our guide on <a href="/images/optimization/make-responsive-images/">serving responsive images</a>.</p>
<h3 id="4-publish-your-flow"><ol start="4">
<li>Publish your flow</li>
</ol></h3>
<p>Select <strong>Save</strong> on the side panel to add your custom flow, then select <strong>Save</strong> on your list of flows to turn on your flow.</p>
