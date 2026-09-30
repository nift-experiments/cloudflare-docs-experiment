<h2 id="rate-limit-suspicious-logins-with-leaked-credentials">Rate limit suspicious logins with leaked credentials</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15535.md")
</aside>
<p><a href="/waf/rate-limiting-rules/create-zone-dashboard/">Create a rate limiting rule</a> using <a href="/bots/additional-configurations/detection-ids/account-takeover-detections/">account takeover (ATO) detection</a> and leaked credentials fields to limit volumetric attacks from particular IP addresses, JA4 Fingerprints, or countries.</p>
<p>The following example rule applies rate limiting to requests with a specific <a href="/bots/additional-configurations/detection-ids/account-takeover-detections/">ATO detection ID</a> (corresponding to <code>Observes all login traffic to the zone</code>) that contain a previously leaked username and password:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/15536.md")
</div>
<h2 id="challenge-requests-containing-leaked-credentials">Challenge requests containing leaked credentials</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15534.md")
</aside>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> that challenges requests containing a previously leaked set of credentials (username and password).</p>
<ul>
<li><strong>Expression</strong>: If you use the Expression Builder, configure the following expression:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User and Password Leaked</td>
<td>equals</td>
<td>True</td>
</tr>
</tbody>
</table>
<p>If you use the Expression Editor, enter the following expression:</p>
<pre><code class="language-txt">(cf.waf.credential_check.username_and_password_leaked)&#10;</code></pre>
<ul>
<li><strong>Action</strong>: <em>Managed Challenge</em></li>
</ul>
<hr />
