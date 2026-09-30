<p>Send Zaraz logs to an external storage provider like R2 or S3.</p>
<p>This is an Enterprise only feature.</p>
<h2 id="setup">Setup</h2>
<p>Follow these steps to configure Logpush support for Zaraz:</p>
<h3 id="1-create-a-logpush-job"><ol>
<li>Create a Logpush job</li>
</ol></h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create a Logpush Job</strong> and follow the steps described in the <a href="/logs/logpush/">Logpush</a> documentation.<br/>
When selecting a dataset, make sure you select <strong>Zaraz Events</strong>.</li>
</ol>
<h3 id="2-enable-logpush-from-zaraz-settings"><ol start="2">
<li>Enable Logpush from Zaraz settings</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, go to <strong>Delivery &amp; Performance</strong> &gt; <strong>Web tag management</strong> &gt; <strong>Tag setup</strong> &gt; select your domain &gt; <strong>Settings</strong>.</p>
<p>Alternatively, navigate directly to <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz/:zone/tools-config/tools">Zaraz settings</a></p>
</li>
<li>
<p>Enable <strong>Export Zaraz Logs</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17606.md")
</aside>
<h2 id="fields">Fields</h2>
<p>Logs will have the following fields:</p>
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
<td>RequestHeaders</td>
<td><code>JSON</code></td>
<td>The headers that were sent with the request.</td>
</tr>
<tr>
<td>URL</td>
<td><code>String</code></td>
<td>The Zaraz URL to which the request was made.</td>
</tr>
<tr>
<td>IP</td>
<td><code>String</code></td>
<td>The originating IP.</td>
</tr>
<tr>
<td>Body</td>
<td><code>JSON</code></td>
<td>The body that was sent along with the request.</td>
</tr>
<tr>
<td>Event Type</td>
<td><code>String</code></td>
<td>Can be one of the following: <code>server_request</code>, <code>server_response</code>, <code>action_triggered</code>, <code>ecommerce_triggered</code>, <code>client_request</code>, <code>component_error</code>.</td>
</tr>
<tr>
<td>Event Details</td>
<td><code>JSON</code></td>
<td>Details about the event.</td>
</tr>
<tr>
<td>TimestampStart</td>
<td><code>String</code></td>
<td>The time at which the event occurred.</td>
</tr>
</tbody>
</table>
