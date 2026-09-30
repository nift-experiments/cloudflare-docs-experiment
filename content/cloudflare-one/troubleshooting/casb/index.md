---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/troubleshooting/casb/
  description: CASB for Zero Trust.
  full_title: CASB · Cloudflare One docs
  head_html: <title>CASB · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="CASB for Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/troubleshooting/casb/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/troubleshooting/casb/index.md"><meta property="og:title" content="CASB · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="CASB for Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/troubleshooting/casb/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-one/troubleshooting/casb/#page","headline":"CASB \u00b7 Cloudflare One docs","description":"CASB for Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/troubleshooting/casb/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/troubleshooting/casb/
  schema: 1
---
<p>Use this guide to troubleshoot common issues with Cloud Access Security Broker (CASB).</p>
<h2 id="security-findings">Security findings</h2>
<h3 id="findings-not-appearing">Findings not appearing</h3>
If you do not see findings for an integrated application:
- **Wait for scan**: Initial scans can take up to 24 hours depending on the size of the application.
- **Permissions**: Ensure the account used to integrate the application has the necessary administrative permissions.
- **Enabled status**: Verify that the integration is enabled in the Zero Trust dashboard.
<h3 id="false-positives">False positives</h3>
If CASB flags a configuration that is intended for your organization:
1. Go to **CASB** &gt; **Findings**.
2. Select the finding and choose **Dismiss**.
3. Provide a reason for dismissal to help refine future scans.
<hr />
<h2 id="more-casb-resources">More CASB resources</h2>
<p>For more information, refer to the full CASB documentation.</p>
<p><a class="nb-link-button" href="/cloudflare-one/integrations/cloud-and-saas/troubleshooting/">CASB troubleshooting ❯</a></p>
