---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/security/recovering-from-hacked-site/
  description: Steps to recover your website after a hack and prevent future compromises using Cloudflare security features.
  full_title: Recovering from a hacked site · Cloudflare Fundamentals docs
  head_html: <title>Recovering from a hacked site · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Steps to recover your website after a hack and prevent future compromises using Cloudflare security features."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/security/recovering-from-hacked-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/security/recovering-from-hacked-site/index.md"><meta property="og:title" content="Recovering from a hacked site · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Steps to recover your website after a hack and prevent future compromises using Cloudflare security features."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/security/recovering-from-hacked-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/security/recovering-from-hacked-site/#page","headline":"Recovering from a hacked site \u00b7 Cloudflare Fundamentals docs","description":"Steps to recover your website after a hack and prevent future compromises using Cloudflare security features.","url":"https://developers.cloudflare.com/fundamentals/security/recovering-from-hacked-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/security/recovering-from-hacked-site/
  schema: 1
---
<p>If your website has been hacked recently, review the recommended steps below to recover a hacked website and prevent future hacks.</p>
<h2 id="recovering-from-an-attack">Recovering from an attack</h2>
<p>To recover from an attack, reach out to your hosting provider to request:</p>
<ul>
<li>Details about the hack, including how they believe the site was hacked.</li>
<li>That your hosting provider remove any malicious content placed on your website.</li>
</ul>
<p>Once the hack has been resolved, you should resolve site warnings in <a href="https://www.google.com/webmasters/tools">Google Webmaster Tools</a> and resubmit your site for Google's review.</p>
<hr />
<h2 id="preventing-and-mitigating-the-risks-of-a-future-hack">Preventing and mitigating the risks of a future hack</h2>
<p>To prevent the risk of a hacked site:</p>
<ul>
<li>Activate Cloudflare's <a href="/waf/managed-rules/">WAF managed rules</a> so they can challenge or block known malicious behavior.</li>
<li>If you use a Content Management System (CMS), make sure you have the most recent version installed (CMS platforms push out updates to address known vulnerabilities).</li>
<li>If you use plugins, make sure they are updated.</li>
<li>If you have an admin login page, protect it with Cloudflare's <a href="/waf/rate-limiting-rules/">Rate limiting rules</a> or a <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access policy</a>.</li>
<li>Use a backup service so you can avoid losing valid content.</li>
</ul>
