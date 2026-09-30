<p>Use <strong>Profile Analysis</strong> in <a href="/waf/analytics/security-analytics/">Security Analytics</a> to investigate profile detections.</p>
<h2 id="understand-request-statuses">Understand request statuses</h2>
<p>Profile Analysis classifies requests with these statuses:</p>
<ul>
<li><strong>Conforms:</strong> The evaluated request matched its applicable profile.</li>
<li><strong>Violates:</strong> The evaluated request did not match its applicable profile.</li>
<li><strong>Not evaluated:</strong> No applicable profile is available, or the profile does not apply.</li>
</ul>
<h2 id="understand-violation-details">Understand violation details</h2>
<p>Sampled violations include structured details about the first detected validation failure:</p>
<table>
<thead>
<tr>
<th>Detail</th>
<th>Meaning</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Location</td>
<td>The request component containing the violation.</td>
<td><code>body</code></td>
</tr>
<tr>
<td>Error class</td>
<td>A stable, broad category for grouping similar violations.</td>
<td><code>constraint_violation</code></td>
</tr>
<tr>
<td>Error detail</td>
<td>An optional, specific reason within the error class.</td>
<td><code>number_not_in_range</code></td>
</tr>
<tr>
<td>Target</td>
<td>An optional parameter, header, cookie, or JSON body path associated with the violation.</td>
<td><code>$.items[0].quantity</code></td>
</tr>
</tbody>
</table>
<p>The error detail or target can be empty when the other fields fully describe the violation. For example, a missing request body has the <code>missing_required</code> error class without a target.</p>
<p>For all possible error classes and details, refer to <a href="/waf/detections/application-profiles/fields/#violation-details">Fields</a>.</p>
<h2 id="review-detections">Review detections</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15548.md")
</div>
<h2 id="interpret-violations">Interpret violations</h2>
<p>A non-conforming request is not necessarily malicious. Releases, new clients, and valid edge cases can produce violations.</p>
<p>Cloudflare runs an <strong>always-on detection</strong> after a profile becomes available. Detection does not block requests by itself.</p>
<p>After reviewing representative traffic, refer to <a href="/waf/detections/application-profiles/enforce-profiles-with-custom-rules/">Enforce profiles with Custom Rules</a>.</p>
