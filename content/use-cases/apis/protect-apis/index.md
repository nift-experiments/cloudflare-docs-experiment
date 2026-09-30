<p>APIs are exposed to abuse, injection attacks, and unauthorized access. Cloudflare provides defense in depth with API Shield schema validation, per-endpoint rate limiting, mutual TLS (mTLS) client authentication, and security rules.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="api-shield">API Shield</h3>
<p>Discover, secure, and monitor your APIs. <a href="/api-shield/">Learn more about API Shield</a>.</p>
<ul>
<li><strong>Schema validation</strong> - Reject requests that do not conform to your OpenAPI specification before they reach your origin</li>
</ul>
<h3 id="rate-limiting">Rate Limiting</h3>
<p>Limit request rates based on flexible matching criteria. <a href="/waf/rate-limiting-rules/">Learn more about Rate Limiting</a>.</p>
<ul>
<li><strong>Rate limiting</strong> - Prevent abuse and volumetric attacks with per-IP or per-API-key request limits</li>
</ul>
<h3 id="mtls">mTLS</h3>
<p>Mutual TLS client certificate authentication. <a href="/ssl/client-certificates/">Learn more about mTLS</a>.</p>
<ul>
<li><strong>Client authentication</strong> - Require mutual TLS certificates for machine-to-machine communication</li>
</ul>
<h3 id="application-security">Application Security</h3>
<p>Get automatic protection from vulnerabilities and create your own custom rules. <a href="/waf/">Learn more about Application Security</a>.</p>
<ul>
<li><strong>Attack protection</strong> - Application security's managed rulesets block SQL injection, Cross-Site Scripting (XSS), and other injection attacks</li>
</ul>
<h3 id="access">Access</h3>
<p>Zero Trust access control for applications and infrastructure. <a href="/cloudflare-one/access-controls/policies/">Learn more about Access</a>.</p>
<ul>
<li><strong>Identity providers</strong> - Integrate with Okta, Azure AD, Google Workspace, and other identity providers (IdPs) to gate API access</li>
<li><strong>Service tokens</strong> - Issue long-lived credentials for machine-to-machine authentication between services</li>
</ul>
<h3 id="workers">Workers</h3>
<p>Build and deploy serverless applications on Cloudflare's global network. <a href="/workers/">Learn more about Workers</a>.</p>
<ul>
<li><strong>JWT validation</strong> - Verify and decode JSON Web Tokens (JWTs) at the edge before requests reach your backend</li>
<li><strong>Custom auth logic</strong> - Build any authentication scheme — API keys, Hash-based Message Authentication Code (HMAC) signatures, custom headers — directly at the edge</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/api-shield/get-started/">API Shield get started</a></li>
<li><a href="/waf/rate-limiting-rules/">Configure rate limiting rules</a></li>
<li><a href="/ssl/client-certificates/">Set up mTLS authentication</a></li>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/">Configure applications with Cloudflare Access</a></li>
<li><a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Service tokens</a></li>
<li><a href="/workers/get-started/">Workers get started</a></li>
</ol>
