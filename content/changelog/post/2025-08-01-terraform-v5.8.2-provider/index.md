---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/
  description: New updates and improvements at Cloudflare.
  full_title: Terraform v5.8.2 now available · Changelog
  head_html: <title>Terraform v5.8.2 now available · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Terraform v5.8.2 now available · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/#page","headline":"Terraform v5.8.2 now available \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-01-terraform-v5.8.2-provider/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 1, 2025</time><h2 id="post-title">Terraform v5.8.2 now available</h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and reliability. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<h4 id="changes">Changes</h4>
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
<h4 id="issues-closed">Issues Closed</h4>
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
<h4 id="upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div></article></div>
