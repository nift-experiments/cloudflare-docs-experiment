<p><a href="/fundamentals/account/account-security/review-audit-logs/">Audit logs</a> provide a comprehensive summary of changes made within your Cloudflare account, including those made to gateways in AI Gateway. This functionality is available on all plan types, free of charge, and is enabled by default.</p>
<h2 id="viewing-audit-logs">Viewing Audit Logs</h2>
<p>To view audit logs for AI Gateway, in the Cloudflare dashboard, go to the <strong>Audit logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>For more information on how to access and use audit logs, refer to <a href="/fundamentals/account/account-security/review-audit-logs/">review audit logs documentation</a>.</p>
<h2 id="logged-operations">Logged Operations</h2>
<p>The following configuration actions are logged:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>gateway created</td>
<td>Creation of a new gateway.</td>
</tr>
<tr>
<td>gateway deleted</td>
<td>Deletion of an existing gateway.</td>
</tr>
<tr>
<td>gateway updated</td>
<td>Edit of an existing gateway.</td>
</tr>
</tbody>
</table>
<h2 id="example-log-entry">Example Log Entry</h2>
<p>Below is an example of an audit log entry showing the creation of a new gateway:</p>
<pre><code class="language-json">{&#10; &quot;action&quot;: {&#10;     &quot;info&quot;: &quot;gateway created&quot;,&#10;     &quot;result&quot;: true,&#10;     &quot;type&quot;: &quot;create&quot;&#10; },&#10; &quot;actor&quot;: {&#10;     &quot;email&quot;: &quot;&lt;ACTOR_EMAIL&gt;&quot;,&#10;     &quot;id&quot;: &quot;3f7b730e625b975bc1231234cfbec091&quot;,&#10;     &quot;ip&quot;: &quot;fe32:43ed:12b5:526::1d2:13&quot;,&#10;     &quot;type&quot;: &quot;user&quot;&#10; },&#10; &quot;id&quot;: &quot;5eaeb6be-1234-406a-87ab-1971adc1234c&quot;,&#10; &quot;interface&quot;: &quot;UI&quot;,&#10; &quot;metadata&quot;: {},&#10; &quot;newValue&quot;: &quot;&quot;,&#10; &quot;newValueJson&quot;: {&#10;     &quot;cache_invalidate_on_update&quot;: false,&#10;     &quot;cache_ttl&quot;: 0,&#10;     &quot;collect_logs&quot;: true,&#10;     &quot;id&quot;: &quot;test&quot;,&#10;     &quot;rate_limiting_interval&quot;: 0,&#10;     &quot;rate_limiting_limit&quot;: 0,&#10;     &quot;rate_limiting_technique&quot;: &quot;fixed&quot;&#10; },&#10; &quot;oldValue&quot;: &quot;&quot;,&#10; &quot;oldValueJson&quot;: {},&#10; &quot;owner&quot;: {&#10;     &quot;id&quot;: &quot;1234d848c0b9e484dfc37ec392b5fa8a&quot;&#10; },&#10; &quot;resource&quot;: {&#10;     &quot;id&quot;: &quot;89303df8-1234-4cfa-a0f8-0bd848e831ca&quot;,&#10;     &quot;type&quot;: &quot;ai_gateway.gateway&quot;&#10; },&#10; &quot;when&quot;: &quot;2024-07-17T14:06:11.425Z&quot;&#10;}&#10;</code></pre>
