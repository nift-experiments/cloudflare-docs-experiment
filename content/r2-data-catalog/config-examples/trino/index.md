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
<pre><code class="language-bash">mkdir -p trino-catalog &amp;&amp; cd trino-catalog/&#10;</code></pre>
<p>Create a configuration file called <code>r2.properties</code> for your R2 Data Catalog connection:</p>
<pre><code class="language-properties">&#35; r2.properties&#10;connector.name=iceberg&#10;&#10;&#35; R2 Configuration&#10;fs.native-s3.enabled=true&#10;s3.region=auto&#10;s3.aws-access-key=&lt;Your R2 access key&gt;&#10;s3.aws-secret-key=&lt;Your R2 secret&gt;&#10;s3.endpoint=&lt;Your R2 endpoint&gt;&#10;s3.path-style-access=true&#10;&#10;&#35; R2 Data Catalog Configuration&#10;iceberg.catalog.type=rest&#10;iceberg.rest-catalog.uri=&lt;Your R2 Data Catalog URI&gt;&#10;iceberg.rest-catalog.warehouse=&lt;Your R2 Data Catalog warehouse&gt;&#10;iceberg.rest-catalog.security=OAUTH2&#10;iceberg.rest-catalog.oauth2.token=&lt;Your R2 authentication token&gt;&#10;</code></pre>
<h2 id="example-usage">Example usage</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11321.md")
</div>
