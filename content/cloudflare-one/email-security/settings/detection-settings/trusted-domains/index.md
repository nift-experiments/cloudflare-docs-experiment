<p>Email security allows you to exempt known partner and internal domains from typical detection scanning. Adding trusted domains helps to reduce false positives on malicious, suspicious, and spoof <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">dispositions</a>. Email security only checks the date when the domain is created.</p>
<h2 id="how-trusted-domains-work">How trusted domains work</h2>
<p>Trusted domains are not for the email message itself, but for entire domains.</p>
<p>By default, Email security automatically detects lookalike domains. Lookalike domains can be something like this: <code>thisisdomain.com</code> and <code>thisisadomain.com</code>. Both domains almost look identical.</p>
<p>If an email is received from a domain that looks like a configured domain, this will trigger a detection. Trusted domain is configured to ignore this detection.</p>
<p>In <a href="/cloudflare-one/email-security/settings/detection-settings/additional-detections/">Additional detections</a>, you can configure malicious domain and suspicious <a href="/cloudflare-one/email-security/settings/detection-settings/additional-detections/#configure-domain-age">domain age</a>.</p>
<p>Malicious domain age means that someone may create a domain today, similar to a target, and start sending emails with that domain. This is usually how many phish campaigns start. In this case, the domain is usually marked as Malicious. Malicious domain age is usually set to 7 days.</p>
<p>Suspicious domain age means that after 7 days (this number corresponds to the Malicious domain age), a domain may not be malicious, but it can still be suspicious. Email security will mark these domains as Suspicious. It is recommended to configure the <strong>Suspicious domain age</strong> between 30 and 45 days.</p>
<p>To view whether a domain is malicious or suspicious:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Investigation</strong>.</li>
<li>Run a screen. For example, select <strong>Run screen</strong> for <strong>Malicious emails</strong>, then select <strong>Run screen</strong>.</li>
<li>Under <strong>Your matching messages</strong>, if any message displays <strong>Domain Age</strong> under <strong>Threat types</strong>, that means that the domain age is too low, and therefore the disposition assigned is Malicious. If the domain is legitimate, you can add it as a trusted domain:
<ul>
<li>Go to <strong>Settings</strong> &gt; <strong>Trusted Domains</strong>.</li>
<li>Under <strong>Domain Info</strong>, add the domain, and select <strong>New Domain</strong>. This will mark the domain whose age is low as a trusted domain.</li>
</ul>
</li>
</ol>
<h2 id="configure-trusted-domains">Configure trusted domains</h2>
<p>To configure a trusted domain:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>, go to <strong>Detection settings</strong> &gt; <strong>Trusted domains</strong>.</li>
<li>On the <strong>Detection settings</strong> page, select <strong>Add a domain</strong>.</li>
<li>Select the <strong>Input method</strong>: Choose between <strong>Manual input</strong>, and <strong>Upload trusted domain list</strong>:
<ul>
<li><strong>Manual input</strong>:
<ul>
<li><strong>Domain info</strong>: Enter a valid domain name.</li>
<li><strong>Domain type</strong>: Select one or both options:
<ul>
<li><strong>Proximity domain</strong>: Domains with similar spelling to your existing domain.</li>
<li><strong>Recent domain</strong>: Domains created recently.</li>
</ul>
</li>
</ul>
<ul>
<li><strong>Notes</strong>: Provide additional information about the trusted domain list.</li>
</ul>
</li>
<li><strong>Upload trusted domain list</strong>: You can upload a file no larger than 150 KB of multiple trusted domains. The file can only contain <code>Domain</code>, <code>Proximity</code>, <code>New</code> and <code>Notes</code> fields. The first row must be a header row. Refer to <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/#csv-uploads">CSV uploads</a> for an example file.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="csv-uploads">CSV uploads</h3>
<p>You can upload a file no larger than 150 KB of multiple trusted domains. The file can only contain <code>Domain</code>, <code>Proximity</code>, <code>New</code> and <code>Notes</code> fields. The first row must be a header row.</p>
<p>An example file would look like this:</p>
<pre><code class="language-txt">Domain, Proximity, New, Notes&#10;mydomain.com, true, true, First Person&#10;testdomain.com, false, true, New Hire&#10;</code></pre>
<h2 id="export-trusted-domains">Export trusted domains</h2>
<p>To export all trusted domains:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select <strong>Domain</strong>. Selecting <strong>Domain</strong> will select all trusted domains.</li>
<li>Select <strong>Export to CSV</strong>.</li>
</ol>
<p>To export specific trusted domains:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select the trusted domains you want to export.</li>
<li>Select <strong>Export to CSV</strong>.</li>
</ol>
<h2 id="edit-trusted-domains">Edit trusted domains</h2>
<p>To edit a trusted domain:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select the trusted domains you want to edit.</li>
<li>Select the three dots &gt; Edit.</li>
<li>Edit the trusted domain.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="delete-trusted-domains">Delete trusted domains</h2>
<p>To delete trusted domains:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select the trusted domain you want to delete.</li>
<li>Select the three dots &gt; <strong>Delete</strong>.</li>
<li>On the pop up message, select <strong>Delete</strong>.</li>
</ol>
<p>To delete multiple trusted domains at once:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select the trusted domains you want to delete.</li>
<li>Select <strong>Action</strong>.</li>
<li>Select <strong>Delete</strong>.</li>
</ol>
