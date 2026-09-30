---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/
  description: New updates and improvements at Cloudflare.
  full_title: Fight CSAM More Easily Than Ever · Changelog
  head_html: <title>Fight CSAM More Easily Than Ever · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Fight CSAM More Easily Than Ever · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/#page","headline":"Fight CSAM More Easily Than Ever \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 4, 2025</time><h2 id="post-title">Fight CSAM More Easily Than Ever</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now implement our <strong>child safety tooling</strong>, the <strong><a href="/cache/reference/csam-scanning/">CSAM Scanning Tool</a></strong>, more easily. Instead of requiring external reporting credentials, you only need a verified email address for notifications to onboard. This change makes the tool more accessible to a wider range of customers.</p>
<p><strong>How It Works</strong></p>
<p>When enabled, the tool automatically <a href="https://blog.cloudflare.com/the-csam-scanning-tool/">hashes images for enabled websites as they enter the Cloudflare cache</a>. These hashes are then checked against a database of <strong>known abusive images</strong>.</p>
<ul>
<li><strong>Potential match detected?</strong>
<ul>
<li>The <strong>content URL is blocked</strong>, and</li>
<li><strong>Cloudflare will notify you</strong> about the found matches via the provided email address.</li>
</ul>
</li>
</ul>
<p><strong>Updated Service-Specific Terms</strong></p>
<p>We have also made updates to our <strong><a href="https://www.cloudflare.com/service-specific-terms-application-services/#csam-scanning-tool-terms">Service-Specific Terms</a></strong> to reflect these changes.</p>
</div></article></div>
