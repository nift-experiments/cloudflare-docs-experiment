---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/
  description: New updates and improvements at Cloudflare.
  full_title: Manage Browser Rendering sessions with Wrangler CLI · Changelog
  head_html: <title>Manage Browser Rendering sessions with Wrangler CLI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Manage Browser Rendering sessions with Wrangler CLI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/#page","headline":"Manage Browser Rendering sessions with Wrangler CLI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-14-browser-wrangler-commands/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 14, 2026</time><h2 id="post-title">Manage Browser Rendering sessions with Wrangler CLI</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Rendering</a> now supports <code>wrangler browser</code> commands, letting you create, manage, and view browser sessions directly from your terminal, streamlining your workflow. Since Wrangler handles authentication, you do not need to pass API tokens in your commands.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler browser create</code></td>
<td>Create a new browser session</td>
</tr>
<tr>
<td><code>wrangler browser close</code></td>
<td>Close a session</td>
</tr>
<tr>
<td><code>wrangler browser list</code></td>
<td>List active sessions</td>
</tr>
<tr>
<td><code>wrangler browser view</code></td>
<td>View a live browser session</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command spins up a browser instance on Cloudflare's network and returns a session URL. Once created, you can connect to the session using any <a href="/browser-run/cdp/">CDP</a>-compatible client like <a href="/browser-run/cdp/puppeteer/">Puppeteer</a>, <a href="/browser-run/cdp/playwright/">Playwright</a>, or <a href="/browser-run/cdp/mcp-clients/">MCP clients</a> to automate browsing, scrape content, or debug remotely.</p>
<pre tabindex="0"><code class="language-sh">wrangler browser create&#10;</code></pre>
<p>Use <code>--keepAlive</code> to set the session keep-alive duration (60-600 seconds):</p>
<pre tabindex="0"><code class="language-sh">wrangler browser create --keepAlive 300&#10;</code></pre>
<p>The <code>view</code> command auto-selects when only one session exists, or prompts for selection when multiple sessions are available.</p>
<p>All commands support <code>--json</code> for structured output, and because these are CLI commands, you can incorporate them into scripts to automate session management.</p>
<p>For full usage details, refer to the <a href="/browser-run/reference/wrangler-commands/">Wrangler commands documentation</a>.</p>
</div></article></div>
