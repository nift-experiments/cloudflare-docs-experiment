---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/
  description: Phish submissions in Email Security.
  full_title: Phish submissions · Cloudflare One docs
  head_html: <title>Phish submissions · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Phish submissions in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/index.md"><meta property="og:title" content="Phish submissions · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Phish submissions in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/#page","headline":"Phish submissions \u00b7 Cloudflare One docs","description":"Phish submissions in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/settings/phish-submissions/
  schema: 1
---
<p>As part of your continuous email security posture, administrators and security analysts need to submit missed <span class="nb-glossary-tooltip" title="phishing">phishing</span> samples to Email security, so Cloudflare can process them and take necessary action.</p>
<p>Submitting missed phish samples to Cloudflare is of paramount importance and necessary for continuous protection. Submitting missed phish samples helps Cloudflare improve our machine learning (ML) models, and alerts us of new attack vectors before they become prevalent.</p>
<p>There are three routes you can use to report an email as a phish:</p>
<ul>
<li>Via Investigation, by <a href="/cloudflare-one/email-security/settings/phish-submissions/#reclassify-an-email">reclassifying an email</a>.</li>
<li>Via <a href="/cloudflare-one/email-security/settings/phish-submissions/phishnet-365/">PhishNet 365</a>.</li>
<li>Via <a href="/cloudflare-one/email-security/settings/phish-submissions/submission-addresses/">Submission addresses</a>.</li>
</ul>
<h2 id="reclassify-an-email">Reclassify an email</h2>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong> &gt; <strong>Investigation</strong>.</li>
<li>On the <strong>Investigation</strong> page, under <strong>Your matching messages</strong>, select the message you want to reclassify. Select the three dots, then select <strong>Submit for review</strong>. By selecting <strong>Submit for review</strong>, you are requesting a new disposition for the message.</li>
<li>Select the new disposition, then select <strong>Save</strong>.</li>
</ol>
<p>When you report an email as phish, this email will be displayed under <a href="/cloudflare-one/email-security/submissions/user-submissions/">User submissions</a>.</p>
