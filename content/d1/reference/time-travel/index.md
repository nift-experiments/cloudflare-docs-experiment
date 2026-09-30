<p>Time Travel is D1's approach to backups and point-in-time-recovery, and allows you to restore a database to any minute within the last 30 days.</p>
<ul>
<li>You do not need to enable Time Travel. It is always on.</li>
<li>Database history and restoring a database incur no additional costs.</li>
<li>Time Travel automatically creates <a href="#bookmarks">bookmarks</a> on your behalf. You do not need to manually trigger or remember to initiate a backup.</li>
</ul>
<p>By not having to rely on scheduled backups and/or manually initiated backups, you can go back in time and restore a database prior to a failed migration or schema change, a <code>DELETE</code> or <code>UPDATE</code> statement without a specific <code>WHERE</code> clause, and in the future, fork/copy a production database directly.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="support-for-time-travel">Support for Time Travel</h3>
@markup("md", "content/.markup/bodies/7332.md")
</aside>
<h2 id="bookmarks">Bookmarks</h2>
<p>Time Travel leverages D1's concept of a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7333.md")
</div> to restore to a point in time.
<ul>
<li>Bookmarks older than 30 days are invalid and cannot be used as a restore point.</li>
<li>Restoring a database to a specific bookmark does not remove or delete older bookmarks. For example, if you restore to a bookmark representing the state of your database 10 minutes ago, and determine that you needed to restore to an earlier point in time, you can still do so.</li>
<li>Bookmarks are lexicographically sortable. Sorting orders a list of bookmarks from oldest-to-newest.</li>
<li>Bookmarks can be derived from a <a href="https://en.wikipedia.org/wiki/Unix_time">Unix timestamp</a> (seconds since Jan 1st, 1970), and conversion between a specific timestamp and a bookmark is deterministic (stable).</li>
</ul>
<p>Bookmarks are also leveraged by <a href="/d1/best-practices/read-replication/#use-sessions-api">Sessions API</a> to ensure sequential consistency within a Session.</p>
<h2 id="timestamps">Timestamps</h2>
<p>Time Travel supports two timestamp formats:</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Unix_time">Unix timestamps</a>, which correspond to seconds since January 1st, 1970 at midnight. This is always in UTC.</li>
<li>The <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format">JavaScript date-time string format</a>, which is a simplified version of the ISO-8601 timestamp format. An valid date-time string for the July 27, 2023 at 11:18AM in Americas/New_York (EST) would look like <code>2023-07-27T11:18:53.000-04:00</code>.</li>
</ul>
<h2 id="requirements">Requirements</h2>
<ul>
<li><a href="/workers/wrangler/install-and-update/"><code>Wrangler</code></a> <code>v3.4.0</code> or later installed to use Time Travel commands.</li>
<li>A database on D1's production backend. You can check whether a database is using this backend via <code>wrangler d1 info DB_NAME</code> - the output show <code>version: production</code>.</li>
</ul>
<h2 id="retrieve-a-bookmark">Retrieve a bookmark</h2>
<p>You can retrieve a bookmark for the current timestamp by calling the <code>d1 info</code> command, which defaults to returning the current bookmark:</p>
<pre><code class="language-sh">wrangler d1 time-travel info YOUR_DATABASE&#10;</code></pre>
<pre><code class="language-sh">🚧 Time Traveling...&#10;⚠️ The current bookmark is &#x27;00000085-0000024c-00004c6d-8e61117bf38d7adb71b934ebbf891683&#x27;&#10;⚡️ To restore to this specific bookmark, run:&#10; `wrangler d1 time-travel restore YOUR_DATABASE --bookmark=00000085-0000024c-00004c6d-8e61117bf38d7adb71b934ebbf891683`&#10;</code></pre>
<p>To retrieve the bookmark for a timestamp in the past, pass the <code>--timestamp</code> flag with a valid Unix or RFC3339 timestamp:</p>
<pre><code class="language-sh">wrangler d1 time-travel info YOUR_DATABASE --timestamp=&quot;2023-07-09T17:31:11+00:00&quot;&#10;</code></pre>
<h2 id="restore-a-database">Restore a database</h2>
<p>To restore a database to a specific point-in-time:</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7331.md")
</aside>
<pre><code class="language-sh">wrangler d1 time-travel restore YOUR_DATABASE --timestamp=UNIX_TIMESTAMP&#10;</code></pre>
<pre><code class="language-sh">🚧 Restoring database YOUR_DATABASE from bookmark 00000080-ffffffff-00004c60-390376cb1c4dd679b74a19d19f5ca5be&#10;&#10;⚠️ This will overwrite all data in database YOUR_DATABASE.&#10;In-flight queries and transactions will be cancelled.&#10;&#10;✔ OK to proceed (y/N) … yes&#10;⚡️ Time travel in progress...&#10;✅ Database YOUR_DATABASE restored back to bookmark 00000080-ffffffff-00004c60-390376cb1c4dd679b74a19d19f5ca5be&#10;&#10;↩️ To undo this operation, you can restore to the previous bookmark: 00000085-ffffffff-00004c6d-2510c8b03a2eb2c48b2422bb3b33fad5&#10;</code></pre>
<p>Note that:</p>
<ul>
<li>Timestamps are converted to a deterministic, stable bookmark. The same timestamp will always represent the same bookmark.</li>
<li>Queries in flight will be cancelled, and an error returned to the client.</li>
<li>The restore operation will return a <a href="#bookmarks">bookmark</a> that allows you to <a href="#undo-a-restore">undo</a> and revert the database.</li>
</ul>
<h2 id="undo-a-restore">Undo a restore</h2>
<p>You can undo a restore by:</p>
<ul>
<li>Taking note of the previous bookmark returned as part of a <code>wrangler d1 time-travel restore</code> operation</li>
<li>Restoring directly to a bookmark in the past, prior to your last restore.</li>
</ul>
<p>To fetch a bookmark from an earlier state:</p>
<pre><code class="language-sh">wrangler d1 time-travel info YOUR_DATABASE&#10;</code></pre>
<pre><code class="language-sh">🚧 Time Traveling...&#10;⚠️ The current bookmark is &#x27;00000085-0000024c-00004c6d-8e61117bf38d7adb71b934ebbf891683&#x27;&#10;⚡️ To restore to this specific bookmark, run:&#10; `wrangler d1 time-travel restore YOUR_DATABASE --bookmark=00000085-0000024c-00004c6d-8e61117bf38d7adb71b934ebbf891683`&#10;</code></pre>
<h2 id="export-d1-into-r2-using-workflows">Export D1 into R2 using Workflows</h2>
<p>You can automatically export your D1 database into R2 storage via REST API and Cloudflare Workflows. This may be useful if you wish to store a state of your D1 database for longer than 30 days.</p>
<p>Refer to the guide <a href="/workflows/examples/backup-d1/">Export and save D1 database</a>.</p>
<h2 id="notes">Notes</h2>
<ul>
<li>You can quickly get the Unix timestamp from the command-line in macOS and Windows via <code>date +%s</code>.</li>
<li>Time Travel does not yet allow you to clone or fork an existing database to a new copy. In the future, Time Travel will allow you to fork (clone) an existing database into a new database, or overwrite an existing database.</li>
<li>You can restore a database back to a point in time up to 30 days in the past (Workers Paid plan) or 7 days (Workers Free plan). Refer to <a href="/d1/platform/limits/">Limits</a> for details on Time Travel's limits.</li>
</ul>
