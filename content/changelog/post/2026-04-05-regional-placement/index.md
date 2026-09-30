<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 5, 2026</time><h2 id="post-title">Control where your Containers run with regional and jurisdictional placement</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>You can now specify placement constraints to control where your <a href="/containers/">Containers</a> run.</p>
<table>
<thead>
<tr>
<th>Constraint</th>
<th>Values</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>regions</code></td>
<td><code>ENAM</code>, <code>WNAM</code>, <code>EEUR</code>, <code>WEUR</code></td>
<td>Geographic placement</td>
</tr>
<tr>
<td><code>jurisdiction</code></td>
<td><code>eu</code>, <code>fedramp</code></td>
<td>Compliance boundaries</td>
</tr>
</tbody>
</table>
<p>Use <code>regions</code> to limit placement to specific geographic areas. Use <code>jurisdiction</code> to restrict containers to compliance boundaries — <code>eu</code> maps to European regions (EEUR, WEUR) and <code>fedramp</code> maps to North American regions (ENAM, WNAM).</p>
<p>Refer to <a href="/containers/concepts/placement/">Containers placement</a> for more details.</p>
</div></article></div>
