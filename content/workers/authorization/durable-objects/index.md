<p>Durable Objects do not have separate roles or permissions. Access to a Durable Object is determined by your access to the Worker that implements it.</p>
<p>To give a member, User Group, or API token access to a Durable Object, assign the appropriate Workers role at either the individual Worker scope or the Workers product scope. Refer to <a href="/workers/authorization/workers/">Workers roles and permissions</a> for available roles and scopes.</p>
<h2 id="observability-access">Observability access</h2>
<p><code>Metadata Read-Only</code> access to the implementing Worker includes Durable Object metrics, logs, and traces without granting access to data stored in the Durable Object. Granular authorization supports analytics for both SQLite-backed and KV-backed Durable Objects, with one current exception: the <strong>Total KV storage</strong> metric is unavailable for KV-backed Durable Objects.</p>
<h2 id="data-studio-access">Data Studio access</h2>
<p><a href="/durable-objects/observability/data-studio/">Durable Objects Data Studio</a> can query and modify data stored in SQLite-backed Durable Objects. Accessing Data Studio requires at least <code>Editor</code> access to the Worker that implements the Durable Object.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/authorization/workers/">Workers roles and permissions</a></li>
<li><a href="/durable-objects/observability/metrics-and-analytics/">Durable Objects metrics and analytics</a></li>
<li><a href="/durable-objects/observability/data-studio/">Durable Objects Data Studio</a></li>
</ul>
