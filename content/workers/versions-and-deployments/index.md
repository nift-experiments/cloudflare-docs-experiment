<p>Every time you change your Worker's code or configuration, Workers creates a <strong>version</strong>. A <strong>deployment</strong> determines which version(s) are actively serving traffic.</p>
<p><img src="/assets/upstream/images/workers/platform/versions-and-deployments/versions-and-deployments.png" alt="Versions and Deployments" /></p>
<h2 id="versions">Versions</h2>
<p>A version captures the complete state of your Worker at a point in time: its <a href="/workers/wrangler/bundling/">bundled code</a>, <a href="/workers/static-assets/">static assets</a>, <a href="/workers/runtime-apis/bindings/">bindings</a>, and <a href="/workers/configuration/compatibility-dates/">compatibility settings</a>. Each version has a unique ID and tracks who created it, when, and from where.</p>
<p>You can optionally attach a message and tag to a version when you upload it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16044.md")
</aside>
<h2 id="deployments">Deployments</h2>
<p>A deployment determines which version(s) of your Worker are actively serving traffic. A deployment can reference one version (serving 100% of traffic) or two versions (with traffic split between them during a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a>).</p>
<p>Each deployment tracks who created it, when, and which version(s) it includes.</p>
<h2 id="default-behavior">Default behavior</h2>
<p>By default, these two concepts are coupled together - when you run <a href="/workers/wrangler/commands/workers/#deploy"><code>wrangler deploy</code></a>, Workers creates a new version and immediately deploys it to 100% of traffic in a single step.</p>
<p>You can decouple them so that uploading a version and deploying it are independent actions. This gives you control over when new code goes live, and lets you use strategies like <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployments</a> or manual promotion. Refer to <a href="/workers/versions-and-deployments/deployment-management/">Deployment management</a> for details.</p>
<h2 id="view-versions-and-deployments">View versions and deployments</h2>
<h3 id="via-wrangler">Via Wrangler</h3>
<p>Wrangler allows you to view the 100 most recent versions and deployments. Refer to the <a href="/workers/wrangler/commands/workers/#versions-list"><code>versions list</code></a> and <a href="/workers/wrangler/commands/workers/#deployments-list"><code>deployments list</code></a> documentation for the commands.</p>
<h3 id="via-the-cloudflare-dashboard">Via the Cloudflare dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker &gt; <strong>Deployments</strong>.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/workers/versions-and-deployments/deployment-management/">Deployment management</a> - Upload versions without deploying them and control when they go live</li>
<li><a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a> - Test new versions before deploying them to production</li>
<li><a href="/workers/versions-and-deployments/gradual-deployments/">Gradual deployments</a> - Split traffic between two versions using percentage-based routing</li>
<li><a href="/workers/versions-and-deployments/gradual-deployments/version-affinity/">Version affinity</a> - Consistently route users to the same version across page loads during a gradual deployment</li>
<li><a href="/workers/versions-and-deployments/version-overrides/">Version overrides</a> - Send a request to a specific version by ID for smoke testing and pinning between Workers</li>
<li><a href="/workers/versions-and-deployments/rollbacks/">Rollbacks</a> - Revert to a previously deployed version</li>
</ul>
