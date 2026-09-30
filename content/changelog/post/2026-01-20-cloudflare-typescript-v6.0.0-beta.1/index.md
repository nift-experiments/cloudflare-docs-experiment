<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 20, 2026</time><h2 id="post-title">Cloudflare Typescript SDK v6.0.0-beta.1 now available</h2>
<div class="changelog-badges"><span>fundamentals</span><span>sdk</span></div><div class="changelog-body"><blockquote>
<p><strong>Disclaimer:</strong> Please note that v6.0.0-beta.1 is in Beta and we are still testing it for stability.</p>
</blockquote>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-typescript/compare/v5.2.0...v6.0.0-beta.1">v5.2.0...v6.0.0-beta.1</a></p>
<p>In this release, you'll see a large number of breaking changes. This is primarily due to a change in OpenAPI definitions, which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce our SDK libraries. As the codegen is always evolving and improving, so are our code bases.</p>
<p>Some breaking changes were introduced due to bug fixes, also listed below.</p>
<p>Please ensure you read through the list of changes below before moving to this version - this will help you understand any down or upstream issues it may cause to your environments.</p>
<hr />
<h4 id="breaking-changes">Breaking Changes</h4>
<h4 id="addressing-parameter-requirements-changed">Addressing - Parameter Requirements Changed</h4>
- `BGPPrefixCreateParams.cidr`: optional → **required**
- `PrefixCreateParams.asn`: `number | null` → `number`
- `PrefixCreateParams.loa_document_id`: required → **optional**
- `ServiceBindingCreateParams.cidr`: optional → **required**
- `ServiceBindingCreateParams.service_id`: optional → **required**
<h4 id="api-gateway">API Gateway</h4>
- `ConfigurationUpdateResponse` removed
- `PublicSchema` → `OldPublicSchema`
- `SchemaUpload` → `UserSchemaCreateResponse`
- `ConfigurationUpdateParams.properties` removed; use `normalize`
<h4 id="cloudforceone-response-type-changes">CloudforceOne - Response Type Changes</h4>
- `ThreatEventBulkCreateResponse`: `number` → complex object with counts and errors
<h4 id="d1-database-query-parameters">D1 Database - Query Parameters</h4>
- `DatabaseQueryParams`: simple interface → union type (`D1SingleQuery | MultipleQueries`)
- `DatabaseRawParams`: same change
- Supports batch queries via `batch` array
<h4 id="dns-records-type-renames-21-types">DNS Records - Type Renames (21 types)</h4>
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
<h4 id="iam-resource-groups">IAM Resource Groups</h4>
- `ResourceGroupCreateResponse.scope`: optional single → **required array**
- `ResourceGroupCreateResponse.id`: optional → **required**
<h4 id="origin-ca-certificates-parameter-requirements-changed">Origin CA Certificates - Parameter Requirements Changed</h4>
- `OriginCACertificateCreateParams.csr`: optional → **required**
- `OriginCACertificateCreateParams.hostnames`: optional → **required**
- `OriginCACertificateCreateParams.request_type`: optional → **required**
<h4 id="pages">Pages</h4>
- Renamed: `DeploymentsSinglePage` → `DeploymentListResponsesV4PagePaginationArray`
- Domain response fields: many optional → **required**
<h4 id="pipelines-v0-to-v1-migration">Pipelines - v0 to v1 Migration</h4>
- Entire v0 API deprecated; use v1 methods (`createV1`, `listV1`, etc.)
- New sub-resources: `Sinks`, `Streams`
<h4 id="r2">R2</h4>
- `EventNotificationUpdateParams.rules`: optional → **required**
- Super Slurper: `bucket`, `secret` now required in source params
<h4 id="radar">Radar</h4>
- `dataSource`: `string` → typed enum (23 values)
- `eventType`: `string` → typed enum (6 values)
- V2 methods require `dimension` parameter (breaking signature change)
<h4 id="resource-sharing">Resource Sharing</h4>
- Removed: `status_message` field from all recipient response types
<h4 id="schema-validation">Schema Validation</h4>
- Consolidated `SchemaCreateResponse`, `SchemaListResponse`, `SchemaEditResponse`, `SchemaGetResponse` → `PublicSchema`
- Renamed: `SchemaListResponsesV4PagePaginationArray` → `PublicSchemasV4PagePaginationArray`
<h4 id="spectrum">Spectrum</h4>
- Renamed union members: `AppListResponse.UnionMember0` → `SpectrumConfigAppConfig`
- Renamed union members: `AppListResponse.UnionMember1` → `SpectrumConfigPaygoAppConfig`
<h4 id="workers">Workers</h4>
- Removed: `WorkersBindingKindTailConsumer` type (all occurrences)
- Renamed: `ScriptsSinglePage` → `ScriptListResponsesSinglePage`
- Removed: `DeploymentsSinglePage`
<h4 id="zero-trust-dlp">Zero-Trust DLP</h4>
- `datasets.create()`, `update()`, `get()` return types changed
- `PredefinedGetResponse` union members renamed to `UnionMember0-5`
<h4 id="zero-trust-tunnels">Zero-Trust Tunnels</h4>
- Removed: `CloudflaredCreateResponse`, `CloudflaredListResponse`, `CloudflaredDeleteResponse`, `CloudflaredEditResponse`, `CloudflaredGetResponse`
- Removed: `CloudflaredListResponsesV4PagePaginationArray`
<hr />
<h4 id="features">Features</h4>
<h4 id="abuse-reports-client-abusereports">Abuse Reports (<code>client.abuseReports</code>)</h4>
- **Reports**: `create`, `list`, `get`
- **Mitigations**: sub-resource for abuse mitigations
<h4 id="ai-search-client-aisearch">AI Search (<code>client.aisearch</code>)</h4>
- **Instances**: `create`, `update`, `list`, `delete`, `read`, `stats`
- **Items**: `list`, `get`
- **Jobs**: `create`, `list`, `get`, `logs`
- **Tokens**: `create`, `update`, `list`, `delete`, `read`
<h4 id="connectivity-client-connectivity">Connectivity (<code>client.connectivity</code>)</h4>
- **Directory Services**: `create`, `update`, `list`, `delete`, `get`
- Supports IPv4, IPv6, dual-stack, and hostname configurations
<h4 id="organizations-client-organizations">Organizations (<code>client.organizations</code>)</h4>
- **Organizations**: `create`, `update`, `list`, `delete`, `get`
- **OrganizationProfile**: `update`, `get`
- Hierarchical organization support with parent/child relationships
<h4 id="r2-data-catalog-client-r2datacatalog">R2 Data Catalog (<code>client.r2DataCatalog</code>)</h4>
- **Catalog**: `list`, `enable`, `disable`, `get`
- **Credentials**: `create`
- **MaintenanceConfigs**: `update`, `get`
- **Namespaces**: `list`
- **Tables**: `list`, maintenance config management
- Apache Iceberg integration
<h4 id="realtime-kit-client-realtimekit">Realtime Kit (<code>client.realtimeKit</code>)</h4>
- **Apps**: `get`, `post`
- **Meetings**: `create`, `get`, participant management
- **Livestreams**: 10+ methods for streaming
- **Recordings**: start, pause, stop, get
- **Sessions**: transcripts, summaries, chat
- **Webhooks**: full CRUD
- **ActiveSession**: polls, kick participants
- **Analytics**: organization analytics
<h4 id="token-validation-client-tokenvalidation">Token Validation (<code>client.tokenValidation</code>)</h4>
- **Configuration**: `create`, `list`, `delete`, `edit`, `get`
- **Credentials**: `update`
- **Rules**: `create`, `list`, `delete`, `bulkCreate`, `bulkEdit`, `edit`, `get`
- JWT validation with RS256/384/512, PS256/384/512, ES256, ES384
<h4 id="alerting-silences-client-alerting-silences">Alerting Silences (<code>client.alerting.silences</code>)</h4>
- `create`, `update`, `list`, `delete`, `get`
<h4 id="iam-sso-client-iam-sso">IAM SSO (<code>client.iam.sso</code>)</h4>
- `create`, `update`, `list`, `delete`, `get`, `beginVerification`
<h4 id="pipelines-v1-client-pipelines">Pipelines v1 (<code>client.pipelines</code>)</h4>
- **Sinks**: `create`, `list`, `delete`, `get`
- **Streams**: `create`, `update`, `list`, `delete`, `get`
<h4 id="zero-trust-ai-controls-mcp-client-zerotrust-access-aicontrols-mcp">Zero-Trust AI Controls / MCP (<code>client.zeroTrust.access.aiControls.mcp</code>)</h4>
- **Portals**: `create`, `update`, `list`, `delete`, `read`
- **Servers**: `create`, `update`, `list`, `delete`, `read`, `sync`
<h4 id="accounts">Accounts</h4>
- `managed_by` field with `parent_org_id`, `parent_org_name`
<h4 id="addressing-loa-documents">Addressing LOA Documents</h4>
- `auto_generated` field on `LOADocumentCreateResponse`
<h4 id="addressing-prefixes">Addressing Prefixes</h4>
- `delegate_loa_creation`, `irr_validation_state`, `ownership_validation_state`, `ownership_validation_token`, `rpki_validation_state`
<h4 id="ai">AI</h4>
- Added `toMarkdown.supported()` method to get all supported conversion formats
<h4 id="ai-gateway">AI Gateway</h4>
- `zdr` field added to all responses and params
<h4 id="alerting">Alerting</h4>
- New alert type: `abuse_report_alert`
- `type` field added to PolicyFilter
<h4 id="browser-rendering">Browser Rendering</h4>
- `ContentCreateParams`: refined to discriminated union (`Variant0 | Variant1`)
- Split into URL-based and HTML-based parameter variants for better type safety
<h4 id="client-certificates">Client Certificates</h4>
- `reactivate` parameter in edit
<h4 id="cloudforceone">CloudforceOne</h4>
- `ThreatEventCreateParams.indicatorType`: required → optional
- `hasChildren` field added to all threat event response types
- `datasetIds` query parameter on `AttackerListParams`, `CategoryListParams`, `TargetIndustryListParams`
- `categoryUuid` field on `TagCreateResponse`
- `indicators` array for multi-indicator support per event
- `uuid` and `preserveUuid` fields for UUID preservation in bulk create
- `format` query parameter (`'json' | 'stix2'`) on `ThreatEventListParams`
- `createdAt`, `datasetId` fields on `ThreatEventEditParams`
<h4 id="content-scanning">Content Scanning</h4>
- Added `create()`, `update()`, `get()` methods
<h4 id="custom-pages">Custom Pages</h4>
- New page types: `basic_challenge`, `under_attack`, `waf_challenge`
<h4 id="d1">D1</h4>
- `served_by_colo` - colo that handled query
- `jurisdiction` - `'eu' | 'fedramp'`
- **Time Travel** (`client.d1.database.timeTravel`): `getBookmark()`, `restore()` - point-in-time recovery
<h4 id="email-security">Email Security</h4>
- New fields on `InvestigateListResponse`/`InvestigateGetResponse`: `envelope_from`, `envelope_to`, `postfix_id_outbound`, `replyto`
- New detection classification: `'outbound_ndr'`
- Enhanced `Finding` interface with `attachment`, `detection`, `field`, `portion`, `reason`, `score`
- Added `cursor` query parameter to `InvestigateListParams`
<h4 id="gateway-lists">Gateway Lists</h4>
- New list types: `CATEGORY`, `LOCATION`, `DEVICE`
<h4 id="intel">Intel</h4>
- New issue type: `'configuration_suggestion'`
- `payload` field: `unknown` → typed `Payload` interface with `detection_method`, `zone_tag`
<h4 id="leaked-credential-checks">Leaked Credential Checks</h4>
- Added `detections.get()` method
<h4 id="logpush">Logpush</h4>
- New datasets: `dex_application_tests`, `dex_device_state_events`, `ipsec_logs`, `warp_config_changes`, `warp_toggle_changes`
<h4 id="load-balancers">Load Balancers</h4>
- `Monitor.port`: `number` → `number | null`
- `Pool.load_shedding`: `LoadShedding` → `LoadShedding | null`
- `Pool.origin_steering`: `OriginSteering` → `OriginSteering | null`
<h4 id="magic-transit">Magic Transit</h4>
- `license_key` field on connectors
- `provision_license` parameter for auto-provisioning
- IPSec: `custom_remote_identities` with FQDN support
- Snapshots: Bond interface, `probed_mtu` field
<h4 id="pages-1">Pages</h4>
- New response types: `ProjectCreateResponse`, `ProjectListResponse`, `ProjectEditResponse`, `ProjectGetResponse`
- Deployment methods return specific response types instead of generic `Deployment`
<h4 id="queues">Queues</h4>
- Added `subscriptions.get()` method
- Enhanced `SubscriptionGetResponse` with typed event source interfaces
- New event source types: Images, KV, R2, Vectorize, Workers AI, Workers Builds, Workflows
<h4 id="r2-1">R2</h4>
- Sippy: new provider `s3` (S3-compatible endpoints)
- Sippy: `bucketUrl` field for S3-compatible sources
- Super Slurper: `keys` field on source response schemas (specify specific keys to migrate)
- Super Slurper: `pathPrefix` field on source schemas
- Super Slurper: `region` field on S3 source params
<h4 id="radar-1">Radar</h4>
- Added `geolocations.list()`, `geolocations.get()` methods
- Added V2 dimension-based methods (`summaryV2`, `timeseriesGroupsV2`) to radar sub-resources
<h4 id="resource-sharing-1">Resource Sharing</h4>
- Added `terminal` boolean field to Resource Error interfaces
<h4 id="rules">Rules</h4>
- Added `id` field to `ItemDeleteParams.Item`
<h4 id="rulesets">Rulesets</h4>
- New buffering fields on `SetConfigRule`: `request_body_buffering`, `response_body_buffering`
<h4 id="secrets-store">Secrets Store</h4>
- New scopes: `'dex'`, `'access'` (in addition to `'workers'`, `'ai_gateway'`)
<h4 id="ssl-certificate-packs">SSL Certificate Packs</h4>
- Response types now proper interfaces (was `unknown`)
- Fields now required: `id`, `certificates`, `hosts`, `status`, `type`
<h4 id="security-center">Security Center</h4>
- `payload` field: `unknown` → typed `Payload` interface with `detection_method`, `zone_tag`
<h4 id="shared-types">Shared Types</h4>
- Added: `CloudflareTunnelsV4PagePaginationArray` pagination class
<h4 id="workers-1">Workers</h4>
- Added `subdomains.delete()` method
- `Worker.references` - track external dependencies (domains, Durable Objects, queues)
- `Worker.startup_time_ms` - startup timing
- `Script.observability` - observability settings with logging
- `Script.tag`, `Script.tags` - immutable ID and tags
- Placement: support for region, hostname, host-based placement
- `tags`, `tail_consumers` now accept `| null`
- Telemetry: `traces` field, `$containers` event info, `durableObjectId`, `transactionName`, `abr_level` fields
<h4 id="workers-for-platforms">Workers for Platforms</h4>
- `ScriptUpdateResponse`: new fields `entry_point`, `observability`, `tag`, `tags`
- `placement` field now union of 4 variants (smart mode, region, hostname, host)
- `tags`, `tail_consumers` now nullable
- `TagUpdateParams.body` now accepts `null`
<h4 id="workflows">Workflows</h4>
- `instance_retention`: `unknown` → typed `InstanceRetention` interface with `error_retention`, `success_retention`
- New status option: `'restart'` added to `StatusEditParams.status`
<h4 id="zero-trust-devices">Zero-Trust Devices</h4>
- External emergency disconnect settings (4 new fields)
- `antivirus` device posture check type
- `os_version_extra` documentation improvements
<h4 id="zones">Zones</h4>
- New response types: `SubscriptionCreateResponse`, `SubscriptionUpdateResponse`, `SubscriptionGetResponse`
<h4 id="zero-trust-access-applications">Zero-Trust Access Applications</h4>
- New `ApplicationType` values: `'mcp'`, `'mcp_portal'`, `'proxy_endpoint'`
- New destination type: `ViaMcpServerPortalDestination` for MCP server access
<h4 id="zero-trust-gateway">Zero-Trust Gateway</h4>
- Added `rules.listTenant()` method
<h4 id="zero-trust-gateway-proxy-endpoints">Zero-Trust Gateway - Proxy Endpoints</h4>
- `ProxyEndpoint`: interface → discriminated union (`ZeroTrustGatewayProxyEndpointIP | ZeroTrustGatewayProxyEndpointIdentity`)
- `ProxyEndpointCreateParams`: interface → union type
- Added `kind` field: `'ip' | 'identity'`
<h4 id="zero-trust-tunnels-1">Zero-Trust Tunnels</h4>
- `WARPConnector*Response`: union type → interface
<hr />
<h4 id="deprecations">Deprecations</h4>
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
<h4 id="bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>mcp:</strong> correct code tool API endpoint (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/599703c45672dc899455d74b124018efd4b75095">599703c</a>)</li>
<li><strong>mcp:</strong> return correct lines on typescript errors (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/5d6f9998ed9999aaa95e1bda8cf50929f3555cf1">5d6f999</a>)</li>
<li><strong>organization_profile:</strong> fix bad reference (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/d84ea77094400055c06554812b84c2f0c8d00cc4">d84ea77</a>)</li>
<li><strong>schema_validation:</strong> correctly reflect model to openapi mapping (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/bb861516774b159d80e0f46a5f3abc5a4c9f9d49">bb86151</a>)</li>
<li><strong>workers:</strong> fix tests (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/2ee37f7adf5a4637d65f61fc225e135eec2579fc">2ee37f7</a>)</li>
</ul>
<hr />
<h4 id="documentation">Documentation</h4>
<ul>
<li>Added deprecation notices with migration paths</li>
<li><strong>api_gateway:</strong> deprecate API Shield Schema Validation resources (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/8a4b20f7a572422f74179fbdb4f1c4fb555e3e40">8a4b20f</a>)</li>
<li>Improved JSDoc examples across all resources</li>
<li><strong>workers:</strong> expose subdomain delete documentation (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/4f7cc1f2b8861a5b8abc193d287f78264a425062">4f7cc1f</a>)</li>
</ul>
</div></article></div>
