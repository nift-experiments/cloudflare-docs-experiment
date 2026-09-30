<p>Cloudflare Workers accounts come with a <code>workers.dev</code> subdomain that is configurable in the Cloudflare dashboard. Your <code>workers.dev</code> subdomain allows you getting started quickly by deploying Workers without first onboarding your custom domain to Cloudflare.</p>
<p>It's recommended to run production Workers on a <a href="/workers/configuration/routing/">Workers route or custom domain</a>, rather than on your <code>workers.dev</code> subdomain. Your <code>workers.dev</code> subdomain is treated as a <a href="https://www.cloudflare.com/plans/">Free website</a> and is intended for personal or hobby projects that aren't business-critical.</p>
<h2 id="configure-workers-dev">Configure <code>workers.dev</code></h2>
<p><code>workers.dev</code> subdomains take the format: <code>&lt;YOUR_ACCOUNT_SUBDOMAIN&gt;.workers.dev</code>. To change your <code>workers.dev</code> subdomain:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Change</strong> next to <strong>Your subdomain</strong>.</li>
</ol>
<p>All Workers are assigned a <code>workers.dev</code> route when they are created or renamed following the syntax <code>&lt;YOUR_WORKER_NAME&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>. The <a href="/workers/wrangler/configuration/#inheritable-keys"><code>name</code></a> field in your Worker configuration is used as the subdomain for the deployed Worker.</p>
<h2 id="manage-access-to-workers-dev">Manage access to <code>workers.dev</code></h2>
<p>When enabled, your <code>workers.dev</code> URL is available publicly. To require visitors to sign in before they can access a <code>workers.dev</code> URL, use <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<p>Access can protect one Worker's production <code>workers.dev</code> URL, preview URLs, or both. You can also protect all Workers or all Worker previews in an account.</p>
<p>To use details about the signed-in user in your Worker, use <a href="/workers/configuration/cloudflare-access/#read-authenticated-user-identity-with-ctxaccess"><code>ctx.access</code></a>. You can also read the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/#user-identity">user's identity</a> from the validated JWT or the <code>/cdn-cgi/access/get-identity</code> endpoint.</p>
<h2 id="disabling-workers-dev">Disabling <code>workers.dev</code></h2>
<h3 id="disabling-workers-dev-in-the-dashboard">Disabling <code>workers.dev</code> in the dashboard</h3>
<p>To disable the <code>workers.dev</code> route for a Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>On <code>workers.dev</code> click &quot;Disable&quot;.</li>
<li>Confirm you want to disable.</li>
</ol>
<h3 id="disabling-workers-dev-in-the-wrangler-configuration-file">Disabling <code>workers.dev</code> in the Wrangler configuration file</h3>
<p>To disable the <code>workers.dev</code> route for a Worker, include the following in your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16824.md")
</div>
<p>When you redeploy your Worker with this change, the <code>workers.dev</code> route will be disabled. Preview URLs default to matching your <code>workers_dev</code> setting unless explicitly configured. If you explicitly enabled Preview URLs, <a href="/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable">disable them separately</a>.</p>
<p>If you do not specify <code>workers_dev = false</code> but add a <a href="/workers/wrangler/configuration/#routes"><code>routes</code> component</a> to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, the value of <code>workers_dev</code> will be inferred as <code>false</code> on the next deploy.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16823.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>When deploying a Worker with a <code>workers.dev</code> subdomain enabled, your Worker name must meet the following requirements:</p>
<ul>
<li>Must be 63 characters or less</li>
<li>Must contain only alphanumeric characters (<code>a-z</code>, <code>A-Z</code>, <code>0-9</code>) and dashes (<code>-</code>)</li>
<li>Cannot start or end with a dash (<code>-</code>)</li>
</ul>
<p>These restrictions apply because the Worker name is used as a DNS label in your <code>workers.dev</code> URL. DNS labels have a maximum length of 63 characters and cannot begin or end with a dash.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16822.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/announcing-workers-dev">Announcing <code>workers.dev</code></a></li>
<li><a href="/workers/wrangler/configuration/#types-of-routes">Wrangler routes configuration</a></li>
</ul>
