---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/
  description: New updates and improvements at Cloudflare.
  full_title: Detect PII records with a new predefined DLP profile · Changelog
  head_html: <title>Detect PII records with a new predefined DLP profile · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Detect PII records with a new predefined DLP profile · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/#page","headline":"Detect PII records with a new predefined DLP profile \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-28-pii-record-profile/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 28, 2026</time><h2 id="post-title">Detect PII records with a new predefined DLP profile</h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>Cloudflare DLP now includes a new predefined profile designed to detect PII records that contain multiple types of personal data: <strong>Personally Identifiable Information (PII) Record</strong>.</p>
<p>Most predefined and custom DLP profiles match when any enabled detection entry matches. The <strong>Personally Identifiable Information (PII) Record</strong> profile is different. It only matches when at least three unique detection entries are found in close proximity, which reduces false positives from standalone values that may not represent a real PII record.</p>
<p>Detection entries included in the profile:</p>
<ul>
<li>AU Passport Number</li>
<li>American Express Card Number</li>
<li>Diners Club Card Number</li>
<li>US Driver's License Number</li>
<li>Email Address</li>
<li>Full Name</li>
<li>US Mailing Address</li>
<li>Mastercard Card Number</li>
<li>US Individual Tax Identification Number (ITIN)</li>
<li>US Passport Number</li>
<li>US Phone Number</li>
<li>Union Pay Card Number</li>
<li>United States SSN Numeric Detection</li>
<li>Visa Card Number</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>
</div></article></div>
