---
cp9:
  canonical: https://developers.cloudflare.com/billing/troubleshoot/resolve-zone-cannot-be-upgraded/
  description: Fix errors when upgrading a zone or subscription.
  full_title: Resolve the zone cannot be upgraded error · Cloudflare Billing docs
  head_html: <title>Resolve the zone cannot be upgraded error · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Fix errors when upgrading a zone or subscription."><link rel="canonical" href="https://developers.cloudflare.com/billing/troubleshoot/resolve-zone-cannot-be-upgraded/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/troubleshoot/resolve-zone-cannot-be-upgraded/index.md"><meta property="og:title" content="Resolve the zone cannot be upgraded error · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fix errors when upgrading a zone or subscription."><meta property="og:url" content="https://developers.cloudflare.com/billing/troubleshoot/resolve-zone-cannot-be-upgraded/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/troubleshoot/resolve-zone-cannot-be-upgraded/#page","headline":"Resolve the zone cannot be upgraded error \u00b7 Cloudflare Billing docs","description":"Fix errors when upgrading a zone or subscription.","url":"https://developers.cloudflare.com/billing/troubleshoot/resolve-zone-cannot-be-upgraded/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/troubleshoot/resolve-zone-cannot-be-upgraded/
  schema: 1
---
<p>When trying to upgrade a domain or purchase a subscription, you may see an error that contains one of the following phrases:</p>
<ul>
<li>&quot;this zone cannot be upgraded&quot;</li>
<li>&quot;there is a problem with your billing profile&quot;</li>
</ul>
<h2 id="causes">Causes</h2>
<ul>
<li>Your account may have an outstanding unpaid balance.</li>
<li>Another account previously associated with the domain or zone may have an outstanding unpaid balance.</li>
</ul>
<h2 id="solution">Solution</h2>
<p>This message appears when the account or domain involved has an outstanding unpaid balance. For a domain, this may also be triggered by a previous account that owned the domain.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3385.md")
</div>
<p>As a reference, the full error messages you may see are:</p>
<ul>
<li>&quot;Due to a Billing related issue, the zone cannot be upgraded at this time. Please visit the Billing section to ensure there is no outstanding balance.&quot;</li>
<li>&quot;Refer to <a href="https://cfl.re/3VUQyyL">https://cfl.re/3VUQyyL</a> for assistance. For security reasons, there is a problem with your billing profile.&quot;</li>
</ul>
<h2 id="verify-the-fix">Verify the fix</h2>
<p>After you pay the outstanding balance and wait 24 hours, return to the domain or subscription you were trying to purchase and retry the upgrade.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/manage/pay-invoices-overdue-balances/">Pay an outstanding balance</a> — Resolve unpaid balances</li>
<li><a href="/billing/manage/change-plan/">Change domain plan</a> — Upgrade or downgrade your plan</li>
<li><a href="/billing/troubleshoot/error-reference/">Error reference</a> — Look up other billing error messages</li>
</ul>
