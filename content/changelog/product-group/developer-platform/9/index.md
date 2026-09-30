---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/developer-platform/9/
  description: '2026-04-30'
  full_title: Developer platform changelog - page 9 | Cloudflare Docs
  head_html: <title>Developer platform changelog - page 9 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-04-30"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/developer-platform/9/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Developer platform changelog - page 9"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-04-30"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/developer-platform/9/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/9/#page","headline":"Developer platform changelog - page 9 | Cloudflare Docs","description":"2026-04-30","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/9/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/developer-platform/9/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="web-analytics-adds-navigation-type-filtering-and-reporting"><a href="/changelog/post/2026-04-30-rum-navigation-types/">Web Analytics adds Navigation Type filtering and reporting</a></h2>
<p><em>2026-04-30</em></p>
<p>Cloudflare Web Analytics now supports <strong>Navigation Type</strong> reporting and filtering.</p>
<p>This update allows developers and performance analysts to see how users are navigating between pages — whether through a link click or form submission, a page reload, or using the browser's back/forward buttons — and whether a browser cache hit occurred for these behaviors.</p>
<p>Understanding navigation types is critical for optimizing user experience. For example, if a high volume of your traffic consists of &quot;Back-forward&quot; navigations versus &quot;Back-forward Cache&quot;, those visitors are not benefiting from the Back/Forward Cache (bfcache) and therefore are experiencing higher load times due to potentially unnecessary network requests.</p>
<p>The same applies for regular &quot;Navigate&quot; entries — where &quot;Navigate Cache&quot;, &quot;Navigate Prefetch Cache&quot; and &quot;Prerender&quot; would provide instant document retrieval — and &quot;Reload&quot;, where &quot;Reload cache&quot; would be more optimal.</p>
<p>A high volume of &quot;Reload&quot; entries can also indicate a potential stability problem with your website.</p>
<p>By identifying these patterns, you can tune your browser caching strategies to ensure HTML documents are served instantaneously from local caches rather than requiring a roundtrip to the network.</p>
<p>For more information, refer to <a href="/web-analytics/data-metrics/dimensions/#navigation-types">Navigation Types</a>.</p>
<h4 id="2026-04-30-rum-navigation-types-key-benefits">Key benefits</h4>
<ul>
<li><strong>Monitor Cache Effectiveness:</strong> See how often your site is served from the HTTP cache or bfcache.</li>
<li><strong>Identify Performance Bottlenecks:</strong> Filter by the different types to understand performance opportunity of improving browser cache hit ratio.</li>
</ul>
<h4 id="2026-04-30-rum-navigation-types-analyze-navigation-types-in-the-cloudflare-dashboard">Analyze navigation types in the Cloudflare dashboard</h4>
<p>You can now find the <strong>Navigation Type</strong> dimension in the Web Analytics dashboard. You can filter to include/exclude one or more specific types using &quot;equals&quot;, &quot;does not equal&quot;, &quot;in&quot;, or &quot;not in&quot; matchers.</p>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-navigation-type-filter.png" alt="Navigation Type filter" /></p>
<p>To check the list of popular navigation types, select <strong>Page views</strong> on the Web Analytics sidebar and scroll down to the bottom:</p>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-navigation-types-list.png" alt="Navigation Types list in Page Views tab" /></p>


<h2 id="hyperdrive-support-for-private-databases-with-workers-vpc"><a href="/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/">Hyperdrive support for private databases with Workers VPC</a></h2>
<p><em>2026-04-29</em></p>
<p>You can now connect Hyperdrive to a private database through a <a href="/workers-vpc/">Workers VPC service</a>. This is the recommended way to connect Hyperdrive to a private database that is not exposed to the public Internet.</p>
<p>When creating a Hyperdrive configuration in the Cloudflare dashboard, choose <strong>Connect to private database</strong> and then <strong>Workers VPC</strong>. From there, you can select an existing VPC service or create a new one inline by picking a Cloudflare Tunnel and entering your origin host and TCP port.</p>
<p>You can also create a Hyperdrive configuration backed by a Workers VPC service from the command line:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler hyperdrive create my-vpc-database \&#10;  &#45;-service-id &lt;YOUR_VPC_SERVICE_ID&gt; \&#10;  &#45;-database &lt;DATABASE_NAME&gt; \&#10;  &#45;-user &lt;DATABASE_USER&gt; \&#10;  &#45;-password &lt;DATABASE_PASSWORD&gt; \&#10;  &#45;-scheme postgresql&#10;</code></pre>
<p>Workers VPC services are reusable across Hyperdrive configurations and can also be bound directly to Workers, so you can share the same private connection across multiple products.</p>
<p>To get started, refer to <a href="/hyperdrive/configuration/connect-to-private-database-vpc/">Connect Hyperdrive to a private database using Workers VPC</a>.</p>


<h2 id="realtime-backlog-metrics-now-available-for-queues"><a href="/changelog/post/2026-04-28-improved-queues-metrics/">Realtime backlog metrics now available for Queues</a></h2>
<p><em>2026-04-28</em></p>
<p><a href="/queues/">Queues</a>, Cloudflare's managed message queue, now exposes realtime backlog metrics via the dashboard, REST API, and JavaScript API. Three new fields are available:</p>
<ul>
<li><strong><code>backlog_count</code></strong> — the number of unacknowledged messages in the queue</li>
<li><strong><code>backlog_bytes</code></strong> — the total size of those messages in bytes</li>
<li><strong><code>oldest_message_timestamp_ms</code></strong> — the timestamp of the oldest unacknowledged message</li>
</ul>
<p>The following endpoints also now include a <code>metadata.metrics</code> object on the result field after successful message consumption:</p>
<ul>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages/pull</code></li>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages</code></li>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages/batch</code></li>
</ul>
<h4 id="2026-04-28-improved-queues-metrics-javascript-apis">Javascript APIs</h4>
<p>Call <code>env.QUEUE.metrics()</code> to get realtime backlog metrics:</p>
<pre tabindex="0"><code class="language-ts">const {&#10;	backlogCount, // number&#10;	backlogBytes, // number&#10;	oldestMessageTimestamp, // Date | undefined&#10;} = await env.QUEUE.metrics();&#10;</code></pre>
<p><code>env.QUEUE.send()</code> and <code>env.QUEUE.sendBatch()</code> also now return a metrics object on the response.</p>
<p>You can also query these fields via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> or view realtime backlog on the <a href="https://dash.cloudflare.com/?to=/:account/workers/queues">dashboard</a>.</p>
<p><img src="/assets/upstream/images/changelog/queues/2026-04-28-queues-metrics.png" alt="Queues realtime backlog" /></p>
<p>For more information, refer to <a href="/queues/observability/metrics/">Queues metrics</a>.</p>


<h2 id="terraform-v5-19-0-now-available"><a href="/changelog/post/2026-04-24-terraform-v5.19.0-provider/">Terraform v5.19.0 now available</a></h2>
<p><em>2026-04-24</em></p>
<p>Terraform Provider v5.19.0 introduces 14 new resources spanning AI Gateway, Pipelines, R2 Data Catalog, User Groups, Vulnerability Scanner, Workers Observability, and Zero Trust capabilities. This release significantly improves the v4 to v5 migration experience with automatic state upgraders for 26 resources, working seamlessly with the new <a href="https://github.com/cloudflare/tf-migrate">tf-migrate CLI tool</a> to automate resource renames, attribute updates, and <code>moved</code> block generation. Together, these enhancements reduce manual migration effort and minimize risk when upgrading from v4 to v5.</p>
<p><strong>Note:</strong> <code>cmd/migrate</code> is deprecated in favor of <code>tf-migrate</code> and will be removed in a future release (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/pull/7062">#7062</a>)</p>
<h4 id="2026-04-24-terraform-v5.19.0-provider-new-resources">New Resources</h4>
<ul>
<li><strong>cloudflare_ai_gateway</strong>: Manage AI Gateway instances</li>
<li><strong>cloudflare_certificate_authorities_hostname_associations</strong>: Manage mTLS certificate hostname associations</li>
<li><strong>cloudflare_custom_page_asset</strong>: Manage custom page assets</li>
<li><strong>cloudflare_pipeline</strong>: Manage Cloudflare Pipelines</li>
<li><strong>cloudflare_r2_data_catalog</strong>: Manage R2 Data Catalog</li>
<li><strong>cloudflare_user_group</strong>: Manage user groups</li>
<li><strong>cloudflare_user_group_members</strong>: Manage user group memberships</li>
<li><strong>cloudflare_vulnerability_scanner_credential</strong>: Manage vulnerability scanner credentials</li>
<li><strong>cloudflare_vulnerability_scanner_credential_set</strong>: Manage vulnerability scanner credential sets</li>
<li><strong>cloudflare_vulnerability_scanner_target_environment</strong>: Manage vulnerability scanner target environments</li>
<li><strong>cloudflare_workers_observability_destination</strong>: Manage Workers Observability destinations</li>
<li><strong>cloudflare_zero_trust_device_ip_profile</strong>: Manage Zero Trust device IP profiles</li>
<li><strong>cloudflare_zero_trust_device_subnet</strong>: Manage Zero Trust device subnets</li>
<li><strong>cloudflare_zero_trust_dlp_settings</strong>: Manage Zero Trust DLP settings</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-features">Features</h4>
<h4 id="2026-04-24-terraform-v5.19.0-provider-v4-to-v5-migration-state-upgraders">V4 to V5 Migration State Upgraders</h4>
<p>State upgraders added for seamless migration from v4 to v5 for the following resources:</p>
<ul>
<li>account</li>
<li>account_member</li>
<li>account_token</li>
<li>authenticated_origin_pulls</li>
<li>authenticated_origin_pulls_hostname_certificate</li>
<li>byo_ip_prefix</li>
<li>custom_hostname</li>
<li>custom_ssl</li>
<li>leaked_credential_check</li>
<li>leaked_credential_check_rule</li>
<li>logpush_ownership_challenge</li>
<li>mtls_certificate</li>
<li>observatory_scheduled_test</li>
<li>pages_domain</li>
<li>regional_tiered_cache</li>
<li>turnstile_widget</li>
<li>workers_custom_domain</li>
<li>zero_trust_device_custom_profile</li>
<li>zero_trust_device_default_profile</li>
<li>zero_trust_device_posture_integration</li>
<li>zero_trust_gateway_certificate</li>
<li>zero_trust_gateway_settings</li>
<li>zero_trust_organization</li>
<li>zero_trust_tunnel_cloudflared_virtual_network</li>
<li>zone_setting</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-other-features">Other Features</h4>
<ul>
<li><strong>ruleset</strong>: Add <code>content_converter</code> and <code>redirects_for_ai_training</code> support to configuration rules</li>
<li><strong>zero_trust_gateway_logging</strong>: Make importable</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-bug-fixes">Bug Fixes</h4>
<h4 id="2026-04-24-terraform-v5.19.0-provider-migration-state-management">Migration &amp; State Management</h4>
<ul>
<li><strong>account_member</strong>: Add UseStateForUnknown to status field to prevent drift</li>
<li><strong>authenticated_origin_pulls_settings</strong>: Fix no prior schema and no-op upgrade</li>
<li><strong>certificate_pack</strong>: Initialize empty lists instead of null in state upgrader to prevent drift</li>
<li><strong>migrations</strong>: Handle ambiguous schema_version state for v4/v5 coexistence</li>
<li><strong>zero_trust_access_policy</strong>: Fix nil pointer panic in state upgrader; set PriorSchema nil for v4 state upgrade</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-resource-specific-fixes">Resource-Specific Fixes</h4>
<ul>
<li><strong>ai_search_instance</strong>: Restore original defaults for cache and cache_threshold; conflict resolution</li>
<li><strong>apijson</strong>: Return empty object from MarshalForPatch when no fields are serializable</li>
<li><strong>dlp_predefined_profile</strong>: Eliminate perpetual entries and enabled_entries drift</li>
<li><strong>dns_record</strong>: Avoid unnecessary drift for ipv4_only and ipv6_only attributes; remove private_routing default value</li>
<li><strong>drift</strong>: Preserve prior state values for optional fields not returned by API</li>
<li><strong>healthcheck</strong>: Use buildHealthcheckPlanChecks helper for correct plan checks per migration source; update assertions</li>
<li><strong>leaked_credential_check_rule</strong>: Handle empty ID from v4 provider state migration</li>
<li><strong>list_item</strong>: Remove context</li>
<li><strong>logpush_job</strong>: Update model for migration</li>
<li><strong>ruleset</strong>: Fix migration; add redirects_for_ai_training to SourceV4ActionParametersModel; fix duplicate model attribute</li>
<li><strong>worker</strong>: Add UseStateForUnknown() plan modifiers and update tests for observability.traces</li>
<li><strong>workers_custom_domain</strong>: Handle HTTP 200 no content header; update assertions</li>
<li><strong>workers_script</strong>: Fix model drift</li>
<li><strong>zero_trust_access_identity_provider</strong>: Fix boolean drifts</li>
<li><strong>zero_trust_device_managed_networks</strong>: Upgrade resource state</li>
<li><strong>zero_trust_gateway_policy</strong>: Make filters Computed+Optional to prevent drift</li>
<li><strong>zero_trust_gateway_settings</strong>: Fix breaking changes; implement sweeper to reset account to clean defaults</li>
<li><strong>zone_setting</strong>: Migration test improvements and fixes</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-documentation">Documentation</h4>
<ul>
<li><strong>healthcheck</strong>: Update port description to clarify defaults</li>
<li>Add application-scoped access policy migration guidance</li>
<li>Update zone_settings_override migration guide for tf-migrate v2 workflow</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-for-more-information">For more information</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform Provider</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration">Version 5 Migration Guide</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="automate-migration-from-cloudflare-s-terraform-v4-to-v5-provider"><a href="/changelog/post/2026-04-24-tf-migrate-tool-released/">Automate migration from Cloudflare's Terraform v4 to v5 provider</a></h2>
<p><em>2026-04-24</em></p>
<p>We're excited to announce <strong>tf-migrate</strong>, a purpose-built CLI tool that simplifies migrating from Cloudflare Terraform Provider v4 to v5.</p>
<h4 id="2026-04-24-tf-migrate-tool-released-v5-is-stable-and-ready-for-production">v5 is stable and ready for production</h4>
<p><strong>Terraform Provider v5 is stable and actively receiving updates.</strong>  We encourage all users to migrate to v5 to take advantage of ongoing enhancements and new capabilities.</p>
<p>Cloudflare uses tf-migrate to migrate our own infrastructure — the same tool we're providing to the community — ensuring the best possible migration experience.</p>
<h4 id="2026-04-24-tf-migrate-tool-released-what-tf-migrate-does">What tf-migrate does</h4>
<p><strong>tf-migrate</strong> automates the tedious and error-prone parts of the v4 to v5 migration process:</p>
<ul>
<li><strong>Resource type renames</strong> – Automatically updates <code>cloudflare_record</code> → <code>cloudflare_dns_record</code>, <code>cloudflare_access_application</code> → <code>cloudflare_zero_trust_access_application</code>, and 40+ other renamed resources</li>
<li><strong>Attribute transformations</strong> – Updates field names (e.g., <code>value</code> → <code>content</code> for DNS records) and restructures nested blocks</li>
<li><strong>Moved block generation</strong> – Creates Terraform 1.8+ <code>moved</code> blocks to prevent resource replacements and ensure zero-downtime migrations</li>
<li><strong>Cross-file reference updates</strong> – Automatically finds and updates all references to renamed resources across your entire configuration</li>
<li><strong>Dry-run mode</strong> – Preview all changes before applying them to ensure safety</li>
</ul>
<p>Combined with the automatic state upgraders introduced in v5.19+, tf-migrate eliminates the manual work and risk that previously made v5 migrations challenging. Tf-migrate operates directly on the config, and the built-in state upgraders handle the rest.</p>
<h4 id="2026-04-24-tf-migrate-tool-released-supported-resources">Supported resources</h4>
<p>Tf-migrate currently supports the most common Terraform resources our customers use. We are actively working to expand coverage, with the most commonly used resources prioritized first.</p>
<p>For the complete list of supported resources and their migration status, refer to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">v5 Stabilization Tracker</a>. This list is updated regularly as additional resources are stabilized and migration support is added.</p>
<p>Resources not yet supported by tf-migrate will need to be migrated manually using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">version 5 upgrade guide</a>. The upgrade guide provides step-by-step instructions for handling resource renames, attribute changes, and state migrations.</p>
<h4 id="2026-04-24-tf-migrate-tool-released-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/tf-migrate/releases">Download tf-migrate</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration">Version 5 Migration Guide</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Terraform Provider documentation</a></li>
<li><a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">v5 Stabilization Tracker</a></li>
</ul>
<p>We have been releasing Betas over the past month and a half while testing this tool. See the full changelog of those Betas here: <a href="https://github.com/cloudflare/tf-migrate/releases">tf-migrate releases</a>.</p>


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


<h2 id="r2-data-catalog-snapshot-expiration-now-removes-unreferenced-data-files"><a href="/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/">R2 Data Catalog snapshot expiration now removes unreferenced data files</a></h2>
<p><em>2026-04-22</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a>, a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built into R2, now removes unreferenced data files during automatic snapshot expiration. This improvement reduces storage costs and eliminates the need to run manual maintenance jobs to reclaim space from deleted data.</p>
<p>Previously, snapshot expiration only cleaned up Iceberg metadata files such as manifests and manifest lists. Data files that were no longer referenced by active snapshots remained in R2 storage until you manually ran <code>remove_orphan_files</code> or <code>expire_snapshots</code> through an engine like Spark. This required extra operational overhead and left stale data files consuming storage.</p>
<p>Snapshot expiration now handles both metadata and data file cleanup automatically. When a snapshot is expired, any data files that are no longer referenced by retained snapshots are removed from R2 storage.</p>
<pre tabindex="0"><code class="language-bash">&#35; Enable catalog-level snapshot expiration&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;</code></pre>
<p>For more information, refer to the <a href="/r2-data-catalog/table-maintenance/">table maintenance documentation</a>.</p>


<h2 id="additional-step-context-and-readablestream-support-now-available-in-workflows-step-do"><a href="/changelog/post/2026-04-21-step-context-and-readable-streams/">Additional step context and ReadableStream support now available in Workflows step.do()</a></h2>
<p><em>2026-04-21 12:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> now provides additional context inside <code>step.do()</code> callbacks and supports returning <code>ReadableStream</code> to handle larger step outputs.</p>
<h4 id="2026-04-21-step-context-and-readable-streams-step-context-properties">Step context properties</h4>
<p>The <code>step.do()</code> callback receives a context object with new properties <a href="/changelog/post/2026-03-06-step-context-available/">alongside</a> <code>attempt</code>:</p>
<ul>
<li><strong><code>step.name</code></strong> — The name passed to <code>step.do()</code></li>
<li><strong><code>step.count</code></strong> — How many times a step with that name has been invoked in this instance (1-indexed)
<ul>
<li>Useful when running the same step in a loop.</li>
</ul>
</li>
<li><strong><code>config</code></strong> — The resolved step configuration, including <code>timeout</code> and <code>retries</code> with defaults applied</li>
</ul>
<pre tabindex="0"><code class="language-ts">type ResolvedStepConfig = {&#10;	retries: {&#10;		limit: number;&#10;		delay: WorkflowDelayDuration | number;&#10;		backoff?: &quot;constant&quot; | &quot;linear&quot; | &quot;exponential&quot;;&#10;	};&#10;	timeout: WorkflowTimeoutDuration | number;&#10;};&#10;&#10;type WorkflowStepContext = {&#10;	step: {&#10;		name: string;&#10;		count: number;&#10;	};&#10;	attempt: number;&#10;	config: ResolvedStepConfig;&#10;};&#10;</code></pre>
<h4 id="2026-04-21-step-context-and-readable-streams-readablestream-support-in-step-do">ReadableStream support in <code>step.do()</code></h4>
<p>Steps can now return a <code>ReadableStream</code> directly. Although non-stream step outputs are <a href="/workflows/reference/limits/">limited to 1 MiB</a>, streamed outputs support much larger payloads.</p>
<pre tabindex="0"><code class="language-ts">const largePayload = await step.do(&quot;fetch-large-file&quot;, async () =&gt; {&#10;	const object = await env.MY_BUCKET.get(&quot;large-file.bin&quot;);&#10;	return object.body;&#10;});&#10;</code></pre>
<p>Note that streamed outputs are still considered part of the Workflow instance storage limit.</p>


<h2 id="container-logs-page-now-includes-relevant-worker-and-durable-object-logs"><a href="/changelog/post/2026-04-21-correlated-worker-durable-object-logs/">Container logs page now includes relevant Worker and Durable Object logs</a></h2>
<p><em>2026-04-21</em></p>
<p>The Container logs page now displays related <a href="/workers/">Worker</a> and <a href="/durable-objects/">Durable Object</a> logs alongside container logs. This co-locates all relevant log events for a container application in one place, making it easier to trace requests and debug issues.</p>
<p><img src="/assets/upstream/images/containers/container-worker-logs.png" alt="Container logs page showing Worker and Durable Object logs alongside container logs" /></p>
<p>You can filter to a single source when you need to isolate Container, Worker, or Durable Object output.</p>
<p>For information on configuring container logging, refer to <a href="/containers/faq/#how-do-container-logs-work">How do Container logs work?</a>.</p>


<h2 id="introducing-billable-usage-dashboard-and-budget-alerts"><a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Introducing Billable Usage dashboard and Budget alerts</a></h2>
<p><em>2026-04-21</em></p>
<p>Pay-as-you-go customers can now monitor usage-based costs and configure spend alerts through two new features: the Billable Usage dashboard and Budget alerts.</p>
<h4 id="2026-04-13-billable-usage-dashboard-and-budget-alerts-billable-usage-dashboard">Billable Usage dashboard</h4>
<p>The Billable Usage dashboard provides daily visibility into usage-based costs across your Cloudflare account. The data comes from the same system that generates your monthly invoice, so the figures match your bill.</p>
<p>The dashboard displays:</p>
<ul>
<li>A bar chart showing daily usage charges for your billing period</li>
<li>A sortable table breaking down usage by product, including total usage, billable usage, and cumulative costs</li>
<li>Ability to view previous billing periods</li>
</ul>
<p>Usage data aligns to your billing cycle, not the calendar month. The total usage cost shown at the end of a completed billing period matches the usage overage charges on your corresponding invoice.</p>
<p>To access the dashboard, go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-13-billable-usage-dashboard.png" alt="Screenshot of the Billable Usage dashboard in the Cloudflare dashboard" /></p>
<h4 id="2026-04-13-billable-usage-dashboard-and-budget-alerts-budget-alerts">Budget alerts</h4>
<p>Budget alerts allow you to set dollar-based thresholds for your account-level usage spend. You receive an email notification when your projected monthly spend reaches your configured threshold, giving you proactive visibility into your bill before month-end.</p>
<p>To configure a budget alert:</p>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</li>
<li>Select <strong>Set Budget Alert</strong>.</li>
<li>Enter a budget threshold amount greater than $0.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<p>Alternatively, configure alerts via <strong>Notifications</strong> &gt; <strong>Add</strong> &gt; <strong>Budget Alert</strong>.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-13-budget-alert-modal.png" alt="Create Budget Alert modal in the Cloudflare dashboard" /></p>
<p>You can create multiple budget alerts at different dollar amounts. The notifications system automatically deduplicates alerts if multiple thresholds trigger at the same time. Budget alerts are calculated daily based on your usage trends and fire once per billing cycle when your projected spend first crosses your threshold.</p>
<p>Both features are available to Pay-as-you-go accounts with usage-based products (Workers, R2, Images, etc.). Enterprise contract accounts are not supported.</p>
<p>For more information, refer to the <a href="/billing/understand/usage-based-billing/">Usage based billing documentation</a>.</p>


<h2 id="websocket-binary-messages-now-delivered-as-blob-by-default"><a href="/changelog/post/2026-04-21-websocket-standard-binary-type/">WebSocket binary messages now delivered as Blob by default</a></h2>
<p><em>2026-04-21</em></p>
<p>Binary frames received on a <code>WebSocket</code> are now delivered to the <code>message</code> event as <a href="https://developer.mozilla.org/en-US/docs/Web/API/Blob"><code>Blob</code></a> objects by default. This matches the <a href="https://websockets.spec.whatwg.org/">WebSocket specification</a> and standard browser behavior. Previously, binary frames were always delivered as <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer"><code>ArrayBuffer</code></a>. The <a href="/workers/runtime-apis/websockets/#binarytype"><code>binaryType</code></a> property on <code>WebSocket</code> controls the delivery type on a per-WebSocket basis.</p>
<p>This change has been active for Workers with compatibility dates on or after <code>2026-03-17</code>, via the <a href="/workers/configuration/compatibility-flags/#websocket-standard-binary-type"><code>websocket_standard_binary_type</code></a> compatibility flag. We should have documented this change when it shipped but didn't. We're sorry for the trouble that caused. If your Worker handles binary WebSocket messages and assumes <code>event.data</code> is an <code>ArrayBuffer</code>, the frames will arrive as <code>Blob</code> instead, and a naive <code>instanceof ArrayBuffer</code> check will silently drop every frame.</p>
<p>To opt back into <code>ArrayBuffer</code> delivery, assign <code>binaryType</code> before calling <code>accept()</code>. This works regardless of the compatibility flag:</p>
<pre tabindex="0"><code class="language-js">const resp = await fetch(&quot;https://example.com&quot;, {&#10;	headers: { Upgrade: &quot;websocket&quot; },&#10;});&#10;const ws = resp.webSocket;&#10;&#10;// Opt back into ArrayBuffer delivery for this WebSocket.&#10;ws.binaryType = &quot;arraybuffer&quot;;&#10;ws.accept();&#10;&#10;ws.addEventListener(&quot;message&quot;, (event) =&gt; {&#10;	if (typeof event.data === &quot;string&quot;) {&#10;		// Text frame.&#10;	} else {&#10;		// event.data is an ArrayBuffer because we set binaryType above.&#10;	}&#10;});&#10;</code></pre>
<p>If you are not ready to migrate and want to keep <code>ArrayBuffer</code> as the default for all WebSockets in your Worker, add the <code>no_websocket_standard_binary_type</code> flag to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>This change has no effect on the Durable Object hibernatable WebSocket <a href="/durable-objects/best-practices/websockets/"><code>webSocketMessage</code></a> handler, which continues to receive binary data as <code>ArrayBuffer</code>.</p>
<p>For more information, refer to <a href="/workers/runtime-apis/websockets/#binary-messages">WebSockets binary messages</a>.</p>


<h2 id="cloudflare-pipelines-as-a-logpush-destination"><a href="/changelog/post/2026-04-20-pipelines-logpush-destination/">Cloudflare Pipelines as a Logpush destination</a></h2>
<p><em>2026-04-20</em></p>
<p>Logpush has traditionally been great at delivering Cloudflare logs to a variety of destinations in JSON format. While JSON is flexible and easily readable, it can be inefficient to store and query at scale.</p>
<p>With this release, you can now send your logs directly to <a href="/pipelines/">Pipelines</a> to ingest, transform, and store your logs in <a href="/r2/">R2</a> as Parquet files or Apache Iceberg tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>. This makes the data footprint more compact and more efficient at querying your logs instantly with <a href="/r2-sql/">R2 SQL</a> or any other query engine that supports Apache Iceberg or Parquet.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-transform-logs-before-storage">Transform logs before storage</h4>
<p>Pipelines SQL runs on each log record in-flight, so you can reshape your data before it is written. For example, you can drop noisy fields, redact sensitive values, or derive new columns:</p>
<pre tabindex="0"><code class="language-sql">INSERT INTO http_logs_sink&#10;SELECT&#10;  ClientIP,&#10;  EdgeResponseStatus,&#10;  to_timestamp_micros(EdgeStartTimestamp) AS event_time,&#10;  upper(ClientRequestMethod) AS method,&#10;  sha256(ClientIP) AS hashed_ip&#10;FROM http_logs_stream&#10;WHERE EdgeResponseStatus &gt;= 400;&#10;</code></pre>
<p>Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the <a href="/pipelines/sql-reference/">Pipelines SQL reference</a>.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-get-started">Get started</h4>
<p>To configure Pipelines as a Logpush destination, refer to <a href="/logs/logpush/logpush-job/enable-destinations/pipelines/">Enable Cloudflare Pipelines</a>.</p>


<h2 id="r2-sql-adds-json-functions-explain-format-json-and-unpartitioned-table-support"><a href="/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/">R2 SQL adds JSON functions, EXPLAIN FORMAT JSON, and unpartitioned table support</a></h2>
<p><em>2026-04-20</em></p>
<p><a href="/r2-sql/">R2 SQL</a> is Cloudflare's serverless, distributed, analytics query engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<p>R2 SQL now supports functions for querying JSON data stored in Apache Iceberg tables, an easier way to parse query plans with <code>EXPLAIN FORMAT JSON</code>, and querying tables without partition keys stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<p>JSON functions extract and manipulate JSON values directly in SQL without client-side processing:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;  json_get_str(doc, &#x27;name&#x27;) AS name,&#10;  json_get_int(doc, &#x27;user&#x27;, &#x27;profile&#x27;, &#x27;level&#x27;) AS level,&#10;  json_get_bool(doc, &#x27;active&#x27;) AS is_active&#10;FROM my_namespace.sales_data&#10;WHERE json_contains(doc, &#x27;email&#x27;)&#10;</code></pre>
<p>For a full list of available functions, refer to <a href="/r2-sql/sql-reference/scalar-functions/#json-functions">JSON functions</a>.</p>
<p><code>EXPLAIN FORMAT JSON</code> returns query execution plans as structured JSON for programmatic analysis and observability integrations:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 sql query &quot;${WAREHOUSE}&quot; &quot;EXPLAIN FORMAT JSON SELECT * FROM logpush.requests LIMIT 10;&quot;&#10;&#10;┌──────────────────────────────────────┐&#10;│ plan                                 │&#10;├──────────────────────────────────────┤&#10;│ {                                    │&#10;│   &quot;name&quot;: &quot;CoalescePartitionsExec&quot;,  │&#10;│   &quot;output_partitions&quot;: 1,            │&#10;│   &quot;rows&quot;: 10,                        │&#10;│   &quot;size_approx&quot;: &quot;310B&quot;,             │&#10;│   &quot;children&quot;: [                      │&#10;│     {                                │&#10;│       &quot;name&quot;: &quot;DataSourceExec&quot;,      │&#10;│       &quot;output_partitions&quot;: 4,        │&#10;│       &quot;rows&quot;: 28951,                 │&#10;│       &quot;size_approx&quot;: &quot;900.0KB&quot;,      │&#10;│       &quot;table&quot;: &quot;logpush.requests&quot;,   │&#10;│       &quot;files&quot;: 7,                    │&#10;│       &quot;bytes&quot;: 900019,               │&#10;│       &quot;projection&quot;: [                │&#10;│         &quot;__ingest_ts&quot;,               │&#10;│         &quot;CPUTimeMs&quot;,                 │&#10;│         &quot;DispatchNamespace&quot;,         │&#10;│         &quot;Entrypoint&quot;,                │&#10;│         &quot;Event&quot;,                     │&#10;│         &quot;EventTimestampMs&quot;,          │&#10;│         &quot;EventType&quot;,                 │&#10;│         &quot;Exceptions&quot;,                │&#10;│         &quot;Logs&quot;,                      │&#10;│         &quot;Outcome&quot;,                   │&#10;│         &quot;ScriptName&quot;,                │&#10;│         &quot;ScriptTags&quot;,                │&#10;│         &quot;ScriptVersion&quot;,             │&#10;│         &quot;WallTimeMs&quot;                 │&#10;│       ],                             │&#10;│       &quot;limit&quot;: 10                    │&#10;│     }                                │&#10;│   ]                                  │&#10;│ }                                    │&#10;└──────────────────────────────────────┘&#10;</code></pre>
<p>For more details, refer to <a href="/r2-sql/sql-reference/#explain">EXPLAIN</a>.</p>
<p>Unpartitioned Iceberg tables can now be queried directly, which is useful for smaller datasets or data without natural time dimensions. For tables with more than 1000 files, partitioning is still recommended for better performance.</p>
<p>Refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a> for the latest guidance on using R2 SQL.</p>


<h2 id="moonshot-ai-kimi-k2-6-now-available-on-workers-ai"><a href="/changelog/post/2026-04-20-kimi-k2-6-workers-ai/">Moonshot AI Kimi K2.6 now available on Workers AI</a></h2>
<p><em>2026-04-20</em></p>
<p><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> is now available on Workers AI, in partnership with Moonshot AI for Day 0 support. Kimi K2.6 is a native multimodal agentic model from Moonshot AI that advances practical capabilities in long-horizon coding, coding-driven design, proactive autonomous execution, and swarm-based task orchestration.</p>
<p>Built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token, Kimi K2.6 delivers frontier-scale intelligence with efficient inference. It scores competitively against GPT-5.4 and Claude Opus 4.6 on agentic and coding benchmarks, including BrowseComp (83.2), SWE-Bench Verified (80.2), and Terminal-Bench 2.0 (66.7).</p>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with significant improvements on complex, end-to-end coding tasks across languages including Rust, Go, and Python</li>
<li><strong>Coding-driven design</strong> that transforms simple prompts and visual inputs into production-ready interfaces and full-stack workflows</li>
<li><strong>Agent swarm orchestration</strong> scaling horizontally to 300 sub-agents executing 4,000 coordinated steps for complex autonomous tasks</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth</li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
</ul>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-differences-from-kimi-k2-5">Differences from Kimi K2.5</h4>
<p>If you are migrating from Kimi K2.5, note the following API changes:</p>
<ul>
<li>K2.6 uses <code>chat_template_kwargs.thinking</code> to control reasoning, replacing <code>chat_template_kwargs.enable_thinking</code></li>
<li>K2.6 returns reasoning content in the <code>reasoning</code> field, replacing <code>reasoning_content</code></li>
</ul>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.6 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.6/">Kimi K2.6 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="ai-search-instances-now-include-built-in-storage-and-namespace-workers-bindings"><a href="/changelog/post/2026-04-16-ai-search-namespace-binding/">AI Search instances now include built-in storage and namespace Workers Bindings</a></h2>
<p><em>2026-04-16T12:00:00+00:00</em></p>
<p>New <a href="/ai-search/">AI Search</a> instances created after today will work differently. New instances come with built-in storage and a vector index, so you can upload a file, have it indexed immediately, and search it right away.</p>
<p>Additionally new Workers Bindings are now available to use with AI Search. The new namespace binding lets you create and manage instances at runtime, and cross-instance search API lets you query across multiple instances in one call.</p>
<h4 id="2026-04-16-ai-search-namespace-binding-built-in-storage-and-vector-index">Built-in storage and vector index</h4>
<p>All new instances now comes with built-in storage which allows you to upload files directly to it using the <a href="/ai-search/api/items/workers-binding/">Items API</a> or the dashboard. No R2 buckets to set up, no external data sources to connect first.</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;// upload and wait for indexing to complete&#10;const item = await instance.items.uploadAndPoll(&quot;faq.md&quot;, content);&#10;&#10;// search immediately after indexing&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;onboarding guide&quot; }],&#10;});&#10;</code></pre>
<h4 id="2026-04-16-ai-search-namespace-binding-namespace-binding">Namespace binding</h4>
<p>The new <code>ai_search_namespaces</code> binding replaces the previous <code>env.AI.autorag()</code> API provided through the <code>AI</code> binding. It gives your Worker access to all instances within a <a href="/ai-search/concepts/namespaces/">namespace</a> and lets you create, update, and delete instances at runtime without redeploying.</p>
<pre tabindex="0"><code class="language-jsonc">// wrangler.jsonc&#10;{&#10;	&quot;ai_search_namespaces&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;AI_SEARCH&quot;,&#10;			&quot;namespace&quot;: &quot;default&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-ts">// create an instance at runtime&#10;const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;});&#10;</code></pre>
<p>For migration details, refer to <a href="/ai-search/api/migration/workers-binding/">Workers binding migration</a>. For more on namespaces, refer to <a href="/ai-search/concepts/namespaces/">Namespaces</a>.</p>
<h4 id="2026-04-16-ai-search-namespace-binding-cross-instance-search">Cross-instance search</h4>
<p>Within the new AI Search binding, you now have access to a Search and Chat API on the namespace level. Pass an array of instance IDs and get one ranked list of results back.</p>
<pre tabindex="0"><code class="language-ts">const results = await env.AI_SEARCH.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		instance_ids: [&quot;product-docs&quot;, &quot;customer-abc123&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/api/search/workers-binding/#namespace-level">Namespace-level search</a> for details.</p>


<h2 id="ai-search-now-has-hybrid-search-and-relevance-boosting"><a href="/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/">AI Search now has hybrid search and relevance boosting</a></h2>
<p><em>2026-04-16T12:00:00+00:00</em></p>
<p><a href="/ai-search/">AI Search</a> now supports hybrid search and relevance boosting, giving you more control over how results are found and ranked.</p>
<h4 id="2026-04-16-hybrid-search-and-relevance-boosting-hybrid-search">Hybrid search</h4>
<p>Hybrid search combines vector (semantic) search with BM25 keyword search in a single query. Vector search finds chunks with similar meaning, even when the exact words differ. Keyword search matches chunks that contain your query terms exactly. When you enable hybrid search, both run in parallel and the results are fused into a single ranked list.</p>
<p>You can configure the tokenizer (<code>porter</code> for natural language, <code>trigram</code> for code), keyword match mode (<code>and</code> for precision, <code>or</code> for recall), and fusion method (<code>rrf</code> or <code>max</code>) per instance:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;	index_method: { vector: true, keyword: true },&#10;	fusion_method: &quot;rrf&quot;,&#10;	indexing_options: { keyword_tokenizer: &quot;porter&quot; },&#10;	retrieval_options: { keyword_match_mode: &quot;and&quot; },&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/concepts/search-modes/">Search modes</a> for an overview and <a href="/ai-search/configuration/indexing/hybrid-search/">Hybrid search</a> for configuration details.</p>
<h4 id="2026-04-16-hybrid-search-and-relevance-boosting-relevance-boosting">Relevance boosting</h4>
<p>Relevance boosting lets you nudge search rankings based on document metadata. For example, you can prioritize recent documents by boosting on <code>timestamp</code>, or surface high-priority content by boosting on a custom metadata field like <code>priority</code>.</p>
<p>Configure up to 3 boost fields per instance or override them per request:</p>
<pre tabindex="0"><code class="language-ts">const results = await env.AI_SEARCH.get(&quot;my-instance&quot;).search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;deployment guide&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			boost_by: [&#10;				{ field: &quot;timestamp&quot;, direction: &quot;desc&quot; },&#10;				{ field: &quot;priority&quot;, direction: &quot;desc&quot; },&#10;			],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/configuration/retrieval/boosting/">Relevance boosting</a> for configuration details.</p>


<h2 id="artifacts-now-in-beta-versioned-filesystem-with-git-access"><a href="/changelog/post/2026-04-16-artifacts-now-in-beta/">Artifacts now in beta: versioned filesystem with Git access</a></h2>
<p><em>2026-04-16</em></p>
<p><a href="/artifacts/">Artifacts</a> is now in private beta. Artifacts is Git-compatible storage built for scale: create tens of millions of repos, fork from any remote, and hand off a URL to any Git client. It provides a versioned filesystem for storing and exchanging file trees across Workers, the REST API, and any Git client, running locally or within an agent.</p>
<p>You can <a href="https://blog.cloudflare.com/artifacts-git-for-agents-beta/">read the announcement blog</a> to learn more about what Artifacts does, how it works, and how to create repositories for your agents to use.</p>
<p>Artifacts has three API surfaces:</p>
<ul>
<li>Workers bindings (for creating and managing repositories)</li>
<li>REST API (for creating and managing repos from any other compute platform)</li>
<li>Git protocol (for interacting with repos)</li>
</ul>
<p>As an example: you can use the Workers binding to create a repo and read back its remote URL:</p>
<pre tabindex="0"><code class="language-ts">&#35; Create a thousand, a million or ten million repos: one for every agent, for every upstream branch, or every user.&#10;const created = await env.PROD_ARTIFACTS.create(&quot;agent-007&quot;);&#10;const remote = (await created.repo.info())?.remote;&#10;</code></pre>
<p>Or, use the REST API to create a repo inside a namespace from your agent(s) running on any platform:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST &quot;https://artifacts.cloudflare.net/v1/api/namespaces/some-namespace/repos&quot; --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; --header &quot;Content-Type: application/json&quot; --data &#x27;{&quot;name&quot;:&quot;agent-007&quot;}&#x27;&#10;</code></pre>
<p>Any Git client that speaks smart HTTP can use the returned remote URL:</p>
<pre tabindex="0"><code class="language-bash">&#35; Agents know git.&#10;&#35; Every repository can act as a git repo, allowing agents to interact with Artifacts the way they know best: using the git CLI.&#10;git clone https://x:${REPO_TOKEN}@artifacts.cloudflare.net/some-namespace/agent-007.git&#10;</code></pre>
<p>To learn more, refer to <a href="/artifacts/get-started/">Get started</a>, <a href="/artifacts/api/workers-binding/">Workers binding</a>, and <a href="/artifacts/api/git-protocol/">Git protocol</a>.</p>


<h2 id="email-sending-now-in-public-beta"><a href="/changelog/post/2026-04-16-email-sending-public-beta/">Email Sending now in public beta</a></h2>
<p><em>2026-04-16</em></p>
<p><strong><a href="/email-service/api/send-emails/">Email Sending</a></strong> is now in public beta. Send transactional emails directly from Workers (<code>env.EMAIL.send()</code>) or the REST API, with support for HTML, plain text, attachments, inline images, and custom headers. Email Sending joins <a href="https://blog.cloudflare.com/introducing-email-routing/">Email Routing</a> under the new <strong>Cloudflare Email Service</strong> — a single service for sending and receiving email on the Cloudflare developer platform.</p>
<p>Send an email from a Worker in a few lines of code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17722.md")</div>
<p>Email Service also integrates with the <a href="/agents/">Agents SDK</a>, giving your agents a native <code>onEmail</code> hook to receive, process, and reply to emails. Combined with the new <a href="https://github.com/cloudflare/mcp-server-cloudflare">Email MCP server</a> and Wrangler CLI email commands, any agent can send email regardless of where it runs.</p>
<p>Start sending and receiving emails from Workers and agents today. Email Sending is available on the Workers paid plan. Refer to the <a href="/email-service/">Email Service documentation</a> to get started.</p>


<h2 id="browser-rendering-is-now-browser-run"><a href="/changelog/post/2026-04-15-br-rename/">Browser Rendering is now Browser Run</a></h2>
<p><em>2026-04-15T12:00:00+00:00</em></p>
<p>We are renaming Browser Rendering to <strong><a href="/browser-run/">Browser Run</a></strong>. The name Browser Rendering never fully captured what the product does. Browser Run lets you run full browser sessions on Cloudflare's global network, drive them with code or AI, record and replay sessions, crawl pages for content, debug in real time, and let humans intervene when your agent needs help.</p>
<p>Along with the rename, we have increased limits for Workers Paid plans and redesigned the Browser Run dashboard.</p>
<p>We have 4x-ed concurrency limits for Workers Paid plan users:</p>
<ul>
<li><strong>Concurrent browsers per account</strong>: 30 → <strong>120 per account</strong></li>
<li><strong>New browser instances</strong>: 30 per minute → <strong>1 per second</strong></li>
<li><strong>REST API rate limits</strong>: recently increased from <a href="/changelog/post/2026-03-04-br-rest-api-limit-increase/">3 to 10 requests per second</a></li>
</ul>
<p>Rate limits across the <a href="/browser-run/limits/">limits page</a> are now expressed in per-second terms, matching how they are enforced. No action is needed to benefit from the higher limits.</p>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/workers/browser-run">redesigned dashboard</a> now shows every request in a single Runs tab, not just browser sessions but also quick actions like screenshots, PDFs, markdown, and crawls. Filter by endpoint, view target URLs, status, and duration, and expand any row for more detail.</p>
<p><img src="/images/browser-run/BRdashboardredesign.png" alt="Browser Run dashboard Runs tab with browser sessions and quick actions visible in one list, and an expanded crawl job showing its progress" /></p>
<p>We are also shipping several new features:</p>
<ul>
<li><strong><a href="/changelog/post/2026-04-15-br-observability/">Live View, Human in the Loop, and Session Recordings</a></strong> - See what your agent is doing in real time, let humans step in when automation hits a wall, and replay any session after it ends.</li>
<li><strong><a href="/changelog/post/2026-04-15-br-webmcp/">WebMCP</a></strong> - Websites can expose structured tools for AI agents to discover and call directly, replacing slow screenshot-analyze-click loops.</li>
</ul>
<p>For the full story, read our Agents Week blog <a href="https://blog.cloudflare.com/browser-run-for-ai-agents">Browser Run: Give your agents a browser</a>.</p>


<h2 id="browser-run-adds-live-view-human-in-the-loop-and-session-recordings"><a href="/changelog/post/2026-04-15-br-observability/">Browser Run adds Live View, Human in the Loop, and Session Recordings</a></h2>
<p><em>2026-04-15T11:00:00+00:00</em></p>
<p>When browser automation fails or behaves unexpectedly, it can be hard to understand what happened. We are shipping three new features in <a href="/browser-run/">Browser Run</a> (formerly Browser Rendering) to help:</p>
<ul>
<li><strong><a href="/browser-run/features/live-view/">Live View</a></strong> for real-time visibility</li>
<li><strong><a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a></strong> for human intervention</li>
<li><strong><a href="/browser-run/features/session-recording/">Session Recordings</a></strong> for replaying sessions after they end</li>
</ul>
<h4 id="2026-04-15-br-observability-live-view">Live View</h4>
<p><a href="/browser-run/features/live-view/">Live View</a> lets you see what your agent is doing in real time. The page, DOM, console, and network requests are all visible for any active browser session. Access Live View from the Cloudflare dashboard, via the hosted UI at <code>live.browser.run</code>, or using native Chrome DevTools.</p>
<h4 id="2026-04-15-br-observability-human-in-the-loop">Human in the Loop</h4>
<p>When your agent hits a snag like a login page or unexpected edge case, it can hand off to a human instead of failing. With <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>, a human steps into the live browser session through Live View, resolves the issue, and hands control back to the script.</p>
<p>Today, you can step in by opening the Live View URL for any active session. Next, we are adding a handoff flow where the agent can signal that it needs help, notify a human to step in, then hand control back to the agent once the issue is resolved.</p>
<p><img src="/images/browser-run/liveview.gif" alt="Browser Run Human in the Loop demo where an AI agent searches Amazon, selects a product, and requests human help when authentication is needed to buy" /></p>
<h4 id="2026-04-15-br-observability-session-recordings">Session Recordings</h4>
<p><a href="/browser-run/features/session-recording/">Session Recordings</a> records DOM state so you can replay any session after it ends. Enable recordings by passing <code>recording: true</code> when launching a browser. After the session closes, view the recording in the Cloudflare dashboard under <strong>Browser Run</strong> &gt; <strong>Runs</strong>, or retrieve via API using the session ID. Next, we are adding the ability to inspect DOM state and console output at any point during the recording.</p>
<p><img src="/images/browser-run/sessionrecording.gif" alt="Browser Run session recording showing an automated browser navigating the Sentry Shop and adding a bomber jacket to the cart" /></p>
<p>To get started, refer to the documentation for <a href="/browser-run/features/live-view/">Live View</a>, <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>, and <a href="/browser-run/features/session-recording/">Session Recording</a>.</p>


<h2 id="browser-run-adds-webmcp-support"><a href="/changelog/post/2026-04-15-br-webmcp/">Browser Run adds WebMCP support</a></h2>
<p><em>2026-04-15T10:00:00+00:00</em></p>
<p><a href="/browser-run/">Browser Run</a> (formerly Browser Rendering) now supports <a href="https://webmachinelearning.github.io/webmcp/">WebMCP</a> (Web Model Context Protocol), a new browser API from the Google Chrome team.</p>
<p>The Internet was built for humans, so navigating as an AI agent today is unreliable. WebMCP lets websites expose structured tools for AI agents to discover and call directly. Instead of slow screenshot-analyze-click loops, agents can call website functions like <code>searchFlights()</code> or <code>bookTicket()</code> with typed parameters, making browser automation faster, more reliable, and less fragile.</p>
<p><img src="/images/browser-run/webMCP.gif" alt="Browser Run lab session showing WebMCP tools being discovered and executed in the Chrome DevTools console to book a hotel" /></p>
<p>With WebMCP, you can:</p>
<ul>
<li><strong>Discover website tools</strong> - Use <code>navigator.modelContextTesting.listTools()</code> to see available actions on any WebMCP-enabled site</li>
<li><strong>Execute tools directly</strong> - Call <code>navigator.modelContextTesting.executeTool()</code> with typed parameters</li>
<li><strong>Handle human-in-the-loop interactions</strong> - Some tools pause for user confirmation before completing sensitive actions</li>
</ul>
<p>WebMCP requires Chrome beta features. We have an experimental pool with browser instances running Chrome beta so you can test emerging browser features before they reach stable Chrome. To start a WebMCP session, add <code>lab=true</code> to your <code>/devtools/browser</code> request:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/devtools/browser?lab=true&amp;keep_alive=300000&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot;&#10;</code></pre>
<p>Combined with the recently launched <a href="/browser-run/cdp/">CDP endpoint</a>, AI agents can also use WebMCP. Connect an <a href="/browser-run/cdp/mcp-clients/">MCP client</a> to Browser Run via CDP, and your agent can discover and call website tools directly. Here's the same hotel booking demo, this time driven by an AI agent through OpenCode:</p>
<p><img src="/images/browser-run/webMCPagent.gif" alt="Browser Run Live View showing an AI agent navigating a hotel booking site in real time" /></p>
<p>For a step-by-step guide, refer to the <a href="/browser-run/features/webmcp/">WebMCP documentation</a>.</p>


<h2 id="increased-concurrency-creation-rate-and-queued-instance-limits-for-workflows-instances"><a href="/changelog/post/2026-04-15-workflows-limits-raised/">Increased concurrency, creation rate, and queued instance limits for Workflows instances</a></h2>
<p><em>2026-04-15 13:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> limits have been raised to the following:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous</th>
<th>New</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concurrent instances (running in parallel)</td>
<td>10,000</td>
<td>50,000</td>
</tr>
<tr>
<td>Instance creation rate (per account)</td>
<td>100/second per account</td>
<td>300/second per account, 100/second per workflow</td>
</tr>
<tr>
<td>Queued instances per Workflow <sup><a href="#2026-04-15-workflows-limits-raised-footnote-1">1</a></sup></td>
<td>1 million</td>
<td>2 million</td>
</tr>
</tbody>
</table>
<p>These increases apply to all users on the <a href="/workers/platform/pricing/">Workers Paid plan</a>. Refer to the <a href="/workflows/reference/limits/">Workflows limits documentation</a> for more details.</p>
<section class="footnotes"><h4 id="2026-04-15-workflows-limits-raised-footnotes">Footnotes</h4><ol><li id="2026-04-15-workflows-limits-raised-footnote-1">Queued instances are instances that have been created or awoken and are waiting for a concurrency slot.</li></ol></section>


<h2 id="agent-lee-adds-write-operations-and-generative-ui"><a href="/changelog/post/2026-04-15-agentlee-writeops-genui/">Agent Lee adds Write Operations and Generative UI</a></h2>
<p><em>2026-04-15</em></p>
<h4 id="2026-04-15-agentlee-writeops-genui-agent-lee-adds-write-operations-and-generative-ui">Agent Lee adds Write Operations and Generative UI</h4>
<p>We are excited to announce two major capability upgrades for <strong>Agent Lee</strong>, the AI co-pilot built directly into the Cloudflare dashboard. Agent Lee is designed to understand your specific account configuration, and with this release, it moves from a passive advisor to an active assistant that can help you manage your infrastructure and visualize your data through natural language.</p>
<h4 id="2026-04-15-agentlee-writeops-genui-take-action-with-write-operations">Take action with Write Operations</h4>
<p>Agent Lee can now perform changes on your behalf across your Cloudflare account. Whether you need to update DNS records, modify SSL/TLS settings, or configure Workers routes, you can simply ask.</p>
<p>To ensure security and accuracy, every write operation requires <strong>explicit user approval</strong>. Before any change is committed, Agent Lee will present a summary of the proposed action in plain language. No action is taken until you select <strong>Confirm</strong>, and this approval requirement is enforced at the infrastructure level to prevent unauthorized changes.</p>
<p><strong>Example requests:</strong></p>
<ul>
<li><em>&quot;Add an A record for blog.example.com pointing to 192.0.2.10.&quot;</em></li>
<li><em>&quot;Enable Always Use HTTPS on my zone.&quot;</em></li>
<li><em>&quot;Set the SSL mode for example.com to Full (strict).&quot;</em></li>
</ul>
<h4 id="2026-04-15-agentlee-writeops-genui-visualize-data-with-generative-ui">Visualize data with Generative UI</h4>
<p>Understanding your traffic and security trends is now as easy as asking a question. Agent Lee now features <strong>Generative UI</strong>, allowing it to render inline charts and structured data visualizations directly within the chat interface using your actual account telemetry.</p>
<p><strong>Example requests:</strong></p>
<ul>
<li><em>&quot;Show me a chart of my traffic over the last 7 days.&quot;</em></li>
<li><em>&quot;What does my error rate look like for the past 24 hours?&quot;</em></li>
<li><em>&quot;Graph my cache hit rate for example.com this week.&quot;</em></li>
</ul>
<hr />
<h4 id="2026-04-15-agentlee-writeops-genui-availability">Availability</h4>
<p>These features are currently available in <strong>Beta</strong> for all users on the <strong>Free plan</strong>. To get started, log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select <strong>Ask AI</strong> in the upper right corner.</p>
<p>To learn more about how to interact with your account using AI, refer to the <a href="/agent-lee/">Agent Lee documentation</a>.</p>


<h2 id="privacy-proxy-metrics-now-available-via-graphql-analytics-api"><a href="/changelog/post/2026-04-15-graphql-analytics-api/">Privacy Proxy metrics now available via GraphQL Analytics API</a></h2>
<p><em>2026-04-15</em></p>
<p>Privacy Proxy metrics are now queryable through Cloudflare's <a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a>, the new default method for accessing Privacy Proxy observability data. All metrics are available through a single endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/graphql \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;query&quot;: &quot;{ viewer { accounts(filter: { accountTag: $accountTag }) { privacyProxyRequestMetricsAdaptiveGroups(filter: { date_geq: $startDate, date_leq: $endDate }, limit: 10000, orderBy: [date_ASC]) { count dimensions { date } } } } }&quot;,&#10;    &quot;variables&quot;: {&#10;      &quot;accountTag&quot;: &quot;&lt;YOUR_ACCOUNT_TAG&gt;&quot;,&#10;      &quot;startDate&quot;: &quot;2026-04-04&quot;,&#10;      &quot;endDate&quot;: &quot;2026-04-06&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-04-15-graphql-analytics-api-available-nodes">Available nodes</h4>
<p>Four GraphQL nodes are now live, providing aggregate metrics across all key dimensions of your Privacy Proxy deployment:</p>
<ul>
<li><strong><code>privacyProxyRequestMetricsAdaptiveGroups</code></strong> — Request volume, error rates, status codes, and proxy status breakdowns.</li>
<li><strong><code>privacyProxyIngressConnMetricsAdaptiveGroups</code></strong> — Client-to-proxy connection counts, bytes transferred, and latency percentiles.</li>
<li><strong><code>privacyProxyEgressConnMetricsAdaptiveGroups</code></strong> — Proxy-to-origin connection counts, bytes transferred, and latency percentiles.</li>
<li><strong><code>privacyProxyAuthMetricsAdaptiveGroups</code></strong> — Authentication attempt counts by method and result.</li>
</ul>
<p>All nodes support filtering by time, data center (<code>coloCode</code>), and endpoint, with additional node-specific dimensions such as transport protocol and authentication method.</p>
<h4 id="2026-04-15-graphql-analytics-api-what-this-means-for-existing-opentelemetry-users">What this means for existing OpenTelemetry users</h4>
<p>OpenTelemetry-based metrics export remains available. The GraphQL Analytics API is now the recommended default method — a plug-and-play method that requires no collector infrastructure, saving engineering overhead.</p>
<h4 id="2026-04-15-graphql-analytics-api-learn-more">Learn more</h4>
<ul>
<li><a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API for Privacy Proxy</a></li>
<li><a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API — getting started</a></li>
</ul>


<h2 id="manage-browser-rendering-sessions-with-wrangler-cli"><a href="/changelog/post/2026-04-14-browser-wrangler-commands/">Manage Browser Rendering sessions with Wrangler CLI</a></h2>
<p><em>2026-04-14</em></p>
<p><a href="/browser-run/">Browser Rendering</a> now supports <code>wrangler browser</code> commands, letting you create, manage, and view browser sessions directly from your terminal, streamlining your workflow. Since Wrangler handles authentication, you do not need to pass API tokens in your commands.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler browser create</code></td>
<td>Create a new browser session</td>
</tr>
<tr>
<td><code>wrangler browser close</code></td>
<td>Close a session</td>
</tr>
<tr>
<td><code>wrangler browser list</code></td>
<td>List active sessions</td>
</tr>
<tr>
<td><code>wrangler browser view</code></td>
<td>View a live browser session</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command spins up a browser instance on Cloudflare's network and returns a session URL. Once created, you can connect to the session using any <a href="/browser-run/cdp/">CDP</a>-compatible client like <a href="/browser-run/cdp/puppeteer/">Puppeteer</a>, <a href="/browser-run/cdp/playwright/">Playwright</a>, or <a href="/browser-run/cdp/mcp-clients/">MCP clients</a> to automate browsing, scrape content, or debug remotely.</p>
<pre tabindex="0"><code class="language-sh">wrangler browser create&#10;</code></pre>
<p>Use <code>--keepAlive</code> to set the session keep-alive duration (60-600 seconds):</p>
<pre tabindex="0"><code class="language-sh">wrangler browser create --keepAlive 300&#10;</code></pre>
<p>The <code>view</code> command auto-selects when only one session exists, or prompts for selection when multiple sessions are available.</p>
<p>All commands support <code>--json</code> for structured output, and because these are CLI commands, you can incorporate them into scripts to automate session management.</p>
<p>For full usage details, refer to the <a href="/browser-run/reference/wrangler-commands/">Wrangler commands documentation</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/8/">Previous</a><span>Page 9 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/10/">Next</a></nav>
