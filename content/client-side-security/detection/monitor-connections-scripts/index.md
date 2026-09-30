<p>Once you <a href="/client-side-security/get-started/">activate client-side security's resource monitoring</a>, the main client-side resources dashboard will show which resources (scripts and connections) are running on your domain, as well as the cookies recently detected in HTTP traffic.</p>
<p>If you notice unexpected scripts or connections on the dashboard, check them for signs of malicious activity. Customers with Client-Side Security Advanced will have their <a href="/client-side-security/how-it-works/malicious-script-detection/">connections and scripts classified as potentially malicious</a> based on threat feeds. You should also check for any new or unexpected cookies.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/4001.md")
</aside>
<h2 id="use-the-client-side-resources-dashboards">Use the client-side resources dashboards</h2>
<p>To review the resources detected by Cloudflare:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4002.md")
</div>
<h2 id="view-all-reported-scripts-or-connections">View all reported scripts or connections</h2>
<p>The All Reported Connections and All Reported Scripts dashboards show all the detected resources including infrequent or inactive ones, reported in the last 30 days. After 30 days without any report, Cloudflare will delete information about a previously reported resource, and it will no longer appear in any of the dashboards.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4000.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4003.md")
</div>
<p>You can filter the data in these dashboards using different criteria, and print a report with the displayed records.</p>
<h2 id="view-details">View details</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3999.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4006.md")
</div>
<h2 id="export-data">Export data</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3997.md")
</aside>
<p>Use this feature to extract data for review and annotation. The data in the exported file will honor any filters you configure in the dashboard.</p>
<p>To export script, connection, or cookie information in CSV format:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4007.md")
</div>
