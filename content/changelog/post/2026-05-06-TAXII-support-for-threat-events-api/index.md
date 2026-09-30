---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/
  description: New updates and improvements at Cloudflare.
  full_title: TAXII support added to Threat Events API · Changelog
  head_html: <title>TAXII support added to Threat Events API · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="TAXII support added to Threat Events API · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/#page","headline":"TAXII support added to Threat Events API \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-06-TAXII-support-for-threat-events-api/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 6, 2026</time><h2 id="post-title">TAXII support added to Threat Events API</h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>The Cloudforce One Threat Events API now supports <a href="https://www.cloudflare.com/en-gb/learning/security/what-is-stix-and-taxii/"><strong>TAXII</strong></a> as an output format, enabling standardized, automated sharing of cyber threat intelligence with your existing security stack.</p>
<h4 id="why-this-matters">Why this matters</h4>
<ul>
<li>You can now ingest Cloudforce One threat data directly into your SIEM, TIP or SOAR tools that prefer TAXII-formatted streams without needing custom translation scripts.</li>
<li>By supporting the TAXII format parameter in our API, security teams can automate the synchronization of indicator data, reducing the manual overhead of updating blocklists and detection rules.</li>
<li>This alignment with industry standards ensures that your threat data remains consistent across different security ecosystems and partner integrations.</li>
</ul>
<h4 id="how-to-use-it">How to use it</h4>
<p>When calling the Threat Events API, you can now specify <code>taxii</code> in the <code>format</code> query parameter:</p>
<p><code>GET /accounts/{account_id}/cloudforce_one/threat_events?format=taxii</code></p>
<p>You can find the updated documentation in the <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list#%28resource%29%20cloudforce_one.threat_events%20%3E%20%28method%29%20list%20%3E%20%28params%29%20default%20%3E%20%28param%29%20format%20%3E%20%28schema%29">Cloudflare API Reference</a>.</p>
</div></article></div>
