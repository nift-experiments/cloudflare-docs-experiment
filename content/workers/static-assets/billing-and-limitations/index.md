<h2 id="billing">Billing</h2>
<p>Requests to a project with static assets can either return static assets or invoke the Worker script, depending on if the request <a href="/workers/static-assets/routing/">matches a static asset or not</a>.</p>
<ul>
<li>Requests to static assets are free and unlimited. Requests to the Worker script (for example, in the case of SSR content) are billed according to Workers pricing. Refer to <a href="/workers/platform/pricing/#example-2">pricing</a> for an example.</li>
<li>There is no additional cost for storing Assets.</li>
<li><strong>Important note for free tier users</strong>: When using <a href="/workers/static-assets/binding/#run_worker_first"><code>run_worker_first</code></a>, requests matching the specified patterns will always invoke your Worker script. If you exceed your free tier request limits, these requests will receive a 429 (Too Many Requests) response instead of falling back to static asset serving. Negative patterns (patterns beginning with <code>!/</code>) will continue to serve assets correctly, as requests are directed to assets, without invoking your Worker script.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<p>See the <a href="/workers/platform/limits/#static-assets">Platform Limits</a></p>
<h2 id="troubleshooting">Troubleshooting</h2>
<ul>
<li><code>assets.bucket is a required field</code> — if you see this error, you need to update Wrangler to at least <code>3.78.10</code> or later. <code>bucket</code> is not a required field.</li>
</ul>
