<p>Refer to the section below to learn how to manage your Smart Shield health checks.</p>
<h2 id="create-and-edit-health-checks">Create and edit health checks</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Speed</strong> &gt; <strong>Smart Shield</strong>.</li>
<li>For Health Checks, select <strong>Manage</strong>.</li>
<li>Select <strong>Create</strong> or find an existing health check and select <strong>Edit</strong>.</li>
<li>Fill out the form or edit existing values, paying special attention to:
<ul>
<li>The values for <strong>Interval</strong> and <strong>Check regions</strong>, because decreasing the <strong>Interval</strong> and increasing <strong>Check regions</strong> may increase the load on your origin server.</li>
<li><strong>Retries</strong>, which specify the number of retries to attempt in case of a timeout before marking the origin as unhealthy.</li>
</ul>
</li>
<li>Select <strong>Save and Deploy</strong>.</li>
</ol>
<h2 id="configure-alerts">Configure alerts</h2>
<p>You can configure <a href="/notifications/get-started/">notification emails</a> to be alerted when the health check detects that there is a change in the status of your origin server. Cloudflare will send you an email within seconds so you can take the necessary action before customers are impacted.</p>
<p>The email provides information to determine what caused the health status change. You can evaluate when the change happened, the status of the origin server, if and why it is unhealthy, the expected response code, and the received response code. Refer to <a href="/smart-shield/configuration/health-checks/analytics/#common-error-codes">common error codes</a> for further guidance.</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Speed</strong> &gt; <strong>Smart Shield</strong>.</li>
<li>For Health Checks, select <strong>Manage</strong> and then <strong>Configure an alert</strong>.</li>
<li>Fill out the <strong>Notification name</strong> and <strong>Description</strong>.</li>
<li>Add a Notification email.</li>
<li>Select <strong>Next</strong>.</li>
<li>Add health checks to include in your alerts.</li>
<li>Choose the <strong>Notification trigger</strong>, which determines when you receive alerts.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
