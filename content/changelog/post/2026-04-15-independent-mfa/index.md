---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/
  description: New updates and improvements at Cloudflare.
  full_title: Independent MFA for Access applications · Changelog
  head_html: <title>Independent MFA for Access applications · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Independent MFA for Access applications · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/#page","headline":"Independent MFA for Access applications \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-15-independent-mfa/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 15, 2026</time><h2 id="post-title">Independent MFA for Access applications</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access now supports independent multi-factor authentication (MFA), allowing you to enforce MFA requirements without relying on your identity provider (IdP). With per-application and per-policy configuration, you can enforce stricter authentication methods like hardware security keys on sensitive applications without requiring them across your entire organization. This reduces the risk of MFA fatigue for your broader user population while adding additional security where it matters most.</p>
<p>This feature also addresses common gaps in IdP-based MFA, such as inconsistent MFA policies across different identity providers or the need for additional security layers beyond what the IdP provides.</p>
<p>Independent MFA supports the following authenticator types:</p>
<ul>
<li><strong>Authenticator application</strong> — Time-based one-time passwords (TOTP) using apps like Google Authenticator, Microsoft Authenticator, or Authy.</li>
<li><strong>Security key</strong> — Hardware security keys such as YubiKeys.</li>
<li><strong>Biometrics</strong> — Built-in device authenticators including Apple Touch ID, Apple Face ID, and Windows Hello.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17620.md")</aside>
<h4 id="configuration-levels">Configuration levels</h4>
<p>You can configure MFA requirements at three levels:</p>
<table>
<thead>
<tr>
<th>Level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Organization</strong></td>
<td>Enforce MFA by default for all applications in your account.</td>
</tr>
<tr>
<td><strong>Application</strong></td>
<td>Require or turn off MFA for a specific application.</td>
</tr>
<tr>
<td><strong>Policy</strong></td>
<td>Require or turn off MFA for users who match a specific policy.</td>
</tr>
</tbody>
</table>
<p>Settings at lower levels (policy) override settings at higher levels (organization), giving you granular control over MFA enforcement.</p>
<h4 id="user-enrollment">User enrollment</h4>
<p>Users enroll their authenticators through the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>. To help with onboarding, administrators can share a direct enrollment link: <code>&lt;your-team-name&gt;.cloudflareaccess.com/AddMfaDevice</code>.</p>
<p>To get started with Independent MFA, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a>.</p>
</div></article></div>
