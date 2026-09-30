---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/
  description: Troubleshoot Cloudflare 1014 error code.
  full_title: Error 1014 · Cloudflare Support docs
  head_html: <title>Error 1014 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Cloudflare 1014 error code."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/index.md"><meta property="og:title" content="Error 1014 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Cloudflare 1014 error code."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/#page","headline":"Error 1014 \u00b7 Cloudflare Support docs","description":"Troubleshoot Cloudflare 1014 error code.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/
  schema: 1
---
<h2 id="error-1014-cname-cross-user-banned">Error 1014: CNAME Cross-User Banned</h2>
<p>This error indicates that a CNAME record between domains in different Cloudflare accounts is prohibited.</p>
<h3 id="common-cause">Common cause</h3>
<p>By default, Cloudflare prohibits a DNS CNAME record between domains in different Cloudflare accounts. CNAME records are permitted within a domain (<code>www.example.com</code> CNAME to <code>api.example.com</code>) and across zones within the same user account (<code>www.example.com</code> CNAME to <code>www.example.net</code>) or using our <a href="https://www.cloudflare.com/saas/">Cloudflare for SaaS</a> solution.</p>
<p>Another common cause is connecting a custom domain to an R2 bucket, where the domain is an active zone with the <a href="/fundamentals/account/account-security/zone-holds/">zone hold</a> feature enabled or if the zone is banned.</p>
<h3 id="resolution">Resolution</h3>
<ul>
<li>
<p>To allow CNAME record resolution to a domain in a different Cloudflare account, the domain owner of the CNAME target must use <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a>.</p>
</li>
<li>
<p>To allow connecting to a R2 bucket with a custom domain, disable the <a href="/fundamentals/account/account-security/zone-holds/">zone hold</a> feature on the custom domain target zone to resolve the 1014 error.</p>
</li>
<li>
<p>To allow connections to an R2 bucket whose zone is banned:</p>
<ul>
<li>First, check whether there is any <a href="/fundamentals/reference/report-abuse/complaint-types/">phishing report</a> for the hostname (and request a review if there is one).</li>
<li>Second, make sure that you have no unpaid invoice(s), as you will not be able to enable any new services until <a href="/billing/manage/pay-invoices-overdue-balances/">any outstanding balance</a> is addressed. If this does not resolve the issue, contact your account team.</li>
</ul>
</li>
</ul>
