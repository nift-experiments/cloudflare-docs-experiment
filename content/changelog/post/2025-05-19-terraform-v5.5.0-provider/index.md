---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/
  description: New updates and improvements at Cloudflare.
  full_title: Terraform v5.5.0 now available · Changelog
  head_html: <title>Terraform v5.5.0 now available · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Terraform v5.5.0 now available · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/#page","headline":"Terraform v5.5.0 now available \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-05-19-terraform-v5.5.0-provider/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 19, 2025</time><h2 id="post-title">Terraform v5.5.0 now available</h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.5.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="changes">Changes</h4>
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
<h4 id="issues-closed">Issues Closed</h4>
- [#5304: Importing cloudflare_zero_trust_gateway_policy invalid attribute filter value](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5304)
- [#5303: cloudflare_page_rule import does not set values for all of the fields in terraform state](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5303)
- [#5178: cloudflare_page_rule Page rule creation with redirect fails](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5178)
- [#5336: cloudflare_turnstile_wwidget not able to update](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5336)
- [#5418: cloudflare_cloud_connector_rules: Provider returned invalid result object after apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5418)
- [#5423: cloudflare_zone_setting: "Invalid value for zone setting always_use_https"](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5423)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div></article></div>
