---
cp9:
  canonical: https://developers.cloudflare.com/d1/sql-api/sql-statements/
  description: Supported SQL statements, PRAGMA commands, and SQLite extensions available in D1.
  full_title: SQL statements · Cloudflare D1 docs
  head_html: <title>SQL statements · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Supported SQL statements, PRAGMA commands, and SQLite extensions available in D1."><link rel="canonical" href="https://developers.cloudflare.com/d1/sql-api/sql-statements/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/sql-api/sql-statements/index.md"><meta property="og:title" content="SQL statements · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Supported SQL statements, PRAGMA commands, and SQLite extensions available in D1."><meta property="og:url" content="https://developers.cloudflare.com/d1/sql-api/sql-statements/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/sql-api/sql-statements/#page","headline":"SQL statements \u00b7 Cloudflare D1 docs","description":"Supported SQL statements, PRAGMA commands, and SQLite extensions available in D1.","url":"https://developers.cloudflare.com/d1/sql-api/sql-statements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/sql-api/sql-statements/
  schema: 1
---
<p>D1 is compatible with most SQLite's SQL convention since it leverages SQLite's query engine. D1 supports a number of database-level statements that allow you to list tables, indexes, and inspect the schema for a given table or index.</p>
<p>You can execute any of these statements via the D1 console in the Cloudflare dashboard, <a href="/workers/wrangler/commands/d1/#d1-execute"><code>wrangler d1 execute</code></a>, or with the <a href="/d1/worker-api/d1-database">D1 Worker Bindings API</a>.</p>
<h2 id="supported-sqlite-extensions">Supported SQLite extensions</h2>
<p>D1 supports a subset of SQLite extensions for added functionality, including:</p>
<ul>
<li><a href="https://www.sqlite.org/fts5.html">FTS5 module</a> for full-text search (including <code>fts5vocab</code>).</li>
<li><a href="https://www.sqlite.org/json1.html">JSON extension</a> for JSON functions and operators.</li>
<li><a href="https://sqlite.org/lang_mathfunc.html">Math functions</a>.</li>
</ul>
<p>Refer to the <a href="https://github.com/cloudflare/workerd/blob/4c42a4a9d3390c88e9bd977091c9d3395a6cd665/src/workerd/util/sqlite.c%2B%2B#L269">source code</a> for the full list of supported functions.</p>
<h2 id="compatible-pragma-statements">Compatible PRAGMA statements</h2>
<p>D1 supports some <a href="https://www.sqlite.org/pragma.html">SQLite PRAGMA</a> statements. The PRAGMA statement is an SQL extension for SQLite. PRAGMA commands can be used to:</p>
<ul>
<li>Modify the behavior of certain SQLite operations.</li>
<li>Query the SQLite library for internal data about schemas or tables (but note that PRAGMA statements cannot query the contents of a table).</li>
<li>Control <a href="/workers/configuration/environment-variables/">environmental variables</a>.</li>
</ul>
<p>The PRAGMA statement examples on this page use the following SQL.</p>
<pre tabindex="0"><code class="language-sql">PRAGMA foreign_keys=off;&#10;DROP TABLE IF EXISTS &quot;Employee&quot;;&#10;DROP TABLE IF EXISTS &quot;Category&quot;;&#10;DROP TABLE IF EXISTS &quot;Customer&quot;;&#10;DROP TABLE IF EXISTS &quot;Shipper&quot;;&#10;DROP TABLE IF EXISTS &quot;Supplier&quot;;&#10;DROP TABLE IF EXISTS &quot;Order&quot;;&#10;DROP TABLE IF EXISTS &quot;Product&quot;;&#10;DROP TABLE IF EXISTS &quot;OrderDetail&quot;;&#10;DROP TABLE IF EXISTS &quot;CustomerCustomerDemo&quot;;&#10;DROP TABLE IF EXISTS &quot;CustomerDemographic&quot;;&#10;DROP TABLE IF EXISTS &quot;Region&quot;;&#10;DROP TABLE IF EXISTS &quot;Territory&quot;;&#10;DROP TABLE IF EXISTS &quot;EmployeeTerritory&quot;;&#10;DROP VIEW IF EXISTS [ProductDetails_V];&#10;CREATE TABLE IF NOT EXISTS &quot;Employee&quot; ( &quot;Id&quot; INTEGER PRIMARY KEY, &quot;LastName&quot; VARCHAR(8000) NULL, &quot;FirstName&quot; VARCHAR(8000) NULL, &quot;Title&quot; VARCHAR(8000) NULL, &quot;TitleOfCourtesy&quot; VARCHAR(8000) NULL, &quot;BirthDate&quot; VARCHAR(8000) NULL, &quot;HireDate&quot; VARCHAR(8000) NULL, &quot;Address&quot; VARCHAR(8000) NULL, &quot;City&quot; VARCHAR(8000) NULL, &quot;Region&quot; VARCHAR(8000) NULL, &quot;PostalCode&quot; VARCHAR(8000) NULL, &quot;Country&quot; VARCHAR(8000) NULL, &quot;HomePhone&quot; VARCHAR(8000) NULL, &quot;Extension&quot; VARCHAR(8000) NULL, &quot;Photo&quot; BLOB NULL, &quot;Notes&quot; VARCHAR(8000) NULL, &quot;ReportsTo&quot; INTEGER NULL, &quot;PhotoPath&quot; VARCHAR(8000) NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;Category&quot; ( &quot;Id&quot; INTEGER PRIMARY KEY, &quot;CategoryName&quot; VARCHAR(8000) NULL, &quot;Description&quot; VARCHAR(8000) NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;Customer&quot; ( &quot;Id&quot; VARCHAR(8000) PRIMARY KEY, &quot;CompanyName&quot; VARCHAR(8000) NULL, &quot;ContactName&quot; VARCHAR(8000) NULL, &quot;ContactTitle&quot; VARCHAR(8000) NULL, &quot;Address&quot; VARCHAR(8000) NULL, &quot;City&quot; VARCHAR(8000) NULL, &quot;Region&quot; VARCHAR(8000) NULL, &quot;PostalCode&quot; VARCHAR(8000) NULL, &quot;Country&quot; VARCHAR(8000) NULL, &quot;Phone&quot; VARCHAR(8000) NULL, &quot;Fax&quot; VARCHAR(8000) NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;Shipper&quot; ( &quot;Id&quot; INTEGER PRIMARY KEY, &quot;CompanyName&quot; VARCHAR(8000) NULL, &quot;Phone&quot; VARCHAR(8000) NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;Supplier&quot; ( &quot;Id&quot; INTEGER PRIMARY KEY, &quot;CompanyName&quot; VARCHAR(8000) NULL, &quot;ContactName&quot; VARCHAR(8000) NULL, &quot;ContactTitle&quot; VARCHAR(8000) NULL, &quot;Address&quot; VARCHAR(8000) NULL, &quot;City&quot; VARCHAR(8000) NULL, &quot;Region&quot; VARCHAR(8000) NULL, &quot;PostalCode&quot; VARCHAR(8000) NULL, &quot;Country&quot; VARCHAR(8000) NULL, &quot;Phone&quot; VARCHAR(8000) NULL, &quot;Fax&quot; VARCHAR(8000) NULL, &quot;HomePage&quot; VARCHAR(8000) NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;Order&quot; ( &quot;Id&quot; INTEGER PRIMARY KEY, &quot;CustomerId&quot; VARCHAR(8000) NULL, &quot;EmployeeId&quot; INTEGER NOT NULL, &quot;OrderDate&quot; VARCHAR(8000) NULL, &quot;RequiredDate&quot; VARCHAR(8000) NULL, &quot;ShippedDate&quot; VARCHAR(8000) NULL, &quot;ShipVia&quot; INTEGER NULL, &quot;Freight&quot; DECIMAL NOT NULL, &quot;ShipName&quot; VARCHAR(8000) NULL, &quot;ShipAddress&quot; VARCHAR(8000) NULL, &quot;ShipCity&quot; VARCHAR(8000) NULL, &quot;ShipRegion&quot; VARCHAR(8000) NULL, &quot;ShipPostalCode&quot; VARCHAR(8000) NULL, &quot;ShipCountry&quot; VARCHAR(8000) NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;Product&quot; ( &quot;Id&quot; INTEGER PRIMARY KEY, &quot;ProductName&quot; VARCHAR(8000) NULL, &quot;SupplierId&quot; INTEGER NOT NULL, &quot;CategoryId&quot; INTEGER NOT NULL, &quot;QuantityPerUnit&quot; VARCHAR(8000) NULL, &quot;UnitPrice&quot; DECIMAL NOT NULL, &quot;UnitsInStock&quot; INTEGER NOT NULL, &quot;UnitsOnOrder&quot; INTEGER NOT NULL, &quot;ReorderLevel&quot; INTEGER NOT NULL, &quot;Discontinued&quot; INTEGER NOT NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;OrderDetail&quot; ( &quot;Id&quot; VARCHAR(8000) PRIMARY KEY, &quot;OrderId&quot; INTEGER NOT NULL, &quot;ProductId&quot; INTEGER NOT NULL, &quot;UnitPrice&quot; DECIMAL NOT NULL, &quot;Quantity&quot; INTEGER NOT NULL, &quot;Discount&quot; DOUBLE NOT NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;CustomerCustomerDemo&quot; ( &quot;Id&quot; VARCHAR(8000) PRIMARY KEY, &quot;CustomerTypeId&quot; VARCHAR(8000) NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;CustomerDemographic&quot; ( &quot;Id&quot; VARCHAR(8000) PRIMARY KEY, &quot;CustomerDesc&quot; VARCHAR(8000) NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;Region&quot; ( &quot;Id&quot; INTEGER PRIMARY KEY, &quot;RegionDescription&quot; VARCHAR(8000) NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;Territory&quot; ( &quot;Id&quot; VARCHAR(8000) PRIMARY KEY, &quot;TerritoryDescription&quot; VARCHAR(8000) NULL, &quot;RegionId&quot; INTEGER NOT NULL);&#10;CREATE TABLE IF NOT EXISTS &quot;EmployeeTerritory&quot; ( &quot;Id&quot; VARCHAR(8000) PRIMARY KEY, &quot;EmployeeId&quot; INTEGER NOT NULL, &quot;TerritoryId&quot; VARCHAR(8000) NULL);&#10;CREATE VIEW [ProductDetails_V] as select p.*, c.CategoryName, c.Description as [CategoryDescription], s.CompanyName as [SupplierName], s.Region as [SupplierRegion] from [Product] p join [Category] c on p.CategoryId = c.id join [Supplier] s on s.id = p.SupplierId;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7321.md")
</aside>
<h3 id="pragma-table-list"><code>PRAGMA table_list</code></h3>
<p>Lists the tables and views in the database. This includes the system tables maintained by D1.</p>
<h4 id="return-values">Return values</h4>
<p>One row per each table. Each row contains:</p>
<ol>
<li><code>Schema</code>: the schema in which the table appears (for example, <code>main</code> or <code>temp</code>)</li>
<li><code>name</code>: the name of the table</li>
<li><code>type</code>: the type of the object (one of <code>table</code>, <code>view</code>, <code>shadow</code>, <code>virtual</code>)</li>
<li><code>ncol</code>: the number of columns in the table, including generated or hidden columns</li>
<li><code>wr</code>: <code>1</code> if the table is a WITHOUT ROWID table, <code>0</code> otherwise</li>
<li><code>strict</code>: <code>1</code> if the table is a STRICT table, <code>0</code> otherwise</li>
</ol>
<details class="nb-details"><summary>Example of �CODE38�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7322.md")
</div></details>
<h3 id="pragma-table-info-table-name"><code>PRAGMA table_info(&quot;TABLE_NAME&quot;)</code></h3>
<p>Shows the schema (columns, types, null, default values) for the given <code>TABLE_NAME</code>.</p>
<h4 id="return-values-1">Return values</h4>
<p>One row for each column in the specified table. Each row contains:</p>
<ol>
<li><code>cid</code>: a row identifier</li>
<li><code>name</code>: the name of the column</li>
<li><code>type</code>: the data type (if provided), <code>''</code> otherwise</li>
<li><code>notnull</code>: <code>1</code> if the column can be NULL, <code>0</code> otherwise</li>
<li><code>dflt_value</code>: the default value of the column</li>
<li><code>pk</code>: <code>1</code> if the column is a primary key, <code>0</code> otherwise</li>
</ol>
<details class="nb-details"><summary>Example of �CODE51�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7323.md")
</div></details>
<h3 id="pragma-table-xinfo-table-name"><code>PRAGMA table_xinfo(&quot;TABLE_NAME&quot;)</code></h3>
<p>Similar to <code>PRAGMA table_info(TABLE_NAME)</code> but also includes <a href="/d1/reference/generated-columns/">generated columns</a>.</p>
<details class="nb-details"><summary>Example of �CODE53�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7324.md")
</div></details>
<h3 id="pragma-index-list-table-name"><code>PRAGMA index_list(&quot;TABLE_NAME&quot;)</code></h3>
<p>Show the indexes for the given <code>TABLE_NAME</code>.</p>
<h4 id="return-values-2">Return values</h4>
<p>One row for each index associated with the specified table. Each row contains:</p>
<ol>
<li><code>seq</code>: a sequence number for internal tracking</li>
<li><code>name</code>: the name of the index</li>
<li><code>unique</code>: <code>1</code> if the index is UNIQUE, <code>0</code> otherwise</li>
<li><code>origin</code>: the origin of the index (<code>c</code> if created by <code>CREATE INDEX</code> statement, <code>u</code> if created by UNIQUE constraint, <code>pk</code> if created by a PRIMARY KEY constraint)</li>
<li><code>partial</code>: <code>1</code> if the index is a partial index, <code>0</code> otherwise</li>
</ol>
<details class="nb-details"><summary>Example of �CODE68�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7325.md")
</div></details>
<h3 id="pragma-index-info-index-name"><code>PRAGMA index_info(INDEX_NAME)</code></h3>
<p>Show the indexed column(s) for the given <code>INDEX_NAME</code>.</p>
<h4 id="return-values-3">Return values</h4>
<p>One row for each key column in the specified index. Each row contains:</p>
<ol>
<li><code>seqno</code>: the rank of the column within the index</li>
<li><code>cid</code>: the rank of the column within the table being indexed</li>
<li><code>name</code>: the name of the column being indexed</li>
</ol>
<details class="nb-details"><summary>Example of �CODE73�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7326.md")
</div></details>
<h3 id="pragma-index-xinfo-index-name"><code>PRAGMA index_xinfo(&quot;INDEX_NAME&quot;)</code></h3>
<p>Similar to <code>PRAGMA index_info(&quot;TABLE_NAME&quot;)</code> but also includes hidden columns.</p>
<details class="nb-details"><summary>Example of �CODE75�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7327.md")
</div></details>
<h3 id="pragma-quick-check"><code>PRAGMA quick_check</code></h3>
<p>Checks the formatting and consistency of the table, including:</p>
<ul>
<li>Incorrectly formatted records</li>
<li>Missing pages</li>
<li>Sections of the database which are used multiple times, or are not used at all.</li>
</ul>
<h4 id="return-values-4">Return values</h4>
<ul>
<li><strong>If there are no errors:</strong> a single row with the value <code>OK</code></li>
<li><strong>If there are errors:</strong> a string which describes the issues flagged by the check</li>
</ul>
<details class="nb-details"><summary>Example of �CODE77�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7328.md")
</div></details>
<h3 id="pragma-foreign-key-check"><code>PRAGMA foreign_key_check</code></h3>
<p>Checks for invalid references of foreign keys in the selected table.</p>
<h3 id="pragma-foreign-key-list-table-name"><code>PRAGMA foreign_key_list(&quot;TABLE_NAME&quot;)</code></h3>
<p>Lists the foreign key constraints in the selected table.</p>
<h3 id="pragma-case-sensitive-like-on-off"><code>PRAGMA case_sensitive_like = (on|off)</code></h3>
<p>Toggles case sensitivity for LIKE operators. When <code>PRAGMA case_sensitive_like</code> is set to:</p>
<ul>
<li><code>ON</code>: 'a' LIKE 'A' is false</li>
<li><code>OFF</code>: 'a' LIKE 'A' is true (this is the default behavior of the LIKE operator)</li>
</ul>
<h3 id="pragma-ignore-check-constraints-on-off"><code>PRAGMA ignore_check_constraints = (on|off)</code></h3>
<p>Toggles the enforcement of CHECK constraints. When <code>PRAGMA ignore_check_constraints</code> is set to:</p>
<ul>
<li><code>ON</code>: check constraints are ignored</li>
<li><code>OFF</code>: check constraints are enforced (this is the default behavior)</li>
</ul>
<h3 id="pragma-legacy-alter-table-on-off"><code>PRAGMA legacy_alter_table = (on|off)</code></h3>
<p>Toggles the ALTER TABLE RENAME command behavior before/after the legacy version of SQLite (3.24.0). When <code>PRAGMA legacy_alter_table</code> is set to:</p>
<ul>
<li><code>ON</code>: ALTER TABLE RENAME only rewrites the initial occurrence of the table name in its CREATE TABLE statement and any associated CREATE INDEX and CREATE TRIGGER statements. All other occurrences are unmodified.</li>
<li><code>OFF</code>: ALTER TABLE RENAME rewrites all references to the table name in the schema (this is the default behavior).</li>
</ul>
<h3 id="pragma-recursive-triggers-on-off"><code>PRAGMA recursive_triggers = (on|off)</code></h3>
<p>Toggles the recursive trigger capability. When <code>PRAGMA recursive_triggers</code> is set to:</p>
<ul>
<li><code>ON</code>: triggers which fire can activate other triggers (a single trigger can fire multiple times over the same row)</li>
<li><code>OFF</code>: triggers which fire cannot activate other triggers</li>
</ul>
<h3 id="pragma-reverse-unordered-selects-on-off"><code>PRAGMA reverse_unordered_selects = (on|off)</code></h3>
<p>Toggles the order of the results of a SELECT statement without an ORDER BY clause. When <code>PRAGMA reverse_unordered_selects</code> is set to:</p>
<ul>
<li><code>ON</code>: reverses the order of results of a SELECT statement</li>
<li><code>OFF</code>: returns the results of a SELECT statement in the usual order</li>
</ul>
<h3 id="pragma-foreign-keys-on-off"><code>PRAGMA foreign_keys = (on|off)</code></h3>
<p>Toggles the foreign key constraint enforcement. When <code>PRAGMA foreign_keys</code> is set to:</p>
<ul>
<li><code>ON</code>: stops operations which violate foreign key constraints</li>
<li><code>OFF</code>: allows operations which violate foreign key constraints</li>
</ul>
<h3 id="pragma-defer-foreign-keys-on-off"><code>PRAGMA defer_foreign_keys = (on|off)</code></h3>
<p>Allows you to defer the enforcement of <a href="/d1/sql-api/foreign-keys/">foreign key constraints</a> until the end of the current transaction. This can be useful during <a href="/d1/reference/migrations/">database migrations</a>, as schema changes may temporarily violate constraints depending on the order in which they are applied.</p>
<p>This does not disable foreign key enforcement outside of the current transaction. If you have not resolved outstanding foreign key violations at the end of your transaction, it will fail with a <code>FOREIGN KEY constraint failed</code> error.</p>
<p>Note that setting <code>PRAGMA defer_foreign_keys = ON</code> does not prevent <code>ON DELETE CASCADE</code> actions from being executed. While foreign key constraint checks are deferred until the end of a transaction, <code>ON DELETE CASCADE</code> operations will remain active, consistent with SQLite's behavior.</p>
<p>To defer foreign key enforcement, set <code>PRAGMA defer_foreign_keys = on</code> at the start of your transaction, or ahead of changes that would violate constraints:</p>
<pre tabindex="0"><code class="language-sql">&#45;- Defer foreign key enforcement in this transaction.&#10;PRAGMA defer_foreign_keys = on&#10;&#10;&#45;- Run your CREATE TABLE or ALTER TABLE / COLUMN statements&#10;ALTER TABLE users ...&#10;&#10;&#45;- This is implicit if not set by the end of the transaction.&#10;PRAGMA defer_foreign_keys = off&#10;</code></pre>
<p>Refer to the <a href="/d1/sql-api/foreign-keys/">foreign key documentation</a> to learn more about how to work with foreign keys.</p>
<h3 id="pragma-optimize"><code>PRAGMA optimize</code></h3>
<p>Attempts to optimize all schemas in a database by running the <code>ANALYZE</code> command for each table, if necessary. <code>ANALYZE</code> updates an internal table which contain statistics about tables and indices. These statistics helps the <span class="nb-glossary-tooltip" title="query planner">query planner</span> to execute the input query more efficiently.</p>
<p>When <code>PRAGMA optimize</code> runs <code>ANALYZE</code>, it sets a limit to ensure the command does not take too long to execute. Alternatively, <code>PRAGMA optimize</code> may deem it unnecessary to run <code>ANALYZE</code> (for example, if the schema has not changed significantly). In this scenario, no optimizations are made.</p>
<p>We recommend running this command after making any changes to the schema (for example, after <a href="/d1/best-practices/use-indexes/">creating an index</a>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7320.md")
</aside>
<p>Refer to <a href="https://www.sqlite.org/pragma.html#pragma_optimize">SQLite PRAGMA optimize documentation</a> for more information on how <code>PRAGMA optimize</code> optimizes a database.</p>
<h2 id="query-sqlite-master">Query <code>sqlite_master</code></h2>
<p>You can also query the <code>sqlite_master</code> table to show all tables, indexes, and the original SQL used to generate them:</p>
<pre tabindex="0"><code class="language-sql">SELECT name, sql FROM sqlite_master&#10;</code></pre>
<pre tabindex="0"><code class="language-json">      {&#10;        &quot;name&quot;: &quot;users&quot;,&#10;        &quot;sql&quot;: &quot;CREATE TABLE users ( user_id INTEGER PRIMARY KEY, email_address TEXT, created_at INTEGER, deleted INTEGER, settings TEXT)&quot;&#10;      },&#10;      {&#10;        &quot;name&quot;: &quot;idx_ordered_users&quot;,&#10;        &quot;sql&quot;: &quot;CREATE INDEX idx_ordered_users ON users(created_at DESC)&quot;&#10;      },&#10;      {&#10;        &quot;name&quot;: &quot;Order&quot;,&#10;        &quot;sql&quot;: &quot;CREATE TABLE \&quot;Order\&quot; ( \&quot;Id\&quot; INTEGER PRIMARY KEY, \&quot;CustomerId\&quot; VARCHAR(8000) NULL, \&quot;EmployeeId\&quot; INTEGER NOT NULL, \&quot;OrderDate\&quot; VARCHAR(8000) NULL, \&quot;RequiredDate\&quot; VARCHAR(8000) NULL, \&quot;ShippedDate\&quot; VARCHAR(8000) NULL, \&quot;ShipVia\&quot; INTEGER NULL, \&quot;Freight\&quot; DECIMAL NOT NULL, \&quot;ShipName\&quot; VARCHAR(8000) NULL, \&quot;ShipAddress\&quot; VARCHAR(8000) NULL, \&quot;ShipCity\&quot; VARCHAR(8000) NULL, \&quot;ShipRegion\&quot; VARCHAR(8000) NULL, \&quot;ShipPostalCode\&quot; VARCHAR(8000) NULL, \&quot;ShipCountry\&quot; VARCHAR(8000) NULL)&quot;&#10;      },&#10;      {&#10;        &quot;name&quot;: &quot;Product&quot;,&#10;        &quot;sql&quot;: &quot;CREATE TABLE \&quot;Product\&quot; ( \&quot;Id\&quot; INTEGER PRIMARY KEY, \&quot;ProductName\&quot; VARCHAR(8000) NULL, \&quot;SupplierId\&quot; INTEGER NOT NULL, \&quot;CategoryId\&quot; INTEGER NOT NULL, \&quot;QuantityPerUnit\&quot; VARCHAR(8000) NULL, \&quot;UnitPrice\&quot; DECIMAL NOT NULL, \&quot;UnitsInStock\&quot; INTEGER NOT NULL, \&quot;UnitsOnOrder\&quot; INTEGER NOT NULL, \&quot;ReorderLevel\&quot; INTEGER NOT NULL, \&quot;Discontinued\&quot; INTEGER NOT NULL)&quot;&#10;      }&#10;</code></pre>
<h2 id="search-with-like">Search with LIKE</h2>
<p>You can perform a search using SQL's <code>LIKE</code> operator:</p>
<pre tabindex="0"><code class="language-js">const { results } = await env.DB.prepare(&#10;	&quot;SELECT * FROM Customers WHERE CompanyName LIKE ?&quot;,&#10;)&#10;	.bind(&quot;%eve%&quot;)&#10;	.run();&#10;console.log(&quot;results: &quot;, results);&#10;</code></pre>
<pre tabindex="0"><code class="language-js">results:  [...]&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Learn <a href="/d1/best-practices/use-indexes/#list-indexes">how to create indexes</a> in D1.</li>
<li>Use D1's <a href="/d1/sql-api/query-json/">JSON functions</a> to query JSON data.</li>
<li>Use <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> to run your Worker and D1 locally and debug issues before deploying.</li>
</ul>
