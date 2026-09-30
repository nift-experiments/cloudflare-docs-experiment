---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/go-sdk/
  description: '2026-04-30'
  full_title: go-sdk changelog | Cloudflare Docs
  head_html: <title>go-sdk changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-04-30"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/go-sdk/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="go-sdk changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-04-30"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/go-sdk/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/go-sdk/#page","headline":"go-sdk changelog | Cloudflare Docs","description":"2026-04-30","url":"https://developers.cloudflare.com/changelog/product/go-sdk/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/go-sdk/
  schema: 1
---
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



