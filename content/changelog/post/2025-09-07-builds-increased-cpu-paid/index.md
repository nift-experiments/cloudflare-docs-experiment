<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 18, 2025</time><h2 id="post-title">Increased vCPU for Workers Builds on paid plans</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We recently <a href="/changelog/2025-08-04-builds-increased-disk-size/">increased the available disk space</a> from 8 GB to 20 GB for <strong>all</strong> plans. Building on that improvement, we’re now doubling the CPU power available for paid plans — from 2 vCPU to <strong>4 vCPU</strong>.</p>
<p>These changes continue our focus on making <a href="/workers/ci-cd/builds/">Workers Builds</a> faster and more reliable.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Free Plan</th>
<th>Paid Plans</th>
</tr>
</thead>
<tbody>
<tr>
<td>CPU</td>
<td>2 vCPU</td>
<td><strong>4 vCPU</strong></td>
</tr>
</tbody>
</table>
<h4 id="performance-improvements">Performance Improvements</h4>
- **Fast build times**: Even single-threaded workloads benefit from having more vCPUs 
- **2x faster multi-threaded builds**: Tools like [esbuild](https://esbuild.github.io/) and [webpack](https://webpack.js.org/) can now utilize additional cores, delivering near-linear performance scaling
<p>All other <a href="/workers/ci-cd/builds/limits-and-pricing/">build limits</a> — including memory, build minutes, and timeout remain unchanged.</p>
</div></article></div>
