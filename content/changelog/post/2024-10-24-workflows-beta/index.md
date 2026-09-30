---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/
  description: New updates and improvements at Cloudflare.
  full_title: Workflows is now in open beta · Changelog
  head_html: <title>Workflows is now in open beta · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Workflows is now in open beta · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/#page","headline":"Workflows is now in open beta \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2024-10-24-workflows-beta/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 24, 2024</time><h2 id="post-title">Workflows is now in open beta</h2>
<div class="changelog-badges"><span>workers</span><span>workflows</span></div><div class="changelog-body"><p>Workflows is now in open beta, and available to any developer a free or paid Workers plan.</p>
<p>Workflows allow you to build multi-step applications that can automatically retry, persist state and run for minutes, hours, days, or weeks. Workflows introduces a programming model that makes it easier to build reliable, long-running tasks, observe as they progress, and programmatically trigger instances based on events across your services.</p>
<h4 id="get-started">Get started</h4>
<p>You can get started with Workflows by <a href="/workflows/get-started/guide/">following our get started guide</a> and/or using <code>npm create cloudflare</code> to pull down the starter project:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest workflows-starter -- --template &quot;cloudflare/workflows-starter&quot;&#10;</code></pre>
<p>You can open the <code>src/index.ts</code> file, extend it, and use <code>wrangler deploy</code> to deploy your first Workflow. From there, you can:</p>
<ul>
<li>Learn the <a href="/workflows/build/workers-api/">Workflows API</a></li>
<li><a href="/workflows/build/trigger-workflows/">Trigger Workflows</a> via your Workers apps.</li>
<li>Understand the <a href="/workflows/build/rules-of-workflows/">Rules of Workflows</a> and how to adopt best practices</li>
</ul>
</div></article></div>
