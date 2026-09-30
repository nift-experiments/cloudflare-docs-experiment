<h2 id="1-turn-on-the-detection"><ol>
<li>Turn on the detection</li>
</ol></h2>
<p>On Free plans, the leaked credentials detection is enabled by default, and no action is required. On paid plans, you can turn on the detection in the Cloudflare dashboard, via API, or using Terraform.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15525.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15520.md")
</aside>
<h2 id="2-validate-the-leaked-credentials-detection-behavior"><ol start="2">
<li>Validate the leaked credentials detection behavior</li>
</ol></h2>
<p>Use <a href="/waf/analytics/security-analytics/">Security Analytics</a> and HTTP logs to validate that Cloudflare is correctly detecting leaked credentials in incoming requests.</p>
<p>Refer to <a href="#test-your-configuration">Test your configuration</a> for more information on the test credentials you can use to validate your configuration.</p>
<p>Alternatively, create a custom rule like the one described in the next step using a <em>Log</em> action (only available to Enterprise customers). This rule will generate <a href="/waf/analytics/security-events/">security events</a> that will allow you to validate your configuration.</p>
<h2 id="3-mitigate-requests-with-leaked-credentials"><ol start="3">
<li>Mitigate requests with leaked credentials</li>
</ol></h2>
<p>If you are on a Free plan, deploy the suggested <a href="/waf/rate-limiting-rules/">rate limiting rule</a> template available in <strong>Security</strong> &gt; <strong>Security rules</strong>.</p>
<p>When you deploy a rule using this template, you get instant protection against IPs attempting to access your application with a leaked password more than five times per 10 seconds. This rule can delay attacks by blocking them for a period of time. Alternatively, you can create a custom rule.</p>
<p>Paid plans have access to more granular controls when creating a rule. If you are on a paid plan, <a href="/waf/custom-rules/create-dashboard/">create a custom rule</a> that challenges requests containing leaked credentials:</p>
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
<p>Rule action: <em>Managed Challenge</em></p>
<p>This rule will match requests where Cloudflare detects a previously leaked set of credentials (username and password). For a list of fields provided by leaked credentials detection, refer to <a href="/waf/detections/leaked-credentials/#leaked-credentials-fields">Leaked credentials fields</a>.</p>
<details class="nb-details"><summary>Combine with other Rules language fields</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15526.md")
</div></details>
<p>For additional examples, refer to <a href="/waf/detections/leaked-credentials/examples/">Example mitigation rules</a>.</p>
<h3 id="handle-detected-leaked-credentials-at-the-origin-server">Handle detected leaked credentials at the origin server</h3>
<p>Additionally, you may want to handle leaked credentials detected by Cloudflare at your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15527.md")
</div>:
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15528.md")
</div>
<h2 id="4-optional-configure-a-custom-detection-location"><ol start="4">
<li>(Optional) Configure a custom detection location</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15519.md")
</aside>
<p>To check for leaked credentials in a way that is not covered by the default configuration, add a <a href="/waf/detections/leaked-credentials/#custom-detection-locations">custom detection location</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15533.md")
</div></div>
<p>You only need to provide an expression for the username in custom detection locations.</p>
<p>For more examples of custom detection locations for different request types, refer to <a href="/waf/detections/leaked-credentials/#custom-detection-locations">Custom detection locations</a>.</p>
<hr />
<h2 id="test-your-configuration">Test your configuration</h2>
<p>Cloudflare provides a special set of case-sensitive credentials for testing the configuration of the leaked credentials detection.</p>
<p>After enabling and configuring the detection, you can use the credentials mentioned in this section in your test HTTP requests.</p>
<p>Test credentials for users on a Free plan (will also work in paid plans):</p>
<ul>
<li>Username: <code>CF_LEAKED_USERNAME_FREE</code></li>
<li>Password: <code>CF_LEAKED_PASSWORD</code></li>
</ul>
<p>Test credentials for users on paid plans (will not work on Free plans):</p>
<ul>
<li>Username: <code>CF_EXPOSED_USERNAME</code> or <code>CF_EXPOSED_USERNAME@example.com</code></li>
<li>Password: <code>CF_EXPOSED_PASSWORD</code></li>
</ul>
<p>Cloudflare considers these specific credentials as having been previously leaked. Use them in your tests to check the behavior of your current configuration.</p>
