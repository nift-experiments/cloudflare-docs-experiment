---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/
  description: New updates and improvements at Cloudflare.
  full_title: 'Preview: @cloudflare/computer agent runtime · Changelog'
  head_html: '<title>Preview: @cloudflare/computer agent runtime · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Preview: @cloudflare/computer agent runtime · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/#page","headline":"Preview: @cloudflare/computer agent runtime \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-03-cloudflare-computer/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 3, 2026</time><h2 id="post-title">Preview: @cloudflare/computer agent runtime</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>We're releasing an early preview of <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code></a>, an open-source agent runtime that gives every agent its own computer. The runtime dynamically orchestrates between fast, efficient isolates and full Linux containers, so the agent always runs on the right compute primitive for the task at hand.</p>
<p><code>@cloudflare/computer</code> provides a virtual filesystem backed by SQLite, which you can populate from cloud storage, source control, or any files you choose. Agents can read, write, and edit files, run shell commands, and interact with Git repositories. All operations are gated, audited, and observed.</p>
<p>Install the package via npm:</p>
<pre tabindex="0"><code class="language-sh">npm install @cloudflare/computer&#10;</code></pre>
<p>Instantiate a <code>Workspace</code> inside any Durable Object to give your agent a filesystem and execution runtime:</p>
<pre tabindex="0"><code class="language-ts">import { Workspace } from &quot;@cloudflare/computer&quot;;&#10;&#10;export class Agent {&#10;	workspace = new Workspace({&#10;		storage: this.ctx.storage,&#10;	});&#10;}&#10;</code></pre>
<p>Several execution backends are included or you can write your own:</p>
<ul>
<li><strong>Isolate runtime</strong> — fast, horizontally scalable execution via <code>just-bash</code> and Dynamic Workers, ideal for file manipulation and data processing.</li>
<li><strong>Container runtime</strong> — full Linux environment via Cloudflare Containers, mounted through FUSE, for tasks that need native binaries, package managers, or a complete userland.</li>
</ul>
<p>The AI SDK-compatible toolkit provides common agent tools (<code>read</code>, <code>write</code>, <code>edit</code>, <code>ls</code>, <code>exec</code>) and guides the model to choose the appropriate backend for each task.</p>
<p>For more examples, including a step-by-step tutorial, visit the <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code> repository</a>.</p>
<p>Read the announcement blog post for more details: <a href="https://blog.cloudflare.com/cloudflare-computer/">Your agent needs a computer, not a container</a>.</p>
</div></article></div>
