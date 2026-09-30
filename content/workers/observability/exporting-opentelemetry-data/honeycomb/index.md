<p>Honeycomb is an observability platform built for high-cardinality data that helps you understand and debug your applications. By exporting your Cloudflare Workers application telemetry to Honeycomb, you can:</p>
<ul>
<li>Visualize traces to understand request flows and identify performance bottlenecks</li>
<li>Query and analyze logs with unlimited dimensionality across any attribute</li>
<li>Create custom queries and dashboards to monitor your Workers</li>
</ul>
<p><img src="/assets/upstream/images/workers-observability/honeycomb-example.png" alt="Trace view including POST request, fetch operations, durable object subrequest, and queue send, with timing information displayed on a timeline" /></p>
<p>This guide will walk you through configuring your Cloudflare Worker application to export OpenTelemetry-compliant traces and logs to Honeycomb.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, ensure you have:</p>
<ul>
<li>An active <a href="https://ui.honeycomb.io/signup">Honeycomb account</a> (free tier available)</li>
<li>A deployed Worker that you want to monitor</li>
</ul>
<h2 id="step-1-get-your-honeycomb-api-key">Step 1: Get your Honeycomb API key</h2>
<ol>
<li>Log in to your <a href="https://ui.honeycomb.io/">Honeycomb account</a></li>
<li>Navigate to your account settings by clicking on your profile icon in the top right</li>
<li>Select <strong>Team Settings</strong></li>
<li>In the left sidebar, click <strong>Environments</strong> and click the gear icon</li>
<li>Find your environment (e.g., <code>production</code>, <code>test</code>) or create a new one</li>
<li>Under <strong>API Keys</strong>, click <strong>Create Ingest API Key</strong></li>
<li>Configure your API key:
<ul>
<li><strong>Name</strong>: Enter a descriptive name (e.g., <code>cloudflare-workers-otel</code>)</li>
<li><strong>Permissions</strong>: Select <strong>Can create services/datasets</strong> (required for OTLP ingestion)</li>
</ul>
</li>
<li>Click <strong>Create</strong></li>
<li><strong>Important</strong>: Copy the API key immediately and store it securely - you won't be able to see it again</li>
</ol>
<p>The API key will look something like: <code>hcaik_01hq...</code></p>
<h2 id="step-2-configure-cloudflare-destinations">Step 2: Configure Cloudflare destinations</h2>
<p>Now you'll create destinations in the Cloudflare dashboard that point to Honeycomb.</p>
<h3 id="honeycomb-otlp-endpoints">Honeycomb OTLP endpoints</h3>
<p>Honeycomb provides separate OTLP endpoints for traces and logs:</p>
<ul>
<li><strong>Traces</strong>: <code>https://api.honeycomb.io/v1/traces</code></li>
<li><strong>Logs</strong>: <code>https://api.honeycomb.io/v1/logs</code></li>
</ul>
<h3 id="configure-trace-destination">Configure trace destination</h3>
<ol>
<li>Navigate to your Cloudflare account's <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/pipelines">Workers Observability</a> section</li>
<li>Click <strong>Add destination</strong></li>
<li>Configure your trace destination:
<ul>
<li><strong>Destination Name</strong>: <code>honeycomb-traces</code> (or any descriptive name)</li>
<li><strong>Destination Type</strong>: Select <strong>Traces</strong></li>
<li><strong>OTLP Endpoint</strong>: <code>https://api.honeycomb.io/v1/traces</code></li>
<li><strong>Custom Headers</strong>: Add the authentication header:
<ul>
<li>Header name: <code>x-honeycomb-team</code></li>
<li>Header value: Your Honeycomb API key (e.g., <code>hcaik_01hq...</code>)</li>
</ul>
</li>
</ul>
</li>
<li>Click <strong>Save</strong></li>
</ol>
<h3 id="configure-logs-destination">Configure logs destination</h3>
<p>Repeat the process for logs:</p>
<ol>
<li>Click <strong>Add destination</strong> again</li>
<li>Configure your logs destination:
<ul>
<li><strong>Destination Name</strong>: <code>honeycomb-logs</code> (or any descriptive name)</li>
<li><strong>Destination Type</strong>: Select <strong>Logs</strong></li>
<li><strong>OTLP Endpoint</strong>: <code>https://api.honeycomb.io/v1/logs</code></li>
<li><strong>Custom Headers</strong>: Add the authentication header:
<ul>
<li>Header name: <code>x-honeycomb-team</code></li>
<li>Header value: Your Honeycomb API key (same as above)</li>
</ul>
</li>
</ul>
</li>
<li>Click <strong>Save</strong></li>
</ol>
<h2 id="step-3-configure-your-worker">Step 3: Configure your Worker</h2>
<p>With your destinations created in the Cloudflare dashboard, update your Worker's configuration to enable telemetry export.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17055.md")
</div>
<p>After updating your configuration, deploy your Worker for the changes to take effect.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17054.md")
</aside>
