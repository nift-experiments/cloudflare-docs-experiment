<p>When you <a href="/notifications/get-started/configure-webhooks/#generic-webhooks">configure a generic webhook</a>, Cloudflare sends a JSON payload to your specified URL for each notification. This page documents the structure of that payload.</p>
<h2 id="payload-structure">Payload structure</h2>
<p>All generic webhook notifications follow this schema:</p>
<pre><code class="language-json">{&#10;	&quot;name&quot;: &quot;string&quot;,&#10;	&quot;text&quot;: &quot;string&quot;,&#10;	&quot;data&quot;: {},&#10;	&quot;ts&quot;: 1136214245,&#10;	&quot;account_id&quot;: &quot;string&quot;,&#10;	&quot;policy_id&quot;: &quot;string&quot;,&#10;	&quot;policy_name&quot;: &quot;string&quot;,&#10;	&quot;alert_type&quot;: &quot;string&quot;,&#10;	&quot;alert_correlation_id&quot;: &quot;string&quot;,&#10;	&quot;alert_event&quot;: &quot;string&quot;&#10;}&#10;</code></pre>
<h3 id="field-descriptions">Field descriptions</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>string</td>
<td>The name of the notification policy.</td>
</tr>
<tr>
<td><code>text</code></td>
<td>string</td>
<td>A human-readable description of the notification with interpolated values.</td>
</tr>
<tr>
<td><code>data</code></td>
<td>object</td>
<td>The alert-specific data. The structure varies by <code>alert_type</code>.</td>
</tr>
<tr>
<td><code>ts</code></td>
<td>integer</td>
<td>The unix timestamp (seconds since epoch, UTC) when the notification was generated.</td>
</tr>
<tr>
<td><code>account_id</code></td>
<td>string</td>
<td>The account ID for which this webhook was fired.</td>
</tr>
<tr>
<td><code>policy_id</code></td>
<td>string</td>
<td>The UUID of the notification policy that triggered this webhook.</td>
</tr>
<tr>
<td><code>policy_name</code></td>
<td>string</td>
<td>The name of the notification policy.</td>
</tr>
<tr>
<td><code>alert_type</code></td>
<td>string</td>
<td>The unique identifier for the alert type (for example, <code>http_alert_origin_error</code>).</td>
</tr>
<tr>
<td><code>alert_correlation_id</code></td>
<td>string</td>
<td>The UUID that groups related alerts together.</td>
</tr>
<tr>
<td><code>alert_event</code></td>
<td>string</td>
<td>The event state, such as <code>ALERT_STATE_EVENT_START</code> or <code>ALERT_STATE_EVENT_END</code>.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10842.md")
</aside>
<h2 id="example-payloads">Example payloads</h2>
<p>The following examples show the payload structure for common alert types. The <code>data</code> object varies based on the specific alert.</p>
<details class="nb-details"><summary>DDoS attack (Layer 4)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10843.md")
</div></details>
<details class="nb-details"><summary>DDoS attack (Layer 7)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10844.md")
</div></details>
<details class="nb-details"><summary>SSL certificate expiration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10845.md")
</div></details>
<details class="nb-details"><summary>Origin health check</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10846.md")
</div></details>
<details class="nb-details"><summary>Workers alert</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10847.md")
</div></details>
<details class="nb-details"><summary>Access certificate expiration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10848.md")
</div></details>
<details class="nb-details"><summary>Workers observability alert</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10849.md")
</div></details>
<h2 id="validate-webhook-payloads">Validate webhook payloads</h2>
<p>You can use the <code>cf-webhook-auth</code> header to verify that incoming webhooks are from Cloudflare. When you configure a webhook with a secret, Cloudflare includes this header with your secret value in every request. Reject any requests where this header is missing or does not match your configured secret.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/notifications/get-started/configure-webhooks/">Configure webhooks</a></li>
<li><a href="/notifications/notification-available/">Available notification types</a></li>
</ul>
