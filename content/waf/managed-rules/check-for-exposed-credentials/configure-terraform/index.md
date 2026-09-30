<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/15656.md")
</aside>
<p>The following Terraform configuration example addresses a common use case of exposed credentials checks.</p>
<p>For more information, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform Cloudflare provider documentation</a>.</p>
<p>If you are using the Cloudflare API, refer to <a href="/waf/managed-rules/check-for-exposed-credentials/configure-api/">Configure exposed credentials checks via API</a>.</p>
<h2 id="add-a-custom-rule-to-check-for-exposed-credentials">Add a custom rule to check for exposed credentials</h2>
<p>The following configuration creates a custom ruleset with a single rule that <a href="/waf/managed-rules/check-for-exposed-credentials/configure-api/#create-a-custom-rule-checking-for-exposed-credentials">checks for exposed credentials</a>.</p>
<p>You can only add exposed credential checks to rules in a custom ruleset (that is, a ruleset with <code>kind = &quot;custom&quot;</code>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15655.md")
</aside>
<pre><code class="language-tf">resource &quot;cloudflare_ruleset&quot; &quot;account_firewall_custom_ruleset_exposed_creds&quot; {&#10;  account_id  = &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;  name        = &quot;Custom ruleset checking for exposed credentials&quot;&#10;  description = &quot;&quot;&#10;  kind        = &quot;custom&quot;&#10;  phase       = &quot;http_request_firewall_custom&quot;&#10;&#10;  rules {&#10;    ref         = &quot;check_for_exposed_creds_add_header&quot;&#10;    description = &quot;Add header when there is a rule match and exposed credentials are detected&quot;&#10;    expression  = &quot;http.request.method == \&quot;POST\&quot; &amp;&amp; http.request.uri == \&quot;/login.php\&quot;&quot;&#10;    action      = &quot;rewrite&quot;&#10;    action_parameters {&#10;      headers {&#10;        name      = &quot;Exposed-Credential-Check&quot;&#10;        operation = &quot;set&quot;&#10;        value     = &quot;1&quot;&#10;      }&#10;    }&#10;    exposed_credential_check {&#10;      username_expression = &quot;url_decode(http.request.body.form[\&quot;username\&quot;][0])&quot;&#10;      password_expression = &quot;url_decode(http.request.body.form[\&quot;password\&quot;][0])&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>To create another rule, add a new <code>rules</code> object to the same <code>cloudflare_ruleset</code> resource.</p>
<p>The following configuration deploys the custom ruleset. It defines a dependency on the <code>account_firewall_custom_ruleset_exposed_creds</code> resource and obtains the ID of the created custom ruleset:</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15654.md")
</aside>
<pre><code class="language-tf">resource &quot;cloudflare_ruleset&quot; &quot;account_firewall_custom_entrypoint&quot; {&#10;  account_id  = &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;  name        = &quot;Account-level entry point ruleset for the http_request_firewall_custom phase deploying a custom ruleset checking for exposed credentials&quot;&#10;  description = &quot;&quot;&#10;  kind        = &quot;root&quot;&#10;  phase       = &quot;http_request_firewall_custom&quot;&#10;&#10;  depends_on = [cloudflare_ruleset.account_firewall_custom_ruleset_exposed_creds]&#10;&#10;  rules {&#10;    ref         = &quot;deploy_custom_ruleset_example_com&quot;&#10;    description = &quot;Deploy custom ruleset for example.com&quot;&#10;    expression  = &quot;(cf.zone.name eq \&quot;example.com\&quot;)&quot;&#10;    action      = &quot;execute&quot;&#10;    action_parameters {&#10;      id = cloudflare_ruleset.account_firewall_custom_ruleset_exposed_creds.id&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="more-resources">More resources</h2>
<p>For additional Terraform configuration examples, refer to <a href="/terraform/additional-configurations/waf-custom-rules/">WAF custom rules configuration using Terraform</a>.</p>
