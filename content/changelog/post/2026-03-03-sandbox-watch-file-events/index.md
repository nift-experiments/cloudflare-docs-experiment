---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/
  description: New updates and improvements at Cloudflare.
  full_title: Real-time file watching in Sandboxes · Changelog
  head_html: <title>Real-time file watching in Sandboxes · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Real-time file watching in Sandboxes · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/#page","headline":"Real-time file watching in Sandboxes \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-03-sandbox-watch-file-events/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 3, 2026</time><h2 id="post-title">Real-time file watching in Sandboxes</h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><p><a href="/sandbox/">Sandboxes</a> now support real-time filesystem watching via <code>sandbox.watch()</code>. The method returns a <a href="https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events">Server-Sent Events</a> stream backed by native inotify, so your Worker receives <code>create</code>, <code>modify</code>, <code>delete</code>, and <code>move</code> events as they happen inside the container.</p>
<h4 id="sandbox-watch-path-options"><code>sandbox.watch(path, options)</code></h4>
<p>Pass a directory path and optional filters. The returned stream is a standard <code>ReadableStream</code> you can proxy directly to a browser client or consume server-side.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17650.md")</div>
<h4 id="server-side-consumption-with-parsessestream">Server-side consumption with <code>parseSSEStream</code></h4>
<p>Use <code>parseSSEStream</code> to iterate over events inside a Worker without forwarding them to a client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17651.md")</div>
<p>Each event includes a <code>type</code> field (<code>create</code>, <code>modify</code>, <code>delete</code>, or <code>move</code>) and the affected <code>path</code>. Move events also include a <code>from</code> field with the original path.</p>
<h4 id="options">Options</h4>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>recursive</code></td>
<td><code>boolean</code></td>
<td>Watch subdirectories. Defaults to <code>false</code>.</td>
</tr>
<tr>
<td><code>include</code></td>
<td><code>string[]</code></td>
<td>Glob patterns to filter events. Omit to receive all events.</td>
</tr>
</tbody>
</table>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/sandbox@latest&#10;</code></pre>
<p>For full API details, refer to the <a href="/sandbox/api/file-watching/">Sandbox file watching reference</a>.</p>
</div></article></div>
