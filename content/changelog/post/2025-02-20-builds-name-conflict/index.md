---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/
  description: New updates and improvements at Cloudflare.
  full_title: Autofix Worker name configuration errors at build time · Changelog
  head_html: <title>Autofix Worker name configuration errors at build time · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Autofix Worker name configuration errors at build time · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/#page","headline":"Autofix Worker name configuration errors at build time \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-02-20-builds-name-conflict/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 20, 2025</time><h2 id="post-title">Autofix Worker name configuration errors at build time</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/platform/ci-cd/gh-auto-pr-name.png" alt="Auto-fixing Workers Name in Git Repo" /></p>
<p>Small misconfigurations shouldn’t break your deployments. Cloudflare is introducing automatic error detection and fixes in <a href="/workers/ci-cd/builds/">Workers Builds</a>, identifying common issues in your wrangler.toml or wrangler.jsonc and proactively offering fixes, so you spend less time debugging and more time shipping.</p>
<p>Here's how it works:</p>
<ol>
<li>Before running your build, Cloudflare checks your Worker's Wrangler configuration file (wrangler.toml or wrangler.jsonc) for common errors.</li>
<li>Once you submit a build, if Cloudflare finds an error it can fix, it will submit a pull request to your repository that fixes it.</li>
<li>Once you merge this pull request, Cloudflare will run another build.</li>
</ol>
<p>We're starting with fixing name mismatches between your Wrangler file and the Cloudflare dashboard, a top cause of build failures.</p>
<p>This is just the beginning, we want your feedback on what other errors we should catch and fix next. Let us know in the Cloudflare Developers Discord, <a href="https://discord.com/channels/595317990191398933/1064502845061210152">#workers-and-pages-feature-suggestions</a>.</p>
</div></article></div>
