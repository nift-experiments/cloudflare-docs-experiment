<p>By default, Cloudflare Gateway policies apply at all times when turned on. With timed DNS policies, you can control when DNS policies are active — for example, to block social media only during work hours or to temporarily allow access to a restricted site for a maintenance window. You can configure a policy to be active during specific time periods or set the policy to expire after a certain duration.</p>
<p>There are two timed DNS policy options:</p>
<ul>
<li><a href="#policy-duration">Policy duration</a>: The policy is active for a specific amount of time after being turned on (for example, 30 minutes).</li>
<li><a href="#policy-schedule">Policy schedule</a>: The policy is active during a recurring weekly schedule (for example, weekdays from 9 AM to 5 PM).</li>
</ul>
<h2 id="policy-duration">Policy duration</h2>
<p>You can use a time-based policy duration to set a specific time frame for the policy to turn on or configure an exact time for the policy to turn off.</p>
<p>To set a duration for a DNS policy:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>DNS</strong>.</li>
<li>Create a new DNS policy or choose an existing policy and select <strong>Edit</strong>.</li>
<li>In <strong>Apply durations and schedules</strong>, turn on <strong>Policy duration</strong>.</li>
<li>In <strong>Input method</strong>, choose the type of duration:
<ul>
<li>Choose <em>Duration</em> and enter a specific amount of time until the policy turns off.</li>
<li>Choose <em>Exact end date</em> and enter a specific date and time in your account's time zone for the policy to turn off.</li>
</ul>
</li>
<li>Select <strong>Save policy</strong>.</li>
</ol>
<p>When a policy turns off, it will remain off until you turn it back on.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6638.md")
</aside>
<p>For example, you can create a policy at 12:00 PM and set it to turn off after six hours. If you turn the policy off at 3:00 PM and turn it back on at 4:00 PM, the policy will still turn off at 6:00 PM — six hours after the original activation time, not six hours of cumulative active time.</p>
<h3 id="reset-a-policy-s-duration">Reset a policy's duration</h3>
<p>When a policy's time duration expires, you can turn the policy back on for the duration you originally configured. To reset a policy's duration, select the policy and choose <strong>Reset policy duration</strong>.</p>
<p>For policies with an exact end time, you can change the time before the policy turns off. Once the policy reaches its exact end time, you will need to edit the policy and set a new end time. To set a new exact end time:</p>
<ol>
<li>Select the policy.</li>
<li>Choose <strong>Edit</strong>.</li>
<li>Turn on <strong>Set a policy duration</strong>.</li>
<li>In <strong>Input method</strong>, choose <em>Exact end date</em>. In <strong>Date and time</strong>, enter a new date and time for the policy to turn off.</li>
<li>Select <strong>Save policy</strong>.</li>
</ol>
<h2 id="policy-schedule">Policy schedule</h2>
<p>You can use Gateway to create a new DNS policy with a schedule or add a schedule to an existing policy.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6641.md")
</div></div>
<p>The policy's schedule will appear in the Cloudflare dashboard under <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>DNS</strong> when you select the policy.</p>
<h3 id="how-gateway-determines-time-zone">How Gateway determines time zone</h3>
<p>If you <a href="#example-fixed-time-zone">assign a time zone</a> to your schedule, Gateway will always use the current time at that time zone regardless of the user's location. This allows you to enable a policy during a certain fixed time period.</p>
<p>If you <a href="#example-users-time-zone">do not specify a time zone</a>, Gateway will enable the DNS policy based on the user's local time zone. The user's time zone is inferred from the IP geolocation of their source IP address. If Gateway is unable to determine the time zone from the source IP, it will fall back to the time zone of the data center where the query was received.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6637.md")
</aside>
<h4 id="example-fixed-time-zone">Example: Fixed time zone</h4>
<p>The following command creates a DNS policy to block <code>facebook.com</code> only on weekdays from 8:00 AM - 12:30 PM and 1:30 PM - 5:00 PM in the Chicago, USA time zone.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/gateway/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;office-no-facebook-policy&quot;,&#10;  &quot;action&quot;: &quot;block&quot;,&#10;  &quot;traffic&quot;: &quot;dns.fqdn == \&quot;facebook.com\&quot;&quot;,&#10;  &quot;enabled&quot;: true,&#10;  &quot;schedule&quot;: {&#10;    &quot;time_zone&quot;: &quot;America/Chicago&quot;,&#10;    &quot;mon&quot;: &quot;08:00-12:30,13:30-17:00&quot;,&#10;    &quot;tue&quot;: &quot;08:00-12:30,13:30-17:00&quot;,&#10;    &quot;wed&quot;: &quot;08:00-12:30,13:30-17:00&quot;,&#10;    &quot;thu&quot;: &quot;08:00-12:30,13:30-17:00&quot;,&#10;    &quot;fri&quot;: &quot;08:00-12:30,13:30-17:00&quot;&#10;  }&#10;}&#x27;</code></pre>
<p>Refer to <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List">this table</a> for a list of all time zone identifiers.</p>
<h4 id="example-user-s-time-zone">Example: User's time zone</h4>
<p>The following command creates a DNS policy to block <code>clockin.com</code> only on weekends in the time zone where the user is currently located.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/gateway/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;clock-in-policy&quot;,&#10;  &quot;action&quot;: &quot;block&quot;,&#10;  &quot;traffic&quot;: &quot;dns.fqdn == \&quot;clockin.com\&quot;&quot;,&#10;  &quot;enabled&quot;: true,&#10;  &quot;schedule&quot;: {&#10;    &quot;sat&quot;: &quot;00:00-24:00&quot;,&#10;    &quot;sun&quot;: &quot;00:00-24:00&quot;&#10;  }&#10;}&#x27;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6636.md")
</aside>
