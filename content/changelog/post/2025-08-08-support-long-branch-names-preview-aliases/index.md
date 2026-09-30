---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/
  description: New updates and improvements at Cloudflare.
  full_title: Workers per-branch preview URLs now support long branch names · Changelog
  head_html: <title>Workers per-branch preview URLs now support long branch names · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Workers per-branch preview URLs now support long branch names · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/#page","headline":"Workers per-branch preview URLs now support long branch names \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-08-support-long-branch-names-preview-aliases/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 14, 2025</time><h2 id="post-title">Workers per-branch preview URLs now support long branch names</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We've updated <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> for Cloudflare Workers to support long branch names.</p>
<p>Previously, branch and Worker names exceeding the 63-character DNS limit would cause alias generation to fail, leaving pull requests without aliased preview URLs. This particularly impacted teams relying on descriptive branch naming.</p>
<p>Now, Cloudflare automatically truncates long branch names and appends a unique hash, ensuring every pull request gets a working preview link.</p>
<h4 id="how-it-works">How it works</h4>
<ul>
<li><strong>63 characters or less</strong>: <code>&lt;branch-name&gt;-&lt;worker-name&gt;</code> → Uses actual branch name as is</li>
<li><strong>64 characters or more</strong>: <code>&lt;truncated-branch-name&gt;--&lt;hash&gt;-&lt;worker-name&gt;</code> → Uses truncated name with 4-character hash</li>
<li><strong>Hash generation</strong>: The hash is derived from the full branch name to ensure uniqueness</li>
<li><strong>Stable URLs</strong>: The same branch always generates the same hash across all commits</li>
</ul>
<h4 id="requirements-and-compatibility">Requirements and compatibility</h4>
<ul>
<li><strong>Wrangler 4.30.0 or later</strong>: This feature requires updating to wrangler@4.30.0+</li>
<li><strong>No configuration needed</strong>: Works automatically with existing preview URL setups</li>
</ul>
</div></article></div>
