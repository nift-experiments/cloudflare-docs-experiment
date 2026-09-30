---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/axiom/
  description: Send OpenTelemetry traces and logs from Cloudflare Workers to Axiom.
  full_title: Export to Axiom · Cloudflare Workers docs
  head_html: <title>Export to Axiom · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Send OpenTelemetry traces and logs from Cloudflare Workers to Axiom."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/axiom/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/axiom/index.md"><meta property="og:title" content="Export to Axiom · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send OpenTelemetry traces and logs from Cloudflare Workers to Axiom."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/axiom/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/axiom/#page","headline":"Export to Axiom \u00b7 Cloudflare Workers docs","description":"Send OpenTelemetry traces and logs from Cloudflare Workers to Axiom.","url":"https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/axiom/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/exporting-opentelemetry-data/axiom/
  schema: 1
---
<p>Axiom is a serverless log analytics platform that helps you store, search, and analyze massive amounts of data. By exporting your Cloudflare Workers application telemetry to Axiom, you can:</p>
<ul>
<li>Store and query logs and traces at scale</li>
<li>Create dashboards and alerts to monitor your Workers</li>
</ul>
<p><img src="/assets/upstream/images/workers-observability/axiom-example.png" alt="Trace view with timing information displayed on a timeline" /></p>
<p>This guide will walk you through exporting OpenTelemetry-compliant traces and logs to Axiom from your Cloudflare Worker application</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, ensure you have:</p>
<ul>
<li>An active <a href="https://app.axiom.co/register">Axiom account</a> (free tier available)</li>
<li>A deployed Worker that you want to monitor</li>
<li>An Axiom dataset to send data to</li>
</ul>
<h2 id="step-1-create-a-dataset">Step 1: Create a dataset</h2>
<p>If you don't already have a dataset to send data to:</p>
<ol>
<li>Log in to your <a href="https://app.axiom.co/">Axiom account</a></li>
<li>Navigate to <strong>Datasets</strong> in the left sidebar</li>
<li>Click <strong>New Dataset</strong></li>
<li>Enter a name (e.g. <code>cloudflare-workers-otel</code>)</li>
<li>Click <strong>Create Dataset</strong></li>
</ol>
<h2 id="step-2-get-your-axiom-api-token-and-dataset">Step 2: Get your Axiom API token and dataset</h2>
<ol>
<li>Navigate to <strong>Settings</strong> in the left sidebar</li>
<li>Click on <strong>API Tokens</strong></li>
<li>Click <strong>Create API Token</strong></li>
<li>Configure your API token:
<ul>
<li><strong>Name</strong>: Enter a descriptive name (e.g., <code>cloudflare-workers-otel</code>)</li>
<li><strong>Permissions</strong>: Select <strong>Ingest</strong> permission (required for sending telemetry data)</li>
<li><strong>Datasets</strong>: Choose which datasets this token can write to, or select <strong>All Datasets</strong></li>
</ul>
</li>
<li>Click <strong>Create</strong></li>
<li><strong>Important</strong>: Copy the API token immediately and store it securely - you won't be able to see it again</li>
</ol>
<p>The API token will look something like: <code>xaat-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx</code></p>
<h2 id="step-3-configure-cloudflare-destinations">Step 3: Configure Cloudflare destinations</h2>
<p>Now you'll create destinations in the Cloudflare dashboard that point to Axiom.</p>
<h3 id="axiom-otlp-endpoints">Axiom OTLP endpoints</h3>
<p>Axiom provides separate OTLP endpoints for traces and logs:</p>
<ul>
<li><strong>Traces</strong>: <code>https://api.axiom.co/v1/traces</code></li>
<li><strong>Logs</strong>: <code>https://api.axiom.co/v1/logs</code></li>
</ul>
<h3 id="configure-trace-or-logs-destination">Configure trace or logs destination</h3>
<ol>
<li>Navigate to your Cloudflare account's <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/pipelines">Workers Observability</a> section</li>
<li>Click <strong>Add destination</strong></li>
<li>Configure your trace destination:
<ul>
<li><strong>Destination Name</strong>: <code>axiom-traces</code> (or any descriptive name)</li>
<li><strong>Destination Type</strong>: Select <strong>Traces</strong></li>
<li><strong>OTLP Endpoint</strong>: <code>https://api.axiom.co/v1/traces</code> (or <code>/v1/logs</code>)</li>
<li><strong>Custom Headers</strong>: Add two required headers:
<ul>
<li>Authentication header
<ul>
<li>Header name: <code>Authorization</code></li>
<li>Header value: <code>Bearer &lt;your-api-token&gt;</code></li>
</ul>
</li>
<li>Dataset header:
<ul>
<li>Header name: <code>X-Axiom-Dataset</code></li>
<li>Header value: Your dataset name (e.g., <code>cloudflare-workers-otel</code>)</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>Click <strong>Save</strong></li>
</ol>
<h2 id="step-3-configure-your-worker">Step 3: Configure your Worker</h2>
<p>With your destinations created in the Cloudflare dashboard, update your Worker's configuration to enable telemetry export.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17059.md")
</div>
<p>After updating your configuration, deploy your Worker for the changes to take effect.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17058.md")
</aside>
