<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/3209.md")
</aside>
<p>Use the <strong>API Shield</strong> interface to configure <a href="/api-shield/security/schema-validation/">API Schema validation</a>, which validates requests according to the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3210.md")
</div> you provide.
<p>Before you can configure Schema validation for an API, you must obtain an API Schema file matching our <a href="/api-shield/security/schema-validation/#specifications">specifications</a>.</p>
<p>If you are in the Schema validation 2.0, you can make changes to your settings but you cannot add any new Classic Schema validation schemas.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3208.md")
</aside>
<h2 id="create-an-api-shield-with-schema-validation">Create an API Shield with Schema validation</h2>
<p>To configure Schema validation in the Cloudflare dashboard:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Select <strong>Security</strong> &gt; <strong>API Shield</strong>.</li>
<li>Go to <strong>Schema validation</strong> and select <strong>Add schema</strong>.</li>
<li>Enter a descriptive name for your policy and optionally edit the expression to trigger Schema validation. For example, if your API is available at <code>http://api.example.com/v1</code>, include a check for the <em>Hostname</em> field — equal to <code>api.example.com</code> — and a check for the <em>URI Path</em> field using a regular expression — matching the regex <code>^/v1</code>.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/3207.md")
</aside>
5. Select **Next**.
6. Upload your schema file.
7. Select **Save** to validate the content of the schema file and deploy the Schema validation rule. If you get a validation error, ensure that you are using one of the [supported file formats](/api-shield/security/schema-validation/#specifications) and that each endpoint and method pair has a unique operation ID.
<p>After deploying your API Shield rule, Cloudflare displays a summary of all <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3211.md")
</div> organized by their protection level and actions that will occur for non-compliant and unprotected requests.
<ol>
<li>In the <strong>Endpoint action</strong> dropdown, select an action for every request that targets a protected endpoint and fails Schema validation.</li>
<li>In the <strong>Fallthrough action</strong> dropdown, select an action for every request that targets an unprotected endpoint.</li>
<li>Optionally, you can save the endpoints to Endpoint Management at the same time the Schema is saved by selecting <strong>Save new endpoints to <a href="/api-shield/management-and-monitoring/">endpoint management</a></strong>. Endpoints will be saved regardless of whether the Schema is saved as a draft or published live.</li>
<li>Select <strong>Done</strong>.</li>
</ol>
