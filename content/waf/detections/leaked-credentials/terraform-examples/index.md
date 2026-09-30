<p>The following Terraform configuration examples address common scenarios for managing, configuring, and using leaked credentials detection.</p>
<p>For more information, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform Cloudflare provider documentation</a>.</p>
<p>If you are using the Cloudflare API, refer to <a href="/waf/detections/leaked-credentials/api-calls/">Common API calls</a>.</p>
<h2 id="enable-leaked-credentials-detection">Enable leaked credentials detection</h2>
<p>Use the <code>cloudflare_leaked_credential_check</code> resource to enable leaked credentials detection for a zone. For example:</p>
<pre><code class="language-terraform">resource &quot;cloudflare_leaked_credential_check&quot; &quot;zone_lcc_example&quot; {&#10;	zone_id = var.cloudflare_zone_id&#10;	enabled = true&#10;}&#10;</code></pre>
<h2 id="configure-a-custom-detection-location">Configure a custom detection location</h2>
<p>Use the <code>cloudflare_leaked_credential_check_rule</code> resource to add a custom detection location. For example:</p>
<pre><code class="language-terraform">resource &quot;cloudflare_leaked_credential_check_rule&quot; &quot;custom_location_example&quot; {&#10;	zone_id = var.cloudflare_zone_id&#10;	username = &quot;lookup_json_string(http.request.body.raw, \&quot;user\&quot;)&quot;&#10;	password = &quot;lookup_json_string(http.request.body.raw, \&quot;secret\&quot;)&quot;&#10;}&#10;</code></pre>
<p>You only need to provide an expression for the username in custom detection locations.</p>
<h2 id="add-a-custom-rule-to-challenge-requests-with-leaked-credentials">Add a custom rule to challenge requests with leaked credentials</h2>
<p>This example adds a <a href="/waf/custom-rules/">custom rule</a> that challenges requests with leaked credentials by using one of the <a href="/waf/detections/leaked-credentials/#leaked-credentials-fields">leaked credentials fields</a> in the rule expression.</p>
<p>To use the <a href="/ruleset-engine/rules-language/fields/reference/cf.waf.credential_check.username_and_password_leaked/"><code>cf.waf.credential_check.username_and_password_leaked</code></a> field you must <a href="#enable-leaked-credentials-detection">enable leaked credentials detection</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15515.md")
</div></div>
<h2 id="more-resources">More resources</h2>
<p>For additional Terraform configuration examples, refer to <a href="/terraform/additional-configurations/waf-custom-rules/">WAF custom rules configuration using Terraform</a>.</p>
