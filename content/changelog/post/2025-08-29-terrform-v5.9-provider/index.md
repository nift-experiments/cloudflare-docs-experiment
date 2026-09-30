<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 29, 2025</time><h2 id="post-title">Terraform v5.9 now available</h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadence to ensure its stability and reliability, including the v5.9 release. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release, and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<p>This release includes a new resource, <code>cloudflare_snippet</code>, which replaces <code>cloudflare_snippets</code>. <code>cloudflare_snippet</code> is now considered deprecated but can still be used. Please utilize <code>cloudflare_snippet</code> as soon as possible.</p>
<h4 id="changes">Changes</h4>
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
<h4 id="issues-closed">Issues Closed</h4>
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
<h4 id="upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition. These do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
<li><a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub Repository</a></li>
</ul>
</div></article></div>
