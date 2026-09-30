<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15420.md")
</aside>
<p>At the account level, rate limiting rules are grouped into rate limiting rulesets. You must first create a custom ruleset with one or more rate limiting rules, and then deploy it to one or more zones on an Enterprise plan.</p>
<p>For more information on rule parameters, refer to <a href="/waf/rate-limiting-rules/parameters/">Rate limiting parameters</a>.</p>
<h2 id="1-create-a-custom-rate-limiting-ruleset"><ol>
<li>Create a custom rate limiting ruleset</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15421.md")
</div>
<h2 id="2-deploy-the-custom-rate-limiting-ruleset"><ol start="2">
<li>Deploy the custom rate limiting ruleset</li>
</ol></h2>
<p>To deploy a custom rate limiting ruleset to one or more zones on an Enterprise plan:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15422.md")
</div>
<p>The <strong>Deployed custom rate limiting rulesets</strong> list will show a rule for each deployed custom rate limiting ruleset.</p>
<h2 id="configure-a-custom-response-for-blocked-requests">Configure a custom response for blocked requests</h2>
<p>When you select the <em>Block</em> action in a rule you can optionally define a custom response.</p>
<p>The custom response has three settings:</p>
<ul>
<li><strong>With response type</strong>: Choose a content type or the default rate limiting response from the list. The available custom response types are the following:</li>
</ul>
<table>
<thead>
<tr>
<th>Dashboard value</th>
<th>API value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Custom HTML</td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
<tr>
<td>Custom Text</td>
<td><code>&quot;text/plain&quot;</code></td>
</tr>
<tr>
<td>Custom JSON</td>
<td><code>&quot;application/json&quot;</code></td>
</tr>
<tr>
<td>Custom XML</td>
<td><code>&quot;text/xml&quot;</code></td>
</tr>
</tbody>
</table>
<ul>
<li>
<p><strong>With response code</strong>: Choose an HTTP status code for the response, in the range 400-499. The default response code is 429.</p>
</li>
<li>
<p><strong>Response body</strong>: The body of the response. Configure a valid body according to the response type you selected. The maximum field size is 30 KB.</p>
</li>
</ul>
