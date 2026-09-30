<h1 id="changelog">Changelog</h1>

<h2 id="dedicated-egress-ip-for-logpush"><a href="/changelog/post/2025-08-22-dedicated-egress-ip-logpush/">Dedicated Egress IP for Logpush</a></h2>
<p><em>2025-08-22</em></p>
<p>Cloudflare Logpush can now deliver logs from using fixed, dedicated egress IPs. By routing Logpush traffic through a Cloudflare zone enabled with <a href="/smart-shield/configuration/dedicated-egress-ips/">Aegis IP</a>, your log destination only needs to allow Aegis IPs making setup more secure.</p>
<p>Highlights:</p>
<ul>
<li>Fixed egress IPs ensure your destination only accepts traffic from known addresses.</li>
<li>Works with any supported Logpush destination.</li>
<li>Recommended to use a dedicated zone as a proxy for easier management.</li>
</ul>
<p>To get started, work with your Cloudflare account team to provision Aegis IPs, then configure your Logpush job to deliver logs through the proxy zone. For full setup instructions, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/egress-ip/">Logpush documentation</a>.</p>


<h2 id="extended-retention"><a href="/changelog/post/2025-08-15-extended-retention/">Extended retention</a></h2>
<p><em>2025-08-15</em></p>
<p>Customers can now rely on Log Explorer to meet their log retention compliance requirements.</p>
<p>Contract customers can choose to store their logs in Log Explorer for up to two years, at an additional cost of $0.10 per GB per month. Customers interested in this feature can contact their account team to have it added to their contract.</p>


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


<h2 id="ibm-cloud-logs-as-logpush-destination"><a href="/changelog/post/2025-08-13-ibm-cloud-logs-destination/">IBM Cloud Logs as Logpush destination</a></h2>
<p><em>2025-08-13</em></p>
<p>Cloudflare Logpush now supports IBM Cloud Logs as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://www.ibm.com/products/cloud-logs">IBM Cloud Logs</a> via <a href="/logs/logpush/">Logpush</a>. The setup can be done through the Logpush UI in the Cloudflare Dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>. The integration requires IBM Cloud Logs HTTP Source Address and an IBM API Key. The feature also allows for filtering events and selecting specific log fields.</p>
<p>For more information, refer to <a href="/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/">Destination Configuration</a> documentation.</p>


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


<h2 id="audit-logs-version-2-ui-beta-release"><a href="/changelog/post/2025-07-29-audit-logs-v2-ui-beta/">Audit logs (version 2) - UI Beta Release</a></h2>
<p><em>2025-07-29</em></p>
<p>The Audit Logs v2 UI is now available to all Cloudflare customers in Beta. This release builds on the public <a href="/changelog/product/audit-logs/">Beta of the Audit Logs v2 API</a> and introduces a redesigned user interface with powerful new capabilities to make it easier to investigate account activity.</p>
<p><strong>Enabling the new UI</strong></p>
<p>To try the new user interface, go to <strong>Manage Account &gt; Audit Logs</strong>. The previous version of Audit Logs remains available and can be re-enabled at any time using the <strong>Switch back to old Audit Logs</strong> link in the banner at the top of the page.</p>
<p><strong>New Features:</strong></p>
<ul>
<li><strong>Advanced Filtering</strong>: Filter logs by actor, resource, method, and more for faster insights.</li>
<li><strong>On-hover filter controls</strong>: Easily include or exclude values in queries by hovering over fields within a log entry.</li>
<li><strong>Detailed Log Sidebar</strong>: View rich context for each log entry without leaving the main view.</li>
<li><strong>JSON Log View</strong>: Inspect the raw log data in a structured JSON format.</li>
<li><strong>Custom Time Ranges</strong>: Define your own time windows to view historical activity.</li>
<li><strong>Infinite Scroll</strong>: Seamlessly browse logs without clicking through pages.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_filters.png" alt="Audit Logs v2 new UI" /></p>
<p>For more details on Audit Logs v2, see the <a href="https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>
<p><strong>Known issues</strong></p>
<ul>
<li>A small number of audit logs may currently be unavailable in Audit Logs v2. In some cases, certain fields such as actor information may be missing in certain audit logs. We are actively working to improve coverage and completeness for General Availability.</li>
<li>Export to CSV is not supported in the new UI.</li>
</ul>
<p>We are actively refining the Audit Logs v2 experience and welcome your feedback. You can share overall feedback by clicking the thumbs up or thumbs down icons at the top of the page, or provide feedback on specific audit log entries using the thumbs icons next to each audit log line or by filling out our <a href="https://docs.google.com/forms/d/e/1FAIpQLSfXGkJpOG1jUPEh-flJy9B13icmcdBhveFwe-X0EzQjJQnQfQ/viewform?usp=sharing">feedback form</a>.</p>


<h2 id="faster-more-reliable-udp-traffic-for-cloudflare-tunnel"><a href="/changelog/post/2025-07-15-udp-improvements/">Faster, more reliable UDP traffic for Cloudflare Tunnel</a></h2>
<p><em>2025-07-15</em></p>
<p>Your real-time applications running over <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> are now faster and more reliable. We've completely re-architected the way <code>cloudflared</code> proxies UDP traffic in order to isolate it from other traffic, ensuring latency-sensitive applications like private DNS are no longer slowed down by heavy TCP traffic (like file transfers) on the same Tunnel.</p>
<p>This is a foundational improvement to Cloudflare Tunnel, delivered automatically to all customers. There are no settings to configure — your UDP traffic is already flowing faster and more reliably.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Faster UDP performance</strong>: We've significantly reduced the latency for establishing new UDP sessions, making applications like private DNS much more responsive.</li>
<li><strong>Greater reliability for mixed traffic</strong>: UDP packets are no longer affected by heavy TCP traffic, preventing timeouts and connection drops for your real-time services.</li>
</ul>
<p>Learn more about running <a href="/reference-architecture/architectures/sase/#connecting-applications">TCP or UDP applications</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private networks</a> through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>


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


<h2 id="usage-tracking"><a href="/changelog/post/2025-07-09-usage-tracking/">Usage tracking</a></h2>
<p><em>2025-07-09</em></p>
<p><a href="/log-explorer/">Log Explorer</a> customers can now monitor their data ingestion volume to keep track of their billing. Monthly usage is displayed at the top of the <a href="/log-explorer/log-search/">Log Search</a> and <a href="/log-explorer/manage-datasets/">Manage Datasets</a> screens in Log Explorer.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/ingested-data.png" alt="Ingested data" /></p>


<h2 id="introducing-pay-per-crawl-private-beta"><a href="/changelog/post/2025-07-01-pay-per-crawl/">Introducing Pay Per Crawl (private beta)</a></h2>
<p><em>2025-07-01</em></p>
<p>We are introducing a new feature of <a href="/ai-crawl-control/">AI Crawl Control</a> — Pay Per Crawl. <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Pay Per Crawl</a> enables site owners to require payment from AI crawlers every time the crawlers access their content, thereby fostering a fairer Internet by enabling site owners to control and monetize how their content gets used by AI.</p>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/pay-per-crawl.png" alt="Pay per crawl" /></p>
<p><strong>For Site Owners:</strong></p>
<ul>
<li>Set pricing and select which crawlers to charge for content access</li>
<li>Manage payments via Stripe</li>
<li>Monitor analytics on successful content deliveries</li>
</ul>
<p><strong>For AI Crawler Owners:</strong></p>
<ul>
<li>Use HTTP headers to request and accept pricing</li>
<li>Receive clear confirmations on charges for accessed content</li>
</ul>
<p>Learn more in the <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Pay Per Crawl documentation</a>.</p>


<h2 id="ai-crawl-control-refresh"><a href="/changelog/post/2025-07-01-refresh/">AI Crawl Control refresh</a></h2>
<p><em>2025-07-01</em></p>
<p>We redesigned the AI Crawl Control dashboard to provide more intuitive and granular control over AI crawlers.</p>
<ul>
<li>From the new <strong>AI Crawlers</strong> tab: block specific AI crawlers.</li>
<li>From the new <strong>Metrics</strong> tab: view AI Crawl Control metrics.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/manage-ai-crawlers.png" alt="Block AI crawlers" /></p>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/analyze-metrics.png" alt="Analyze AI crawler activity" /></p>
<p>To get started, explore:</p>
<ul>
<li><a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a>.</li>
<li><a href="/ai-crawl-control/features/analyze-ai-traffic/">Analyze AI traffic</a>.</li>
</ul>


<h2 id="cloudflare-user-groups-scim-user-groups-are-now-in-ga"><a href="/changelog/post/2025-06-23-user-groups-ga/">Cloudflare User Groups & SCIM User Groups are now in GA</a></h2>
<p><em>2025-06-23</em></p>
<p>We're announcing the GA of <strong>User Groups for Cloudflare Dashboard</strong> and <strong>System for Cross Domain Identity Management (SCIM) User Groups</strong>, strengthening our RBAC capabilities with stable, production-ready primitives for managing access at scale.</p>
<p><strong>What's New</strong></p>
<p><strong>User Groups [GA]</strong>: <a href="/fundamentals/manage-members/user-groups/">User Groups</a> are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.</p>
<p><strong>SCIM User Groups [GA]</strong>: Centralize &amp; simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.</p>
<p><strong>Stability &amp; Scale</strong>:
These features have undergone extensive testing during the Public Beta period and are now ready for production use across enterprises of all sizes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17727.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/manage-members/user-groups/">Get started with User Groups</a></li>
<li><a href="/fundamentals/account/account-security/scim-setup/">Explore our SCIM integration guide</a></li>
</ul>


<h2 id="log-explorer-is-ga"><a href="/changelog/post/2025-06-18-log-explorer-ga/">Log Explorer is GA</a></h2>
<p><em>2025-06-18</em></p>
<p><a href="/log-explorer/">Log Explorer</a> is now GA, providing native observability and forensics for traffic flowing through Cloudflare.</p>
<p>Search and analyze your logs, natively in the Cloudflare dashboard. These logs are also stored in Cloudflare's network, eliminating many of the costs associated with other log providers.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/log-explorer-dash.png" alt="Log Explorer dashboard" /></p>
<p>With Log Explorer, you can now:</p>
<ul>
<li><strong>Monitor security and performance issues with custom dashboards</strong> – use natural language to define charts for measuring response time, error rates, top statistics and more.</li>
<li><strong>Investigate and troubleshoot issues with Log Search</strong> – use data type-aware search filters or custom sql to investigate detailed logs.</li>
<li><strong>Save time and collaborate with saved queries</strong> – save Log Search queries for repeated use or sharing with other users in your account.</li>
<li><strong>Access Log Explorer at the account and zone level</strong> – easily find Log Explorer at the account and zone level for querying any dataset.</li>
</ul>
<p>For help getting started, refer to <a href="/log-explorer/">our documentation</a>.</p>


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


<h2 id="more-flexible-fallback-handling-custom-errors-now-support-fetching-assets-returned-with-4xx-or-5xx-status-codes"><a href="/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/">More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes</a></h2>
<p><em>2025-06-09</em></p>
<p><a href="/rules/custom-errors/">Custom Errors</a> can now fetch and store <a href="/rules/custom-errors/create-rules/#create-a-custom-error-asset-dashboard">assets</a> and <a href="/rules/custom-errors/#error-pages">error pages</a> from your origin even if they are served with a 4xx or 5xx HTTP status code — previously, only 200 OK responses were allowed.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>You can now upload error pages and error assets that return error status codes (for example, 403, 500, 502, 503, 504) when fetched.</li>
<li>These assets are stored and minified at the edge, so they can be reused across multiple Custom Error rules without triggering requests to the origin.</li>
</ul>
<p>This is especially useful for retrieving error content or downtime banners from your backend when you can’t override the origin status code.</p>
<p>Learn more in the <a href="/rules/custom-errors/">Custom Errors</a> documentation.</p>


<h2 id="match-workers-subrequests-by-upstream-zone-cf-worker-upstream-zone-now-supported-in-transform-rules"><a href="/changelog/post/2025-06-09-transform-rule-subrequest-matching/">Match Workers subrequests by upstream zone — cf.worker.upstream_zone now supported in Transform Rules</a></h2>
<p><em>2025-06-09</em></p>
<p>You can now use the <a href="/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/"><code>cf.worker.upstream_zone</code></a> field in <a href="/rules/transform/">Transform Rules</a> to control rule execution based on whether a request originates from <a href="/workers/">Workers</a>, including subrequests issued by Workers in other zones.</p>
<p><img src="/assets/upstream/images/changelog/rules/transform-rule-subrequest-matching.png" alt="Match Workers subrequests by upstream zone in Transform Rules" /></p>
<p><strong>What's new:</strong></p>
<ul>
<li><code>cf.worker.upstream_zone</code> is now supported in Transform Rules expressions.</li>
<li>Skip or apply logic conditionally when handling <a href="/workers/platform/limits/#subrequests">Workers subrequests</a>.</li>
</ul>
<p>For example, to add a header when the subrequest comes from another zone:</p>
<div class="nb-example"><h3 class="nb-component-title" id="2025-06-09-transform-rule-subrequest-matching-example">Example</h3>
@markup("md", "content/.markup/bodies/17746.md")</div>
<p>This gives you more granular control in how you handle incoming requests for your zone.</p>
<p>Learn more in the <a href="/rules/transform/">Transform Rules</a> documentation and <a href="/ruleset-engine/rules-language/fields/reference/">Rules language fields</a> reference.</p>


<h2 id="cloudflare-user-groups-enhanced-permission-policies-are-now-in-beta"><a href="/changelog/post/2025-06-02-user-groups-beta/">Cloudflare User Groups & Enhanced Permission Policies are now in Beta</a></h2>
<p><em>2025-06-02</em></p>
<p>We're excited to announce the Public Beta launch of <strong>User Groups for Cloudflare Dashboard</strong> and <strong>System for Cross Domain Identity Management (SCIM) User Groups</strong>, expanding our RBAC capabilities to simplify user and group management at scale.</p>
<p>We've also visually overhauled the <strong>Permission Policies UI</strong> to make defining permissions more intuitive.</p>
<p><strong>What's New</strong></p>
<p><strong>User Groups [BETA]</strong>: <a href="/fundamentals/manage-members/user-groups/">User Groups</a> are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.</p>
<p><strong>SCIM User Groups [BETA]</strong>: Centralize &amp; simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17726.md")</aside>
<p><strong>Revamped Permission Policies UI [BETA]</strong>: As Cloudflare's services have grown, so has the need for precise, role-based access control. We've given the Permission Policies builder a visual overhaul to make it much easier for administrators to find and define the exact permissions they want for specific principals.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-06-02-permissions-policy-ux.png" alt="Updated Permissions Policy UX" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17725.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/manage-members/user-groups/">Get started with User Groups</a></li>
<li><a href="/fundamentals/account/account-security/scim-setup/">Explore our SCIM integration guide</a></li>
</ul>


<h2 id="fine-tune-image-optimization-webp-now-supported-in-configuration-rules"><a href="/changelog/post/2025-05-30-configuration-rules-webp/">Fine-tune image optimization — WebP now supported in Configuration Rules</a></h2>
<p><em>2025-05-30</em></p>
<p>You can now enable <a href="/images/polish/activate-polish/">Polish</a> with the <code>webp</code> format directly in <a href="/rules/configuration-rules/">Configuration Rules</a>, allowing you to optimize image delivery for specific routes, user agents, or A/B tests — without applying changes zone-wide.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><a href="/images/polish/compression/#webp">WebP</a> is now a supported <a href="/rules/configuration-rules/settings/#polish">value</a> in the <strong>Polish</strong> setting for Configuration Rules.</li>
</ul>
<p>This gives you more precise control over how images are compressed and delivered, whether you're targeting modern browsers, running experiments, or tailoring performance by geography or device type.</p>
<p>Learn more in the <a href="/images/polish/">Polish</a> and <a href="/rules/configuration-rules/">Configuration Rules</a> documentation.</p>


<h2 id="new-graphql-analytics-api-explorer-and-mcp-server"><a href="/changelog/post/2025-05-23-graphql-api-explorer/">New GraphQL Analytics API Explorer and MCP Server</a></h2>
<p><em>2025-05-23</em></p>
<p>We’ve launched two powerful new tools to make the GraphQL Analytics API more accessible:</p>
<h4 id="2025-05-23-graphql-api-explorer-graphql-api-explorer">GraphQL API Explorer</h4>
<p>The new <a href="https://graphql.cloudflare.com/explorer">GraphQL API Explorer</a> helps you build, test, and run queries directly in your browser. Features include:</p>
<ul>
<li>In-browser schema documentation to browse available datasets and fields</li>
<li>Interactive query editor with autocomplete and inline documentation</li>
<li>A &quot;Run in GraphQL API Explorer&quot; button to execute example queries from our docs</li>
<li>Seamless OAuth authentication — no manual setup required</li>
</ul>
<p><img src="/assets/upstream/images/changelog/analytics/graphql-api-explorer.png" alt="GraphQL API Explorer" /></p>
<h4 id="2025-05-23-graphql-api-explorer-graphql-model-context-protocol-mcp-server">GraphQL Model Context Protocol (MCP) Server</h4>
<p>MCP Servers let you use natural language tools like Claude to generate structured queries against your data. See our <a href="https://blog.cloudflare.com/thirteen-new-mcp-servers-from-cloudflare/">blog post</a> for details on how they work and which servers are available. The new <a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql">GraphQL MCP server</a> helps you discover and generate useful queries for the GraphQL Analytics API. With this server, you can:</p>
<ul>
<li>Explore what data is available to query</li>
<li>Generate and refine queries using natural language, with one-click links to run them in the API Explorer</li>
<li>Build dashboards and visualizations from structured query outputs</li>
</ul>
<p>Example prompts include:</p>
<ul>
<li>“Show me HTTP traffic for the last 7 days for example.com”</li>
<li>“What GraphQL node returns firewall events?”</li>
<li>“Can you generate a link to the Cloudflare GraphQL API Explorer with a pre-populated query and variables?”</li>
</ul>
<p>We’re continuing to expand these tools, and your feedback helps shape what’s next. <a href="/analytics/graphql-api/">Explore the documentation</a> to learn more and get started.</p>


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


<h2 id="more-ways-to-match-snippets-now-support-custom-lists-bot-score-and-waf-attack-score"><a href="/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/">More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score</a></h2>
<p><em>2025-05-09</em></p>
<p>You can now use IP, Autonomous System (AS), and Hostname <a href="/waf/tools/lists/custom-lists/">custom lists</a> to route traffic to <a href="/rules/snippets/">Snippets</a> and <a href="/rules/cloud-connector/">Cloud Connector</a>, giving you greater precision and control over how you match and process requests at the edge.</p>
<p>In Snippets, you can now also match on <a href="/bots/concepts/bot-score/">Bot Score</a> and <a href="/waf/detections/attack-score/">WAF Attack Score</a>, unlocking smarter edge logic for everything from request filtering and mitigation to <a href="/rules/snippets/examples/slow-suspicious-requests/">tarpitting</a> and logging.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><a href="/waf/tools/lists/custom-lists/">Custom lists</a> matching – Snippets and Cloud Connector now support user-created IP, AS, and Hostname lists via dashboard or <a href="/api/resources/rules/subresources/lists/methods/list/">Lists API</a>. Great for shared logic across zones.</li>
<li><a href="/bots/concepts/bot-score/">Bot Score</a> and <a href="/waf/detections/attack-score/">WAF Attack Score</a> – Use Cloudflare’s intelligent traffic signals to detect bots or attacks and take advanced, tailored actions with just a few lines of code.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/rules/snippets-lists-scores.png" alt="New fields in Snippets" /></p>
<p>These enhancements unlock new possibilities for building smarter traffic workflows with minimal code and maximum efficiency.</p>
<p>Learn more in the <a href="/rules/snippets/">Snippets</a> and <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>


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


<h2 id="custom-errors-are-now-generally-available"><a href="/changelog/post/2025-04-24-custom-errors-ga/">Custom Errors are now Generally Available</a></h2>
<p><em>2025-04-24</em></p>
<p><a href="/rules/custom-errors/">Custom Errors</a> are now generally available for all paid plans — bringing a unified and powerful experience for customizing error responses at both the zone and account levels.</p>
<p>You can now manage <strong>Custom Error Rules</strong>, <strong>Custom Error Assets</strong>, and redesigned <strong>Error Pages</strong> directly from the Cloudflare dashboard. These features let you deliver tailored messaging when errors occur, helping you maintain brand consistency and improve user experience — whether it’s a 404 from your origin or a security challenge from Cloudflare.</p>
<p>What's new:</p>
<ul>
<li><strong>Custom Errors are now GA</strong> – Available on all paid plans and ready for production traffic.</li>
<li><strong>UI for Custom Error Rules and Assets</strong> – Manage your zone-level rules from the Rules &gt; Overview and your zone-level assets from the Rules &gt; Settings tabs.</li>
<li><strong>Define inline content or upload assets</strong> – Create custom responses directly in the rule builder, upload new or reuse previously stored assets.</li>
<li><strong>Refreshed UI and new name for Error Pages</strong> – Formerly known as “Custom Pages,” Error Pages now offer a cleaner, more intuitive experience for both zone and account-level configurations.</li>
<li><strong>Powered by Ruleset Engine</strong> – Custom Error Rules support <a href="/ruleset-engine/rules-language/">conditional logic</a> and override Error Pages for 500 and 1000 class errors, as well as errors originating from your origin or <a href="/ruleset-engine/reference/phases-list/">other Cloudflare products</a>. You can also configure <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> to add, change, or remove HTTP headers from responses returned by Custom Error Rules.</li>
</ul>
<p>Learn more in the <a href="/rules/custom-errors/">Custom Errors documentation</a>.</p>


<h2 id="custom-fields-raw-and-transformed-values-support"><a href="/changelog/post/2025-04-18-custom-fields-raw-transformed-values/">Custom fields raw and transformed values support</a></h2>
<p><em>2025-04-18</em></p>
<p>Custom Fields now support logging both <strong>raw and transformed values</strong> for request and response headers in the HTTP requests dataset.</p>
<p>These fields are configured per zone and apply to all Logpush jobs in that zone that include request headers, response headers. Each header can be logged in only one format—either raw or transformed—not both.</p>
<p>By default:</p>
<ul>
<li>Request headers are logged as raw values</li>
<li>Response headers are logged as transformed values</li>
</ul>
<p>These defaults can be overridden to suit your logging needs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17737.md")</aside>
<p>For more information refer to <a href="/logs/logpush/logpush-job/custom-fields/">Custom fields</a> documentation</p>


<h2 id="cloudflare-registrar-api-is-now-in-beta"><a href="/changelog/post/2026-04-15-registrar-api-beta/">Cloudflare Registrar API is now in beta</a></h2>
<p><em>2025-04-15</em></p>
<p>Cloudflare Registrar API is now in beta.</p>
<p>You can now use the Cloudflare API to:</p>
<ul>
<li>Search for domain names.</li>
<li>Check real-time availability and pricing.</li>
<li>Register supported domains programmatically.</li>
</ul>
<p>This beta supports a subset of popular extensions available through Cloudflare Registrar. Search returns suggestions across API-supported extensions, check confirms current availability and pricing, and registration starts a workflow that can complete immediately or be polled if it takes longer.</p>
<p>Because the Registrar API is part of the Cloudflare API, it can also be used in <a href="https://github.com/cloudflare/mcp">Cloudflare MCP</a> and other agent-driven workflows.</p>
<p>If you are using Cloudflare MCP or other agent-driven workflows, prompts can be as simple as:</p>
<ul>
<li><code>Search for domain ideas for a coffee shop based in Evergreen, Colorado.</code></li>
<li><code>Check whether example.com is available and show me the current price.</code></li>
<li><code>Register example.com</code></li>
</ul>
<p>For supported operations, extension availability, and workflow details, refer to:</p>
<ul>
<li><a href="https://developers.cloudflare.com/registrar/registrar-api/">Registrar API guide</a></li>
<li><a href="https://developers.cloudflare.com/api/resources/registrar">Registrar API reference</a></li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/core-platform/6/">Previous</a><span>Page 7 of 8</span><a class="pagination-next" rel="next" href="/changelog/product-group/core-platform/8/">Next</a></nav>
