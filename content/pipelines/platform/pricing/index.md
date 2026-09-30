---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/platform/pricing/
  description: Cloudflare Pipelines pricing for SQL transforms, sinks, and included usage details.
  full_title: Cloudflare Pipelines - Pricing · Cloudflare Pipelines Docs
  head_html: <title>Cloudflare Pipelines - Pricing · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare Pipelines pricing for SQL transforms, sinks, and included usage details."><link rel="canonical" href="https://developers.cloudflare.com/pipelines/platform/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/platform/pricing/index.md"><meta property="og:title" content="Cloudflare Pipelines - Pricing · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare Pipelines pricing for SQL transforms, sinks, and included usage details."><meta property="og:url" content="https://developers.cloudflare.com/pipelines/platform/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/platform/pricing/#page","headline":"Cloudflare Pipelines - Pricing \u00b7 Cloudflare Pipelines Docs","description":"Cloudflare Pipelines pricing for SQL transforms, sinks, and included usage details.","url":"https://developers.cloudflare.com/pipelines/platform/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/platform/pricing/
  schema: 1
---
<p>Pipelines charges based on two dimensions:</p>
<ol>
<li><strong>SQL transforms</strong>: The volume of data processed by stateless SQL.</li>
<li><strong>Sinks</strong>: The volume of data delivered to each sink destination.</li>
</ol>
<p>Ingress into a Pipeline stream is free. Standard <a href="/r2/pricing/">R2 storage and operations</a> charges apply for data written to R2 buckets. <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges apply when writing to Iceberg tables.</p>
<p>All included usage is on a monthly basis.</p>
<h2 id="pipelines-pricing">Pipelines pricing</h2>
<table>
<thead>
<tr>
<th></th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Streams (ingress)</strong></td>
<td></td>
</tr>
<tr>
<td>Included</td>
<td>Unlimited</td>
</tr>
<tr>
<td><strong>SQL transforms</strong></td>
<td></td>
</tr>
<tr>
<td>Included</td>
<td>50 GB / month</td>
</tr>
<tr>
<td>Additional</td>
<td>$0.04 / GB</td>
</tr>
<tr>
<td><strong>Sinks (egress)</strong> <sup><a href="#footnote-1">1</a></sup></td>
<td></td>
</tr>
<tr>
<td>Included</td>
<td>50 GB / month</td>
</tr>
<tr>
<td>R2 — JSON format</td>
<td>$0.03 / GB</td>
</tr>
<tr>
<td>R2 — Parquet / Iceberg</td>
<td>$0.06 / GB</td>
</tr>
</tbody>
</table>
<h3 id="streams">Streams</h3>
<p>Streams provide durable, distributed log storage that buffers incoming messages. Ingress into a stream is free regardless of volume. A single stream can be read by multiple pipelines.</p>
<h3 id="sql-transforms">SQL transforms</h3>
<p>SQL transforms let you filter, reshape, and compute over data before it reaches a sink. Any query currently counts as a transform.</p>
<p>Pricing covers stateless transforms (for example, filter, reshape, unnest, cast, and compute). Future stateful operations such as aggregations, joins, and windows may be priced separately.</p>
<h3 id="sinks">Sinks</h3>
<p>Sink pricing is based on the volume of uncompressed data delivered to the destination. The rate varies by output format:</p>
<ul>
<li><strong>JSON</strong>: $0.03 / GB — lowest compute cost, suitable for simple log forwarding.</li>
<li><strong>Parquet / Iceberg</strong>: $0.06 / GB — higher compute cost for columnar encoding and Iceberg table management. Best for analytics workloads.</li>
</ul>
<h2 id="billing-examples">Billing examples</h2>
<h3 id="example-filtered-ingest-to-iceberg-with-sql">Example: filtered ingest to Iceberg with SQL</h3>
<p>A pipeline ingests 500 GB of event data per month. A SQL transform filters and reshapes the data, reducing output to 300 GB written to an R2 Data Catalog Iceberg table.</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Streams</td>
<td>500 GB</td>
<td>Unlimited</td>
<td>0 GB</td>
<td>$0.00</td>
</tr>
<tr>
<td>SQL transforms</td>
<td>500 GB</td>
<td>50 GB</td>
<td>450 GB</td>
<td>$18.00</td>
</tr>
<tr>
<td>Sinks (Iceberg)</td>
<td>300 GB</td>
<td>50 GB</td>
<td>250 GB</td>
<td>$15.00</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$33.00</strong></td>
</tr>
</tbody>
</table>
<h2 id="cloudflare-billing-policy">Cloudflare billing policy</h2>
<p>To learn more about how usage is billed, refer to <a href="/billing/understand/billing-policy/">Cloudflare Billing Policy</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Sink egress is measured on uncompressed data.</li></ol></section>
