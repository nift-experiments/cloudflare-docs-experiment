---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/
  description: New updates and improvements at Cloudflare.
  full_title: Require Access protection for zones · Changelog
  head_html: <title>Require Access protection for zones · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Require Access protection for zones · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/#page","headline":"Require Access protection for zones \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-01-22-deny-by-default-for-zones/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 22, 2026</time><h2 id="post-title">Require Access protection for zones</h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span></div><div class="changelog-body"><p>You can now require Cloudflare Access protection for all hostnames in your account. When enabled, traffic to any hostname that does not have a matching Access application is automatically blocked.</p>
<p>This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. If a developer deploys a new application or creates a DNS record without configuring an Access application, the traffic is blocked rather than exposed.</p>
<p><img src="/assets/upstream/images/changelog/access/require-cloudflare-access-protection.png" alt="Require Cloudflare Access protection in the dashboard" /></p>
<h4 id="how-it-works">How it works</h4>
<ul>
<li><strong>Blocked by default</strong>: Traffic to all hostnames in the account is blocked unless an Access application exists for that hostname.</li>
<li><strong>Explicit access required</strong>: To allow traffic, create an Access application with an Allow or Bypass policy.</li>
<li><strong>Hostname exemptions</strong>: You can exempt specific hostnames from this requirement.</li>
</ul>
<p>To turn on this feature, refer to <a href="/cloudflare-one/access-controls/access-settings/require-access-protection/">Require Access protection</a>.</p>
</div></article></div>
