<h1 id="changelog">Changelog</h1>

<h2 id="instant-bank-payments-via-link"><a href="/changelog/post/2026-04-29-instant-bank-payments-via-link/">Instant Bank Payments via Link</a></h2>
<p><em>2026-04-29</em></p>
<p>You can now pay for Cloudflare services directly from your bank account using <a href="/billing/payment-methods/instant-bank-payments-link/">Instant Bank Payments via Link</a>.</p>
<h4 id="2026-04-29-instant-bank-payments-via-link-what-changed">What changed</h4>
<p><a href="https://link.co/">Link</a> now supports bank account payments in addition to cards. If you have a bank account saved in Link, it appears as a payment option at checkout. If not, you can connect one during the checkout flow.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-29-instant-bank-payments-link.png" alt="Instant Bank Payments via Link at checkout" /></p>
<h4 id="2026-04-29-instant-bank-payments-via-link-how-to-use-it">How to use it</h4>
<ol>
<li>During checkout, select your bank account from your saved Link payment methods.</li>
<li>Confirm the payment.</li>
</ol>
<p>After your first Link authentication, your bank account is available for future purchases without re-entering details.</p>
<h4 id="2026-04-29-instant-bank-payments-via-link-who-is-eligible">Who is eligible</h4>
<p>Instant Bank Payments via Link is available to US-based self-serve accounts across all Cloudflare products. Your existing cards remain available at checkout.</p>
<p>Bank-based Link payments appear in your billing history with the payment method shown as <code>link</code> and last four digits as <code>0000</code>. For details, refer to the <a href="/billing/payment-methods/instant-bank-payments-link/">Instant Bank Payments via Link documentation</a>.</p>


<h2 id="direct-access-to-support-from-the-dashboard"><a href="/changelog/post/2026-04-28-direct-support-navigation/">Direct access to Support from the dashboard</a></h2>
<p><em>2026-04-28</em></p>
<h4 id="2026-04-28-direct-support-navigation-direct-access-to-support-from-the-dashboard">Direct access to Support from the dashboard</h4>
<p>The <strong>Support</strong> button in the dashboard global navigation header now takes you directly to the <a href="https://support.cloudflare.com">Cloudflare Support Portal</a>, eliminating the previous dropdown menu.</p>
<p>This change ensures that when you need help, you spend less time navigating the UI and more time getting the answers you need.</p>
<h4 id="2026-04-28-direct-support-navigation-what-changed">What changed?</h4>
<ul>
<li><strong>Previous behavior</strong>: Selecting <strong>? Support</strong> opened a dropdown menu with various links (Help Center, Cloudflare Community, etc.).</li>
<li><strong>New behavior</strong>: Selecting <strong>Support</strong> immediately redirects your current tab to the Support Portal.</li>
</ul>
<p>To learn more about the resources available to you, refer to the <a href="https://developers.cloudflare.com/support/contacting-cloudflare-support/">Cloudflare Support documentation</a>.</p>


<h2 id="structured-error-responses-for-cloudflare-5xx-errors"><a href="/changelog/post/2026-04-27-structured-responses-for-5xx-errors/">Structured error responses for Cloudflare 5xx errors</a></h2>
<p><em>2026-04-27</em></p>
<p>Cloudflare-generated 5xx error responses now return structured JSON and Markdown when agents request them, matching the format already available for 1xxx errors. Responses follow <a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 (Problem Details for HTTP APIs)</a> and include a <code>Retry-After</code> HTTP header on retryable codes.</p>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-changes">Changes</h4>
<p><strong>5xx coverage.</strong> Ten Cloudflare-generated error codes (500, 502, 504, 520-526) now serve structured responses. These are errors Cloudflare itself generates when it cannot reach or understand the origin server. Origin-generated 5xx responses that Cloudflare passes through are not affected.</p>
<p><strong>Fault attribution.</strong> The <code>error_category</code> field tells agents where the fault lies:</p>
<ul>
<li><code>origin</code> (502, 504, 520-524) — the origin server is responsible. Transient; retry with the backoff in <code>retry_after</code>.</li>
<li><code>cloudflare</code> (500) — Cloudflare's fault, not the website or the request. Short retry.</li>
<li><code>ssl</code> (525, 526) — the origin's TLS configuration is broken. Do not retry.</li>
</ul>
<p><strong>Retry-After header.</strong> Retryable codes (500, 502, 504, 520-524) include a <code>Retry-After</code> HTTP header matching the <code>retry_after</code> body field. Non-retryable codes (525, 526) do not include the header.</p>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-negotiation-behavior">Negotiation behavior</h4>
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
<h4 id="2026-04-27-structured-responses-for-5xx-errors-availability">Availability</h4>
<p>Available now for all zones on all plans.</p>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-get-started">Get started</h4>
<p>Get JSON response for error 522:</p>
<pre><code class="language-bash">curl -s --compressed -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/522&quot; | jq .&#10;</code></pre>
<p>Check presence of the <code>Retry-After</code> HTTP header associated with the JSON response for error 521:</p>
<pre><code class="language-bash">curl -s --compressed -D - -o /dev/null -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/521&quot; | grep -i retry-after&#10;</code></pre>
<p>References:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 — Problem Details for HTTP APIs</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Cloudflare 5xx error documentation</a></li>
</ul>


<h2 id="resource-tagging-enters-public-beta"><a href="/changelog/post/2026-04-27-resource-tagging-public-beta/">Resource Tagging enters public beta</a></h2>
<p><em>2026-04-27</em></p>
<p>Resource Tagging is now in public beta and rolling out to all Cloudflare accounts over the coming days. You can attach custom key-value metadata to your Cloudflare resources and query across your entire account to find what you need.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-what-s-included">What's included</h4>
<ul>
<li><strong>Broad resource type support</strong> — Tag zones, custom hostnames, Cloudflare Tunnels, Workers, D1 databases, R2 buckets, KV namespaces, Durable Object namespaces, Queues, Stream videos, Images, Access applications, Gateway rules, AI Gateways, and more. Refer to the <a href="/resource-tagging/reference/resource-types/">full list of supported resource types</a>.</li>
<li><strong>Powerful filtering</strong> — Query tagged resources using AND/OR logic, negation, and key-only matching. Combine up to 20 filters per query to build precise resource views.</li>
<li><strong>Account and zone-level endpoints</strong> — Full CRUD operations across both scopes.</li>
<li><strong>Token-based authentication</strong> — Tagging supports <a href="/fundamentals/api/get-started/account-owned-tokens/">Account Owned Tokens</a> that persist independently of individual users, so your automation keeps running through credential rotations and team changes.</li>
<li><strong>Flexible role support</strong> — Super Administrators, Workers Admins, and Tag Admins can all manage tags.</li>
</ul>
<h4 id="2026-04-27-resource-tagging-public-beta-api-first-by-design">API-first by design</h4>
<p>The API is the primary interface for Resource Tagging and the recommended path for all workflows — scripting tag assignments, building CI/CD pipelines, or integrating with your infrastructure-as-code toolchain.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-dashboard-ui">Dashboard UI</h4>
<p>You can also view and manage tagged resources directly in the Cloudflare dashboard. Navigate to <strong>Manage Account</strong> &gt; <strong>Resource Tagging</strong> to see all tagged resources across your account, filter by resource name or tag, and add or edit tags inline.</p>
<p><img src="/assets/upstream/images/changelog/resource-tagging/tagged-resources-dashboard.png" alt="Tagged Resources dashboard" /></p>
<h4 id="2026-04-27-resource-tagging-public-beta-what-s-coming-next">What's coming next</h4>
<p>In future releases, expect support for additional resource types across the Cloudflare platform, tag-based access control policies for scoping user permissions to tagged resources, billing and usage attribution by tag for breaking down costs by team, project, or environment, and Terraform provider support for managing tags declaratively.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-current-limitations">Current limitations</h4>
<ul>
<li><code>PUT</code> replaces all tags on a resource (no partial update). Use the <a href="/resource-tagging/how-to/manage-tags/#add-a-single-tag">GET, merge, PUT workflow</a> to modify individual tags safely.</li>
<li><code>DELETE</code> removes all tags from a resource. To remove a single tag, PUT the remaining tags back.</li>
<li>Querying tags for a resource that has never been tagged returns <code>500</code> instead of <code>404</code>. This is a known beta limitation.</li>
</ul>
<p>To get started, refer to the <a href="/resource-tagging/">Resource Tagging documentation</a>.</p>


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


<h2 id="audit-logs-v2-organization-level-support"><a href="/changelog/post/2026-04-23-audit-logs-v2-organization-level/">Audit Logs v2 — Organization-level support</a></h2>
<p><em>2026-04-23</em></p>
<p>Audit Logs v2 now supports organization-level audit logs. Org Admins can retrieve audit events for actions performed at the organization level via the Audit Logs v2 API.</p>
<p>To retrieve organization-level audit logs, use the following endpoint:</p>
<pre><code class="language-bash">GET https://api.cloudflare.com/client/v4/organizations/{organization_id}/logs/audit&#10;</code></pre>
<p>This release covers user-initiated actions performed through organization-level APIs. Audit logs for system-initiated actions, a dashboard UI, and Logpush support for organizations will be added in future releases.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17692.md")</aside>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>


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


<h2 id="custom-dashboards-available-to-all-customers"><a href="/changelog/post/2026-04-22-custom-dashboards-ga/">Custom dashboards available to all customers</a></h2>
<p><em>2026-04-22</em></p>
<p>Custom Dashboards are now available to all Cloudflare customers. Build personalized views that highlight the metrics most critical to your infrastructure and security posture, moving beyond standard product dashboards.</p>
<p>This update significantly expands the data available for visualization. Build charts based on any of the <strong>100+ datasets</strong> available via the Cloudflare GraphQL API, covering everything from WAF events and Workers metrics to Load Balancing and Zero Trust logs.</p>
<h4 id="2026-04-22-custom-dashboards-ga-log-explorer-integration">Log Explorer integration</h4>
<p>Log Explorer customers can select Log Explorer datasets to create charts from raw, unsampled log data.</p>
<h4 id="2026-04-22-custom-dashboards-ga-key-benefits">Key benefits</h4>
<ul>
<li><strong>Unified visibility</strong>: Consolidate signals from different Cloudflare products (for example, HTTP Traffic and R2 Storage) into a single view.</li>
<li><strong>Flexible monitoring</strong>: Create charts that focus on specific status codes, ASN regions, or security actions that matter to your business.</li>
<li><strong>Expanded limits</strong>: Log Explorer customers can create up to <strong>100 dashboards</strong> (up from 25 for standard customers).</li>
</ul>
<p><img src="/assets/upstream/images/analytics/customdashboardshome.jpg" alt="Custom Dashboards home page showing dashboard list and chart previews" /></p>
<p>To get started, refer to the <a href="/analytics/custom-dashboards/">Custom Dashboards documentation</a>.</p>


<h2 id="network-overview-page-in-the-dashboard"><a href="/changelog/post/2026-04-21-network-overview-page/">Network Overview page in the dashboard</a></h2>
<p><em>2026-04-21T12:00:00</em></p>
<p>A new <strong>Network Overview</strong> page in the Cloudflare dashboard gives you a single starting point for network security and connectivity products.</p>
<p>From the Network Overview page, you can:</p>
<ul>
<li><strong>Connect resources with <a href="/tunnel/">Cloudflare Tunnel</a></strong> - Create tunnels to connect your infrastructure to Cloudflare without exposing it to the public Internet.</li>
<li><strong>Monitor traffic with Network Flow</strong> - Get real-time visibility into traffic volume from your routers.</li>
<li><strong>Configure Address Maps</strong> - Map dedicated static IPs or BYOIP prefixes to specific hostnames.</li>
<li><strong>Explore Magic Transit and Cloudflare WAN</strong> - Set up DDoS protection for your networks and connectivity for your branch offices and data centers.</li>
</ul>
<p>To find it, go to <a href="https://dash.cloudflare.com/?to=/:account/magic-networks/overview"><strong>Networking</strong></a> in the dashboard sidebar.</p>
<p>If you already use <a href="/magic-transit/">Magic Transit</a>, <a href="/cloudflare-wan/">Cloudflare WAN</a>, or other Cloudflare network services products, your existing experience is unchanged.</p>
<p><img src="/assets/upstream/images/fundamentals/network-overview.png" alt="Network Overview page in the Cloudflare dashboard" /></p>


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


<h2 id="logpush-subrequest-merging-for-http-requests"><a href="/changelog/post/2026-04-21-logpush-subrequests-merging/">Logpush subrequest merging for HTTP requests</a></h2>
<p><em>2026-04-21</em></p>
<p>When a Cloudflare Worker intercepts a visitor request, it can dispatch additional outbound fetch calls called subrequests. By default, each subrequest generates its own log entry in Logpush, resulting in multiple log lines per visitor request. With subrequest merging enabled, subrequest data is embedded as a nested array field on the parent log record instead.</p>
<h4 id="2026-04-21-logpush-subrequests-merging-what-s-new">What's new</h4>
- New subrequest_merging field on Logpush jobs — Set "merge_subrequests": true when creating or updating an http_requests Logpush job to enable the feature.
- New Subrequests log field — When subrequest merging is enabled, a Subrequests field (`array\<object\>`) is added to each parent request log record. Each element in the array contains the standard http_requests fields for that subrequest.
<h4 id="2026-04-21-logpush-subrequests-merging-limitations">Limitations</h4>
- Applies to the http_requests (zone-scoped) dataset only.
- A maximum of 50 subrequests are merged per parent request. Subrequests beyond this limit are passed through unmodified as individual log entries.
- Subrequests must complete within 5 minutes of the visitor request. Subrequests that exceed this window are passed through unmodified.
- Subrequests that do not qualify appear as separate log entries — no data is lost.
- Subrequest merging is being gradually rolled out and is not yet available on all zones. Contact your account team for concerns or to ensure it is enabled for your zone.
- For more information, refer to [Subrequests](/logs/logpush/logpush-job/subrequests/).


<h2 id="cloudflare-pipelines-as-a-logpush-destination"><a href="/changelog/post/2026-04-20-pipelines-logpush-destination/">Cloudflare Pipelines as a Logpush destination</a></h2>
<p><em>2026-04-20</em></p>
<p>Logpush has traditionally been great at delivering Cloudflare logs to a variety of destinations in JSON format. While JSON is flexible and easily readable, it can be inefficient to store and query at scale.</p>
<p>With this release, you can now send your logs directly to <a href="/pipelines/">Pipelines</a> to ingest, transform, and store your logs in <a href="/r2/">R2</a> as Parquet files or Apache Iceberg tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>. This makes the data footprint more compact and more efficient at querying your logs instantly with <a href="/r2-sql/">R2 SQL</a> or any other query engine that supports Apache Iceberg or Parquet.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-transform-logs-before-storage">Transform logs before storage</h4>
<p>Pipelines SQL runs on each log record in-flight, so you can reshape your data before it is written. For example, you can drop noisy fields, redact sensitive values, or derive new columns:</p>
<pre><code class="language-sql">INSERT INTO http_logs_sink&#10;SELECT&#10;  ClientIP,&#10;  EdgeResponseStatus,&#10;  to_timestamp_micros(EdgeStartTimestamp) AS event_time,&#10;  upper(ClientRequestMethod) AS method,&#10;  sha256(ClientIP) AS hashed_ip&#10;FROM http_logs_stream&#10;WHERE EdgeResponseStatus &gt;= 400;&#10;</code></pre>
<p>Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the <a href="/pipelines/sql-reference/">Pipelines SQL reference</a>.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-get-started">Get started</h4>
<p>To configure Pipelines as a Logpush destination, refer to <a href="/logs/logpush/logpush-job/enable-destinations/pipelines/">Enable Cloudflare Pipelines</a>.</p>


<h2 id="introducing-redirects-for-ai-training"><a href="/changelog/post/2026-04-17-redirects-for-ai-training/">Introducing Redirects for AI Training</a></h2>
<p><em>2026-04-17</em></p>
<p>Cloudflare's network now supports redirecting verified AI training crawlers to canonical URLs when they request deprecated or duplicate pages. When enabled via <strong>AI Crawl Control</strong> &gt; <strong>Quick Actions</strong>, AI training crawlers that request a page with a canonical tag pointing elsewhere receive a 301 redirect to the canonical version. Humans, search engine crawlers, and AI Search agents continue to see the original page normally.</p>
<p>This feature leverages your existing <code>&lt;link rel=&quot;canonical&quot;&gt;</code> tags. No additional configuration required beyond enabling the toggle. Available on Pro, Business, and Enterprise plans at no additional cost.</p>
<p>Refer to the <a href="/ai-crawl-control/reference/redirects-for-ai-training/">Redirects for AI Training documentation</a> for details.</p>


<h2 id="tools-to-prepare-your-site-for-the-agentic-internet"><a href="/changelog/post/2026-04-17-tools-for-agentic-internet/">Tools to prepare your site for the agentic Internet</a></h2>
<p><em>2026-04-17</em></p>
<p>AI Crawl Control now includes new tools to help you prepare your site for the agentic Internet—a web where AI agents are first-class citizens that discover and interact with content differently than human visitors.</p>
<h4 id="2026-04-17-tools-for-agentic-internet-content-format-insights">Content Format insights</h4>
<p>The <strong>Metrics</strong> tab now includes a <strong>Content Format</strong> chart showing what content types AI systems request versus what your origin serves. Understanding these patterns helps you optimize content delivery for both human and agent consumption.</p>
<h4 id="2026-04-17-tools-for-agentic-internet-directives-tab-formerly-robots-txt">Directives tab (formerly Robots.txt)</h4>
<p>The <strong>Robots.txt</strong> tab has been renamed to <strong>Directives</strong> and now includes a link to check your site's <a href="https://isitagentready.com">Agent Readiness</a> score.</p>
<p>Refer to our <a href="https://blog.cloudflare.com/agent-readiness/">blog post on preparing for the agentic Internet</a> for more on why these capabilities matter.</p>


<h2 id="new-tenantid-and-firewall-for-ai-fields-in-logpush-datasets"><a href="/changelog/post/2026-04-15-logpush-new-fields/">New TenantID and Firewall for AI fields in Logpush datasets</a></h2>
<p><em>2026-04-15</em></p>
<p>Cloudflare has added new fields to multiple <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-04-15-logpush-new-fields-tenantid-field">TenantID field</h4>
<p>The following Gateway and Zero Trust datasets now include a <code>TenantID</code> field:</p>
<ul>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/#tenantid">Gateway DNS</a></strong>: Identifies the tenant ID of the DNS request, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_http/#tenantid">Gateway HTTP</a></strong>: Identifies the tenant ID of the HTTP request, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_network/#tenantid">Gateway Network</a></strong>: Identifies the tenant ID of the network session, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#tenantid">Zero Trust Network Sessions</a></strong>: Identifies the tenant ID of the network session, if it exists.</li>
</ul>
<h4 id="2026-04-15-logpush-new-fields-firewall-for-ai-fields">Firewall for AI fields</h4>
<p>The following datasets now include <a href="/api-shield/security/volumetric-abuse-detection/#firewall-for-ai">Firewall for AI</a> fields:</p>
<ul>
<li>
<p><strong><a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">Firewall Events</a></strong>:</p>
<ul>
<li><code>FirewallForAIInjectionScore</code>: The score indicating the likelihood of a prompt injection attack in the request.</li>
<li><code>FirewallForAIPIICategories</code>: List of PII categories detected in the request.</li>
<li><code>FirewallForAITokenCount</code>: The number of tokens in the request.</li>
<li><code>FirewallForAIUnsafeTopicCategories</code>: List of unsafe topic categories detected in the request.</li>
</ul>
</li>
<li>
<p><strong><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP Requests</a></strong>:</p>
<ul>
<li><code>FirewallForAIInjectionScore</code>: The score indicating the likelihood of a prompt injection attack in the request.</li>
<li><code>FirewallForAIPIICategories</code>: List of PII categories detected in the request.</li>
<li><code>FirewallForAITokenCount</code>: The number of tokens in the request.</li>
<li><code>FirewallForAIUnsafeTopicCategories</code>: List of unsafe topic categories detected in the request.</li>
</ul>
</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="improved-oauth-experience-for-consent-and-management"><a href="/changelog/post/2026-04-14-oauth-consent-and-revoke/">Improved OAuth experience for consent and management</a></h2>
<p><em>2026-04-14</em></p>
<p>OAuth allows third-party applications to access your Cloudflare account on your behalf — like when Wrangler deploys Workers or when monitoring tools read your analytics. You now have <strong>granular control</strong> over which accounts these applications can access, plus the ability to revoke access anytime.</p>
<h4 id="2026-04-14-oauth-consent-and-revoke-what-s-new">What's new</h4>
<h4 id="2026-04-14-oauth-consent-and-revoke-choose-which-accounts-to-authorize">Choose which accounts to authorize</h4>
When authorizing an OAuth application, you can now **select specific accounts** instead of granting access to all your accounts:
- **Account-by-account selection** — Choose exactly which accounts the application can access
- **"All accounts" option** — Still available for trusted tools like Wrangler
This gives you precise control who can access your data.
<h4 id="2026-04-14-oauth-consent-and-revoke-clear-consent-screens">Clear consent screens</h4>
The OAuth consent screen now shows:
- **What the application can access** — Explicit list of permissions being requested
- **Who created the application** — Application owner and contact information  
- **Which accounts you're authorizing** — Checkboxes for account selection
<h4 id="2026-04-14-oauth-consent-and-revoke-revoke-access-anytime">Revoke access anytime</h4>
Manage authorized OAuth applications from your profile:
- **See all connected apps** — View every OAuth application with access to your accounts
- **Review permissions and scope** — Check what each application can do and which accounts it can access
- **Revoke instantly** — Remove access with one click when you no longer need it
To manage your OAuth applications, navigate to **Profile** > **Access Management** > **[Connected Applications](https://dash.cloudflare.com/profile/access-management/authorization)**.
<h4 id="2026-04-14-oauth-consent-and-revoke-why-this-matters">Why this matters</h4>
These updates give you:
- **Granular control** — Authorize apps per-account instead of all-or-nothing
- **Transparency** — Know exactly what you're authorizing before you consent
- **Security** — Limit blast radius by restricting access to only necessary accounts
- **Easy cleanup** — Revoke access when applications are no longer needed
<h4 id="2026-04-14-oauth-consent-and-revoke-learn-more">Learn more</h4>
Read more about these improvements in our blog post: [Improving the OAuth consent experience](https://blog.cloudflare.com/improved-developer-security/#improving-the-oauth-consent-experience).


<h2 id="logpush-to-bigquery-cloudflare-dashboard-support"><a href="/changelog/post/2026-04-14-bigquery-dashboard-support/">Logpush to BigQuery — Cloudflare dashboard support</a></h2>
<p><em>2026-04-14</em></p>
<p>You can now configure Logpush jobs to Google BigQuery directly from the Cloudflare dashboard, in addition to the existing API-based setup.</p>
<p>Previously, setting up a BigQuery Logpush destination required using the Logpush API. Now you can create and manage BigQuery Logpush jobs from the <strong>Logpush</strong> page in the Cloudflare dashboard by selecting <strong>Google BigQuery</strong> as the destination and entering your Google Cloud project ID, dataset ID, table ID, and service account credentials.</p>
<p>For more information, refer to <a href="/logs/logpush/logpush-job/enable-destinations/bigquery/">Enable Logpush to Google BigQuery</a>.</p>


<h2 id="api-tokens-now-detectable-by-secret-scanning-tools"><a href="/changelog/post/2026-04-10-secret-scanning-support/">API tokens now detectable by secret scanning tools</a></h2>
<p><em>2026-04-10</em></p>
<p>Cloudflare API tokens now include <strong>identifiable patterns</strong> that enable secret scanning tools to automatically detect them when leaked in code repositories, configuration files, or other public locations.</p>
<h4 id="2026-04-10-secret-scanning-support-what-changed">What changed</h4>
<p>API tokens generated by Cloudflare now follow a standardized format that secret scanning tools can recognize. When a Cloudflare token is accidentally committed to GitHub, GitLab, or another platform with secret scanning enabled, the tool will flag it and alert you.</p>
<h4 id="2026-04-10-secret-scanning-support-why-this-matters">Why this matters</h4>
<p>Leaked credentials are a common security risk. By making Cloudflare tokens detectable by scanning tools, you can:</p>
<ul>
<li><strong>Detect leaks faster</strong> — Get notified immediately when a token is exposed.</li>
<li><strong>Reduce risk window</strong> — Exposed tokens are deactivated immediately, before they can be exploited.</li>
<li><strong>Automate security</strong> — Leverage existing secret scanning infrastructure without additional configuration.</li>
</ul>
<h4 id="2026-04-10-secret-scanning-support-what-happens-when-a-leak-is-detected">What happens when a leak is detected</h4>
<p>When a third-party secret scanning tool detects a leaked Cloudflare API token:</p>
<ol>
<li><strong>Cloudflare immediately deactivates the token</strong> to prevent unauthorized access.</li>
<li><strong>The token creator receives an email notification</strong> alerting them to the leak.</li>
<li><strong>The token is marked as &quot;Exposed&quot;</strong> in the Cloudflare dashboard.</li>
<li><strong>You can then roll or delete the token</strong> from the token management pages.</li>
</ol>
<h4 id="2026-04-10-secret-scanning-support-supported-platforms">Supported platforms</h4>
<ul>
<li><strong>GitHub Secret Scanning</strong> — Automatically enabled for public repositories</li>
</ul>
<p>For more information on token formats and secret scanning, refer to <a href="/fundamentals/api/get-started/token-formats/">API token formats</a>.</p>


<h2 id="redesigned-support-portal-for-faster-personalized-help"><a href="/changelog/post/2026-04-06-redesigned-support-portal/">Redesigned Support Portal for faster, personalized help</a></h2>
<p><em>2026-04-07</em></p>
<h4 id="2026-04-06-redesigned-support-portal-redesigned-get-help-portal-for-faster-personalized-help">Redesigned &quot;Get Help&quot; Portal for faster, personalized help</h4>
<p>Cloudflare has officially launched a redesigned &quot;Get Help&quot; Support Portal to eliminate friction and get you to a resolution faster. Previously, navigating support meant clicking through multiple tiles, categorizing your own technical issues across 50+ conditional fields, and translating your problem into Cloudflare's internal taxonomy.</p>
<p>The new experience replaces that complexity with a personalized front door built around your specific account plan. Whether you are under a DDoS attack or have a simple billing question, the portal now presents a single, clean page that surfaces the direct paths available to you — such as &quot;Ask AI&quot;, &quot;Chat with a human&quot;, or &quot;Community&quot; — without the manual triage.</p>
<h4 id="2026-04-06-redesigned-support-portal-what-s-new">What's New</h4>
<ul>
<li><strong>One Page, Clear Choices</strong>: No more navigating a grid of overlapping categories. The portal now uses action cards tailored to your plan (Free, Pro, Business, or Enterprise), ensuring you only see the support channels you can actually use.</li>
<li><strong>A Radically Simpler Support Form</strong>: We've reduced the ticket submission process from four+ screens and 50+ fields to a single screen with five critical inputs. You describe the issue in your own words, and our backend handles the categorization.</li>
<li><strong>AI-Driven Triage</strong>: Using <a href="https://developers.cloudflare.com/workers-ai/">Cloudflare Workers AI</a> and <a href="https://developers.cloudflare.com/vectorize/">Vectorize</a>, the portal now automatically generates case subjects and predicts product categories.</li>
</ul>
<h4 id="2026-04-06-redesigned-support-portal-moving-complexity-to-the-backend">Moving complexity to the backend</h4>
<p>Behind the scenes, we've moved the complexity from the user to our own developer stack. When you describe an issue, we use semantic embeddings to capture intent rather than just keywords.</p>
<p>By leveraging case-based reasoning, our system compares your request against millions of resolved cases to route your inquiry to the specialist best equipped to help. This ensures that while the front-end experience is simpler for you, the back-end routing is more accurate than ever.</p>
<p>To learn more, refer to the <a href="/support/contacting-cloudflare-support/">Support documentation</a> or select <strong>Get Help</strong> directly in the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a>.</p>


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


<h2 id="new-responsetimems-field-in-gateway-dns-logpush-dataset"><a href="/changelog/post/2026-04-06-gateway-dns-response-time-ms/">New ResponseTimeMs field in Gateway DNS Logpush dataset</a></h2>
<p><em>2026-04-06</em></p>
<p>Cloudflare has added a new field to the <a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/#responsetimems">Gateway DNS</a> Logpush dataset:</p>
<ul>
<li><strong>ResponseTimeMs</strong>: Total response time of the DNS request in milliseconds.</li>
</ul>
<p>For the complete field definitions, refer to <a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/">Gateway DNS dataset</a>.</p>


<h2 id="bigquery-as-logpush-destination"><a href="/changelog/post/2026-04-02-bigquery-destination/">BigQuery as Logpush destination</a></h2>
<p><em>2026-04-02</em></p>
<p>Cloudflare Logpush now supports <strong>BigQuery</strong> as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://cloud.google.com/bigquery">Google Cloud BigQuery</a> via <a href="/logs/logpush/">Logpush</a>. The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/bigquery/">Destination Configuration</a> documentation.</p>


<h2 id="new-quic-rtt-and-delivery-rate-fields"><a href="/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/">New QUIC RTT and delivery rate fields</a></h2>
<p><em>2026-04-01</em></p>
<p>Two new fields are now available in rule expressions that surface Layer 4 transport telemetry from the client connection. Together with the existing <a href="/ruleset-engine/rules-language/fields/reference/"><code>cf.timings.client_tcp_rtt_msec</code></a> field, these fields give you a complete picture of connection quality for both TCP and QUIC traffic — enabling transport-aware rules without requiring any client-side changes.</p>
<p>Previously, QUIC RTT and delivery rate data was only available via the <code>Server-Timing: cfL4</code> response header. These new fields make the same data available directly in rule expressions, so you can use them in Transform Rules, WAF Custom Rules, and other phases that support dynamic fields.</p>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-new-fields">New fields</h4>
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
<td><code>cf.timings.client_quic_rtt_msec</code></td>
<td>Integer</td>
<td>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only populated for QUIC (HTTP/3) connections. Returns <code>0</code> for TCP connections.</td>
</tr>
<tr>
<td><code>cf.edge.l4.delivery_rate</code></td>
<td>Integer</td>
<td>The most recent data delivery rate estimate for the client connection, in bytes per second. Returns <code>0</code> when L4 statistics are not available for the request.</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-example-route-slow-connections-to-a-lightweight-origin">Example: Route slow connections to a lightweight origin</h4>
<p>Use a request header transform rule to tag requests from high-latency connections, so your origin can serve a lighter page variant:</p>
<p><strong>Rule expression:</strong></p>
<pre><code class="language-txt">cf.timings.client_tcp_rtt_msec &gt; 200 or cf.timings.client_quic_rtt_msec &gt; 200&#10;</code></pre>
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
<td><code>X-High-Latency</code></td>
<td><code>true</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-example-match-low-bandwidth-connections">Example: Match low-bandwidth connections</h4>
<pre><code class="language-txt">cf.edge.l4.delivery_rate &gt; 0 and cf.edge.l4.delivery_rate &lt; 100000&#10;</code></pre>
<p>For more information, refer to <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a> and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="logpush-more-granular-timestamps"><a href="/changelog/post/2026-03-25-logpush-granular-timestamps/">Logpush — More granular timestamps</a></h2>
<p><em>2026-03-25</em></p>
<p>Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>To use the new formats, set <code>timestamp_format</code> in your Logpush job's <code>output_options</code>:</p>
<ul>
<li><code>rfc3339ms</code> — <code>2024-02-17T23:52:01.123Z</code></li>
<li><code>rfc3339ns</code> — <code>2024-02-17T23:52:01.123456789Z</code></li>
</ul>
<p>Default timestamp formats apply unless explicitly set. The dashboard defaults to <code>rfc3339</code> and the API defaults to <code>unixnano</code>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/log-output-options/">Log output options</a> documentation.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/core-platform/2/">Previous</a><span>Page 3 of 8</span><a class="pagination-next" rel="next" href="/changelog/product-group/core-platform/4/">Next</a></nav>
