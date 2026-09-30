---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/
  description: New updates and improvements at Cloudflare.
  full_title: Container image for Cloudflare Mesh · Changelog
  head_html: <title>Container image for Cloudflare Mesh · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Container image for Cloudflare Mesh · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/#page","headline":"Container image for Cloudflare Mesh \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-07-mesh-container-image/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 7, 2026</time><h2 id="post-title">Container image for Cloudflare Mesh</h2>
<div class="changelog-badges"><span>mesh</span><span>cloudflare-one</span></div><div class="changelog-body"><p><a href="/mesh/">Cloudflare Mesh</a> nodes can now run as Docker containers. The <a href="https://hub.docker.com/r/cloudflare/mesh"><code>cloudflare/mesh</code></a> image is available on Docker Hub for Docker Compose, Kubernetes, and any OCI-compatible runtime — no host-level package installation required.</p>
<p>The image supports <code>amd64</code> and <code>arm64</code> architectures and includes built-in <a href="/mesh/guides/run-mesh-in-containers/#source-nat">source NAT</a> so return traffic routes correctly without VPC route table changes.</p>
<h4 id="deployment-patterns">Deployment patterns</h4>
<ul>
<li><strong>Docker Compose</strong> — add a <code>cloudflare-mesh</code> service to your <code>compose.yaml</code> and connect your entire stack to a private network.</li>
<li><strong>Kubernetes StatefulSet</strong> — deploy a standalone Mesh node with persistent registration state.</li>
<li><strong>Kubernetes sidecar</strong> — add the Mesh image as a sidecar container in a Pod to connect an application to Cloudflare without application changes.</li>
<li><strong>CI/CD</strong> — pull the image in a pipeline step, join the Mesh, run integration tests against private infrastructure, and tear down. The node disappears when the container exits.</li>
</ul>
<p>For <a href="/mesh/features/high-availability/">high availability</a>, run multiple replicas with the same Mesh node token. Cloudflare operates replicas in active-passive mode with automatic failover.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, runtime configuration, and deployment examples, refer to <a href="/mesh/guides/run-mesh-in-containers/">Run Mesh in Docker / Kubernetes</a>.</p>
</div></article></div>
