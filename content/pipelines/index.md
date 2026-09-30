---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/
  description: Ingest, transform, and deliver streaming data to R2 as Apache Iceberg tables or Parquet and JSON files.
  full_title: Pipelines · Cloudflare Pipelines Docs
  head_html: <title>Pipelines · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Ingest, transform, and deliver streaming data to R2 as Apache Iceberg tables or Parquet and JSON files."><link rel="canonical" href="https://developers.cloudflare.com/pipelines/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/index.md"><meta property="og:title" content="Pipelines · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Ingest, transform, and deliver streaming data to R2 as Apache Iceberg tables or Parquet and JSON files."><meta property="og:url" content="https://developers.cloudflare.com/pipelines/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/pipelines/#page","headline":"Pipelines \u00b7 Cloudflare Pipelines Docs","description":"Ingest, transform, and deliver streaming data to R2 as Apache Iceberg tables or Parquet and JSON files.","url":"https://developers.cloudflare.com/pipelines/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/620.md")
</aside>
<div class="nb-description">
@markup("md", "content/.markup/bodies/621.md")
</div>
<div class="nb-plan">
<p>Available on Paid plans</p>
</div>
<p>Cloudflare Pipelines ingests events, transforms them with SQL, and delivers them to R2 as <a href="/r2-data-catalog/">Iceberg tables</a> or as Parquet and JSON files.</p>
<p>Whether you're processing server logs, mobile application events, IoT telemetry, or clickstream data, Pipelines provides durable ingestion via HTTP endpoints or Worker bindings, SQL-based transformations, and exactly-once delivery to R2. This makes it easy to build analytics-ready data warehouses and lakehouses without managing streaming infrastructure.</p>
<p>Create your first pipeline by following the <a href="/pipelines/getting-started">getting started guide</a> or running this <a href="/workers/wrangler/">Wrangler</a> command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pipelines setup&#10;</code></pre>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/622.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/623.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/624.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/625.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/626.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/627.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/628.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/632.md")
</div>
