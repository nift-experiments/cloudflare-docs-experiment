---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/
  description: Push Cloudflare logs to Cloudflare Pipelines.
  full_title: Enable Cloudflare Pipelines · Cloudflare Logs docs
  head_html: <title>Enable Cloudflare Pipelines · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Push Cloudflare logs to Cloudflare Pipelines."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/index.md"><meta property="og:title" content="Enable Cloudflare Pipelines · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Push Cloudflare logs to Cloudflare Pipelines."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush,Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/#page","headline":"Enable Cloudflare Pipelines \u00b7 Cloudflare Logs docs","description":"Push Cloudflare logs to Cloudflare Pipelines.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/pipelines/
  schema: 1
---
<p><a href="/pipelines/">Cloudflare Pipelines</a> ingests events, transforms them with <a href="/pipelines/sql-reference/">SQL</a>, and delivers them to <a href="/r2/">R2</a> as <a href="/r2-data-catalog/">Iceberg</a> tables or as Parquet and JSON files. Logpush can write data to Pipelines as a native destination.</p>
<p>Instead of sending raw logs directly to a storage bucket as JSON, Logpush can route them to a Pipeline to filter, enrich, and transform your data into Parquet or Apache Iceberg tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>. This allows the data to be much more compact and optimized for analytics such as querying with <a href="/r2-sql/">R2 SQL</a>.</p>
<p>The Pipelines destination supports the following Logpush datasets:</p>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Datasets</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zone</td>
<td><code>http_requests</code>, <code>firewall_events</code>, <code>dns_logs</code></td>
</tr>
<tr>
<td>Account</td>
<td><code>workers_trace_events</code></td>
</tr>
</tbody>
</table>
<p>For a full list of fields available in each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Datasets</a>.</p>
<h2 id="manage-via-the-cloudflare-dashboard">Manage via the Cloudflare dashboard</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/10549.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10548.md")
</aside>
