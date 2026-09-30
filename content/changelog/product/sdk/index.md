<h1 id="changelog">Changelog</h1>

<h2 id="go-sdk-v7-0-0-released"><a href="/changelog/post/2026-04-30-go-sdk-v7.0.0/">Go SDK v7.0.0 Released</a></h2>
<p><em>2026-04-30</em></p>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-go/compare/v6.10.0...v7.0.0">v6.10.0...v7.0.0</a></p>
<p>This is a major version release that includes breaking changes to three packages: <code>ai_search</code>, <code>email_security</code>, and <code>workers</code>. These changes reflect upstream API specification updates that improve type correctness and consistency.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-breaking-changes">Breaking Changes</h4>
<p>See the <a href="https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md">v7.0.0 Migration Guide</a> for before/after code examples and actions needed for each change.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-ai-search-searchforagents-metadata-removed">AI Search - SearchForAgents Metadata Removed</h4>
<p>The <code>SearchForAgents</code> nested type has been removed from all instance metadata structs. This field is no longer part of the API specification.</p>
<p><strong>Removed Types:</strong></p>
<ul>
<li><code>InstanceNewResponseMetadataSearchForAgents</code></li>
<li><code>InstanceUpdateResponseMetadataSearchForAgents</code></li>
<li><code>InstanceListResponseMetadataSearchForAgents</code></li>
<li><code>InstanceDeleteResponseMetadataSearchForAgents</code></li>
<li><code>InstanceReadResponseMetadataSearchForAgents</code></li>
<li><code>InstanceNewParamsMetadataSearchForAgents</code></li>
<li><code>InstanceUpdateParamsMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceNewResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceUpdateResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceListResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceDeleteResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceReadResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceNewParamsMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceUpdateParamsMetadataSearchForAgents</code></li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-path-parameter-type-changes">Email Security - Path Parameter Type Changes</h4>
<p>Multiple Email Security settings sub-resources have changed their path parameter types from <code>int64</code> to <code>string</code>:</p>
<ul>
<li><code>AllowPolicies</code> (<code>policyID int64</code> -&gt; <code>policyID string</code>)</li>
<li><code>BlockSenders</code> (<code>patternID int64</code> -&gt; <code>patternID string</code>)</li>
<li><code>Domains</code> (<code>domainID int64</code> -&gt; <code>domainID string</code>)</li>
<li><code>ImpersonationRegistry</code> (<code>displayNameID int64</code> -&gt; <code>impersonationRegistryID string</code>)</li>
<li><code>TrustedDomains</code> (<code>trustedDomainID int64</code> -&gt; <code>trustedDomainID string</code>)</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-investigate-parameter-rename">Email Security - Investigate Parameter Rename</h4>
<p>The <code>Investigate.Get</code>, <code>Investigate.Move.New</code>, and <code>Investigate.Reclassify.New</code> methods now use <code>investigateID</code> instead of <code>postfixID</code> as the path parameter name.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-domains-bulkdelete-method-removed">Email Security - Domains BulkDelete Method Removed</h4>
<p>The <code>SettingDomainService.BulkDelete</code> method and its associated types have been removed:</p>
<ul>
<li><code>SettingDomainBulkDeleteResponse</code></li>
<li><code>SettingDomainBulkDeleteParams</code></li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-trusteddomains-return-type-change">Email Security - TrustedDomains Return Type Change</h4>
<p><code>SettingTrustedDomainService.New</code> now returns <code>*SettingTrustedDomainNewResponse</code> instead of <code>*SettingTrustedDomainNewResponseUnion</code>.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-investigate-move-return-type-change">Email Security - Investigate.Move Return Type Change</h4>
<p><code>InvestigateMoveService.New</code> now returns <code>*pagination.SinglePage[InvestigateMoveNewResponse]</code> instead of <code>*[]InvestigateMoveNewResponse</code>.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-workers-observability-telemetry-filter-restructuring">Workers - Observability Telemetry Filter Restructuring</h4>
<p>The observability telemetry filter parameter types have been restructured to support nested filter groups. New discriminated union types replace the previous flat filter arrays:</p>
<ul>
<li><code>ObservabilityTelemetryKeysParams.Filters</code> now accepts <code>FiltersObjectFilterUnion</code> (was <code>[]interface\{\}</code>)</li>
<li><code>ObservabilityTelemetryQueryParams.Parameters.Filters</code> now accepts <code>FiltersObjectFilterUnion</code></li>
<li><code>ObservabilityTelemetryValuesParams.Filters</code> now accepts <code>FiltersObjectFilterUnion</code></li>
</ul>
<p>New types include <code>FiltersObjectFiltersObject</code> (for group filters with <code>FilterCombination</code>) and <code>FiltersWorkersObservabilityFilterLeaf</code> (for leaf filters with typed <code>Operation</code>, <code>Type</code>, and <code>Value</code> fields).</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-features">Features</h4>
<h4 id="2026-04-30-go-sdk-v7.0.0-organizations-audit-logs-client-organizations-logs-audit">Organizations - Audit Logs (<code>client.Organizations.Logs.Audit</code>)</h4>
<p><strong>NEW SERVICE:</strong> Query organization audit logs with cursor-based pagination.</p>
<ul>
<li><code>List()</code> - Retrieve audit logs</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-browser-rendering-client-browserrendering">Browser Rendering (<code>client.BrowserRendering</code>)</h4>
<ul>
<li><code>client.BrowserRendering.Devtools.Browser.Targets.Close()</code> - Close a specific browser target (tab, page) by ID</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-queues-client-queues">Queues (<code>client.Queues</code>)</h4>
<ul>
<li><code>client.Queues.GetMetrics()</code> - Retrieve queue metrics for a specific queue</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-ai-search-client-aisearch">AI Search (<code>client.AISearch</code>)</h4>
<ul>
<li>Added <code>WaitForCompletion</code> parameter to <code>NamespaceInstanceItemNewOrUpdateParams</code> and <code>NamespaceInstanceItemSyncParams</code> for synchronous indexing confirmation</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>Magic Transit</strong>: <code>ConnectorService.List</code> parameter name corrected from <code>query</code> to <code>params</code> (non-functional, affects generated documentation only)</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-deprecations">Deprecations</h4>
<p>None in this release.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-go/releases/tag/v7.0.0">Download Go SDK v7.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/go/">Go SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md">Migration Guide</a></li>
</ul>


<h2 id="cloudflare-python-sdk-v5-0-0-released"><a href="/changelog/post/2026-04-30-cloudflare-python-v5.0.0/">Cloudflare Python SDK v5.0.0 Released</a></h2>
<p><em>2026-04-30</em></p>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0">v4.3.1...v5.0.0</a></p>
<p>This is a major release of the Cloudflare Python SDK. It drops support for Python 3.8, adds 11 new API services, introduces optional aiohttp backend support for improved async concurrency, and includes hundreds of type and method updates across the entire API surface.</p>
<p><strong>Please review the breaking changes below before upgrading.</strong> A migration guide is available at <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">v5.0.0 Migration Guide</a>.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-breaking-changes">Breaking Changes</h4>
<ul>
<li><strong>Python 3.8 is no longer supported.</strong> The minimum required version is now Python 3.9.</li>
<li><strong><code>typing-extensions</code> minimum version bumped</strong> from <code>&gt;=4.10</code> to <code>&gt;=4.14</code>.</li>
</ul>
<p>The following resources have breaking changes. See the <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">v5.0.0 Migration Guide</a> for detailed migration instructions.</p>
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
<h4 id="2026-04-30-cloudflare-python-v5.0.0-features">Features</h4>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-aiohttp-backend-support">aiohttp Backend Support</h4>
<p>The async client now supports an optional <code>aiohttp</code> HTTP backend for improved concurrency performance. Install with <code>pip install cloudflare[aiohttp]</code> and use <code>DefaultAioHttpClient()</code> as the <code>http_client</code> parameter.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-python-3-13-and-3-14-support">Python 3.13 and 3.14 Support</h4>
<p>Python 3.13 and 3.14 are now tested and supported.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-new-services">New Services</h4>
<p>The following top-level resources are new in this release:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Client Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Search</td>
<td><code>aisearch</code></td>
<td>AI-powered search capabilities</td>
</tr>
<tr>
<td>Connectivity</td>
<td><code>connectivity</code></td>
<td>Connectivity testing and diagnostics</td>
</tr>
<tr>
<td>Email Sending</td>
<td><code>email_sending</code></td>
<td>Email send and send_raw endpoints</td>
</tr>
<tr>
<td>Fraud</td>
<td><code>fraud</code></td>
<td>Fraud detection and prevention</td>
</tr>
<tr>
<td>Google Tag Gateway</td>
<td><code>google_tag_gateway</code></td>
<td>Google Tag Gateway management</td>
</tr>
<tr>
<td>Organizations</td>
<td><code>organizations</code></td>
<td>Organization audit logs and management</td>
</tr>
<tr>
<td>R2 Data Catalog</td>
<td><code>r2_data_catalog</code></td>
<td>R2 Data Catalog operations</td>
</tr>
<tr>
<td>Realtime Kit</td>
<td><code>realtime_kit</code></td>
<td>Realtime communication (Calls/TURN)</td>
</tr>
<tr>
<td>Resource Tagging</td>
<td><code>resource_tagging</code></td>
<td>Resource tagging and labeling</td>
</tr>
<tr>
<td>Token Validation</td>
<td><code>token_validation</code></td>
<td>Token validation configuration and rules</td>
</tr>
<tr>
<td>Vulnerability Scanner</td>
<td><code>vulnerability_scanner</code></td>
<td>Vulnerability scanning, credential sets, and target environments</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-new-endpoints-on-existing-services">New Endpoints on Existing Services</h4>
<ul>
<li><strong>api_gateway</strong>: Labels endpoints</li>
<li><strong>billing</strong>: Billable usage PayGo endpoint</li>
<li><strong>brand_protection</strong>: v2 endpoints</li>
<li><strong>browser_rendering</strong>: DevTools methods</li>
<li><strong>cache</strong>: Origin cloud regions resource</li>
<li><strong>custom_origin_trust_store</strong>: Custom origin trust store</li>
<li><strong>dns</strong>: <code>dns_records/usage</code> endpoints</li>
<li><strong>email_security</strong>: Phishguard reports endpoint</li>
<li><strong>iam</strong>: User groups and user group members resources</li>
<li><strong>radar</strong>: Botnet Threat Feed and Post-Quantum endpoints</li>
<li><strong>workers</strong>: Observability Destinations resources</li>
<li><strong>zero_trust</strong>: Access Users, DEX rules, Device IP Profile, Device Subnet, WARP Connector connections and failover, WARP Subnet, Gateway PAC files</li>
<li><strong>zones</strong>: Zone environments endpoints</li>
</ul>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li>Fixed <code>polymorphic_serialization</code> parameter in <code>model_dump</code> overrides</li>
<li>Added <code>BaseModel</code> base to response <code>SchemaFieldStruct</code>/<code>SchemaFieldList</code> stubs in Pipelines</li>
<li>Added missing <code>model_rebuild</code>/<code>update_forward_refs</code> for <code>SharedEntryCustomEntry</code> classes in DLP</li>
<li>Made <code>RunQueryParametersNeedleValue</code> a <code>BaseModel</code> with <code>arbitrary_types_allowed</code> in Workers</li>
<li>Removed duplicate <code>notification_url</code> field in webhook response types for Stream</li>
<li>Resolved pre-existing codegen type errors</li>
<li>Fixed <code>type: ignore[call-arg]</code> placement for mypy compatibility in Radar</li>
</ul>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-deprecations">Deprecations</h4>
<p>Resources with <code>@deprecated</code> annotations on some methods include: <code>accounts</code>, <code>addressing</code>, <code>ai-gateway</code>, <code>aisearch</code>, <code>api-gateway</code>, <code>billing</code>, <code>cloudforce-one</code>, <code>dns</code>, <code>email-routing</code>, <code>email-security</code>, <code>filters</code>, <code>firewall</code>, <code>images</code>, <code>intel</code>, <code>kv</code>, <code>logpush</code>, <code>origin-tls-client-auth</code>, <code>pages</code>, <code>pipelines</code>, <code>radar</code>, <code>rate-limits</code>, <code>registrar</code>, <code>rulesets</code>, <code>ssl</code>, <code>user</code>, <code>workers</code>, <code>workers-for-platforms</code>, <code>zero-trust</code>, <code>zones</code></p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-python/releases/tag/v5.0.0">Download Python SDK v5.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/python/">Python SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">Migration Guide</a></li>
</ul>


<h2 id="cloudflare-typescript-sdk-v6-0-0-released"><a href="/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/">Cloudflare TypeScript SDK v6.0.0 Released</a></h2>
<p><em>2026-04-30</em></p>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-typescript/compare/v6.0.0-beta.2...v6.0.0">v6.0.0-beta.2...v6.0.0</a></p>
<p>This is a major version release of the Cloudflare TypeScript SDK. It includes 11 entirely new top-level API resources, new sub-resources and methods across 50+ existing resources, SDK infrastructure improvements, and breaking changes to the generated API surface from the v5.x line.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-breaking-changes">Breaking Changes</h4>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-sdk-infrastructure">SDK Infrastructure</h4>
<ul>
<li><strong>Retry-After handling changed</strong>: The SDK now respects any server-specified <code>Retry-After</code> value for rate-limited requests. Previously, values over 60 seconds were ignored and a default backoff was used instead.</li>
<li><strong>Empty response handling</strong>: Responses with <code>content-length: 0</code> now return <code>undefined</code> instead of attempting to parse the body.</li>
<li><strong>Environment variable reading</strong>: Empty string env vars (for example, <code>CLOUDFLARE_API_TOKEN=&quot;&quot;</code>) are now treated as unset.</li>
<li><strong>Path query parameter merging</strong>: URL search params embedded in endpoint paths are now extracted and merged into the query object.</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-removed-endpoints-17">Removed Endpoints (17)</h4>
<p>17 HTTP endpoints were removed from the SDK, affecting <code>abuse-reports</code>, <code>cloudforce-one</code>, <code>dlp/profiles/predefined</code>, <code>email-security/investigate</code>, <code>email-security/settings</code>, and <code>intel/ip-list</code>.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-method-signature-changes">Method Signature Changes</h4>
<ul>
<li><code>client.ai.toMarkdown.transform(file, \{ ...params \})</code> -&gt; <code>client.ai.toMarkdown.transform(\{ ...params \})</code> -- <code>file</code> moved from positional arg into params body</li>
<li><code>client.radar.ai.toMarkdown.create(body, \{ ...params \})</code> -&gt; <code>client.radar.ai.toMarkdown.create(\{ ...params \})</code> -- <code>body</code> moved from positional arg into params</li>
<li><code>client.abuseReports.create(reportType, \{ ...params \})</code> -&gt; <code>client.abuseReports.create(reportParam, \{ ...params \})</code> -- positional arg renamed</li>
<li><code>client.iam.userGroups.members.create(userGroupId, [ ...body ])</code> -&gt; <code>client.iam.userGroups.members.create(userGroupId, [ ...members ])</code> -- body array param renamed</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-renamed-client-paths">Renamed Client Paths</h4>
<ul>
<li><code>client.originTLSClientAuth.hostnames.certificates</code> -&gt; <code>client.originTLSClientAuth.zoneCertificates</code></li>
<li><code>client.radar.netflows</code> -&gt; <code>client.radar.netFlows</code> (casing change)</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-return-type-changes-179">Return Type Changes (179)</h4>
<ul>
<li><strong>133 methods now return <code>null</code></strong> instead of a typed response object. This primarily affects delete operations across <code>accounts</code>, <code>cache</code>, <code>d1</code>, <code>filters</code>, <code>firewall</code>, <code>hyperdrive</code>, <code>iam</code>, <code>kv</code>, <code>logpush</code>, <code>logs</code>, <code>r2</code>, <code>stream</code>, <code>workers</code>, <code>zero-trust</code>, <code>zones</code>, and others.</li>
<li><strong>17 methods changed pagination type</strong> (for example, <code>KeysCursorPaginationAfter</code> -&gt; <code>KeysCursorLimitPagination</code>).</li>
<li><strong>29 methods changed to a different named type</strong> (for example, <code>CloudflaredCreateResponse</code> -&gt; <code>CloudflareTunnel</code>).</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-removed-types-43">Removed Types (43)</h4>
<p>24 shared types removed from root namespace (<code>ASN</code>, <code>AuditLog</code>, <code>Member</code>, <code>Permission</code>, <code>Role</code>, <code>Subscription</code>, <code>Token</code>, etc.). 19 response types consolidated or renamed.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-resource-restructuring">Resource Restructuring</h4>
<p>19 resources were restructured from single files to directories. Public API client paths are unchanged, but deep imports may break.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-new-top-level-resources">New Top-Level Resources</h4>
<p>11 entirely new resources added to the client:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Client Path</th>
<th>Methods</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Search</td>
<td><code>client.aiSearch</code></td>
<td>46</td>
<td>Instances, namespaces, tokens, and items</td>
</tr>
<tr>
<td>Connectivity</td>
<td><code>client.connectivity</code></td>
<td>5</td>
<td>Directory service APIs</td>
</tr>
<tr>
<td>Email Sending</td>
<td><code>client.emailSending</code></td>
<td>7</td>
<td>Send and send_raw endpoints</td>
</tr>
<tr>
<td>Fraud</td>
<td><code>client.fraud</code></td>
<td>2</td>
<td>Fraud detection API</td>
</tr>
<tr>
<td>Google Tag Gateway</td>
<td><code>client.googleTagGateway</code></td>
<td>2</td>
<td>Google Tag Gateway management</td>
</tr>
<tr>
<td>Organizations</td>
<td><code>client.organizations</code></td>
<td>8</td>
<td>Organization profiles and audit logs</td>
</tr>
<tr>
<td>R2 Data Catalog</td>
<td><code>client.r2DataCatalog</code></td>
<td>11</td>
<td>R2 Data Catalog routes</td>
</tr>
<tr>
<td>Realtime Kit</td>
<td><code>client.realtimeKit</code></td>
<td>54</td>
<td>Realtime Kit APIs</td>
</tr>
<tr>
<td>Resource Tagging</td>
<td><code>client.resourceTagging</code></td>
<td>9</td>
<td>Resource tagging routes</td>
</tr>
<tr>
<td>Token Validation</td>
<td><code>client.tokenValidation</code></td>
<td>13</td>
<td>Token validation rules</td>
</tr>
<tr>
<td>Vulnerability Scanner</td>
<td><code>client.vulnerabilityScanner</code></td>
<td>21</td>
<td>Vulnerability scanning</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-new-sub-resources-on-existing-resources">New Sub-Resources on Existing Resources</h4>
<ul>
<li><strong>browser-rendering</strong>: <code>crawl</code>, <code>devtools</code> - Crawl endpoints and DevTools methods</li>
<li><strong>cache</strong>: <code>origin-cloud-regions</code> - Origin cloud regions resource</li>
<li><strong>dns</strong>: <code>usage</code> - DNS records usage endpoints</li>
<li><strong>d1</strong>: <code>time-travel</code> - Time travel get_bookmark and restore</li>
<li><strong>email-security</strong>: <code>phishguard</code> - Phishguard reports endpoint</li>
<li><strong>pipelines</strong>: <code>sinks</code>, <code>streams</code> - Pipelines restructure</li>
<li><strong>radar</strong>: <code>agent-readiness</code>, <code>geolocations</code>, <code>post-quantum</code> - New analytics endpoints</li>
<li><strong>workers</strong>: <code>observability</code> - Observability destinations</li>
<li><strong>zones</strong>: <code>environments</code> - Zone environments endpoints</li>
<li><strong>api-gateway</strong>: <code>labels</code> - Labels endpoints</li>
<li><strong>brand-protection</strong>: <code>v2</code> - V2 endpoints</li>
<li><strong>alerting</strong>: <code>silences</code> - Alert silencing API</li>
<li><strong>billing</strong>: <code>usage</code> - Billable usage PayGo endpoint</li>
<li><strong>iam</strong>: <code>sso</code> - SSO Connectors resource</li>
<li><strong>queues</strong>: <code>getMetrics</code> method - Queues metrics endpoint</li>
<li><strong>registrar</strong>: <code>registration-status</code>, <code>update-status</code> - Registrar API convergence</li>
<li><strong>zero-trust</strong>: DLP settings, DEX rules, Access Users, WARP Connector, WARP Subnets, Gateway PAC files, Gateway tenants</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li>Resolved type errors from codegen overwriting manual fixes</li>
<li>Fixed <code>post()</code> usage for to-markdown endpoints to resolve async type error</li>
<li>Added least-privilege permissions to all workflow jobs</li>
<li>Reverted erroneous removal of rulesets resource methods and types</li>
<li>Resolved prettier formatting errors in codegen output</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-deprecations">Deprecations</h4>
<p>The following resources now include <code>@deprecated</code> annotations on some methods:</p>
<p><code>accounts</code>, <code>addressing</code>, <code>ai-gateway</code>, <code>aisearch</code>, <code>api-gateway</code>, <code>billing</code>, <code>cloudforce-one</code>, <code>custom-nameservers</code>, <code>dns</code>, <code>email-routing</code>, <code>email-security</code>, <code>filters</code>, <code>firewall</code>, <code>images</code>, <code>intel</code>, <code>keyless-certificates</code>, <code>kv</code>, <code>logpush</code>, <code>origin-tls-client-auth</code>, <code>page-shield</code>, <code>pages</code>, <code>pipelines</code>, <code>radar</code>, <code>rate-limits</code>, <code>registrar</code>, <code>rulesets</code>, <code>ssl</code>, <code>user</code>, <code>workers</code>, <code>workers-for-platforms</code>, <code>zero-trust</code>, <code>zones</code></p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript/releases/tag/v6.0.0">Download TypeScript SDK v6.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/typescript/">TypeScript SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/CHANGELOG.md">Full Changelog</a></li>
</ul>


<h2 id="go-sdk-v6-10-0-released"><a href="/changelog/post/2026-04-23-go-sdk-v6.10.0/">Go SDK v6.10.0 Released</a></h2>
<p><em>2026-04-23</em></p>
<h4 id="2026-04-23-go-sdk-v6.10.0-v6-10-0">v6.10.0</h4>
<p>In this release, you'll see a number of breaking changes. This is primarily due to changes in OpenAPI definitions, which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce our SDK libraries.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-breaking-changes">Breaking Changes</h4>
<p>See the <a href="https://github.com/cloudflare/cloudflare-go/blob/main/MIGRATION_GUIDE.md">v6.10.0 Migration Guide</a> for before/after code examples and actions needed for each change.</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-abuse-reports-registrar-whois-report-field-removals">Abuse Reports - Registrar WHOIS Report Field Removals</h4>
<p>Several fields have been removed from <code>AbuseReportNewParamsBodyAbuseReportsRegistrarWhoisReportRegWhoRequest</code>:</p>
<ul>
<li><code>RegWhoGoodFaithAffirmation</code></li>
<li><code>RegWhoLawfulProcessingAgreement</code></li>
<li><code>RegWhoLegalBasis</code></li>
<li><code>RegWhoRequestType</code></li>
<li><code>RegWhoRequestedDataElements</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-ai-search-instance-params-restructured">AI Search - Instance Params Restructured</h4>
<p>The <code>InstanceNewParams</code> and <code>InstanceUpdateParams</code> types have been significantly restructured. Many fields have been moved or removed:</p>
<ul>
<li><code>InstanceNewParams.TokenID</code>, <code>Type</code>, <code>CreatedFromAISearchWizard</code>, <code>WorkerDomain</code> removed</li>
<li><code>InstanceUpdateParams</code> — most configuration fields removed (including <code>IndexMethod</code>, <code>IndexingOptions</code>, <code>MaxNumResults</code>, <code>Metadata</code>, <code>Paused</code>, <code>PublicEndpointParams</code>, <code>Reranking</code>, <code>RerankingModel</code>, <code>RetrievalOptions</code>, <code>RewriteModel</code>, <code>RewriteQuery</code>, <code>ScoreThreshold</code>, <code>SourceParams</code>, <code>Summarization</code>, <code>SummarizationModel</code>, <code>SystemPromptAISearch</code>, <code>SystemPromptIndexSummarization</code>, <code>SystemPromptRewriteQuery</code>, <code>TokenID</code>, <code>CreatedFromAISearchWizard</code>, <code>WorkerDomain</code>)</li>
<li><code>InstanceSearchParams.Messages</code> field removed along with <code>InstanceSearchParamsMessage</code> and <code>InstanceSearchParamsMessagesRole</code> types</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-ai-search-instanceitem-service-removed">AI Search - InstanceItem Service Removed</h4>
<p>The <code>InstanceItemService</code> type has been removed. The items sub-resource at <code>client.AISearch.Instances.Items</code> no longer exists in the non-namespace path. Use <code>client.AISearch.Namespaces.Instances.Items</code> instead.</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-ai-search-token-types-removed">AI Search - Token Types Removed</h4>
<p>The following types have been removed from the <code>ai_search</code> package:</p>
<ul>
<li><code>TokenDeleteResponse</code></li>
<li><code>TokenListParams</code> (and associated <code>TokenListParamsOrderBy</code>, <code>TokenListParamsOrderByDirection</code>)</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-email-security-investigate-move-return-type-change">Email Security - Investigate Move Return Type Change</h4>
<p>The <code>Investigate.Move.New()</code> method now returns a raw slice instead of a paginated wrapper:</p>
<ul>
<li><code>New()</code> returns <code>*[]InvestigateMoveNewResponse</code> instead of <code>*pagination.SinglePage[InvestigateMoveNewResponse]</code></li>
<li><code>NewAutoPaging()</code> method removed</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-hyperdrive-config-params-restructured">Hyperdrive - Config Params Restructured</h4>
<p>The <code>ConfigEditParams</code> type lost its <code>MTLS</code> and <code>Name</code> fields. The <code>HyperdriveMTLSParam</code> type lost <code>MTLS</code> and <code>Host</code> fields. The <code>Host</code> field on origin config changed from <code>param.Field[string]</code> to a plain <code>string</code>.</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-iam-usergroupmember-params-and-return-types-changed">IAM - UserGroupMember Params and Return Types Changed</h4>
<p>The <code>UserGroupMemberNewParams</code> struct has been restructured and the <code>New()</code> method now returns a paginated response:</p>
<ul>
<li><code>UserGroupMemberNewParams.Body</code> renamed to <code>UserGroupMemberNewParams.Members</code></li>
<li><code>UserGroupMemberNewParamsBody</code> renamed to <code>UserGroupMemberNewParamsMember</code></li>
<li><code>UserGroupMemberUpdateParams.Body</code> renamed to <code>UserGroupMemberUpdateParams.Members</code></li>
<li><code>UserGroupMemberUpdateParamsBody</code> renamed to <code>UserGroupMemberUpdateParamsMember</code></li>
<li><code>UserGroups.Members.New()</code> returns <code>*pagination.SinglePage[UserGroupMemberNewResponse]</code> instead of <code>*UserGroupMemberNewResponse</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-iam-usergroup-list-direction-type-changed">IAM - UserGroup List Direction Type Changed</h4>
<p>The <code>UserGroupListParams.Direction</code> field changed from <code>param.Field[string]</code> to <code>param.Field[UserGroupListParamsDirection]</code> (typed enum with <code>asc</code>/<code>desc</code> values).</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-pipelines-delete-methods-now-return-typed-responses">Pipelines - Delete Methods Now Return Typed Responses</h4>
<p>Several delete methods across Pipelines now return typed responses instead of bare error:</p>
<ul>
<li><code>Pipelines.DeleteV1()</code> returns <code>(*PipelineDeleteV1Response, error)</code> instead of <code>error</code></li>
<li><code>Pipelines.Sinks.Delete()</code> returns <code>(*SinkDeleteResponse, error)</code> instead of <code>error</code></li>
<li><code>Pipelines.Streams.Delete()</code> returns <code>(*StreamDeleteResponse, error)</code> instead of <code>error</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-queues-message-response-types-removed">Queues - Message Response Types Removed</h4>
<p>The following response envelope types have been removed:</p>
<ul>
<li><code>MessageBulkPushResponseSuccess</code></li>
<li><code>MessagePushResponseSuccess</code></li>
<li><code>MessageAckResponse</code> fields <code>RetryCount</code> and <code>Warnings</code> removed</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-secrets-store-pagination-wrapper-removal-and-type-changes">Secrets Store - Pagination Wrapper Removal and Type Changes</h4>
<p>Methods now return direct types instead of <code>SinglePage</code> wrappers, and several internal types have been removed. Associated <code>AutoPaging</code> methods have also been removed:</p>
<ul>
<li><code>Stores.New()</code> returns <code>*StoreNewResponse</code> instead of <code>*pagination.SinglePage[StoreNewResponse]</code></li>
<li><code>Stores.NewAutoPaging()</code> method removed</li>
<li><code>Stores.Secrets.BulkDelete()</code> returns <code>*StoreSecretBulkDeleteResponse</code> instead of <code>*pagination.SinglePage[StoreSecretBulkDeleteResponse]</code></li>
<li><code>Stores.Secrets.BulkDeleteAutoPaging()</code> method removed</li>
<li>Removed types: <code>StoreDeleteResponse</code>, <code>StoreDeleteResponseEnvelopeResultInfo</code>, <code>StoreSecretDeleteResponse</code>, <code>StoreSecretDeleteResponseStatus</code>, <code>StoreSecretBulkDeleteResponse</code> (old shape), <code>StoreSecretBulkDeleteResponseStatus</code>, <code>StoreSecretDeleteResponseEnvelopeResultInfo</code></li>
<li><code>StoreNewParams</code> restructured (old <code>StoreNewParamsBody</code> removed)</li>
<li><code>StoreSecretBulkDeleteParams</code> restructured</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-stream-audiotracks-return-type-change">Stream - AudioTracks Return Type Change</h4>
<p>The <code>AudioTracks.Get()</code> method now returns a dedicated response type instead of a paginated list. The <code>GetAutoPaging()</code> method has been removed:</p>
<ul>
<li><code>Get()</code> returns <code>*AudioTrackGetResponse</code> instead of <code>*pagination.SinglePage[Audio]</code></li>
<li><code>GetAutoPaging()</code> method removed</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-stream-clip-type-removal-and-return-type-change">Stream - Clip Type Removal and Return Type Change</h4>
<p>The <code>Clip.New()</code> method now returns the shared <code>Video</code> type. The following types have been entirely removed:</p>
<ul>
<li><code>Clip</code>, <code>ClipPlayback</code>, <code>ClipStatus</code>, <code>ClipWatermark</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-stream-copy-and-clip-params-field-removals">Stream - Copy and Clip Params Field Removals</h4>
<ul>
<li><code>ClipNewParams.MaxDurationSeconds</code>, <code>ThumbnailTimestampPct</code>, <code>Watermark</code> removed</li>
<li><code>CopyNewParams.ThumbnailTimestampPct</code>, <code>Watermark</code> removed</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-stream-download-and-webhook-changes">Stream - Download and Webhook Changes</h4>
<ul>
<li><code>DownloadNewResponseStatus</code> type removed</li>
<li><code>WebhookUpdateResponse</code> and <code>WebhookGetResponse</code> changed from <code>interface{}</code> type aliases to full struct types</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-zero-trust-access-ai-control-mcp-portal-union-types-removed">Zero Trust - Access AI Control MCP Portal Union Types Removed</h4>
<p>The following union interface types have been removed:</p>
<ul>
<li><code>AccessAIControlMcpPortalListResponseServersUpdatedPromptsUnion</code></li>
<li><code>AccessAIControlMcpPortalListResponseServersUpdatedToolsUnion</code></li>
<li><code>AccessAIControlMcpPortalReadResponseServersUpdatedPromptsUnion</code></li>
<li><code>AccessAIControlMcpPortalReadResponseServersUpdatedToolsUnion</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-features">Features</h4>
<h4 id="2026-04-23-go-sdk-v6.10.0-vulnerability-scanner-client-vulnerabilityscanner">Vulnerability Scanner (<code>client.VulnerabilityScanner</code>)</h4>
<p><strong>NEW SERVICE:</strong> Full vulnerability scanning management</p>
<ul>
<li><strong>CredentialSets</strong> - CRUD for credential sets (<code>New</code>, <code>Update</code>, <code>List</code>, <code>Delete</code>, <code>Edit</code>, <code>Get</code>)</li>
<li><strong>Credentials</strong> - Manage credentials within sets (<code>New</code>, <code>Update</code>, <code>List</code>, <code>Delete</code>, <code>Edit</code>, <code>Get</code>)</li>
<li><strong>Scans</strong> - Create and manage vulnerability scans (<code>New</code>, <code>List</code>, <code>Get</code>)</li>
<li><strong>TargetEnvironments</strong> - Manage scan target environments (<code>New</code>, <code>Update</code>, <code>List</code>, <code>Delete</code>, <code>Edit</code>, <code>Get</code>)</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-ai-search-namespaces-client-aisearch-namespaces">AI Search - Namespaces (<code>client.AISearch.Namespaces</code>)</h4>
<p><strong>NEW SERVICE:</strong> Namespace-scoped AI Search management</p>
<ul>
<li><code>New()</code>, <code>Update()</code>, <code>List()</code>, <code>Delete()</code>, <code>ChatCompletions()</code>, <code>Read()</code>, <code>Search()</code></li>
<li><strong>Instances</strong> - Namespace-scoped instances (<code>New</code>, <code>Update</code>, <code>List</code>, <code>Delete</code>, <code>ChatCompletions</code>, <code>Read</code>, <code>Search</code>, <code>Stats</code>)</li>
<li><strong>Jobs</strong> - Instance job management (<code>New</code>, <code>Update</code>, <code>List</code>, <code>Get</code>, <code>Logs</code>)</li>
<li><strong>Items</strong> - Instance item management (<code>List</code>, <code>Delete</code>, <code>Chunks</code>, <code>NewOrUpdate</code>, <code>Download</code>, <code>Get</code>, <code>Logs</code>, <code>Sync</code>, <code>Upload</code>)</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-browser-rendering-devtools-client-browserrendering-devtools">Browser Rendering - Devtools (<code>client.BrowserRendering.Devtools</code>)</h4>
<p><strong>NEW SERVICE:</strong> DevTools protocol browser control</p>
<ul>
<li><strong>Session</strong> - List and get devtools sessions</li>
<li><strong>Browser</strong> - Browser lifecycle management (<code>New</code>, <code>Delete</code>, <code>Connect</code>, <code>Launch</code>, <code>Protocol</code>, <code>Version</code>)</li>
<li><strong>Page</strong> - Get page by target ID</li>
<li><strong>Targets</strong> - Manage browser targets (<code>New</code>, <code>List</code>, <code>Activate</code>, <code>Get</code>)</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-registrar-client-registrar">Registrar (<code>client.Registrar</code>)</h4>
<p><strong>NEW:</strong> Domain check and search endpoints</p>
<ul>
<li><code>Check()</code> - <code>POST /accounts/{account_id}/registrar/domain-check</code></li>
<li><code>Search()</code> - <code>GET /accounts/{account_id}/registrar/domain-search</code></li>
</ul>
<p><strong>NEW:</strong> Registration management (<code>client.Registrar.Registrations</code>)</p>
<ul>
<li><code>New()</code>, <code>List()</code>, <code>Edit()</code>, <code>Get()</code></li>
<li><code>RegistrationStatus.Get()</code> - Get registration workflow status</li>
<li><code>UpdateStatus.Get()</code> - Get update workflow status</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-cache-origin-cloud-regions-client-cache-origincloudregions">Cache - Origin Cloud Regions (<code>client.Cache.OriginCloudRegions</code>)</h4>
<p><strong>NEW SERVICE:</strong> Manage origin cloud region configurations</p>
<ul>
<li><code>New()</code>, <code>List()</code>, <code>Delete()</code>, <code>BulkDelete()</code>, <code>BulkEdit()</code>, <code>Edit()</code>, <code>Get()</code>, <code>SupportedRegions()</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-zero-trust-dlp-settings-client-zerotrust-dlp-settings">Zero Trust - DLP Settings (<code>client.ZeroTrust.DLP.Settings</code>)</h4>
<p><strong>NEW SERVICE:</strong> DLP settings management</p>
<ul>
<li><code>Update()</code>, <code>Delete()</code>, <code>Edit()</code>, <code>Get()</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-radar">Radar</h4>
<ul>
<li><code>AgentReadiness.Summary()</code> - Agent readiness summary by dimension</li>
<li><code>AI.MarkdownForAgents.Summary()</code> - Markdown-for-agents summary</li>
<li><code>AI.MarkdownForAgents.Timeseries()</code> - Markdown-for-agents timeseries</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-iam-client-iam">IAM (<code>client.IAM</code>)</h4>
<ul>
<li><code>UserGroups.Members.Get()</code> - Get details of a specific member in a user group</li>
<li><code>UserGroups.Members.NewAutoPaging()</code> - Auto-paging variant for adding members</li>
<li><code>UserGroups.NewParams.Policies</code> changed from required to optional</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-bot-management">Bot Management</h4>
<ul>
<li><code>ContentBotsProtection</code> field added to <code>BotFightModeConfiguration</code> and <code>SubscriptionConfiguration</code> (<code>block</code>/<code>disabled</code>)</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-deprecations">Deprecations</h4>
<p>None in this release.</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-go/releases/tag/v6.10.0">Download Go SDK v6.10.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/go/">Go SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-go/blob/main/MIGRATION_GUIDE.md">Migration Guide</a></li>
</ul>


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



