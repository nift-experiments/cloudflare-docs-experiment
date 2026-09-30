---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/
  description: New updates and improvements at Cloudflare.
  full_title: Terraform v5.19.0 now available · Changelog
  head_html: <title>Terraform v5.19.0 now available · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Terraform v5.19.0 now available · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/#page","headline":"Terraform v5.19.0 now available \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-24-terraform-v5.19.0-provider/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 24, 2026</time><h2 id="post-title">Terraform v5.19.0 now available</h2>
<div class="changelog-badges"><span>terraform</span></div><div class="changelog-body"><p>Terraform Provider v5.19.0 introduces 14 new resources spanning AI Gateway, Pipelines, R2 Data Catalog, User Groups, Vulnerability Scanner, Workers Observability, and Zero Trust capabilities. This release significantly improves the v4 to v5 migration experience with automatic state upgraders for 26 resources, working seamlessly with the new <a href="https://github.com/cloudflare/tf-migrate">tf-migrate CLI tool</a> to automate resource renames, attribute updates, and <code>moved</code> block generation. Together, these enhancements reduce manual migration effort and minimize risk when upgrading from v4 to v5.</p>
<p><strong>Note:</strong> <code>cmd/migrate</code> is deprecated in favor of <code>tf-migrate</code> and will be removed in a future release (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/pull/7062">#7062</a>)</p>
<h4 id="new-resources">New Resources</h4>
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
<h4 id="features">Features</h4>
<h4 id="v4-to-v5-migration-state-upgraders">V4 to V5 Migration State Upgraders</h4>
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
<h4 id="other-features">Other Features</h4>
<ul>
<li><strong>ruleset</strong>: Add <code>content_converter</code> and <code>redirects_for_ai_training</code> support to configuration rules</li>
<li><strong>zero_trust_gateway_logging</strong>: Make importable</li>
</ul>
<h4 id="bug-fixes">Bug Fixes</h4>
<h4 id="migration-state-management">Migration &amp; State Management</h4>
<ul>
<li><strong>account_member</strong>: Add UseStateForUnknown to status field to prevent drift</li>
<li><strong>authenticated_origin_pulls_settings</strong>: Fix no prior schema and no-op upgrade</li>
<li><strong>certificate_pack</strong>: Initialize empty lists instead of null in state upgrader to prevent drift</li>
<li><strong>migrations</strong>: Handle ambiguous schema_version state for v4/v5 coexistence</li>
<li><strong>zero_trust_access_policy</strong>: Fix nil pointer panic in state upgrader; set PriorSchema nil for v4 state upgrade</li>
</ul>
<h4 id="resource-specific-fixes">Resource-Specific Fixes</h4>
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
<h4 id="documentation">Documentation</h4>
<ul>
<li><strong>healthcheck</strong>: Update port description to clarify defaults</li>
<li>Add application-scoped access policy migration guidance</li>
<li>Update zone_settings_override migration guide for tf-migrate v2 workflow</li>
</ul>
<h4 id="for-more-information">For more information</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform Provider</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration">Version 5 Migration Guide</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div></article></div>
