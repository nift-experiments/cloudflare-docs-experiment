<h1 id="changelog">Changelog</h1>

<h2 id="terraform-v5-20-0-now-available"><a href="/changelog/post/2026-06-12-terraform-v5.20.0-provider/">Terraform v5.20.0 now available</a></h2>
<p><em>2026-06-12</em></p>
<p>Cloudflare's Terraform v5 Provider makes it easy for developers to manage their Cloudflare infrastructure using a configuration as code approach. It releases every <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 weeks</a> to ensure that you can always manage the latest features in the platform. This week, we launched Terraform v5.20.0, which adds 24 new resources, bumps the underlying Go SDK to cloudflare-go v7, and includes a range of bug fixes and state upgraders based on community feedback.</p>
<h4 id="2026-06-12-terraform-v5.20.0-provider-new-resources">New resources</h4>
<ul>
<li><strong>cloudflare_ai_search_namespace:</strong> Manage AI Search namespaces</li>
<li><strong>cloudflare_custom_csr:</strong> Manage custom certificate signing requests</li>
<li><strong>cloudflare_dls_prefix_binding:</strong> Manage DLS regional service prefix bindings</li>
<li><strong>cloudflare_flagship_app:</strong> Manage Flagship feature flag apps</li>
<li><strong>cloudflare_flagship_flag:</strong> Manage Flagship feature flags</li>
<li><strong>cloudflare_google_tag_gateway:</strong> Manage Google Tag Gateway</li>
<li><strong>cloudflare_load_balancer_monitor_group:</strong> Manage load balancer monitor groups</li>
<li><strong>cloudflare_oauth_client:</strong> Manage IAM OAuth clients</li>
<li><strong>cloudflare_origin_cloud_region:</strong> Manage origin cloud regions (v2 endpoints)</li>
<li><strong>cloudflare_secrets_store:</strong> Manage Secrets Store instances</li>
<li><strong>cloudflare_secrets_store_secret:</strong> Manage Secrets Store secrets</li>
<li><strong>cloudflare_share:</strong> Manage resource shares</li>
<li><strong>cloudflare_share_recipient:</strong> Manage share recipients</li>
<li><strong>cloudflare_share_resource:</strong> Manage shared resources</li>
<li><strong>cloudflare_zero_trust_device_deployment_groups:</strong> Manage Zero Trust device deployment groups</li>
<li><strong>cloudflare_zero_trust_dlp_data_class:</strong> Manage DLP data classes</li>
<li><strong>cloudflare_zero_trust_dlp_data_tag:</strong> Manage DLP data tags</li>
<li><strong>cloudflare_zero_trust_dlp_data_tag_category:</strong> Manage DLP data tag categories</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_group:</strong> Manage DLP sensitivity groups</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_level:</strong> Manage DLP sensitivity levels</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_level_order:</strong> Manage DLP sensitivity level ordering</li>
<li><strong>cloudflare_zero_trust_resource_library_application:</strong> Manage Zero Trust resource library applications</li>
<li><strong>cloudflare_zero_trust_resource_library_category:</strong> Manage Zero Trust resource library categories</li>
<li><strong>cloudflare_zero_trust_tunnel_warp_connector_config:</strong> Manage WARP connector tunnel configurations</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-features">Features</h4>
<ul>
<li><strong>cache:</strong> add create (POST) method for smart_tiered_cache</li>
<li><strong>cache:</strong> update OPCR config to v2 endpoints</li>
<li><strong>dlp:</strong> promote classification Stainless config to main</li>
<li><strong>dlp:</strong> add custom prompt topics endpoint</li>
<li><strong>email_security_block_sender:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>email_security_impersonation_registry:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>email_security_trusted_domains:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>snippets:</strong> add Terraform <code>id_property</code> annotations for snippet and snippet_rules</li>
<li>bump Go SDK to cloudflare-go v7</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-bug-fixes">Bug fixes</h4>
<ul>
<li><strong>account_member:</strong> missing upgrade path from v5.0–v5.15</li>
<li><strong>authenticated_origin_pulls_settings:</strong> nil pointer panic</li>
<li><strong>bot_management:</strong> restore <code>content_bots_protection</code> handling in model.go</li>
<li><strong>dns_record:</strong> prevent FQDN normalization from swallowing name shortening changes</li>
<li><strong>list:</strong> nullify empty nested objects to prevent inconsistent result after apply</li>
<li><strong>load_balancer_pool:</strong> accept early-v5 object-shape state at schema_version=0</li>
<li><strong>load_balancer_pool:</strong> add <code>UseStateForUnknown</code> for <code>load_shedding</code> attribute to prevent drift</li>
<li><strong>r2_custom_domain:</strong> restore degraded-response handling in resource.go</li>
<li><strong>regional_hostname:</strong> update cloudflare-go imports from v6 to v7</li>
<li><strong>secrets_store:</strong> fix model/schema parity and guard acceptance tests</li>
<li><strong>spectrum_application:</strong> accept early-v5 object-shape state at schema_version=0</li>
<li><strong>worker:</strong> preserve <code>observability.traces.propagation_policy</code> across reads</li>
<li><strong>worker:</strong> add <code>propagation_policy</code> to observability defaults</li>
<li><strong>worker_version:</strong> restore handwritten D1 <code>database_id</code> handling</li>
<li><strong>workers_custom_domain:</strong> missing <code>CertId</code> field in state migration</li>
<li><strong>workers_script:</strong> restore annotations Read workaround stripped by codegen</li>
<li><strong>zero_trust_access_identity_provider:</strong> change <code>read_only</code> from computed to optional</li>
<li><strong>zero_trust_access_identity_provider:</strong> add <code>UseStateForUnknown</code> to SAML-only config fields</li>
<li><strong>zero_trust_access_identity_provider:</strong> use <code>UseNonNullStateForUnknown</code> on scim_config fields</li>
<li><strong>zero_trust_access_policy:</strong> populate <code>account_id</code> when migrating zone-scoped v4 state</li>
<li><strong>zero_trust_access_policy:</strong> missing <code>common_names</code> transform in migration</li>
<li>gracefully handle nil pointer dereference when config has <code>attributes_flat</code> during migration</li>
<li>set initial schema version to 500 for all new resources</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-refactors">Refactors</h4>
<p>Extracted <code>MoveState</code> nil guard into shared helper</p>
<h4 id="2026-06-12-terraform-v5.20.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Version 5 Migration Guide](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)


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


<h2 id="terraform-v5-9-now-available"><a href="/changelog/post/2025-08-29-terrform-v5.9-provider/">Terraform v5.9 now available</a></h2>
<p><em>2025-08-29</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadence to ensure its stability and reliability, including the v5.9 release. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release, and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<p>This release includes a new resource, <code>cloudflare_snippet</code>, which replaces <code>cloudflare_snippets</code>. <code>cloudflare_snippet</code> is now considered deprecated but can still be used. Please utilize <code>cloudflare_snippet</code> as soon as possible.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_zone_setting`
  - `cloudflare_worker_script`
  - `cloudflare_worker_route`
  - `tiered_cache`
- **NEW** resource `cloudflare_snippet` which should be used in place of `cloudflare_snippets`. `cloudflare_snippets` is now deprecated. This enables the management of Cloudflare's snippet functionality through Terraform.
- DNS Record Improvements: Enhanced handling of DNS record drift detection
- Load Balancer Fixes: Resolved `created_on` field inconsistencies and improved pool configuration handling
- Bot Management: Enhanced auto-update model state consistency and fight mode configurations
- Other bug fixes
<p>For a more detailed look at all of the changes, refer to the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.9.0">changelog</a> in GitHub.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-issues-closed">Issues Closed</h4>
- [#5921: In cloudflare_ruleset removing an existing rule causes recreation of later rules](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5921)
- [#5904: cloudflare_zero_trust_access_application is not idempotent](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5904)
- [#5898: (cloudflare_workers_script) Durable Object migrations not applied](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5898)
- [#5892: cloudflare_workers_script secret_text environment variable gets replaced on every deploy](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5892)
- [#5891: cloudflare_zone suddenly started showing drift](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5891)
- [#5882: cloudflare_zero_trust_list always marked for change due to read only attributes](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5882)
- [#5879: cloudflare_zero_trust_gateway_certificate unable to manage resource (cant mark as active/inactive)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5879)
- [#5858: cloudflare_dns_records is always updated in-place](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5858)
- [#5839: Recurring change on cloudflare_zero_trust_gateway_policy after upgrade to V5 provider & also setting expiration fails](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5839)
- [#5811: Reusable policies are imported as inline type for cloudflare_zero_trust_access_application](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5811)
- [#5795: cloudflare_zone_setting inconsistent value of "editable" upon apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5795)
- [#5789: Pagination issue fetching all policies in "cloudflare_zero_trust_access_policies" data source](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5789)
- [#5770: cloudflare_zero_trust_access_application type warp diff on every apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5770)
- [#5765: V5 / cloudflare_zone_dnssec fails with HTTP/400 "Malformed request body"](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5765)
- [#5755: Unable to manage Cloudflare managed WAF rules via Terraform](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5755)
- [#5738: v4 to v5 upgrade failing Error: no schema available AND Unable to Read Previously Saved State for UpgradeResourceState](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5738)
- [#5727: cloudflare_ruleset http_request_cache_settings bypass mismatch between dashboard and terraform](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5727)
- [#5700: cloudflare_account_member invalid type 'string' for field 'roles'](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5700)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new issue if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition. These do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
<li><a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub Repository</a></li>
</ul>


<h2 id="terraform-v5-8-4-now-available"><a href="/changelog/post/2025-08-15-terraform-v5.8.4-provider/">Terraform v5.8.4 now available</a></h2>
<p><em>2025-08-15</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare Community related to the v5 release. We have committed to releasing improvements on a two week cadence to ensure stability and reliability.</p>
<p>One key change we adopted in recent weeks is a pivot to more comprehensive, test-driven development. We are still evaluating individual issues, but are also investing in much deeper testing to drive our stabilization efforts. We will subsequently be investing in comprehensive migration scripts. As a result, you will see several of the highest traffic APIs have been stabilized in the most recent release, and are supported by comprehensive acceptance tests.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_argo_smart_routing`
  - `cloudflare_bot_management`
  - `cloudflare_list`
  - `cloudflare_list_item`
  - `cloudflare_load_balancer`
  - `cloudflare_load_balancer_monitor`
  - `cloudflare_load_balancer_pool`
  - `cloudflare_spectrum_application`
  - `cloudflare_managed_transforms`
  - `cloudflare_url_normalization_settings`
  - `cloudflare_snippet`
  - `cloudflare_snippet_rules`
  - `cloudflare_zero_trust_access_application`
  - `cloudflare_zero_trust_access_group`
  - `cloudflare_zero_trust_access_identity_provider`
  - `cloudflare_zero_trust_access_mtls_certificate`
  - `cloudflare_zero_trust_access_mtls_hostname_settings`
  - `cloudflare_zero_trust_access_policy`
  - `cloudflare_zone`
- Multipart handling restored for `cloudflare_snippet`
- `cloudflare_bot_management` diff issues resolves when running `terraform plan` and `terraform apply`
- Other bug fixes
<p>For a more detailed look at all of the changes, refer to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.4">changelog</a> in GitHub.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-issues-closed">Issues Closed</h4>
- [#5017: 'Uncaught Error: No such module' using cloudflare_snippets](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5017)
- [#5701: cloudflare_workers_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5640: cloudflare_argo_smart_routing importing doesn't read the actual value](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5640)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This will help you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition. These migration scripts do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="terraform-v5-8-2-now-available"><a href="/changelog/post/2025-08-01-terraform-v5.8.2-provider/">Terraform v5.8.2 now available</a></h2>
<p><em>2025-08-01</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and reliability. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_custom_pages`
  - `cloudflare_page_rule`
  - `cloudflare_dns_record`
  - `cloudflare_argo_tiered_caching`
- Addressed chronic drift issues in `cloudflare_logpush_job`, `cloudflare_zero_trust_dns_location`, `cloudflare_ruleset` & `cloudflare_api_token`
- `cloudflare_zone_subscription` returns expected values `rate_plan.id` from former versions
- `cloudflare_workers_script` can now successfully be destroyed with bindings & migration for Durable Objects now recorded in tfstate 
- Ability to configure `add_headers` under `cloudflare_zero_trust_gateway_policy` 
- Other bug fixes
<p>For a more detailed look at all of the changes, see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.2">changelog</a> in GitHub.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-issues-closed">Issues Closed</h4>
- [#5666: cloudflare_ruleset example lists id which is a read-only field](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5666)
- [#5578: cloudflare_logpush_job plan always suggests changes](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5578)
- [#5552: 5.4.0: Since provider update, existing cloudflare_list_item would be recreated "created" state](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5552)
- [#5670: cloudflare_zone_subscription: uses wrong ID field in Read/Update](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5670)
- [#5548: cloudflare_api_token resource always shows changes (drift)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5548)
- [#5634: cloudflare_workers_script with bindings fails to be destroyed](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5634)
- [#5616: cloudflare_workers_script Unable to deploy worker assets](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5616)
- [#5331: cloudflare_workers_script 500 internal server error when uploading python](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5331)
- [#5701: cloudflare_workers_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5704: cloudflare_workers_script randomly fails to deploy when changing compatibility_date](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5704)
- [#5439: cloudflare_workers_script (v5.2.0) ignoring content and bindings properties](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5439)
- [#5522: cloudflare_workers_script always detects changes after apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5522)
- [#5693: cloudflare_zero_trust_access_identity_provider gives recurring change on OTP pin login](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5693)
- [#5567: cloudflare_r2_custom_domain doesn't roundtrip jurisdiction properly](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5567)
- [#5179: Bad request with when creating cloudflare_api_shield_schema resource](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5179)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="terraform-v5-7-0-now-available"><a href="/changelog/post/2025-07-11-terraform-v5.7.0-provider/">Terraform v5.7.0 now available</a></h2>
<p><em>2025-07-14</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release, with 13.5% of resources impacted. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and relability, including the v5.7 release.</p>
<p>Thank you for continuing to raise issues and please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-changes">Changes</h4>
- Addressed permanent diff bug on Cloudflare Tunnel config
- State is now saved correctly for Zero Trust Access applications
- Exact match is now working as expected within `data.cloudflare_zero_trust_access_applications`
- `cloudflare_zero_trust_access_policy` now supports OIDC claims & diff issues resolved
- Self hosted applications with private IPs no longer require a public domain for `cloudflare_zero_trust_access_application`.
- New resource:
  - `cloudflare_zero_trust_tunnel_warp_connector`
- Other bug fixes
<p>For a more detailed look at all of the changes, see the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.7.0">changelog</a> in GitHub.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-issues-closed">Issues Closed</h4>
- [#5563: cloudflare_logpull_retention is missing import](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5563)
- [#5608: cloudflare_zero_trust_access_policy in 5.5.0 provider gives error upon apply unexpected new value: .app_count: was cty.NumberIntVal(0), but now cty.NumberIntVal(1)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5608)
- [#5612: data.cloudflare_zero_trust_access_applications does not exact match](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5612)
- [#5532: cloudflare_zero_trust_access_identity_provider detects changes on every plan](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
- [#5662: cloudflare_zero_trust_access_policy does not support OIDC claims](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5662)
- [#5565: Running Terraform with the cloudflare_zero_trust_access_policy resource results in updates on every apply, even when no changes are made - breaks idempotency](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5565)
- [#5529: cloudflare_zero_trust_access_application: self hosted applications with private ips require public domain ](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5529)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-upgrading">Upgrading</h4>
<p>We suggest holding on migration to v5 while we work on stabilization of the v5 provider. This will ensure Cloudflare can work ahead and avoid any blocking issues.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the
<a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have
provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which
use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our
<a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="terraform-v5-6-0-now-available"><a href="/changelog/post/2025-06-17-terraform-v5.6.0-provider/">Terraform v5.6.0 now available</a></h2>
<p><em>2025-06-17</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>.
Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since
launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a>
reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address
these issues across the company, and have released the v5.6.0 release which includes a number of bug fixes. Please keep an
eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-changes">Changes</h4>
<ul>
<li>Broad fixes across resources with recurring diffs, including, but not limited to:
<ul>
<li><code>cloudflare_zero_trust_access_identity_provider</code>
<ul>
<li><code>cloudflare_zone</code></li>
</ul>
</li>
</ul>
</li>
<li><code>cloudflare_page_rules</code> runtime panic when setting <code>cache_level</code> to <code>cache_ttl_by_status</code></li>
<li>Failure to serialize requests in <code>cloudflare_zero_trust_tunnel_cloudflared_config</code></li>
<li>Undocumented field 'priority' on <code>zone_lockdown</code> resource</li>
<li>Missing importability for <code>cloudflare_zero_trust_device_default_profile_local_domain_fallback</code> and <code>cloudflare_account_subscription</code></li>
<li>New resources:
<ul>
<li><code>cloudflare_schema_validation_operation_settings</code></li>
<li><code>cloudflare_schema_validation_schemas</code></li>
<li><code>cloudflare_schema_validation_settings</code></li>
<li><code>cloudflare_zero_trust_device_settings</code></li>
</ul>
</li>
<li>Other bug fixes</li>
</ul>
<p>For a more detailed look at all of the changes, see the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.6.0">changelog</a> in GitHub.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-issues-closed">Issues Closed</h4>
- [#5098: 500 Server Error on updating 'zero_trust_tunnel_cloudflared_virtual_network' Terraform resource](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5098)
- [#5148: cloudflare_user_agent_blocking_rule doesn’t actually support user agents](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5148)
- [#5472: cloudflare_zone showing changes in plan after following upgrade steps](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5472)
- [#5508: cloudflare_zero_trust_tunnel_cloudflared_config failed to serialize http request](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5508)
- [#5509: cloudflare_zone: Problematic Terraform behaviour with paused zones](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5509)
- [#5520: Resource 'cloudflare_magic_wan_static_route' is not working](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5520)
- [#5524: Optional fields cause crash in cloudflare_zero_trust_tunnel_cloudflared(s) when left null](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5524)
- [#5526: Provider v5 migration issue: no import method for cloudflare_zero_trust_device_default_profile_local_domain_fallback](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5526)
- [#5532: cloudflare_zero_trust_access_identity_provider detects changes on every plan](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
- [#5561: cloudflare_zero_trust_tunnel_cloudflared: cannot rotate tunnel secret](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5561)
- [#5569: cloudflare_zero_trust_device_custom_profile_local_domain_fallback not allowing multiple DNS Server entries](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5569)
- [#5577: Panic modifying page_rule resource](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5577)
- [#5653: cloudflare_zone_setting resource schema confusion in 5.5.0: value vs enabled](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5653)
<p>If you have an unaddressed issue with the provider, we encourage you to check the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already
exist for what you are experiencing.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the
<a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have
provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which
use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our
<a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="terraform-v5-5-0-now-available"><a href="/changelog/post/2025-05-19-terraform-v5.5.0-provider/">Terraform v5.5.0 now available</a></h2>
<p><em>2025-05-19</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.5.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-changes">Changes</h4>
<ul>
<li>Broad fixes across resources with recurring diffs, including, but not limited to:
<ul>
<li><code>cloudflare_zero_trust_gateway_policy</code></li>
<li><code>cloudflare_zero_trust_access_application</code></li>
<li><code>cloudflare_zero_trust_tunnel_cloudflared_route</code></li>
<li><code>cloudflare_zone_setting</code></li>
<li><code>cloudflare_ruleset</code></li>
<li><code>cloudflare_page_rule</code></li>
</ul>
</li>
<li>Zone settings can be re-applied without client errors</li>
<li>Page rules conversion errors are fixed</li>
<li>Failure to apply changes to <code>cloudflare_zero_trust_tunnel_cloudflared_route</code></li>
<li>Other bug fixes</li>
</ul>
<p>For a more detailed look at all of the changes, see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.5.0">changelog</a> in GitHub.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-issues-closed">Issues Closed</h4>
- [#5304: Importing cloudflare_zero_trust_gateway_policy invalid attribute filter value](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5304)
- [#5303: cloudflare_page_rule import does not set values for all of the fields in terraform state](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5303)
- [#5178: cloudflare_page_rule Page rule creation with redirect fails](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5178)
- [#5336: cloudflare_turnstile_wwidget not able to update](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5336)
- [#5418: cloudflare_cloud_connector_rules: Provider returned invalid result object after apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5418)
- [#5423: cloudflare_zone_setting: "Invalid value for zone setting always_use_https"](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5423)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="terraform-v5-4-0-now-available"><a href="/changelog/post/2025-05-06-terraform-v5.4.0-provider/">Terraform v5.4.0 now available</a></h2>
<p><em>2025-05-06</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.4.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-changes">Changes</h4>
<ul>
<li>
<p>Removes the <code>worker_platforms_script_secret</code> resource from the provider (see <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade#cloudflare_worker_secret">migration guide</a> for alternatives—applicable to both Workers and Workers for Platforms)</p>
</li>
<li>
<p>Removes duplicated fields in <code>cloudflare_cloud_connector_rules</code> resource</p>
</li>
<li>
<p>Fixes <code>cloudflare_workers_route</code> id issues <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5134">#5134</a> <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5501">#5501</a></p>
</li>
<li>
<p>Fixes issue around refreshing resources that have unsupported response types</p>
<details>
<pre><code>&lt;summary&gt;Affected resources&lt;/summary&gt;
&lt;ul&gt;
</code></pre>
<pre><code>  &lt;li&gt;`cloudflare_certificate_pack`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_registrar_domain`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_stream_download`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_stream_webhook`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_user`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_kv`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_script`&lt;/li&gt;&#10;</code></pre>
<pre><code>&lt;/ul&gt;
</code></pre>
</details>
</li>
<li>
<p>Fixes <code>cloudflare_workers_kv</code> state refresh issues</p>
</li>
<li>
<p>Fixes issues around configurability of nested properties without computed values for the following resources</p>
<details>
<pre><code>&lt;summary&gt;Affected resources&lt;/summary&gt;
&lt;ul&gt;
</code></pre>
<pre><code>  &lt;li&gt;`cloudflare_account`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_account_dns_settings`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_account_token`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_api_token`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_cloud_connector_rules`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_custom_ssl`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_d1_database`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_dns_record`&lt;/li&gt;&#10;  &lt;li&gt;`email_security_trusted_domains`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_hyperdrive_config`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_keyless_certificate`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_list_item`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_load_balancer`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_logpush_dataset_job`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_network_monitoring_configuration`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site_lan`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site_wan`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_wan_static_route`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_notification_policy`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_pages_project`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_queue`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_queue_consumer`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_cors`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_event_notification`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_lifecycle`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_lock`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_sippy`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_ruleset`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_snippet_rules`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_snippets`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_spectrum_application`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_deployment`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_zero_trust_access_application`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_zero_trust_access_group`&lt;/li&gt;&#10;</code></pre>
<pre><code>&lt;/ul&gt;
</code></pre>
</details>
</li>
<li>
<p>Fixed defaults that made <code>cloudflare_workers_script</code> fail when using Assets</p>
</li>
<li>
<p>Fixed Workers Logpush setting in <code>cloudflare_workers_script</code> mistakenly being readonly</p>
</li>
<li>
<p>Fixed <code>cloudflare_pages_project</code> broken when using &quot;source&quot;</p>
</li>
</ul>
<p>The detailed <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.4.0">changelog</a> is available on GitHub.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues either by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>, or by opening a <a href="https://www.support.cloudflare.com/s/?language=en_US">support ticket</a>.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="dozens-of-cloudflare-terraform-provider-resources-now-have-proper-drift-detection"><a href="/changelog/post/2025-03-21-resource-force-replacement-bug/">Dozens of Cloudflare Terraform Provider resources now have proper drift detection</a></h2>
<p><em>2025-03-21</em></p>
<p>In <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your <code>terraform plan</code> to only show what resources are expected to change.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>API Shield</li>
<li>Argo Smart Routing</li>
<li>Argo Tiered Caching</li>
<li>Bot Management</li>
<li>BYOIP</li>
<li>D1</li>
<li>DNS</li>
<li>Email Routing</li>
<li>Hyperdrive</li>
<li>Observatory</li>
<li>Pages</li>
<li>R2</li>
<li>Rules</li>
<li>SSL/TLS</li>
<li>Waiting Room</li>
<li>Workers</li>
<li>Zero Trust</li>
</ul>


<h2 id="cloudflare-terraform-provider-now-properly-redacts-sensitive-values"><a href="/changelog/post/2025-03-21-sensitive-values-redacted/">Cloudflare Terraform Provider now properly redacts sensitive values</a></h2>
<p><em>2025-03-21</em></p>
<p>In the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in <a href="https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml">Cloudflare's OpenAPI Schema</a> are now annotated with <code>x-sensitive: true</code>. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>Alerts and Audit Logs</li>
<li>Device API</li>
<li>DLP</li>
<li>DNS</li>
<li>Magic Visibility</li>
<li>Magic WAN</li>
<li>TLS Certs and Hostnames</li>
<li>Tunnels</li>
<li>Turnstile</li>
<li>Workers</li>
<li>Zaraz</li>
</ul>


<h2 id="terraform-v5-provider-is-now-generally-available"><a href="/changelog/post/2025-02-03-terraform-v5-provider/">Terraform v5 Provider is now generally available</a></h2>
<p><em>2025-02-03</em></p>
<p><img src="/assets/upstream/images/changelog/2024-02-03-terraform-v5-screenshot.png" alt="Screenshot of Terraform defining a Zone" /></p>
<p>Cloudflare's v5 Terraform Provider is now generally available. With this release, Terraform resources are now automatically generated based on OpenAPI Schemas. This change brings alignment across our SDKs, API documentation, and now Terraform Provider. The new provider boosts coverage by increasing support for API properties to 100%, adding 25% more resources, and more than 200 additional data sources. Going forward, this will also reduce the barriers to bringing more resources into Terraform across the broader Cloudflare API. This is a small, but important step to making more of our platform manageable through GitOps, making it easier for you to manage Cloudflare just like you do your other infrastructure.</p>
<p>The Cloudflare Terraform Provider v5 is a ground-up rewrite of the provider and introduces breaking changes for some resource types. Please refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">upgrade guide</a> for best practices, or the <a href="https://blog.cloudflare.com/automatically-generating-cloudflares-terraform-provider/">blog post on automatically generating Cloudflare's Terraform Provider</a> for more information about the approach.</p>
<p>For more info</p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>



