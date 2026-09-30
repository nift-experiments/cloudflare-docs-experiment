---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/
  description: New updates and improvements at Cloudflare.
  full_title: Docker-in-Docker support added to Containers and Sandboxes · Changelog
  head_html: <title>Docker-in-Docker support added to Containers and Sandboxes · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Docker-in-Docker support added to Containers and Sandboxes · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/#page","headline":"Docker-in-Docker support added to Containers and Sandboxes \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-17-docker-in-docker/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 17, 2026</time><h2 id="post-title">Docker-in-Docker support added to Containers and Sandboxes</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><a href="/sandbox/">Sandboxes</a> and <a href="/containers/">Containers</a> now support running Docker for &quot;Docker-in-Docker&quot; setups. This is particularly useful when your end users or <a href="/agents">agents</a> want to run a full sandboxed development environment.</p>
<p>This allows you to:</p>
<ul>
<li>Develop containerized applications with your Sandbox</li>
<li>Run isolated test environments for images</li>
<li>Build container images as part of CI/CD workflows</li>
<li>Deploy arbitrary images supplied at runtime within a container</li>
</ul>
<p>For <a href="/sandbox/">Sandbox SDK</a> users, see the <a href="/sandbox/guides/docker-in-docker/">Docker-in-Docker guide</a> for instructions on combining Docker with the SandboxSDK. For general Containers usage, see the <a href="/containers/faq/#can-i-run-docker-inside-a-container-docker-in-docker">Containers FAQ</a>.</p>
</div></article></div>
