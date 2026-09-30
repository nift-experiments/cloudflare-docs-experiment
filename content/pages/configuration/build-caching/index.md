<p>Improve Pages build times by caching dependencies and build output between builds with a project-wide shared cache.</p>
<p>The first build to occur after enabling build caching on your Pages project will save to cache. Every subsequent build will restore from cache unless configured otherwise.</p>
<h2 id="about-build-cache">About build cache</h2>
<p>When enabled, the build cache will automatically detect and cache data from each build. Refer to <a href="/pages/configuration/build-caching/#frameworks">Frameworks</a> to review what directories are automatically saved and restored from the build cache.</p>
<h3 id="requirements">Requirements</h3>
<p>Build caching requires the <a href="/pages/configuration/build-image/#v2-build-system">V2 build system</a> or later. To update from V1, refer to the <a href="/pages/configuration/build-image/#v1-to-v2-migration">V2 build system migration instructions</a>.</p>
<h3 id="package-managers">Package managers</h3>
<p>Pages will cache the global cache directories of the following package managers:</p>
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
<td><code>.pnpm-store</code></td>
</tr>
<tr>
<td><a href="https://bun.sh/">bun</a></td>
<td><code>.bun/install/cache</code></td>
</tr>
</tbody>
</table>
<h3 id="frameworks">Frameworks</h3>
<p>Some frameworks provide a cache directory that is typically populated by the framework with intermediate build outputs or dependencies during build time. Pages will automatically detect the framework you are using and cache this directory for reuse in subsequent builds.</p>
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
<td>Hugo</td>
<td><code>.cache</code></td>
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
<h3 class="nb-aside-title" id="hugo-build-caching">Hugo build caching</h3>
@markup("md", "content/.markup/bodies/11077.md")
</aside>
<h3 id="limits">Limits</h3>
<p>The following limits are imposed for build caching:</p>
<ul>
<li><strong>Retention</strong>: Cache is purged seven days after its last read date. Unread cache artifacts are purged seven days after creation.</li>
<li><strong>Storage</strong>: Every project is allocated 10 GB. If the project cache exceeds this limit, the project will automatically start deleting artifacts that were read least recently.</li>
</ul>
<h2 id="enable-build-cache">Enable build cache</h2>
<p>To enable build caching :</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11078.md")
</div>
<h2 id="clear-build-cache">Clear build cache</h2>
<p>The build cache can be cleared for a project if needed, such as when debugging build issues. To clear the build cache:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11079.md")
</div>
