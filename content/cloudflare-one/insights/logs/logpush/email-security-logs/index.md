<p>Email security allows you to configure Logpush to export two types of log data: detection logs (records of threats identified in email traffic) and user action logs (records of administrative actions taken via the API or the dashboard). Each log type requires separate configuration.</p>
<h2 id="enable-detection-logs">Enable detection logs</h2>
<p>Detection logs record each threat identified by Email security, including metadata such as the message sender, recipient, and detection verdict.</p>
<p>To enable detection logs, refer to <a href="/logs/logpush/logpush-job/enable-destinations/">Enable destinations</a>. When configuring the Logpush job, select <strong>Email security alerts</strong> as the dataset.</p>
<h2 id="enable-user-action-logs">Enable user action logs</h2>
<p>User action logs record all administrative actions taken via the <a href="/api/resources/email_security/">API</a> or the dashboard.</p>
<p>Before you can enable user action logs for Email security, you must have a Logpush job configured for your storage destination. Refer to <a href="/logs/logpush/logpush-job/enable-destinations/">Enable destinations</a> to enable logs on destinations such as Cloudflare R2, HTTP, Amazon S3, and more.</p>
<p>Once you have configured your destination, you can set up user action logs:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your storage destination.</li>
<li>Select the three dots &gt; <strong>Edit</strong>.</li>
<li>Under <strong>Configure logpush job</strong>:</li>
</ol>
<ul>
<li><strong>Job name</strong>: Enter the job name, if it is not already prepopulated.</li>
<li><strong>If logs match</strong> &gt; Select <strong>Filtered logs</strong> to capture only Email security events:
<ul>
<li><strong>Field</strong>: Choose <code>ResourceType</code> (the type of resource that was changed).</li>
<li><strong>Operator</strong>: Choose <code>starts with</code>.</li>
<li><strong>Value</strong>: Enter <code>email_security</code>.</li>
</ul>
</li>
</ul>
<ol start="5">
<li>Select <strong>Submit</strong>.</li>
</ol>
<p>You can now view logs via the Cloudflare dashboard.</p>
