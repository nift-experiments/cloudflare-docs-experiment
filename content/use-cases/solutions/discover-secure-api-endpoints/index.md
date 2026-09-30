<p>Once your API is in production and receiving traffic, you need to decide which endpoints to protect first, what restrictions to apply, and how to monitor for abuse without blocking legitimate clients. This guide walks through that process in five stages: inventory your endpoints, enforce encrypted connections, restrict access to expected traffic patterns, block automated abuse, and monitor the results.</p>
<p>The core workflow uses <a href="/waf/">Cloudflare Application Security</a> (also known as Web Application Firewall or WAF) features, <a href="/ssl/">SSL/TLS</a> settings, and <a href="/bots/">bot detection</a>, all available on Free, Pro, and Business plans. Enterprise callouts cover <a href="/api-shield/">API Shield</a> capabilities for teams that need schema validation, JSON Web Token (JWT) validation, and sequence analysis.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15210.md")
</aside>
<h2 id="know-what-you-are-exposing">Know what you are exposing</h2>
<p>Before configuring any security rules, build an inventory of your API endpoints. Without a complete list, you cannot target protections at the right paths or detect when an unknown endpoint starts receiving traffic.</p>
<h3 id="audit-your-api-surface-manually">Audit your API surface manually</h3>
<ol>
<li>Review your application's routing configuration and list every endpoint with its HTTP method and expected parameters.</li>
</ol>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="ai-assisted-endpoint-discovery">AI-assisted endpoint discovery</h3>
@markup("md", "content/.markup/bodies/15209.md")
</aside>
<ol start="2">
<li>Categorize each endpoint by access level (public, authenticated, internal). Prioritize endpoints that accept file uploads, process payments, or return sensitive data.</li>
</ol>
<table>
<thead>
<tr>
<th>Access level</th>
<th>Description</th>
<th>Example endpoints</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Public</strong></td>
<td>No authentication required</td>
<td><code>/api/status</code>, <code>/api/products</code></td>
</tr>
<tr>
<td><strong>Authenticated</strong></td>
<td>Require a token or session</td>
<td><code>/api/account</code>, <code>/api/orders</code></td>
</tr>
<tr>
<td><strong>Internal</strong></td>
<td>Should not be publicly accessible</td>
<td><code>/api/admin</code>, <code>/api/debug</code></td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Record the inventory in a spreadsheet or OpenAPI schema file for reference when writing rule expressions in later sections. If you already have an OpenAPI specification, you can use it directly with API Shield's schema validation (covered in the Enterprise callout below).</li>
</ol>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="api-shield-endpoint-discovery-enterprise">API Shield Endpoint Discovery (Enterprise)</h3>
@markup("md", "content/.markup/bodies/15208.md")
</aside>
<h2 id="enforce-https-for-all-api-traffic">Enforce HTTPS for all API traffic</h2>
<p>API requests carry credentials, tokens, and response data that attackers can intercept over unencrypted connections. Some API clients silently downgrade to HTTP if the server accepts it, sending sensitive data in plaintext. Enforcing HTTPS at the edge prevents this.</p>
<h3 id="set-your-ssl-tls-encryption-mode">Set your SSL/TLS encryption mode</h3>
<p>Set your encryption mode to <strong>Full (Strict)</strong> to encrypt traffic between visitors and Cloudflare and between Cloudflare and your origin server. This mode requires a valid certificate on your origin.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15211.md")
</div>
<p>For more information on encryption modes and their requirements, refer to <a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS encryption modes</a>.</p>
<h3 id="turn-on-always-use-https">Turn on Always Use HTTPS</h3>
<p><a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a> redirects all HTTP requests to HTTPS for every subdomain and host in your application. This prevents clients from accidentally sending API requests over unencrypted connections.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15207.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15212.md")
</div>
<h3 id="set-minimum-tls-version-to-1-2">Set minimum TLS version to 1.2</h3>
<p>Since APIs can carry sensitive information, like credentials and tokens, you want to select an appropriate minimum TLS version with this in mind.</p>
<p>TLS 1.0 and 1.1 have known vulnerabilities. Setting the minimum to TLS 1.2 rejects connections from clients using older protocols.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15213.md")
</div>
<p>For more information, refer to <a href="/ssl/edge-certificates/additional-options/minimum-tls/">Minimum TLS Version</a>.</p>
<h3 id="disable-automatic-https-rewrites-for-api-only-domains">Disable Automatic HTTPS Rewrites for API-only domains</h3>
<p><a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a> changes HTTP links to HTTPS within HTML responses. For API endpoints that return JSON or other non-HTML content, this rewriting is unnecessary and can cause unexpected behavior if API clients follow rewritten URLs. If your domain serves only API traffic, turn off this setting.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15214.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15206.md")
</aside>
<h2 id="restrict-access-to-your-api-endpoints">Restrict access to your API endpoints</h2>
<p>Legitimate API clients send predictable request patterns: specific HTTP methods, expected headers like <code>Content-Type: application/json</code>, and requests to documented paths. Application Security <a href="/waf/custom-rules/">custom rules</a> let you block traffic that deviates from these patterns. <a href="/waf/rate-limiting-rules/">Rate limiting rules</a> cap request volume per client to prevent abuse.</p>
<h3 id="block-requests-missing-expected-headers">Block requests missing expected headers</h3>
<p>API clients typically include a <code>Content-Type</code> header and may include an <code>Authorization</code> header or a custom API key header. Requests to your API paths that lack these headers are not from your expected clients.</p>
<p>The following custom security rule blocks requests to <code>/api/</code> paths that are missing a <code>Content-Type</code> header. Adjust the path and header checks to match your API.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Security</strong> &gt; <strong>Security rules</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong> &gt; <strong>Custom rules</strong>.</li>
<li>Define the rule name. For example, <code>Block API requests missing Content-Type</code>.</li>
<li>In the expression editor, enter:</li>
</ol>
<pre><code class="language-txt">(starts_with(http.request.uri.path, &quot;/api/&quot;) and not len(http.request.headers[&quot;content-type&quot;][0]) &gt; 0)&#10;</code></pre>
<ol start="5">
<li>For <strong>Choose action</strong>, select <strong>Block</strong>.</li>
<li>Select <strong>Deploy</strong>.</li>
</ol>
<h3 id="restrict-http-methods-per-endpoint">Restrict HTTP methods per endpoint</h3>
<p>If your <code>/api/users</code> endpoint only accepts <code>GET</code> and <code>POST</code> requests, block all other HTTP methods on that path. This prevents attackers from probing with <code>PUT</code>, <code>DELETE</code>, or <code>PATCH</code> requests against endpoints that do not support them.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Security</strong> &gt; <strong>Security rules</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong> &gt; <strong>Custom rules</strong>.</li>
<li>Define the rule name. For example, <code>Block unexpected methods on /api/users</code>.</li>
<li>In the expression editor, enter:</li>
</ol>
<pre><code class="language-txt">(http.request.uri.path eq &quot;/api/users&quot; and http.request.method ne &quot;GET&quot; and http.request.method ne &quot;POST&quot;)&#10;</code></pre>
<p>Adjust the path and allowed methods to match your endpoint.</p>
<ol start="5">
<li>For <strong>Choose action</strong>, select <strong>Block</strong>.</li>
<li>Select <strong>Deploy</strong>.</li>
</ol>
<p>Repeat this pattern for each endpoint with restricted methods. You can combine multiple paths into a single rule using <a href="/ruleset-engine/rules-language/operators/#logical-operators"><code>or</code> operators</a> if they share the same allowed methods.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/15205.md")
</aside>
<h3 id="rate-limit-api-endpoints">Rate limit API endpoints</h3>
<p>API endpoints receive more targeted abuse than web pages because attackers can call them at machine speed without rendering a browser. Rate limiting caps the number of requests a single client can send within a time window.</p>
<p>Create separate rate limiting rules for authenticated and unauthenticated endpoints. Unauthenticated endpoints (login, registration, password reset) need tighter limits because they are primary targets for <a href="/waf/detections/leaked-credentials/">credential stuffing</a> and brute force attacks.</p>
<p>The following example limits requests to <code>/api/auth/login</code> to 10 per minute per IP address. Adjust the path, request threshold, and period for your endpoints.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15215.md")
</div>
<p>For more information on rate limiting parameters and counting characteristics, refer to <a href="/waf/rate-limiting-rules/parameters/">Rate limiting parameters</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15204.md")
</aside>
<p>For an API-specific example using an API key as a counting characteristic, refer to <a href="/waf/rate-limiting-rules/use-cases/#example-2">Rate limiting rule examples</a>.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="schema-validation-and-jwt-validation-enterprise">Schema Validation and JWT Validation (Enterprise)</h3>
@markup("md", "content/.markup/bodies/15203.md")
</aside>
<h2 id="protect-against-automated-api-abuse">Protect against automated API abuse</h2>
<p>Bots call API endpoints at machine speed without browser overhead. Common automated attacks against APIs include credential stuffing against authentication endpoints, data scraping through listing endpoints, and inventory manipulation through cart or checkout endpoints.</p>
<h3 id="turn-on-bot-fight-mode-free">Turn on Bot Fight Mode (Free)</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15202.md")
</aside>
<p>Bot Fight Mode challenges requests that match known bot patterns. It applies to your entire domain and is available on all plans at no additional cost.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15216.md")
</div>
<p>Bot Fight Mode may interfere with legitimate automated traffic to your API, such as monitoring tools, CI/CD pipelines, or partner integrations. If you have legitimate bot clients, create an exception rule before turning on Bot Fight Mode (see the next section).</p>
<p>For more information on Bot Fight Mode behavior and limitations, refer to <a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a>.</p>
<h3 id="create-exception-rules-for-legitimate-bot-clients-pro-business">Create exception rules for legitimate bot clients (Pro, Business)</h3>
<p>If your API receives traffic from known automated clients (monitoring services, partner APIs, CI/CD systems), create a <a href="/waf/custom-rules/skip/">custom security rule with the <em>Skip</em> action</a> to exclude them from bot protections. Create the exception rule before turning on Super Bot Fight Mode in the next section.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Security</strong> &gt; <strong>Security rules</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong> &gt; <strong>Custom rules</strong>.</li>
<li>Define the rule name. For example, <code>Skip bot protections for monitoring service</code>.</li>
<li>Build an expression that matches your known bot traffic. For example, to skip protections for requests from a specific IP range with a known User-Agent:</li>
</ol>
<pre><code class="language-txt">(ip.src in {203.0.113.0/24} and http.user_agent contains &quot;MonitoringBot&quot;)&#10;</code></pre>
<p>Replace the IP range and User-Agent with values that match your legitimate bot clients.</p>
<ol start="5">
<li>For <strong>Choose action</strong>, select <em>Skip</em> and then select <strong>All Super Bot Fight Mode rules</strong>.</li>
<li>Select <strong>Deploy</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15201.md")
</aside>
<h3 id="configure-super-bot-fight-mode-pro-business">Configure Super Bot Fight Mode (Pro, Business)</h3>
<p><a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> provides granular controls that apply across your domain, allowing you to apply different actions to different bot types.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15200.md")
</aside>
<p>To configure Super Bot Fight Mode:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15217.md")
</div>
<p>With Super Bot Fight Mode, you can configure different actions for different bot types:</p>
<ul>
<li>Block or allow verified bots</li>
<li>Configure a separate action (allow, block, or challenge) for <strong>Definitely automated traffic</strong> (<a href="/bots/concepts/bot-score/">bot score</a> of 1)</li>
<li>On Business plans and above: Configure a separate action for <strong>Likely automated traffic</strong> (bot score of 2-29)</li>
</ul>
<p>Super Bot Fight Mode applies domain-wide and does not support path-specific rules. If you need to apply different bot thresholds to different API paths, you need a <a href="/bots/get-started/bot-management/">Bot Management</a> subscription (Enterprise).</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="bot-score-in-custom-rules-enterprise">Bot score in custom rules (Enterprise)</h3>
@markup("md", "content/.markup/bodies/15199.md")
</aside>
<h3 id="detect-leaked-credentials-on-login-endpoints">Detect leaked credentials on login endpoints</h3>
<p>Application Security <a href="/waf/detections/leaked-credentials/">leaked credentials detection</a> checks incoming requests for username and password combinations that appeared in known data breaches. Use this detection to rate limit or challenge requests containing compromised credentials on your authentication endpoints.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15198.md")
</aside>
<p>The following rate limiting rule limits requests that contain a previously leaked username and password combination to 5 per minute per IP:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Expression</td>
<td><code>cf.waf.credential_check.username_and_password_leaked</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Requests per period</td>
<td>5 requests / 1 minute</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>For the full expression including account takeover (ATO) detection IDs, refer to <a href="/waf/detections/leaked-credentials/examples/">Example mitigation rules</a>.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="sequence-analytics-and-sequence-mitigation-custom-rules-enterprise">Sequence Analytics and sequence mitigation custom rules (Enterprise)</h3>
@markup("md", "content/.markup/bodies/15197.md")
</aside>
<h2 id="monitor-your-api-traffic">Monitor your API traffic</h2>
<p>After deploying your security rules, review the results to identify false positives and tune your thresholds. False positives (legitimate clients being blocked) and false negatives (abuse getting through) both require adjustments.</p>
<h3 id="review-security-events-for-api-paths">Review Security Events for API paths</h3>
<p><a href="/waf/analytics/security-events/">Security Events</a> shows every request that your rules matched, including the action taken and the rule that triggered it. Filter by your API path prefix to see what Cloudflare is blocking and why.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15218.md")
</div>
<p>If you find false positives, update your custom rules to exclude the affected traffic. Refer to the <a href="#create-exception-rules-for-legitimate-bot-clients-pro-business">exception rule procedure</a> in an earlier section.</p>
<h3 id="tune-rate-limiting-thresholds">Tune rate limiting thresholds</h3>
<p>Rate limiting thresholds that are too tight block legitimate clients. Thresholds that are too loose allow abuse. Review rate limiting events in <a href="/waf/analytics/security-events/">Security Events</a> to find the right balance.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15219.md")
</div>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="security-analytics-rate-analysis-requires-an-enterprise-plan">Security Analytics rate analysis requires an Enterprise plan</h3>
@markup("md", "content/.markup/bodies/15196.md")
</aside>
<h3 id="set-up-notifications-for-security-event-spikes">Set up notifications for security event spikes</h3>
<p>Cloudflare Notifications can alert you when security event volume exceeds a threshold, indicating a potential attack or a misconfigured rule.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15220.md")
</div>
<p>For the full list of available notification types, refer to <a href="/notifications/notification-available/">Available notifications</a>.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="advanced-security-events-notifications-enterprise">Advanced security events notifications (Enterprise)</h3>
@markup("md", "content/.markup/bodies/15195.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<p><strong>Application Security</strong></p>
<ul>
<li><a href="/waf/custom-rules/">Custom rules</a> — Create rules based on request attributes to block, challenge, or skip specific security features for targeted traffic</li>
<li><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> — Define request rate thresholds per client and choose enforcement actions</li>
<li><a href="/waf/rate-limiting-rules/best-practices/">Rate limiting best practices</a> — Common rate limiting patterns for credential stuffing, API protection, and GraphQL</li>
<li><a href="/waf/rate-limiting-rules/use-cases/">Rate limiting rule examples</a> — Example rules with expressions for login pages, API keys, and complexity-based limiting</li>
<li><a href="/waf/feature-interoperability/">Security features interoperability</a> — How custom rules, rate limiting rules, Super Bot Fight Mode, and Managed Rules interact</li>
<li><a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a> — Detect requests containing credentials from known data breaches</li>
<li><a href="/waf/analytics/security-events/">Security Events</a> — Review matched requests and rule actions</li>
</ul>
<p><strong>Bots</strong></p>
<ul>
<li><a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a> — Automatic challenge for requests matching known bot patterns (Free plan)</li>
<li><a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> — Granular bot controls including verified bot allowlisting (Pro, Business, Enterprise)</li>
<li><a href="/bots/get-started/bot-management/">Bot Management</a> — Bot score, detection IDs, and custom rule templates (Enterprise)</li>
<li><a href="/bots/reference/bot-management-variables/">Bot Management variables</a> — Fields available in rule expressions for bot detection (Enterprise)</li>
</ul>
<p><strong>SSL/TLS</strong></p>
<ul>
<li><a href="/ssl/get-started/">Get started with SSL/TLS</a> — Edge certificates, encryption modes, and HTTPS enforcement</li>
<li><a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a> — Redirect all HTTP requests to HTTPS</li>
<li><a href="/ssl/edge-certificates/additional-options/minimum-tls/">Minimum TLS Version</a> — Reject connections using older TLS protocols</li>
</ul>
<p><strong>API Shield (Enterprise)</strong></p>
<ul>
<li><a href="/api-shield/">API Shield overview</a> — Discovery, schema validation, JWT validation, and sequence analytics for API security</li>
<li><a href="/api-shield/get-started/">Get started with API Shield</a> — Onboarding flow from session identifiers through schema validation</li>
<li><a href="/api-shield/security/api-discovery/">API Discovery</a> — Automatic endpoint discovery from traffic analysis</li>
<li><a href="/api-shield/security/schema-validation/">Schema validation</a> — Validate incoming requests against your OpenAPI schema</li>
<li><a href="/api-shield/security/jwt-validation/">JWT validation</a> — Verify JSON Web Tokens at the edge</li>
<li><a href="/api-shield/security/sequence-analytics/">Sequence Analytics</a> — Track and analyze API request sequences</li>
<li><a href="/api-shield/security/volumetric-abuse-detection/">Volumetric Abuse Detection</a> — Per-session, per-endpoint adaptive rate limiting</li>
<li><a href="/api-shield/security/authentication-posture/">Authentication Posture</a> — helps users identify authentication misconfigurations for APIs and alerts of their presence</li>
<li><a href="/api-shield/security/bola-vulnerability-detection/">BOLA vulnerability detection</a> — Detect endpoints at risk of Broken Object Level Authorization (BOLA) attacks</li>
<li><a href="/api-shield/security/vulnerability-scanner/">Vulnerability Scanner</a> — Test your API endpoints for common vulnerabilities</li>
</ul>
