<p>During a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a>, each request has a random chance of routing to either version based on the specified percentages. This means the same user can be served content from a different version every time a request is made, which can cause <strong>version skew</strong> issues.</p>
<p>Version affinity solves this by deterministically assigning users to a version based on a stable identifier, so they consistently hit the same version across page loads and subrequests for the duration of the gradual deployment.</p>
<h2 id="how-it-works">How it works</h2>
<p>Set the <code>Cloudflare-Workers-Version-Key</code> header on the incoming request to your Worker:</p>
<pre><code class="language-sh">curl -s https://example.com -H &#x27;Cloudflare-Workers-Version-Key: foo&#x27;&#10;</code></pre>
<p>For a given <a href="/workers/versions-and-deployments/#deployments">deployment</a>, all requests with a version key set to <code>foo</code> will be handled by the same version of your Worker. The platform hashes the key and uses the result with the configured percentages to deterministically assign a version - you do not choose which version a key maps to.</p>
<p>As you progress a gradual deployment (for example, from 10% to 20% to 50%), users whose keys were already assigned to the new version will remain on it. Users on the old version will progressively move to the new version as the percentage increases, but will not flip back unless you roll back.</p>
<p>You can set the <code>Cloudflare-Workers-Version-Key</code> header both when making an external request from the Internet to your Worker, as well as when making a subrequest from one Worker to another Worker using a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a>.</p>
<h2 id="static-assets">Static assets</h2>
<p>Version affinity is particularly important when your Worker serves <a href="/workers/static-assets/">static assets</a> with content-hashed filenames (like <code>index-a1b2c3d4.js</code>), which is the default behavior of most modern build tools and frameworks.</p>
<p>During a gradual rollout, different versions of your application will have different asset filenames:</p>
<ul>
<li>Version A's HTML references <code>assets/index-a1b2c3d4.js</code></li>
<li>Version B's HTML references <code>assets/index-m3n4o5p6.js</code></li>
</ul>
<p>Without version affinity, a user can receive HTML from version A, but when their browser requests <code>index-a1b2c3d4.js</code>, that request may be routed to version B - which does not have that file - resulting in a 404 error and a broken page.</p>
<p>Configuring version affinity using any of the methods in <a href="#choose-a-version-key">Choose a version key</a> prevents this entirely by ensuring all requests from the same user are routed to the same version.</p>
<h2 id="choose-a-version-key">Choose a version key</h2>
<p>The right version key depends on what stable identifiers your application has available. You can set the header using a <a href="/rules/transform/request-header-modification/">Transform Rule</a> on your zone, which extracts values from the request without modifying your application code.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17374.md")
</aside>
<h3 id="authenticated-applications">Authenticated applications</h3>
<p>If your application has a user identifier in a cookie or header, this is the best option. Each user is deterministically assigned to a version and stays there across sessions, devices, and reloads.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/17375.md")
</div>
<h3 id="applications-with-sessions">Applications with sessions</h3>
<p>If your application sets a session cookie, use the session identifier. This gives consistent routing for the duration of the session. If the session expires and a new one is created, the user may be assigned to a different version.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/17376.md")
</div>
<h3 id="anonymous-or-cookieless-applications">Anonymous or cookieless applications</h3>
<p>If your application does not have any stable identifier in the request, you have two options:</p>
<p><strong>Option 1: Use the client IP address.</strong> This is the simplest approach and requires no application changes. Users behind the same NAT or VPN will be grouped together, and mobile users who switch networks may change version, but for most applications this significantly reduces version flip-flopping compared to random per-request routing.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@markup("md", "content/.markup/bodies/17377.md")
</div>
<p><strong>Option 2: Set a long-lived cookie from your Worker.</strong> On the first request (which will be randomly assigned), your Worker generates a stable identifier and sets it as a cookie. All subsequent requests use that cookie as the version key. This gives the best consistency for anonymous users, at the cost of a small amount of application code.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17378.md")
</div>
<p>Then create a Transform Rule to use this cookie as the version key:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-3">Example</h3>
@markup("md", "content/.markup/bodies/17379.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17373.md")
</aside>
<h2 id="testing">Testing</h2>
<p>You can verify that version affinity is working by sending multiple requests with the same version key and confirming they are handled by the same version:</p>
<pre><code class="language-sh">&#35; Both requests should return responses from the same version&#10;curl -s https://example.com -H &#x27;Cloudflare-Workers-Version-Key: test-user-123&#x27;&#10;curl -s https://example.com -H &#x27;Cloudflare-Workers-Version-Key: test-user-123&#x27;&#10;</code></pre>
<p>Use the <a href="/workers/runtime-apis/bindings/version-metadata/">version metadata binding</a> to include the version ID in your Worker's response during testing.</p>
<p>During gradual rollouts, monitor your Worker's analytics for increased 404 response rates, especially for asset files (<code>.js</code>, <code>.css</code>, <code>.png</code>). Use <a href="/analytics/analytics-engine/">Analytics Engine</a> or <a href="/workers/observability/logs/logpush/">Logpush</a> to track these metrics and catch version skew issues early. If you notice problems, you can <a href="/workers/versions-and-deployments/rollbacks/">roll back</a> to the previous version.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/versions-and-deployments/gradual-deployments/">Gradual deployments</a> - How percentage-based traffic splitting works</li>
<li><a href="/workers/versions-and-deployments/version-overrides/">Version overrides</a> - Send a request to a specific version by ID (for smoke testing and debugging, not for end-user routing)</li>
<li><a href="/workers/runtime-apis/bindings/version-metadata/">Version metadata binding</a> - Access version ID and tag from within your Worker</li>
</ul>
