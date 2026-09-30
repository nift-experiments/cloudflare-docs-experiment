---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2024-12-29-faster-builds/
  description: New updates and improvements at Cloudflare.
  full_title: Faster Workers Builds with Build Caching and Watch Paths · Changelog
  head_html: <title>Faster Workers Builds with Build Caching and Watch Paths · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2024-12-29-faster-builds/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Faster Workers Builds with Build Caching and Watch Paths · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2024-12-29-faster-builds/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-12-29-faster-builds/#page","headline":"Faster Workers Builds with Build Caching and Watch Paths \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2024-12-29-faster-builds/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2024-12-29-faster-builds/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 29, 2024</time><h2 id="post-title">Faster Workers Builds with Build Caching and Watch Paths</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/platform/ci-cd/workers-build-caching.png" alt="Build caching settings" />
<img src="/assets/upstream/images/workers/platform/ci-cd/workers-build-watch-paths.png" alt="Build watch path settings" /></p>
<p><a href="/workers/ci-cd/builds/"><strong>Workers Builds</strong></a>, the integrated CI/CD system for Workers (currently in beta), now lets you cache artifacts across builds, speeding up build jobs by eliminating repeated work, such as downloading dependencies at the start of each build.</p>
<ul>
<li>
<p><strong><a href="/workers/ci-cd/builds/build-caching/">Build Caching</a></strong>: Cache dependencies and build outputs between builds with a shared project-wide cache, ensuring faster builds for the entire team.</p>
</li>
<li>
<p><strong><a href="/workers/ci-cd/builds/build-watch-paths/">Build Watch Paths</a></strong>: Define paths to include or exclude from the build process, ideal for <a href="/workers/ci-cd/builds/advanced-setups/#monorepos">monorepos</a> to target only the files that need to be rebuilt per Workers project.</p>
</li>
</ul>
<p>To get started, select your Worker on the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> then go to <strong>Settings</strong> &gt; <strong>Builds</strong>, and connect a GitHub or GitLab repository. Once connected, you'll see options to configure Build Caching and Build Watch Paths.</p>
</div></article></div>
