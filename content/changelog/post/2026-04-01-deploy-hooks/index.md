---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/
  description: New updates and improvements at Cloudflare.
  full_title: Deploy Hooks are now available for Workers Builds · Changelog
  head_html: <title>Deploy Hooks are now available for Workers Builds · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Deploy Hooks are now available for Workers Builds · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/#page","headline":"Deploy Hooks are now available for Workers Builds \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-01-deploy-hooks/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 1, 2026</time><h2 id="post-title">Deploy Hooks are now available for Workers Builds</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/ci-cd/builds/">Workers Builds</a> now supports Deploy Hooks — trigger builds from your headless CMS, a Cron Trigger, a Slack bot, or any system that can send an HTTP request.</p>
<p>Each Deploy Hook is a unique URL tied to a specific branch. Send it a <code>POST</code> and your Worker builds and deploys.</p>
<pre tabindex="0"><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/workers/builds/deploy_hooks/&lt;DEPLOY_HOOK_ID&gt;&quot;&#10;</code></pre>
<p>To create one, go to <strong>Workers &amp; Pages</strong> &gt; your Worker &gt; <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Deploy Hooks</strong>.</p>
<p>Since a Deploy Hook is a URL, you can also call it from another Worker. For example, a Worker with a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> can rebuild your project on a schedule:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17803.md")</div>
<p>You can also use Deploy Hooks to <a href="/workers/ci-cd/builds/deploy-hooks/#cms-integration">rebuild when your CMS publishes new content</a> or <a href="/workers/ci-cd/builds/deploy-hooks/#deploy-from-a-slack-slash-command">deploy from a Slack slash command</a>.</p>
<h4 id="built-in-optimizations">Built-in optimizations</h4>
<ul>
<li><strong>Automatic deduplication</strong>: If a Deploy Hook fires multiple times before the first build starts running, redundant builds are automatically skipped. This keeps your build queue clean when webhooks retry or CMS events arrive in bursts.</li>
<li><strong>Last triggered</strong>: The dashboard shows when each hook was last triggered.</li>
<li><strong>Build source</strong>: Your Worker's build history shows which Deploy Hook started each build by name.</li>
</ul>
<p>Deploy Hooks are rate limited to 10 builds per minute per Worker and 100 builds per minute per account. For all limits, see <a href="/workers/ci-cd/builds/limits-and-pricing/">Limits &amp; pricing</a>.</p>
<p>To get started, read the <a href="/workers/ci-cd/builds/deploy-hooks/">Deploy Hooks documentation</a>.</p>
</div></article></div>
