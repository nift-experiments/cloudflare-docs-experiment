<p>With Email security, you can enable logs to review actions performed on your account.</p>
<p>To enable audit logs:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select your storage destination.</p>
</li>
<li>
<p>Select the three dots &gt; <strong>Edit</strong>.</p>
</li>
<li>
<p>Under <strong>Configure logpush job</strong>:</p>
<ul>
<li><strong>Job name</strong>: Enter the job name, if it is not already prepopulated.</li>
<li><strong>If logs match</strong> &gt; Select <strong>Filtered logs</strong>:
<ul>
<li><strong>Field</strong>: Choose <code>ResourceType</code>.</li>
<li><strong>Operator</strong>: Choose <code>starts with</code>.</li>
<li><strong>Value</strong>: Enter <code>email_security</code>.</li>
</ul>
</li>
</ul>
</li>
<li>
<p>Select <strong>Submit</strong>.</p>
</li>
</ol>
<p>You can now view logs via the Cloudflare dashboard.</p>
