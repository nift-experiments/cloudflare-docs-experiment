---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/sentry/
  description: Export OpenTelemetry traces and logs from Cloudflare Workers to Sentry for monitoring and debugging.
  full_title: Export to Sentry · Cloudflare Workers docs
  head_html: <title>Export to Sentry · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Export OpenTelemetry traces and logs from Cloudflare Workers to Sentry for monitoring and debugging."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/sentry/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/sentry/index.md"><meta property="og:title" content="Export to Sentry · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Export OpenTelemetry traces and logs from Cloudflare Workers to Sentry for monitoring and debugging."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/sentry/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/sentry/#page","headline":"Export to Sentry \u00b7 Cloudflare Workers docs","description":"Export OpenTelemetry traces and logs from Cloudflare Workers to Sentry for monitoring and debugging.","url":"https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/sentry/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/exporting-opentelemetry-data/sentry/
  schema: 1
---
<p>Sentry is a software monitoring tool that helps developers identify and debug performance issues and errors. From end-to-end distributed tracing to performance monitoring, Sentry provides code-level observability that makes it easy to diagnose issues and learn continuously about your application code health across systems and services. By exporting your Cloudflare Workers application telemetry to Sentry, you can:</p>
<ul>
<li>Query logs and traces in Sentry</li>
<li>Create custom alerts and dashboards to monitor your Workers</li>
</ul>
<p><img src="/assets/upstream/images/workers-observability/sentry-example.png" alt="Sentry trace view with timing information displayed on a timeline" /></p>
<p>This guide will walk you through exporting OpenTelemetry-compliant traces and logs to Sentry from your Cloudflare Worker application</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, ensure you have:</p>
<ul>
<li>Are signed up for a <a href="https://sentry.io/signup/">Sentry account</a> (free tier available)</li>
<li>A deployed Worker that you want to monitor</li>
</ul>
<h2 id="step-1-create-a-sentry-project">Step 1: Create a Sentry project</h2>
<p>If you don't already have a Sentry project to send data to, you'll need to create one to start sending Cloudflare Workers application telemetry to Sentry.</p>
<ol>
<li>Log in to your <a href="https://sentry.io/">Sentry account</a></li>
<li>Navigate to the Insights &gt; Projects in the navigation sidebar, which will open a list of your projects.</li>
<li>Click <a href="https://sentry.io/orgredirect/organizations/:orgslug/insights/projects/new/"><strong>New Project</strong></a></li>
<li>Fill out the project creation form and click <strong>Create Project</strong> to complete the process.</li>
</ol>
<h2 id="step-2-get-your-sentry-otlp-endpoints">Step 2: Get your Sentry OTLP endpoints</h2>
<p>Sentry provides separate OTLP endpoints for traces and logs which you can use to send your telemetry data to Sentry.</p>
<ul>
<li><strong>Traces</strong>: <code>https://{HOST}/api/{PROJECT_ID}/integration/otlp/v1/traces</code></li>
<li><strong>Logs</strong>: <code>https://{HOST}/api/{PROJECT_ID}/integration/otlp/v1/logs</code></li>
</ul>
<p>You can find your OTLP endpoints in the your project settings.</p>
<ol>
<li>Go to the <a href="https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/">Settings &gt; Projects</a> page in Sentry.</li>
<li>Select your project from the list and click on the project name to open the project settings.</li>
<li>Go to the &quot;Client Keys (DSN)&quot; sub-page for this project under the &quot;SDK Setup&quot; heading.</li>
</ol>
<p>There you'll find your Sentry project's OTLP logs and OTLP traces endpoints, as well as authentication headers for the endpoints. Make sure to copy the endpoints and authentication headers.</p>
<p>For more details on how to use Sentry's OTLP endpoints, refer to <a href="https://docs.sentry.io/concepts/otlp/">Sentry's OTLP documentation</a>.</p>
<h2 id="step-3-set-up-destination-in-the-cloudflare-dashboard">Step 3: Set up destination in the Cloudflare dashboard</h2>
<p>To set up a destination in the Cloudflare dashboard, navigate to your Cloudflare account's <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/pipelines">Workers Observability</a> section. Then click <strong>Add destination</strong> and configure either a traces or logs destination.</p>
<h3 id="traces-destination">Traces Destination</h3>
<p>To configure your traces destination, click <strong>Add destination</strong> and configure the following:</p>
<ul>
<li><strong>Destination Name</strong>: <code>sentry-traces</code> (or any descriptive name)</li>
<li><strong>Destination Type</strong>: Select <strong>Traces</strong></li>
<li><strong>OTLP Endpoint</strong>: Your Sentry OTLP traces endpoint (e.g., <code>https://{HOST}/api/{PROJECT_ID}/integration/otlp/v1/traces</code>)</li>
<li><strong>Custom Headers</strong>: Add the Sentry authentication header:
<ul>
<li>Header name: <code>x-sentry-auth</code></li>
<li>Header value: <code>sentry sentry_key={SENTRY_PUBLIC_KEY}</code> where <code>{SENTRY_PUBLIC_KEY}</code> is your Sentry project's public key</li>
</ul>
</li>
</ul>
<h3 id="logs-destination">Logs destination</h3>
<p>To configure your logs destination, click <strong>Add destination</strong> and configure the following:</p>
<ul>
<li><strong>Destination Name</strong>: <code>sentry-logs</code> (or any descriptive name)</li>
<li><strong>Destination Type</strong>: Select <strong>Logs</strong></li>
<li><strong>OTLP Endpoint</strong>: Your Sentry OTLP logs endpoint (e.g., <code>https://{HOST}/api/{PROJECT_ID}/integration/otlp/v1/logs</code>)</li>
<li><strong>Custom Headers</strong>: Add the Sentry authentication header:
<ul>
<li>Header name: <code>x-sentry-auth</code></li>
<li>Header value: <code>sentry sentry_key={SENTRY_PUBLIC_KEY}</code> where <code>{SENTRY_PUBLIC_KEY}</code> is your Sentry project's public key</li>
</ul>
</li>
</ul>
<h2 id="step-4-configure-your-worker">Step 4: Configure your Worker</h2>
<p>With your destinations created in the Cloudflare dashboard, update your Worker's configuration to enable telemetry export.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17046.md")
</div>
<p>After updating your configuration, deploy your Worker for the changes to take effect.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17045.md")
</aside>
