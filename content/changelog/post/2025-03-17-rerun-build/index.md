---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/
  description: New updates and improvements at Cloudflare.
  full_title: Retry Pages & Workers Builds Directly from GitHub · Changelog
  head_html: <title>Retry Pages &amp; Workers Builds Directly from GitHub · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Retry Pages &amp; Workers Builds Directly from GitHub · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/#page","headline":"Retry Pages & Workers Builds Directly from GitHub \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-03-17-rerun-build/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 17, 2025</time><h2 id="post-title">Retry Pages &amp; Workers Builds Directly from GitHub</h2>
<div class="changelog-badges"><span>workers</span><span>pages</span></div><div class="changelog-body"><p>You can now retry your Cloudflare Pages and Workers builds directly from GitHub. No need to switch to the Cloudflare Dashboard for a simple retry!</p>
<p>Let\u2019s say you push a commit, but your build fails due to a spurious error like a network timeout. Instead of going to the Cloudflare Dashboard to manually retry, you can now rerun the build with just a few clicks inside GitHub, keeping you inside your workflow.</p>
<p>For Pages and Workers projects connected to a GitHub repository:</p>
<ol>
<li>When a build fails, go to your GitHub repository or pull request</li>
<li>Select the failed Check Run for the build</li>
<li>Select &quot;Details&quot; on the Check Run</li>
<li>Select &quot;Rerun&quot; to trigger a retry build for that commit</li>
</ol>
<p>Learn more about <a href="/pages/configuration/git-integration/github-integration/">Pages Builds</a> and <a href="/workers/ci-cd/builds/git-integration/github-integration/">Workers Builds</a>.</p>
</div></article></div>
