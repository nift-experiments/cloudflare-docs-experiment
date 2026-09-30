<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 9, 2025</time><h2 id="post-title">Investigate your Workers with the Query Builder in the new Observability dashboard</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/">Workers Observability dashboard</a> offers a single place to investigate and explore your <a href="/workers/observability/logs/workers-logs">Workers Logs</a>.</p>
<p>The <strong>Overview</strong> tab shows logs from all your Workers in one place. The <strong>Invocations</strong> view groups logs together by invocation, which refers to the specific trigger that started the execution of the Worker (i.e. fetch). The <strong>Events</strong> view shows logs in the order they were produced, based on timestamp. Previously, you could only view logs for a single Worker.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-workers-observability-overview.png" alt="Workers Observability Overview Tab" /></p>
<p>The <strong>Investigate</strong> tab presents a Query Builder, which helps you write structured queries to investigate and visualize your logs. The Query Builder can help answer questions such as:</p>
<ul>
<li>Which paths are experiencing the most 5XX errors?</li>
<li>What is the wall time distribution by status code for my Worker?</li>
<li>What are the slowest requests, and where are they coming from?</li>
<li>Who are my top N users?</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-query-builder.png" alt="Workers Observability Overview Tab" /></p>
<p>The Query Builder can use any field that you store in your logs as a key to visualize, filter, and group by. Use the Query Builder to quickly access your data, build visualizations, save queries, and share them with your team.</p>
<h4 id="workers-logs-is-now-generally-available">Workers Logs is now Generally Available</h4>
<p><a href="/workers/observability/logs/workers-logs">Workers Logs</a> is now Generally Available. With a <a href="/workers/observability/logs/workers-logs/#enable-workers-logs">small change</a> to your Wrangler configuration, Workers Logs ingests, indexes, and stores all logs emitted from your Workers for up to 7 days.</p>
<p>We've introduced a number of changes during our beta period, including:</p>
<ul>
<li>Dashboard enhancements with customizable fields as columns in the Logs view and support for invocation-based grouping</li>
<li>Performance improvements to ensure no adverse impact</li>
<li>Public <a href="https://developers.cloudflare.com/api/resources/workers/subresources/observability/">API endpoints</a> for broader consumption</li>
</ul>
<p>The API documents three endpoints: list the keys in the telemetry dataset, run a query, and list the unique values for a key. For more, visit our <a href="https://developers.cloudflare.com/api/resources/workers/subresources/observability/">REST API documentation</a>.</p>
<p>Visit the <a href="/workers/observability/query-builder">docs</a> to learn more about the capabilities and methods exposed by the Query Builder. Start using Workers Logs and the Query Builder today by enabling observability for your Workers:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17771.md")</div>
</div></article></div>
