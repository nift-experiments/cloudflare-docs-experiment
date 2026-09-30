<p>Cloudflare Workers provides comprehensive observability tools to help you understand how your applications are performing, diagnose issues, and gain insights into request flows. Whether you want to use Cloudflare's native observability platform or export telemetry data to your existing monitoring stack, Workers has you covered.</p>
<h2 id="logs">Logs</h2>
<p>Logs are essential for troubleshooting and understanding your application's behavior. Cloudflare offers several ways to access and manage your Worker logs.</p>
<div class="nb-card-grid">
@input("content/.markup/bodies/16253.md")
</div>
<h2 id="traces">Traces</h2>
<p><a href="/workers/observability/traces/">Tracing</a> gives you end-to-end visibility into the life of a request as it travels through your Workers application and connected services. With automatic instrumentation, Cloudflare captures telemetry data for fetch calls, binding operations (KV, R2, Durable Objects), and handler invocations - no code changes required.</p>
<h2 id="metrics-and-analytics">Metrics and analytics</h2>
<p><a href="/workers/observability/metrics-and-analytics/">Metrics and analytics</a> let you monitor your Worker's health with built-in metrics including request counts, error rates, CPU time, wall time, and execution duration. View metrics per Worker or aggregated across all Workers on a zone.</p>
<h2 id="query-builder">Query Builder</h2>
<p>The <a href="/workers/observability/query-builder/">Query Builder</a> helps you write structured queries to investigate and visualize your telemetry data. Build queries with filters, aggregations, and groupings to analyze logs and identify patterns.</p>
<h2 id="exporting-data">Exporting data</h2>
<p><a href="/workers/observability/exporting-opentelemetry-data/">Export OpenTelemetry-compliant traces and logs</a> from Workers to your existing observability stack. Workers supports exporting to any destination with an OTLP endpoint, including Honeycomb, Grafana Cloud, Axiom, and Sentry.</p>
<h2 id="debugging">Debugging</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/16254.md")
</div>
<h2 id="additional-resources">Additional resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/16255.md")
</div>
