<p>Preview URLs allow you to preview new versions of your Worker without deploying it to production.</p>
<p>There are two types of preview URLs:</p>
<ul>
<li><strong>Versioned Preview URLs</strong>: A unique URL generated automatically for each new version of your Worker.</li>
<li><strong>Aliased Preview URLs</strong>: A static, human-readable alias that you can manually assign to a Worker version.</li>
</ul>
<p>Both preview URL types follow the format: <code>&lt;VERSION_PREFIX OR ALIAS&gt;-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code>.</p>
<p>Preview URLs can be:</p>
<ul>
<li>Integrated into CI/CD pipelines, allowing automatic generation of preview environments for every pull request.</li>
<li>Used for collaboration between teams to test code changes in a live environment and verify updates.</li>
<li>Used to test new API endpoints, validate data formats, and ensure backward compatibility with existing services.</li>
</ul>
<p>When testing zone level performance or security features for a version, we recommend using <a href="/workers/versions-and-deployments/version-overrides/">version overrides</a> so that your zone's performance and security settings apply.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16041.md")
</aside>
<h2 id="types-of-preview-urls">Types of Preview URLs</h2>
<h3 id="versioned-preview-urls">Versioned Preview URLs</h3>
<p>Every time you create a new <a href="/workers/versions-and-deployments/#versions">version</a> of your Worker, a unique static version preview URL is generated automatically. These URLs use a version prefix and follow the format <code>&lt;VERSION_PREFIX&gt;-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code>.</p>
<p>New versions of a Worker are created when you run:</p>
<ul>
<li><a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a></li>
<li><a href="/workers/wrangler/commands/general/#versions-upload"><code>wrangler versions upload</code></a></li>
<li>Or when you make edits via the Cloudflare dashboard</li>
</ul>
<p>If Preview URLs have been enabled, they are public and available immediately after version creation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16040.md")
</aside>
<h4 id="view-versioned-preview-urls-using-wrangler">View versioned preview URLs using Wrangler</h4>
<p>The <a href="/workers/wrangler/commands/general/#versions-upload"><code>wrangler versions upload</code></a> command uploads a new <a href="/workers/versions-and-deployments/#versions">version</a> of your Worker and returns a preview URL for each version uploaded.</p>
<h4 id="view-versioned-preview-urls-on-the-workers-dashboard">View versioned preview URLs on the Workers dashboard</h4>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker.</li>
<li>Go to the <strong>Deployments</strong> tab, and find the version you would like to view.</li>
</ol>
<h3 id="aliased-preview-urls">Aliased preview URLs</h3>
<p>Aliased preview URLs let you assign a persistent, readable alias to a specific Worker version. These are useful for linking to stable previews across many versions (e.g. to share an upcoming but still actively being developed new feature). A common workflow would be to assign an alias for the branch that you're working on. These types of preview URLs follow the same pattern as other preview URLs:
<code>&lt;ALIAS&gt;-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16039.md")
</aside>
<h4 id="create-an-alias">Create an Alias</h4>
<p>Aliases may be created during <code>versions upload</code>, by providing the <code>--preview-alias</code> flag with a valid alias name:</p>
<pre><code class="language-bash">wrangler versions upload --preview-alias staging&#10;</code></pre>
<p>The resulting alias would be associated with this version, and immediately available at:
<code>staging-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code></p>
<h4 id="rules-and-limitations">Rules and limitations</h4>
<ul>
<li>Aliases may only be created during version upload.</li>
<li>Aliases must use only lowercase letters, numbers, and dashes.</li>
<li>Aliases must begin with a lowercase letter.</li>
<li>The alias and Worker name combined (with a dash) must not exceed 63 characters due to DNS label limits.</li>
<li>Only the 1000 most recently deployed aliases are retained. When a new alias is created beyond this limit, the least recently deployed alias is deleted.</li>
</ul>
<h2 id="manage-access-to-preview-urls">Manage access to Preview URLs</h2>
<p>When enabled, Preview URLs are available publicly. To require visitors to sign in before they can access Preview URLs, use <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<p>Access can protect previews for one Worker or every Worker in an account. You can also protect both production and preview deployments.</p>
<p>To use details about the signed-in user in your Worker, read the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/#user-identity">user's identity</a> from the validated JWT or the <code>/cdn-cgi/access/get-identity</code> endpoint.</p>
<h2 id="toggle-preview-urls-enable-or-disable">Toggle Preview URLs (Enable or Disable)</h2>
<p>Note:</p>
<ul>
<li>Preview URLs are enabled by default when <code>workers_dev</code> is enabled.</li>
<li>Preview URLs are disabled by default when <code>workers_dev</code> is disabled.</li>
<li>Disabling Preview URLs will disable routing to both versioned and aliased preview URLs.</li>
</ul>
<h3 id="from-the-dashboard">From the Dashboard</h3>
<p>To toggle Preview URLs for a Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>For Preview URLs, click <strong>Enable</strong> or <strong>Disable</strong>.</li>
<li>Confirm your action.</li>
</ol>
<h3 id="from-the-wrangler-configuration-file-workers-wrangler-configuration">From the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16038.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16037.md")
</aside>
<p>To toggle Preview URLs for a Worker, include any of the following in your Worker's Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16042.md")
</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16043.md")
</div>
<p>If not given, <code>preview_urls = workers_dev</code> is the default.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16036.md")
</aside>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Preview URLs are not generated for Workers that implement a <a href="/durable-objects/">Durable Object</a>, including <a href="/containers/">Containers</a> and <a href="/sandbox/">Sandbox</a> Workers. For Containers testing options, refer to <a href="/containers/guides/deploy/#before-production">Deploy Containers</a>.</li>
<li>Preview URLs are not currently generated for <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers">user Workers</a>. This is a temporary limitation, we are working to remove it.</li>
<li>You cannot currently configure Preview URLs to run on a subdomain other than <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a>.</li>
<li>You cannot view logs for Preview URLs today, this includes Workers Logs, Wrangler tail and Logpush.</li>
</ul>
