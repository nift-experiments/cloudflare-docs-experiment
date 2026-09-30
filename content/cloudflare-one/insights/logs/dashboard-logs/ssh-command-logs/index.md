<p>SSH command logs record the commands that users run on infrastructure targets protected by <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Access for Infrastructure</a>. Use these logs to audit user activity on your SSH servers and investigate specific sessions.</p>
<p>To view SSH command logs, log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>SSH command logs</strong>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To generate SSH command logs, you must:</p>
<ol>
<li>Set up <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Access for Infrastructure</a> for your SSH servers.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#ssh-command-logs">Enable SSH command logging</a> by uploading an encryption public key. Cloudflare uses this key to encrypt your logs so that only you can read their contents.</li>
</ol>
<h2 id="view-ssh-logs">View SSH logs</h2>
<p>SSH command logs displayed in the dashboard are encrypted using the public key you provided during setup. The logs are not readable in the dashboard — you must download and decrypt them locally. To view the contents of the logs:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>SSH command logs</strong>.</li>
<li>Filter the logs using the name of your SSH application.</li>
<li>Select the SSH session for which you want to export command logs.</li>
<li>In the side panel, scroll down to <strong>SSH logs</strong> and select <strong>Download</strong>.</li>
<li>Decrypt the log using the <a href="https://github.com/cloudflare/ssh-log-cli/">SSH Logging CLI</a> and the private key that corresponds to the public key you uploaded.</li>
</ol>
<h2 id="log-fields">Log fields</h2>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Session ID</strong></td>
<td>Unique identifier for the SSH session.</td>
</tr>
<tr>
<td><strong>User email</strong></td>
<td>Email address of the user who initiated the SSH session.</td>
</tr>
<tr>
<td><strong>Target ID</strong></td>
<td>Identifier of the infrastructure target being accessed. Corresponds to the target you configured in Access for Infrastructure.</td>
</tr>
<tr>
<td><strong>Client address</strong></td>
<td>Source IP address of the SSH connection.</td>
</tr>
<tr>
<td><strong>Server address</strong></td>
<td>Destination IP address of the SSH server.</td>
</tr>
<tr>
<td><strong>Session start datetime</strong></td>
<td>Timestamp when the SSH session started.</td>
</tr>
<tr>
<td><strong>Session finish datetime</strong></td>
<td>Timestamp when the SSH session ended.</td>
</tr>
<tr>
<td><strong>Program type</strong></td>
<td>Type of SSH program: <code>shell</code> (interactive terminal), <code>exec</code> (single command execution), <code>x11</code>, <code>direct-tcpip</code>, or <code>forwarded-tcpip</code>. Note that <code>x11</code>, <code>direct-tcpip</code>, and <code>forwarded-tcpip</code> correspond to SSH features that are <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#known-limitations">not currently supported</a> by Access for Infrastructure.</td>
</tr>
<tr>
<td><strong>Payload</strong></td>
<td>Captured request/response data in <a href="https://docs.asciinema.org/manual/asciicast/v2/">asciicast v2</a> format, a structured terminal recording format. Includes commands for <code>exec</code> programs.</td>
</tr>
<tr>
<td><strong>Error</strong></td>
<td>SSH error message, if an error occurred during the session.</td>
</tr>
</tbody>
</table>
<h2 id="export-ssh-logs-with-logpush">Export SSH logs with Logpush</h2>
<p>Enterprise users can export SSH command logs to external storage or analysis destinations using <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>. Unlike dashboard logs, Logpush payloads are not encrypted with a customer-provided public key — secure access to your storage destination accordingly.</p>
<p>For a list of all available fields, refer to <a href="/logs/logpush/logpush-job/datasets/account/ssh_logs/">SSH Logs</a>.</p>
