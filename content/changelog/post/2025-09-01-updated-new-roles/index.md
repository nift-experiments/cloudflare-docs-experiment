---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/
  description: New updates and improvements at Cloudflare.
  full_title: Updated Email security roles · Changelog
  head_html: <title>Updated Email security roles · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Updated Email security roles · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/#page","headline":"Updated Email security roles \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-01-updated-new-roles/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 2, 2025</time><h2 id="post-title">Updated Email security roles</h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>To provide more granular controls, we refined the <a href="/cloudflare-one/roles-permissions/#email-security-roles">existing roles</a> for Email security and launched a new Email security role as well.</p>
<p>All Email security roles no longer have read or write access to any of the other Zero Trust products:</p>
<ul>
<li><strong>Email Configuration Admin</strong></li>
<li><strong>Email Integration Admin</strong></li>
<li><strong>Email security Read Only</strong></li>
<li><strong>Email security Analyst</strong></li>
<li><strong>Email security Policy Admin</strong></li>
<li><strong>Email security Reporting</strong></li>
</ul>
<p>To configure <a href="/cloudflare-one/email-security/outbound-dlp/">Data Loss Prevention (DLP)</a> or <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#set-up-clientless-web-isolation">Remote Browser Isolation (RBI)</a>, you now need to be an admin for the Zero Trust dashboard with the <strong>Cloudflare Zero Trust</strong> role.</p>
<p>Also through customer feedback, we have created a new additive role to allow <strong>Email security Analyst</strong> to create, edit, and delete Email security policies, without needing to provide access via the <strong>Email Configuration Admin</strong> role. This role is called <strong>Email security Policy Admin</strong>, which can read all settings, but has write access to <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policies</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">trusted domains</a>, and <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">blocked senders</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div></article></div>
