<p>Logging is a fundamental building block for application development. Logs provide insights during the early stages of development and are often critical to understanding issues occurring in production.</p>
<p>Your AI Gateway dashboard shows logs of individual requests, including the user prompt, model response, provider, timestamp, request status, token usage, cost, duration, and the user agent of the client that made the request. When <a href="/ai-gateway/features/dlp/">DLP</a> policies are configured, logs for requests that trigger a DLP match also include the DLP action taken (Flag or Block), matched policy IDs, matched profile IDs, and the specific detection entries that were triggered. These logs persist, giving you the flexibility to store them for your preferred duration and do more with valuable request data.</p>
<p>Each gateway has a storage limit based on your plan. You can customize this limit per gateway in your gateway settings. If your storage limit is reached, new logs will stop being saved. To continue saving logs, you must delete older logs to free up space for new logs.
To learn more about your plan limits, refer to <a href="/ai-gateway/reference/limits/">Limits</a>.</p>
<p>We recommend using an authenticated gateway when storing logs to prevent unauthorized access and protects against invalid requests that can inflate log storage usage and make it harder to find the data you need. Learn more about setting up an <a href="/ai-gateway/configuration/authentication/">authenticated gateway</a>.</p>
<h2 id="default-configuration">Default configuration</h2>
<p>Logs, which include metrics as well as request and response data, are enabled by default for each gateway. This logging behavior will be uniformly applied to all requests in the gateway. If you are concerned about privacy or compliance and want to turn log collection off, you can go to settings and opt out of logs. If you need to modify the log settings for specific requests, you can override this setting on a per-request basis.</p>
<p>To change the default log configuration in the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>AI Gateway</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Settings</strong>.</li>
<li>Change the <strong>Logs</strong> setting to your preference.</li>
</ol>
<h2 id="per-request-logging">Per-request logging</h2>
<p>To override the default logging behavior set in the settings tab, you can define headers on a per-request basis.</p>
<h3 id="collect-logs-cf-aig-collect-log">Collect logs (<code>cf-aig-collect-log</code>)</h3>
<p>The <code>cf-aig-collect-log</code> header allows you to bypass the default log setting for the gateway. If the gateway is configured to save logs, the header will exclude the log for that specific request. Conversely, if logging is disabled at the gateway level, this header will save the log for that request.</p>
<p>In the example below, we use <code>cf-aig-collect-log</code> to bypass the default setting to avoid saving the log.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-header &quot;cf-aig-collect-log: false&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is the email address and phone number of user123?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h3 id="collect-log-payload-cf-aig-collect-log-payload">Collect log payload (<code>cf-aig-collect-log-payload</code>)</h3>
<p>The <code>cf-aig-collect-log-payload</code> header allows you to control whether the raw request and response bodies (payloads) are stored for a given request. Unlike <code>cf-aig-collect-log</code>, which controls the entire log entry, this header only affects payload storage — metadata such as token counts, model, provider, status code, cost, and duration will still be logged.</p>
<p>This is useful when you want to maintain visibility into usage metrics and request metadata without persisting sensitive prompt or completion data.</p>
<table>
<thead>
<tr>
<th>Header value</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>true</code></td>
<td>Request and response payloads are stored.</td>
</tr>
<tr>
<td><code>false</code></td>
<td>Payload storage is skipped. Metadata-only log entries are still saved.</td>
</tr>
</tbody>
</table>
<p>In the example below, we use <code>cf-aig-collect-log-payload</code> to skip storing the request and response bodies while keeping the metadata log.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-header &quot;cf-aig-collect-log-payload: false&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is the email address and phone number of user123?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2946.md")
</aside>
<h2 id="dlp-fields-in-logs">DLP fields in logs</h2>
<p>When <a href="/ai-gateway/features/dlp/">Data Loss Prevention (DLP)</a> policies are enabled on a gateway, log entries for requests that trigger a DLP policy match include additional fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>DLP Action</td>
<td>The action taken by the DLP policy: <code>FLAG</code> or <code>BLOCK</code></td>
</tr>
<tr>
<td>DLP Policies Matched</td>
<td>The IDs of the DLP policies that matched</td>
</tr>
<tr>
<td>DLP Profiles Matched</td>
<td>The IDs of the DLP profiles that triggered within each matched policy</td>
</tr>
<tr>
<td>DLP Entries Matched</td>
<td>The specific detection entry IDs that matched within each profile</td>
</tr>
<tr>
<td>DLP Check</td>
<td>Whether the match occurred in the <code>REQUEST</code>, <code>RESPONSE</code>, or both</td>
</tr>
</tbody>
</table>
<p>These fields are available both in the dashboard log viewer and through the <a href="/api/resources/ai_gateway/subresources/logs/methods/list/">Logs API</a>. You can filter logs by <strong>DLP Action</strong> in the dashboard to view only flagged or blocked requests. For more details on DLP monitoring, refer to <a href="/ai-gateway/features/dlp/set-up-dlp/#monitor-dlp-events">Monitor DLP events</a>.</p>
<h2 id="managing-log-storage">Managing log storage</h2>
<p>To manage your log storage effectively, you can:</p>
<ul>
<li>Set Storage Limits: Configure a limit on the number of logs stored per gateway in your gateway settings to ensure you only pay for what you need.</li>
<li>Enable Automatic Log Deletion: Activate the Automatic Log Deletion feature in your gateway settings to automatically delete the oldest logs once the storage limit for your account is reached. This ensures new logs are always saved without manual intervention.</li>
</ul>
<h2 id="how-to-delete-logs">How to delete logs</h2>
<p>To manage your log storage effectively and ensure continuous logging, you can delete logs using the following methods:</p>
<h3 id="automatic-log-deletion">Automatic Log Deletion</h3>
<p>​To maintain continuous logging within your gateway's storage constraints, enable Automatic Log Deletion in your Gateway settings. This feature automatically deletes the oldest logs once the storage limit for your account is reached, ensuring new logs are saved without manual intervention.</p>
<h3 id="manual-deletion">Manual deletion</h3>
<p>To manually delete logs through the dashboard, navigate to the Logs tab in the dashboard. Use the available filters such as status, cache, provider, cost, or any other options in the dropdown to refine the logs you wish to delete. Once filtered, select Delete logs to complete the action.</p>
<p>See full list of available filters and their descriptions below:</p>
<table>
<thead>
<tr>
<th>Filter category</th>
<th>Filter options</th>
<th>Filter by description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Status</td>
<td>error, status</td>
<td>error type or status.</td>
</tr>
<tr>
<td>Cache</td>
<td>cached, not cached</td>
<td>based on whether they were cached or not.</td>
</tr>
<tr>
<td>Provider</td>
<td>specific providers</td>
<td>the selected AI provider.</td>
</tr>
<tr>
<td>AI Models</td>
<td>specific models</td>
<td>the selected AI model.</td>
</tr>
<tr>
<td>Cost</td>
<td>less than, greater than</td>
<td>cost, specifying a threshold.</td>
</tr>
<tr>
<td>Request type</td>
<td>Workers AI Binding, WebSockets</td>
<td>the type of request.</td>
</tr>
<tr>
<td>Tokens</td>
<td>Total tokens, Tokens In, Tokens Out</td>
<td>token count (less than or greater than).</td>
</tr>
<tr>
<td>Duration</td>
<td>less than, greater than</td>
<td>request duration.</td>
</tr>
<tr>
<td>Feedback</td>
<td>equals, does not equal (thumbs up, thumbs down, no feedback)</td>
<td>feedback type.</td>
</tr>
<tr>
<td>Metadata Key</td>
<td>equals, does not equal</td>
<td>specific metadata keys.</td>
</tr>
<tr>
<td>Metadata Value</td>
<td>equals, does not equal</td>
<td>specific metadata values.</td>
</tr>
<tr>
<td>Log ID</td>
<td>equals, does not equal</td>
<td>a specific Log ID.</td>
</tr>
<tr>
<td>Event ID</td>
<td>equals, does not equal</td>
<td>a specific Event ID.</td>
</tr>
<tr>
<td>DLP Action</td>
<td>FLAG, BLOCK</td>
<td>the DLP action taken on the request.</td>
</tr>
<tr>
<td>User Agent</td>
<td>equals, does not equal, contains</td>
<td>the user agent of the client that made the request.</td>
</tr>
</tbody>
</table>
<h3 id="api-deletion">API deletion</h3>
<p>You can programmatically delete logs using the AI Gateway API. For more comprehensive information on the <code>DELETE</code> logs endpoint, check out the <a href="/api/resources/ai_gateway/subresources/logs/methods/delete/">Cloudflare API documentation</a>.</p>
