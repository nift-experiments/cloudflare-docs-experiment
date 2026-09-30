---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/
  description: Configure which git branches should trigger a Workers Build
  full_title: Build branches · Cloudflare Workers docs
  head_html: <title>Build branches · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure which git branches should trigger a Workers Build"><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/index.md"><meta property="og:title" content="Build branches · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure which git branches should trigger a Workers Build"><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#page","headline":"Build branches \u00b7 Cloudflare Workers docs","description":"Configure which git branches should trigger a Workers Build","url":"https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/builds/build-branches/
  schema: 1
---
<p>When you connect a git repository to Workers, commits made on the production git branch will produce a Workers Build. If you want to take advantage of <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> and <a href="/workers/ci-cd/builds/git-integration/github-integration/#pull-request-comment">pull request comments</a>, you can additionally enable &quot;non-production branch builds&quot; in order to trigger a build on all branches of your repository.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16782.md")
</aside>
<h2 id="change-production-branch">Change production branch</h2>
<p>To change the production branch of your project:</p>
<ol>
<li>In <strong>Overview</strong>, select your Workers project.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Build</strong> &gt; <strong>Branch control</strong>. Workers will default to the default branch of your git repository, but this can be changed in the dropdown.</li>
</ol>
<p>Every push event made to this branch will trigger a build and execute the <a href="/workers/ci-cd/builds/configuration/#deploy-command">build command</a>, followed by the <a href="/workers/ci-cd/builds/configuration/#deploy-command">deploy command</a>.</p>
<h2 id="configure-non-production-branch-builds">Configure non-production branch builds</h2>
<p>To enable or disable non-production branch builds:</p>
<ol>
<li>In <strong>Overview</strong>, select your Workers project.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Build</strong> &gt; <strong>Branch control</strong>. The checkbox <strong>Builds for non-production branches</strong> allows you to enable or disable builds for non-production branches.</li>
</ol>
<p>When enabled, every push event made to a non-production branch will trigger a build and execute the <a href="/workers/ci-cd/builds/configuration/#deploy-command">build command</a>, followed by the <a href="/workers/ci-cd/builds/configuration/#non-production-branch-deploy-command">non-production branch deploy command</a>.</p>
