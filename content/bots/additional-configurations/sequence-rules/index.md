<p><a href="/bots/additional-configurations/sequence-rules/">Sequence rules</a> uses cookies to track the order of requests a user has made and the time between requests and makes them available via <a href="/rules/">Cloudflare Rules</a>. This allows you to write rules that match valid or invalid sequences. The specific cookies used to validate sequences are called sequence cookies.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="431-error">`431` error</h3>
@markup("md", "content/.markup/bodies/3532.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Your account must have the Fraud Detection subscription.</li>
<li>Each zone must configure the endpoints to track via Endpoint Management.</li>
</ul>
<p>You can <a href="#build-a-sequence-custom-rule-via-the-cloudflare-dashboard">build a sequence custom rule via the Cloudflare dashboard</a> or <a href="#manage-sequence-rules-via-the-api">using the API</a>.</p>
<hr />
<h2 id="availability">Availability</h2>
<p>These sequence fields are available in:</p>
<ul>
<li><a href="/waf/custom-rules/">Custom rules</a> (<code>http_request_firewall_custom</code> phase)</li>
<li><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> (<code>http_request_ratelimit</code>)</li>
<li><a href="/workers/examples/bulk-redirects/">Bulk Redirects</a> (<code>http_request_redirect</code>)</li>
<li><a href="/rules/transform/response-header-modification/">Request Header Transform Rules</a> (<code>http_request_late_transform</code>)</li>
</ul>
<table>
<thead>
<tr>
<th style="width: 35%;">Field name</th>
<th>Description</th>
<th>Example value</th>
</tr>
</thead>
<tbody style='vertical-align:top'>
<tr>
<td><p><code>cf.sequence.current_op</code><br />`String`</p></td>
<td>
          <p>This field contains the ID of the operation that matches the current request. If the current request does not match any operations defined in Endpoint Management, it will be an empty string.</p>
</td>
<td><p><code>c821cc00</code></p></td>
</tr>
<tr>
<td><p><code>cf.sequence.previous_ops</code><br />`Array<String>`</p></td>
<td>
          <p>This field contains an array of the prior operation IDs in the sequence, ordered from most to least recent. It does not include the current request. <br /><br /> If an operation is repeated, it will appear multiple times in the sequence.</p>
</td>
<td><p><code>["f54dac32", "c821cc00", "a37dc89b"]</code></p></td>
</tr>
<tr>
<td><p><code>cf.sequence.msec_since_op</code><br />`Map<Number>`</p></td>
<td>
          <p>This field contains a map where the keys are operation IDs and the values are the number of milliseconds since that operation has most recently occurred. <br /><br /> This does not include the current request or operation as it only factors in previous operations in the sequence.</p>
</td>
<td><p>`{"f54dac32": 1000, "c821cc00": 2000}`</p></td>
</tr>
</tbody>
</table>
<hr />
<h2 id="build-a-sequence-custom-rule-via-the-cloudflare-dashboard">Build a sequence custom rule via the Cloudflare dashboard</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3533.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3531.md")
</aside>
<hr />
<h2 id="manage-sequence-rules-via-the-api">Manage sequence rules via the API</h2>
<h3 id="enable-sequence-rules">Enable sequence rules</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3534.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3530.md")
</aside>
<pre><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/zones/{zone_id}/fraud_detection/sequence_cookies \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&quot;enabled&quot;: true}&#x27;&#10;</code></pre>
<ol start="5">
<li>Use the expression editor to write sequence or timing based rules via <a href="/waf/custom-rules/">custom rules</a>, <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, or <a href="/rules/transform/">transform rules</a>. You can put these rules in log only mode to monitor.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3529.md")
</aside>
<p>Once you have enabled sequence rules, the rules fields will be populated and you can now use the new fields in your rules.</p>
<h3 id="disable-sequence-rules">Disable sequence rules</h3>
<p>Disabling sequence rules will stop the rules fields from being populated. If you still have rules deployed which depend on these fields, those rules may not behave as intended. Remove or disable any rules that rely on sequence fields before disabling sequence rules.</p>
<p>To disable sequence rules:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3535.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3528.md")
</aside>
<pre><code class="language-bash">curl --request PUT https://api.cloudflare.com/client/v4/zones/{zone_id}/fraud_detection/sequence_cookies \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;enabled&quot;: false}&#x27;&#10;</code></pre>
<hr />
<h2 id="rules-fields">Rules fields</h2>
<p>Sequence rules introduces three new fields to Cloudflare Rules. All of these fields reference operations by their short ID. Accounts that have the Fraud Detection subscription can refer to the short ID by viewing the endpoint details via <strong>API Shield</strong> &gt; <strong>Endpoint Management</strong> in the Cloudflare dashboard. Accounts without Fraud Detection do not have access to this field.</p>
<p>Cloudflare only stores up to the 10 most recent operations in a sequence for up to one hour. If there are more than 10 operations in the sequence, older operations will be dropped and will not be included in the following fields. Similarly, if an operation happened more than one hour ago, it will also not be included in the following fields.</p>
<h3 id="example-rules">Example rules</h3>
<p>The customer must request endpoint A before endpoint B.</p>
<pre><code class="language-txt">cf.sequence.current_op eq &quot;bbbbbbbb&quot; and&#10;any(cf.sequence.previous_ops[*] == &quot;aaaaaaaa&quot;)&#10;</code></pre>
<pre><code class="language-txt">cf.sequence.current_op eq &quot;bbbbbbbb&quot; and&#10;not any(cf.sequence.previous_ops[*] == &quot;aaaaaaaa&quot;)&#10;</code></pre>
<p>Customer must request endpoint A at least one second before endpoint B.</p>
<pre><code class="language-txt">cf.sequence.current_op eq &quot;bbbbbbbb&quot; and&#10;cf.sequence.msec_since_op[&quot;aaaaaaaa&quot;] ge 1000&#10;</code></pre>
<pre><code class="language-txt">cf.sequence.current_op eq &quot;bbbbbbbb&quot; and&#10;not cf.sequence.msec_since_op[&quot;aaaaaaaa&quot;] ge 1000&#10;</code></pre>
<hr />
<h2 id="limitations">Limitations</h2>
<p>Cloudflare only supports HTTPS requests since our cookies set the <code>Secure</code> attribute.</p>
<hr />
<h2 id="availability-1">Availability</h2>
<p>Sequence rules is currently in private beta. If you would like to be included in the beta, contact your account team.</p>
