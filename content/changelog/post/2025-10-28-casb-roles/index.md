---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/
  description: New updates and improvements at Cloudflare.
  full_title: CASB introduces new granular roles · Changelog
  head_html: <title>CASB introduces new granular roles · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="CASB introduces new granular roles · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/#page","headline":"CASB introduces new granular roles \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-28-casb-roles/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 28, 2025</time><h2 id="post-title">CASB introduces new granular roles</h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p>Cloudflare CASB (Cloud Access Security Broker) now supports two new granular roles to provide more precise access control for your security teams:</p>
<ul>
<li><strong>Cloudflare CASB Read:</strong> Provides read-only access to view CASB findings and dashboards. This role is ideal for security analysts, compliance auditors, or team members who need visibility without modification rights.</li>
<li><strong>Cloudflare CASB:</strong> Provides full administrative access to configure and manage all aspects of the CASB product.</li>
</ul>
<p>These new roles help you better enforce the principle of least privilege. You can now grant specific members access to CASB security findings without assigning them broader permissions, such as the <strong>Super Administrator</strong> or <strong>Administrator</strong> roles.</p>
<p>To enable <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">Data Loss Prevention (DLP)</a>, scans in CASB, account members will need the <strong>Cloudflare Zero Trust</strong> role.</p>
<p>You can find these new roles when inviting members or creating API tokens in the Cloudflare dashboard under <strong>Manage Account</strong> &gt; <strong>Members</strong>.</p>
<p>To learn more about managing roles and permissions, refer to the <a href="/fundamentals/manage-members/roles/">Manage account members and roles documentation</a>.</p>
</div></article></div>
