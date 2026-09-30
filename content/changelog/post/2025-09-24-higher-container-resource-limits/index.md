<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 25, 2025</time><h2 id="post-title">Run more Containers with higher resource limits</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>You can now run more Containers concurrently with higher limits on CPU, memory, and disk.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>New Limit</th>
<th>Previous Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Memory for concurrent live Container instances</td>
<td>400GiB</td>
<td>40GiB</td>
</tr>
<tr>
<td>vCPU for concurrent live Container instances</td>
<td>100</td>
<td>20</td>
</tr>
<tr>
<td>Disk for concurrent live Container instances</td>
<td>2TB</td>
<td>100GB</td>
</tr>
</tbody>
</table>
<p>You can now run 1000 instances of the <code>dev</code> instance type, 400 instances of <code>basic</code>, or 100 instances of <code>standard</code> concurrently.</p>
<p>This opens up new possibilities for running larger-scale workloads on Containers.</p>
<p>See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,
and the <a href="/containers/platform/limits/">limits documentation</a> for more details on the available instance types and limits.</p>
</div></article></div>
