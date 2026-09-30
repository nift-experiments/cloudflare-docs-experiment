<p>Check the <strong>Security Insights</strong> tab for a list of detected insights that you should address.</p>
<p>For each detected insight, you can resolve it or archive it, after understanding its risks.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Next to the insight you wish to address, select <strong>Details</strong> to review it.</li>
</ol>
<h2 id="resolve-an-insight">Resolve an insight</h2>
<aside class="nb-aside warning">
@markup("md", "content/.markup/bodies/13843.md")
</aside>
<p>In the Resolve insights page, if you choose to update a configuration based on the recommendation actions, follow the instructions on the insight details page.</p>
<p>The following insights follow a different yet straightforward workflow to be resolved:</p>
<ul>
<li><strong>Minimum Version of TLS 1.2 not enforced</strong>: To resolve this insight:
<ul>
<li>Go to <strong>SSL/TLS</strong> &gt; <strong>Edge Certificates</strong>.</li>
<li>Select <strong>TLS 1.2</strong>.</li>
</ul>
</li>
<li><strong>Domains without &quot;Always use HTTPS&quot;</strong>: To resolve this insight:
<ul>
<li>Go to <strong>SSL/TLS</strong> &gt; <strong>Edge Certificates</strong>.</li>
<li>Select <strong>Always Use HTTPS</strong>.</li>
</ul>
</li>
<li><strong>Turn on JavaScript Detections</strong>: To resolve this insight:
<ul>
<li>Go to <strong>Security</strong> &gt; <strong>Bots</strong> &gt; Select <strong>Configure Bot Management</strong>.</li>
<li>Select <strong>JavaScript Detections</strong>.</li>
</ul>
</li>
</ul>
<h2 id="export-insights">Export insights</h2>
<p>You can export security insights to a CSV format directly from the dashboard.</p>
<p>To export security insights:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Export insights</strong>.</li>
</ol>
<p>Exporting security insights allow you to perform a deeper analysis of your insights.</p>
<p>The exported CSV file includes information such as the severity of your data, insight type scan date, issue class and additional optional fields, such as insight details, risk assessment, detection method, and recommended actions.</p>
<h2 id="archive-insights">Archive insights</h2>
<p>You can archive one or more insights from the dashboard.</p>
<p>To archive insights:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the insight(s) you want to archive, then select <strong>Archive selected</strong>.</li>
</ol>
<p>Alternatively, to archive an insight:</p>
<ol>
<li>Select the insight you want to archive and select <strong>Details</strong>. The dashboard will open a page where you will be able to review <a href="/security/security-insights/how-it-works/#scan-properties">insight properties</a>.</li>
<li>Select <strong>Archive insight</strong>.</li>
</ol>
<h2 id="enable-alerts">Enable alerts</h2>
<p>You can enable alerts for critical insights.</p>
<p>To enable alerts:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the security insight(s) you want to create an alert for, then select <strong>Create alert for selected classes</strong>.</li>
<li>Enter the notification name, and choose one or more insights classes to filter a notification.</li>
<li>Select <strong>Add email recipient</strong> and enter an email address to receive the alert.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
