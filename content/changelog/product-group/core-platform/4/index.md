---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/core-platform/4/
  description: '2026-03-25'
  full_title: Core platform changelog - page 4 | Cloudflare Docs
  head_html: <title>Core platform changelog - page 4 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-03-25"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/core-platform/4/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Core platform changelog - page 4"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-03-25"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/core-platform/4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/core-platform/4/#page","headline":"Core platform changelog - page 4 | Cloudflare Docs","description":"2026-03-25","url":"https://developers.cloudflare.com/changelog/product-group/core-platform/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/core-platform/4/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="new-mtls-certificate-fields-for-transform-rules"><a href="/changelog/post/2026-03-25-rfc9440-mtls-fields/">New mTLS certificate fields for Transform Rules</a></h2>
<p><em>2026-03-25</em></p>
<p>Cloudflare now exposes four new fields in the Transform Rules phase that encode client certificate data in <a href="https://www.rfc-editor.org/rfc/rfc9440">RFC 9440</a> format. Previously, forwarding client certificate information to your origin required custom parsing of PEM-encoded fields or non-standard HTTP header formats. These new fields produce output in the standardized <code>Client-Cert</code> and <code>Client-Cert-Chain</code> header format defined by RFC 9440, so your origin can consume them directly without any additional decoding logic.</p>
<p>Each certificate is DER-encoded, Base64-encoded, and wrapped in colons. For example, <code>:MIIDsT...Vw==:</code>. A chain of intermediates is expressed as a comma-separated list of such values.</p>
<h4 id="2026-03-25-rfc9440-mtls-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
<td>String</td>
<td>The client leaf certificate in RFC 9440 format. Empty if no client certificate was presented.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the leaf certificate exceeded 10 KB and was omitted. In practice this will almost always be <code>false</code>.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
<td>String</td>
<td>The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediate certificates were sent or if the chain exceeded 16 KB.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the intermediate chain exceeded 16 KB and was omitted.</td>
</tr>
</tbody>
</table>
<p>The chain encoding follows the same ordering as the TLS handshake: the certificate closest to the leaf appears first, working up toward the trust anchor. The root certificate is not included.</p>
<h4 id="2026-03-25-rfc9440-mtls-fields-example-forwarding-client-certificate-headers-to-your-origin-server">Example: Forwarding client certificate headers to your origin server</h4>
<p>Add a request header transform rule to set the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> headers on requests forwarded to your origin server. For example, to forward headers for verified, non-revoked certificates:</p>
<p><strong>Rule expression:</strong></p>
<pre tabindex="0"><code class="language-txt">cf.tls_client_auth.cert_verified and not cf.tls_client_auth.cert_revoked&#10;</code></pre>
<p><strong>Header modifications:</strong></p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Header name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set</td>
<td><code>Client-Cert</code></td>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
</tr>
<tr>
<td>Set</td>
<td><code>Client-Cert-Chain</code></td>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
</tr>
</tbody>
</table>
<p>To get the most out of these fields, upload your client CA certificate to Cloudflare so that Cloudflare validates the client certificate at the edge and populates <code>cf.tls_client_auth.cert_verified</code> and <code>cf.tls_client_auth.cert_revoked</code>.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="2026-03-25-rfc9440-mtls-fields-prevent-header-injection">Prevent header injection</h4>
@markup("md", "content/.markup/bodies/17749.md")</aside>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Mutual TLS authentication</a>, <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a>, and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="advanced-waf-customization-for-ai-crawl-control-blocks"><a href="/changelog/post/2026-03-24-waf-rule-preservation/">Advanced WAF customization for AI Crawl Control blocks</a></h2>
<p><em>2026-03-24</em></p>
<p>AI Crawl Control now supports extending the underlying WAF rule with custom modifications. Any changes you make directly in the WAF custom rules editor — such as adding path-based exceptions, extra user agents, or additional expression clauses — are preserved when you update crawler actions in AI Crawl Control.</p>
<p>If the WAF rule expression has been modified in a way AI Crawl Control cannot parse, a warning banner appears on the <strong>Crawlers</strong> page with a link to view the rule directly in WAF.</p>
<p>For more information, refer to <a href="/ai-crawl-control/features/manage-ai-crawlers/#waf-rule-management">WAF rule management</a>.</p>


<h2 id="stream-logs-from-multiple-replicas-of-cloudflare-tunnel-simultaneously"><a href="/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/">Stream logs from multiple replicas of Cloudflare Tunnel simultaneously</a></h2>
<p><em>2026-03-20</em></p>
<p>In the Cloudflare One dashboard, the overview page for a specific Cloudflare Tunnel now shows all <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> of that tunnel and supports streaming logs from multiple replicas at once.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-multiconn.gif" alt="View replicas and stream logs from multiple connectors" /></p>
<p>Previously, you could only stream logs from one replica at a time. With this update:</p>
<ul>
<li><strong>Replicas on the tunnel overview</strong> — All active replicas for the selected tunnel now appear on that tunnel's overview page under <strong>Connectors</strong>. Select any replica to stream its logs.</li>
<li><strong>Multi-connector log streaming</strong> — Stream logs from multiple replicas simultaneously, making it easier to correlate events across your infrastructure during debugging or incident response. To try it out, log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Networks</strong> &gt; <strong>Connectors</strong> &gt; <strong>Cloudflare Tunnels</strong>. Select <strong>View logs</strong> next to the tunnel you want to monitor.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/">Deploy replicas</a>.</p>


<h2 id="service-key-authentication-deprecated"><a href="/changelog/post/2026-03-19-service-key-authentication-deprecated/">Service Key authentication deprecated</a></h2>
<p><em>2026-03-19</em></p>
<p>Service Key authentication for the Cloudflare API is deprecated. Service Keys will stop working on September 30, 2026.</p>
<p><a href="/fundamentals/api/get-started/create-token/">API Tokens</a> replace Service Keys with fine-grained permissions, expiration, and revocation.</p>
<h4 id="2026-03-19-service-key-authentication-deprecated-what-you-need-to-do">What you need to do</h4>
<p>Replace any use of the <code>X-Auth-User-Service-Key</code> header with an <a href="/fundamentals/api/get-started/create-token/">API Token</a> scoped to the permissions your integration requires.</p>
<p>If you use <code>cloudflared</code>, update to a version from November 2022 or later. These versions already use API Tokens.</p>
<p>If you use <a href="https://github.com/cloudflare/origin-ca-issuer">origin-ca-issuer</a>, update to a version that supports API Token authentication.</p>
<p>For more information, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>


<h2 id="manage-cloudflare-tunnels-with-wrangler"><a href="/changelog/post/2026-03-19-wrangler-tunnel-commands/">Manage Cloudflare Tunnels with Wrangler</a></h2>
<p><em>2026-03-19</em></p>
<p>You can now manage <a href="/tunnel/">Cloudflare Tunnels</a> directly from <a href="/workers/wrangler/">Wrangler</a>, the CLI for the Cloudflare Developer Platform. The new <a href="/workers/wrangler/commands/tunnel/"><code>wrangler tunnel</code></a> commands let you create, run, and manage tunnels without leaving your terminal.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/wrangler-tunnel.gif" alt="Wrangler tunnel commands demo" /></p>
<p>Available commands:</p>
<ul>
<li><code>wrangler tunnel create</code> — Create a new remotely managed tunnel.</li>
<li><code>wrangler tunnel list</code> — List all tunnels in your account.</li>
<li><code>wrangler tunnel info</code> — Display details about a specific tunnel.</li>
<li><code>wrangler tunnel delete</code> — Delete a tunnel.</li>
<li><code>wrangler tunnel run</code> — Run a tunnel using the cloudflared daemon.</li>
<li><code>wrangler tunnel quick-start</code> — Start a free, temporary tunnel without an account using <a href="/tunnel/get-started/#quick-tunnels-development">Quick Tunnels</a>.</li>
</ul>
<p>Wrangler handles downloading and managing the <a href="/tunnel/downloads/">cloudflared</a> binary automatically. On first use, you will be prompted to download <code>cloudflared</code> to a local cache directory.</p>
<p>These commands are currently experimental and may change without notice.</p>
<p>To get started, refer to the <a href="/workers/wrangler/commands/tunnel/">Wrangler tunnel commands documentation</a>.</p>


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


<h2 id="worker-execution-timing-field-now-available-in-rules"><a href="/changelog/post/2026-03-18-worker-timing-field/">Worker execution timing field now available in Rules</a></h2>
<p><em>2026-03-18</em></p>
<p>The <code>cf.timings.worker_msec</code> field is now available in the Ruleset Engine. This field reports the wall-clock time that a Cloudflare Worker spent handling a request, measured in milliseconds.</p>
<p>You can use this field to identify slow Worker executions, detect performance regressions, or build rules that respond differently based on Worker processing time, such as logging requests that exceed a latency threshold.</p>
<h4 id="2026-03-18-worker-timing-field-field-details">Field details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.timings.worker_msec</code></td>
<td>Integer</td>
<td>The time spent executing a Cloudflare Worker in milliseconds. Returns <code>0</code> if no Worker was invoked.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre tabindex="0"><code>cf.timings.worker_msec &gt; 500&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/">Fields reference</a>.</p>


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
<pre tabindex="0"><code class="language-bash">curl -s --compressed -D - -o /dev/null -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | grep -i retry-after&#10;</code></pre>
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
<pre tabindex="0"><code class="language-bash">curl -s --compressed -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | jq .&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl -s --compressed -H &quot;Accept: application/problem+json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | jq .&#10;</code></pre>
<p>References:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 — Problem Details for HTTP APIs</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></li>
</ul>


<h2 id="ingest-field-selection-for-log-explorer"><a href="/changelog/post/2026-03-11-ingest-field-selection/">Ingest field selection for Log Explorer</a></h2>
<p><em>2026-03-11</em></p>
<p>Cloudflare Log Explorer now allows you to customize exactly which data fields are ingested and stored when enabling or managing log datasets.</p>
<p>Previously, ingesting logs often meant taking an &quot;all or nothing&quot; approach to data fields. With <strong>Ingest Field Selection</strong>, you can now choose from a list of available and recommended fields for each dataset. This allows you to reduce noise, focus on the metrics that matter most to your security and performance analysis, and manage your data footprint more effectively.</p>
<h4 id="2026-03-11-ingest-field-selection-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Granular control:</strong> Select only the specific fields you need when enabling a new dataset.</li>
<li><strong>Dynamic updates:</strong> Update fields for existing, already enabled logstreams at any time.</li>
<li><strong>Historical consistency:</strong> Even if you disable a field later, you can still query and receive results for that field for the period it was captured.</li>
<li><strong>Data integrity:</strong> Core fields, such as <code>Timestamp</code>, are automatically retained to ensure your logs remain searchable and chronologically accurate.</li>
</ul>
<h4 id="2026-03-11-ingest-field-selection-example-configuration">Example configuration</h4>
<p>When configuring a dataset via the dashboard or API, you can define a specific set of fields. The <code>Timestamp</code> field remains mandatory to ensure data indexability.</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;dataset&quot;: &quot;firewall_events&quot;,&#10;  &quot;enabled&quot;: true,&#10;  &quot;fields&quot;: [&#10;    &quot;Timestamp&quot;,&#10;    &quot;ClientRequestHost&quot;,&#10;    &quot;ClientIP&quot;,&#10;    &quot;Action&quot;,&#10;    &quot;EdgeResponseStatus&quot;,&#10;    &quot;OriginResponseStatus&quot;&#10;  ]&#10;}&#10;</code></pre>
<p>For more information, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>


<h2 id="audit-logs-version-2-general-availability"><a href="/changelog/post/2026-03-10-audit-logs-v2-ga/">Audit logs (version 2) - General Availability</a></h2>
<p><em>2026-03-10</em></p>
<p>Audit Logs v2 is now generally available to all Cloudflare customers.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/auditlogsv2.gif" alt="Audit Logs v2 GA" /></p>
<p>Audit Logs v2 provides a unified and standardized system for tracking and recording all user and system actions across Cloudflare products. Built on Cloudflare's API Shield / OpenAPI gateway, logs are generated automatically without requiring manual instrumentation from individual product teams, ensuring consistency across ~95% of Cloudflare products.</p>
<p><strong>What's available at GA:</strong></p>
<ul>
<li><strong>Standardized logging</strong> — Audit logs follow a consistent format across all Cloudflare products, making it easier to search, filter, and investigate activity.</li>
<li><strong>Expanded product coverage</strong> — ~95% of Cloudflare products covered, up from ~75% in v1.</li>
<li><strong>Granular filtering</strong> — Filter by actor, action type, action result, resource, raw HTTP method, zone, and more. Over 20 filter parameters available via the API.</li>
<li><strong>Enhanced context</strong> — Each log entry includes authentication method, interface (API or dashboard), Cloudflare Ray ID, and actor token details.</li>
<li><strong>18-month retention</strong> — Logs are retained for 18 months. Full history is accessible via the API or Logpush.</li>
</ul>
<p><strong>Access:</strong></p>
<ul>
<li><strong>Dashboard</strong>: Go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>. Audit Logs v2 is shown by default.</li>
<li><strong>API</strong>: <code>GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit</code></li>
<li><strong>Logpush</strong>: Available via the <code>audit_logs_v2</code> account-scoped dataset.</li>
</ul>
<p><strong>Important notes:</strong></p>
<ul>
<li>Approximately 30 days of logs from the Beta period (back to ~February 8, 2026) are available at GA. These Beta logs will expire on ~April 9, 2026. Logs generated after GA will be retained for the full 18 months. Older logs remain available in Audit Logs v1.</li>
<li>The UI query window is limited to 90 days for performance reasons. Use the API or Logpush for access to the full 18-month history.</li>
<li><code>GET</code> requests (view actions) and <code>4xx</code> error responses are not logged at GA. <code>GET</code> logging will be selectively re-enabled for sensitive read operations in a future release.</li>
<li>Audit Logs v1 continues to run in parallel. A deprecation timeline will be communicated separately.</li>
<li>Before and after values — the ability to see what a value changed from and to — is a highly requested feature and is on our roadmap for a post-GA release. In the meantime, we recommend using Audit Logs v1 for before and after values. Audit Logs v1 will continue to run in parallel until this feature is available in v2.</li>
</ul>
<p>For more details, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2 documentation</a>.</p>


<h2 id="new-mcp-portal-logs-dataset-and-new-fields-across-multiple-logpush-datasets-in-cloudflare-logs"><a href="/changelog/post/2026-03-09-log-fields-updated/">New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<p><em>2026-03-09</em></p>
<p>Cloudflare has added new fields across multiple <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-03-09-log-fields-updated-new-dataset">New dataset</h4>
<ul>
<li><strong>MCP Portal Logs</strong>: A new dataset with fields including <code>ClientCountry</code>, <code>ClientIP</code>, <code>ColoCode</code>, <code>Datetime</code>, <code>Error</code>, <code>Method</code>, <code>PortalAUD</code>, <code>PortalID</code>, <code>PromptGetName</code>, <code>ResourceReadURI</code>, <code>ServerAUD</code>, <code>ServerID</code>, <code>ServerResponseDurationMs</code>, <code>ServerURL</code>, <code>SessionID</code>, <code>Success</code>, <code>ToolCallName</code>, <code>UserEmail</code>, and <code>UserID</code>.</li>
</ul>
<h4 id="2026-03-09-log-fields-updated-new-fields-in-existing-datasets">New fields in existing datasets</h4>
<ul>
<li><strong>DEX Application Tests</strong>: <code>HTTPRedirectEndMs</code>, <code>HTTPRedirectStartMs</code>, <code>HTTPResponseBody</code>, and <code>HTTPResponseHeaders</code>.</li>
<li><strong>DEX Device State Events</strong>: <code>ExperimentalExtra</code>.</li>
<li><strong>Firewall Events</strong>: <code>FraudUserID</code>.</li>
<li><strong>Gateway HTTP</strong>: <code>AppControlInfo</code> and <code>ApplicationStatuses</code>.</li>
<li><strong>Gateway DNS</strong>: <code>InternalDNSDurationMs</code>.</li>
<li><strong>HTTP Requests</strong>: <code>FraudEmailRisk</code>, <code>FraudUserID</code>, and <code>PayPerCrawlStatus</code>.</li>
<li><strong>Network Analytics Logs</strong>: <code>DNSQueryName</code>, <code>DNSQueryType</code>, and <code>PFPCustomTag</code>.</li>
<li><strong>WARP Toggle Changes</strong>: <code>UserEmail</code>.</li>
<li><strong>WARP Config Changes</strong>: <code>UserEmail</code>.</li>
<li><strong>Zero Trust Network Session Logs</strong>: <code>SNI</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


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
<pre tabindex="0"><code class="language-bash">curl -H &quot;Accept: text/markdown&quot; https://&lt;your-domain&gt;/cdn-cgi/error/1015&#10;</code></pre>
<p>Reference: <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></p>


<h2 id="manage-cloudflare-tunnel-directly-from-the-main-cloudflare-dashboard"><a href="/changelog/post/2026-02-20-tunnel-core-dashboard/">Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard</a></h2>
<p><em>2026-02-20</em></p>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is now available in the main Cloudflare Dashboard at <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a>, bringing first-class Tunnel management to developers using Tunnel for securing origin servers.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-core-dashboard.gif" alt="Manage Tunnels in the Core Dashboard" /></p>
<p>This new experience provides everything you need to manage Tunnels for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, including:</p>
<ul>
<li><strong>Full Tunnel lifecycle management</strong>: Create, configure, delete, and monitor all your Tunnels in one place.</li>
<li><strong>Native integrations</strong>: View Tunnels by name when configuring <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS records</a> and <a href="/workers-vpc/">Workers VPC</a> — no more copy-pasting UUIDs.</li>
<li><strong>Real-time visibility</strong>: Monitor <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> and Tunnel <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">health status</a> directly in the dashboard.</li>
<li><strong>Routing map</strong>: Manage all ingress routes for your Tunnel, including <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostnames</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">private CIDRs</a>, and <a href="/workers-vpc/">Workers VPC services</a>, from a single interactive interface.</li>
</ul>
<h4 id="2026-02-20-tunnel-core-dashboard-choose-the-right-dashboard-for-your-use-case">Choose the right dashboard for your use case</h4>
<p><strong>Core Dashboard</strong>: Navigate to <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a> to manage Tunnels for:</p>
<ul>
<li>Securing origin servers and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a> with CDN, WAF, Load Balancing, and DDoS protection</li>
<li>Connecting <a href="/workers-vpc/">Workers to private services</a> via Workers VPC</li>
</ul>
<p><strong>Cloudflare One Dashboard</strong>: Navigate to <a href="https://one.dash.cloudflare.com/?to=/:account/networks/connectors">Zero Trust &gt; Networks &gt; Connectors</a> to manage Tunnels for:</p>
<ul>
<li>Securing your public applications with <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Zero Trust access policies</a></li>
<li>Connecting users to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private applications</a></li>
<li>Building a <a href="/reference-architecture/architectures/sase/#connecting-networks">private mesh network</a></li>
</ul>
<p>Both dashboards provide complete Tunnel management capabilities — choose based on your primary workflow.</p>
<h4 id="2026-02-20-tunnel-core-dashboard-get-started">Get started</h4>
<p>New to Tunnel? Learn how to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">get started with Cloudflare Tunnel</a> or explore advanced use cases like <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/">securing SSH servers</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/">running Tunnels in Kubernetes</a>.</p>


<h2 id="new-cfworker-metric-in-server-timing-header"><a href="/changelog/post/2026-02-18-cfworker-server-timing/">New cfWorker metric in Server-Timing header</a></h2>
<p><em>2026-02-18</em></p>
<p>The Server-Timing header now includes a new <code>cfWorker</code> metric that measures time spent executing Cloudflare Workers, including any subrequests performed by the Worker. This helps developers accurately identify whether high Time to First Byte (TTFB) is caused by Worker processing or slow upstream dependencies.</p>
<p>Previously, Worker execution time was included in the <code>edge</code> metric, making it harder to identify true edge performance. The new <code>cfWorker</code> metric provides this visibility:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>edge</code></td>
<td>Total time spent on the Cloudflare edge, including Worker execution</td>
</tr>
<tr>
<td><code>origin</code></td>
<td>Time spent fetching from the origin server</td>
</tr>
<tr>
<td><code>cfWorker</code></td>
<td>Time spent in Worker execution, including subrequests but excluding origin fetch time</td>
</tr>
</tbody>
</table>
<h4 id="2026-02-18-cfworker-server-timing-example-response">Example response</h4>
<pre tabindex="0"><code class="language-txt">Server-Timing: cdn-cache; desc=DYNAMIC, edge; dur=20, origin; dur=100, cfWorker; dur=7&#10;</code></pre>
<p>In this example, the edge took 20ms, the origin took 100ms, and the Worker added just 7ms of processing time.</p>
<h4 id="2026-02-18-cfworker-server-timing-availability">Availability</h4>
<p>The <code>cfWorker</code> metric is enabled by default if you have <a href="/web-analytics/">Real User Monitoring (RUM)</a> enabled. Otherwise, you can enable it using <a href="/rules/">Rules</a>.</p>
<p>This metric is particularly useful for:</p>
<ul>
<li><strong>Performance debugging</strong>: Quickly determine if latency is caused by Worker code, external API calls within Workers, or slow origins.</li>
<li><strong>Optimization targeting</strong>: Identify which component of your request path needs optimization.</li>
<li><strong>Real User Monitoring (RUM)</strong>: Access detailed timing breakdowns directly from response headers for client-side analytics.</li>
</ul>
<p>For more information about Server-Timing headers, refer to the <a href="https://www.w3.org/TR/server-timing/">W3C Server Timing specification</a>.</p>


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
<pre tabindex="0"><code class="language-bash">curl https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ \&#10;  &#45;H &quot;Accept: text/markdown&quot;&#10;</code></pre>
<p>The response to this request is now formatted in markdown:</p>
<pre tabindex="0"><code class="language-http">HTTP/2 200&#10;date: Wed, 11 Feb 2026 11:44:48 GMT&#10;content-type: text/markdown; charset=utf-8&#10;content-length: 2899&#10;vary: accept&#10;x-markdown-tokens: 725&#10;content-signal: ai-train=yes, search=yes, ai-input=yes&#10;&#10;&#45;--&#10;title: Markdown for Agents · Cloudflare Agents docs&#10;&#45;--&#10;&#10;&#35;# What is Markdown for Agents&#10;&#10;Markdown has quickly become the lingua franca for agents and AI systems&#10;as a whole. The format’s explicit structure makes it ideal for AI processing,&#10;ultimately resulting in better results while minimizing token waste.&#10;...&#10;</code></pre>
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


<h2 id="analytics-enhancements"><a href="/changelog/post/2026-02-09-analytics-enhancements/">Analytics enhancements</a></h2>
<p><em>2026-02-09</em></p>
<p>AI Crawl Control metrics have been enhanced with new views, improved filtering, and better data visualization.</p>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-path-patterns.png" alt="AI Crawl Control path patterns" /></p>
<p><strong>Path pattern grouping</strong></p>
<ul>
<li>In the <strong>Metrics</strong> tab &gt; <strong>Most popular paths</strong> table, use the new <strong>Patterns</strong> tab that groups requests by URI pattern (<code>/blog/*</code>, <code>/api/v1/*</code>, <code>/docs/*</code>) to identify which site areas crawlers target most. Refer to the screenshot above.</li>
</ul>
<p><strong>Enhanced referral analytics</strong></p>
<ul>
<li>Destination patterns show which site areas receive AI-driven referral traffic.</li>
<li>In the <strong>Metrics</strong> tab, a new <strong>Referrals over time</strong> chart shows trends by operator or source.</li>
</ul>
<p><strong>Data transfer metrics</strong></p>
<ul>
<li>In the <strong>Metrics</strong> tab &gt; <strong>Allowed requests over time</strong> chart, toggle <strong>Bytes</strong> to show bandwidth consumption.</li>
<li>In the <strong>Crawlers</strong> tab, a new <strong>Bytes Transferred</strong> column shows bandwidth per crawler.</li>
</ul>
<p><strong>Image exports</strong></p>
<ul>
<li>Export charts and tables as images for reports and presentations.</li>
</ul>
<p>Learn more about <a href="/ai-crawl-control/features/analyze-ai-traffic/">analyzing AI traffic</a>.</p>


<h2 id="tabs-and-pivots"><a href="/changelog/post/2026-02-09-tabs-and-pivots/">Tabs and pivots</a></h2>
<p><em>2026-02-09</em></p>
<p>Log Explorer now supports multiple concurrent queries with the new Tabs feature. Work with multiple queries simultaneously and pivot between datasets to investigate malicious activity more effectively.</p>
<h4 id="2026-02-09-tabs-and-pivots-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Multiple tabs:</strong> Open and switch between multiple query tabs to compare results across different datasets.</li>
<li><strong>Quick filtering:</strong> Select the filter button from query results to add a value as a filter to your current query.</li>
<li><strong>Pivot to new tab:</strong> Use Cmd + click on the filter button to start a new query tab with that filter applied.</li>
<li><strong>Preserved progress:</strong> Your query progress is preserved on each tab if you navigate away and return.</li>
</ul>
<p>For more information, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>


<h2 id="new-reference-documentation"><a href="/changelog/post/2026-02-09-reference-documentation/">New reference documentation</a></h2>
<p><em>2026-02-04</em></p>
<p>New reference documentation is now available for AI Crawl Control:</p>
<ul>
<li><strong><a href="/ai-crawl-control/reference/graphql-api/">GraphQL API reference</a></strong> — Query examples for crawler requests, top paths, referral traffic, and data transfer. Includes key filters for detection IDs, user agents, and referrer domains.</li>
<li><strong><a href="/ai-crawl-control/reference/bots/">Bot reference</a></strong> — Detection IDs and user agents for major AI crawlers from OpenAI, Anthropic, Google, Meta, and others.</li>
<li><strong><a href="/ai-crawl-control/reference/worker-templates/">Worker templates</a></strong> — Deploy the x402 Payment-Gated Proxy to monetize crawler access or charge bots while letting humans through free.</li>
</ul>


<h2 id="added-timezone-preferences-settings"><a href="/changelog/post/2026-01-27-timezone-preferences/">Added Timezone preferences settings</a></h2>
<p><em>2026-01-27</em></p>
<p>You can now set the timezone in the Cloudflare dashboard as Coordinated Universal Time (UTC) or your browser or system's timezone.</p>
<h4 id="2026-01-27-timezone-preferences-what-s-new">What's New</h4>
<p>Unless otherwise specified in the user interface, all dates and times in the Cloudflare dashboard are now displayed in the selected timezone.</p>
<p>You can change the timezone setting from the user profile dropdown.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-01-27-set-timezone.png" alt="Timezone preference dropdown" /></p>
<p>The page will reload to apply the new timezone setting.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/core-platform/3/">Previous</a><span>Page 4 of 8</span><a class="pagination-next" rel="next" href="/changelog/product-group/core-platform/5/">Next</a></nav>
