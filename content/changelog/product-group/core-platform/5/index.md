<h1 id="changelog">Changelog</h1>

<h2 id="control-request-and-response-body-buffering-in-configuration-rules"><a href="/changelog/post/2026-01-27-body-buffering-settings/">Control request and response body buffering in Configuration Rules</a></h2>
<p><em>2026-01-27</em></p>
<p>You can now control how Cloudflare buffers HTTP request and response bodies using two new settings in <a href="/rules/configuration-rules/">Configuration Rules</a>.</p>
<h4 id="2026-01-27-body-buffering-settings-request-body-buffering">Request body buffering</h4>
<p>Controls how Cloudflare buffers HTTP request bodies before forwarding them to your origin server:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standard</strong> (default)</td>
<td>Cloudflare can inspect a prefix of the request body for enabled functionality such as WAF and Bot Management.</td>
</tr>
<tr>
<td><strong>Full</strong></td>
<td>Buffers the entire request body before sending to origin.</td>
</tr>
<tr>
<td><strong>None</strong></td>
<td>No buffering — the request body streams directly to origin without inspection.</td>
</tr>
</tbody>
</table>
<h4 id="2026-01-27-body-buffering-settings-response-body-buffering">Response body buffering</h4>
<p>Controls how Cloudflare buffers HTTP response bodies before forwarding them to the client:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standard</strong> (default)</td>
<td>Cloudflare can inspect a prefix of the response body for enabled functionality.</td>
</tr>
<tr>
<td><strong>None</strong></td>
<td>No buffering — the response body streams directly to the client without inspection.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17748.md")</aside>
<h4 id="2026-01-27-body-buffering-settings-api-example">API example</h4>
<pre><code class="language-json">{&#10;  &quot;action&quot;: &quot;set_config&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;request_body_buffering&quot;: &quot;standard&quot;,&#10;    &quot;response_body_buffering&quot;: &quot;none&quot;&#10;  }&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/rules/configuration-rules/">Configuration Rules</a>.</p>


<h2 id="new-2fa-experience-for-login"><a href="/changelog/post/2026-01-23-New-2FA-Experience/">New 2FA Experience for Login</a></h2>
<p><em>2026-01-23</em></p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-01-23-2fa-interstitial.png" alt="Screenshot of new 2FA enrollment experience" /></p>
<p>In an effort to improve overall user security, users without 2FA will be prompted upon login to enroll in email 2FA. This will improve user security posture while minimizing friction. Users without email 2FA enabled will see a prompt to secure their account with additional factors upon logging in. Enrolling in 2FA remains optional, but strongly encouraged as it is the best way to prevent account takeovers.</p>
<p>We also made changes to existing 2FA screens to improve the user experience. Now we have distinct experiences for each 2FA factor type, reflective of the way that factor works.</p>
<h4 id="2026-01-23-New-2FA-Experience-for-more-information">For more information</h4>
* [Configure Email Two Factor Authentication](/fundamentals/user-profiles/2fa/#configure-email-two-factor-authentication)


<h2 id="new-cryptographic-functions-encode-base64-and-sha256"><a href="/changelog/post/2026-01-22-sha256-base64-encode-functions/">New cryptographic functions — encode_base64() and sha256()</a></h2>
<p><em>2026-01-22</em></p>
<p>Cloudflare Rulesets now includes <code>encode_base64()</code> and <code>sha256()</code> functions, enabling you to generate signed request headers directly in rule expressions. These functions support common patterns like constructing a canonical string from request attributes, computing a SHA256 digest, and Base64-encoding the result.</p>
<hr />
<h4 id="2026-01-22-sha256-base64-encode-functions-new-functions">New functions</h4>
<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>encode_base64(input, flags)</code></td>
<td>Encodes a string to Base64 format. Optional <code>flags</code> parameter: <code>u</code> for URL-safe encoding, <code>p</code> for padding (adds <code>=</code> characters to make the output length a multiple of 4, as required by some systems). By default, output is standard Base64 without padding.</td>
<td>All plans (in header transform rules)</td>
</tr>
<tr>
<td><code>sha256(input)</code></td>
<td>Computes a SHA256 hash of the input string.</td>
<td>Requires enablement</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17747.md")</aside>
<hr />
<h4 id="2026-01-22-sha256-base64-encode-functions-examples">Examples</h4>
<p><strong>Encode a string to Base64 format:</strong></p>
<pre><code class="language-txt">encode_base64(&quot;hello world&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ</code></p>
<p><strong>Encode a string to Base64 format with padding:</strong></p>
<pre><code class="language-txt">encode_base64(&quot;hello world&quot;, &quot;p&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ=</code></p>
<p><strong>Perform a URL-safe Base64 encoding of a string:</strong></p>
<pre><code class="language-txt">encode_base64(&quot;hello world&quot;, &quot;u&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ</code></p>
<p><strong>Compute the SHA256 hash of a secret token:</strong></p>
<pre><code class="language-txt">sha256(&quot;my-token&quot;)&#10;</code></pre>
<p>Returns a hash that your origin can validate to authenticate requests.</p>
<p><strong>Compute the SHA256 hash of a string and encode the result to Base64 format:</strong></p>
<pre><code class="language-txt">encode_base64(sha256(&quot;my-token&quot;))&#10;</code></pre>
<p>Combines hashing and encoding for systems that expect Base64-encoded signatures.</p>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/functions/">Functions reference</a>.</p>


<h2 id="new-functions-for-array-and-map-operations"><a href="/changelog/post/2026-01-20-array-map-functions/">New functions for array and map operations</a></h2>
<p><em>2026-01-20</em></p>
<h4 id="2026-01-20-array-map-functions-new-functions-for-array-and-map-operations">New functions for array and map operations</h4>
<p>Cloudflare Rulesets now include new functions that enable advanced expression logic for evaluating arrays and maps. These functions allow you to build rules that match against lists of values in request or response headers, enabling use cases like country-based blocking using custom headers.</p>
<hr />
<h4 id="2026-01-20-array-map-functions-new-functions">New functions</h4>
<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>split(source, delimiter)</code></td>
<td>Splits a string into an array of strings using the specified delimiter.</td>
</tr>
<tr>
<td><code>join(array, delimiter)</code></td>
<td>Joins an array of strings into a single string using the specified delimiter.</td>
</tr>
<tr>
<td><code>has_key(map, key)</code></td>
<td>Returns <code>true</code> if the specified key exists in the map.</td>
</tr>
<tr>
<td><code>has_value(map, value)</code></td>
<td>Returns <code>true</code> if the specified value exists in the map.</td>
</tr>
</tbody>
</table>
<hr />
<h4 id="2026-01-20-array-map-functions-example-use-cases">Example use cases</h4>
<p><strong>Check if a country code exists in a header list:</strong></p>
<pre><code class="language-txt">has_value(split(http.response.headers[&quot;x-allow-country&quot;][0], &quot;,&quot;), ip.src.country)&#10;</code></pre>
<p><strong>Check if a specific header key exists:</strong></p>
<pre><code class="language-txt">has_key(http.request.headers, &quot;x-custom-header&quot;)&#10;</code></pre>
<p><strong>Join array values for logging or comparison:</strong></p>
<pre><code class="language-txt">join(http.request.headers.names, &quot;, &quot;)&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/functions/">Functions reference</a>.</p>


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


<h2 id="verify-warp-connector-connectivity-with-a-simple-ping"><a href="/changelog/post/2026-01-15-warp-connector-ping-support/">Verify WARP Connector connectivity with a simple ping</a></h2>
<p><em>2026-01-15</em></p>
<p>We have made it easier to validate connectivity when deploying <a href="/mesh/">WARP Connector</a> as part of your <a href="/reference-architecture/architectures/sase/#connecting-networks">software-defined private network</a>.</p>
<p>You can now <code>ping</code> the WARP Connector host directly on its LAN IP address immediately after installation. This provides a fast, familiar way to confirm that the Connector is online and reachable within your network before testing access to downstream services.</p>
<p>Starting with <a href="/changelog/2026-01-13-warp-linux-ga/">version 2025.10.186.0</a>, WARP Connector responds to traffic addressed to its own LAN IP, giving you immediate visibility into Connector reachability.</p>
<p>Learn more about deploying <a href="/mesh/">WARP Connector</a> and building private network connectivity with <a href="/cloudflare-one/">Cloudflare One</a>.</p>


<h2 id="ai-crawl-control-read-only-role-now-available"><a href="/changelog/post/2026-01-13-ai-crawl-control-read-only-role/">AI Crawl Control Read Only role now available</a></h2>
<p><em>2026-01-13</em></p>
<p>Account administrators can now assign the <strong>AI Crawl Control Read Only</strong> role to provide read-only access to AI Crawl Control at the domain level.</p>
<p>Users with this role can view the <strong>Overview</strong>, <strong>Crawlers</strong>, <strong>Metrics</strong>, <strong>Robots.txt</strong>, and <strong>Settings</strong> tabs but cannot modify crawler actions or settings.</p>
<p>This role is specific for AI Crawl Control. You still require correct permissions to access other areas / features of the dashboard.</p>
<p>To assign, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> and add a policy with the <strong>AI Crawl Control Read Only</strong> role scoped to the desired domain.</p>


<h2 id="metro-code-field-now-available-in-rules"><a href="/changelog/post/2026-01-12-dma-metro-code-field/">Metro code field now available in Rules</a></h2>
<p><em>2026-01-12</em></p>
<p>The <code>ip.src.metro_code</code> field in the Ruleset Engine is now populated with DMA (Designated Market Area) data.</p>
<p>You can use this field to build rules that target traffic based on geographic market areas, enabling more granular location-based policies for your applications.</p>
<h4 id="2026-01-12-dma-metro-code-field-field-details">Field details</h4>
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
<td><code>ip.src.metro_code</code></td>
<td>String | null</td>
<td>The metro code (DMA) of the incoming request's IP address. Returns the designated market area code for the client's location.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre><code>ip.src.metro_code eq &quot;501&quot;&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.metro_code/">Fields reference</a>.</p>


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


<h2 id="new-ai-crawl-control-overview-tab"><a href="/changelog/post/2025-12-18-overview-tab/">New AI Crawl Control Overview tab</a></h2>
<p><em>2025-12-18</em></p>
<p>The <strong>Overview</strong> tab is now the default view in AI Crawl Control. The previous default view with controls for individual AI crawlers is available in the <strong>Crawlers</strong> tab.</p>
<h4 id="2025-12-18-overview-tab-what-s-new">What's new</h4>
<ul>
<li><strong>Executive summary</strong> — Monitor total requests, volume change, most common status code, most popular path, and high-volume activity</li>
<li><strong>Operator grouping</strong> — Track crawlers by their operating companies (OpenAI, Microsoft, Google, ByteDance, Anthropic, Meta)</li>
<li><strong>Customizable filters</strong> — Filter your snapshot by date range, crawler, operator, hostname, or path</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-overview-tab.png" alt="AI Crawl Control Overview tab showing executive summary, metrics, and crawler groups" /></p>
<h4 id="2025-12-18-overview-tab-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong>, where the <strong>Overview</strong> tab opens by default with your activity snapshot.</li>
<li>Use filters to customize your view by date range, crawler, operator, hostname, or path.</li>
<li>Navigate to the <strong>Crawlers</strong> tab to manage controls for individual crawlers.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control/features/analyze-ai-traffic/">analyzing AI traffic</a> and <a href="/ai-crawl-control/features/manage-ai-crawlers/">managing AI crawlers</a>.</p>


<h2 id="improved-accuracy-of-cached-request-classification-in-analytics"><a href="/changelog/post/2025-12-18-cached-request-classification/">Improved accuracy of cached request classification in analytics</a></h2>
<p><em>2025-12-18</em></p>
<p>The cached/uncached classification logic used in Zone Overview analytics has been updated to improve accuracy.</p>
<p>Previously, requests were classified as &quot;cached&quot; based on an overly broad condition that included blocked 403 responses, Snippets requests, and other non-cache request types. This caused inflated cache hit ratios — in some cases showing near-100% cached — and affected approximately 15% of requests classified as cached in rollups.</p>
<p>The condition has been removed from the Zone Overview page. Cached/uncached classification now aligns with the heuristics used in <a href="/analytics/account-and-zone-analytics/zone-analytics/">HTTP Analytics</a>, so only requests genuinely served from cache are counted as cached.</p>
<p><strong>What changed:</strong></p>
<ul>
<li><strong>Zone Overview</strong> — Cache ratios now reflect actual cache performance.</li>
<li><strong>HTTP Analytics</strong> — No change. HTTP Analytics already used the correct classification logic.</li>
<li><strong>Historical data</strong> — This fix applies to new requests only. Previously logged data is not retroactively updated.</li>
</ul>


<h2 id="sentinelone-as-logpush-destination"><a href="/changelog/post/2025-12-11-sentinelone-destination/">SentinelOne as Logpush destination</a></h2>
<p><em>2025-12-11</em></p>
<p>Cloudflare Logpush now supports <strong>SentinelOne</strong> as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://www.sentinelone.com/">SentinelOne AI SIEM</a> via <a href="/logs/logpush/">Logpush</a>. The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/sentinelone/">Destination Configuration</a> documentation.</p>


<h2 id="pay-per-crawl-private-beta-discovery-api-custom-pricing-and-advanced-configuration"><a href="/changelog/post/2025-12-10-pay-per-crawl-enhancements/">Pay Per Crawl (Private beta) - Discovery API, custom pricing, and advanced configuration</a></h2>
<p><em>2025-12-10</em></p>
<p>Pay Per Crawl is introducing enhancements for both AI crawler operators and site owners, focusing on programmatic discovery, flexible pricing models, and granular configuration control.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-for-ai-crawler-operators">For AI crawler operators</h4>
<h4 id="2025-12-10-pay-per-crawl-enhancements-discovery-api">Discovery API</h4>
<p>A new authenticated API endpoint allows verified crawlers to programmatically discover domains participating in Pay Per Crawl. Crawlers can use this to build optimized crawl queues, cache domain lists, and identify new participating sites. This eliminates the need to discover payable content through trial requests.</p>
<p>The API endpoint is <code>GET https://crawlers-api.ai-audit.cfdata.org/charged_zones</code> and requires Web Bot Auth authentication. Refer to <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/">Discover payable content</a> for authentication steps, request parameters, and response schema.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-payment-header-signature-requirement">Payment header signature requirement</h4>
<p>Payment headers (<code>crawler-exact-price</code> or <code>crawler-max-price</code>) must now be included in the Web Bot Auth <code>signature-input</code> header components. This security enhancement prevents payment header tampering, ensures authenticated payment intent, validates crawler identity with payment commitment, and protects against replay attacks with modified pricing. Crawlers must add their payment header to the list of signed components when <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/#22-sign-your-request-with-web-bot-auth">constructing the signature-input header</a>.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-new-crawler-error-header">New <code>crawler-error</code> header</h4>
<p>Pay Per Crawl error responses now include a new <code>crawler-error</code> header with 11 specific <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/">error codes</a> for programmatic handling. Error response bodies remain unchanged for compatibility. These codes enable robust error handling, automated retry logic, and accurate spending tracking.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-for-site-owners">For site owners</h4>
<h4 id="2025-12-10-pay-per-crawl-enhancements-configure-free-pages">Configure free pages</h4>
<p>Site owners can now offer free access to specific pages like homepages, navigation, or discovery pages while charging for other content. Create a <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/#disable-pay-per-crawl-by-uri-pattern">Configuration Rule</a> in <strong>Rules</strong> &gt; <strong>Configuration Rules</strong>, set your URI pattern using wildcard, exact, or prefix matching on the <strong>URI Full</strong> field, and enable the <strong>Disable Pay Per Crawl</strong> setting. When disabled for a URI pattern, crawler requests pass through without blocking or charging.</p>
<p>Some paths are always free to crawl. These paths are: <code>/robots.txt</code>, <code>/sitemap.xml</code>, <code>/security.txt</code>, <code>/.well-known/security.txt</code>, <code>/crawlers.json</code>.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-get-started">Get started</h4>
<p><strong>AI crawler operators</strong>: <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/">Discover payable content</a> | <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/">Crawl pages</a></p>
<p><strong>Site owners</strong>: <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/">Advanced configuration</a></p>


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


<h2 id="fixed-custom-sql-date-picker-inconsistencies"><a href="/changelog/post/2025-11-13-fixed-custom-date/">Fixed custom SQL date picker inconsistencies</a></h2>
<p><em>2025-11-13</em></p>
<p>We've resolved a bug in Log Explorer that caused inconsistencies between the custom SQL date field filters and the date picker dropdown. Previously, users attempting to filter logs based on a custom date field via a SQL query sometimes encountered unexpected results or mismatching dates when using the interactive date picker.</p>
<p>This fix ensures that the custom SQL date field filters now align correctly with the selection made in the date picker dropdown, providing a reliable and predictable filtering experience for your log data. This is particularly important for users creating custom log views based on time-sensitive fields.</p>


<h2 id="log-explorer-adds-14-new-datasets"><a href="/changelog/post/2025-11-13-new-datasets/">Log Explorer adds 14 new datasets</a></h2>
<p><em>2025-11-13</em></p>
<p>We've significantly enhanced Log Explorer by adding support for 14 additional Cloudflare product datasets.</p>
<p>This expansion enables Operations and Security Engineers to gain deeper visibility and telemetry across a wider range of Cloudflare services. By integrating these new datasets, users can now access full context to efficiently investigate security incidents, troubleshoot application performance issues, and correlate logged events across different layers (like application and network) within a single interface. This capability is crucial for a complete and cohesive understanding of event flows across your Cloudflare environment.</p>
<p>The newly supported datasets include:</p>
<h4 id="2025-11-13-new-datasets-zone-level">Zone Level</h4>
<ul>
<li><code>Dns_logs</code></li>
<li><code>Nel_reports</code></li>
<li><code>Page_shield_events</code></li>
<li><code>Spectrum_events</code></li>
<li><code>Zaraz_events</code></li>
</ul>
<h4 id="2025-11-13-new-datasets-account-level">Account Level</h4>
<ul>
<li><code>Audit Logs</code></li>
<li><code>Audit_logs_v2</code></li>
<li><code>Biso_user_actions</code></li>
<li><code>DNS firewall logs</code></li>
<li><code>Email_security_alerts</code></li>
<li><code>Magic Firewall IDS</code></li>
<li><code>Network Analytics</code></li>
<li><code>Sinkhole HTTP</code></li>
<li><code>ipsec_logs</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17736.md")</aside>
<h4 id="2025-11-13-new-datasets-example-correlating-logs">Example: Correlating logs</h4>
<p>You can now use Log Explorer to query and filter with each of these datasets. For example, you can identify an IP address exhibiting suspicious behavior in the <code>FW_event</code> logs, and then instantly pivot to the <code>Network Analytics</code> logs or <code>Access</code> logs to see its network-level traffic profile or if it bypassed a corporate policy.</p>
<p>To learn more and get started, refer to the <a href="/log-explorer/">Log Explorer documentation</a> and the <a href="/logs/">Cloudflare Logs documentation</a>.</p>


<h2 id="resize-your-custom-sql-window-in-log-explorer"><a href="/changelog/post/2025-11-11-resize-sql-window/">Resize your custom SQL window in Log Explorer</a></h2>
<p><em>2025-11-11</em></p>
<p>We're excited to announce a quality-of-life improvement for Log Explorer users. You can now resize the custom SQL query window to accommodate longer and more complex queries.</p>
<p>Previously, if you were writing a long custom SQL query, the fixed-size window required excessive scrolling to view the full query. This update allows you to easily drag the bottom edge of the query window to make it taller. This means you can view your entire custom query at once, improving the efficiency and experience of writing and debugging complex queries.</p>
<p>To learn more and get started, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>


<h2 id="logpush-health-dashboards"><a href="/changelog/post/2025-11-11-health-dashboards/">Logpush Health Dashboards</a></h2>
<p><em>2025-11-11</em></p>
<p>We’re excited to introduce <strong>Logpush Health Dashboards</strong>, giving customers real-time visibility into the status, reliability, and performance of their <a href="/logs/logpush/">Logpush</a> jobs. Health dashboards make it easier to detect delivery issues, monitor job stability, and track performance across destinations. The dashboards are divided into two sections:</p>
<ul>
<li>
<p><strong>Upload Health</strong>: See how much data was successfully uploaded, where drops occurred, and how your jobs are performing overall. This includes data completeness, success rate, and upload volume.</p>
</li>
<li>
<p><strong>Upload Reliability</strong> – Diagnose issues impacting stability, retries, or latency, and monitor key metrics such as retry counts, upload duration, and destination availability.</p>
</li>
</ul>
<p><img src="/assets/upstream/images/logs/Health-Dashboard.gif" alt="Health Dashboard" /></p>
<p>Health Dashboards can be accessed from the Logpush page in the Cloudflare dashboard at the account or zone level, under the Health tab. For more details, refer to our <a href="/logs/logpush/logpush-health"><strong>Logpush Health Dashboards</strong></a> documentation, which includes a comprehensive troubleshooting guide to help interpret and resolve common issues.</p>


<h2 id="cloudflared-proxy-dns-command-will-be-removed-starting-february-2-2026"><a href="/changelog/post/2025-11-11-cloudflared-proxy-dns/">cloudflared proxy-dns command will be removed starting February 2, 2026</a></h2>
<p><em>2025-11-11</em></p>
<p>Starting February 2, 2026, the <code>cloudflared proxy-dns</code> command will be removed from all new <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">releases</a>.</p>
<p>This change is being made to enhance security and address a potential vulnerability in an underlying DNS library. This vulnerability is specific to the <code>proxy-dns</code> command and does not affect any other <code>cloudflared</code> features, such as the core <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> service.</p>
<p>The <code>proxy-dns</code> command, which runs a client-side <a href="/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS (DoH)</a> proxy, has been an officially undocumented feature for several years. This functionality is fully and securely supported by our actively developed products.</p>
<p>Versions of <code>cloudflared</code> released before this date will not be affected and will continue to operate. However, note that our <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#deprecated-releases">official support policy</a> for any <code>cloudflared</code> release is one year from its release date.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-migration-paths">Migration paths</h4>
<p>We strongly advise users of this undocumented feature to migrate to one of the following officially supported solutions before February 2, 2026, to continue benefiting from secure <a href="/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS</a>.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-end-user-devices">End-user devices</h4>
<p>The preferred method for enabling DNS-over-HTTPS on user devices is the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare WARP client</a>. The WARP client automatically secures and proxies all DNS traffic from your device, integrating it with your organization's <a href="/cloudflare-one/traffic-policies/">Zero Trust policies</a> and <a href="/cloudflare-one/reusable-components/posture-checks/">posture checks</a>.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-servers-routers-and-iot-devices">Servers, routers, and IoT devices</h4>
<p>For scenarios where installing a client on every device is not possible (such as servers, routers, or IoT devices), we recommend using the <a href="/mesh/">WARP Connector</a>.</p>
<p>Instead of running <code>cloudflared proxy-dns</code> on a machine, you can install the WARP Connector on a single Linux host within your private network. This connector will act as a gateway, securely routing all DNS and network traffic from your <a href="/mesh/features/routes/">entire subnet</a> to Cloudflare for <a href="/cloudflare-one/traffic-policies/">filtering and logging</a>.</p>


<h2 id="crawler-drilldowns-with-extended-actions-menu"><a href="/changelog/post/2025-11-10-ai-crawl-control-crawler-info/">Crawler drilldowns with extended actions menu</a></h2>
<p><em>2025-11-10</em></p>
<p>AI Crawl Control now supports per-crawler drilldowns with an extended actions menu and status code analytics. Drill down into Metrics, Cloudflare Radar, and Security Analytics, or export crawler data for use in <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/rules/url-forwarding/">Redirect Rules</a>, and robots.txt files.</p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-what-s-new">What's new</h4>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-status-code-distribution-chart">Status code distribution chart</h4>
<p>The <strong>Metrics</strong> tab includes a status code distribution chart showing HTTP response codes (2xx, 3xx, 4xx, 5xx) over time. Filter by individual crawler, category, operator, or time range to analyze how specific crawlers interact with your site.</p>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-status-codes.png" alt="AI Crawl Control status code distribution chart" /></p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-extended-actions-menu">Extended actions menu</h4>
<p>Each crawler row includes a three-dot menu with per-crawler actions:</p>
<ul>
<li><strong>View Metrics</strong> — Filter the AI Crawl Control Metrics page to the selected crawler.</li>
<li><strong>View on Cloudflare Radar</strong> — Access verified crawler details on Cloudflare Radar.</li>
<li><strong>Copy User Agent</strong> — Copy user agent strings for use in WAF custom rules, Redirect Rules, or robots.txt files.</li>
<li><strong>View in Security Analytics</strong> — Filter Security Analytics by detection IDs (Bot Management customers).</li>
<li><strong>Copy Detection ID</strong> — Copy detection IDs for use in WAF custom rules (Bot Management customers).</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-crawler-info.png" alt="AI Crawl Control crawler actions menu" /></p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Metrics</strong> to access the status code distribution chart.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Crawlers</strong> and select the three-dot menu for any crawler to access per-crawler actions.</li>
<li>Select multiple crawlers to use bulk copy buttons for user agents or detection IDs.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control/">AI Crawl Control</a>.</p>


<h2 id="logpush-permission-update-for-zero-trust-datasets"><a href="/changelog/post/2025-11-05-logpush-permissions-update/">Logpush Permission Update for Zero Trust Datasets</a></h2>
<p><em>2025-11-05</em></p>
<p><a href="/logs/logpush/permissions/">Permissions</a> for managing Logpush jobs related to <a href="/logs/logpush/logpush-job/datasets/account/">Zero Trust datasets</a> (Access, Gateway, and DEX) have been updated to improve data security and enforce appropriate access controls.</p>
<p>To view, create, update, or delete Logpush jobs for Zero Trust datasets, users must now have both of the following permissions:</p>
<ul>
<li>Logs Edit</li>
<li>Zero Trust: PII Read</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17738.md")</aside>


<h2 id="log-explorer-now-supports-query-cancellation"><a href="/changelog/post/2025-11-04-query-cancellation/">Log Explorer now supports query cancellation</a></h2>
<p><em>2025-11-04</em></p>
<p>We're excited to announce that Log Explorer users can now cancel queries that are currently running.</p>
<p>This new feature addresses a common pain point: waiting for a long, unintended, or misconfigured query to complete before you can submit a new, correct one. With query cancellation, you can immediately stop the execution of any undesirable query, allowing you to quickly craft and submit a new query, significantly improving your investigative workflow and productivity within Log Explorer.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/core-platform/4/">Previous</a><span>Page 5 of 8</span><a class="pagination-next" rel="next" href="/changelog/product-group/core-platform/6/">Next</a></nav>
