<p>Create a learned Schema Profile for one operation. Then review its detections before configuring mitigation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15545.md")
</aside>
<h2 id="review-learning-requirements">Review learning requirements</h2>
<p>Cloudflare learns profiles weekly from qualifying traffic during the previous seven days. Only requests that received a <code>2xx</code> response qualify.</p>
<p>An operation needs 1,000 qualifying requests for the field-learning threshold. It needs 10,000 qualifying requests for the boundary-learning threshold.</p>
<p>After meeting the field-learning threshold, Cloudflare can learn request fields. After meeting the boundary-learning threshold, Cloudflare can learn constraints such as numeric ranges and string lengths.</p>
<p>The first profile appears after the next weekly learning run. This can take up to seven days after meeting the relevant threshold.</p>
<h2 id="learn-and-review-a-profile">Learn and review a profile</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15546.md")
</div>
<p>After the profile becomes available, Cloudflare runs an <strong>always-on detection</strong>. It does not mitigate requests without a Custom Rule.</p>
<p>If no learned schema appears, confirm that you selected <strong>Learn profile</strong>. Cloudflare may still be collecting enough qualifying traffic.</p>
<p>For learning details and limitations, refer to <a href="/waf/detections/application-profiles/schema-profiles/">Schema Profiles</a>.</p>
<h2 id="use-an-uploaded-schema">Use an uploaded schema</h2>
<p>If you have an OpenAPI schema, upload it through <a href="/api-shield/security/schema-validation/">Schema validation</a>. Uploaded schemas produce detections through <code>cf.schema_validation.uploaded.violated</code>.</p>
<p>The API Shield reference covers upload formats, OpenAPI requirements, API configuration, Terraform configuration, and limitations.</p>
