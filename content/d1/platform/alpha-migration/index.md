<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7346.md")
</aside>
<p>D1's open beta launched in October 2023, and newly created databases use a different underlying architecture that is significantly more reliable and performant, with increased database sizes, improved query throughput, and reduced latency.</p>
<p>This guide will instruct you to recreate alpha D1 databases on our production-ready system.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>You have the <a href="/workers/wrangler/install-and-update/"><code>wrangler</code> command-line tool</a> installed</li>
<li>You are using <code>wrangler</code> version <code>3.33.0</code> or later (released March 2024) as earlier versions do not have the <a href="/d1/platform/release-notes/#2024-03-12"><code>--remote</code> flag</a> required as part of this guide</li>
<li>An 'alpha' D1 database. All databases created before July 27th, 2023 (<a href="/d1/platform/release-notes/#2024-03-12">release notes</a>) use the alpha storage backend, which is no longer supported and was not recommended for production.</li>
</ol>
<h2 id="1-verify-that-a-database-is-alpha"><ol>
<li>Verify that a database is alpha</li>
</ol></h2>
<pre><code class="language-sh">npx wrangler d1 info &lt;database_name&gt;&#10;</code></pre>
<p>If the database is alpha, the output of the command will include <code>version</code> set to <code>alpha</code>:</p>
<pre><code>...&#10;│ version           │ alpha                                 │&#10;...&#10;</code></pre>
<h2 id="2-create-a-manual-backup"><ol start="2">
<li>Create a manual backup</li>
</ol></h2>
<pre><code class="language-sh">npx wrangler d1 backup create &lt;alpha_database_name&gt;&#10;</code></pre>
<h2 id="3-download-the-manual-backup"><ol start="3">
<li>Download the manual backup</li>
</ol></h2>
<p>The command below will download the manual backup of the alpha database as <code>.sqlite3</code> file:</p>
<pre><code class="language-sh">npx wrangler d1 backup download &lt;alpha_database_name&gt; &lt;backup_id&gt; # See available backups with wrangler d1 backup list &lt;database_name&gt;&#10;</code></pre>
<h2 id="4-convert-the-manual-backup-into-sql-statements"><ol start="4">
<li>Convert the manual backup into SQL statements</li>
</ol></h2>
<p>The command below will convert the manual backup of the alpha database from the downloaded <code>.sqlite3</code> file into SQL statements which can then be imported into the new database:</p>
<pre><code class="language-sh">sqlite3 db_dump.sqlite3 .dump &gt; db.sql&#10;</code></pre>
<p>Once you have run the above command, you will need to edit the output SQL file to be compatible with D1:</p>
<ol>
<li>Remove <code>BEGIN TRANSACTION</code> and <code>COMMIT;</code> from the file.</li>
<li>Remove the following table creation statement:</li>
</ol>
<pre><code class="language-sql">CREATE TABLE _cf_KV (&#10; 	key TEXT PRIMARY KEY,&#10; 	value BLOB&#10;) WITHOUT ROWID;&#10;</code></pre>
<h2 id="5-create-a-new-d1-database"><ol start="5">
<li>Create a new D1 database</li>
</ol></h2>
<p>All new D1 databases use the updated architecture by default.</p>
<p>Run the following command to create a new database:</p>
<pre><code class="language-sh">npx wrangler d1 create &lt;new_database_name&gt;&#10;</code></pre>
<h2 id="6-run-sql-statements-against-the-new-d1-database"><ol start="6">
<li>Run SQL statements against the new D1 database</li>
</ol></h2>
<pre><code class="language-sh">npx wrangler d1 execute &lt;new_database_name&gt; --remote --file=./db.sql&#10;</code></pre>
<h2 id="7-delete-your-alpha-database"><ol start="7">
<li>Delete your alpha database</li>
</ol></h2>
<p>To delete your previous alpha database, run:</p>
<pre><code class="language-sh">npx wrangler d1 delete &lt;alpha_database_name&gt;&#10;</code></pre>
