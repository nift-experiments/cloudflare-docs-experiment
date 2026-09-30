<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 8, 2025</time><h2 id="post-title">Python cold start improvements</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Python Workers now feature improved cold start performance, reducing initialization time for new Worker instances.
This improvement is particularly noticeable for Workers with larger dependency sets or complex initialization logic.</p>
<p>Every time you deploy a Python Worker, a memory snapshot is captured after the top level of the Worker is executed.
This snapshot captures all imports, including package imports that are often costly to load. The memory snapshot is loaded
when the Worker is first started, avoiding the need to reload the Python runtime and all dependencies on each cold start.</p>
<p>We set up a benchmark that imports common packages (<a href="https://www.python-httpx.org/">httpx</a>,
<a href="https://fastapi.tiangolo.com/">fastapi</a> and <a href="https://docs.pydantic.dev/latest/">pydantic</a>)
to see how Python Workers stack up against other platforms:</p>
<table>
<thead>
<tr>
<th>Platform</th>
<th>Mean Cold Start (ms)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Python Workers</td>
<td>1027</td>
</tr>
<tr>
<td>AWS Lambda</td>
<td>2502</td>
</tr>
<tr>
<td>Google Cloud Run</td>
<td>3069</td>
</tr>
</tbody>
</table>
<p>These benchmarks run continuously. You can view the results and the methodology on our <a href="https://cold.edgeworker.net">benchmark page</a>.</p>
<p>In additional testing, we have found that without any memory snapshot, the cold start for this benchmark takes around 10 seconds, so this change improves cold start performance by roughly a factor of 10.</p>
<p>To get started with Python Workers, check out our <a href="/workers/languages/python/">Python Workers overview</a>.</p>
</div></article></div>
