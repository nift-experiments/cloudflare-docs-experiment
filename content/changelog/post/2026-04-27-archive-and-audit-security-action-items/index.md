---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-27-archive-and-audit-security-action-items/
  description: New updates and improvements at Cloudflare.
  full_title: Archive and audit security action items · Changelog
  head_html: <title>Archive and audit security action items · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-27-archive-and-audit-security-action-items/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Archive and audit security action items · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-27-archive-and-audit-security-action-items/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-27-archive-and-audit-security-action-items/#page","headline":"Archive and audit security action items \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-27-archive-and-audit-security-action-items/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-27-archive-and-audit-security-action-items/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 20, 2026</time><h2 id="post-title">Archive and audit security action items</h2>
<div class="changelog-badges"><span>security-overview</span></div><div class="changelog-body"><h4 id="archive-and-audit-security-action-items">Archive and audit security action items</h4>
<p>Introducing enhanced archiving capabilities for security action items within the Security Overview dashboard. This update allows security teams to maintain a cleaner workspace by removing resolved, accepted, or irrelevant items from their active list while maintaining a clear paper trail for compliance.</p>
<hr />
<h4 id="why-this-matters">Why this matters</h4>
<p>Managing a high volume of security insights can be overwhelming. Previously, users lacked a structured way to dismiss items without losing the context of why they were ignored.</p>
<p>With these new archiving options—<strong>False Positive</strong>, <strong>Accept Risk</strong>, and <strong>Other</strong>—you can now suppress items indefinitely with required rationale text for risk-based decisions. This ensures that your team remains focused on critical, actionable vulnerabilities while preserving institutional knowledge for audits.</p>
<h4 id="key-features">Key features</h4>
<ul>
<li><strong>Structured Archiving:</strong> Choose from specific categories to define why an action item is being moved.</li>
<li><strong>Required Rationale:</strong> For &quot;Accept Risk&quot; and &quot;Other&quot; categories, users must provide documentation, ensuring accountability for security decisions.</li>
<li><strong>Audit Log Transparency:</strong> New API endpoints allow you to programmatically retrieve the history of status changes and rationale for any insight at the account or zone level.</li>
<li><strong>Reversible Actions:</strong> Any archived item can be moved back to the active list at any time if the security context changes.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17753.md")</aside>
<hr />
<h4 id="example-retrieve-audit-logs-via-api">Example: Retrieve audit logs via API</h4>
<p>To review the history and rationale of a specific archived issue at the account level, you can use the following API command:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){account_id}/insights/{insight_id}/audit-log&quot; \&#10;     &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot;&#10;</code></pre>
</div></article></div>
