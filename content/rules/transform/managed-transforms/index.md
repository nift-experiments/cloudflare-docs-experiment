<p>Managed Transforms allow you to perform common adjustments to HTTP request and response headers with pre-built, one-step configurations. The available adjustments include:</p>
<ul>
<li>Add bot protection request headers.</li>
<li>Remove or add headers related to the visitor's IP address.</li>
<li>Add request header when Cloudflare detects <a href="/waf/detections/leaked-credentials/">leaked credentials</a>.</li>
<li>Add security-related response headers.</li>
<li>Remove <code>X-Powered-By</code> response headers.</li>
</ul>
<p>For a complete list, refer to <a href="/rules/transform/managed-transforms/reference/">Available Managed Transforms</a>.</p>
<p>When you enable a Managed Transform, Cloudflare internally deploys one or more Transform Rules to handle the common configuration you selected. These generated rules will not count against the <a href="/rules/transform/#availability">maximum number of Transform Rules</a> available in your Cloudflare plan.</p>
<p>Enabled Managed Transforms will apply to all inbound requests for the <a href="/fundamentals/concepts/accounts-and-zones/#zones">zone</a> (domain or subdomain added to Cloudflare).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13152.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>For dashboard, API, and Terraform instructions, refer to <a href="/rules/transform/managed-transforms/configure/">Configure Managed Transforms</a>.</p>
