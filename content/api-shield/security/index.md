<p><a href="/waf/detections/application-profiles/">Application Profiles</a> provides the shared profile detection, analytics, and mitigation model. Schema Profile is its only current profile type.</p>
<p><a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema Learning</a> learns a Schema Profile from traffic. <a href="/api-shield/security/schema-validation/">Schema Validation</a> supplies the same profile type through uploaded OpenAPI schemas.</p>
<p>API Shield provides API inventory, schema governance, OpenAPI export, and automation. Cloudflare also offers these API security features:</p>
<table>
<thead>
<tr>
<th>Discovery &amp; management</th>
<th>Posture management</th>
<th>Runtime protection</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api-shield/security/api-discovery/">API Discovery</a></td>
<td><a href="/api-shield/security/volumetric-abuse-detection/">Volumetric Abuse Detection</a></td>
<td><a href="/api-shield/security/schema-validation/">Schema validation</a></td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema learning</a></td>
<td><a href="/api-shield/security/authentication-posture/">Authentication Posture</a></td>
<td><a href="/api-shield/security/jwt-validation/">JWT validation</a></td>
</tr>
<tr>
<td><a href="/api-shield/security/sequence-analytics/">Sequence Analytics</a></td>
<td><a href="/api-shield/security/bola-vulnerability-detection/">BOLA vulnerability detection</a></td>
<td><a href="/api-shield/security/sequence-mitigation/">Sequence mitigation</a></td>
</tr>
<tr>
<td></td>
<td><a href="/api-shield/management-and-monitoring/endpoint-labels/#risk-labels">Risk labels</a></td>
<td><a href="/api-shield/security/mtls/">Mutual TLS (mTLS)</a></td>
</tr>
<tr>
<td></td>
<td><a href="/api-shield/security/vulnerability-scanner/">Vulnerability Scanner</a></td>
<td><a href="/api-shield/security/graphql-protection/">GraphQL query protection</a></td>
</tr>
</tbody>
</table>
<h2 id="example-cloudflare-solutions">Example Cloudflare solutions</h2>
<p>Cloudflare API Shield, together with other Cloudflare products, helps protect your API from the <a href="https://owasp.org/www-project-api-security/">OWASP API Security Top 10</a>. These are the most common API security risks, ranging from unauthorized data access to denial of service.</p>
<p>The following table maps each OWASP vulnerability to the Cloudflare features that address it:</p>
<table>
<thead>
<tr>
<th>OWASP issue</th>
<th>Example Cloudflare solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Broken Object Level Authorization</td>
<td><a href="/api-shield/security/bola-vulnerability-detection/">BOLA vulnerability detection</a>, [Sequence mitigation], [Schema validation], [JWT validation], [Rate Limiting], <a href="/api-shield/security/vulnerability-scanner/">Vulnerability Scanner</a></td>
</tr>
<tr>
<td>Broken Authentication</td>
<td><a href="/api-shield/security/authentication-posture/">Authentication Posture</a>, <a href="/api-shield/security/mtls/">mTLS</a>, [JWT validation], <a href="/waf/managed-rules/check-for-exposed-credentials/">Exposed Credential Checks</a>, <a href="/bots/">Bot Management</a></td>
</tr>
<tr>
<td>Broken Object Property Level Authorization</td>
<td>[Schema validation], [JWT validation]</td>
</tr>
<tr>
<td>Unrestricted Resource Consumption</td>
<td>[Rate Limiting], [Sequence mitigation], [Bot Management], [GraphQL Query Protection]</td>
</tr>
<tr>
<td>Broken Function Level Authorization</td>
<td>[Schema validation], [JWT validation]</td>
</tr>
<tr>
<td>Unrestricted Access to Sensitive Business Flows</td>
<td>[Sequence mitigation], [Bot Management], [GraphQL Query Protection]</td>
</tr>
<tr>
<td>Server Side Request Forgery</td>
<td>[Schema validation], [WAF managed rules], <a href="/waf/custom-rules/">WAF custom rules</a></td>
</tr>
<tr>
<td>Security Misconfiguration</td>
<td>[Sequence mitigation], [Schema validation], [WAF managed rules], [GraphQL Query Protection]</td>
</tr>
<tr>
<td>Improper Inventory Management</td>
<td><a href="/api-shield/security/api-discovery/">Discovery</a>, <a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema learning</a></td>
</tr>
<tr>
<td>Unsafe Consumption of APIs</td>
<td>[JWT validation], [WAF managed rules]</td>
</tr>
</tbody>
</table>
