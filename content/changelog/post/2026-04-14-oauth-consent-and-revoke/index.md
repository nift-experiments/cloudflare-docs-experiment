---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-14-oauth-consent-and-revoke/
  description: New updates and improvements at Cloudflare.
  full_title: Improved OAuth experience for consent and management · Changelog
  head_html: <title>Improved OAuth experience for consent and management · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-14-oauth-consent-and-revoke/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Improved OAuth experience for consent and management · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-14-oauth-consent-and-revoke/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-14-oauth-consent-and-revoke/#page","headline":"Improved OAuth experience for consent and management \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-14-oauth-consent-and-revoke/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-14-oauth-consent-and-revoke/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 14, 2026</time><h2 id="post-title">Improved OAuth experience for consent and management</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>OAuth allows third-party applications to access your Cloudflare account on your behalf — like when Wrangler deploys Workers or when monitoring tools read your analytics. You now have <strong>granular control</strong> over which accounts these applications can access, plus the ability to revoke access anytime.</p>
<h4 id="what-s-new">What's new</h4>
<h4 id="choose-which-accounts-to-authorize">Choose which accounts to authorize</h4>
When authorizing an OAuth application, you can now **select specific accounts** instead of granting access to all your accounts:
- **Account-by-account selection** — Choose exactly which accounts the application can access
- **"All accounts" option** — Still available for trusted tools like Wrangler
This gives you precise control who can access your data.
<h4 id="clear-consent-screens">Clear consent screens</h4>
The OAuth consent screen now shows:
- **What the application can access** — Explicit list of permissions being requested
- **Who created the application** — Application owner and contact information  
- **Which accounts you're authorizing** — Checkboxes for account selection
<h4 id="revoke-access-anytime">Revoke access anytime</h4>
Manage authorized OAuth applications from your profile:
- **See all connected apps** — View every OAuth application with access to your accounts
- **Review permissions and scope** — Check what each application can do and which accounts it can access
- **Revoke instantly** — Remove access with one click when you no longer need it
To manage your OAuth applications, navigate to **Profile** > **Access Management** > **[Connected Applications](https://dash.cloudflare.com/profile/access-management/authorization)**.
<h4 id="why-this-matters">Why this matters</h4>
These updates give you:
- **Granular control** — Authorize apps per-account instead of all-or-nothing
- **Transparency** — Know exactly what you're authorizing before you consent
- **Security** — Limit blast radius by restricting access to only necessary accounts
- **Easy cleanup** — Revoke access when applications are no longer needed
<h4 id="learn-more">Learn more</h4>
Read more about these improvements in our blog post: [Improving the OAuth consent experience](https://blog.cloudflare.com/improved-developer-security/#improving-the-oauth-consent-experience).
</div></article></div>
