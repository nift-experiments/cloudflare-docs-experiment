---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/
  description: Error codes you may encounter when validating custom hostnames.
  full_title: Error codes - Custom Hostname Validation · Cloudflare for Platforms docs
  head_html: <title>Error codes - Custom Hostname Validation · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Error codes you may encounter when validating custom hostnames."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/index.md"><meta property="og:title" content="Error codes - Custom Hostname Validation · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Error codes you may encounter when validating custom hostnames."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/#page","headline":"Error codes - Custom Hostname Validation \u00b7 Cloudflare for Platforms docs","description":"Error codes you may encounter when validating custom hostnames.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/
  schema: 1
---
<p>When you <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/">validate a custom hostname</a>, you might encounter the following error codes.</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zone does not have a fallback origin set.</td>
<td>Fallback is not active.</td>
</tr>
<tr>
<td>Fallback origin is in a status of <code>initializing</code>, <code>pending_deployment</code>, <code>pending_deletion</code>, or <code>deleted</code>.</td>
<td>Fallback is not active.</td>
</tr>
<tr>
<td>Custom hostname does not <code>CNAME</code> to this zone.</td>
<td>Zone does not have <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">apex proxying entitlement</a> and custom hostname does not CNAME to zone.</td>
</tr>
<tr>
<td>None of the <code>A</code> or <code>AAAA</code> records are owned by this account and the pre-generated ownership validation token was not found.</td>
<td>Account has <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">apex proxying enabled</a> but the custom hostname failed the hostname validation check on the <code>A</code> record.</td>
</tr>
<tr>
<td>This account and the pre-generated ownership validation token was not found.</td>
<td>Hostname does not <code>CNAME</code> to zone or none of the <code>A</code>/<code>AAAA</code> records match reserved IPs for zone.</td>
</tr>
</tbody>
</table>
