---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/
  description: New updates and improvements at Cloudflare.
  full_title: Terraform v5.16.0 now available · Changelog
  head_html: <title>Terraform v5.16.0 now available · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Terraform v5.16.0 now available · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/#page","headline":"Terraform v5.16.0 now available \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-01-20-terraform-v5.16.0-provider/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 20, 2026</time><h2 id="post-title">Terraform v5.16.0 now available</h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>In January 2025, we announced the launch of the new Terraform v5 Provider. We greatly appreciate the proactive engagement and valuable feedback from the Cloudflare community following the v5 release. In response, we've established a consistent and rapid <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> for releasing targeted improvements, demonstrating our commitment to stability and reliability.</p>
<p>With the help of the community, we have a growing number of resources that we have marked as <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">stable</a>, with that list continuing to grow with every release. The most used <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">resources</a> are on track to be stable by the end of March 2026, when we will also be releasing a new migration tool to you migrate from v4 to v5 with ease.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="features">Features</h4>
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
<h4 id="bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>account_member</strong>: fix resource importability issues</li>
<li><strong>dns_record:</strong> remove unnecessary fmt.Sprintf wrapper around LoadTestCase call in test configuration helper function</li>
<li><strong>load_balancer:</strong> fix session_affinity_ttl type expectations to match Float64 in initial creation and Int64 after migration</li>
<li><strong>workers_kv:</strong> handle special characters correctly in URL encoding</li>
</ul>
<h4 id="documentation">Documentation</h4>
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
<h4 id="for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)
</div></article></div>
