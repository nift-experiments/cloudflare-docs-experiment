<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9635.md")
</aside>
<p>Audit logs summarize the history of changes made within your Cloudflare account. Audit logs include account level actions like login, as well as zone configuration changes.</p>
<p>Audit Logs are available on all plan types and are captured for both individual users and for multi-user organizations.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9634.md")
</aside>
<p>Audit logs are available in the dashboard as well as the API.</p>
<h3 id="using-the-dashboard">Using the dashboard</h3>
<p>To access audit logs in the Cloudflare dashboard:</p>
<p>In the Cloudflare dashboard, go to the <strong>Audit Logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>You can search these audit logs by user email or domain and filter by date range. To download audit logs, click <strong>Download CSV</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9633.md")
</aside>
<h3 id="using-the-api">Using the API</h3>
<p>To get audit logs from the Cloudflare API, send a <a href="/api/resources/audit_logs/methods/list/">GET request</a>.</p>
<p>We recommending using the API for downloading historical audit log data.</p>
<p>To maintain Audit Logs query performance, the Audit Logs API was modified on 2019-06-30 to return records with a maximum age of 18 months.</p>
