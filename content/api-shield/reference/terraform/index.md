<p>Get started with API Shield using Terraform from the examples below. For more information on how to use Terraform with Cloudflare, refer to the <a href="/terraform/">Terraform documentation</a>.</p>
<p>The following resources are available to configure through Terraform:</p>
<p><strong>Session identifiers</strong></p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_shield"><code>api_shield</code></a> for configuring <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/3205.md")
</div> in API Shield.
<p><strong>Web Assets operations</strong></p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_shield_operation"><code>api_shield_operation</code></a> for configuring <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/3206.md")
</div>.
<p><strong>Schema validation</strong></p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/schema_validation_schemas"><code>cloudflare_schema_validation_schemas</code></a> for configuring a schema in <a href="/api-shield/security/schema-validation/">Schema validation</a>.
<del><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_shield_schema"><code>api_shield_schema</code></a></del> has been deprecated and will be removed in a future version of the terraform provider.</li>
</ul>
<p><strong>JWT Validation</strong></p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/token_validation_config"><code>cloudflare_token_validation_config</code></a> for setting up JWT validation with specific keying material and token locations.</li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/token_validation_rules"><code>cloudflare_token_validation_rules</code></a> for setting up rules to action on the validation result.</li>
</ul>
<h2 id="manage-api-shield-session-identifiers">Manage API Shield session identifiers</h2>
<p>Refer to the example configuration below to set up <a href="/api-shield/get-started/#to-set-up-session-identifiers">session identifiers</a> on your zone.</p>
<pre><code class="language-tf">resource &quot;cloudflare_api_shield&quot; &quot;session_identifiers&quot; {&#10;  zone_id = var.zone_id&#10;  auth_id_characteristics = [{&#10;    name = &quot;authorization&quot;&#10;    type = &quot;header&quot;&#10;  }]&#10;}&#10;</code></pre>
<h2 id="manage-web-assets-operations">Manage Web Assets operations</h2>
<p>Manage operations by method, hostname, and path. Operations appear in the Web Assets inventory.</p>
<pre><code class="language-tf">resource &quot;cloudflare_api_shield_operation&quot; &quot;get_image&quot; {&#10;  zone_id  = var.zone_id&#10;  method   = &quot;GET&quot;&#10;  host     = &quot;example.com&quot;&#10;  endpoint = &quot;/api/images/{var1}&quot;&#10;}&#10;&#10;resource &quot;cloudflare_api_shield_operation&quot; &quot;post_image&quot; {&#10;  zone_id  = var.zone_id&#10;  method   = &quot;POST&quot;&#10;  host     = &quot;example.com&quot;&#10;  endpoint = &quot;/api/images/{var1}&quot;&#10;}&#10;</code></pre>
<h2 id="manage-schema-validation">Manage Schema validation</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3204.md")
</aside>
<p>The schema resource uploads an OpenAPI schema. Setting <code>validation_enabled</code> to <code>true</code> makes uploaded profile evaluation available.</p>
<pre><code class="language-tf">&#35; Upload an OpenAPI schema for Schema Validation&#10;resource &quot;cloudflare_schema_validation_schemas&quot; &quot;example_schema&quot; {&#10;  zone_id            = var.zone_id&#10;  kind               = &quot;openapi_v3&quot;&#10;  name               = &quot;example-schema.yaml&quot;&#10;  &#35; In this example, we assume that the `example-schema.yaml` includes `get_image` and `post_image` operations from above&#10;  source             = file(&quot;./schemas/example-schema.yaml&quot;)&#10;  validation_enabled = true&#10;}&#10;</code></pre>
<p>Activation does not configure mitigation. Use <code>cf.schema_validation.uploaded.violated</code> in <a href="/waf/detections/application-profiles/enforce-profiles-with-custom-rules/">WAF Custom Rules</a>.</p>
<h2 id="validate-jwts">Validate JWTs</h2>
<p>Refer to the example configuration below to perform <a href="/api-shield/security/jwt-validation/">JWT Validation</a> on your zone.</p>
<pre><code class="language-tf">&#35; Setting up JWT validation with specific keying material and location of the token&#10;resource &quot;cloudflare_token_validation_config&quot; &quot;example_es256_config&quot; {&#10;  zone_id       = var.zone_id&#10;  token_type    = &quot;JWT&quot;&#10;  title         = &quot;ES256 Example&quot;&#10;  description   = &quot;An example configuration that validates ES256 JWTs with `b0078548-c9bc-46e5-a678-06fb72443427` key ID in the authorization header&quot;&#10;  token_sources = [&quot;http.request.headers[\&quot;authorization\&quot;][0]&quot;]&#10;  credentials   = {&#10;    keys = [&#10;      {&#10;        alg = &quot;ES256&quot;&#10;        kid = &quot;b0078548-c9bc-46e5-a678-06fb72443427&quot;&#10;        kty = &quot;EC&quot;&#10;        crv = &quot;P-256&quot;&#10;        x   = &quot;yl_BZSxUG5II7kJCMxDfWImiU6zkcJcBYaTgzV3Jgnk&quot;&#10;        y   = &quot;0qAzLQe_YGEdotb54qWq00k74QdiTOiWnuw_YzuIqr0&quot;&#10;      }&#10;    ]&#10;  }&#10;}&#10;&#10;&#35; Setting up JWT rules for all configured endpoints on `example.com` except for `get_image`&#10;resource &quot;cloudflare_token_validation_rules&quot; &quot;example_com&quot; {&#10; zone_id      = var.zone_id&#10; title        = &quot;Validate JWTs on example.com&quot;&#10; description  = &quot;This actions JWT validation results for requests to example.com except for the get_image endpoint&quot;&#10; action       = &quot;block&quot;&#10; enabled      = true&#10; &#35; Require that the JWT described through the example_es256_config is valid.&#10; &#35; Reference the ID of the generated token config, this constructs: is_jwt_valid(&quot;&lt;id&gt;&quot;)&#10; &#35; If the expression is &gt;not true&lt;, Cloudflare will perform the configured action on the request&#10; expression   = format(&quot;(is_jwt_valid(%q))&quot;, cloudflare_token_validation_config.example_es256_config.id)&#10; selector     = {&#10;    &#35; all current and future operations matching this include selector will perform the described action when the expression fails to match&#10;    include = [&#10;      {&#10;        host          = [&quot;example.com&quot;]&#10;      }&#10;    ]&#10;    exclude = [&#10;      {&#10;        &#35; reference the ID of the get_image operation to exclude it&#10;        operation_ids = [&quot;${cloudflare_api_shield_operation.get_image.id}&quot;]&#10;      }&#10;    ]&#10; }&#10;}&#10;&#10;&#35; With JWT validation, we can also refine session identifiers to use claims from the JWT&#10;resource &quot;cloudflare_api_shield&quot; &quot;session_identifiers&quot; {&#10;  zone_id = var.zone_id&#10;  auth_id_characteristics = [{&#10;    &#35; select the JWT&#x27;s `sub` claim as an extremely stable session identifier&#10;    &#35; this is &quot;&lt;token_config_id:json_path&gt;&quot; format&#10;    name = &quot;${cloudflare_token_validation_config.example_es256_config.id}:$.sub&quot;&#10;    type = &quot;jwt&quot;&#10;  }]&#10;}&#10;</code></pre>
