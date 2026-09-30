<p>API Shield protects your APIs by discovering endpoints, validating request schemas, and detecting abuse patterns. This guide walks through the initial setup from configuring session identifiers to enabling advanced protections.</p>
<h2 id="session-identifiers">Session identifiers</h2>
<p>While not strictly required, it is recommended that you configure your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1536.md")
</div> when getting started with API Shield. When Cloudflare inspects your API traffic for individual sessions, we can offer more tools for visibility, management, and control.
<p>If you are unsure of the session identifiers that your API uses, consult with your development team.</p>
<p>Session identifiers should uniquely identify API clients. A common session identifier for API traffic is the <code>Authorization</code> header. When a <a href="/api-shield/security/jwt-validation/">JSON Web Token (JWT)</a> is used by the API for client authentication, its value may change over time. You can use a claim value inside the JWT such as <code>sub</code> or <code>email</code> as a session ID to uniquely identify the session over time.</p>
<p>If your API uses the <code>Authorization</code> header on more than 1% of successful requests to your zone, Cloudflare will automatically set it as the API Shield session identifier.</p>
<p>You must have specific entitlements to configure session identifiers or cookies as a form of identifiers, such as an Enterprise subscription, for features such as <a href="/api-shield/security/api-discovery/">API Discovery</a>, <a href="/api-shield/security/sequence-mitigation/">Sequence Mitigation</a> or <a href="/api-shield/security/volumetric-abuse-detection/">rate limiting recommendations</a>, and to see results in <a href="/api-shield/security/sequence-analytics/">Sequence Analytics</a> and <a href="/api-shield/security/authentication-posture/">Authentication Posture</a>.</p>
<h3 id="to-set-up-session-identifiers">To set up session identifiers</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1537.md")
</div>
<p>After setting up session identifiers and allowing some time for Cloudflare to learn your traffic patterns, you can view your per endpoint and per session rate limiting recommendations, as well as enforce per endpoint and per session rate limits by creating new rules. Session identifiers will allow you to view API Discovery results from session ID-based discovery and session traffic patterns in Sequence Analytics.</p>
<h2 id="create-a-schema-profile">Create a Schema Profile</h2>
<p><a href="/waf/detections/application-profiles/">Application Profiles</a> provides one Schema Profile with two sources. Schema Learning derives a profile from traffic, while Schema Validation uses an uploaded <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1538.md")
</div>.
<p>Both sources provide an <strong>always-on detection</strong> after their profile becomes available. Mitigation requires a separate WAF Custom Rule.</p>
<p>If you maintain an OpenAPI schema, follow the <a href="/api-shield/security/schema-validation/#upload-a-schema">Schema Validation upload procedure</a>. API Shield remains the reference for OpenAPI compatibility, schema governance, and automation.</p>
<h2 id="enable-the-sensitive-data-detection-ruleset-and-accompanying-rules">Enable the Sensitive Data Detection ruleset and accompanying rules</h2>
<p>API Shield works with the Cloudflare <a href="/waf/">WAF</a> <a href="/api-shield/management-and-monitoring/endpoint-management/#sensitive-data-detection">Sensitive Data Detection</a> ruleset to identify <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1539.md")
</div> that return sensitive data, such as social security or credit card numbers, in their HTTP responses. Review these endpoints to verify that sensitive data is only returned where expected.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1534.md")
</aside>
<p>You can identify endpoints returning sensitive data by selecting the icon next to the path in a row. Expand the endpoint to see details on which rules were triggered and view more information by exploring events in <strong>Firewall Events</strong>.</p>
<h2 id="manage-operations">Manage operations</h2>
<p>Web Assets continuously discovers operations from traffic. An operation represents an endpoint by HTTP method, hostname pattern, and path pattern.</p>
<p>You can also add operations manually under <strong>Web Assets</strong> &gt; <strong>Operations</strong>. Discovery and manual creation only add inventory entries.</p>
<p>To start Schema Learning, select <strong>Learn profile</strong> from the operation overflow menu. Review the learned schema through <strong>View details</strong> &gt; <strong>Security overview</strong>.</p>
<p>For the complete workflow and traffic thresholds, refer to <a href="/waf/detections/application-profiles/get-started/">Get started with Application Profiles</a>.</p>
<h2 id="add-rate-limits-to-your-most-sensitive-endpoints">Add rate limits to your most sensitive endpoints</h2>
<p><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> allow you to define rate limits for requests matching an expression, and choose the action to perform when those rate limits are reached.</p>
<p>API Shield generates rate limit recommendations for each endpoint based on your session identifiers. These recommendations are scoped per endpoint and per session rather than applied across your entire site or based on IP address.</p>
<p>Per-session rate limits track traffic from individual visitors during their session to a specific endpoint. This reduces false positives from broadly scoped rules while still limiting abusive traffic.</p>
<h2 id="export-a-learned-schema">Export a learned schema</h2>
<p>Learned schemas include the hostname, all endpoints by host, method, and path, and detected path variables (for example, <code>/users/{id}</code>). They can also include detected query parameters and their format. You can optionally include rate limit threshold recommendations.</p>
<p>You can export your learned schemas in the <a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/#export-a-schema">Cloudflare dashboard</a> or via the <a href="/api/resources/api_gateway/subresources/schemas/methods/list/">API</a>.</p>
<p>Exporting creates an OpenAPI <code>v3.0.0</code> file. To use a fixed profile, upload that file through <a href="/api-shield/security/schema-validation/">Schema Validation</a>.</p>
<h2 id="view-and-configure-sequence-analytics">View and configure Sequence Analytics</h2>
<p><a href="/api-shield/security/sequence-analytics/">Sequence Analytics</a> identifies common patterns of API requests — for example, a user checking their account balance before initiating a funds transfer.</p>
<p>Sequences are ranked by precedence score, which measures how likely specific API requests are to occur together in a consistent order. High-scoring sequences contain API requests that are likely to be preceded by the other operations in the sequence.</p>
<p><a href="/api-shield/security/sequence-mitigation/">Sequence mitigation</a> allows you to enforce request patterns for authenticated clients communicating with your API. Use Sequence Analytics to identify the sequences your API clients follow, then apply API Shield protections (rate limiting, Schema validation, JWT validation, and mTLS) to the endpoints in your high-scoring sequences. Verify the expected endpoint order with your development team.</p>
<p>For more information, refer to <a href="https://blog.cloudflare.com/api-sequence-analytics">Detecting API abuse automatically using sequence analysis</a> blog post.</p>
<h2 id="additional-configuration">Additional configuration</h2>
<h3 id="set-up-json-web-tokens-jwt-validation">Set up JSON Web Tokens (JWT) validation</h3>
<p><a href="/api-shield/security/jwt-validation/">JSON Web Tokens (JWT) validation</a> verifies that tokens sent by clients have not been tampered with and have not expired. Configure JWT validation using the Cloudflare dashboard or API.</p>
<h3 id="set-up-graphql-malicious-query-protection">Set up GraphQL malicious query protection</h3>
<p>If your origin uses GraphQL, you may consider setting limits on GraphQL query size and depth.</p>
<p><a href="/api-shield/security/graphql-protection/api/">GraphQL malicious query protection</a> scans GraphQL traffic for queries with excessive nesting or size that could overload your origin and result in a denial of service. You can create rules that set maximum query depth and size to block these queries before they reach your origin.</p>
<p>For more information, refer to the <a href="https://blog.cloudflare.com/protecting-graphql-apis-from-malicious-queries/">blog post</a>.</p>
<h3 id="mutual-tls-mtls-authentication">Mutual TLS (mTLS) authentication</h3>
<p>If you operate an API that requires or would benefit from an extra layer of protection, you may consider using Mutual TLS (mTLS).</p>
<p><a href="/api-shield/security/mtls/">Mutual TLS (mTLS) authentication</a> requires both the client and server to verify each other's identity using certificates. In standard TLS, only the server proves its identity. mTLS adds client verification, which is useful for devices like IoT hardware that do not authenticate via an identity provider.</p>
