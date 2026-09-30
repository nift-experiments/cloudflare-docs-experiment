<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create a redirect rule via API.</p>
<p>Add redirect rules to the entry point ruleset of the <code>http_request_dynamic_redirect</code> phase at the zone level. Refer to the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> documentation for more information on <a href="/ruleset-engine/rulesets-api/create/">creating a ruleset</a> and supplying a list of rules for the ruleset.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13193.md")
</aside>
<h2 id="basic-rule-settings">Basic rule settings</h2>
<p>A redirect rule must have:</p>
<ul>
<li><code>action</code> set to <code>redirect</code></li>
<li>An <code>action_parameters</code> object with additional configuration settings — refer to <a href="/rules/url-forwarding/single-redirects/settings/">Single Redirects settings</a> for details.</li>
</ul>
<h2 id="example-requests">Example requests</h2>
<p>The following request of the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation creates a phase entry point ruleset for the <code>http_request_dynamic_redirect</code> phase at the zone level, and defines a single redirect rule with a dynamic URL redirect. Use this operation if you have not created a phase entry point ruleset for the <code>http_request_dynamic_redirect</code> phase yet.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Redirect rules ruleset&quot;,&#10;  &quot;kind&quot;: &quot;zone&quot;,&#10;  &quot;phase&quot;: &quot;http_request_dynamic_redirect&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;ref&quot;: &quot;redirect_gb_fr_to_localized&quot;,&#10;      &quot;expression&quot;: &quot;(ip.src.country eq \&quot;GB\&quot; or ip.src.country eq \&quot;FR\&quot;) and http.request.uri.path eq \&quot;/\&quot;&quot;,&#10;      &quot;description&quot;: &quot;Redirect GB and FR users in home page to localized site.&quot;,&#10;      &quot;action&quot;: &quot;redirect&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;from_value&quot;: {&#10;          &quot;target_url&quot;: {&#10;            &quot;expression&quot;: &quot;lower(concat(\&quot;https://\&quot;, ip.src.country, \&quot;.example.com\&quot;))&quot;&#10;          },&#10;          &quot;status_code&quot;: 307,&#10;          &quot;preserve_query_string&quot;: true&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<details class="nb-details"><summary>Response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13194.md")
</div></details>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a> in the Terraform documentation.</p>
<p>If there is already a phase entry point ruleset for the <code>http_request_dynamic_redirect</code> phase, use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset</a> operation instead, like in the following example:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Redirect rules ruleset&quot;,&#10;  &quot;kind&quot;: &quot;zone&quot;,&#10;  &quot;phase&quot;: &quot;http_request_dynamic_redirect&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;ref&quot;: &quot;redirect_gb_fr_to_localized&quot;,&#10;      &quot;expression&quot;: &quot;(ip.src.country eq \&quot;GB\&quot; or ip.src.country eq \&quot;FR\&quot;) and http.request.uri.path eq \&quot;/\&quot;&quot;,&#10;      &quot;description&quot;: &quot;Redirect GB and FR users in home page to localized site.&quot;,&#10;      &quot;action&quot;: &quot;redirect&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;from_value&quot;: {&#10;          &quot;target_url&quot;: {&#10;            &quot;expression&quot;: &quot;lower(concat(\&quot;https://\&quot;, ip.src.country, \&quot;.example.com\&quot;))&quot;&#10;          },&#10;          &quot;status_code&quot;: 307,&#10;          &quot;preserve_query_string&quot;: true&#10;        }&#10;      }&#10;    },&#10;    {&#10;      &quot;ref&quot;: &quot;redirect_contacts_to_new_page&quot;,&#10;      &quot;expression&quot;: &quot;http.request.uri.path eq \&quot;/contacts.html\&quot;&quot;,&#10;      &quot;description&quot;: &quot;Redirect to new contacts page.&quot;,&#10;      &quot;action&quot;: &quot;redirect&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;from_value&quot;: {&#10;          &quot;target_url&quot;: {&#10;            &quot;value&quot;: &quot;https://example.com/contact-us/&quot;&#10;          },&#10;          &quot;status_code&quot;: 308&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<details class="nb-details"><summary>Response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13195.md")
</div></details>
<hr />
<h2 id="required-api-token-permissions">Required API token permissions</h2>
<p>The API token used in API requests to manage redirect rules must have at least the following permission:</p>
<ul>
<li><em>Zone</em> &gt; <em>Single Redirect</em> &gt; <em>Edit</em></li>
</ul>
