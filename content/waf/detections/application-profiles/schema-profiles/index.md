<p>A Schema Profile models expected request fields and their constraints. You can learn one from traffic or supply an uploaded schema.</p>
<p>After a profile becomes available, Cloudflare runs an <strong>always-on detection</strong>. Detection does not mitigate requests by itself.</p>
<h2 id="learn-from-traffic">Learn from traffic</h2>
<p>An operation is Cloudflare's term for an endpoint. Its identity combines an HTTP method, hostname pattern, and path pattern.</p>
<p><a href="/security/web-assets/">Web Assets</a> continuously discovers operations under <strong>Web Assets</strong> &gt; <strong>Operations</strong>. You can also add an operation manually.</p>
<p>Both methods only add operations to the inventory. To start profiling, select <strong>Learn profile</strong> from the operation overflow menu.</p>
<h3 id="meet-traffic-requirements">Meet traffic requirements</h3>
<p>Learning runs weekly using qualifying traffic from the previous seven days. Only requests that received a <code>2xx</code> response contribute.</p>
<p>The field-learning threshold requires 1,000 qualifying requests. The boundary-learning threshold requires 10,000 qualifying requests.</p>
<p>The field-learning threshold allows Cloudflare to learn request fields. The boundary-learning threshold allows Cloudflare to learn constraints such as numeric ranges and string lengths.</p>
<p>The first profile appears after the next weekly learning run. This can take up to seven days after meeting the relevant threshold.</p>
<h3 id="review-learned-content">Review learned content</h3>
<p>From the operation overflow menu, select <strong>View details</strong>. The learned schema appears under <strong>Security overview</strong>.</p>
<p>Profiles can learn these request components where supported:</p>
<ul>
<li>Path variables</li>
<li>Query parameters</li>
<li>Headers and cookies</li>
<li>JSON request bodies</li>
<li>Form-encoded request bodies</li>
</ul>
<p>Profiles can validate integers, strings, universally unique identifiers (UUIDs), and arrays. Supported constraints include numeric ranges, string lengths, character classes, and enumerations containing up to three values.</p>
<p>Successful traffic can include bots, scanners, or malicious requests. Review the learned profile before enforcing its detection.</p>
<p>Each weekly run can update a profile as qualifying traffic changes. For a fixed schema, <a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/#export-a-schema">export the learned schema</a> as OpenAPI and <a href="/api-shield/security/schema-validation/#upload-a-schema">upload it for validation</a>.</p>
<h3 id="consider-limitations">Consider limitations</h3>
<p>Learned Schema Profiles have these limitations:</p>
<ul>
<li>Multipart forms, GraphQL, and XML are unsupported.</li>
<li>Repeated parameters have each value validated, without uniqueness enforcement.</li>
<li>Required parameter presence is not enforced.</li>
<li>New parameters alone do not produce violations.</li>
<li>Constraints apply to learned fields, not a complete allowlist.</li>
</ul>
<h2 id="use-an-uploaded-schema">Use an uploaded schema</h2>
<p>An uploaded OpenAPI schema supplies expected structure instead of observed traffic. It produces detections through <code>cf.schema_validation.uploaded.violated</code>.</p>
<p>API Shield provides the detailed <a href="/api-shield/security/schema-validation/">Schema validation reference</a>. It covers supported versions, import procedures, OpenAPI fields, body limits, and troubleshooting.</p>
<p>For automation, refer to the <a href="/api-shield/security/schema-validation/api/">API</a> and <a href="/api-shield/reference/terraform/#manage-schema-validation">Terraform</a> instructions.</p>
