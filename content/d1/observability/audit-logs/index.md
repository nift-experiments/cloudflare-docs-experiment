<p><a href="/fundamentals/account/account-security/review-audit-logs/">Audit logs</a> provide a comprehensive summary of changes made within your Cloudflare account, including those made to D1 databases. This functionality is available on all plan types, free of charge, and is always enabled.</p>
<h2 id="viewing-audit-logs">Viewing audit logs</h2>
<p>To view audit logs for your D1 databases, go to the <strong>Audit Logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>For more information on how to access and use audit logs, refer to <a href="/fundamentals/account/account-security/review-audit-logs/">Review audit logs</a>.</p>
<h2 id="logged-operations">Logged operations</h2>
<p>The following configuration actions are logged:</p>
<table>
<tbody>
<th colspan="5" rowspan="1" style="width:220px">
			Operation
</th>
<th colspan="5" rowspan="1">
			Description
</th>
<tr>
<td colspan="5" rowspan="1">
				CreateDatabase
</td>
<td colspan="5" rowspan="1">
				Creation of a new database.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				DeleteDatabase
</td>
<td colspan="5" rowspan="1">
				Deletion of an existing database.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				<a href="/d1/reference/time-travel">TimeTravel</a>
</td>
<td colspan="5" rowspan="1">
				Restoration of a past database version.
</td>
</tr>
</tbody>
</table>
<h2 id="example-log-entry">Example log entry</h2>
<p>Below is an example of an audit log entry showing the creation of a new database:</p>
<pre><code class="language-json">{&#10;	&quot;action&quot;: { &quot;info&quot;: &quot;CreateDatabase&quot;, &quot;result&quot;: true, &quot;type&quot;: &quot;create&quot; },&#10;	&quot;actor&quot;: {&#10;		&quot;email&quot;: &quot;&lt;ACTOR_EMAIL&gt;&quot;,&#10;		&quot;id&quot;: &quot;b1ab1021a61b1b12612a51b128baa172&quot;,&#10;		&quot;ip&quot;: &quot;1b11:a1b2:12b1:12a::11a:1b&quot;,&#10;		&quot;type&quot;: &quot;user&quot;&#10;	},&#10;	&quot;id&quot;: &quot;a123b12a-ab11-1212-ab1a-a1aa11a11abb&quot;,&#10;	&quot;interface&quot;: &quot;API&quot;,&#10;	&quot;metadata&quot;: {},&#10;	&quot;newValue&quot;: &quot;&quot;,&#10;	&quot;newValueJson&quot;: { &quot;database_name&quot;: &quot;my-db&quot; },&#10;	&quot;oldValue&quot;: &quot;&quot;,&#10;	&quot;oldValueJson&quot;: {},&#10;	&quot;owner&quot;: { &quot;id&quot;: &quot;211b1a74121aa32a19121a88a712aa12&quot; },&#10;	&quot;resource&quot;: {&#10;		&quot;id&quot;: &quot;11a21122-1a11-12bb-11ab-1aa2aa1ab12a&quot;,&#10;		&quot;type&quot;: &quot;d1.database&quot;&#10;	},&#10;	&quot;when&quot;: &quot;2024-08-09T04:53:55.752Z&quot;&#10;}&#10;</code></pre>
