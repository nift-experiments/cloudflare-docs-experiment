---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/
  description: Verify customer ownership of custom hostnames before proxying traffic.
  full_title: Hostname validation · Cloudflare for Platforms docs
  head_html: <title>Hostname validation · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Verify customer ownership of custom hostnames before proxying traffic."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/index.md"><meta property="og:title" content="Hostname validation · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Verify customer ownership of custom hostnames before proxying traffic."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/#page","headline":"Hostname validation \u00b7 Cloudflare for Platforms docs","description":"Verify customer ownership of custom hostnames before proxying traffic.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/
  schema: 1
---
<p>Before Cloudflare can proxy traffic through a custom hostname, we need to verify your customer's ownership of that hostname.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4120.md")
</aside>
<h2 id="options">Options</h2>
<p>If minimizing downtime is more important to you, refer to our <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/">pre-validation methods</a>.</p>
<p>If ease of use for your customers is more important, review our <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/">real-time validation methods</a>.</p>
<h2 id="hostname-validation-and-certificate-validation">Hostname validation and certificate validation</h2>
<p>Hostname validation and certificate validation use different tokens and API fields.</p>
<ul>
<li><code>ownership_verification</code> and <code>ownership_verification_http</code> validate hostname ownership and affect the custom hostname <code>status</code>.</li>
<li><code>ssl.validation_records</code> validates certificate issuance and affects <code>ssl.status</code>.</li>
</ul>
<p>For production traffic, the hostname should have <code>status: active</code>, <code>ssl.status: active</code>, and DNS that points to your SaaS target.</p>
<h2 id="limitations">Limitations</h2>
<p>Custom hostnames using another CDN are not compatible with Cloudflare for SaaS. Since Cloudflare must be able to validate your customer's ownership of the hostname you add, if their usage of another CDN obfuscates their DNS records, hostname validation will fail.</p>
<h2 id="migrate-a-hostname-from-another-saas-provider">Migrate a hostname from another SaaS provider</h2>
<p>If you are onboarding a hostname that is currently active on another Cloudflare for SaaS provider, follow these steps to minimize downtime:</p>
<ol>
<li>Create the custom hostname on your zone and complete <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/">pre-validation</a> so it reaches <code>status: active</code> before the DNS change.</li>
<li>Issue and validate the certificate (using <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/">TXT</a> or <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/">Delegated DCV</a>) so <code>ssl.status</code> reaches <code>active</code>.</li>
<li>Ask your customer to update their DNS CNAME to point to your SaaS target.</li>
<li>Confirm traffic has switched to your zone. The previous provider can then delete their custom hostname.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4119.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul class="directory-listing"><li><a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/">Pre-validation</a></li><li><a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/">Real-time validation</a></li><li><a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/zero-downtime-migration/">Zero-downtime migration</a></li><li><a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/backoff-schedule/">Backoff schedule</a></li><li><a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/">Validation status</a></li><li><a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/">Error codes</a></li></ul>
