---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/
  description: New updates and improvements at Cloudflare.
  full_title: Precursor introduces session-based bot detection · Changelog
  head_html: <title>Precursor introduces session-based bot detection · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Precursor introduces session-based bot detection · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/#page","headline":"Precursor introduces session-based bot detection \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-07-13-precursor-session-based-detection/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 13, 2026</time><h2 id="post-title">Precursor introduces session-based bot detection</h2>
<div class="changelog-badges"><span>bots</span></div><div class="changelog-body"><p>Precursor is rolling out to all customers starting today. Precursor is client-side JavaScript that enables session-based bot detection.</p>
<p>You can <a href="https://blog.cloudflare.com/introducing-precursor">read the announcement blog</a> for background on why we built Precursor and how session-level behavioral detection works.</p>
<p>With Precursor enabled, Cloudflare can:</p>
<ul>
<li>Continuously evaluate behavioral signals across a session</li>
<li>Re-validate challenge clearance as behavior changes</li>
<li>Update bot scores with session context</li>
<li>Provide client-side visibility where none previously existed</li>
</ul>
<p>It integrates with existing protections, including Security Rules, and can be enabled directly from the Cloudflare dashboard with configurable modes to balance security and user experience.</p>
<img src="/images/precursor/enabling_precursor.gif" alt="Animated walkthrough of enabling Precursor in the Cloudflare dashboard" style="border:1px solid #e5e7eb;border-radius:6px;display:block;margin:16px 0;" />
<p>To learn more, refer to the <a href="/cloudflare-challenges/precursor/">Precursor documentation</a>.</p>
</div></article></div>
