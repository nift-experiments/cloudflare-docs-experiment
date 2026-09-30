---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/traces/
  description: Gain end-to-end visibility into request flows across your Workers application with automatic tracing instrumentation.
  full_title: Traces · Cloudflare Workers docs
  head_html: <title>Traces · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Gain end-to-end visibility into request flows across your Workers application with automatic tracing instrumentation."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/traces/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/traces/index.md"><meta property="og:title" content="Traces · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Gain end-to-end visibility into request flows across your Workers application with automatic tracing instrumentation."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/traces/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/observability/traces/#page","headline":"Traces \u00b7 Cloudflare Workers docs","description":"Gain end-to-end visibility into request flows across your Workers application with automatic tracing instrumentation.","url":"https://developers.cloudflare.com/workers/observability/traces/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/traces/
  schema: 1
---
<h3 id="what-is-workers-tracing">What is Workers tracing?</h3>
<p>Tracing gives you end-to-end visibility into the life of a request as it travels through your Workers application and connected services. This helps you identify performance bottlenecks, debug issues, and understand complex request flows. With tracing you can answer questions such as:</p>
<ul>
<li>What is the cause of a long-running request?</li>
<li>How long do subrequests from my Worker take?</li>
<li>How long are my calls to my KV Namespace or R2 bucket taking?</li>
</ul>
<p><img src="/assets/upstream/images/workers-observability/wobs_waterfall_trace_122.png" alt="Example trace showing a POST request to a cake shop with multiple spans including fetch requests and durable object operations" /></p>
<h3 id="automatic-instrumentation">Automatic instrumentation</h3>
<p>Cloudflare Workers provides tracing instrumentation <strong>out of the box</strong> — no code changes or SDK are required. Simply enable tracing on your Worker and Cloudflare automatically captures telemetry data for:</p>
<ul>
<li><strong>Fetch calls</strong> — All outbound HTTP requests, capturing timing, status codes, and request metadata. This enables you to quickly identify how external dependencies affect your application's performance.</li>
<li><strong>Binding calls</strong> — Interactions with various Worker bindings such as KV reads and writes, R2 object storage operations and Durable Object invocations.</li>
<li><strong>RPC calls</strong> — Calls between Workers and Durable Objects, including caller-side session spans and individual method-call spans.</li>
<li><strong>Handler calls</strong> — The complete lifecycle of each Worker invocation, including triggers such as <a href="/workers/runtime-apis/handlers/fetch/">fetch handlers</a>,
<a href="/workers/runtime-apis/handlers/scheduled/">scheduled handlers</a>, and <a href="/queues/configuration/javascript-apis/#consumer">queue handlers</a>.</li>
</ul>
<p>For a full list of instrumented operations, refer to the <a href="/workers/observability/traces/spans-and-attributes/">spans and attributes documentation</a>.</p>
<h3 id="custom-spans">Custom spans</h3>
<p>You can also create your own spans to trace application-specific logic. Custom spans nest automatically with the built-in instrumentation, giving you end-to-end visibility across both platform operations and your own code.</p>
<p>For more information, refer to <a href="/workers/observability/traces/custom-spans/">Custom spans</a>.</p>
<h3 id="how-to-enable-tracing">How to enable tracing</h3>
<p>You can configure tracing by setting <code>observability.traces.enabled = true</code> in your <a href="/workers/wrangler/configuration/#observability">Wrangler configuration file</a>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17020.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17019.md")
</aside>
<h3 id="exporting-opentelemetry-traces-to-a-3rd-party-destination">Exporting OpenTelemetry traces to a 3rd party destination</h3>
<p>Workers tracing follows <a href="https://opentelemetry.io/">OpenTelemetry (OTel) standards</a>. This makes it compatible with popular observability platforms,
such as <a href="/workers/observability/exporting-opentelemetry-data/honeycomb/">Honeycomb</a>, <a href="/workers/observability/exporting-opentelemetry-data/grafana-cloud/">Grafana Cloud</a>, and
<a href="/workers/observability/exporting-opentelemetry-data/axiom/">Axiom</a>, while requiring zero development effort from you. If your observability provider has an available OpenTelemetry endpoint, you can export traces (and logs)!</p>
<p>You can also set <code>persist: false</code> to export traces to your destination without persisting them in the Cloudflare dashboard. This allows you to use a third-party observability provider as your sole traces destination.</p>
<p>Learn more about exporting OpenTelemetry data from Workers <a href="/workers/observability/exporting-opentelemetry-data/">here</a>.</p>
<h3 id="sampling">Sampling</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="default-sampling-rate">Default Sampling Rate</h3>
@markup("md", "content/.markup/bodies/17018.md")
</aside>
<p>With sampling, you can trace a percentage of incoming requests in your Cloudflare Worker.
This allows you to manage volume and costs, while still providing meaningful insights into your application.</p>
<p>The valid sampling range is from <code>0</code> to <code>1</code>, where <code>0</code> indicates zero out of one hundred invocations will be traced, and <code>1</code> indicates every requests will be traced,
and a number such a <code>0.05</code> indicates five out of one hundred requests will be traced.</p>
<p>If you have not specified a sampling rate, it defaults to <code>1</code>, meaning 100% of requests will be traced.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17021.md")
</div>
<p>If you have <code>head_sampling_rate</code> configured for logs, you can also create a separate rate for traces.</p>
<p>Sampling is <a href="https://opentelemetry.io/docs/concepts/sampling/#head-sampling">head-based</a>, meaning that non-traced requests do not incur any tracing overhead.</p>
<h3 id="limits-pricing">Limits &amp; Pricing</h3>
<p>Workers tracing is currently <strong>free</strong> during the initial beta period. This includes all tracing functionality such as collecting traces, storing them, and viewing them in the Cloudflare dashboard.</p>
<p>Starting on October 1, 2026, tracing will be billed as part of your usage on the Workers Free Paid and Enterprise plans. Each span in a trace represents one observability event, sharing the same monthly quota and pricing as <a href="/workers/platform/pricing/#workers-logs">Workers logs</a>:</p>
<table>
<thead>
<tr>
<th></th>
<th>Events (trace spans or log events)</th>
<th>Retention</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers Free</strong></td>
<td>200,000 per day</td>
<td>3 Days</td>
</tr>
<tr>
<td><strong>Workers Paid</strong></td>
<td>20 million included per month +$0.60 per additional million events</td>
<td>7 Days</td>
</tr>
</tbody>
</table>
