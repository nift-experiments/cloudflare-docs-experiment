---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/
  description: New updates and improvements at Cloudflare.
  full_title: Interactive browser terminals in Sandboxes · Changelog
  head_html: <title>Interactive browser terminals in Sandboxes · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Interactive browser terminals in Sandboxes · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/#page","headline":"Interactive browser terminals in Sandboxes \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-09-pty-terminal-support/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 9, 2026</time><h2 id="post-title">Interactive browser terminals in Sandboxes</h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><p>The <a href="https://github.com/cloudflare/sandbox-sdk">Sandbox SDK</a> now supports PTY (pseudo-terminal) passthrough, enabling browser-based terminal UIs to connect to sandbox shells via WebSocket.</p>
<h4 id="sandbox-terminal-request"><code>sandbox.terminal(request)</code></h4>
<p>The new <code>terminal()</code> method proxies a WebSocket upgrade to the container's PTY endpoint, with output buffering for replay on reconnect.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17632.md")</div>
<h4 id="multiple-terminals-per-sandbox">Multiple terminals per sandbox</h4>
<p>Each session can have its own terminal with an isolated working directory and environment, so users can run separate shells side-by-side in the same container.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17633.md")</div>
<h4 id="xterm-js-addon">xterm.js addon</h4>
<p>The new <code>@cloudflare/sandbox/xterm</code> export provides a <code>SandboxAddon</code> for <a href="https://xtermjs.org/">xterm.js</a> with automatic reconnection (exponential backoff + jitter), buffered output replay, and resize forwarding.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17634.md")</div>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/sandbox@latest&#10;</code></pre>
</div></article></div>
