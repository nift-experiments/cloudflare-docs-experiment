<p>Improve Workers build times by caching dependencies and build output between builds with a project-wide shared cache.</p>
<p>The first build to occur after enabling build caching on your Workers project will save relevant artifacts to cache. Every subsequent build will restore from cache unless configured otherwise.</p>
<h2 id="about-build-cache">About build cache</h2>
<p>When enabled, build caching will automatically detect which package manager and framework the project is using from its <code>package.json</code> and cache data accordingly for the build.</p>
<p>The following shows which package managers and frameworks are supported for dependency and build output caching respectively.</p>
<h3 id="package-managers">Package managers</h3>
<p>Workers build cache will cache the global cache directories of the following package managers:</p>
<table>
<thead>
<tr>
<th>Package Manager</th>
<th>Directories cached</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.npmjs.com/">npm</a></td>
<td><code>.npm</code></td>
</tr>
<tr>
<td><a href="https://yarnpkg.com/">yarn</a></td>
<td><code>.cache/yarn</code></td>
</tr>
<tr>
<td><a href="https://pnpm.io/">pnpm</a></td>
<td><code>.pnpm-store</code>, <code>.local/share/pnpm/store</code></td>
</tr>
<tr>
<td><a href="https://bun.sh/">bun</a></td>
<td><code>.bun/install/cache</code></td>
</tr>
</tbody>
</table>
<p>If you configure pnpm to use a different store directory, Workers Builds does not cache it.</p>
<h3 id="frameworks">Frameworks</h3>
<p>Some frameworks provide a cache directory that is typically populated by the framework with intermediate build outputs or dependencies during build time. Workers Builds will automatically detect the framework you are using and cache this directory for reuse in subsequent builds.</p>
<p>The following frameworks support build output caching:</p>
<table>
<thead>
<tr>
<th>Framework</th>
<th>Directories cached</th>
</tr>
</thead>
<tbody>
<tr>
<td>Astro</td>
<td><code>node_modules/.astro</code></td>
</tr>
<tr>
<td>Docusaurus</td>
<td><code>node_modules/.cache</code>, <code>.docusaurus</code>, <code>build</code></td>
</tr>
<tr>
<td>Eleventy</td>
<td><code>.cache</code></td>
</tr>
<tr>
<td>Gatsby</td>
<td><code>.cache</code>, <code>public</code></td>
</tr>
<tr>
<td>Next.js</td>
<td><code>.next/cache</code></td>
</tr>
<tr>
<td>Nuxt</td>
<td><code>node_modules/.cache/nuxt</code></td>
</tr>
<tr>
<td>SvelteKit</td>
<td><code>node_modules/.cache/imagetools</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16781.md")
</aside>
<h3 id="limits">Limits</h3>
<p>The following limits are imposed for build caching:</p>
<ul>
<li><strong>Retention</strong>: Cache is purged 7 days after its last read date. Unread cache artifacts are purged 7 days after creation.</li>
<li><strong>Storage</strong>: Every project is allocated 10 GB. If the project cache exceeds this limit, the project will automatically start deleting artifacts that were read least recently.</li>
</ul>
<h2 id="enable-build-cache">Enable build cache</h2>
<p>To enable build caching:</p>
<ol>
<li>Navigate to <a href="https://dash.cloudflare.com">Workers &amp; Pages Overview</a> on the Dashboard.</li>
<li>Find your Workers project.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Build</strong> &gt; <strong>Build cache</strong>.</li>
<li>Select <strong>Enable</strong> to turn on build caching.</li>
</ol>
<h2 id="clear-build-cache">Clear build cache</h2>
<p>The build cache can be cleared for a project when needed, such as when debugging build issues. To clear the build cache:</p>
<ol>
<li>Navigate to <a href="https://dash.cloudflare.com">Workers &amp; Pages Overview</a> on the Dashboard.</li>
<li>Find your Workers project.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Build</strong> &gt; <strong>Build cache</strong>.</li>
<li>Select <strong>Clear Cache</strong> to clear the build cache.</li>
</ol>
