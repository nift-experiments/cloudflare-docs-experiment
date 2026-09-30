<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3235.md")
</aside>
<p>Schema Learning observes qualifying traffic for selected operations. It learns expected request fields and constraints for a Schema Profile.</p>
<h2 id="start-profile-learning">Start profile learning</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3236.md")
</div>
<p>Cloudflare runs an <strong>always-on detection</strong> after the learned profile becomes available. The detection does not mitigate requests by itself.</p>
<p>To investigate results, refer to <a href="/waf/detections/application-profiles/analyze-profile-detections/">Analyze profile detections</a>. To mitigate violations, refer to <a href="/waf/detections/application-profiles/enforce-profiles-with-custom-rules/">Enforce profiles with Custom Rules</a>.</p>
<h2 id="meet-learning-requirements">Meet learning requirements</h2>
<p>Learning runs weekly using qualifying traffic from the previous seven days. Only requests that received a <code>2xx</code> response contribute.</p>
<p>The field-learning threshold requires 1,000 qualifying requests. The boundary-learning threshold requires 10,000 qualifying requests.</p>
<p>The first profile appears after the next weekly learning run. This can take up to seven days after meeting the relevant threshold.</p>
<p>For supported request components, constraints, and limitations, refer to <a href="/waf/detections/application-profiles/schema-profiles/">Schema Profiles</a>.</p>
<h2 id="export-a-schema">Export a schema</h2>
<p>Export creates a separate OpenAPI file from the current learned profile. It does not change the profile or its detection.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3237.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3234.md")
</aside>
<h2 id="learned-schema-contents">Learned schema contents</h2>
<p>Exported schemas include the listed hostname in the servers section. They also include operations by hostname, method, and path.</p>
<p>For operations that receive sufficient traffic, exported schemas also include:</p>
<ul>
<li>Detected path variables and formats</li>
<li>Detected query parameters and formats</li>
<li>Detected <code>POST</code>, <code>PUT</code>, and <code>PATCH</code> body variable names and formats for <code>application/json</code> content types</li>
</ul>
<p>Exported schemas can optionally include API Shield rate limit recommendations.</p>
<p>For a fixed Schema Profile, upload the exported file through <a href="/api-shield/security/schema-validation/">Schema validation</a>.</p>
