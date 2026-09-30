<p>The ownership challenge is a one-time verification that proves you have read access to a destination bucket before Cloudflare pushes logs to it. This mechanism prevents you from accidentally configuring a Logpush job that pushes data to a bucket you do not control.</p>
<h2 id="how-it-works">How it works</h2>
<p>When you create a Logpush job to a storage destination, Cloudflare requires you to prove ownership of that destination:</p>
<ol>
<li>You request an ownership challenge for your <code>destination_conf</code>.</li>
<li>Cloudflare writes a JWT to an <code>ownership-challenge.txt</code> file in your bucket.</li>
<li>You read the token from your bucket and submit it with your job creation request.</li>
<li>Cloudflare validates the token and creates the job.</li>
</ol>
<p>For step-by-step instructions, refer to <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a>.</p>
<h2 id="what-the-challenge-protects-against">What the challenge protects against</h2>
<p>The ownership challenge primarily protects you from accidental misconfiguration. Without this verification, you could inadvertently configure a job to push to a bucket you did not intend—for example, pushing to a bucket that is actually owned by someone else.</p>
<p>The challenge also prevents malicious scenarios where someone could:</p>
<ul>
<li>Point a Logpush job at another customer's bucket</li>
<li>Push bogus or malicious log data to that bucket</li>
<li>Pollute or corrupt the victim's log storage</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10505.md")
</aside>
<h2 id="challenge-token-structure">Challenge token structure</h2>
<p>The ownership challenge is a JSON Web Token (JWT) containing claims that bind it to a specific context. The token includes:</p>
<ul>
<li><strong>Object type</strong> - Whether the job is zone-scoped, account-scoped, or tenant-scoped</li>
<li><strong>Object ID</strong> - The specific zone or account identifier</li>
<li><strong>Destination configuration</strong> - The full destination configuration string</li>
<li><strong>Destination fingerprint</strong> - A hash of the bucket name and paths/prefixes</li>
<li><strong>Expiration</strong> - The token expires after 7 days</li>
</ul>
<p>When you submit the challenge token, Cloudflare validates that all claims match your job creation request. This prevents the token from being reused for a different account, zone, or destination.</p>
<h2 id="security-considerations">Security considerations</h2>
<h3 id="can-a-compromised-token-be-exploited">Can a compromised token be exploited?</h3>
<p>In practice, an attack using a compromised ownership challenge token is extremely unlikely. An attacker would need:</p>
<ol>
<li>Access to your Cloudflare account (to match the object ID in the token)</li>
<li>Knowledge of the exact bucket name and paths/prefixes (to match the destination fingerprint)</li>
<li>To act within 7 days (before the challenge expires)</li>
</ol>
<p>Your bucket's IAM/access controls and Cloudflare account security are the primary security layers, not the ownership challenge token.</p>
<h3 id="best-practices">Best practices</h3>
<ul>
<li><strong>Delete the challenge file after job creation</strong> - Once your Logpush job is created, you can safely delete the <code>ownership-challenge.txt</code> file from your bucket.</li>
<li><strong>Restrict bucket permissions</strong> - Grant write access only to Cloudflare's service accounts. For AWS S3, grant <code>PutObject</code> permission to <code>arn:aws:iam::391854517948:user/cloudflare-logpush</code>. For GCS, grant <code>Storage Object Admin</code> to <code>logpush@cloudflare-data.iam.gserviceaccount.com</code>.</li>
<li><strong>Monitor your Logpush jobs</strong> - Use the <a href="/logs/logpush/logpush-health/">Logpush health dashboards</a> to monitor job status and detect anomalies.</li>
</ul>
<h2 id="which-destinations-require-an-ownership-challenge">Which destinations require an ownership challenge?</h2>
<table>
<thead>
<tr>
<th>Destination</th>
<th>Ownership challenge required</th>
</tr>
</thead>
<tbody>
<tr>
<td>AWS S3</td>
<td>Yes (or use access key/secret key)</td>
</tr>
<tr>
<td>Google Cloud Storage</td>
<td>Yes</td>
</tr>
<tr>
<td>Azure Blob Storage</td>
<td>Yes</td>
</tr>
<tr>
<td>Sumo Logic</td>
<td>Yes</td>
</tr>
<tr>
<td>S3-compatible storage</td>
<td>No</td>
</tr>
<tr>
<td>HTTP endpoints</td>
<td>No</td>
</tr>
<tr>
<td>Datadog</td>
<td>No</td>
</tr>
<tr>
<td>Splunk</td>
<td>No</td>
</tr>
<tr>
<td>New Relic</td>
<td>No</td>
</tr>
</tbody>
</table>
<p>For destinations that do not require an ownership challenge, Cloudflare uses alternative authentication methods such as API keys or tokens.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/logs/logpush/logpush-job/api-configuration/">API configuration</a></li>
<li><a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a></li>
<li><a href="/logs/logpush/permissions/">Logpush permissions</a></li>
<li><a href="/logs/logpush/logpush-job/enable-destinations/aws-s3/">Enable AWS S3 destination</a></li>
<li><a href="/logs/logpush/logpush-job/enable-destinations/google-cloud-storage/">Enable GCS destination</a></li>
</ul>
