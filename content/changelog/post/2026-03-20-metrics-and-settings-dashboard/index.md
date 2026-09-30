<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 20, 2026</time><h2 id="post-title">Observability for Workers VPC Services</h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p>Each VPC Service now has a <strong>Metrics</strong> tab so you can monitor connection health and debug failures without leaving the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers-vpc/2026-03-20-metrics-dashboard.png" alt="Workers VPC Metrics dashboard showing connections, latency, and errors charts" /></p>
<ul>
<li><strong>Connections</strong> — See successful and failed connections over time, broken down by what is responsible: your origin (Bad Upstream), your configuration (Client), or Cloudflare (Internal).</li>
<li><strong>Latency</strong> — Track connection and DNS resolution latency trends.</li>
<li><strong>Errors</strong> — Drill into specific error codes grouped by category, with filters to isolate upstream, client, or internal failures.</li>
</ul>
<p>You can also view and edit your VPC Service configuration, host details, and port assignments from the <strong>Settings</strong> tab.</p>
<p>For a full list of error codes and what they mean, refer to <a href="/workers-vpc/reference/troubleshooting/">Troubleshooting</a>.</p>
</div></article></div>
