<p>A <strong>service account</strong> allows admins to create and maintain API credentials separate from a single username and password combination. It also allows you to create and control additional API access for different use cases.</p>
<p>When you connect to the <a href="/email-security/api/">Email security (formerly Area 1) API</a>, the <strong>Public Key</strong> is used for the <em>username</em> and the <strong>Private Key</strong> for the <em>password</em>.</p>
<h2 id="create-service-account">Create service account</h2>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Service Accounts</strong>.</li>
<li>Select <strong>Add Service Account</strong>.</li>
<li>Add a <strong>Name</strong>.</li>
<li>Select <strong>Create Service Account</strong>.</li>
<li>You will see your account's <strong>Private Key</strong> in a pop-up message (which will never be displayed again) and <strong>Public Key</strong> in the list of service accounts. Make sure to copy both values and store in a secure location.</li>
</ol>
<hr />
<h2 id="rotate-private-key">Rotate private key</h2>
<p>If you lose your private key or need to rotate it for security reasons, you can generate a new private key:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Service Accounts</strong>.</li>
<li>On a specific account, select <strong>...</strong> &gt; <strong>Refresh key</strong>.</li>
</ol>
