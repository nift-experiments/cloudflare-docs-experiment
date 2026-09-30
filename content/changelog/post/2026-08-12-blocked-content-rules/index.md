---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/
  description: New updates and improvements at Cloudflare.
  full_title: Block emails by content with blocked content rules · Changelog
  head_html: <title>Block emails by content with blocked content rules · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Block emails by content with blocked content rules · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/#page","headline":"Block emails by content with blocked content rules \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-12-blocked-content-rules/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 12, 2026</time><h2 id="post-title">Block emails by content with blocked content rules</h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Cloudflare Email security now lets administrators write their own content-based blocking rules. A new <strong>Blocked content</strong> area under <strong>Policies &amp; rules</strong> lets you define a plaintext string or a regular expression, choose whether to scan the message subject, body, or both, and automatically block any message that matches.</p>
<ul>
<li>Create rules using either <strong>plaintext</strong> matches or <strong>regular expressions</strong> — useful for blocking targeted phishing campaigns, known-bad phrases, or content patterns unique to your organization.</li>
<li>Choose the <strong>search location</strong> for each rule: <strong>subject</strong>, <strong>body</strong>, or <strong>subject and body</strong>.</li>
<li>Use the built-in <strong>regular expression checker</strong> to validate your pattern against sample text before saving, so you can confirm the rule matches what you expect and avoid false positives.</li>
<li>Matching messages are marked with a malicious <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">disposition</a> and prevented from reaching users' inboxes.</li>
</ul>
<p>Blocked content rules currently only support the block action.</p>
<p>This feature is available for the following Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-content/">Blocked content</a>.</p>
</div></article></div>
