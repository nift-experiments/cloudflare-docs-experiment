---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-30-email-2FA/
  description: New updates and improvements at Cloudflare.
  full_title: Introducing email two-factor authentication · Changelog
  head_html: <title>Introducing email two-factor authentication · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-30-email-2FA/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Introducing email two-factor authentication · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-30-email-2FA/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-30-email-2FA/#page","headline":"Introducing email two-factor authentication \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-30-email-2FA/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-30-email-2FA/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 30, 2025</time><h2 id="post-title">Introducing email two-factor authentication</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Two-factor authentication (2FA) is one of the best ways to protect your account from the risk of account takeover. Cloudflare has offered phishing resistant 2FA options including hardware based keys (for example, a Yubikey) and app based TOTP (time-based one-time password) options which use apps like Google or Microsoft's Authenticator app. Unfortunately, while these solutions are very secure, they can be lost if you misplace the hardware based key, or lose the phone which includes that app. The result is that users sometimes get locked out of their accounts and need to contact support.</p>
<p>Today, we are announcing the addition of email as a 2FA factor for all Cloudflare accounts. Email 2FA is in wide use across the industry as a least common denominator for 2FA because it is low friction, loss resistant, and still improves security over username/password login only. We also know that most commercial email providers already require 2FA, so your email address is usually well protected already.</p>
<p>You can now enable email 2FA on the Cloudflare dashboard:</p>
<ol>
<li>Go to <strong>Profile</strong> at the top right corner.</li>
<li>Select <strong>Authentication</strong>.</li>
<li>Under <strong>Two-Factor Authentication</strong>, select <strong>Set up</strong>.</li>
</ol>
<h4 id="sign-in-security-best-practices">Sign-in security best practices</h4>
<p>Cloudflare is critical infrastructure, and you should protect it as such. Review the following best practices and make sure you are doing your part to secure your account:</p>
<ul>
<li>Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.</li>
<li>Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked.</li>
<li>Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.</li>
<li>If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.</li>
<li>If you use a custom email domain to sign in, <a href="/fundamentals/manage-members/dashboard-sso/">configure SSO</a>.</li>
<li>If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.</li>
<li>If you manage a Cloudflare account for work:
<ul>
<li>Have at least two administrators in case one of them unexpectedly leaves your company.</li>
<li>Use SCIM to automate permissions management for members in your Cloudflare account.</li>
</ul>
</li>
</ul>
</div></article></div>
