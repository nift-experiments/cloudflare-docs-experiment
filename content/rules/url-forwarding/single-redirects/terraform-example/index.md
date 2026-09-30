<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13186.md")
</aside>
<p>The following example defines a single redirect rule for a zone using Terraform. The rule creates a static URL redirect for visitors requesting the contacts page using an old URL.</p>
<pre><code class="language-tf">&#35; Single Redirects resource&#10;resource &quot;cloudflare_ruleset&quot; &quot;single_redirects_example&quot; {&#10;  zone_id     = &quot;&lt;ZONE_ID&gt;&quot;&#10;  name        = &quot;redirects&quot;&#10;  description = &quot;Redirects ruleset&quot;&#10;  kind        = &quot;zone&quot;&#10;  phase       = &quot;http_request_dynamic_redirect&quot;&#10;&#10;  rules {&#10;    ref         = &quot;redirect_old_url&quot;&#10;    description = &quot;Redirect visitors still using old URL&quot;&#10;    expression  = &quot;(http.request.uri.path matches \&quot;^/contact-us/\&quot;)&quot;&#10;    action      = &quot;redirect&quot;&#10;    action_parameters {&#10;      from_value {&#10;        status_code = 301&#10;        target_url {&#10;          value = &quot;/contacts/&quot;&#10;        }&#10;        preserve_query_string = false&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a> in the Terraform documentation.</p>
<h2 id="additional-resources">Additional resources</h2>
<p>For additional guidance on using Terraform with Cloudflare, refer to the following resources:</p>
<ul>
<li><a href="/terraform/">Terraform documentation</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Provider for Terraform</a> (reference documentation)</li>
</ul>
