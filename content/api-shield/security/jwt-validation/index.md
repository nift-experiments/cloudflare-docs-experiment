<div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/3283.md")
</div> are often used as part of an authentication component on many web applications. Since JWTs are crucial to identifying users and their access, ensuring the token's integrity is important.
<p>API Shield's JWT validation cryptographically verifies incoming JWTs before they reach your API origin. It detects tokens that are expired, tampered with, or not yet valid. You then create a rule to act on the validation results.</p>
<h2 id="process">Process</h2>
<p>JWT validation has two parts: a token configuration that tells Cloudflare how to find and verify JWTs, and a rule that acts on the validation results.</p>
<p>After you create a token configuration, Cloudflare checks every request in the zone for a JWT at the configured locations. When Cloudflare finds a JWT, it validates the token and makes the verified claims available in <code>http.request.jwt.claims</code> fields. For available fields and standard claims, refer to the <a href="/ruleset-engine/rules-language/fields/reference/?field-category=JWT+validation">JWT validation fields</a> reference. You do not need a rule or an operation in <a href="/api-shield/management-and-monitoring/">Endpoint Management</a> for validation. Rules determine how Cloudflare acts on the results.</p>
<h3 id="add-a-token-validation-configuration">Add a token validation configuration</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3284.md")
</div>
<p>JWT issuers that use asymmetric algorithms typically publish public keys (JWKS) for verification at a known URL on the Internet. Issuers that use HMAC algorithms share a symmetric credential with the validator. If you do not know where to get your issuer's verification keys or symmetric credential, contact your identity administrator.</p>
<p>For supported algorithms and symmetric key requirements, refer to <a href="/api-shield/security/jwt-validation/api/#credentials">Configure JWT validation via the API</a>.</p>
<p>To automatically keep your JWKS up to date when your identity provider refreshes them, you can use a Worker. Refer to <a href="/api-shield/security/jwt-validation/jwt-worker/">Configure Workers to automatically update keys</a> to learn more about setting up the Worker.</p>
<h3 id="act-on-jwt-validation-results">Act on JWT validation results</h3>
<p>For new security policies, Cloudflare generally recommends using WAF custom rules.</p>
<ul>
<li><strong><a href="/waf/custom-rules/">WAF custom rules</a></strong> — use these for zone-wide policies based on verified JWT claims. Custom rules can combine claims with other signals, such as <a href="/waf/detections/attack-score/">attack score</a>. Endpoints do not need to be in Endpoint Management.</li>
<li><strong>JWT validation rules</strong> — use these when enforcement must apply only to specific operations in <a href="/api-shield/management-and-monitoring/">Endpoint Management</a>. These rules support the <code>is_jwt_valid()</code> and <code>is_jwt_present()</code> functions, which are not available in custom rules.</li>
</ul>
<p>Cloudflare validates JWTs the same way regardless of which rule type you choose.</p>
<p>For example, to reference a simple string claim in a rule expression, use <a href="/ruleset-engine/rules-language/functions/#lookup_json_string"><code>lookup_json_string()</code></a> with your token configuration ID and the claim name:</p>
<pre><code class="language-txt">lookup_json_string(http.request.jwt.claims[&quot;&lt;TOKEN_CONFIGURATION_ID&gt;&quot;][0], &quot;claim_name&quot;)&#10;</code></pre>
<p>For a complete example, refer to <a href="/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/">Issue challenge for admin user in JWT claim based on attack score</a>. For all available fields, refer to the <a href="/ruleset-engine/rules-language/fields/reference/?field-category=JWT+validation">JWT validation fields</a> reference.</p>
<h3 id="add-a-jwt-validation-rule">Add a JWT validation rule</h3>
<p>JWT validation rules use operations from Endpoint Management to control where Cloudflare applies their <code>log</code> or <code>block</code> action.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3285.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3282.md")
</aside>
<hr />
<h2 id="special-cases">Special cases</h2>
<h3 id="validate-two-jwts-with-different-identity-providers-on-a-single-request">Validate two JWTs with different identity providers on a single request</h3>
<p>If you expect that two different JWTs should be present in a request and you want to validate both, you must create two different token configurations. When selecting the two configurations in your validation rule, select <em>Validate all configurations</em> under <strong>Validation behavior for multiple configurations</strong>.</p>
<h3 id="support-a-migration-from-one-identity-provider-to-another">Support a migration from one identity provider to another</h3>
<p>If you expect to migrate between two different identity providers, you must create two different token configurations and two different validation rules, each corresponding to its own configuration. With this setup, you can change the action for different validation rules depending on the state of your migration.</p>
<h3 id="json-web-tokens-with-the-bearer-prefix">JSON Web Tokens with the <code>Bearer</code> prefix</h3>
<p>API Shield will verify JSON Web Tokens regardless of whether they have the <code>Bearer</code> prefix.</p>
<h3 id="rate-limit-by-user-jwt-claim">Rate limit by user (JWT claim)</h3>
<p>You can rate limit requests based on any claim inside of a JSON Web Token (JWT), such as:</p>
<ul>
<li>Registered claims like <code>aud</code> or <code>sub</code></li>
<li>Custom claims like <code>userEmail</code>, including nested custom claims like <code>user.email</code></li>
</ul>
<p>Rate limiting based on JWT claim values will only work on valid JSON Web Tokens. If you do not block invalid JSON Web Tokens on your path, the <a href="/waf/rate-limiting-rules/parameters/#missing-field-versus-empty-value">JWT claims will all be counted and possibly blocked</a> if high traffic is detected in the Point of Presence (PoP).</p>
<p>You must also count the JWT claim that uniquely identifies the user. If you select a claim that is the same for many of your users, their rate limits will all be counted together.</p>
<h3 id="rate-limit-by-user-tier">Rate limit by user tier</h3>
<p>If you offer multiple tiers on your website or application and you want to enforce rate limiting based on the tiers, such as:</p>
<ul>
<li>If <code>&quot;aud&quot;: &quot;free-tier&quot;</code>, rate limit to five requests per minute.</li>
<li>If <code>&quot;aud&quot;: &quot;premium-tier&quot;</code>, rate limit to 50 requests per minute.</li>
</ul>
<p>You can follow the rate limiting rule example below:</p>
<pre><code class="language-txt">(http.request.method eq &quot;GET&quot; and&#10;http.host eq &quot;&lt;YOUR_DOMAIN&gt;&quot; and&#10;http.request.uri.path matches &quot;&lt;/EXAMPLE_PATH&gt;&quot; and&#10;lookup_json_string(http.request.jwt.claims[&quot;&lt;JWT_TOKEN_CONFIGURATION_ID&gt;&quot;][0], &quot;aud&quot;) eq &quot;free-tier&quot;&#10;</code></pre>
<h3 id="ignore-options-pre-flight-cors-requests">Ignore <code>OPTIONS</code> pre-flight CORS requests</h3>
<p>Due to cross-origin resource sharing (CORS) security, web browsers will send &quot;pre-flight&quot; requests using the <code>OPTIONS</code> verb to API endpoints before sending a <code>GET</code> (or other verb) request. By definition, <code>OPTIONS</code> preflight requests do not include credentials (authentication headers or cookies) and are anonymous.</p>
<p>If you expect web browsers to be valid clients of your API, and to prevent blocking <code>OPTIONS</code> requests from those browsers, Cloudflare recommends adding <code>or http.request.method eq &quot;OPTIONS&quot;</code> to your JWT validation rules.</p>
<hr />
<h2 id="availability">Availability</h2>
<p>JWT validation is available for all API Shield customers. Enterprise customers who have not purchased API Shield can preview <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/api-shield">API Shield as a non-contract service</a> in the Cloudflare dashboard or by contacting your account team.</p>
<hr />
<h2 id="limitations">Limitations</h2>
<p>JWT validation only operates on JWTs sent in client request headers or cookies. If your clients send JWTs in a <code>POST</code> body, contact your account team.</p>
