<p>Application Profiles define application-specific expectations and classify requests against them. They add a positive-security model to your existing protections.</p>
<p>Schema Profile is the only current profile type. It models supported request fields, types, formats, ranges, and values.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15544.md")
</aside>
<h2 id="understand-the-profile-lifecycle">Understand the profile lifecycle</h2>
<p>A Schema Profile can come from observed traffic or an uploaded <a href="/api-shield/security/schema-validation/">OpenAPI schema</a>. Both sources produce the same profile type.</p>
<p>An operation is Cloudflare's term for an endpoint identified by HTTP method, hostname pattern, and path pattern. <a href="/security/web-assets/">Web Assets</a> continuously discovers operations, and you can add operations manually.</p>
<p>Discovery and manual creation only add operations to your inventory. Profiling starts when you select <strong>Learn profile</strong> for an operation.</p>
<p>After the profile becomes available, Cloudflare runs an <strong>always-on detection</strong>. The detection classifies requests but does not mitigate traffic.</p>
<p>Review results in <strong>Profile Analysis</strong> before creating a <a href="/waf/custom-rules/">Custom Rule</a>. This keeps detection, investigation, and mitigation as separate steps.</p>
<h2 id="complement-existing-detections">Complement existing detections</h2>
<p>Positive security identifies requests outside your expected application structure. A non-conforming request does not need to match an attack signature.</p>
<p>Application Profiles complement <a href="/waf/managed-rules/">Managed Rules</a>, <a href="/waf/detections/attack-score/">Attack Score</a>, and other negative-security detections. You can combine these signals in Custom Rules.</p>
<h2 id="explore-application-profiles">Explore Application Profiles</h2>
<ul class="directory-listing"><li><a href="/waf/detections/application-profiles/get-started/">Get started</a></li><li><a href="/waf/detections/application-profiles/schema-profiles/">Schema Profiles</a></li><li><a href="/waf/detections/application-profiles/analyze-profile-detections/">Analyze profile detections</a></li><li><a href="/waf/detections/application-profiles/enforce-profiles-with-custom-rules/">Enforce profiles with Custom Rules</a></li><li><a href="/waf/detections/application-profiles/fields/">Fields</a></li></ul>
<h2 id="see-also">See also</h2>
<ul>
<li><a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema learning</a></li>
<li><a href="/api-shield/security/schema-validation/">Schema validation</a></li>
</ul>
