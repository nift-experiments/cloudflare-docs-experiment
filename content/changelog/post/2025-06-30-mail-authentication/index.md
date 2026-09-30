---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/
  description: New updates and improvements at Cloudflare.
  full_title: Mail authentication requirements for Email Routing · Changelog
  head_html: <title>Mail authentication requirements for Email Routing · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Mail authentication requirements for Email Routing · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/#page","headline":"Mail authentication requirements for Email Routing \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-06-30-mail-authentication/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 30, 2025</time><h2 id="post-title">Mail authentication requirements for Email Routing</h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>The Email Routing platform supports <a href="https://datatracker.ietf.org/doc/html/rfc7208">SPF</a> records and <a href="https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail">DKIM (DomainKeys Identified Mail)</a> signatures and
honors these protocols when the sending domain has them configured. However, if the sending domain doesn't implement them,
we still forward the emails to upstream mailbox providers.</p>
<p>Starting on July 3, 2025, we will require all emails to be authenticated using at least one of the protocols, SPF or DKIM, to
forward them. We also strongly recommend that all senders implement the DMARC protocol.</p>
<p>If you are using a Worker with an Email trigger to receive email messages and forward them upstream, you will need to handle the case where
the forward action may fail due to missing authentication on the incoming email.</p>
<p>SPAM has been a long-standing issue with email. By enforcing mail authentication, we will increase the efficiency of identifying abusive senders and blocking
bad emails.
If you're an email server delivering emails to large mailbox providers, it's likely you already use these protocols; otherwise, please ensure
you have them properly configured.</p>
</div></article></div>
