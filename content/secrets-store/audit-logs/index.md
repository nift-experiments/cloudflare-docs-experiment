---
cp9:
  canonical: https://developers.cloudflare.com/secrets-store/audit-logs/
  description: Actions logged for Secrets Store operations, including create, update, and delete.
  full_title: Audit logs · Cloudflare Secrets Store docs
  head_html: <title>Audit logs · Cloudflare Secrets Store docs</title><meta name="generator" content="Nift"><meta name="description" content="Actions logged for Secrets Store operations, including create, update, and delete."><link rel="canonical" href="https://developers.cloudflare.com/secrets-store/audit-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/secrets-store/audit-logs/index.md"><meta property="og:title" content="Audit logs · Cloudflare Secrets Store docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Actions logged for Secrets Store operations, including create, update, and delete."><meta property="og:url" content="https://developers.cloudflare.com/secrets-store/audit-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Secrets Store"><meta name="algolia_product_filter" content="Secrets Store"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Secrets Store"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/secrets-store/audit-logs/#page","headline":"Audit logs \u00b7 Cloudflare Secrets Store docs","description":"Actions logged for Secrets Store operations, including create, update, and delete.","url":"https://developers.cloudflare.com/secrets-store/audit-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /secrets-store/audit-logs/
  schema: 1
---
<p><a href="/fundamentals/account/account-security/review-audit-logs/">Audit logs</a> provide a comprehensive summary of changes made within your Cloudflare account. This page lists the actions that are logged for Secrets Store.</p>
<ul>
<li>Access</li>
<li>Create
<ul>
<li>Duplicating a secret is presented as a <code>create</code> log with a field <code>duplicated_from_id</code>.</li>
</ul>
</li>
<li>Update
<ul>
<li>A boolean <code>&quot;value_modified&quot;: true</code> is presented when the secret value is edited.</li>
</ul>
</li>
<li>Delete</li>
</ul>
<p>For information on how to access and use audit logs, refer to <a href="/fundamentals/account/account-security/review-audit-logs/">Fundamentals</a>.</p>
