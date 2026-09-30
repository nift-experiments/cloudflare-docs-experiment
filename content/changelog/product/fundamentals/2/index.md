<h1 id="changelog">Changelog</h1>

<h2 id="organizations-is-now-in-public-beta-for-enterprises"><a href="/changelog/post/2026-04-06-organizations-public-beta/">Organizations is now in public beta for enterprises</a></h2>
<p><em>2026-04-06</em></p>
<p>We're announcing the public beta of <strong>Organizations</strong> for enterprise customers, a new top-level Cloudflare container that lets Cloudflare customers manage multiple accounts, members, analytics, and shared policies from one centralized location.</p>
<p><strong>What's New</strong></p>
<p><strong>Organizations [BETA]</strong>: <a href="/fundamentals/organizations/">Organizations</a> are a new top-level container for centrally managing multiple accounts. Each Organization supports up to 500 accounts and 5000 zones, giving larger teams a single place to administer resources at scale.</p>
<p><strong>Self-serve onboarding</strong>: Enterprise customers can <a href="/fundamentals/organizations/setup/">create an Organization</a> in the dashboard and assign accounts where they are already Super Administrators.</p>
<p><strong>Centralized Account Management</strong>: At launch, every Organization member has the Organization Super Admin role. Organization Super Admins can invite other users and manage any child account under the Organization implicitly.
<strong>Shared policies</strong>: Share <a href="/waf/custom-rules/">WAF</a> or <a href="/cloudflare-one/traffic-policies/tiered-policies/organizations/">Gateway</a> policies across multiple accounts within your Organization to simplify centralized policy management.
<strong>Implicit access</strong>: Members of an Organization automatically receive Super Administrator permissions across child accounts, removing the need for explicit membership on each account. Additional Org-level roles will be available over the course of the year.</p>
<p><strong>Unified analytics</strong>: View, filter, and download aggregate HTTP analytics across all Organization child accounts from a single dashboard for centralized visibility into traffic patterns and security events.</p>
<p><strong>Terraform provider support</strong>: Manage Organizations with infrastructure as code from day one. Provision organizations, assign accounts, and configure settings programmatically with the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization">Cloudflare Terraform provider</a>.</p>
<p><strong>Shared policies</strong>: Share <a href="/waf/custom-rules/">WAF</a> or <a href="/cloudflare-one/traffic-policies/">Gateway</a> policies across multiple accounts within your Organization to simplify centralized policy management.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17731.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/organizations/">Get started with Organizations</a></li>
<li><a href="/fundamentals/organizations/setup/">Set up your Organization</a></li>
<li><a href="/fundamentals/organizations/limitations/">Review limitations</a></li>
</ul>


<h2 id="service-key-authentication-deprecated"><a href="/changelog/post/2026-03-19-service-key-authentication-deprecated/">Service Key authentication deprecated</a></h2>
<p><em>2026-03-19</em></p>
<p>Service Key authentication for the Cloudflare API is deprecated. Service Keys will stop working on September 30, 2026.</p>
<p><a href="/fundamentals/api/get-started/create-token/">API Tokens</a> replace Service Keys with fine-grained permissions, expiration, and revocation.</p>
<h4 id="2026-03-19-service-key-authentication-deprecated-what-you-need-to-do">What you need to do</h4>
<p>Replace any use of the <code>X-Auth-User-Service-Key</code> header with an <a href="/fundamentals/api/get-started/create-token/">API Token</a> scoped to the permissions your integration requires.</p>
<p>If you use <code>cloudflared</code>, update to a version from November 2022 or later. These versions already use API Tokens.</p>
<p>If you use <a href="https://github.com/cloudflare/origin-ca-issuer">origin-ca-issuer</a>, update to a version that supports API Token authentication.</p>
<p>For more information, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>


<h2 id="scim-provisioning-for-authentik-is-now-generally-available"><a href="/changelog/post/2026-03-17-scim-authentik-support/">SCIM provisioning for Authentik is now Generally Available</a></h2>
<p><em>2026-03-18</em></p>
<p>Cloudflare dashboard SCIM provisioning now supports <a href="https://goauthentik.io/">Authentik</a> as an identity provider, joining Okta and Microsoft Entra ID as explicitly supported providers.</p>
<p>Customers can now sync users and group information from Authentik to Cloudflare, apply Permission Policies to those groups, and manage the lifecycle of users &amp; groups directly from your Authentik Identity Provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17730.md")</aside>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/account/account-security/scim-setup/">SCIM provisioning overview</a></li>
<li><a href="/fundamentals/account/account-security/scim-setup/authentik/">Provision with Authentik</a></li>
</ul>


<h2 id="scim-audit-logging-support"><a href="/changelog/post/2026-03-18-scim-audit-logging/">SCIM audit logging Support</a></h2>
<p><em>2026-03-18</em></p>
<p>Cloudflare dashboard SCIM provisioning operations are now captured in <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2</a>, giving you visibility into user and group changes made by your identity provider.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-03-18-scim-audit-logging.png" alt="SCIM audit logging" /></p>
<p><strong>Logged actions:</strong></p>
<table>
<thead>
<tr>
<th>Action Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Create SCIM User</td>
<td>User provisioned from IdP</td>
</tr>
<tr>
<td>Replace SCIM User</td>
<td>User fully replaced (PUT)</td>
</tr>
<tr>
<td>Update SCIM User</td>
<td>User attributes modified (PATCH)</td>
</tr>
<tr>
<td>Delete SCIM User</td>
<td>Member deprovisioned</td>
</tr>
<tr>
<td>Create SCIM Group</td>
<td>Group provisioned from IdP</td>
</tr>
<tr>
<td>Update SCIM Group</td>
<td>Group membership or attributes modified</td>
</tr>
<tr>
<td>Delete SCIM Group</td>
<td>Group deprovisioned</td>
</tr>
</tbody>
</table>
<p>For more details, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2 documentation</a>.</p>


<h2 id="retry-after-http-header-for-retryable-1xxx-errors"><a href="/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/">Retry-After HTTP header for retryable 1xxx errors</a></h2>
<p><em>2026-03-12</em></p>
<p>Cloudflare-generated 1xxx error responses now include a standard <code>Retry-After</code> HTTP header when the error is retryable. Agents and HTTP clients can read the recommended wait time from response headers alone — no body parsing required.</p>
<h4 id="2026-03-12-retry-after-header-for-1xxx-errors-changes">Changes</h4>
<p>Seven retryable error codes now emit <code>Retry-After</code>:</p>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Retry-After (seconds)</th>
<th>Error name</th>
</tr>
</thead>
<tbody>
<tr>
<td>1004</td>
<td>120</td>
<td>DNS resolution error</td>
</tr>
<tr>
<td>1005</td>
<td>120</td>
<td>Banned zone</td>
</tr>
<tr>
<td>1015</td>
<td>30</td>
<td>Rate limited</td>
</tr>
<tr>
<td>1033</td>
<td>120</td>
<td>Argo Tunnel error</td>
</tr>
<tr>
<td>1038</td>
<td>60</td>
<td>HTTP headers limit exceeded</td>
</tr>
<tr>
<td>1200</td>
<td>60</td>
<td>Cache connection limit</td>
</tr>
<tr>
<td>1205</td>
<td>5</td>
<td>Too many redirects</td>
</tr>
</tbody>
</table>
<p>The header value matches the existing <code>retry_after</code> body field in JSON and Markdown responses.</p>
<p>If a WAF rate limiting rule has already set a dynamic <code>Retry-After</code> value on the response, that value takes precedence.</p>
<h4 id="2026-03-12-retry-after-header-for-1xxx-errors-availability">Availability</h4>
<p>Available for all zones on all plans.</p>
<h4 id="2026-03-12-retry-after-header-for-1xxx-errors-verify">Verify</h4>
<p>Check for the header on any retryable error:</p>
<pre><code class="language-bash">curl -s --compressed -D - -o /dev/null -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | grep -i retry-after&#10;</code></pre>
<p>References:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9110#section-10.2.3">RFC 9110 section 10.2.3 - Retry-After</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></li>
</ul>


<h2 id="json-responses-and-rfc-9457-support-for-cloudflare-1xxx-errors"><a href="/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/">JSON responses and RFC 9457 support for Cloudflare 1xxx errors</a></h2>
<p><em>2026-03-11</em></p>
<p>Cloudflare-generated 1xxx errors now return structured JSON when clients send <code>Accept: application/json</code> or <code>Accept: application/problem+json</code>. JSON responses follow <a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 (Problem Details for HTTP APIs)</a>, so any HTTP client that understands Problem Details can parse the base members without Cloudflare-specific code.</p>
<h4 id="2026-03-11-json-rfc9457-responses-for-1xxx-errors-breaking-change">Breaking change</h4>
<p>The Markdown frontmatter field <code>http_status</code> has been renamed to <code>status</code>. Agents consuming Markdown frontmatter should update parsers accordingly.</p>
<h4 id="2026-03-11-json-rfc9457-responses-for-1xxx-errors-changes">Changes</h4>
<p><strong>JSON format.</strong> Clients sending <code>Accept: application/json</code> or <code>Accept: application/problem+json</code> now receive a structured JSON object with the same operational fields as Markdown frontmatter, plus RFC 9457 standard members.</p>
<p><strong>RFC 9457 standard members (JSON only):</strong></p>
<ul>
<li><code>type</code> — URI pointing to Cloudflare documentation for the specific error code</li>
<li><code>status</code> — HTTP status code (matching the response status)</li>
<li><code>title</code> — short, human-readable summary</li>
<li><code>detail</code> — human-readable explanation specific to this occurrence</li>
<li><code>instance</code> — Ray ID identifying this specific error occurrence</li>
</ul>
<p><strong>Field renames:</strong></p>
<ul>
<li><code>http_status</code> -&gt; <code>status</code> (JSON and Markdown)</li>
<li><code>what_happened</code> -&gt; <code>detail</code> (JSON only — Markdown prose sections are unchanged)</li>
</ul>
<p><strong>Content-Type mirroring.</strong> Clients sending <code>Accept: application/problem+json</code> receive <code>Content-Type: application/problem+json; charset=utf-8</code> back; <code>Accept: application/json</code> receives <code>application/json; charset=utf-8</code>. Same body in both cases.</p>
<h4 id="2026-03-11-json-rfc9457-responses-for-1xxx-errors-negotiation-behavior">Negotiation behavior</h4>
<table>
<thead>
<tr>
<th>Request header sent</th>
<th>Response format</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Accept: application/json</code></td>
<td>JSON (<code>application/json</code> content type)</td>
</tr>
<tr>
<td><code>Accept: application/problem+json</code></td>
<td>JSON (<code>application/problem+json</code> content type)</td>
</tr>
<tr>
<td><code>Accept: application/json, text/markdown;q=0.9</code></td>
<td>JSON</td>
</tr>
<tr>
<td><code>Accept: text/markdown</code></td>
<td>Markdown</td>
</tr>
<tr>
<td><code>Accept: text/markdown, application/json</code></td>
<td>Markdown (equal <code>q</code>, first-listed wins)</td>
</tr>
<tr>
<td><code>Accept: */*</code></td>
<td>HTML (default)</td>
</tr>
</tbody>
</table>
<h4 id="2026-03-11-json-rfc9457-responses-for-1xxx-errors-availability">Availability</h4>
<p>Available now for Cloudflare-generated 1xxx errors.</p>
<h4 id="2026-03-11-json-rfc9457-responses-for-1xxx-errors-get-started">Get started</h4>
<pre><code class="language-bash">curl -s --compressed -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | jq .&#10;</code></pre>
<pre><code class="language-bash">curl -s --compressed -H &quot;Accept: application/problem+json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | jq .&#10;</code></pre>
<p>References:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 — Problem Details for HTTP APIs</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></li>
</ul>


<h2 id="markdown-responses-for-cloudflare-1xxx-errors"><a href="/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/">Markdown responses for Cloudflare 1xxx errors</a></h2>
<p><em>2026-02-26</em></p>
<p>Cloudflare now returns structured Markdown responses for Cloudflare-generated 1xxx errors when clients send <code>Accept: text/markdown</code>.</p>
<p>Each response includes YAML frontmatter plus guidance sections (<code>What happened</code> / <code>What you should do</code>) so agents can make deterministic retry and escalation decisions without parsing HTML.</p>
<p>In measured 1,015 comparisons, Markdown reduced payload size and token footprint by over 98% versus HTML.</p>
<p>Included frontmatter fields:</p>
<ul>
<li><code>error_code</code>, <code>error_name</code>, <code>error_category</code>, <code>http_status</code></li>
<li><code>ray_id</code>, <code>timestamp</code>, <code>zone</code></li>
<li><code>cloudflare_error</code>, <code>retryable</code>, <code>retry_after</code> (when applicable), <code>owner_action_required</code></li>
</ul>
<p>Default behavior is unchanged: clients that do not explicitly request Markdown continue to receive HTML error pages.</p>
<h4 id="2026-02-26-markdown-responses-for-1xxx-errors-negotiation-behavior">Negotiation behavior</h4>
<p>Cloudflare uses standard HTTP content negotiation on the <code>Accept</code> header.</p>
<ul>
<li><code>Accept: text/markdown</code> -&gt; Markdown</li>
<li><code>Accept: text/markdown, text/html;q=0.9</code> -&gt; Markdown</li>
<li><code>Accept: text/*</code> -&gt; Markdown</li>
<li><code>Accept: */*</code> -&gt; HTML (default browser behavior)</li>
</ul>
<p>When multiple values are present, Cloudflare selects the highest-priority supported media type using <code>q</code> values. If Markdown is not explicitly preferred, HTML is returned.</p>
<h4 id="2026-02-26-markdown-responses-for-1xxx-errors-availability">Availability</h4>
<p>Available now for Cloudflare-generated 1xxx errors.</p>
<h4 id="2026-02-26-markdown-responses-for-1xxx-errors-get-started">Get started</h4>
<pre><code class="language-bash">curl -H &quot;Accept: text/markdown&quot; https://&lt;your-domain&gt;/cdn-cgi/error/1015&#10;</code></pre>
<p>Reference: <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></p>


<h2 id="content-encoding-support-for-markdown-for-agents-and-other-improvements"><a href="/changelog/post/2026-02-16-markdown-for-agents-improvements/">Content encoding support for Markdown for Agents and other improvements</a></h2>
<p><em>2026-02-16</em></p>
<p>When AI systems request pages from any website that uses Cloudflare and has <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> enabled, they can express the preference for <code>text/markdown</code> in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.</p>
<p>This release adds the following improvements:</p>
<ul>
<li>The origin response limit was raised from 1 MB to 2 MB (2,097,152 bytes).</li>
<li>We no longer require the origin to send the <code>content-length</code> header.</li>
<li>We now support content encoded responses from the origin.</li>
</ul>
<p>If you haven’t enabled automatic Markdown conversion yet, visit the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ai">AI Crawl Control</a> section of the Cloudflare dashboard and enable <strong>Markdown for Agents</strong>.</p>
<p>Refer to our <a href="/fundamentals/reference/markdown-for-agents/">developer documentation</a> for more details.</p>


<h2 id="fine-grained-permissions-for-access-policies-and-service-tokens"><a href="/changelog/post/2026-02-13-access-policy-service-token-permissions/">Fine-grained permissions for Access policies and service tokens</a></h2>
<p><em>2026-02-13</em></p>
<p>Fine-grained permissions for <strong>Access policies</strong> and <strong>Access service tokens</strong> are available. These new resource-scoped roles expand the existing RBAC model, enabling administrators to grant permissions scoped to individual resources.</p>
<h4 id="2026-02-13-access-policy-service-token-permissions-new-roles">New roles</h4>
<ul>
<li><strong>Cloudflare Access policy admin</strong>: Can edit a specific <a href="/cloudflare-one/access-controls/policies/">Access policy</a> in an account.</li>
<li><strong>Cloudflare Access service token admin</strong>: Can edit a specific <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Access service token</a> in an account.</li>
</ul>
<p>These roles complement the existing resource-scoped roles for Access applications, identity providers, and infrastructure targets.</p>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/manage-members/roles/#resource-scoped-roles">Resource-scoped roles</a></li>
<li><a href="/fundamentals/manage-members/scope/">Role scopes</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17729.md")</aside>


<h2 id="cloudflare-python-sdk-v5-0-0-beta-1-now-available"><a href="/changelog/post/2026-02-13-cloudflare-python-v5.0.0-beta.1/">Cloudflare Python SDK v5.0.0-beta.1 now available</a></h2>
<p><em>2026-02-13</em></p>
<blockquote>
<p><strong>Disclaimer:</strong> Please note that v5.0.0-beta.1 is in Beta and we are still testing it for stability.</p>
</blockquote>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0-beta.1">v4.3.1...v5.0.0-beta.1</a></p>
<p>In this release, you'll see a large number of breaking changes. This is primarily due to a change in OpenAPI definitions,
which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce
our SDK libraries. As the codegen is always evolving and improving, so are our code bases.</p>
<p>There may be changes that are not captured in this changelog. Feel free to open an issue to report any inaccuracies, and we will make sure it gets into the changelog before the v5.0.0 release.</p>
<p>Most of the breaking changes below are caused by improvements to the accuracy of the base OpenAPI schemas, which
sometimes translates to breaking changes in downstream clients that depend on those schemas.</p>
<p>Please ensure you read through the list of changes below and the migration guide before moving to this version - this
will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-breaking-changes">Breaking Changes</h4>
<p><strong>The following resources have breaking changes. See the <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/v5-migration-guide.md">v5 Migration Guide</a> for detailed migration instructions.</strong></p>
<ul>
<li><code>abusereports</code></li>
<li><code>acm.totaltls</code></li>
<li><code>apigateway.configurations</code></li>
<li><code>cloudforceone.threatevents</code></li>
<li><code>d1.database</code></li>
<li><code>intel.indicatorfeeds</code></li>
<li><code>logpush.edge</code></li>
<li><code>origintlsclientauth.hostnames</code></li>
<li><code>queues.consumers</code></li>
<li><code>radar.bgp</code></li>
<li><code>rulesets.rules</code></li>
<li><code>schemavalidation.schemas</code></li>
<li><code>snippets</code></li>
<li><code>zerotrust.dlp</code></li>
<li><code>zerotrust.networks</code></li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-features">Features</h4>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-new-api-resources">New API Resources</h4>
<ul>
<li><code>abusereports</code> - Abuse report management</li>
<li><code>abusereports.mitigations</code> - Abuse report mitigation actions</li>
<li><code>ai.tomarkdown</code> - AI-powered markdown conversion</li>
<li><code>aigateway.dynamicrouting</code> - AI Gateway dynamic routing configuration</li>
<li><code>aigateway.providerconfigs</code> - AI Gateway provider configurations</li>
<li><code>aisearch</code> - AI-powered search functionality</li>
<li><code>aisearch.instances</code> - AI Search instance management</li>
<li><code>aisearch.tokens</code> - AI Search authentication tokens</li>
<li><code>alerting.silences</code> - Alert silence management</li>
<li><code>brandprotection.logomatches</code> - Brand protection logo match detection</li>
<li><code>brandprotection.logos</code> - Brand protection logo management</li>
<li><code>brandprotection.matches</code> - Brand protection match results</li>
<li><code>brandprotection.queries</code> - Brand protection query management</li>
<li><code>cloudforceone.binarystorage</code> - CloudForce One binary storage</li>
<li><code>connectivity.directory</code> - Connectivity directory services</li>
<li><code>d1.database</code> - D1 database management</li>
<li><code>diagnostics.endpointhealthchecks</code> - Endpoint health check diagnostics</li>
<li><code>fraud</code> - Fraud detection and prevention</li>
<li><code>iam.sso</code> - IAM Single Sign-On configuration</li>
<li><code>loadbalancers.monitorgroups</code> - Load balancer monitor groups</li>
<li><code>organizations</code> - Organization management</li>
<li><code>organizations.organizationprofile</code> - Organization profile settings</li>
<li><code>origintlsclientauth.hostnamecertificates</code> - Origin TLS client auth hostname certificates</li>
<li><code>origintlsclientauth.hostnames</code> - Origin TLS client auth hostnames</li>
<li><code>origintlsclientauth.zonecertificates</code> - Origin TLS client auth zone certificates</li>
<li><code>pipelines</code> - Data pipeline management</li>
<li><code>pipelines.sinks</code> - Pipeline sink configurations</li>
<li><code>pipelines.streams</code> - Pipeline stream configurations</li>
<li><code>queues.subscriptions</code> - Queue subscription management</li>
<li><code>r2datacatalog</code> - R2 Data Catalog integration</li>
<li><code>r2datacatalog.credentials</code> - R2 Data Catalog credentials</li>
<li><code>r2datacatalog.maintenanceconfigs</code> - R2 Data Catalog maintenance configurations</li>
<li><code>r2datacatalog.namespaces</code> - R2 Data Catalog namespaces</li>
<li><code>radar.bots</code> - Radar bot analytics</li>
<li><code>radar.ct</code> - Radar certificate transparency data</li>
<li><code>radar.geolocations</code> - Radar geolocation data</li>
<li><code>realtimekit.activesession</code> - Real-time Kit active session management</li>
<li><code>realtimekit.analytics</code> - Real-time Kit analytics</li>
<li><code>realtimekit.apps</code> - Real-time Kit application management</li>
<li><code>realtimekit.livestreams</code> - Real-time Kit live streaming</li>
<li><code>realtimekit.meetings</code> - Real-time Kit meeting management</li>
<li><code>realtimekit.presets</code> - Real-time Kit preset configurations</li>
<li><code>realtimekit.recordings</code> - Real-time Kit recording management</li>
<li><code>realtimekit.sessions</code> - Real-time Kit session management</li>
<li><code>realtimekit.webhooks</code> - Real-time Kit webhook configurations</li>
<li><code>tokenvalidation.configuration</code> - Token validation configuration</li>
<li><code>tokenvalidation.rules</code> - Token validation rules</li>
<li><code>workers.beta</code> - Workers beta features</li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-new-endpoints-existing-resources">New Endpoints (Existing Resources)</h4>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-acm-totaltls"><code>acm.totaltls</code></h4>
- `edit()`
- `update()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-cloudforceone-threatevents"><code>cloudforceone.threatevents</code></h4>
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-contentscanning"><code>contentscanning</code></h4>
- `create()`
- `get()`
- `update()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-dns-records"><code>dns.records</code></h4>
- `scan_list()`
- `scan_review()`
- `scan_trigger()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-intel-indicatorfeeds"><code>intel.indicatorfeeds</code></h4>
- `create()`
- `delete()`
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-leakedcredentialchecks-detections"><code>leakedcredentialchecks.detections</code></h4>
- `get()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-queues-consumers"><code>queues.consumers</code></h4>
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-radar-ai"><code>radar.ai</code></h4>
- `summary()`
- `timeseries()`
- `timeseries_groups()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-radar-bgp"><code>radar.bgp</code></h4>
- `changes()`
- `snapshot()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-workers-subdomains"><code>workers.subdomains</code></h4>
- `delete()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-zerotrust-networks"><code>zerotrust.networks</code></h4>
- `create()`
- `delete()`
- `edit()`
- `get()`
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-general-fixes-and-improvements">General Fixes and Improvements</h4>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-type-system-compatibility">Type System &amp; Compatibility</h4>
<ul>
<li><strong>Type inference improvements</strong>: Allow Pyright to properly infer TypedDict types within SequenceNotStr</li>
<li><strong>Type completeness</strong>: Add missing types to method arguments and response models</li>
<li><strong>Pydantic compatibility</strong>: Ensure compatibility with Pydantic versions prior to 2.8.0 when using additional fields</li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-request-response-handling">Request/Response Handling</h4>
<ul>
<li><strong>Multipart form data</strong>: Correctly handle sending multipart/form-data requests with JSON data</li>
<li><strong>Header handling</strong>: Do not send headers with default values set to omit</li>
<li><strong>GET request headers</strong>: Don't send Content-Type header on GET requests</li>
<li><strong>Response body model accuracy</strong>: Broad improvements to the correctness of models</li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-parsing-data-processing">Parsing &amp; Data Processing</h4>
<ul>
<li><strong>Discriminated unions</strong>: Correctly handle nested discriminated unions in response parsing</li>
<li><strong>Extra field types</strong>: Parse extra field types correctly</li>
<li><strong>Empty metadata</strong>: Ignore empty metadata fields during parsing</li>
<li><strong>Singularization rules</strong>: Update resource name singularization rules for better consistency</li>
</ul>


<h2 id="introducing-markdown-for-agents"><a href="/changelog/post/2026-02-12-markdown-for-agents/">Introducing Markdown for Agents</a></h2>
<p><em>2026-02-12</em></p>
<p>Cloudflare's network now supports real-time content conversion at the source, for enabled zones using <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation">content negotiation</a> headers. When AI systems request pages from any website that uses Cloudflare and has Markdown for Agents enabled, they can express the preference for <code>text/markdown</code> in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.</p>
<p>Here is a curl example with the <code>Accept</code> negotiation header requesting this page from our developer documentation:</p>
<pre><code class="language-bash">curl https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ \&#10;  &#45;H &quot;Accept: text/markdown&quot;&#10;</code></pre>
<p>The response to this request is now formatted in markdown:</p>
<pre><code class="language-http">HTTP/2 200&#10;date: Wed, 11 Feb 2026 11:44:48 GMT&#10;content-type: text/markdown; charset=utf-8&#10;content-length: 2899&#10;vary: accept&#10;x-markdown-tokens: 725&#10;content-signal: ai-train=yes, search=yes, ai-input=yes&#10;&#10;&#45;--&#10;title: Markdown for Agents · Cloudflare Agents docs&#10;&#45;--&#10;&#10;&#35;# What is Markdown for Agents&#10;&#10;Markdown has quickly become the lingua franca for agents and AI systems&#10;as a whole. The format’s explicit structure makes it ideal for AI processing,&#10;ultimately resulting in better results while minimizing token waste.&#10;...&#10;</code></pre>
<p>Refer to our <a href="/fundamentals/reference/markdown-for-agents/">developer documentation</a> and our <a href="https://blog.cloudflare.com/markdown-for-agents/">blog announcement</a> for more details.</p>


<h2 id="terraform-v5-17-0-now-available"><a href="/changelog/post/2026-02-12-terraform-v5.17.0-provider/">Terraform v5.17.0 now available</a></h2>
<p><em>2026-02-12</em></p>
<p>In January 2025, we announced the launch of the new Terraform v5 Provider. We
greatly appreciate the proactive engagement and valuable feedback from the
Cloudflare community following the v5 release. In response, we have established
a consistent and rapid <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> for releasing targeted improvements,
demonstrating our commitment to stability and reliability.</p>
<p>With the help of the community, we have a growing number of resources that we
have marked as <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">stable</a>, with that list continuing to grow with every release.
The most used <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">resources</a> are on track to be stable by the end of March 2026,
when we will also be releasing a new migration tool to help you migrate from v4
to v5 with ease.</p>
<p>This release brings new capabilities for AI Search, enhanced Workers Script
placement controls, and numerous bug fixes based on community feedback. We also
begun laying foundational work for improving the v4 to v5 migration process.
Stay tuned for more details as we approach the March 2026 release timeline.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and
help us build products that reflect your needs.</p>
<h4 id="2026-02-12-terraform-v5.17.0-provider-features">Features</h4>
<ul>
<li><strong>ai_search_instance:</strong> add data source for querying AI Search instances</li>
<li><strong>ai_search_token:</strong> add data source for querying AI Search tokens</li>
<li><strong>account:</strong> add support for tenant unit management with new <code>unit</code> field</li>
<li><strong>account:</strong> add automatic mapping from <code>managed_by.parent_org_id</code> to <code>unit.id</code></li>
<li><strong>authenticated_origin_pulls_certificate:</strong> add data source for querying authenticated origin pull certificates</li>
<li><strong>authenticated_origin_pulls_hostname_certificate:</strong> add data source for querying hostname-specific authenticated origin pull certificates</li>
<li><strong>authenticated_origin_pulls_settings:</strong> add data source for querying authenticated origin pull settings</li>
<li><strong>workers_kv:</strong> add <code>value</code> field to data source to retrieve KV values directly</li>
<li><strong>workers_script:</strong> add <code>script</code> field to data source to retrieve script content</li>
<li><strong>workers_script:</strong> add support for <code>simple</code> rate limit binding</li>
<li><strong>workers_script:</strong> add support for targeted placement mode with <code>placement.target</code> array for specifying placement targets (region, hostname, host)</li>
<li><strong>workers_script:</strong> add <code>placement_mode</code> and <code>placement_status</code> computed fields</li>
<li><strong>zero_trust_dex_test:</strong> add data source with filter support for finding specific tests</li>
<li><strong>zero_trust_dlp_predefined_profile:</strong> add <code>enabled_entries</code> field for flexible entry management</li>
</ul>
<h4 id="2026-02-12-terraform-v5.17.0-provider-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>account:</strong> map <code>managed_by.parent_org_id</code> to <code>unit.id</code> in unmarshall and add acceptance tests</li>
<li><strong>authenticated_origin_pulls_certificate:</strong> add certificate normalization to prevent drift</li>
<li><strong>authenticated_origin_pulls:</strong> handle array response and implement full lifecycle</li>
<li><strong>authenticated_origin_pulls_hostname_certificate:</strong> fix resource and tests</li>
<li><strong>cloudforce_one_request_message:</strong> use correct <code>request_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>dns_zone_transfers_incoming:</strong> use correct <code>zone_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>dns_zone_transfers_outgoing:</strong> use correct <code>zone_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>email_routing_settings:</strong> use correct <code>zone_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>hyperdrive_config:</strong> add proper handling for write-only fields to prevent state drift</li>
<li><strong>hyperdrive_config:</strong> add normalization for empty <code>mtls</code> objects to prevent unnecessary diffs</li>
<li><strong>magic_network_monitoring_rule:</strong> use correct <code>account_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>mtls_certificates:</strong> fix resource and test</li>
<li><strong>pages_project:</strong> revert build_config to computed optional</li>
<li><strong>stream_key:</strong> use correct <code>account_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>total_tls:</strong> use upsert pattern for singleton zone setting</li>
<li><strong>waiting_room_rules:</strong> use correct <code>waiting_room_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>workers_script:</strong> add support for placement mode/status</li>
<li><strong>zero_trust_access_application:</strong> update v4 version on migration tests</li>
<li><strong>zero_trust_device_posture_rule:</strong> update tests to match API</li>
<li><strong>zero_trust_dlp_integration_entry:</strong> use correct <code>entry_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>zero_trust_dlp_predefined_entry:</strong> use correct <code>entry_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>zero_trust_organization:</strong> fix plan issues</li>
</ul>
<h4 id="2026-02-12-terraform-v5.17.0-provider-chores">Chores</h4>
<ul>
<li>add state upgraders to 95+ resources to lay the foundation for replacing Grit
(still under active development)</li>
<li><strong>certificate_pack:</strong> add state migration handler for SDKv2 to Framework conversion</li>
<li><strong>custom_hostname_fallback_origin:</strong> add comprehensive lifecycle test and migration support</li>
<li><strong>dns_record:</strong> add state migration handler for SDKv2 to Framework conversion</li>
<li><strong>leaked_credential_check:</strong> add import functionality and tests</li>
<li><strong>load_balancer_pool:</strong> add state migration handler with detection for v4 vs v5 format</li>
<li><strong>pages_project:</strong> add state migration handlers</li>
<li><strong>tiered_cache:</strong> add state migration handlers</li>
<li><strong>zero_trust_dlp_predefined_profile:</strong> deprecate <code>entries</code> field in favor of <code>enabled_entries</code></li>
</ul>
<h4 id="2026-02-12-terraform-v5.17.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)


<h2 id="added-timezone-preferences-settings"><a href="/changelog/post/2026-01-27-timezone-preferences/">Added Timezone preferences settings</a></h2>
<p><em>2026-01-27</em></p>
<p>You can now set the timezone in the Cloudflare dashboard as Coordinated Universal Time (UTC) or your browser or system's timezone.</p>
<h4 id="2026-01-27-timezone-preferences-what-s-new">What's New</h4>
<p>Unless otherwise specified in the user interface, all dates and times in the Cloudflare dashboard are now displayed in the selected timezone.</p>
<p>You can change the timezone setting from the user profile dropdown.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-01-27-set-timezone.png" alt="Timezone preference dropdown" /></p>
<p>The page will reload to apply the new timezone setting.</p>


<h2 id="new-2fa-experience-for-login"><a href="/changelog/post/2026-01-23-New-2FA-Experience/">New 2FA Experience for Login</a></h2>
<p><em>2026-01-23</em></p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-01-23-2fa-interstitial.png" alt="Screenshot of new 2FA enrollment experience" /></p>
<p>In an effort to improve overall user security, users without 2FA will be prompted upon login to enroll in email 2FA. This will improve user security posture while minimizing friction. Users without email 2FA enabled will see a prompt to secure their account with additional factors upon logging in. Enrolling in 2FA remains optional, but strongly encouraged as it is the best way to prevent account takeovers.</p>
<p>We also made changes to existing 2FA screens to improve the user experience. Now we have distinct experiences for each 2FA factor type, reflective of the way that factor works.</p>
<h4 id="2026-01-23-New-2FA-Experience-for-more-information">For more information</h4>
* [Configure Email Two Factor Authentication](/fundamentals/user-profiles/2fa/#configure-email-two-factor-authentication)


<h2 id="cloudflare-typescript-sdk-v6-0-0-beta-1-now-available"><a href="/changelog/post/2026-01-20-cloudflare-typescript-v6.0.0-beta.1/">Cloudflare Typescript SDK v6.0.0-beta.1 now available</a></h2>
<p><em>2026-01-20</em></p>
<blockquote>
<p><strong>Disclaimer:</strong> Please note that v6.0.0-beta.1 is in Beta and we are still testing it for stability.</p>
</blockquote>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-typescript/compare/v5.2.0...v6.0.0-beta.1">v5.2.0...v6.0.0-beta.1</a></p>
<p>In this release, you'll see a large number of breaking changes. This is primarily due to a change in OpenAPI definitions, which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce our SDK libraries. As the codegen is always evolving and improving, so are our code bases.</p>
<p>Some breaking changes were introduced due to bug fixes, also listed below.</p>
<p>Please ensure you read through the list of changes below before moving to this version - this will help you understand any down or upstream issues it may cause to your environments.</p>
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-breaking-changes">Breaking Changes</h4>
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-addressing-parameter-requirements-changed">Addressing - Parameter Requirements Changed</h4>
- `BGPPrefixCreateParams.cidr`: optional → **required**
- `PrefixCreateParams.asn`: `number | null` → `number`
- `PrefixCreateParams.loa_document_id`: required → **optional**
- `ServiceBindingCreateParams.cidr`: optional → **required**
- `ServiceBindingCreateParams.service_id`: optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-api-gateway">API Gateway</h4>
- `ConfigurationUpdateResponse` removed
- `PublicSchema` → `OldPublicSchema`
- `SchemaUpload` → `UserSchemaCreateResponse`
- `ConfigurationUpdateParams.properties` removed; use `normalize`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-cloudforceone-response-type-changes">CloudforceOne - Response Type Changes</h4>
- `ThreatEventBulkCreateResponse`: `number` → complex object with counts and errors
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-d1-database-query-parameters">D1 Database - Query Parameters</h4>
- `DatabaseQueryParams`: simple interface → union type (`D1SingleQuery | MultipleQueries`)
- `DatabaseRawParams`: same change
- Supports batch queries via `batch` array
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-dns-records-type-renames-21-types">DNS Records - Type Renames (21 types)</h4>
All record type interfaces renamed from `*Record` to short names:
- `RecordResponse.ARecord` → `RecordResponse.A`
- `RecordResponse.AAAARecord` → `RecordResponse.AAAA`
- `RecordResponse.CNAMERecord` → `RecordResponse.CNAME`
- `RecordResponse.MXRecord` → `RecordResponse.MX`
- `RecordResponse.NSRecord` → `RecordResponse.NS`
- `RecordResponse.PTRRecord` → `RecordResponse.PTR`
- `RecordResponse.TXTRecord` → `RecordResponse.TXT`
- `RecordResponse.CAARecord` → `RecordResponse.CAA`
- `RecordResponse.CERTRecord` → `RecordResponse.CERT`
- `RecordResponse.DNSKEYRecord` → `RecordResponse.DNSKEY`
- `RecordResponse.DSRecord` → `RecordResponse.DS`
- `RecordResponse.HTTPSRecord` → `RecordResponse.HTTPS`
- `RecordResponse.LOCRecord` → `RecordResponse.LOC`
- `RecordResponse.NAPTRRecord` → `RecordResponse.NAPTR`
- `RecordResponse.SMIMEARecord` → `RecordResponse.SMIMEA`
- `RecordResponse.SRVRecord` → `RecordResponse.SRV`
- `RecordResponse.SSHFPRecord` → `RecordResponse.SSHFP`
- `RecordResponse.SVCBRecord` → `RecordResponse.SVCB`
- `RecordResponse.TLSARecord` → `RecordResponse.TLSA`
- `RecordResponse.URIRecord` → `RecordResponse.URI`
- `RecordResponse.OpenpgpkeyRecord` → `RecordResponse.Openpgpkey`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-iam-resource-groups">IAM Resource Groups</h4>
- `ResourceGroupCreateResponse.scope`: optional single → **required array**
- `ResourceGroupCreateResponse.id`: optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-origin-ca-certificates-parameter-requirements-changed">Origin CA Certificates - Parameter Requirements Changed</h4>
- `OriginCACertificateCreateParams.csr`: optional → **required**
- `OriginCACertificateCreateParams.hostnames`: optional → **required**
- `OriginCACertificateCreateParams.request_type`: optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pages">Pages</h4>
- Renamed: `DeploymentsSinglePage` → `DeploymentListResponsesV4PagePaginationArray`
- Domain response fields: many optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pipelines-v0-to-v1-migration">Pipelines - v0 to v1 Migration</h4>
- Entire v0 API deprecated; use v1 methods (`createV1`, `listV1`, etc.)
- New sub-resources: `Sinks`, `Streams`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-r2">R2</h4>
- `EventNotificationUpdateParams.rules`: optional → **required**
- Super Slurper: `bucket`, `secret` now required in source params
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-radar">Radar</h4>
- `dataSource`: `string` → typed enum (23 values)
- `eventType`: `string` → typed enum (6 values)
- V2 methods require `dimension` parameter (breaking signature change)
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-resource-sharing">Resource Sharing</h4>
- Removed: `status_message` field from all recipient response types
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-schema-validation">Schema Validation</h4>
- Consolidated `SchemaCreateResponse`, `SchemaListResponse`, `SchemaEditResponse`, `SchemaGetResponse` → `PublicSchema`
- Renamed: `SchemaListResponsesV4PagePaginationArray` → `PublicSchemasV4PagePaginationArray`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-spectrum">Spectrum</h4>
- Renamed union members: `AppListResponse.UnionMember0` → `SpectrumConfigAppConfig`
- Renamed union members: `AppListResponse.UnionMember1` → `SpectrumConfigPaygoAppConfig`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workers">Workers</h4>
- Removed: `WorkersBindingKindTailConsumer` type (all occurrences)
- Renamed: `ScriptsSinglePage` → `ScriptListResponsesSinglePage`
- Removed: `DeploymentsSinglePage`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-dlp">Zero-Trust DLP</h4>
- `datasets.create()`, `update()`, `get()` return types changed
- `PredefinedGetResponse` union members renamed to `UnionMember0-5`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-tunnels">Zero-Trust Tunnels</h4>
- Removed: `CloudflaredCreateResponse`, `CloudflaredListResponse`, `CloudflaredDeleteResponse`, `CloudflaredEditResponse`, `CloudflaredGetResponse`
- Removed: `CloudflaredListResponsesV4PagePaginationArray`
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-features">Features</h4>
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-abuse-reports-client-abusereports">Abuse Reports (<code>client.abuseReports</code>)</h4>
- **Reports**: `create`, `list`, `get`
- **Mitigations**: sub-resource for abuse mitigations
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ai-search-client-aisearch">AI Search (<code>client.aisearch</code>)</h4>
- **Instances**: `create`, `update`, `list`, `delete`, `read`, `stats`
- **Items**: `list`, `get`
- **Jobs**: `create`, `list`, `get`, `logs`
- **Tokens**: `create`, `update`, `list`, `delete`, `read`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-connectivity-client-connectivity">Connectivity (<code>client.connectivity</code>)</h4>
- **Directory Services**: `create`, `update`, `list`, `delete`, `get`
- Supports IPv4, IPv6, dual-stack, and hostname configurations
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-organizations-client-organizations">Organizations (<code>client.organizations</code>)</h4>
- **Organizations**: `create`, `update`, `list`, `delete`, `get`
- **OrganizationProfile**: `update`, `get`
- Hierarchical organization support with parent/child relationships
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-r2-data-catalog-client-r2datacatalog">R2 Data Catalog (<code>client.r2DataCatalog</code>)</h4>
- **Catalog**: `list`, `enable`, `disable`, `get`
- **Credentials**: `create`
- **MaintenanceConfigs**: `update`, `get`
- **Namespaces**: `list`
- **Tables**: `list`, maintenance config management
- Apache Iceberg integration
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-realtime-kit-client-realtimekit">Realtime Kit (<code>client.realtimeKit</code>)</h4>
- **Apps**: `get`, `post`
- **Meetings**: `create`, `get`, participant management
- **Livestreams**: 10+ methods for streaming
- **Recordings**: start, pause, stop, get
- **Sessions**: transcripts, summaries, chat
- **Webhooks**: full CRUD
- **ActiveSession**: polls, kick participants
- **Analytics**: organization analytics
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-token-validation-client-tokenvalidation">Token Validation (<code>client.tokenValidation</code>)</h4>
- **Configuration**: `create`, `list`, `delete`, `edit`, `get`
- **Credentials**: `update`
- **Rules**: `create`, `list`, `delete`, `bulkCreate`, `bulkEdit`, `edit`, `get`
- JWT validation with RS256/384/512, PS256/384/512, ES256, ES384
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-alerting-silences-client-alerting-silences">Alerting Silences (<code>client.alerting.silences</code>)</h4>
- `create`, `update`, `list`, `delete`, `get`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-iam-sso-client-iam-sso">IAM SSO (<code>client.iam.sso</code>)</h4>
- `create`, `update`, `list`, `delete`, `get`, `beginVerification`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pipelines-v1-client-pipelines">Pipelines v1 (<code>client.pipelines</code>)</h4>
- **Sinks**: `create`, `list`, `delete`, `get`
- **Streams**: `create`, `update`, `list`, `delete`, `get`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-ai-controls-mcp-client-zerotrust-access-aicontrols-mcp">Zero-Trust AI Controls / MCP (<code>client.zeroTrust.access.aiControls.mcp</code>)</h4>
- **Portals**: `create`, `update`, `list`, `delete`, `read`
- **Servers**: `create`, `update`, `list`, `delete`, `read`, `sync`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-accounts">Accounts</h4>
- `managed_by` field with `parent_org_id`, `parent_org_name`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-addressing-loa-documents">Addressing LOA Documents</h4>
- `auto_generated` field on `LOADocumentCreateResponse`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-addressing-prefixes">Addressing Prefixes</h4>
- `delegate_loa_creation`, `irr_validation_state`, `ownership_validation_state`, `ownership_validation_token`, `rpki_validation_state`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ai">AI</h4>
- Added `toMarkdown.supported()` method to get all supported conversion formats
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ai-gateway">AI Gateway</h4>
- `zdr` field added to all responses and params
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-alerting">Alerting</h4>
- New alert type: `abuse_report_alert`
- `type` field added to PolicyFilter
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-browser-rendering">Browser Rendering</h4>
- `ContentCreateParams`: refined to discriminated union (`Variant0 | Variant1`)
- Split into URL-based and HTML-based parameter variants for better type safety
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-client-certificates">Client Certificates</h4>
- `reactivate` parameter in edit
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-cloudforceone">CloudforceOne</h4>
- `ThreatEventCreateParams.indicatorType`: required → optional
- `hasChildren` field added to all threat event response types
- `datasetIds` query parameter on `AttackerListParams`, `CategoryListParams`, `TargetIndustryListParams`
- `categoryUuid` field on `TagCreateResponse`
- `indicators` array for multi-indicator support per event
- `uuid` and `preserveUuid` fields for UUID preservation in bulk create
- `format` query parameter (`'json' | 'stix2'`) on `ThreatEventListParams`
- `createdAt`, `datasetId` fields on `ThreatEventEditParams`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-content-scanning">Content Scanning</h4>
- Added `create()`, `update()`, `get()` methods
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-custom-pages">Custom Pages</h4>
- New page types: `basic_challenge`, `under_attack`, `waf_challenge`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-d1">D1</h4>
- `served_by_colo` - colo that handled query
- `jurisdiction` - `'eu' | 'fedramp'`
- **Time Travel** (`client.d1.database.timeTravel`): `getBookmark()`, `restore()` - point-in-time recovery
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-email-security">Email Security</h4>
- New fields on `InvestigateListResponse`/`InvestigateGetResponse`: `envelope_from`, `envelope_to`, `postfix_id_outbound`, `replyto`
- New detection classification: `'outbound_ndr'`
- Enhanced `Finding` interface with `attachment`, `detection`, `field`, `portion`, `reason`, `score`
- Added `cursor` query parameter to `InvestigateListParams`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-gateway-lists">Gateway Lists</h4>
- New list types: `CATEGORY`, `LOCATION`, `DEVICE`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-intel">Intel</h4>
- New issue type: `'configuration_suggestion'`
- `payload` field: `unknown` → typed `Payload` interface with `detection_method`, `zone_tag`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-leaked-credential-checks">Leaked Credential Checks</h4>
- Added `detections.get()` method
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-logpush">Logpush</h4>
- New datasets: `dex_application_tests`, `dex_device_state_events`, `ipsec_logs`, `warp_config_changes`, `warp_toggle_changes`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-load-balancers">Load Balancers</h4>
- `Monitor.port`: `number` → `number | null`
- `Pool.load_shedding`: `LoadShedding` → `LoadShedding | null`
- `Pool.origin_steering`: `OriginSteering` → `OriginSteering | null`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-magic-transit">Magic Transit</h4>
- `license_key` field on connectors
- `provision_license` parameter for auto-provisioning
- IPSec: `custom_remote_identities` with FQDN support
- Snapshots: Bond interface, `probed_mtu` field
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pages-1">Pages</h4>
- New response types: `ProjectCreateResponse`, `ProjectListResponse`, `ProjectEditResponse`, `ProjectGetResponse`
- Deployment methods return specific response types instead of generic `Deployment`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-queues">Queues</h4>
- Added `subscriptions.get()` method
- Enhanced `SubscriptionGetResponse` with typed event source interfaces
- New event source types: Images, KV, R2, Vectorize, Workers AI, Workers Builds, Workflows
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-r2-1">R2</h4>
- Sippy: new provider `s3` (S3-compatible endpoints)
- Sippy: `bucketUrl` field for S3-compatible sources
- Super Slurper: `keys` field on source response schemas (specify specific keys to migrate)
- Super Slurper: `pathPrefix` field on source schemas
- Super Slurper: `region` field on S3 source params
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-radar-1">Radar</h4>
- Added `geolocations.list()`, `geolocations.get()` methods
- Added V2 dimension-based methods (`summaryV2`, `timeseriesGroupsV2`) to radar sub-resources
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-resource-sharing-1">Resource Sharing</h4>
- Added `terminal` boolean field to Resource Error interfaces
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-rules">Rules</h4>
- Added `id` field to `ItemDeleteParams.Item`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-rulesets">Rulesets</h4>
- New buffering fields on `SetConfigRule`: `request_body_buffering`, `response_body_buffering`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-secrets-store">Secrets Store</h4>
- New scopes: `'dex'`, `'access'` (in addition to `'workers'`, `'ai_gateway'`)
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ssl-certificate-packs">SSL Certificate Packs</h4>
- Response types now proper interfaces (was `unknown`)
- Fields now required: `id`, `certificates`, `hosts`, `status`, `type`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-security-center">Security Center</h4>
- `payload` field: `unknown` → typed `Payload` interface with `detection_method`, `zone_tag`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-shared-types">Shared Types</h4>
- Added: `CloudflareTunnelsV4PagePaginationArray` pagination class
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workers-1">Workers</h4>
- Added `subdomains.delete()` method
- `Worker.references` - track external dependencies (domains, Durable Objects, queues)
- `Worker.startup_time_ms` - startup timing
- `Script.observability` - observability settings with logging
- `Script.tag`, `Script.tags` - immutable ID and tags
- Placement: support for region, hostname, host-based placement
- `tags`, `tail_consumers` now accept `| null`
- Telemetry: `traces` field, `$containers` event info, `durableObjectId`, `transactionName`, `abr_level` fields
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workers-for-platforms">Workers for Platforms</h4>
- `ScriptUpdateResponse`: new fields `entry_point`, `observability`, `tag`, `tags`
- `placement` field now union of 4 variants (smart mode, region, hostname, host)
- `tags`, `tail_consumers` now nullable
- `TagUpdateParams.body` now accepts `null`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workflows">Workflows</h4>
- `instance_retention`: `unknown` → typed `InstanceRetention` interface with `error_retention`, `success_retention`
- New status option: `'restart'` added to `StatusEditParams.status`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-devices">Zero-Trust Devices</h4>
- External emergency disconnect settings (4 new fields)
- `antivirus` device posture check type
- `os_version_extra` documentation improvements
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zones">Zones</h4>
- New response types: `SubscriptionCreateResponse`, `SubscriptionUpdateResponse`, `SubscriptionGetResponse`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-access-applications">Zero-Trust Access Applications</h4>
- New `ApplicationType` values: `'mcp'`, `'mcp_portal'`, `'proxy_endpoint'`
- New destination type: `ViaMcpServerPortalDestination` for MCP server access
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-gateway">Zero-Trust Gateway</h4>
- Added `rules.listTenant()` method
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-gateway-proxy-endpoints">Zero-Trust Gateway - Proxy Endpoints</h4>
- `ProxyEndpoint`: interface → discriminated union (`ZeroTrustGatewayProxyEndpointIP | ZeroTrustGatewayProxyEndpointIdentity`)
- `ProxyEndpointCreateParams`: interface → union type
- Added `kind` field: `'ip' | 'identity'`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-tunnels-1">Zero-Trust Tunnels</h4>
- `WARPConnector*Response`: union type → interface
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-deprecations">Deprecations</h4>
<ul>
<li><strong>API Gateway</strong>: <code>UserSchemas</code>, <code>Settings</code>, <code>SchemaValidation</code> resources</li>
<li><strong>Audit Logs</strong>: <code>auditLogId.not</code> (use <code>id.not</code>)</li>
<li><strong>CloudforceOne</strong>: <code>ThreatEvents.get()</code>, <code>IndicatorTypes.list()</code></li>
<li><strong>Devices</strong>: <code>public_ip</code> field (use DEX API)</li>
<li><strong>Email Security</strong>: <code>item_count</code> field in Move responses</li>
<li><strong>Pipelines</strong>: v0 methods (use v1)</li>
<li><strong>Radar</strong>: old <code>summary()</code> and <code>timeseriesGroups()</code> methods (use V2)</li>
<li><strong>Rulesets</strong>: <code>disable_apps</code>, <code>mirage</code> fields</li>
<li><strong>WARP Connector</strong>: <code>connections</code> field</li>
<li><strong>Workers</strong>: <code>environment</code> parameter in Domains</li>
<li><strong>Zones</strong>: <code>ResponseBuffering</code> page rule</li>
</ul>
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>mcp:</strong> correct code tool API endpoint (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/599703c45672dc899455d74b124018efd4b75095">599703c</a>)</li>
<li><strong>mcp:</strong> return correct lines on typescript errors (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/5d6f9998ed9999aaa95e1bda8cf50929f3555cf1">5d6f999</a>)</li>
<li><strong>organization_profile:</strong> fix bad reference (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/d84ea77094400055c06554812b84c2f0c8d00cc4">d84ea77</a>)</li>
<li><strong>schema_validation:</strong> correctly reflect model to openapi mapping (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/bb861516774b159d80e0f46a5f3abc5a4c9f9d49">bb86151</a>)</li>
<li><strong>workers:</strong> fix tests (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/2ee37f7adf5a4637d65f61fc225e135eec2579fc">2ee37f7</a>)</li>
</ul>
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-documentation">Documentation</h4>
<ul>
<li>Added deprecation notices with migration paths</li>
<li><strong>api_gateway:</strong> deprecate API Shield Schema Validation resources (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/8a4b20f7a572422f74179fbdb4f1c4fb555e3e40">8a4b20f</a>)</li>
<li>Improved JSDoc examples across all resources</li>
<li><strong>workers:</strong> expose subdomain delete documentation (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/4f7cc1f2b8861a5b8abc193d287f78264a425062">4f7cc1f</a>)</li>
</ul>


<h2 id="terraform-v5-16-0-now-available"><a href="/changelog/post/2026-01-20-terraform-v5.16.0-provider/">Terraform v5.16.0 now available</a></h2>
<p><em>2026-01-20</em></p>
<p>In January 2025, we announced the launch of the new Terraform v5 Provider. We greatly appreciate the proactive engagement and valuable feedback from the Cloudflare community following the v5 release. In response, we've established a consistent and rapid <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> for releasing targeted improvements, demonstrating our commitment to stability and reliability.</p>
<p>With the help of the community, we have a growing number of resources that we have marked as <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">stable</a>, with that list continuing to grow with every release. The most used <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">resources</a> are on track to be stable by the end of March 2026, when we will also be releasing a new migration tool to you migrate from v4 to v5 with ease.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="2026-01-20-terraform-v5.16.0-provider-features">Features</h4>
<ul>
<li><strong>custom_pages:</strong> add &quot;waf_challenge&quot; as new supported error page type identifier in both resource and data source schemas</li>
<li><strong>list:</strong> enhance CIDR validator to check for normalized CIDR notation requiring network address for IPv4 and IPv6</li>
<li><strong>magic_wan_gre_tunnel:</strong> add automatic_return_routing attribute for automatic routing control</li>
<li><strong>magic_wan_gre_tunnel:</strong> add BGP configuration support with new BGP model attribute</li>
<li><strong>magic_wan_gre_tunnel:</strong> add bgp_status computed attribute for BGP connection status information</li>
<li><strong>magic_wan_gre_tunnel:</strong> enhance schema with BGP-related attributes and validators</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add automatic_return_routing attribute for automatic routing control</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add BGP configuration support with new BGP model attribute</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add bgp_status computed attribute for BGP connection status information</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add custom_remote_identities attribute for custom identity configuration</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> enhance schema with BGP and identity-related attributes</li>
<li><strong>ruleset:</strong> add request body buffering support</li>
<li><strong>ruleset:</strong> enhance ruleset data source with additional configuration options</li>
<li><strong>workers_script:</strong> add observability logs attributes to list data source model</li>
<li><strong>workers_script:</strong> enhance list data source schema with additional configuration options</li>
</ul>
<h4 id="2026-01-20-terraform-v5.16.0-provider-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>account_member</strong>: fix resource importability issues</li>
<li><strong>dns_record:</strong> remove unnecessary fmt.Sprintf wrapper around LoadTestCase call in test configuration helper function</li>
<li><strong>load_balancer:</strong> fix session_affinity_ttl type expectations to match Float64 in initial creation and Int64 after migration</li>
<li><strong>workers_kv:</strong> handle special characters correctly in URL encoding</li>
</ul>
<h4 id="2026-01-20-terraform-v5.16.0-provider-documentation">Documentation</h4>
<ul>
<li><strong>account_subscription:</strong> update schema description for rate_plan.sets attribute to clarify it returns an array of strings</li>
<li><strong>api_shield:</strong> add resource-level description for API Shield management of auth ID characteristics</li>
<li><strong>api_shield:</strong> enhance auth_id_characteristics.name attribute description to include JWT token configuration format requirements</li>
<li><strong>api_shield:</strong> specify JSONPath expression format for JWT claim locations</li>
<li><strong>hyperdrive_config:</strong> add description attribute to name attribute explaining its purpose in dashboard and API identification</li>
<li><strong>hyperdrive_config:</strong> apply description improvements across resource, data source, and list data source schemas</li>
<li><strong>hyperdrive_config:</strong> improve schema descriptions for cache settings to clarify default values</li>
<li><strong>hyperdrive_config:</strong> update port description to clarify defaults for different database types</li>
</ul>
<h4 id="2026-01-20-terraform-v5.16.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)


<h2 id="enhanced-http-3-request-cancellation-visibility"><a href="/changelog/post/2026-01-19-http3-499-reporting-improvement/">Enhanced HTTP/3 request cancellation visibility</a></h2>
<p><em>2026-01-19</em></p>
<h4 id="2026-01-19-http3-499-reporting-improvement-enhanced-http-3-request-cancellation-visibility">Enhanced HTTP/3 request cancellation visibility</h4>
<p>Cloudflare now provides more accurate visibility into HTTP/3 client request cancellations, giving you better insight into real client behavior and reducing unnecessary load on your origins.</p>
<p>Previously, when an HTTP/3 client cancelled a request, the cancellation was not always actioned immediately. This meant requests could continue through the CDN — potentially all the way to your origin — even after the client had abandoned them. In these cases, logs would show the upstream response status (such as <code>200</code> or a timeout-related code) rather than reflecting the client cancellation.</p>
<p>Now, Cloudflare terminates cancelled HTTP/3 requests immediately and accurately logs them with a <code>499</code> status code.</p>
<hr />
<h4 id="2026-01-19-http3-499-reporting-improvement-better-observability-for-client-behavior">Better observability for client behavior</h4>
<p>When HTTP/3 clients cancel requests, Cloudflare now immediately reflects this in your logs with a <code>499</code> status code. This gives you:</p>
<ul>
<li><strong>More accurate traffic analysis</strong>: Understand exactly when and how often clients cancel requests.</li>
<li><strong>Clearer debugging</strong>: Distinguish between true errors and intentional client cancellations.</li>
<li><strong>Better availability metrics</strong>: Separate client-initiated cancellations from server-side issues.</li>
</ul>
<hr />
<h4 id="2026-01-19-http3-499-reporting-improvement-reduced-origin-load">Reduced origin load</h4>
<p>Cloudflare now terminates cancelled requests faster, which means:</p>
<ul>
<li><strong>Less wasted compute</strong>: Your origin no longer processes requests that clients have already abandoned.</li>
<li><strong>Lower bandwidth usage</strong>: Responses are no longer generated and transmitted for cancelled requests.</li>
<li><strong>Improved efficiency</strong>: Resources are freed up to handle active requests.</li>
</ul>
<hr />
<h4 id="2026-01-19-http3-499-reporting-improvement-what-to-expect-in-your-logs">What to expect in your logs</h4>
<p>You may notice an increase in <code>499</code> status codes for HTTP/3 traffic. For HTTP/3, a <code>499</code> indicates the client <a href="https://datatracker.ietf.org/doc/html/rfc9114#section-4.1.1">cancelled the request stream</a> before receiving a complete response — the underlying connection may remain open. This is a normal part of web traffic.</p>
<p><strong>Tip</strong>: If you use <code>499</code> codes in availability calculations, consider whether client-initiated cancellations should be excluded from error rates. These typically represent normal user behavior — such as closing a browser, navigating away from a page, mobile network drops, or cancelling a download — rather than service issues.</p>
<hr />
<p>For more information, refer to <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-499/">Error 499</a>.</p>


<h2 id="terraform-v5-15-0-now-available"><a href="/changelog/post/2025-12-19-terraform-v5.15.0-provider/">Terraform v5.15.0 now available</a></h2>
<p><em>2025-12-19</em></p>
<p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.15 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="2025-12-19-terraform-v5.15.0-provider-features">Features</h4>
<ul>
<li><strong>ai_search:</strong> Add AI Search endpoints (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/6f02adb420e872457f71f95b49cb527663388915">6f02adb</a>)</li>
<li><strong>certificate_pack:</strong> Ensure proper Terraform resource ID handling for path parameters in API calls (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/081f32acab4ce9a194a7ff51c8e9fcabd349895a">081f32a</a>)</li>
<li><strong>worker_version:</strong> Support <code>startup_time_ms</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/286ab55bea8d5be0faa5a2b5b8b157e4a2214eba">286ab55</a>)</li>
<li><strong>zero_trust_dlp_custom_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_integration_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_predefined_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_gateway_policy:</strong> Support <code>forensic_copy</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b">5741fd0</a>)</li>
<li><strong>zero_trust_list:</strong> Support additional types (category, location, device) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b">5741fd0</a>)</li>
</ul>
<h4 id="2025-12-19-terraform-v5.15.0-provider-bug-fixes">Bug fixes</h4>
<ul>
<li><strong>access_rules:</strong> Add validation to prevent state drift. Ideally, we'd use Semantic Equality but since that isn't an option, this will remove a foot-gun. (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/44577911b3cbe45de6279aefa657bdee73c0794d">4457791</a>)</li>
<li><strong>cloudflare_pages_project:</strong> Addressing drift issues (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/6edffcfcf187fdc9b10b624b9a9b90aed2fb2b2e">6edffcf</a>) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/3db318e747423bf10ce587d9149e90edcd8a77b0">3db318e</a>)</li>
<li><strong>cloudflare_worker:</strong> Can be cleanly imported (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/4859b52968bb25570b680df9813f8e07fd50728f">4859b52</a>)</li>
<li><strong>cloudflare_worker:</strong> Ensure clean imports (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5b525bc478a4e2c9c0d4fd659b92cc7f7c18016a">5b525bc</a>)</li>
<li><strong>list_items:</strong> Add validation for IP List items to avoid inconsistent state (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/b6733dc4be909a5ab35895a88e519fc2582ccada">b6733dc</a>)</li>
<li><strong>zero_trust_access_application:</strong> Remove all conditions from sweeper (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/3197f1aed61be326d507d9e9e3b795b9f1d18fd7">3197f1a</a>)</li>
<li><strong>spectrum_application:</strong> Map missing fields during spectrum resource import (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6495">#6495</a>) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/ddb4e722b82c735825a549d651a9da219c142efa">ddb4e72</a>)</li>
</ul>
<h4 id="2025-12-19-terraform-v5.15.0-provider-upgrade-to-newer-version">Upgrade to newer version</h4>
We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="2025-12-19-terraform-v5.15.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)


<h2 id="terraform-v5-14-0-now-available"><a href="/changelog/post/2025-12-05-terraform-v5.14.0-provider/">Terraform v5.14.0 now available</a></h2>
<p><em>2025-12-05</em></p>
<p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.14 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="2025-12-05-terraform-v5.14.0-provider-deprecation-notice">Deprecation notice</h4>
<p>Resource affected: <code>api_shield_discovery_operation</code></p>
<p>Cloudflare continuously discovers and updates API endpoints and web assets of your web applications. To improve the maintainability of these dynamic resources, we are working on reducing the need to actively engage with discovered operations.</p>
<p>The corresponding public API endpoint of <a href="https://developers.cloudflare.com/api/resources/api_gateway/subresources/discovery/subresources/operations/">discovered operations</a> is not affected and will continue to be supported.</p>
<h4 id="2025-12-05-terraform-v5.14.0-provider-features">Features</h4>
<ul>
<li><strong>pages_project</strong>: Add v4 -&gt; v5 migration tests (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/pull/6506">#6506</a>)</li>
</ul>
<h4 id="2025-12-05-terraform-v5.14.0-provider-bug-fixes">Bug fixes</h4>
<ul>
<li><strong>account_members</strong>: Makes member policies a set (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6488">#6488</a>)</li>
<li><strong>pages_project</strong>: Ensures non empty refresh plans (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6515">#6515</a>)</li>
<li><strong>R2</strong>: Improves sweeper (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6512">#6512</a>)</li>
<li><strong>workers_kv</strong>: Ignores value import state for verify (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6521">#6521</a>)</li>
<li><strong>workers_script</strong>: No longer treats the migrations attribute as WriteOnly (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6489">#6489</a>)</li>
<li><strong>workers_script</strong>: Resolves resource drift when worker has unmanaged secret (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6504">#6504</a>)</li>
<li><strong>zero_trust_device_posture_rule</strong>: Preserves input.version and other fields (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6500">#6500</a>) and (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6503">#6503</a>)</li>
<li><strong>zero_trust_dlp_custom_profile</strong>: Adds sweepers for <code>dlp_custom_profile</code></li>
<li><strong>zone_subscription|account_subscription</strong>: Adds <code>partners_ent</code> as valid enum for <code>rate_plan.id</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6505">#6505</a>)</li>
<li><strong>zone</strong>: Ensures datasource model schema parity (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6487">#6487</a>)</li>
<li><strong>subscription</strong>: Updates import signature to accept account_id/subscription_id to import account subscription (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6510">#6510</a>)</li>
</ul>
<h4 id="2025-12-05-terraform-v5.14.0-provider-upgrade-to-newer-version">Upgrade to newer version</h4>
We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="2025-12-05-terraform-v5.14.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)


<h2 id="terraform-v5-13-0-now-available"><a href="/changelog/post/2025-11-20-terraform-v5.13.0-provider/">Terraform v5.13.0 now available</a></h2>
<p><em>2025-11-20</em></p>
<p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.13 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes new features, new resources and data sources, bug fixes, updates to our Developer Documentation, and more.</p>
<h4 id="2025-11-20-terraform-v5.13.0-provider-breaking-change">Breaking Change</h4>
Please be aware that there are breaking changes for the `cloudflare_api_token` and `cloudflare_account_token` resources. These changes eliminate configuration drift caused by policy ordering differences in the Cloudflare API.
<p>For more specific information about the changes or the actions required, please see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.13.0">detailed Repository changelog</a>.</p>
<h4 id="2025-11-20-terraform-v5.13.0-provider-features">Features</h4>
<ul>
<li><strong>New resources and data sources added</strong>
<ul>
<li>cloudflare_connectivity_directory</li>
<li>cloudflare_sso_connector</li>
<li>cloudflare_universal_ssl_setting</li>
</ul>
</li>
<li><strong>api_token+account_tokens:</strong> state upgrader and schema bump (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6472">#6472</a>)</li>
<li><strong>docs:</strong> make docs explicit when a resource does not have import support</li>
<li><strong>magic_transit_connector:</strong> support self-serve license key (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6398">#6398</a>)</li>
<li><strong>worker_version:</strong> add content_base64 support</li>
<li><strong>worker_version:</strong> boolean support for run_worker_first (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6407">#6407</a>)</li>
<li><strong>workers_script_subdomains:</strong> add import support  (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6375">#6375</a>)</li>
<li><strong>zero_trust_access_application:</strong> add proxy_endpoint for ZT Access Application (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6453">#6453</a>)</li>
<li><strong>zero_trust_dlp_predefined_profile:</strong> Switch DLP Predefined Profile endpoints, introduce enabled_entries attribute</li>
</ul>
<h4 id="2025-11-20-terraform-v5.13.0-provider-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>account_token:</strong> token policy order and nested resources (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6440">#6440</a>)</li>
<li>allow r2_bucket_event_notification to be applied twice without failing (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6419">#6419</a>)</li>
<li><strong>cloudflare_worker+cloudflare_worker_version:</strong> import for the resources (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6357">#6357</a>)</li>
<li><strong>dns_record:</strong> inconsistent apply error (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6452">#6452</a>)</li>
<li><strong>pages_domain:</strong> resource tests (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6338">#6338</a>)</li>
<li><strong>pages_project:</strong> unintended resource state drift (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6377">#6377</a>)</li>
<li><strong>queue_consumer:</strong> id population (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6181">#6181</a>)</li>
<li><strong>workers_kv:</strong> multipart request  (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6367">#6367</a>)</li>
<li><strong>workers_kv:</strong> updating workers metadata attribute to be read from endpoint (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6386">#6386</a>)</li>
<li><strong>workers_script_subdomain:</strong> add note to cloudflare_workers_script_subdomain about redundancy with cloudflare_worker (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6383">#6383</a>)</li>
<li><strong>workers_script:</strong> allow config.run_worker_first to accept list input</li>
<li><strong>zero_trust_device_custom_profile_local_domain_fallback:</strong> drift issues (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6365">#6365</a>)</li>
<li><strong>zero_trust_device_custom_profile:</strong> resolve drift issues (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6364">#6364</a>)</li>
<li><strong>zero_trust_dex_test:</strong> correct configurability for 'targeted' attribute to fix drift</li>
<li><strong>zero_trust_tunnel_cloudflared_config:</strong> remove warp_routing from cloudflared_config (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6471">#6471</a>)</li>
</ul>
<h4 id="2025-11-20-terraform-v5.13.0-provider-upgrading">Upgrading</h4>
We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized. We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="2025-11-20-terraform-v5.13.0-provider-for-more-info">For more info</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)


<h2 id="introducing-email-two-factor-authentication"><a href="/changelog/post/2025-10-30-email-2FA/">Introducing email two-factor authentication</a></h2>
<p><em>2025-10-30</em></p>
<p>Two-factor authentication (2FA) is one of the best ways to protect your account from the risk of account takeover. Cloudflare has offered phishing resistant 2FA options including hardware based keys (for example, a Yubikey) and app based TOTP (time-based one-time password) options which use apps like Google or Microsoft's Authenticator app. Unfortunately, while these solutions are very secure, they can be lost if you misplace the hardware based key, or lose the phone which includes that app. The result is that users sometimes get locked out of their accounts and need to contact support.</p>
<p>Today, we are announcing the addition of email as a 2FA factor for all Cloudflare accounts. Email 2FA is in wide use across the industry as a least common denominator for 2FA because it is low friction, loss resistant, and still improves security over username/password login only. We also know that most commercial email providers already require 2FA, so your email address is usually well protected already.</p>
<p>You can now enable email 2FA on the Cloudflare dashboard:</p>
<ol>
<li>Go to <strong>Profile</strong> at the top right corner.</li>
<li>Select <strong>Authentication</strong>.</li>
<li>Under <strong>Two-Factor Authentication</strong>, select <strong>Set up</strong>.</li>
</ol>
<h4 id="2025-10-30-email-2FA-sign-in-security-best-practices">Sign-in security best practices</h4>
<p>Cloudflare is critical infrastructure, and you should protect it as such. Review the following best practices and make sure you are doing your part to secure your account:</p>
<ul>
<li>Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.</li>
<li>Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked.</li>
<li>Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.</li>
<li>If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.</li>
<li>If you use a custom email domain to sign in, <a href="/fundamentals/manage-members/dashboard-sso/">configure SSO</a>.</li>
<li>If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.</li>
<li>If you manage a Cloudflare account for work:
<ul>
<li>Have at least two administrators in case one of them unexpectedly leaves your company.</li>
<li>Use SCIM to automate permissions management for members in your Cloudflare account.</li>
</ul>
</li>
</ul>


<h2 id="revamped-member-management-ui"><a href="/changelog/post/2025-10-30-member-management-improvements/">Revamped Member Management UI</a></h2>
<p><em>2025-10-30</em></p>
<p>As Cloudflare's platform has grown, so has the need for precise, role-based access control. We’ve redesigned the Member Management experience in the Dashboard to help administrators more easily discover, assign, and refine permissions for specific principals.</p>
<h4 id="2025-10-30-member-management-improvements-what-s-new">What's New</h4>
<p><strong>Refreshed member invite flow</strong></p>
<p>We overhauled the Invite Members UI to simplify inviting users and assigning permissions.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-invite-experience.gif" alt="Updated Invite Flow UX" /></p>
<p><strong>Refreshed Members Overview Page</strong></p>
<p>We've updated the Members Overview Page to clearly display:</p>
<ul>
<li>Member 2FA status</li>
<li>Which members hold Super Admin privileges</li>
<li>API access settings per member</li>
<li>Member onboarding state (accepted vs pending invite)</li>
</ul>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-member-management-screen.png" alt="Updated Member Management Overview" /></p>
<p><strong>New Member Permission Policies Details View</strong></p>
<p>We've created a new member details screen that shows all permission policies associated with a member; including policies inherited from group associations to make it easier for members to understand the effective permissions they have.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-permission-policies-screen.gif" alt="Updated Permission Policies Details Screen" /></p>
<p><strong>Improved Member Permission Workflow</strong></p>
<p>We redesigned the permission management experience to make it faster and easier for administrators to review roles and grant access.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-permission-policies-screen.gif" alt="Updated Member Permission Management UX" /></p>
<p><strong>Account-scoped Policies Restrictions Relaxed</strong></p>
<p>Previously, customers could only associate a single account-scoped policy with a member. We've relaxed this restriction, and now Administrators can now assign multiple account-scoped policies to the same member; bringing policy assignment behavior in-line with user-groups and providing greater flexibility in managing member permissions.</p>


<h2 id="increased-http-header-size-limit-to-128-kb"><a href="/changelog/post/2025-10-16-header-limit-increase/">Increased HTTP header size limit to 128 KB</a></h2>
<p><em>2025-10-16</em></p>
<h4 id="2025-10-16-header-limit-increase-cdn-now-supports-128-kb-request-and-response-headers">CDN now supports 128 KB request and response headers 🚀</h4>
<p>We're excited to announce a significant increase in the maximum header size supported by Cloudflare's Content Delivery Network (CDN). Cloudflare now supports up to <strong>128 KB</strong> for both <strong>request and response headers</strong>.</p>
<p>Previously, customers were limited to a total of 32 KB for request or response headers, with a maximum of 16 KB per individual header. Larger headers could cause requests to fail with <code>HTTP 413</code> (Request Header Fields Too Large) errors.</p>
<hr />
<h4 id="2025-10-16-header-limit-increase-what-s-new">What's new?</h4>
<ul>
<li><strong>Support for large headers:</strong> You can now utilize much larger headers, whether as a single large header up to 128 KB or split over multiple headers.</li>
<li><strong>Reduces <code>413</code> and <code>520</code> HTTP errors:</strong> This change drastically reduces the likelihood of customers encountering <code>HTTP 413</code> errors from large request headers or <code>HTTP 520</code> errors caused by oversized response headers, improving the overall reliability of your web applications.</li>
<li><strong>Enhanced functionality:</strong> This is especially beneficial for applications that rely on:
<ul>
<li>A large number of cookies.</li>
<li>Large Content-Security-Policy (CSP) response headers.</li>
<li>Advanced use cases with Cloudflare Workers that generate large response headers.</li>
</ul>
</li>
</ul>
<p>This enhancement improves compatibility with Cloudflare's CDN, enabling more use cases that previously failed due to header size limits.</p>
<hr />
<p>To learn more and get started, refer to the <a href="/fundamentals/reference/connection-limits/#request-limits">Cloudflare Fundamentals documentation</a>.</p>


<h2 id="single-sign-on-now-manageable-in-the-user-experience"><a href="/changelog/post/2025-10-14-sso-self-service-ux/">Single sign-on now manageable in the user experience</a></h2>
<p><em>2025-10-14</em></p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-14-sso-configuration-ux.png" alt="Screenshot of new user experience for managing SSO" /></p>
<p>During Birthday Week, we announced that <a href="https://blog.cloudflare.com/enterprise-grade-features-for-all/">single sign-on (SSO) is available for free</a> to everyone who signs in with a custom email domain and maintains a compatible <a href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/">identity provider</a>. SSO minimizes user friction around login and provides the strongest security posture available. At the time, this could only be configured using the API.</p>
<p>Today, we are launching a new user experience which allows users to manage their SSO configuration from within the Cloudflare dashboard. You can access this by going to <strong>Manage account</strong> &gt; <strong>Members</strong> &gt; <strong>Settings</strong>.</p>
<h4 id="2025-10-14-sso-self-service-ux-for-more-information">For more information</h4>
<ul>
<li><a href="/fundamentals/manage-members/dashboard-sso/">Cloudflare dashboard SSO</a></li>
</ul>


<h2 id="automated-reminders-for-backup-codes"><a href="/changelog/post/2025-10-07-recovery-codes/">Automated reminders for backup codes</a></h2>
<p><em>2025-10-07</em></p>
<p>The most common reason users contact Cloudflare support is lost two-factor authentication (2FA) credentials. Cloudflare supports both app-based and hardware keys for 2FA, but you could lose access to your account if you lose these. Over the past few weeks, we have been rolling out email and in-product reminders that remind you to also download backup codes (sometimes called recovery keys) that can get you back into your account in the event you lose your 2FA credentials. Download your backup codes now by logging into Cloudflare, then navigating to <strong>Profile</strong> &gt; <strong>Security &amp; Authentication</strong> &gt; <strong>Backup codes</strong>.</p>
<h4 id="2025-10-07-recovery-codes-sign-in-security-best-practices">Sign-in security best practices</h4>
<p>Cloudflare is critical infrastructure, and you should protect it as such. Please review the following best practices and make sure you are doing your part to secure your account.</p>
<ul>
<li>Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.</li>
<li>Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked</li>
<li>Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.</li>
<li>If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.</li>
<li>If you use a custom email domain to sign in, <a href="https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/">configure SSO</a>.</li>
<li>If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.</li>
<li>If you manage a Cloudflare account for work:
<ul>
<li>Have at least two administrators in case one of them unexpectedly leaves your company</li>
<li>Use SCIM to automate permissions management for members in your Cloudflare account</li>
</ul>
</li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/fundamentals/">Previous</a><span>Page 2 of 3</span><a class="pagination-next" rel="next" href="/changelog/product/fundamentals/3/">Next</a></nav>
