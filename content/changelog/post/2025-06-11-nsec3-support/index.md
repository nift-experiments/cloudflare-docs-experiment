---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/
  description: New updates and improvements at Cloudflare.
  full_title: NSEC3 support for DNSSEC · Changelog
  head_html: <title>NSEC3 support for DNSSEC · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="NSEC3 support for DNSSEC · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/#page","headline":"NSEC3 support for DNSSEC \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-06-11-nsec3-support/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 11, 2025</time><h2 id="post-title">NSEC3 support for DNSSEC</h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Enterprise customers can now select NSEC3 as method for proof of non-existence on their zones.</p>
<p>What's new:</p>
<ul>
<li>
<p><strong>NSEC3 support for live-signed zones</strong> – For both primary and secondary zones that are configured to be live-signed (also known as &quot;on-the-fly signing&quot;), NSEC3 can now be selected as proof of non-existence.</p>
</li>
<li>
<p><strong>NSEC3 support for pre-signed zones</strong> – Secondary zones that are transferred to Cloudflare in a <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/#set-up-pre-signed-dnssec">pre-signed setup</a> now also support NSEC3 as proof of non-existence.</p>
</li>
</ul>
<p>For more information and how to enable NSEC3, refer to the <a href="/dns/dnssec/enable-nsec3/">NSEC3 documentation</a>.</p>
</div></article></div>
