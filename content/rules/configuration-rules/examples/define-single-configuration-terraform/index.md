<p class="article-summary">Create a configuration rule using Terraform to turn off Email Obfuscation and Browser Integrity Check for API requests in a given zone.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13064.md")
</aside>
<p>The following example defines a single configuration rule for a zone using Terraform. The rule disables Email Obfuscation and Browser Integrity Check for API requests.</p>
<pre><code class="language-tf">&#35; Disable a couple of Cloudflare settings for API requests&#10;resource &quot;cloudflare_ruleset&quot; &quot;http_config_rules_example&quot; {&#10;  zone_id     = &quot;&lt;ZONE_ID&gt;&quot;&#10;  name        = &quot;Config rules ruleset&quot;&#10;  description = &quot;Set configuration rules for incoming requests&quot;&#10;  kind        = &quot;zone&quot;&#10;  phase       = &quot;http_config_settings&quot;&#10;&#10;  rules {&#10;    ref         = &quot;disable_obfuscation_bic&quot;&#10;    description = &quot;Disable email obfuscation and BIC for API requests&quot;&#10;    expression  = &quot;(http.request.uri.path matches \&quot;^/api/\&quot;)&quot;&#10;    action      = &quot;set_config&quot;&#10;    action_parameters {&#10;      email_obfuscation = false&#10;      bic               = false&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a> in the Terraform documentation.</p>
<h2 id="additional-resources">Additional resources</h2>
<p>For additional guidance on using Terraform with Cloudflare, refer to the following resources:</p>
<ul>
<li><a href="/terraform/">Terraform documentation</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Provider for Terraform</a> (reference documentation)</li>
</ul>
