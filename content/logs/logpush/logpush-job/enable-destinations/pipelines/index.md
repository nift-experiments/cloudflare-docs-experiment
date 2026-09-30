<p><a href="/pipelines/">Cloudflare Pipelines</a> ingests events, transforms them with <a href="/pipelines/sql-reference/">SQL</a>, and delivers them to <a href="/r2/">R2</a> as <a href="/r2-data-catalog/">Iceberg</a> tables or as Parquet and JSON files. Logpush can write data to Pipelines as a native destination.</p>
<p>Instead of sending raw logs directly to a storage bucket as JSON, Logpush can route them to a Pipeline to filter, enrich, and transform your data into Parquet or Apache Iceberg tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>. This allows the data to be much more compact and optimized for analytics such as querying with <a href="/r2-sql/">R2 SQL</a>.</p>
<p>The Pipelines destination supports the following Logpush datasets:</p>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Datasets</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zone</td>
<td><code>http_requests</code>, <code>firewall_events</code>, <code>dns_logs</code></td>
</tr>
<tr>
<td>Account</td>
<td><code>workers_trace_events</code></td>
</tr>
</tbody>
</table>
<p>For a full list of fields available in each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Datasets</a>.</p>
<h2 id="manage-via-the-cloudflare-dashboard">Manage via the Cloudflare dashboard</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/10549.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10548.md")
</aside>
