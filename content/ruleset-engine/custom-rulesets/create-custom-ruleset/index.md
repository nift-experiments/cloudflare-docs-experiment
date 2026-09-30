<p>Use the <a href="/api/resources/rulesets/methods/create/">Create an account or zone ruleset</a> operation to create a custom ruleset, making sure that you:</p>
<ul>
<li>Set the <code>kind</code> field to <code>custom</code>.</li>
<li>Specify the name of the <a href="/ruleset-engine/reference/phases-list/">phase</a> where you want to create the custom ruleset in the <code>phase</code> field.</li>
</ul>
<p>You can also specify the list of rules to include in the custom ruleset in the <code>rules</code> array. To add rules after creating the custom ruleset, refer to <a href="/ruleset-engine/custom-rulesets/add-rules-ruleset/">Add rules to a custom ruleset</a>.</p>
<p>If you are using Terraform, refer to <a href="/terraform/additional-configurations/waf-custom-rules/#create-and-deploy-a-custom-ruleset">WAF custom rules configuration using Terraform</a> for examples of creating and deploying custom rulesets.</p>
<p>If you are using the Cloudflare dashboard, refer to <a href="/waf/account/custom-rulesets/create-dashboard/">Work with custom rulesets in the dashboard</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13282.md")
</aside>
<h2 id="example-a-custom-ruleset-at-the-account-level">Example A - Custom ruleset at the account level</h2>
<p>The following request creates a new custom ruleset at the account level. The response will include the ID of the new custom ruleset in the <code>id</code> field.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Custom Ruleset 1&quot;,&#10;  &quot;description&quot;: &quot;My First Custom Ruleset (account)&quot;,&#10;  &quot;kind&quot;: &quot;custom&quot;,&#10;  &quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;f82ccda3d21f4a02825d3fe45b5e1c10&quot;,&#10;		&quot;name&quot;: &quot;Custom Ruleset 1&quot;,&#10;		&quot;description&quot;: &quot;My First Custom Ruleset (account)&quot;,&#10;		&quot;kind&quot;: &quot;custom&quot;,&#10;		&quot;version&quot;: &quot;1&quot;,&#10;		&quot;last_updated&quot;: &quot;2025-08-09T10:27:30.636197Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>You can include a list of rules in the custom ruleset creation request. If you have not added any rules, refer to <a href="/ruleset-engine/custom-rulesets/add-rules-ruleset/">Add rules to a custom ruleset</a> for more information.</p>
<h2 id="example-b-custom-ruleset-at-the-zone-level">Example B - Custom ruleset at the zone level</h2>
<p>The following request creates a new custom ruleset at the zone level. The response will include the ID of the new custom ruleset in the <code>id</code> field.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Custom Ruleset 1&quot;,&#10;  &quot;description&quot;: &quot;My First Custom Ruleset (zone)&quot;,&#10;  &quot;kind&quot;: &quot;custom&quot;,&#10;  &quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;f82ccda3d21f4a02825d3fe45b5e1c10&quot;,&#10;		&quot;name&quot;: &quot;Custom Ruleset 1&quot;,&#10;		&quot;description&quot;: &quot;My First Custom Ruleset (zone)&quot;,&#10;		&quot;kind&quot;: &quot;custom&quot;,&#10;		&quot;version&quot;: &quot;1&quot;,&#10;		&quot;last_updated&quot;: &quot;2025-08-09T10:27:30.636197Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>You can include a list of rules in the custom ruleset creation request. If you have not added any rules, refer to <a href="/ruleset-engine/custom-rulesets/add-rules-ruleset/">Add rules to a custom ruleset</a> for more information.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13281.md")
</aside>
