---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-30-member-management-improvements/
  description: New updates and improvements at Cloudflare.
  full_title: Revamped Member Management UI · Changelog
  head_html: <title>Revamped Member Management UI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-30-member-management-improvements/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Revamped Member Management UI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-30-member-management-improvements/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-30-member-management-improvements/#page","headline":"Revamped Member Management UI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-30-member-management-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-30-member-management-improvements/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 30, 2025</time><h2 id="post-title">Revamped Member Management UI</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>As Cloudflare's platform has grown, so has the need for precise, role-based access control. We’ve redesigned the Member Management experience in the Dashboard to help administrators more easily discover, assign, and refine permissions for specific principals.</p>
<h4 id="what-s-new">What's New</h4>
<p><strong>Refreshed member invite flow</strong></p>
<p>We overhauled the Invite Members UI to simplify inviting users and assigning permissions.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-invite-experience.gif" alt="Updated Invite Flow UX" /></p>
<p><strong>Refreshed Members Overview Page</strong></p>
<p>We've updated the Members Overview Page to clearly display:</p>
<ul>
<li>Member 2FA status</li>
<li>Which members hold Super Admin privileges</li>
<li>API access settings per member</li>
<li>Member onboarding state (accepted vs pending invite)</li>
</ul>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-member-management-screen.png" alt="Updated Member Management Overview" /></p>
<p><strong>New Member Permission Policies Details View</strong></p>
<p>We've created a new member details screen that shows all permission policies associated with a member; including policies inherited from group associations to make it easier for members to understand the effective permissions they have.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-permission-policies-screen.gif" alt="Updated Permission Policies Details Screen" /></p>
<p><strong>Improved Member Permission Workflow</strong></p>
<p>We redesigned the permission management experience to make it faster and easier for administrators to review roles and grant access.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-permission-policies-screen.gif" alt="Updated Member Permission Management UX" /></p>
<p><strong>Account-scoped Policies Restrictions Relaxed</strong></p>
<p>Previously, customers could only associate a single account-scoped policy with a member. We've relaxed this restriction, and now Administrators can now assign multiple account-scoped policies to the same member; bringing policy assignment behavior in-line with user-groups and providing greater flexibility in managing member permissions.</p>
</div></article></div>
