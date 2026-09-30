<p>Logpush jobs may fail for a few reasons, for instance because the destination is unreachable, because of a change in permissions at the customers’ origin, or because a Logpush job did not complete at least one successful push in the last 24 hour.</p>
<p>With analytics and alerting, you can monitor your Logpush job health and find out for yourself when a job fails. You can get alerted and you can also get analytics about your Logpush jobs health via GraphQL.</p>
<p>Alerts are sent via the <a href="/notifications/">Cloudflare Notifications</a> system. They can be sent via email or webhook. When subscribed to job disablement notification, you will receive at most one alert per job per 24 hours. The notification email contains the job ID and destination configuration.</p>
<details><summary>Failing Logpush Job Disabled</summary><strong>Who is it for?</strong><p>Enterprise customers who use <a href="/logs/">Logpush</a> and want to monitor their job health.</p>
<strong>Other options / filters</strong><ul>
<li>Notification Name: A custom name for the notification.</li>
<li>Description (optional): A custom description for the notification.</li>
<li>Notification Email (can be multiple emails): The email address of the recipient for the notification.</li>
</ul>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>In the email for the notification, you can find the destination name for the failing Logpush job. With this destination name, you should be able to figure out which zone this relates to. There can be multiple reasons why a job fails, but it is best to test that the destination endpoint is healthy, and that necessary credentials are still working. You can also check that the destination has allowlisted <a href="https://www.cloudflare.com/ips/">Cloudflare IPs</a>.</p>
</details>
<h2 id="enable-alerts">Enable alerts</h2>
<p>You can add an alert for <strong>Failing Logpush Job Disabled</strong> via the <strong>Notifications</strong> section of the dashboard. Note that alerts can be configured at the account level and apply to all jobs within an account.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Next, select <strong>Add</strong>.</li>
<li>Select the alert <strong>Failing Logpush Job Disabled</strong>.</li>
<li>Configure the alert: choose a name, add a description (optional), select the notification services, Webhooks and enter the email where you want to be notified.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>When you complete these steps, you will receive an email alert if your Logpush job is disabled.</p>
<h2 id="enable-logpush-health-analytics">Enable Logpush health analytics</h2>
<p>Customers can query Logpush job health metrics via the <a href="/analytics/graphql-api/">GraphQL API</a>. The name of the dataset is <code>logpushHealthAdaptiveGroups</code> and the schema can be explored using the <a href="/analytics/graphql-api/getting-started/explore-graphql-schema/">GraphQL API</a>.</p>
<p>Here is a query to get the count of how many times jobs pushing to S3 failed.</p>
<pre><code class="language-json">query&#10;{&#10;  viewer&#10;  {&#10;    zones(filter: { zoneTag: $zoneTag})&#10;    {&#10;      logpushHealthAdaptiveGroups(filter: {&#10;        datetime_gt:&quot;2022-08-15T00:00:00Z&quot;,&#10;        destinationType:&quot;s3&quot;,&#10;        status_neq:200&#10;      },&#10;      limit:10)&#10;      {&#10;        count,&#10;        dimensions {&#10;          jobId,&#10;          status,&#10;          destinationType&#10;        }&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10476.md")
</aside>
