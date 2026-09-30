<p>Below are limits observed by the Cloudflare Free plan. For more details on removing these limits, refer to the <a href="https://www.cloudflare.com/plans">Cloudflare plans</a> page.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/10873.md")
</aside>
<h2 id="builds">Builds</h2>
<p>Each time you push new code to your Git repository, Pages will build and deploy your site. Build limits depend on your plan:</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
</tr>
</thead>
<tbody>
<tr>
<td>Builds</td>
<td>1 build at a time</td>
<td>5 concurrent builds</td>
<td>20 concurrent builds</td>
</tr>
<tr>
<td>Builds per month</td>
<td>500</td>
<td>5,000</td>
<td>20,000</td>
</tr>
</tbody>
</table>
<p>Builds will timeout after 20 minutes. Concurrent builds are counted per account.</p>
<h2 id="custom-domains">Custom domains</h2>
<p>Based on your Cloudflare plan type, a Pages project is limited to a specific number of custom domains. This limit is on a per-project basis.</p>
<table>
<thead>
<tr>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>100</td>
<td>250</td>
<td>500</td>
<td>500<sup><a href="#footnote-1">1</a></sup></td>
</tr>
</tbody>
</table>
<h2 id="files">Files</h2>
<p>Pages uploads each file on your site to Cloudflare's globally distributed network to deliver a low latency experience to every user that visits your site. Cloudflare Pages sites can contain up to 20,000 files on the Free plan.</p>
<p>Paid plans (such as Pro, Business, and Enterprise plans) can have up to 100,000 files per site. To enable this increased limit, set the environment variable <code>PAGES_WRANGLER_MAJOR_VERSION=4</code> in your Pages project settings.</p>
<h2 id="file-size">File size</h2>
<p>The maximum file size for a single Cloudflare Pages site asset is 25 MiB.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="larger-files">Larger Files</h3>
@markup("md", "content/.markup/bodies/10872.md")
</aside>
<h2 id="functions">Functions</h2>
<p>Requests to <a href="/pages/functions/">Pages functions</a> count towards your quota for Workers plans, including requests from your Function to KV or Durable Object bindings.</p>
<p>Pages supports the <a href="/workers/platform/pricing/#example-pricing-standard-usage-model">Standard usage model</a>.</p>
<h2 id="headers">Headers</h2>
<p>A <code>_headers</code> file can have a maximum of 100 header rules.</p>
<p>An individual header in a <code>_headers</code> file can have a maximum of 2,000 characters. For managing larger headers, it is recommended to implement <a href="/pages/functions/">Pages Functions</a>.</p>
<h2 id="preview-deployments">Preview deployments</h2>
<p>You can have an unlimited number of <a href="/pages/configuration/preview-deployments/">preview deployments</a> active on your project at a time.</p>
<h2 id="redirects">Redirects</h2>
<p>A <code>_redirects</code> file can have a maximum of 2,000 static redirects and 100 dynamic redirects, for a combined total of 2,100 redirects. It is recommended to use <a href="/pages/configuration/redirects/#surpass-_redirects-limits">Bulk Redirects</a> when you have a need for more than the <code>_redirects</code> file supports.</p>
<h2 id="users">Users</h2>
<p>Your Pages site can be managed by an unlimited number of users via the Cloudflare dashboard. Note that this does not correlate with your Git project – you can manage both public and private repositories, open issues, and accept pull requests via without impacting your Pages site.</p>
<h2 id="projects">Projects</h2>
<p>Cloudflare Pages has a limit of 100 projects<sup><a href="#footnote-2">2</a></sup> per account. This limit is not routinely increased.</p>
<p>If you need to host more than 100 sites, use one of these products designed for scale:</p>
<ul>
<li><strong><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a></strong> — Deploy sites and applications at scale with no project limit. Supports <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/">static assets</a>.</li>
<li><strong><a href="/workers/static-assets/">Workers Static Assets</a></strong> — Deploy static sites as individual Workers. Paid plans support up to 500 Workers per account, each serving up to 100,000 static asset files.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10871.md")
</aside>
<p>In order to protect against abuse of the service, Cloudflare limits the number of new Pages projects you can create within your first 48 hours of using the service. If you are temporarily blocked from creating new projects, this restriction will automatically lift once the initial 48-hour window has passed.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">If you need more custom domains, contact your account team.</li>
<li id="footnote-2">If you need a higher project limit, use [Workers for Platforms](/cloudflare-for-platforms/workers-for-platforms/).</li></ol></section>
