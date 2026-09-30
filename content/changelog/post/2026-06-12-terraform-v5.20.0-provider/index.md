---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/
  description: New updates and improvements at Cloudflare.
  full_title: Terraform v5.20.0 now available · Changelog
  head_html: <title>Terraform v5.20.0 now available · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Terraform v5.20.0 now available · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/#page","headline":"Terraform v5.20.0 now available \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-12-terraform-v5.20.0-provider/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 12, 2026</time><h2 id="post-title">Terraform v5.20.0 now available</h2>
<div class="changelog-badges"><span>terraform</span></div><div class="changelog-body"><p>Cloudflare's Terraform v5 Provider makes it easy for developers to manage their Cloudflare infrastructure using a configuration as code approach. It releases every <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 weeks</a> to ensure that you can always manage the latest features in the platform. This week, we launched Terraform v5.20.0, which adds 24 new resources, bumps the underlying Go SDK to cloudflare-go v7, and includes a range of bug fixes and state upgraders based on community feedback.</p>
<h4 id="new-resources">New resources</h4>
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
<h4 id="features">Features</h4>
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
<h4 id="bug-fixes">Bug fixes</h4>
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
<h4 id="refactors">Refactors</h4>
<p>Extracted <code>MoveState</code> nil guard into shared helper</p>
<h4 id="for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Version 5 Migration Guide](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)
</div></article></div>
