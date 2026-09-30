<p>Grafana Cloud is a fully managed observability platform that provides visualization, alerting, and analytics for your telemetry data. By exporting your Cloudflare Workers telemetry to Grafana Cloud, you can:</p>
<ul>
<li>Visualize distributed traces in <strong>Grafana Tempo</strong> to understand request flows and performance bottlenecks</li>
<li>Query and analyze logs in <strong>Grafana Loki</strong> alongside your traces</li>
</ul>
<p>This guide will walk you through configuring Cloudflare Workers to export OpenTelemetry-compliant traces and logs to your Grafana Cloud stack.</p>
<p><img src="/assets/upstream/images/workers-observability/grafana-traces.png" alt="Grafana Tempo trace view showing a distributed trace for a service with multiple spans including fetch requests, durable object subrequests, and queue operations, with timing information displayed on a timeline" /></p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, ensure you have:</p>
<ul>
<li>An active <a href="https://grafana.com/auth/sign-up/create-user">Grafana Cloud account</a> (free tier available)</li>
<li>A deployed Worker that you want to monitor</li>
</ul>
<h2 id="step-1-access-the-opentelemetry-setup-guide">Step 1: Access the OpenTelemetry setup guide</h2>
<ol>
<li>Log in to your <a href="https://grafana.com/">Grafana Cloud portal</a></li>
<li>From your organization's home page, navigate to <strong>Connections</strong> → <strong>Add new connection</strong></li>
<li>Search for &quot;OpenTelemetry&quot; and select <strong>OpenTelemetry (OTLP)</strong></li>
<li>Select <strong>Quickstart</strong> then select <strong>JavaScript</strong></li>
<li>Click <strong>Create a new token</strong></li>
<li>Enter a name for your token (e.g., <code>cloudflare-workers-otel</code>) and click <strong>create token</strong></li>
<li>Click on <strong>Close</strong> without copying the token</li>
<li>Copy and Save the value for <code>OTEL_EXPORTER_OTLP_ENDPOINT</code> and <code>OTEL_EXPORTER_OTLP_HEADERS</code> in the <code>Environment variables</code> code block as the OTel endpoint and as the Auth header value respectively</li>
</ol>
<h2 id="step-2-set-up-destination">Step 2: Set up destination</h2>
1. Navigate to your Cloudflare account's [Workers Observability](https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/pipelines) section
2. Click **Add destination** and configure a destination name (e.g. `grafana-tracing`)
3. From Grafana, copy your Otel endpoint, auth header, and auth value 
  * Your OTEL endpoint will look like `https://otlp-gateway-prod-us-east-2.grafana.net/otlp` (append `/v1/traces` for traces and `/v1/logs` for logs) 
  * Your custom header should include: 
      * Your auth header name `Authorization`
      * Your auth header value `Basic MTMxxx...`
<h2 id="step-3-configure-your-worker">Step 3: Configure your Worker</h2>
<p>With your destination created in the Cloudflare dashboard, update your Worker's configuration to enable telemetry export.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17057.md")
</div>
<p>After updating your configuration, deploy your Worker for the changes to take effect.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17056.md")
</aside>
