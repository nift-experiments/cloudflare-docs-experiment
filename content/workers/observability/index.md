---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/
  description: Understand how your Worker projects are performing via logs, traces, metrics, and other data sources.
  full_title: Observability · Cloudflare Workers docs
  head_html: <title>Observability · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how your Worker projects are performing via logs, traces, metrics, and other data sources."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/index.md"><meta property="og:title" content="Observability · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how your Worker projects are performing via logs, traces, metrics, and other data sources."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/observability/#page","headline":"Observability \u00b7 Cloudflare Workers docs","description":"Understand how your Worker projects are performing via logs, traces, metrics, and other data sources.","url":"https://developers.cloudflare.com/workers/observability/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/
  schema: 1
---
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
