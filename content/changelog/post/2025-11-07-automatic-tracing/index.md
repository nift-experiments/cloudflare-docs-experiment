<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 7, 2025</time><h2 id="post-title">Workers automatic tracing, now in open beta</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Enable automatic tracing on your Workers, giving you detailed metadata and timing information for every operation your Worker performs.</p>
<p><img src="/assets/upstream/images/workers-observability/R2_Screenshot.png" alt="Tracing example" /></p>
<p>Tracing helps you identify performance bottlenecks, resolve errors, and understand how your Worker interacts with other services on the Workers platform. You can now answer questions like:</p>
<ul>
<li>Which calls are slowing down my application?</li>
<li>Which queries to my database take the longest?</li>
<li>What happened within a request that resulted in an error?</li>
</ul>
<p><strong>You can now:</strong></p>
<ul>
<li>View traces alongside your logs in the Workers Observability dashboard</li>
<li>Export traces (and correlated logs) to any <a href="https://opentelemetry.io/docs/specs/otel/protocol/">OTLP-compatible destination</a>, such as <a href="/workers/observability/exporting-opentelemetry-data/honeycomb/">Honeycomb</a>, <a href="/workers/observability/exporting-opentelemetry-data/sentry/">Sentry</a> or <a href="/workers/observability/exporting-opentelemetry-data/grafana-cloud/">Grafana</a>, by configuring a tracing destination in the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/destinations">Cloudflare dashboard</a></li>
<li>Analyze and query across span attributes (operation type, status, duration, errors)</li>
</ul>
<h4 id="to-get-started-set">To get started, set:</h4>
<pre><code class="language-jsonc">{&#10;	&quot;observability&quot;: {&#10;		&quot;traces&quot;: {&#10;			&quot;enabled&quot;: true,&#10;		},&#10;	},&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17790.md")</aside>
<h4 id="want-to-learn-more">Want to learn more?</h4>
<ul>
<li><a href="https://blog.cloudflare.com/workers-tracing-now-in-open-beta/">Read the announcement</a></li>
<li><a href="/workers/observability/traces/">Check out the documentation</a></li>
</ul>
</div></article></div>
