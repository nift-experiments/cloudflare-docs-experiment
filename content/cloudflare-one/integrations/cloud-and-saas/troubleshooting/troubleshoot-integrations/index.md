---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations/
  description: Troubleshoot Troubleshoot integrations issues in Zero Trust integrations.
  full_title: Troubleshoot integrations · Cloudflare One docs
  head_html: <title>Troubleshoot integrations · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Troubleshoot integrations issues in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations/index.md"><meta property="og:title" content="Troubleshoot integrations · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Troubleshoot integrations issues in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations/#page","headline":"Troubleshoot integrations \u00b7 Cloudflare One docs","description":"Troubleshoot Troubleshoot integrations issues in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations/
  schema: 1
---
<p>Cloudflare CASB detects when integrations are unhealthy or outdated.</p>
<p>Common integration issues include changes to SaaS app or cloud environment configurations, user access, or permission scope. Integrations may need to be updated to support new features or permissions.</p>
<h2 id="identify-unhealthy-or-outdated-integrations">Identify unhealthy or outdated integrations</h2>
<p>To identify unhealthy CASB integrations, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>. If an integration is unhealthy, CASB will set its status to <strong>Broken</strong>. If an integration is outdated, CASB will set its status to <strong>Upgrade</strong>.</p>
<h2 id="repair-an-unhealthy-integration">Repair an unhealthy integration</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="repair-limitation">Repair limitation</h3>
@markup("md", "content/.markup/bodies/5099.md")
</aside>
<p>You can repair unhealthy CASB integrations through your list of integrations or findings.</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>.</li>
<li>Choose your unhealthy integration.</li>
<li>Select <strong>Reauthorize</strong>.</li>
<li>In your SaaS app or cloud environment, reauthorize your account.</li>
</ol>
<h2 id="upgrade-an-integration">Upgrade an integration</h2>
<p>Upgrading an outdated integration will allow the integration to access new features and permissions.</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>.</li>
<li>Choose your outdated integration.</li>
<li>Select <strong>Upgrade integration</strong>.</li>
<li>In your SaaS app or cloud environment, upgrade your app and reauthorize your account.</li>
</ol>
