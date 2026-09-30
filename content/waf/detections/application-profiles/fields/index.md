<p>Schema Profile detections populate these fields after an applicable profile becomes available:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Source</th>
<th>Meaning</th>
<th>Available in</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.schema_validation.learned.violated</code></td>
<td><span class="nb-type">Boolean</span></td>
<td>Learned Schema Profile</td>
<td><code>true</code> when an evaluated request violates the learned profile.</td>
<td>Security Analytics and Custom Rules</td>
</tr>
<tr>
<td><code>cf.schema_validation.uploaded.violated</code></td>
<td><span class="nb-type">Boolean</span></td>
<td>Uploaded schema</td>
<td><code>true</code> when an evaluated request violates the supplied schema.</td>
<td>Security Analytics and Custom Rules</td>
</tr>
</tbody>
</table>
<h2 id="violation-details">Violation details</h2>
<p>Sampled violations in Profile Analysis contain four structured fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>location</code></td>
<td><span class="nb-type">String</span></td>
<td>Request component containing the violation: <code>path</code>, <code>query</code>, <code>header</code>, <code>cookie</code>, or <code>body</code>.</td>
</tr>
<tr>
<td><code>error_class</code></td>
<td><span class="nb-type">String</span></td>
<td>Stable, broad category for grouping similar violations.</td>
</tr>
<tr>
<td><code>error_detail</code></td>
<td><span class="nb-type">String</span></td>
<td>Optional specific reason within the error class.</td>
</tr>
<tr>
<td><code>target</code></td>
<td><span class="nb-type">String</span></td>
<td>Optional parameter, header, cookie, or <code>$</code>-prefixed JSON body path associated with the violation.</td>
</tr>
</tbody>
</table>
<p>These values provide context in sampled logs. Schema Validation reports the first detected failure for each request.</p>
<h3 id="error-classes">Error classes</h3>
<p>The <code>error_class</code> field can have the following values:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>missing_required</code></td>
<td>A required parameter, body, or header was absent.</td>
</tr>
<tr>
<td><code>invalid_type</code></td>
<td>A value had the wrong OpenAPI or JSON type.</td>
</tr>
<tr>
<td><code>invalid_encoding</code></td>
<td>Bytes or text did not use the expected encoding.</td>
</tr>
<tr>
<td><code>invalid_syntax</code></td>
<td>Request syntax was invalid, such as malformed JSON.</td>
</tr>
<tr>
<td><code>invalid_media_type</code></td>
<td>A media type did not match the schema.</td>
</tr>
<tr>
<td><code>unsupported_media_type</code></td>
<td>A media type or media type parameter is unsupported.</td>
</tr>
<tr>
<td><code>duplicate_value</code></td>
<td>A value that accepts one entry appeared more than once.</td>
</tr>
<tr>
<td><code>too_many_values</code></td>
<td>A collection contained more values than the validator accepts.</td>
</tr>
<tr>
<td><code>constraint_violation</code></td>
<td>A value violated an OpenAPI or JSON Schema constraint.</td>
</tr>
<tr>
<td><code>body_size</code></td>
<td>The request body could not be validated because of its size or truncation.</td>
</tr>
</tbody>
</table>
<h3 id="error-details">Error details</h3>
<p>The <code>error_detail</code> field adds context when the error class alone is insufficient. The field is empty when the class, location, and target identify the failure.</p>
<details class="nb-details"><summary>Error detail values</summary><div class="nb-details-body">
@input("content/.markup/bodies/15547.md")
</div></details>
<h3 id="targets">Targets</h3>
<p>The <code>target</code> value depends on the violation location:</p>
<table>
<thead>
<tr>
<th>Location</th>
<th>Target</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>path</code>, <code>query</code>, or <code>cookie</code></td>
<td>Parameter name</td>
</tr>
<tr>
<td><code>header</code></td>
<td>Header name, such as <code>content-type</code></td>
</tr>
<tr>
<td><code>body</code></td>
<td><code>$</code>-prefixed JSON path, such as <code>$.items[0].quantity</code></td>
</tr>
</tbody>
</table>
<p>The target is empty for failures that apply to the entire request body. It can also be empty when Cloudflare cannot safely report a target.</p>
<h2 id="availability">Availability</h2>
<p>Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is opening a closed beta to invited Enterprise customers without API Security. Interested customers can contact their account team to express interest. Closed-beta access does not imply future plan availability or pricing.</p>
<h2 id="evaluation">Evaluation</h2>
<p>Cloudflare evaluates requests after the corresponding profile becomes available. The profile must apply to the request operation.</p>
<p>Requests without an applicable profile have <strong>Not evaluated</strong> status.</p>
<p>For request statuses and investigation steps, refer to <a href="/waf/detections/application-profiles/analyze-profile-detections/">Analyze profile detections</a>.</p>
