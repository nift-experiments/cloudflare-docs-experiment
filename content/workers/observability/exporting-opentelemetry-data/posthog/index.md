<p>PostHog is a product analytics platform that helps you understand user behavior and debug issues. By exporting your Cloudflare Workers application telemetry to PostHog, you can:</p>
<ul>
<li>Correlate logs with user sessions, events, and error tracking data</li>
<li>Query and filter logs by severity, attributes, and custom properties</li>
<li>Connect application logs to session replays for full debugging context</li>
</ul>
<p><img src="/assets/upstream/images/workers-observability/posthog-example.png" alt="PostHog logs view with attributes expanded and a timeline view at the top" /></p>
<p>This guide will walk you through configuring your Cloudflare Worker application to export OpenTelemetry-compliant logs to PostHog.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, ensure you have:</p>
<ul>
<li>An active <a href="https://app.posthog.com/signup">PostHog account</a> (free tier available)</li>
<li>A deployed Worker that you want to monitor</li>
<li>Your PostHog project API key</li>
</ul>
<h2 id="step-1-get-your-posthog-project-api-key">Step 1: Get your PostHog project API key</h2>
<ol>
<li>Log in to your <a href="https://app.posthog.com/">PostHog account</a></li>
<li>Navigate to the <a href="https://app.posthog.com/settings/project"><strong>Project settings</strong></a></li>
<li>Find your <strong>Project API key</strong> in the project details section</li>
<li>Copy the API key - this is the same key used for capturing events and exceptions</li>
</ol>
<p>The API key should look something like: <code>phc_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</code></p>
<h2 id="step-2-determine-your-posthog-region-endpoint">Step 2: Determine your PostHog region endpoint</h2>
<p>PostHog has different endpoints depending on your data region:</p>
<table>
<thead>
<tr>
<th>Region</th>
<th>Logs Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>US</strong> (default)</td>
<td><code>https://us.i.posthog.com/i/v1/logs</code></td>
</tr>
<tr>
<td><strong>EU</strong></td>
<td><code>https://eu.i.posthog.com/i/v1/logs</code></td>
</tr>
</tbody>
</table>
<p>You can find your region in your PostHog project settings or by checking the URL when logged into PostHog (either <code>us.posthog.com</code> or <code>eu.posthog.com</code>).</p>
<h2 id="step-3-configure-cloudflare-logs-destination">Step 3: Configure Cloudflare Logs destination</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17048.md")
</aside>
<p>Now you'll create a destination in the Cloudflare dashboard that points to PostHog.</p>
<ol>
<li>Navigate to your Cloudflare account's <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/pipelines">Workers Observability</a> section</li>
<li>Click <strong>Add destination</strong></li>
<li>Configure your logs destination:
<ul>
<li><strong>Destination Name</strong>: <code>posthog-logs</code> (or any descriptive name)</li>
<li><strong>Destination Type</strong>: Select <strong>Logs</strong></li>
<li><strong>OTLP Endpoint</strong>: Your PostHog logs endpoint (e.g., <code>https://us.i.posthog.com/i/v1/logs</code> or <code>https://eu.i.posthog.com/i/v1/logs</code>)</li>
<li><strong>Custom Headers</strong>: Add the authentication header:
<ul>
<li>Header name: <code>Authorization</code></li>
<li>Header value: <code>Bearer &lt;your-project-api-key&gt;</code> (e.g., <code>Bearer phc_xxxxx...</code>)</li>
</ul>
</li>
</ul>
</li>
<li>Click <strong>Save</strong></li>
</ol>
<p><img src="/assets/upstream/images/workers-observability/posthog-example-destination-modal.png" alt="Cloudflare destination configuration for PostHog logs with destination name, type selection, OTLP endpoint, and custom headers" /></p>
<h2 id="step-4-configure-your-worker">Step 4: Configure your Worker</h2>
<p>With your destination created in the Cloudflare dashboard, update your Worker's configuration to enable logs export.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17049.md")
</div>
<p>After updating your configuration, deploy your Worker for the changes to take effect.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17047.md")
</aside>
<h2 id="step-5-view-logs-in-posthog">Step 5: View logs in PostHog</h2>
<p>Once your Worker is deployed and receiving traffic:</p>
<ol>
<li>Log in to your <a href="https://app.posthog.com/">PostHog account</a></li>
<li>Navigate to the <strong>Logs</strong> section in the left sidebar</li>
<li>Your Worker logs will appear with severity levels, timestamps, and attributes</li>
</ol>
<p>You can filter logs by:</p>
<ul>
<li><strong>Severity level</strong> (trace, debug, info, warn, error, fatal)</li>
<li><strong>Time range</strong></li>
<li><strong>Custom attributes</strong> added to your log entries</li>
<li><strong>Keywords</strong> in log messages</li>
</ul>
<h2 id="adding-custom-attributes-to-logs">Adding custom attributes to logs</h2>
<p>You can add custom attributes to your logs using standard <code>console</code> methods with structured data:</p>
<pre><code class="language-javascript">export default {&#10;  async fetch(request, env) {&#10;    // Basic logging&#10;    console.log(&quot;Processing request&quot;);&#10;&#10;    // Logs with additional context&#10;    console.info(&quot;User action&quot;, {&#10;      userId: &quot;user_123&quot;,&#10;      action: &quot;api_call&quot;,&#10;      path: new URL(request.url).pathname&#10;    });&#10;&#10;    // Error logging with details&#10;    console.error(&quot;Request failed&quot;, {&#10;      error: &quot;Connection timeout&quot;,&#10;      retryCount: 3&#10;    });&#10;&#10;    return new Response(&quot;OK&quot;);&#10;  }&#10;};&#10;</code></pre>
<p>These attributes will be searchable and filterable in the PostHog logs interface.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="logs-not-appearing-in-posthog">Logs not appearing in PostHog</h3>
<ol>
<li><strong>Verify your API key</strong>: Ensure you're using your project API key (starts with <code>phc_</code>), not a personal API key</li>
<li><strong>Check the endpoint region</strong>: Confirm you're using the correct regional endpoint (US or EU) matching your PostHog instance</li>
<li><strong>Confirm destination status</strong>: In the Cloudflare dashboard, verify your destination shows a recent successful delivery</li>
<li><strong>Check sampling rate</strong>: If you've configured a sampling rate, not all logs may be sent</li>
</ol>
<h3 id="authentication-errors">Authentication errors</h3>
<p>If you see authentication errors in your destination status:</p>
<ul>
<li>Ensure the Authorization header value includes <code>Bearer </code> prefix followed by your API key</li>
<li>Verify the API key has not been revoked or regenerated in PostHog</li>
<li>Alternatively, you can pass the token as a query parameter by using <code>https://us.i.posthog.com/i/v1/logs?token=&lt;your-project-api-key&gt;</code> as your endpoint</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://posthog.com/docs/logs">PostHog Logs documentation</a></li>
<li><a href="https://posthog.com/docs/logs/start-here">PostHog Getting Started with Logs</a></li>
<li><a href="https://opentelemetry.io/docs/specs/otel/logs/">OpenTelemetry Logs specification</a></li>
</ul>
