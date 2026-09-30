---
cp9:
  canonical: https://developers.cloudflare.com/d1/sql-api/foreign-keys/
  description: Enforce relational integrity across D1 tables by defining and deferring foreign key constraints.
  full_title: Define foreign keys · Cloudflare D1 docs
  head_html: <title>Define foreign keys · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Enforce relational integrity across D1 tables by defining and deferring foreign key constraints."><link rel="canonical" href="https://developers.cloudflare.com/d1/sql-api/foreign-keys/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/sql-api/foreign-keys/index.md"><meta property="og:title" content="Define foreign keys · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enforce relational integrity across D1 tables by defining and deferring foreign key constraints."><meta property="og:url" content="https://developers.cloudflare.com/d1/sql-api/foreign-keys/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/sql-api/foreign-keys/#page","headline":"Define foreign keys \u00b7 Cloudflare D1 docs","description":"Enforce relational integrity across D1 tables by defining and deferring foreign key constraints.","url":"https://developers.cloudflare.com/d1/sql-api/foreign-keys/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/sql-api/foreign-keys/
  schema: 1
---
<p>D1 supports defining and enforcing foreign key constraints across tables in a database.</p>
<p>Foreign key constraints allow you to enforce relationships across tables. For example, you can use foreign keys to create a strict binding between a <code>user_id</code> in a <code>users</code> table and the <code>user_id</code> in an <code>orders</code> table, so that no order can be created against a user that does not exist.</p>
<p>Foreign key constraints can also prevent you from deleting rows that reference rows in other tables. For example, deleting rows from the <code>users</code> table when rows in the <code>orders</code> table refer to them.</p>
<p>By default, D1 enforces that foreign key constraints are valid within all queries and migrations. This is identical to the behaviour you would observe when setting <code>PRAGMA foreign_keys = on</code> in SQLite for every transaction.</p>
<h2 id="defer-foreign-key-constraints">Defer foreign key constraints</h2>
<p>When running a <a href="/d1/worker-api/">query</a>, <a href="/d1/reference/migrations/">migration</a> or <a href="/d1/best-practices/import-export-data/">importing data</a> against a D1 database, there may be situations in which you need to disable foreign key validation during table creation or changes to your schema.</p>
<p>D1's foreign key enforcement is equivalent to SQLite's <code>PRAGMA foreign_keys = on</code> directive. Because D1 runs every query inside an implicit transaction, user queries cannot change this during a query or migration.</p>
<p>Instead, D1 allows you to call <code>PRAGMA defer_foreign_keys = on</code> or <code>off</code>, which allows you to violate foreign key constraints temporarily (until the end of the current transaction).</p>
<p>Calling <code>PRAGMA defer_foreign_keys = off</code> does not disable foreign key enforcement outside of the current transaction. If you have not resolved outstanding foreign key violations at the end of your transaction, it will fail with a <code>FOREIGN KEY constraint failed</code> error.</p>
<p>To defer foreign key enforcement, set <code>PRAGMA defer_foreign_keys = on</code> at the start of your transaction, or ahead of changes that would violate constraints:</p>
<pre tabindex="0"><code class="language-sql">&#45;- Defer foreign key enforcement in this transaction.&#10;PRAGMA defer_foreign_keys = on&#10;&#10;&#45;- Run your CREATE TABLE or ALTER TABLE / COLUMN statements&#10;ALTER TABLE users ...&#10;&#10;&#45;- This is implicit if not set by the end of the transaction.&#10;PRAGMA defer_foreign_keys = off&#10;</code></pre>
<p>You can also explicitly set <code>PRAGMA defer_foreign_keys = off</code> immediately after you have resolved outstanding foreign key constraints. If there are still outstanding foreign key constraints, you will receive a <code>FOREIGN KEY constraint failed</code> error and will need to resolve the violation.</p>
<h2 id="define-a-foreign-key-relationship">Define a foreign key relationship</h2>
<p>A foreign key relationship can be defined when creating a table via <code>CREATE TABLE</code> or when adding a column to an existing table via an <code>ALTER TABLE</code> statement.</p>
<p>To illustrate this with an example based on an e-commerce website with two tables:</p>
<ul>
<li>A <code>users</code> table that defines common properties about a user account, including a unique <code>user_id</code> identifier.</li>
<li>An <code>orders</code> table that maps an order back to a <code>user_id</code> in the user table.</li>
</ul>
<p>This mapping is defined as <code>FOREIGN KEY</code>, which ensures that:</p>
<ul>
<li>You cannot delete a row from the <code>users</code> table that would violate the foreign key constraint. This means that you cannot end up with orders that do not have a valid user to map back to.</li>
<li><code>orders</code> are always defined against a valid <code>user_id</code>, mitigating the risk of creating orders that refer to invalid (or non-existent) users.</li>
</ul>
<pre tabindex="0"><code class="language-sql">CREATE TABLE users (&#10;    user_id INTEGER PRIMARY KEY,&#10;    email_address TEXT,&#10;    name TEXT,&#10;    metadata TEXT&#10;)&#10;&#10;CREATE TABLE orders (&#10;    order_id INTEGER PRIMARY KEY,&#10;    status INTEGER,&#10;    item_desc TEXT,&#10;    shipped_date INTEGER,&#10;    user_who_ordered INTEGER,&#10;    FOREIGN KEY(user_who_ordered) REFERENCES users(user_id)&#10;)&#10;</code></pre>
<p>You can define multiple foreign key relationships per-table, and foreign key definitions can reference multiple tables within your overall database schema.</p>
<h2 id="foreign-key-actions">Foreign key actions</h2>
<p>You can define <em>actions</em> as part of your foreign key definitions to either limit or propagate changes to a parent row (<code>REFERENCES table(column)</code>). Defining <em>actions</em> makes using foreign key constraints in your application easier to reason about, and help either clean up related data or prevent data from being islanded.</p>
<p>There are five actions you can set when defining the <code>ON UPDATE</code> and/or <code>ON DELETE</code> clauses as part of a foreign key relationship. You can also define different actions for <code>ON UPDATE</code> and <code>ON DELETE</code> depending on your requirements.</p>
<ul>
<li><code>CASCADE</code> - Updating or deleting a parent key deletes all child keys (rows) associated to it.</li>
<li><code>RESTRICT</code> - A parent key cannot be updated or deleted when <em>any</em> child key refers to it. Unlike the default foreign key enforcement, relationships with <code>RESTRICT</code> applied return errors immediately, and not at the end of the transaction.</li>
<li><code>SET DEFAULT</code> - Set the child column(s) referred to by the foreign key definition to the <code>DEFAULT</code> value defined in the schema. If no <code>DEFAULT</code> is set on the child columns, you cannot use this action.</li>
<li><code>SET NULL</code> - Set the child column(s) referred to by the foreign key definition to SQL <code>NULL</code>.</li>
<li><code>NO ACTION</code> - Take no action.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="cascade-usage">CASCADE usage</h3>
@markup("md", "content/.markup/bodies/7330.md")
</aside>
<p>In the following example, deleting a user from the <code>users</code> table will delete all related rows in the <code>scores</code> table as you have defined <code>ON DELETE CASCADE</code>. Delete all related rows in the <code>scores</code> table if you do not want to retain the scores for any users you have deleted entirely. This might mean that <em>other</em> users can no longer look up or refer to scores that were still valid.</p>
<pre tabindex="0"><code class="language-sql">CREATE TABLE users (&#10;    user_id INTEGER PRIMARY KEY,&#10;    email_address TEXT,&#10;)&#10;&#10;CREATE TABLE scores (&#10;    score_id INTEGER PRIMARY KEY,&#10;    game TEXT,&#10;    score INTEGER,&#10;    player_id INTEGER,&#10;    FOREIGN KEY(player_id) REFERENCES users(user_id) ON DELETE CASCADE&#10;)&#10;</code></pre>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li>Read the SQLite <a href="https://www.sqlite.org/foreignkeys.html"><code>FOREIGN KEY</code></a> documentation.</li>
<li>Learn how to <a href="/d1/worker-api/">use the D1 Workers Binding API</a> from within a Worker.</li>
<li>Understand how <a href="/d1/reference/migrations/">database migrations work</a> with D1.</li>
</ul>
