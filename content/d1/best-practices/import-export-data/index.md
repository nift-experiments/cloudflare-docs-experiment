---
cp9:
  canonical: https://developers.cloudflare.com/d1/best-practices/import-export-data/
  description: Import existing SQLite tables into D1 or export a D1 database for local use.
  full_title: Import and export data · Cloudflare D1 docs
  head_html: <title>Import and export data · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Import existing SQLite tables into D1 or export a D1 database for local use."><link rel="canonical" href="https://developers.cloudflare.com/d1/best-practices/import-export-data/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/best-practices/import-export-data/index.md"><meta property="og:title" content="Import and export data · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Import existing SQLite tables into D1 or export a D1 database for local use."><meta property="og:url" content="https://developers.cloudflare.com/d1/best-practices/import-export-data/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/best-practices/import-export-data/#page","headline":"Import and export data \u00b7 Cloudflare D1 docs","description":"Import existing SQLite tables into D1 or export a D1 database for local use.","url":"https://developers.cloudflare.com/d1/best-practices/import-export-data/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/best-practices/import-export-data/
  schema: 1
---
<p>D1 allows you to import existing SQLite tables and their data directly, enabling you to migrate existing data into D1 quickly and easily. This can be useful when migrating applications to use Workers and D1, or when you want to prototype a schema locally before importing it to your D1 database(s).</p>
<p>D1 also allows you to export a database. This can be useful for <a href="/d1/best-practices/local-development/">local development</a> or testing.</p>
<h2 id="import-an-existing-database">Import an existing database</h2>
<p>To import an existing SQLite database into D1, you must have:</p>
<ol>
<li>The Cloudflare <a href="/workers/wrangler/install-and-update/">Wrangler CLI installed</a>.</li>
<li>A database to use as the target.</li>
<li>An existing SQLite (version 3.0+) database file to import.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7409.md")
</aside>
<p>For example, consider the following <code>users_export.sql</code> schema &amp; values, which includes a <code>CREATE TABLE IF NOT EXISTS</code> statement:</p>
<pre tabindex="0"><code class="language-sql">CREATE TABLE IF NOT EXISTS users (&#10;	id VARCHAR(50),&#10;	full_name VARCHAR(50),&#10;	created_on DATE&#10;);&#10;INSERT INTO users (id, full_name, created_on) VALUES (&#x27;01GREFXCN9519NRVXWTPG0V0BF&#x27;, &#x27;Catlaina Harbar&#x27;, &#x27;2022-08-20 05:39:52&#x27;);&#10;INSERT INTO users (id, full_name, created_on) VALUES (&#x27;01GREFXCNBYBGX2GC6ZGY9FMP4&#x27;, &#x27;Hube Bilverstone&#x27;, &#x27;2022-12-15 21:56:13&#x27;);&#10;INSERT INTO users (id, full_name, created_on) VALUES (&#x27;01GREFXCNCWAJWRQWC2863MYW4&#x27;, &#x27;Christin Moss&#x27;, &#x27;2022-07-28 04:13:37&#x27;);&#10;INSERT INTO users (id, full_name, created_on) VALUES (&#x27;01GREFXCNDGQNBQAJG1AP0TYXZ&#x27;, &#x27;Vlad Koche&#x27;, &#x27;2022-11-29 17:40:57&#x27;);&#10;INSERT INTO users (id, full_name, created_on) VALUES (&#x27;01GREFXCNF67KV7FPPSEJVJMEW&#x27;, &#x27;Riane Zamora&#x27;, &#x27;2022-12-24 06:49:04&#x27;);&#10;</code></pre>
<p>With your <code>users_export.sql</code> file in the current working directory, you can pass the <code>--file=users_export.sql</code> flag to <code>d1 execute</code> to execute (import) our table schema and values:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 execute example-db --remote --file=users_export.sql&#10;</code></pre>
<p>To confirm your table was imported correctly and is queryable, execute a <code>SELECT</code> statement to fetch all the tables from your D1 database:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 execute example-db --remote --command &quot;SELECT name FROM sqlite_schema WHERE type=&#x27;table&#x27; ORDER BY name;&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">...&#10;🌀 To execute on your local development database, remove the --remote flag from your wrangler command.&#10;🚣 Executed 1 commands in 0.3165ms&#10;┌────────┐&#10;│ name   │&#10;├────────┤&#10;│ _cf_KV │&#10;├────────┤&#10;│ users  │&#10;└────────┘&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7408.md")
</aside>
<p>From here, you can now query our new table from our Worker <a href="/d1/worker-api/">using the D1 Workers Binding API</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="known-limitations">Known limitations</h3>
@markup("md", "content/.markup/bodies/7407.md")
</aside>
<h3 id="convert-sqlite-database-files">Convert SQLite database files</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7406.md")
</aside>
<p>If you have an existing SQLite database from another system, you can import its tables into a D1 database. Using the <code>sqlite</code> command-line tool, you can convert an <code>.sqlite3</code> file into a series of SQL statements that can be imported (executed) against a D1 database.</p>
<p>For example, if you have a raw SQLite dump called <code>db_dump.sqlite3</code>, run the following <code>sqlite</code> command to convert it:</p>
<pre tabindex="0"><code class="language-sh">sqlite3 db_dump.sqlite3 .dump &gt; db.sql&#10;</code></pre>
<p>Once you have run the above command, you will need to edit the output SQL file to be compatible with D1:</p>
<ol>
<li>Remove <code>BEGIN TRANSACTION</code> and <code>COMMIT;</code> from the file</li>
<li>Remove the following table creation statement (if present):</li>
</ol>
<pre tabindex="0"><code class="language-sql">CREATE TABLE _cf_KV (&#10; 	key TEXT PRIMARY KEY,&#10; 	value BLOB&#10;) WITHOUT ROWID;&#10;</code></pre>
<p>You can then follow the steps to <a href="#import-an-existing-database">import an existing database</a> into D1 by using the <code>.sql</code> file you generated from the database dump as the input to <code>wrangler d1 execute</code>.</p>
<h2 id="export-an-existing-d1-database">Export an existing D1 database</h2>
<p>In addition to importing existing SQLite databases, you might want to export a D1 database for local development or testing. You can export a D1 database to a <code>.sql</code> file using <a href="/workers/wrangler/commands/d1/#d1-export">wrangler d1 export</a> and then execute (import) with <code>d1 execute --file</code>.</p>
<p>To export full D1 database schema and data:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 export &lt;database_name&gt; --remote --output=./database.sql&#10;</code></pre>
<p>To export single table schema and data:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 export &lt;database_name&gt; --remote --table=&lt;table_name&gt; --output=./table.sql&#10;</code></pre>
<p>To export only D1 database schema:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 export &lt;database_name&gt; --remote --output=./schema.sql --no-data&#10;</code></pre>
<p>To export only D1 table schema:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 export &lt;database_name&gt; --remote --table=&lt;table_name&gt; --output=./schema.sql --no-data&#10;</code></pre>
<p>To export only D1 database data:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 export &lt;database_name&gt; --remote --output=./data.sql --no-schema&#10;</code></pre>
<p>To export only D1 table data:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 export &lt;database_name&gt; --remote --table=&lt;table_name&gt; --output=./data.sql --no-schema&#10;</code></pre>
<h3 id="known-limitations-1">Known limitations</h3>
<ul>
<li>Export is not supported for virtual tables, including databases with virtual tables. D1 supports virtual tables for full-text search using SQLite's <a href="https://www.sqlite.org/fts5.html">FTS5 module</a>. As a workaround, delete any virtual tables, export, and then recreate virtual tables.</li>
<li>A running export will block other database requests.</li>
<li>Any numeric value in a column is affected by JavaScript's 52-bit precision for numbers. If you store a very large number (in <code>int64</code>), then retrieve the same value, the returned value may be less precise than your original number.</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you receive an error when trying to import an existing schema and/or dataset into D1:</p>
<ul>
<li>Ensure you are importing data in SQL format (typically with a <code>.sql</code> file extension). Refer to <a href="#convert-sqlite-database-files">how to convert SQLite files</a> if you have a <code>.sqlite3</code> database dump.</li>
<li>Make sure the schema is <a href="https://www.sqlite.org/docs.html">SQLite3</a> compatible. You cannot import data from a MySQL or PostgreSQL database into D1, as the types and SQL syntax are not directly compatible.</li>
<li>If you have foreign key relationships between tables, ensure you are importing the tables in the right order. You cannot refer to a table that does not yet exist.</li>
<li>If you receive a <code>&quot;cannot start a transaction within a transaction&quot;</code> error, make sure you have removed <code>BEGIN TRANSACTION</code> and <code>COMMIT</code> from your dumped SQL statements.</li>
</ul>
<h3 id="resolve-statement-too-long-error">Resolve <code>Statement too long</code> error</h3>
<p>If you encounter a <code>Statement too long</code> error when trying to import a large SQL file into D1, it means that one of the SQL statements in your file exceeds the maximum allowed length.</p>
<p>To resolve this issue, convert the single large <code>INSERT</code> statement into multiple smaller <code>INSERT</code> statements. For example, instead of inserting 1,000 rows in one statement, split it into four groups of 250 rows, as illustrated in the code below.</p>
<p>Before:</p>
<pre tabindex="0"><code class="language-sql">INSERT INTO users (id, full_name, created_on)&#10;VALUES&#10;  (&#x27;1&#x27;, &#x27;Jacquelin Elara&#x27;, &#x27;2022-08-20 05:39:52&#x27;),&#10;  (&#x27;2&#x27;, &#x27;Hubert Simmons&#x27;, &#x27;2022-12-15 21:56:13&#x27;),&#10;  ...&#10;  (&#x27;1000&#x27;, &#x27;Boris Pewter&#x27;, &#x27;2022-12-24 07:59:54&#x27;);&#10;</code></pre>
<p>After:</p>
<pre tabindex="0"><code class="language-sql">INSERT INTO users (id, full_name, created_on)&#10;VALUES&#10;  (&#x27;1&#x27;, &#x27;Jacquelin Elara&#x27;, &#x27;2022-08-20 05:39:52&#x27;),&#10;  ...&#10;  (&#x27;100&#x27;, &#x27;Eddy Orelo&#x27;, &#x27;2022-12-15 22:16:15&#x27;);&#10;...&#10;INSERT INTO users (id, full_name, created_on)&#10;VALUES&#10;  (&#x27;901&#x27;, &#x27;Roran Eroi&#x27;, &#x27;2022-08-20 05:39:52&#x27;),&#10;  ...&#10;  (&#x27;1000&#x27;, &#x27;Boris Pewter&#x27;, &#x27;2022-12-15 22:16:15&#x27;);&#10;</code></pre>
<h2 id="foreign-key-constraints">Foreign key constraints</h2>
<p>When importing data, you may need to temporarily disable <a href="/d1/sql-api/foreign-keys/">foreign key constraints</a>. To do so, call <code>PRAGMA defer_foreign_keys = true</code> before making changes that would violate foreign keys.</p>
<p>Refer to the <a href="/d1/sql-api/foreign-keys/">foreign key documentation</a> to learn more about how to work with foreign keys and D1.</p>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li>Read the SQLite <a href="https://www.sqlite.org/lang_createtable.html"><code>CREATE TABLE</code></a> documentation.</li>
<li>Learn how to <a href="/d1/worker-api/">use the D1 Workers Binding API</a> from within a Worker.</li>
<li>Understand how <a href="/d1/reference/migrations/">database migrations work</a> with D1.</li>
</ul>
