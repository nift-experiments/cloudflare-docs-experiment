<p>D1 has built-in support for creating and restoring backups of your databases with wrangler v3, including support for scheduled automatic backups and manual backup management.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="planned-removal">Planned removal</h3>
@markup("md", "content/.markup/bodies/7341.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="time-travel">Time Travel</h3>
@markup("md", "content/.markup/bodies/7340.md")
</aside>
<h2 id="automatic-backups">Automatic backups</h2>
<p>D1 automatically backs up your databases every hour on your behalf, and <a href="/d1/platform/limits/">retains backups for 24 hours</a>. Backups will block access to the DB while they are running. In most cases this should only be a second or two, and any requests that arrive during the backup will be queued.</p>
<p>To view and manage these backups, including any manual backups you have made, you can use the <code>d1 backup list &lt;DATABASE_NAME&gt;</code> command to list each backup.</p>
<p>For example, to list all of the backups of a D1 database named <code>existing-db</code>:</p>
<pre><code class="language-sh">wrangler d1 backup list existing-db&#10;</code></pre>
<pre><code class="language-sh">&#10;┌──────────────┬──────────────────────────────────────┬────────────┬─────────┐&#10;│ created_at   │ id                                   │ num_tables │ size    │&#10;├──────────────┼──────────────────────────────────────┼────────────┼─────────┤&#10;│ 1 hour ago   │ 54a23309-db00-4c5c-92b1-c977633b937c │ 1          │ 95.3 kB │&#10;├──────────────┼──────────────────────────────────────┼────────────┼─────────┤&#10;│ &lt;...&gt;        │ &lt;...&gt;                                │ &lt;...&gt;      │ &lt;...&gt;   │&#10;├──────────────┼──────────────────────────────────────┼────────────┼─────────┤&#10;│ 2 months ago │ 8433a91e-86d0-41a3-b1a3-333b080bca16 │ 1          │ 65.5 kB │&#10;└──────────────┴──────────────────────────────────────┴────────────┴─────────┘%&#10;</code></pre>
<p>The <code>id</code> of each backup allows you to download or restore a specific backup.</p>
<h2 id="manually-back-up-a-database">Manually back up a database</h2>
<p>Creating a manual backup of your database before making large schema changes, manually inserting or deleting data, or otherwise modifying a database you are actively using is a good practice to get into. D1 allows you to make a backup of a database at any time, and stores the backup on your behalf. You should also consider <a href="/d1/reference/migrations/">using migrations</a> to simplify changes to an existing database.</p>
<p>To back up a D1 database, you must have:</p>
<ol>
<li>The Cloudflare <a href="/workers/wrangler/install-and-update/">Wrangler CLI installed</a></li>
<li>An existing D1 database you want to back up.</li>
</ol>
<p>For example, to create a manual backup of a D1 database named <code>example-db</code>, call <code>d1 backup create</code>.</p>
<pre><code class="language-sh">wrangler d1 backup create example-db&#10;</code></pre>
<pre><code class="language-sh">┌─────────────────────────────┬──────────────────────────────────────┬────────────┬─────────┬───────┐&#10;│ created_at                  │ id                                   │ num_tables │ size    │ state │&#10;├─────────────────────────────┼──────────────────────────────────────┼────────────┼─────────┼───────┤&#10;│ 2023-02-04T15:49:36.113753Z │ 123a81a2-ab91-4c2e-8ebc-64d69633faf1 │ 1          │ 65.5 kB │ done  │&#10;└─────────────────────────────┴──────────────────────────────────────┴────────────┴─────────┴───────┘&#10;</code></pre>
<p>Larger databases, especially those that are several megabytes (MB) in size with many tables, may take a few seconds to backup. The <code>state</code> column in the output will let you know when the backup is done.</p>
<h2 id="downloading-a-backup-locally">Downloading a backup locally</h2>
<p>To download a backup locally, call <code>wrangler d1 backup download &lt;DATABASE_NAME&gt; &lt;BACKUP_ID&gt;</code>. Use <code>wrangler d1 backup list &lt;DATABASE_NAME&gt;</code> to list the available backups, including their IDs, for a given D1 database.</p>
<p>For example, to download a specific backup for a database named <code>example-db</code>:</p>
<pre><code class="language-sh">wrangler d1 backup download example-db 123a81a2-ab91-4c2e-8ebc-64d69633faf1&#10;</code></pre>
<pre><code class="language-sh">&#10;🌀 Downloading backup 123a81a2-ab91-4c2e-8ebc-64d69633faf1 from &#x27;example-db&#x27;&#10;🌀 Saving to /Users/you/projects/example-db.123a81a2.sqlite3&#10;🌀 Done!&#10;</code></pre>
<p>The database backup will be download to the current working directory in native SQLite3 format. To import a local database, read <a href="/d1/best-practices/import-export-data/">the documentation on importing data</a> to D1.</p>
<h2 id="restoring-a-backup">Restoring a backup</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7339.md")
</aside>
<p>Restoring a backup will overwrite the current running version of a database with the backup. Database tables (and their data) that do not exist in the backup will no longer exist in the current version of the database, and queries that rely on them will fail.</p>
<p>To restore a previous backup of a D1 database named <code>existing-db</code>, pass the ID of that backup to <code>d1 backup restore</code>:</p>
<pre><code class="language-sh">wrangler d1 backup restore existing-db  6cceaf8c-ceab-4351-ac85-7f9e606973e3&#10;</code></pre>
<pre><code class="language-sh">Restoring existing-db from backup 6cceaf8c-ceab-4351-ac85-7f9e606973e3....&#10;Done!&#10;</code></pre>
<p>Any queries against the database will immediately query the current (restored) version once the restore has completed.</p>
