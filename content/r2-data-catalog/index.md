<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/557.md")
</aside>
<p>R2 Data Catalog is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> data catalog built directly into your R2 bucket. It exposes a standard Iceberg REST catalog interface, so you can connect the engines you already use, like <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, <a href="/r2-data-catalog/config-examples/snowflake/">Snowflake</a>, and <a href="/r2-data-catalog/config-examples/pyiceberg/">PyIceberg</a>.</p>
<p>R2 Data Catalog makes it easy to turn an R2 bucket into a data warehouse or lakehouse for a variety of analytical workloads including log analytics, business intelligence, and data pipelines. R2's zero-egress fee model means that data users and consumers can access and analyze data from different clouds, data platforms, or regions without incurring transfer costs.</p>
<p>To get started with R2 Data Catalog, refer to the <a href="/r2-data-catalog/get-started/">R2 Data Catalog: Getting started</a>.</p>
<h2 id="what-is-apache-iceberg">What is Apache Iceberg?</h2>
<p><a href="https://iceberg.apache.org/">Apache Iceberg</a> is an open table format designed to handle large-scale analytics datasets stored in object storage. Key features include:</p>
<ul>
<li>ACID transactions - Ensures reliable, concurrent reads and writes with full data integrity.</li>
<li>Optimized metadata - Avoids costly full table scans by using indexed metadata for faster queries.</li>
<li>Full schema evolution - Allows adding, renaming, and deleting columns without rewriting data.</li>
</ul>
<p>Iceberg is already <a href="https://iceberg.apache.org/vendors/">widely supported</a> by engines like Apache Spark, Trino, Snowflake, DuckDB, and ClickHouse, with a fast-growing community behind it.</p>
<h2 id="why-do-you-need-a-data-catalog">Why do you need a data catalog?</h2>
<p>Although the Iceberg data and metadata files themselves live directly in object storage (like <a href="/r2/">R2</a>), the list of tables and pointers to the current metadata need to be tracked centrally by a data catalog.</p>
<p>Think of a data catalog as a library's index system. While books (your data) are physically distributed across shelves (object storage), the index provides a single source of truth about what books exist, their locations, and their latest editions. Without this index, readers (query engines) would waste time searching for books, might access outdated versions, or could accidentally shelve new books in ways that make them unfindable.</p>
<p>Similarly, data catalogs ensure consistent, coordinated access, which allows multiple query engines to safely read from and write to the same tables without conflicts or data corruption.</p>
<h2 id="learn-more">Learn more</h2>
<p><a class="nb-card nb-link-card" href="/r2-data-catalog/get-started/"><h3 id="card-get-started-r2-data-catalog-get-started">Get started</h3><p>Learn how to enable the R2 Data Catalog on your bucket, load sample data, and run your first query.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2-data-catalog/manage-catalogs/"><h3 id="card-managing-catalogs-r2-data-catalog-manage-catalogs">Managing catalogs</h3><p>Enable or disable R2 Data Catalog on your bucket, retrieve configuration details, and authenticate your Iceberg engine.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2-data-catalog/config-examples/"><h3 id="card-connect-to-iceberg-engines-r2-data-catalog-config-examples">Connect to Iceberg engines</h3><p>Find detailed setup instructions for Apache Spark and other common query engines.</p></a></p>
