<p>Below is an example of using <a href="https://py.iceberg.apache.org/">PyIceberg</a> to connect to R2 Data Catalog.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li><a href="/r2/buckets/create-buckets/">Create an R2 bucket</a> and <a href="/r2-data-catalog/manage-catalogs/#enable-r2-data-catalog-on-a-bucket">enable the data catalog</a>.</li>
<li><a href="/r2/api/tokens/">Create an R2 API token</a> with both <a href="/r2/api/tokens/#permissions">R2 and data catalog permissions</a>.</li>
<li>Install the <a href="https://py.iceberg.apache.org/#installation">PyIceberg</a> and <a href="https://arrow.apache.org/docs/python/install.html">PyArrow</a> libraries.</li>
</ul>
<h2 id="example-usage">Example usage</h2>
<pre><code class="language-py">import pyarrow as pa&#10;from pyiceberg.catalog.rest import RestCatalog&#10;from pyiceberg.exceptions import NamespaceAlreadyExistsError&#10;&#10;&#35; Define catalog connection details (replace variables)&#10;WAREHOUSE = &quot;&lt;WAREHOUSE&gt;&quot;&#10;TOKEN = &quot;&lt;TOKEN&gt;&quot;&#10;CATALOG_URI = &quot;&lt;CATALOG_URI&gt;&quot;&#10;&#10;&#35; Connect to R2 Data Catalog&#10;catalog = RestCatalog(&#10;    name=&quot;my_catalog&quot;,&#10;    warehouse=WAREHOUSE,&#10;    uri=CATALOG_URI,&#10;    token=TOKEN,&#10;)&#10;&#10;&#35; Create default namespace&#10;catalog.create_namespace(&quot;default&quot;)&#10;&#10;&#35; Create simple PyArrow table&#10;df = pa.table({&#10;    &quot;id&quot;: [1, 2, 3],&#10;    &quot;name&quot;: [&quot;Alice&quot;, &quot;Bob&quot;, &quot;Charlie&quot;],&#10;})&#10;&#10;&#35; Create an Iceberg table&#10;test_table = (&quot;default&quot;, &quot;my_table&quot;)&#10;table = catalog.create_table(&#10;    test_table,&#10;    schema=df.schema,&#10;)&#10;</code></pre>
