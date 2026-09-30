<div class="nb-description">
@markup("md", "content/.markup/bodies/9462.md")
</div>
<p>When you ship applications on Cloudflare, you can use Images to automatically optimize and cache your images from any origin.</p>
<p>Our image optimization pipeline provides a rich set of <a href="/images/optimization/features">features</a> that can be applied across entire media libraries to compress images at scale, transcode files into efficient formats for delivery, and resize and crop images for different use cases and devices.</p>
<h2 id="how-it-works">How it works</h2>
<p>You can request transformations by using a specially-formatted URL to serve images on your Cloudflare zone or through Workers.</p>
<p>To serve transformations on your zone, you must first enable the feature:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/?to=/:account/images/transformations">Cloudflare dashboard</a>, go to <strong>Images</strong> &gt; <strong>Transformations</strong>.</li>
<li>Select the zone where you want to serve transformations.</li>
<li>Enable <strong>transformations</strong> on your zone.</li>
</ol>
<p>When the browser requests a transformed image, Cloudflare checks the edge cache for a previously optimized version with the same parameters:</p>
<p><strong>On a cache hit</strong> — Cloudflare serves the optimized image directly from the edge without contacting the origin or re-applying the optimization parameters.</p>
<p><strong>On a cache miss</strong> — Cloudflare fetches the original image from the source origin, applies the requested parameters (e.g. <code>format</code>, <code>width</code>, <code>quality</code>), caches the transformed result, and serves it to the browser. The original image is also cached to speed up future transformations of the same source.</p>
<p>Each unique combination of source image and parameters is cached and billed separately. The first request for each unique version within a calendar month is billed as one <a href="/images/optimization/features">unique transformation</a>, regardless of cache status. Subsequent requests for this transformation do not incur billable usage within the same calendar month.</p>
<h2 id="configure-your-zone">Configure your zone</h2>
<p>After enabling transformations on your zone, you can configure how Cloudflare handles transformation requests:</p>
<ul>
<li><strong><a href="/images/optimization/transformations/sources">Define source origins</a></strong> — Specify which origins Cloudflare can pull source images from. By default, Cloudflare only accepts source images from the same zone where transformations are served.</li>
<li><strong><a href="/images/optimization/transformations/flows">Create transformation flows</a></strong> — Set up automated rules that apply image optimization to matching requests without requiring URL changes or custom code.</li>
<li><strong><a href="/images/optimization/transformations/control-origin-access">Control origin access</a></strong> — Use Workers to add custom logic for validating and controlling access to source images.</li>
<li><strong><a href="/images/optimization/transformations/rewrite-rules">Set up rewrite rules</a></strong> — Use Transform Rules to rewrite image URLs and serve transformations from custom paths.</li>
</ul>
