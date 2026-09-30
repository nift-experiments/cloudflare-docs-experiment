<p>Below is an example of using <a href="https://docs.starrocks.io/docs/data_source/catalog/iceberg/iceberg_catalog/#rest">StarRocks</a> to connect, query, modify data from R2 Data Catalog (read-write).</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li><a href="/r2/buckets/create-buckets/">Create an R2 bucket</a> and <a href="/r2-data-catalog/manage-catalogs/#enable-r2-data-catalog-on-a-bucket">enable the data catalog</a>.</li>
<li><a href="/r2/api/tokens/">Create an R2 API token</a> with both <a href="/r2/api/tokens/#permissions">R2 and data catalog permissions</a>.</li>
<li>A running <a href="https://www.starrocks.io/">StarRocks</a> frontend instance. You can use the <a href="https://docs.starrocks.io/docs/quick_start/shared-nothing/#launch-starrocks">all-in-one</a> docker setup.</li>
</ul>
<h2 id="example-usage">Example usage</h2>
<p>In your running StarRocks instance, run these commands:</p>
<pre><code class="language-sql">&#45;- Create an Iceberg catalog named `r2` and set it as the current catalog&#10;&#10;CREATE EXTERNAL CATALOG r2&#10;PROPERTIES&#10;(&#10;    &quot;type&quot; = &quot;iceberg&quot;,&#10;    &quot;iceberg.catalog.type&quot; = &quot;rest&quot;,&#10;    &quot;iceberg.catalog.uri&quot; = &quot;&lt;r2_catalog_uri&gt;&quot;,&#10;    &quot;iceberg.catalog.security&quot; = &quot;oauth2&quot;,&#10;    &quot;iceberg.catalog.oauth2.token&quot; = &quot;&lt;r2_api_token&gt;&quot;,&#10;    &quot;iceberg.catalog.warehouse&quot; = &quot;&lt;r2_warehouse_name&gt;&quot;&#10;);&#10;&#10;SET CATALOG r2;&#10;&#10;&#45;- Create a database and display all databases in newly connected catalog&#10;&#10;CREATE DATABASE testdb;&#10;&#10;SHOW DATABASES FROM r2;&#10;&#10;&#43;--------------------+&#10;| Database           |&#10;&#43;--------------------+&#10;| information_schema |&#10;| testdb             |&#10;&#43;--------------------+&#10;2 rows in set (0.66 sec)&#10;</code></pre>
