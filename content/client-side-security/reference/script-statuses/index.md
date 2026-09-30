<p>Cloudflare classifies scripts and connections (also known as resources) according to the following:</p>
<ul>
<li>The number of times a script/connection was reported.</li>
<li>Whether the script/connection is considered malicious or not.</li>
</ul>
<p>Use client-side security's dashboards to review the scripts loaded in your domain and the connections they make. For more information, refer to <a href="/client-side-security/detection/monitor-connections-scripts/">Monitor resources and cookies</a>.</p>
<h2 id="available-statuses">Available statuses</h2>
<ul>
<li><strong>Infrequent</strong>: There are less than three reports for the script/connection. If there are no reports for a script/connection with <em>Infrequent</em> status for five days, then Cloudflare will delete all the information about the script/connection. Scripts with <em>Infrequent</em> status appear only in the All Reported Scripts dashboard, and connections with <em>Infrequent</em> status appear only in the All Reported Connections dashboard.</li>
<li><strong>Active</strong>: There are more than three reports for the script/connection.</li>
<li><strong>Inactive</strong>: A previously active script/connection was not reported in the last seven days. If the script/connection is reported again later, its status will change back to <em>Active</em>. If the script/connection is not reported for 30 days, Cloudflare will delete all the information about it. Scripts with <em>Inactive</em> status appear only in the All Reported Scripts dashboard, and connections with <em>Inactive</em> status appear only in the All Reported Connections dashboard.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3976.md")
</aside>
