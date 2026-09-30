---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/
  description: Possible statuses for custom hostname validation and their meanings.
  full_title: Validation status - Custom Hostname Validation · Cloudflare for Platforms docs
  head_html: <title>Validation status - Custom Hostname Validation · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Possible statuses for custom hostname validation and their meanings."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/index.md"><meta property="og:title" content="Validation status - Custom Hostname Validation · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Possible statuses for custom hostname validation and their meanings."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/#page","headline":"Validation status - Custom Hostname Validation \u00b7 Cloudflare for Platforms docs","description":"Possible statuses for custom hostname validation and their meanings.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/
  schema: 1
---
<p>When you <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/">validate a custom hostname</a>, that hostname can be in several different statuses.</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pending</td>
<td>Custom hostname is pending hostname validation.</td>
</tr>
<tr>
<td>Active</td>
<td>Custom hostname has completed hostname validation and is active.</td>
</tr>
<tr>
<td>Active re-deploying</td>
<td>Customer hostname is active and the changes have been processed.</td>
</tr>
<tr>
<td>Blocked</td>
<td>Custom hostname cannot be added to Cloudflare at this time. Custom hostname was likely associated with Cloudflare previously and flagged for abuse.<br/><br/>If you are an Enterprise customer, contact your account team. Otherwise, email <code>abusereply@cloudflare.com</code> with the name of the web property and a detailed explanation of your association with this web property.</td>
</tr>
<tr>
<td>Moved</td>
<td>Custom hostname is not active after <strong>Pending</strong> for the entirety of the <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/backoff-schedule/">Validation Backoff Schedule</a> or it no longer points to the fallback origin.</td>
</tr>
<tr>
<td>Deleted</td>
<td>Custom hostname was deleted from the zone. Occurs when status is <strong>Moved</strong> for more than seven days.</td>
</tr>
</tbody>
</table>
<p>The custom hostname validation status is separate from the certificate status. In the <a href="/api/resources/custom_hostnames/methods/get/">Custom hostname details endpoint</a> response, <code>result.status</code> tracks hostname activation and <code>result.ssl.status</code> tracks certificate issuance and deployment.</p>
<p>A custom hostname is ready for production traffic when <code>result.status</code> is <code>active</code>, <code>result.ssl.status</code> is <code>active</code>, and DNS points to your SaaS target. If <code>result.status</code> is <code>active</code> but <code>result.ssl.status</code> is not <code>active</code>, Cloudflare has validated the hostname, but the certificate has not completed issuance and deployment.</p>
<h2 id="refresh-validation">Refresh validation</h2>
<p>To run the custom hostname validation check again, select <strong>Refresh</strong> on the dashboard or send a <code>PATCH</code> request to the <a href="/api/resources/custom_hostnames/methods/edit/">Edit custom hostname endpoint</a>. If using the API, make sure that the <code>--data</code> field contains an <code>ssl</code> object with the same <code>method</code> and <code>type</code> as the original request.</p>
<p>If the hostname is in a <strong>Moved</strong> or <strong>Deleted</strong> state, the refresh will set the custom hostname back to <strong>Pending validation</strong>.</p>
