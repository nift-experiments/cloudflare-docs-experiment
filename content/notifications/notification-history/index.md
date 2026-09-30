<p>Notification History is a log of notifications that have been sent to your account via the Notifications service. Information contained in Notification History includes the notification itself, when the notification was sent, and who the notification was sent to.</p>
<h2 id="how-to-access-notification-history">How to access Notification History</h2>
<p>Currently, customers can access Notification History <a href="/api/resources/alerting/subresources/history/methods/list/">via the Cloudflare API</a>. Using <code>GET</code>, customers can retrieve a list of history records for notifications sent to an account. The records are displayed for the last 30 or 90 days, based on the type of plan.</p>
<pre><code class="language-txt">GET accounts/{account_id}/alerting/v3/history&#10;</code></pre>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/alerting/v3/history?page=1&amp;per_page=25&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<h2 id="availability">Availability</h2>
<p>Notification History is available on all plans. The amount of history clients have access to depends on the type of plan:</p>
<ul>
<li><strong>Free, Pro, and Business</strong>: History from the past 30 days.</li>
<li><strong>Enterprise</strong>: History from the past 90 days.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/659.md")
</aside>
