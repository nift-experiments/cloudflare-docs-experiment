<p>The following Terraform configuration examples address common scenarios for managing, configuring, and using WAF content scanning.</p>
<p>For more information, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform Cloudflare provider documentation</a>.</p>
<p>If you are using the Cloudflare API, refer to <a href="/waf/detections/malicious-uploads/api-calls/">Common API calls</a>.</p>
<h2 id="enable-waf-content-scanning">Enable WAF content scanning</h2>
<p>Use the <code>cloudflare_content_scanning</code> resource to enable content scanning for a zone. For example:</p>
<pre><code class="language-terraform">resource &quot;cloudflare_content_scanning&quot; &quot;zone_content_scanning_example&quot; {&#10;	zone_id = var.cloudflare_zone_id&#10;	enabled = true&#10;}&#10;</code></pre>
<h2 id="configure-a-custom-scan-expression">Configure a custom scan expression</h2>
<p>Use the <code>cloudflare_content_scanning_expression</code> resource to add a custom scan expression. For example:</p>
<pre><code class="language-terraform">resource &quot;cloudflare_content_scanning_expression&quot; &quot;my_custom_scan_expression&quot; {&#10;  zone_id = var.cloudflare_zone_id&#10;  payload = &quot;lookup_json_string(http.request.body.raw, \&quot;file\&quot;)&quot;&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/waf/detections/malicious-uploads/#custom-scan-expressions">Custom scan expressions</a>.</p>
<h2 id="add-a-custom-rule-to-block-malicious-uploads">Add a custom rule to block malicious uploads</h2>
<p>This example adds a <a href="/waf/custom-rules/">custom rule</a> that blocks requests with one or more <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15489.md")
</div> considered malicious by using one of the [content scanning fields](/waf/detections/malicious-uploads/#content-scanning-fields) in the rule expression.
<p>To use the <a href="/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_malicious_obj/"><code>cf.waf.content_scan.has_malicious_obj</code></a> field you must <a href="#enable-waf-content-scanning">enable content scanning</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15493.md")
</div></div>
<h2 id="more-resources">More resources</h2>
<p>For additional Terraform configuration examples, refer to <a href="/terraform/additional-configurations/waf-custom-rules/">WAF custom rules configuration using Terraform</a>.</p>
