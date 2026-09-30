<ol>
<li>On the <a href="https://console.cloud.google.com/welcome/new">Google Cloud Console</a>, select <strong>Credentials</strong>.</li>
<li>Select <strong>CREATE CREDENTIALS</strong> &gt; <strong>Service account</strong>.</li>
<li>Fill in the details to create a service account:
<ul>
<li><strong>Service account name</strong>: Enter <code>Message Retraction Service Account</code>.</li>
<li><strong>Service account ID</strong>: Enter <code>message-retraction-service-acc</code>.</li>
<li><strong>Service account description</strong>: Enter <code>Email security Message Retraction</code>.</li>
<li>Select <strong>CREATE AND CONTINUE</strong>.</li>
</ul>
</li>
<li>In <strong>Grant this service account access to project</strong>, select <strong>Select a role</strong> &gt; Choose <strong>Owner</strong>. Select <strong>CONTINUE</strong>, then <strong>DONE</strong>.</li>
<li>Go back to <strong>Credentials</strong>, and select your service account under <strong>Service Accounts</strong>. In <strong>Details</strong>, take note of the <strong>Unique ID</strong>.</li>
<li>Select <strong>Advanced settings</strong> &gt; <strong>VIEW GOOGLE WORKSPACE ADMIN CONSOLE</strong>, then enter your password.</li>
<li>On the sidebar, select <strong>Security</strong> &gt; <strong>Access and data control</strong> &gt; <strong>API controls</strong> &gt; Select <strong>MANAGE DOMAIN WIDE DELEGATION</strong>.</li>
<li>Select <strong>Add new</strong> &gt; Add a new client ID:
<ul>
<li><strong>Client ID</strong>: Enter the <strong>Unique ID</strong> you took note of.</li>
<li><strong>OAuth scopes</strong>: Enter the following URLs:</li>
</ul>
</li>
</ol>
<pre><code class="language-txt">https://www.googleapis.com/auth/admin.directory.user.readonly, https://www.googleapis.com/auth/admin.directory.group.readonly, https://www.googleapis.com/auth/admin.directory.user.alias.readonly, https://www.googleapis.com/auth/gmail.labels, https://mail.google.com/&#10;</code></pre>
<ul>
<li>Select <strong>AUTHORIZE</strong>.</li>
</ul>
<ol start="9">
<li>Go back to the sidebar &gt; <strong>Service Accounts</strong>.</li>
<li>Select the three dots &gt; <strong>Manage keys</strong> &gt; <strong>ADD KEY</strong> &gt; <strong>Create new key</strong> &gt; Select <strong>JSON</strong> &gt; Select <strong>CREATE</strong>. This downloads a <code>.json</code> file which you will use at a later stage.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have created a service account, proceed to <a href="/email-security/deployment/api/setup/gsuite-bcc-setup/add-retraction/">adding retractions</a> to your email.</p>
