---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/
  description: New updates and improvements at Cloudflare.
  full_title: Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers · Changelog
  head_html: <title>Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/#page","headline":"Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-07-23-workers-preview-urls/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 22, 2025</time><h2 id="post-title">Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Now, when you connect your Cloudflare Worker to a git repository on GitHub or GitLab, each branch of your repository has its own stable preview URL, that you can use to preview code changes before merging the pull request and deploying to production.</p>
<p>This works the same way that Cloudflare Pages does — every time you create a pull request, you'll automatically get a shareable preview link where you can see your changes running, without affecting production. The link stays the same, even as you add commits to the same branch.
These preview URLs are named after your branch and are posted as a comment to each pull request. The URL stays the same with every commit and always points to the latest version of that branch.</p>
<p><img src="/assets/upstream/images/changelog/workers/preview-urls-comment.png" alt="PR comment preview" /></p>
<h4 id="preview-url-types">Preview URL types</h4>
<p>Each comment includes <strong>two preview URLs</strong> as shown above:</p>
<ul>
<li><strong>Commit Preview URL</strong>: Unique to the specific version/commit (e.g., <code>&lt;version-prefix&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
<li><strong>Branch Preview URL</strong>: A stable alias based on the branch name (e.g., <code>&lt;branch-name&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
</ul>
<h4 id="how-it-works">How it works</h4>
<p>When you create a pull request:</p>
<ul>
<li><strong>A preview alias is automatically created</strong> based on the Git branch name (e.g., <code>&lt;branch-name&gt;</code> becomes <code>&lt;branch-name&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
<li><strong>No configuration is needed</strong>, the alias is generated for you</li>
<li><strong>The link stays the same</strong> even as you add commits to the same branch</li>
<li><strong>Preview URLs are posted directly to your pull request as comments</strong> (just like they are in Cloudflare Pages)</li>
</ul>
<h4 id="custom-alias-name">Custom alias name</h4>
<p>You can also assign a custom preview alias using the <a href="/workers/wrangler/">Wrangler CLI</a>, by passing the <code>--preview-alias</code> flag when <a href="/workers/wrangler/commands/general/#versions-upload">uploading a version</a> of your Worker:</p>
<pre tabindex="0"><code class="language-bash">wrangler versions upload --preview-alias staging&#10;</code></pre>
<h4 id="limitations-while-in-beta">Limitations while in beta</h4>
<ul>
<li>Only available on the <strong>workers.dev</strong> subdomain (custom domains not yet supported)</li>
<li>Requires <strong>Wrangler v4.21.0+</strong></li>
<li>Preview URLs are not generated for Workers that use <a href="/durable-objects/">Durable Objects</a></li>
<li>Not yet supported for <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a></li>
</ul>
</div></article></div>
