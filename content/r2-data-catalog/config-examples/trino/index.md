---
cp9:
  canonical: https://developers.cloudflare.com/r2-data-catalog/config-examples/trino/
  description: Connect Trino to R2 Data Catalog using the Iceberg REST catalog connector.
  full_title: Trino · Cloudflare R2 Data Catalog docs
  head_html: <title>Trino · Cloudflare R2 Data Catalog docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Trino to R2 Data Catalog using the Iceberg REST catalog connector."><link rel="canonical" href="https://developers.cloudflare.com/r2-data-catalog/config-examples/trino/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-data-catalog/config-examples/trino/index.md"><meta property="og:title" content="Trino · Cloudflare R2 Data Catalog docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Trino to R2 Data Catalog using the Iceberg REST catalog connector."><meta property="og:url" content="https://developers.cloudflare.com/r2-data-catalog/config-examples/trino/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 Data Catalog"><meta name="algolia_product_filter" content="R2 Data Catalog"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="R2 Data Catalog"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-data-catalog/config-examples/trino/#page","headline":"Trino \u00b7 Cloudflare R2 Data Catalog docs","description":"Connect Trino to R2 Data Catalog using the Iceberg REST catalog connector.","url":"https://developers.cloudflare.com/r2-data-catalog/config-examples/trino/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2-data-catalog/config-examples/trino/
  schema: 1
---
<p>Below is an example of using <a href="https://trino.io/">Trino</a> to connect to R2 Data Catalog. For more information on connecting to R2 Data Catalog with Trino, refer to <a href="https://trino.io/docs/current/connector/iceberg.html">Trino documentation</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li><a href="/r2/buckets/create-buckets/">Create an R2 bucket</a> and <a href="/r2-data-catalog/manage-catalogs/#enable-r2-data-catalog-on-a-bucket">enable the data catalog</a>.</li>
<li><a href="/r2/api/tokens/">Create an R2 API token, key, and secret</a> with both <a href="/r2/api/tokens/#permissions">R2 and data catalog permissions</a>.</li>
<li>Install <a href="https://docs.docker.com/get-docker/">Docker</a> to run the Trino container.</li>
</ul>
<h2 id="setup">Setup</h2>
<p>Create a local directory for the catalog configuration and change directories to it</p>
<pre tabindex="0"><code class="language-bash">mkdir -p trino-catalog &amp;&amp; cd trino-catalog/&#10;</code></pre>
<p>Create a configuration file called <code>r2.properties</code> for your R2 Data Catalog connection:</p>
<pre tabindex="0"><code class="language-properties">&#35; r2.properties&#10;connector.name=iceberg&#10;&#10;&#35; R2 Configuration&#10;fs.native-s3.enabled=true&#10;s3.region=auto&#10;s3.aws-access-key=&lt;Your R2 access key&gt;&#10;s3.aws-secret-key=&lt;Your R2 secret&gt;&#10;s3.endpoint=&lt;Your R2 endpoint&gt;&#10;s3.path-style-access=true&#10;&#10;&#35; R2 Data Catalog Configuration&#10;iceberg.catalog.type=rest&#10;iceberg.rest-catalog.uri=&lt;Your R2 Data Catalog URI&gt;&#10;iceberg.rest-catalog.warehouse=&lt;Your R2 Data Catalog warehouse&gt;&#10;iceberg.rest-catalog.security=OAUTH2&#10;iceberg.rest-catalog.oauth2.token=&lt;Your R2 authentication token&gt;&#10;</code></pre>
<h2 id="example-usage">Example usage</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11321.md")
</div>
