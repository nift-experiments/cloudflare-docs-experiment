---
cp9:
  canonical: https://developers.cloudflare.com/r2-sql/query-data/
  description: Understand how to query data with R2 SQL
  full_title: Query data · R2 SQL docs
  head_html: <title>Query data · R2 SQL docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how to query data with R2 SQL"><link rel="canonical" href="https://developers.cloudflare.com/r2-sql/query-data/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-sql/query-data/index.md"><meta property="og:title" content="Query data · R2 SQL docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how to query data with R2 SQL"><meta property="og:url" content="https://developers.cloudflare.com/r2-sql/query-data/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 SQL"><meta name="algolia_product_filter" content="R2 SQL"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="R2 SQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-sql/query-data/#page","headline":"Query data \u00b7 R2 SQL docs","description":"Understand how to query data with R2 SQL","url":"https://developers.cloudflare.com/r2-sql/query-data/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2-sql/query-data/
  schema: 1
---
<p>Query <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>. R2 SQL queries can be made via <a href="/workers/wrangler/">Wrangler</a> or HTTP API.</p>
<h2 id="get-your-warehouse-name">Get your warehouse name</h2>
<p>To query data with R2 SQL, you need your warehouse name associated with your <a href="/r2-data-catalog/manage-catalogs/">catalog</a>. To retrieve it, you can run the <a href="/workers/wrangler/commands/r2/#r2-bucket-catalog-get"><code>r2 bucket catalog get</code> command</a>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 bucket catalog get &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>Alternatively, you can find it in the dashboard by going to the <strong>R2 object storage</strong> page, selecting the bucket, switching to the <strong>Settings</strong> tab, scrolling to <strong>R2 Data Catalog</strong>, and finding <strong>Warehouse name</strong>.</p>
<h2 id="query-via-wrangler">Query via Wrangler</h2>
<p>To begin, install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>. Then <a href="/workers/wrangler/install-and-update/">install Wrangler, the Developer Platform CLI</a>.</p>
<p>Wrangler needs an API token with permissions to access R2 Data Catalog, R2 storage, and R2 SQL to execute queries. The <code>r2 sql query</code> command looks for the token in the <code>WRANGLER_R2_SQL_AUTH_TOKEN</code> environment variable.</p>
<p>Set up your environment:</p>
<pre tabindex="0"><code class="language-bash">export WRANGLER_R2_SQL_AUTH_TOKEN=YOUR_API_TOKEN&#10;</code></pre>
<p>Or create a <code>.env</code> file with:</p>
<pre tabindex="0"><code>WRANGLER_R2_SQL_AUTH_TOKEN=YOUR_API_TOKEN&#10;</code></pre>
<p>Where <code>YOUR_API_TOKEN</code> is the token you created with the <a href="#authentication">required permissions</a>. For more information on setting environment variables, refer to <a href="/workers/wrangler/system-environment-variables/">Wrangler system environment variables</a>.</p>
<p>To run a SQL query, run the <a href="/workers/wrangler/commands/r2/#r2-sql-query"><code>r2 sql query</code> command</a>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 sql query &lt;WAREHOUSE&gt; &quot;SELECT * FROM namespace.table_name limit 10;&quot;&#10;</code></pre>
<p>For a full list of supported SQL commands, refer to the <a href="/r2-sql/sql-reference/">R2 SQL reference</a>.</p>
<h2 id="query-via-api">Query via API</h2>
<p>Below is an example of using R2 SQL via the REST endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST \&#10;  &quot;https://api.sql.cloudflarestorage.com/api/v1/accounts/{ACCOUNT_ID}/r2-sql/query/{BUCKET_NAME}&quot; \&#10;  &#45;H &quot;Authorization: Bearer ${WRANGLER_R2_SQL_AUTH_TOKEN}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;query&quot;: &quot;SELECT * FROM namespace.table_name limit 10;&quot;&#10;  }&#x27;&#10;</code></pre>
<p>The API requires an API token with the appropriate permissions in the Authorization header. Refer to <a href="#authentication">Authentication</a> for details on creating a token.</p>
<p>For a full list of supported SQL commands, refer to the <a href="/r2-sql/sql-reference/">R2 SQL reference</a>.</p>
<h2 id="authentication">Authentication</h2>
<p>To query data with R2 SQL, you must provide a Cloudflare API token with R2 SQL, R2 Data Catalog, and R2 storage permissions. R2 SQL requires these permissions to access catalog metadata and read the underlying data files stored in R2.</p>
<h3 id="create-api-token-in-the-dashboard">Create API token in the dashboard</h3>
<p>Create an <a href="/r2/api/tokens/#permissions">R2 API token</a> with the following permissions:</p>
<ul>
<li>Access to R2 Data Catalog (read-only)</li>
<li>Access to R2 storage (Admin read/write)</li>
<li>Access to R2 SQL (read-only)</li>
</ul>
<p>Use this token value for the <code>WRANGLER_R2_SQL_AUTH_TOKEN</code> environment variable when querying with Wrangler, or in the Authorization header when using the REST API.</p>
<h3 id="create-api-token-via-api">Create API token via API</h3>
<p>To create an API token programmatically for use with R2 SQL, you'll need to specify R2 SQL, R2 Data Catalog, and R2 storage permission groups in your <a href="/r2/api/tokens/#access-policy">Access Policy</a>.</p>
<h4 id="example-access-policy">Example Access Policy</h4>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;id&quot;: &quot;f267e341f3dd4697bd3b9f71dd96247f&quot;,&#10;		&quot;effect&quot;: &quot;allow&quot;,&#10;		&quot;resources&quot;: {&#10;			&quot;com.cloudflare.edge.r2.bucket.4793d734c0b8e484dfc37ec392b5fa8a_default_my-bucket&quot;: &quot;*&quot;,&#10;			&quot;com.cloudflare.edge.r2.bucket.4793d734c0b8e484dfc37ec392b5fa8a_eu_my-eu-bucket&quot;: &quot;*&quot;&#10;		},&#10;		&quot;permission_groups&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;f45430d92e2b4a6cb9f94f2594c141b8&quot;,&#10;				&quot;name&quot;: &quot;Workers R2 SQL Read&quot;&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;d229766a2f7f4d299f20eaa8c9b1fde9&quot;,&#10;				&quot;name&quot;: &quot;Workers R2 Data Catalog Write&quot;&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;bf7481a1826f439697cb59a20b22293e&quot;,&#10;				&quot;name&quot;: &quot;Workers R2 Storage Write&quot;&#10;			}&#10;		]&#10;	}&#10;]&#10;</code></pre>
<p>To learn more about how to create API tokens for R2 SQL using the API, including required permission groups and usage examples, refer to the <a href="/r2/api/tokens/#create-api-tokens-via-api">Create API tokens via API documentation</a>.</p>
<h2 id="additional-resources">Additional resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-manage-r2-data-catalogs-r2-data-catalog-manage-catalogs"><a href="/r2-data-catalog/manage-catalogs/">Manage R2 Data Catalogs</a></h3><p>Enable or disable R2 Data Catalog on your bucket, retrieve configuration details, and authenticate your Iceberg engine.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-build-an-end-to-end-data-pipeline-r2-sql-tutorials-end-to-end-pipeline"><a href="/r2-sql/tutorials/end-to-end-pipeline">Build an end to end data pipeline</a></h3><p>Detailed tutorial for setting up a simple fraud detection data pipeline, and generate events for it in Python.</p></div>
