<p class="article-summary">Create an origin rule using Terraform to override the `Host` header, the resolved hostname, and the destination port of API requests.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13083.md")
</aside>
<p>The following example defines a single origin rule for a zone using Terraform. The rule overrides the <code>Host</code> header, the resolved hostname, and the destination port of API requests.</p>
<pre><code class="language-tf">&#35; Change origin for API requests&#10;resource &quot;cloudflare_ruleset&quot; &quot;http_origin_example&quot; {&#10;  zone_id     = &quot;&lt;ZONE_ID&gt;&quot;&#10;  name        = &quot;Change origin&quot;&#10;  description = &quot;&quot;&#10;  kind        = &quot;zone&quot;&#10;  phase       = &quot;http_request_origin&quot;&#10;&#10;  rules {&#10;	  ref         = &quot;change_api_origin&quot;&#10;    description = &quot;Change origin of API requests&quot;&#10;    expression  = &quot;(http.request.uri.path matches \&quot;^/api/\&quot;)&quot;&#10;    action      = &quot;route&quot;&#10;    action_parameters {&#10;      host_header = &quot;example.net&quot;&#10;      origin {&#10;        host = &quot;example.net&quot;&#10;        port = 8000&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a> in the Terraform documentation.</p>
<h2 id="additional-resources">Additional resources</h2>
<p>For additional guidance on using Terraform with Cloudflare, refer to the following resources:</p>
<ul>
<li><a href="/terraform/">Terraform documentation</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Provider for Terraform</a> (reference documentation)</li>
</ul>
