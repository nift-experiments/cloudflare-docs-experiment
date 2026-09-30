---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/
  description: New updates and improvements at Cloudflare.
  full_title: Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development · Changelog
  head_html: <title>Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/#page","headline":"Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-16-remote-bindings-ga/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 16, 2025</time><h2 id="post-title">Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Three months ago <a href="/changelog/2025-06-18-remote-bindings-beta/">we announced the public beta</a> of <a href="/workers/local-development/#remote-bindings">remote bindings</a> for local development. Now, we're excited to say that it's available for everyone in Wrangler, Vite, and Vitest without using an experimental flag!</p>
<p>With remote bindings, you can now connect to deployed resources like <a href="/r2/">R2 buckets</a> and <a href="/d1/">D1 databases</a> while running Worker code on your local machine. This means you can test your local code changes against real data and services, without the overhead of deploying for each iteration.</p>
<h4 id="example-configuration">Example configuration</h4>
<p>To enable remote bindings, add <code>&quot;remote&quot; : true</code> to each binding that you want to rely on a remote resource running on Cloudflare:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17787.md")</div>
<p>When remote bindings are configured, your Worker <strong>still executes locally</strong>, but all binding calls are proxied to the deployed resource that runs on Cloudflare's network.</p>
<p><strong>You can <a href="/workers/local-development/#remote-bindings">try out remote bindings</a> for local development today with:</strong></p>
<ul>
<li><a href="/workers/wrangler/">Wrangler v4.37.0</a></li>
<li>The <a href="/workers/vite-plugin/">Cloudflare Vite Plugin</a></li>
<li>The <a href="/workers/testing/vitest-integration/">Cloudflare Vitest Plugin</a></li>
</ul>
</div></article></div>
