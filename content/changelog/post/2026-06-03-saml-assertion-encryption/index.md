---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/
  description: New updates and improvements at Cloudflare.
  full_title: SAML assertion encryption for identity providers · Changelog
  head_html: <title>SAML assertion encryption for identity providers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="SAML assertion encryption for identity providers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/#page","headline":"SAML assertion encryption for identity providers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-03-saml-assertion-encryption/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 3, 2026</time><h2 id="post-title">SAML assertion encryption for identity providers</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access now supports SAML assertion encryption for identity provider integrations. When turned on, your identity provider encrypts SAML assertions using a Cloudflare-managed certificate before sending them through the user's browser. Only Access can decrypt these assertions, protecting sensitive identity data even after TLS termination.</p>
<p>Without encryption, SAML assertions are transmitted in plaintext and could be visible to browser extensions or client-side malware.</p>
<p><img src="/assets/upstream/images/changelog/access/saml-encryption.png" alt="SAML encryption toggle in the identity provider configuration" /></p>
<p>SAML encryption includes built-in certificate lifecycle management:</p>
<ul>
<li><strong>Automatic certificate generation</strong>: Access generates an encryption certificate when you turn on SAML encryption for an identity provider.</li>
<li><strong>Certificate rotation</strong>: Rotate certificates without downtime. The previous certificate remains valid until expiration, giving you time to update your IdP.</li>
<li><strong>PEM export</strong>: Copy the certificate in PEM format for manual upload to your IdP, or point your IdP to the SAML metadata endpoint for automatic retrieval.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#encrypt-saml-assertions">Encrypt SAML assertions</a>.</p>
</div></article></div>
