<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 20, 2025</time><h2 id="post-title">Terraform v5.13.0 now available</h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.13 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes new features, new resources and data sources, bug fixes, updates to our Developer Documentation, and more.</p>
<h4 id="breaking-change">Breaking Change</h4>
Please be aware that there are breaking changes for the `cloudflare_api_token` and `cloudflare_account_token` resources. These changes eliminate configuration drift caused by policy ordering differences in the Cloudflare API.
<p>For more specific information about the changes or the actions required, please see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.13.0">detailed Repository changelog</a>.</p>
<h4 id="features">Features</h4>
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
<h4 id="bug-fixes">Bug Fixes</h4>
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
<h4 id="upgrading">Upgrading</h4>
We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized. We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="for-more-info">For more info</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
</div></article></div>
