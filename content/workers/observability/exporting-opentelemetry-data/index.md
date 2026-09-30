---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/
  description: Export traces and logs from Cloudflare Workers to any OpenTelemetry-compatible destination.
  full_title: Exporting OpenTelemetry Data · Cloudflare Workers docs
  head_html: <title>Exporting OpenTelemetry Data · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Export traces and logs from Cloudflare Workers to any OpenTelemetry-compatible destination."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/index.md"><meta property="og:title" content="Exporting OpenTelemetry Data · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Export traces and logs from Cloudflare Workers to any OpenTelemetry-compatible destination."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/#page","headline":"Exporting OpenTelemetry Data \u00b7 Cloudflare Workers docs","description":"Export traces and logs from Cloudflare Workers to any OpenTelemetry-compatible destination.","url":"https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/exporting-opentelemetry-data/
  schema: 1
---
<p>Cloudflare Workers supports exporting OpenTelemetry (OTel)-compliant telemetry data to any destination with an available OTel endpoint, allowing you to integrate with your existing monitoring and observability stack.</p>
<h3 id="supported-telemetry-types">Supported telemetry types</h3>
<p>You can export the following types of telemetry data:</p>
<ul>
<li><strong>Traces</strong> - Traces showing request flows through your Worker and connected services</li>
<li><strong>Logs</strong> - Application logs including <code>console.log()</code> output and system-generated logs</li>
</ul>
<p><strong>Note</strong>: exporting Worker metrics and custom metrics is not yet supported.</p>
<h3 id="available-opentelemetry-destinations">Available OpenTelemetry destinations</h3>
<p>Below are common OTLP endpoint formats for popular observability providers. Refer to your provider's documentation for specific details and authentication requirements.</p>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Traces Endpoint</th>
<th>Logs Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/observability/exporting-opentelemetry-data/honeycomb/"><strong>Honeycomb</strong></a></td>
<td><code>https://api.honeycomb.io/v1/traces</code></td>
<td><code>https://api.honeycomb.io/v1/logs</code></td>
</tr>
<tr>
<td><a href="/workers/observability/exporting-opentelemetry-data/grafana-cloud/"><strong>Grafana Cloud</strong></a></td>
<td><code>https://otlp-gateway-{region}.grafana.net/otlp/v1/traces</code></td>
<td><code>https://otlp-gateway-{region}.grafana.net/otlp/v1/logs</code>[^1]</td>
</tr>
<tr>
<td><a href="https://docs.firetiger.com/ingest/cloudflare-workers.html"><strong>Firetiger</strong></a></td>
<td><code>https://ingest.cloud.firetiger.com/v1/traces</code></td>
<td><code>https://ingest.cloud.firetiger.com/v1/logs</code></td>
</tr>
<tr>
<td><a href="/workers/observability/exporting-opentelemetry-data/axiom/"><strong>Axiom</strong></a></td>
<td><code>https://api.axiom.co/v1/traces</code></td>
<td><code>https://api.axiom.co/v1/logs</code></td>
</tr>
<tr>
<td><a href="/workers/observability/exporting-opentelemetry-data/sentry/"><strong>Sentry</strong></a></td>
<td><code>https://{HOST}/api/{PROJECT_ID}/integration/otlp/v1/traces</code></td>
<td><code>https://{HOST}/api/{PROJECT_ID}/integration/otlp/v1/logs</code></td>
</tr>
<tr>
<td><a href="https://sematext.com/docs/guide/managed-otlp-endpoint/"><strong>Sematext</strong></a></td>
<td><code>https://otlp-receiver.sematext.com</code> (US), <code>https://otlp-receiver.eu.sematext.com</code> (EU)</td>
<td><code>https://otlp-receiver.sematext.com</code> (US), <code>https://otlp-receiver.eu.sematext.com</code> (EU)</td>
</tr>
<tr>
<td><a href="/workers/observability/exporting-opentelemetry-data/posthog/"><strong>PostHog</strong></a></td>
<td>Not supported</td>
<td><code>https://{REGION}.i.posthog.com/i/v1/logs</code></td>
</tr>
<tr>
<td><a href="https://docs.datadoghq.com/opentelemetry/setup/otlp_ingest/managed_platforms/"><strong>Datadog</strong></a></td>
<td><code>https://cloudflare.integrations.otlp.{DD_SITE}/v1/traces</code></td>
<td><code>https://cloudflare.integrations.otlp.{DD_SITE}/v1/logs</code></td>
</tr>
<tr>
<td><a href="https://docs.newrelic.com/docs/opentelemetry/best-practices/opentelemetry-otlp/"><strong>New Relic</strong></a></td>
<td><code>https://otlp.nr-data.net/v1/traces</code></td>
<td><code>https://otlp.nr-data.net/v1/logs</code></td>
</tr>
<tr>
<td><a href="https://dev.splunk.com/observability/reference/api/ingest_data/latest"><strong>Splunk Observability</strong></a></td>
<td><code>https://ingest.{REALM}.signalfx.com/v2/trace/otlp</code></td>
<td>N/A</td>
</tr>
<tr>
<td><a href="https://github.com/splunk/splunk-connect-for-otlp"><strong>Splunk Platform</strong></a></td>
<td><code>http://splunk.internal:4318/v1/traces</code></td>
<td><code>http://splunk.internal:4318/v1/logs</code></td>
</tr>
<tr>
<td><a href="https://signoz.io/docs/integrations/outposts/cloudflare-workers/"><strong>SigNoz</strong></a></td>
<td><code>https://ingest.&lt;region&gt;.signoz.cloud:443/v1/traces</code></td>
<td><code>https://ingest.&lt;region&gt;.signoz.cloud:443/v1/logs</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="authentication">Authentication</h3>
@markup("md", "content/.markup/bodies/17052.md")
</aside>
<h2 id="setting-up-opentelemetry-compatible-destinations">Setting up OpenTelemetry-compatible destinations</h2>
<p>To start sending data to your destination, you'll need to create a destination in the Cloudflare dashboard.</p>
<h3 id="creating-a-destination">Creating a destination</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="protocol">Protocol</h3>
@markup("md", "content/.markup/bodies/17051.md")
</aside>
<p><img src="/assets/upstream/images/workers-observability/destinations.png" alt="Observability Destinations dashboard showing configured destinations for Grafana and Honeycomb with their respective endpoints and status" /></p>
<ol>
<li>Head to your account's <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/pipelines">Workers Observability</a> section of the dashboard</li>
<li>Click add destination.</li>
<li>Configure your destination:
<ul>
<li><strong>Destination Name</strong> - A descriptive name (e.g., &quot;Grafana-tracing&quot;, &quot;Honeycomb-Logs&quot;)</li>
<li><strong>Destination Type</strong> - Choose between &quot;Traces&quot; or &quot;Logs&quot;</li>
<li><strong>OTLP Endpoint</strong> - The URL where your observability platform accepts OTLP data.</li>
<li><strong>Custom Headers</strong> (Optional) - Any authentication headers or other provider-required headers</li>
</ul>
</li>
<li>Save your destination</li>
</ol>
<p><img src="/assets/upstream/images/workers-observability/destination-setup.png" alt="Edit Destination dialog showing configuration for Honeycomb tracing with destination name, type selection, OTLP endpoint, and custom headers" /></p>
<h2 id="enabling-opentelemetry-export-for-your-worker">Enabling OpenTelemetry export for your Worker</h2>
<p>After setting up destinations in the dashboard, configure your Worker to export telemetry data by updating your Wrangler configuration. Your destination name configured in your configuration file should be the same as the destination configured in the dashboard.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17053.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="persist-and-pricing">`persist` and pricing</h3>
@markup("md", "content/.markup/bodies/17050.md")
</aside>
<p>Once you've configured your Wrangler configuration file, redeploy your Worker for new configurations to take effect. Note that it may take a few minutes for events to reach your destination.</p>
<h2 id="destination-status">Destination status</h2>
<p>After creating a destination, you can monitor its health and delivery status in the Cloudflare dashboard. Each destination displays a status indicator that shows how recently data was successfully delivered.</p>
<h3 id="status-indicators">Status indicators</h3>
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
<th>Troubleshooting</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Last: n minutes ago</strong></td>
<td>Data was recently delivered successfully.</td>
<td></td>
</tr>
<tr>
<td><strong>Never run</strong></td>
<td>No data has been delivered to this destination.</td>
<td>•Check if your Worker is receiving traffic <br /> • Review sampling rates (low rates generate less data)<br /></td>
</tr>
<tr>
<td><strong>Error</strong></td>
<td>An error occurred while attempting to deliver data to this destination.</td>
<td>• Verify OTLP endpoint URL is correct<br />• Check authentication headers are valid<br /></td>
</tr>
</tbody>
</table>
<h2 id="limits-and-pricing">Limits and pricing</h2>
<p>Exporting OTel data is currently <strong>free</strong> to those currently on a Workers Paid subscription or higher during the early beta period. However, starting on <strong><code>October 1, 2026</code></strong>, tracing will be billed as part of your usage on the Workers Paid plan or contract.</p>
<p>This includes the following limits and pricing:</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Traces</th>
<th>Logs</th>
<th>Pricing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers Free</strong></td>
<td>Not available</td>
<td>Not available</td>
<td>-</td>
</tr>
<tr>
<td><strong>Workers Paid</strong></td>
<td>10 million events per month included</td>
<td>10 million events per month included</td>
<td>$0.05 per million additional events</td>
</tr>
</tbody>
</table>
<h2 id="known-limitations">Known limitations</h2>
<p>OpenTelemetry data export is currently in beta. Please be aware of the following limitations:</p>
<ul>
<li><strong>Metrics export not yet supported</strong>: Exporting Worker infrastructure metrics and custom metrics via OpenTelemetry is not currently available. We are actively working to add metrics support in the future.</li>
<li><strong>Limited OTLP support from some providers</strong>: Some observability providers are still rolling out OTLP endpoint support. Check the <a href="#available-opentelemetry-destinations">Available OpenTelemetry destinations</a> table above for current availability.</li>
</ul>
