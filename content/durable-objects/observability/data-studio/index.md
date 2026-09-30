<p>Each Durable Object can access private storage using <a href="/durable-objects/api/sqlite-storage-api/">Storage API</a> available on <code>ctx.storage</code>. To view and write to an object's stored data, you can use Durable Objects Data Studio as a UI editor available on the Cloudflare dashboard.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="data-studio-only-supported-for-sqlite-backed-objects">Data Studio only supported for SQLite-backed objects</h3>
@markup("md", "content/.markup/bodies/8175.md")
</aside>
<h2 id="view-data-studio">View Data Studio</h2>
<p>You need at least <code>Editor</code> access to the Worker that implements the Durable Object to access Data Studio. Refer to <a href="/workers/authorization/durable-objects/">Durable Objects roles and permissions</a> for more information.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8176.md")
</div>
<ul>
<li>Queries executed by Data Studio send requests to your remote, deployed objects and incur <a href="/durable-objects/platform/pricing/">usage billing</a> for requests, duration, rows read, and rows written. You should use Data Studio as you would handle your production, running objects.</li>
<li>In the <strong>Query</strong> tab when running all statements, each SQL statement is sent as a separate Durable Object request.</li>
</ul>
<h2 id="audit-logging">Audit logging</h2>
<p>All queries issued by the Data Studio are logged with <a href="/fundamentals/account/account-security/review-audit-logs/">audit logging v1</a> for your security and compliance needs.</p>
<ul>
<li>Each query emits two audit logs, a <code>query executed</code> action and a <code>query completed</code> action indicating query success or failure. <code>query_id</code> in the log event can be used to correlate the two events per query.</li>
</ul>
