---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-25-wrangler-autoconfig-ga/
  description: New updates and improvements at Cloudflare.
  full_title: No config? No problem. Just `wrangler deploy` · Changelog
  head_html: <title>No config? No problem. Just `wrangler deploy` · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-25-wrangler-autoconfig-ga/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="No config? No problem. Just `wrangler deploy` · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-25-wrangler-autoconfig-ga/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-25-wrangler-autoconfig-ga/#page","headline":"No config? No problem. Just `wrangler deploy` \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-25-wrangler-autoconfig-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-25-wrangler-autoconfig-ga/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 25, 2026</time><h2 id="post-title">No config? No problem. Just `wrangler deploy`</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now deploy any existing project to Cloudflare Workers — even without a Wrangler configuration file — and <code>wrangler deploy</code> will <em>just work</em>.</p>
<p>Starting with Wrangler <strong>4.68.0</strong>, running <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> <a href="/workers/framework-guides/automatic-configuration/">automatically configures your project</a> by detecting your framework, installing required adapters, and deploying it to Cloudflare Workers.</p>
<h4 id="using-wrangler-locally">Using Wrangler locally</h4>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>When you run <code>wrangler deploy</code> in a project without a configuration file, Wrangler:</p>
<ol>
<li>Detects your framework from <code>package.json</code></li>
<li>Prompts you to confirm the detected settings</li>
<li>Installs any required adapters</li>
<li>Generates a <code>wrangler.jsonc</code> <a href="/workers/wrangler/configuration/">configuration file</a></li>
<li>Deploys your project to Cloudflare Workers</li>
</ol>
<p>You can also use <a href="/workers/wrangler/commands/general/#setup"><code>wrangler setup</code></a> to configure without deploying, or pass <a href="/workers/wrangler/commands/general/#deploy"><code>--yes</code></a> to skip prompts.</p>
<h4 id="using-the-cloudflare-dashboard">Using the Cloudflare dashboard</h4>
<p><img src="/assets/upstream/images/workers/ci-cd/builds/automatic-pr.png" alt="Automatic configuration pull request created by Workers Builds" /></p>
<p>When you connect a repository through the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create">Workers dashboard</a>, a <a href="/workers/ci-cd/builds/automatic-prs/">pull request is generated</a> for you with all necessary files, and a <a href="/workers/versions-and-deployments/preview-urls/">preview deployment</a> to check before merging.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17800.md")</aside>
<h4 id="background">Background</h4>
<p>In December 2025, we <a href="/changelog/2025-12-16-wrangler-autoconfig/">introduced automatic configuration</a> as an experimental feature. It is now generally available and the default behavior.</p>
<p>If you have questions or run into issues, join the <a href="https://github.com/cloudflare/workers-sdk/discussions/11667">GitHub discussion</a>.</p>
</div></article></div>
