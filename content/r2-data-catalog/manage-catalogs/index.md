---
cp9:
  canonical: https://developers.cloudflare.com/r2-data-catalog/manage-catalogs/
  description: Understand how to manage Iceberg REST catalogs associated with R2 buckets
  full_title: Manage catalogs · Cloudflare R2 Data Catalog docs
  head_html: <title>Manage catalogs · Cloudflare R2 Data Catalog docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how to manage Iceberg REST catalogs associated with R2 buckets"><link rel="canonical" href="https://developers.cloudflare.com/r2-data-catalog/manage-catalogs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-data-catalog/manage-catalogs/index.md"><meta property="og:title" content="Manage catalogs · Cloudflare R2 Data Catalog docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how to manage Iceberg REST catalogs associated with R2 buckets"><meta property="og:url" content="https://developers.cloudflare.com/r2-data-catalog/manage-catalogs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 Data Catalog"><meta name="algolia_product_filter" content="R2 Data Catalog"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="R2 Data Catalog"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-data-catalog/manage-catalogs/#page","headline":"Manage catalogs \u00b7 Cloudflare R2 Data Catalog docs","description":"Understand how to manage Iceberg REST catalogs associated with R2 buckets","url":"https://developers.cloudflare.com/r2-data-catalog/manage-catalogs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2-data-catalog/manage-catalogs/
  schema: 1
---
<p>Learn how to:</p>
<ul>
<li>Enable and disable <a href="/r2-data-catalog/">R2 Data Catalog</a> on your buckets.</li>
<li>Enable and disable <a href="/r2-data-catalog/table-maintenance/">table maintenance</a> features like compaction and snapshot expiration.</li>
<li>Authenticate Iceberg engines using API tokens.</li>
</ul>
<h2 id="enable-r2-data-catalog-on-a-bucket">Enable R2 Data Catalog on a bucket</h2>
<p>Enabling the catalog on a bucket turns on the REST catalog interface and provides a <strong>Catalog URI</strong> and <strong>Warehouse name</strong> required by Iceberg clients. Once enabled, you can create and manage Iceberg tables in that bucket.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/536.md")
</div></div>
<h2 id="disable-r2-data-catalog-on-a-bucket">Disable R2 Data Catalog on a bucket</h2>
<p>When you disable the catalog on a bucket, it immediately stops serving requests from the catalog interface. Any Iceberg table references stored in that catalog become inaccessible until you re-enable it.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/540.md")
</div></div>
<h2 id="enable-compaction">Enable compaction</h2>
<p>Compaction improves query performance by combining the many small files created during data ingestion into fewer, larger files according to the set <code>target file size</code>. For more information about compaction and why it is valuable, refer to <a href="/r2-data-catalog/table-maintenance/">About compaction</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="api-token-permission-requirements">API token permission requirements</h3>
@markup("md", "content/.markup/bodies/532.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/544.md")
</div></div>
<p>Once enabled, compaction applies retroactively to all existing tables (for catalog-level compaction) or the specified table (for table-level compaction).</p>
<h2 id="disable-compaction">Disable compaction</h2>
<p>Disabling compaction will prevent the process from running for all tables (catalog level) or a specific table (table level). You can re-enable it at any time.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/548.md")
</div></div>
<h2 id="enable-snapshot-expiration">Enable snapshot expiration</h2>
<p>Snapshot expiration automatically removes old table snapshots and any unreferenced data files to reduce metadata overhead and storage costs. You can configure:</p>
<ul>
<li><strong>Max snapshot age</strong> - Snapshots older than this duration are expired. Specify a value followed by a unit (<code>d</code> for days, <code>h</code> for hours, <code>m</code> for minutes, <code>s</code> for seconds). For example, <code>7d</code> expires snapshots older than 7 days.</li>
<li><strong>Min snapshots to keep</strong> - The minimum number of snapshots to retain, regardless of age.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/552.md")
</div></div>
<h2 id="disable-snapshot-expiration">Disable snapshot expiration</h2>
<p>Disabling snapshot expiration prevents the process from running for all tables (catalog level) or a specific table (table level). You can re-enable snapshot expiration at any time.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/556.md")
</div></div>
<h2 id="authenticate-your-iceberg-engine">Authenticate your Iceberg engine</h2>
<p>To connect your Iceberg engine to R2 Data Catalog, you must provide a Cloudflare API token with <strong>both</strong> R2 Data Catalog permissions and R2 storage permissions. Iceberg engines interact with R2 Data Catalog to perform table operations. The catalog also provides engines with SigV4 credentials, which are required to access the underlying data files stored in R2.</p>
<p>R2 Data Catalog supports both read-only and read-write tokens:</p>
<ul>
<li><strong>Read-only</strong> operations (for example, listing namespaces, loading tables, and querying data) require a token with read access to R2 Data Catalog and R2 storage.</li>
<li><strong>Write</strong> operations (for example, creating or dropping tables and committing transactions) require a token with read and write access to R2 Data Catalog and R2 storage.</li>
</ul>
<p>Use a read-only token for query engines and clients that only read data (such as R2 SQL, DuckDB, or PyIceberg readers), and a read-write token for engines and pipelines that create tables or write data.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="vended-credentials-inherit-your-token-s-r2-storage-permissions">Vended credentials inherit your token's R2 storage permissions</h3>
@markup("md", "content/.markup/bodies/528.md")
</aside>
<h3 id="create-api-token-in-the-dashboard">Create API token in the dashboard</h3>
<p>Create an <a href="/r2/api/tokens/#permissions">R2 API token</a> with the permissions matching your workload:</p>
<ul>
<li><strong>Admin Read &amp; Write</strong> — for engines and pipelines that read and write data. Includes read and write access to both R2 Data Catalog and R2 storage.</li>
<li><strong>Admin Read only</strong> — for query engines and clients that only read data. Includes read access to both R2 Data Catalog and R2 storage.</li>
</ul>
<p>Providing the resulting token value to your Iceberg engine gives it the ability to manage catalog metadata and handle data operations (reads or writes to R2).</p>
<h3 id="create-api-token-via-api">Create API token via API</h3>
<p>To create an API token programmatically for use with R2 Data Catalog, you need to specify both R2 Data Catalog and R2 storage permission groups in your <a href="/r2/api/tokens/#access-policy">Access Policy</a>.</p>
<h4 id="example-read-write-access-policy">Example read-write Access Policy</h4>
<p>Use read and write permission groups for engines and pipelines that create tables or write data:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;id&quot;: &quot;f267e341f3dd4697bd3b9f71dd96247f&quot;,&#10;		&quot;effect&quot;: &quot;allow&quot;,&#10;		&quot;resources&quot;: {&#10;			&quot;com.cloudflare.edge.r2.bucket.4793d734c0b8e484dfc37ec392b5fa8a_default_my-bucket&quot;: &quot;*&quot;,&#10;			&quot;com.cloudflare.edge.r2.bucket.4793d734c0b8e484dfc37ec392b5fa8a_eu_my-eu-bucket&quot;: &quot;*&quot;&#10;		},&#10;		&quot;permission_groups&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;d229766a2f7f4d299f20eaa8c9b1fde9&quot;,&#10;				&quot;name&quot;: &quot;Workers R2 Data Catalog Write&quot;&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;2efd5506f9c8494dacb1fa10a3e7d5b6&quot;,&#10;				&quot;name&quot;: &quot;Workers R2 Storage Bucket Item Write&quot;&#10;			}&#10;		]&#10;	}&#10;]&#10;</code></pre>
<h4 id="example-read-only-access-policy">Example read-only Access Policy</h4>
<p>Use read permission groups for query engines and clients that only read data:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;id&quot;: &quot;f267e341f3dd4697bd3b9f71dd96247f&quot;,&#10;		&quot;effect&quot;: &quot;allow&quot;,&#10;		&quot;resources&quot;: {&#10;			&quot;com.cloudflare.edge.r2.bucket.4793d734c0b8e484dfc37ec392b5fa8a_default_my-bucket&quot;: &quot;*&quot;,&#10;			&quot;com.cloudflare.edge.r2.bucket.4793d734c0b8e484dfc37ec392b5fa8a_eu_my-eu-bucket&quot;: &quot;*&quot;&#10;		},&#10;		&quot;permission_groups&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;45db74139a62490b9b60eb7c4f34994b&quot;,&#10;				&quot;name&quot;: &quot;Workers R2 Data Catalog Read&quot;&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;6a018a9f2fc74eb6b293b0c548f38b39&quot;,&#10;				&quot;name&quot;: &quot;Workers R2 Storage Bucket Item Read&quot;&#10;			}&#10;		]&#10;	}&#10;]&#10;</code></pre>
<p>To learn more about how to create API tokens for R2 Data Catalog using the API, including required permission groups and usage examples, refer to the <a href="/r2/api/tokens/#create-api-tokens-via-api">Create API tokens via API documentation</a>.</p>
<h2 id="r2-local-uploads">R2 Local Uploads</h2>
<p><a href="/r2/buckets/local-uploads">Local Uploads</a> writes object data to a nearby location, then asynchronously copies it to your bucket. Data is queryable immediately and remains strongly consistent. This can significantly improve latency of writes from Apache Iceberg clients outside of the region of the respective R2 Data Catalog bucket.</p>
<p>To enable R2 Local Uploads, you can use the following Wrangler command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 bucket catalog local-uploads enable &lt;R2_Data_Catalog_BUCKET_NAME&gt;&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<ul>
<li>R2 Data Catalog does not currently support R2 buckets in a non-default jurisdiction.</li>
</ul>
<h2 id="learn-more">Learn more</h2>
<div class="nb-card nb-link-card"><h3 id="card-get-started-r2-data-catalog-get-started"><a href="/r2-data-catalog/get-started/">Get started</a></h3><p>Learn how to enable the R2 Data Catalog on your bucket, load sample data, and run your first query.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-connect-to-iceberg-engines-r2-data-catalog-config-examples"><a href="/r2-data-catalog/config-examples/">Connect to Iceberg engines</a></h3><p>Find detailed setup instructions for Apache Spark and other common query engines.</p></div>
