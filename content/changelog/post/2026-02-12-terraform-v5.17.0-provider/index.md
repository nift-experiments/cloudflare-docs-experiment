---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/
  description: New updates and improvements at Cloudflare.
  full_title: Terraform v5.17.0 now available · Changelog
  head_html: <title>Terraform v5.17.0 now available · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Terraform v5.17.0 now available · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/#page","headline":"Terraform v5.17.0 now available \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-12-terraform-v5.17.0-provider/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 12, 2026</time><h2 id="post-title">Terraform v5.17.0 now available</h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>In January 2025, we announced the launch of the new Terraform v5 Provider. We
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
<h4 id="features">Features</h4>
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
<h4 id="bug-fixes">Bug Fixes</h4>
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
<h4 id="chores">Chores</h4>
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
<h4 id="for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)
</div></article></div>
