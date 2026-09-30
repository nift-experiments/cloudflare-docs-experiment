<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 7, 2025</time><h2 id="post-title">Capture up to 256 KB of log events in each Workers Invocation</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now capture a maximum of 256 KB of log events per Workers invocation, helping you gain better visibility into application behavior.</p>
<p>All console.log() statements, exceptions, request metadata, and headers are automatically captured during the Worker invocation and emitted
as <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">JSON object</a>. <a href="/workers/observability/logs/workers-logs">Workers Logs</a> deserializes
this object before indexing the fields and storing them. You can also capture, transform, and export the JSON object in a
<a href="/workers/observability/logs/tail-workers">Tail Worker</a>.</p>
<p>256 KB is a 2x increase from the previous 128 KB limit. After you exceed this limit, further context associated with the request will not be
recorded in your logs.</p>
<p>This limit is automatically applied to all Workers.</p>
</div></article></div>
