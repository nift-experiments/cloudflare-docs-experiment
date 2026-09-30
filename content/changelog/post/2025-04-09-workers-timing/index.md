<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 9, 2025</time><h2 id="post-title">CPU time and Wall time now published for Workers Invocations</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now observe and investigate the CPU time and Wall time for every Workers Invocations.</p>
<ul>
<li>For <a href="/workers/observability/logs/workers-logs">Workers Logs</a>, CPU time and Wall time are surfaced in the <a href="/workers/observability/logs/workers-logs/#invocation-logs">Invocation Log</a>..</li>
<li>For <a href="/workers/observability/logs/tail-workers">Tail Workers</a>, CPU time and Wall time are surfaced at the top level of the <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">Workers Trace Events object</a>.</li>
<li>For <a href="/workers/observability/logs/logpush">Workers Logpush</a>, CPU and Wall time are surfaced at the top level of the <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">Workers Trace Events object</a>. All new jobs will have these new fields included by default. Existing jobs need to be updated to include CPU time and Wall time.</li>
</ul>
<p>You can use a Workers Logs filter to search for logs where Wall time exceeds 100ms.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-wall-time-filter.png" alt="Workers Logs Wall Time Filter" /></p>
<p>You can also use the Workers Observability <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/investigate">Query Builder</a> to find the median CPU time and median Wall time for all of your Workers.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-query-builder.png" alt="Query Builder filter" /></p>
</div></article></div>
