<p>You can <a href="/health-checks/how-to/health-checks-notifications/#configure-notifications">configure notification emails</a> to be alerted when the Health Check detects that there is a change in the status of your origin server. Cloudflare will send you an email within seconds so you can take the necessary action before customers are impacted.</p>
<p>The email provides information to determine what caused the health status change. You can evaluate when the change happened, the status of the origin server, if and why it is unhealthy, the expected response code, and the received response code.</p>
<h2 id="configure-notifications">Configure notifications</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Health Checks</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Configure an alert</strong>.</li>
<li>Fill out the <strong>Notification name</strong> and <strong>Description</strong>.</li>
<li>Add a Notification email.</li>
<li>Select <strong>Next</strong>.</li>
<li>Add health checks to include in your alerts.</li>
<li>Choose the <strong>Notification trigger</strong>, which determines when you receive alerts.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9013.md")
</aside>
<p>See <a href="/health-checks/health-checks-analytics/#common-error-codes">common error codes</a> for more information regarding the cause of any changes to your Health Check.</p>
<p>Cloudflare encourages you to view your <a href="/health-checks/health-checks-analytics/#common-error-codes">Health Checks Analytics</a> to get more context about the health of your servers over time.</p>
