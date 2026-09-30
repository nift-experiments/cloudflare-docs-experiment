---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/
  description: New updates and improvements at Cloudflare.
  full_title: Local Explorer for local resource data · Changelog
  head_html: <title>Local Explorer for local resource data · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Local Explorer for local resource data · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/#page","headline":"Local Explorer for local resource data \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-13-local-explorer/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 13, 2026</time><h2 id="post-title">Local Explorer for local resource data</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Local Explorer is a browser-based interface and REST API for viewing and editing local resource data during development. It removes the need to write throwaway scripts or dig through <code>.wrangler/state</code> to understand what data your Worker has stored locally.</p>
<p>Local Explorer is available in Wrangler 4.82.1+ and the Cloudflare Vite plugin 1.32.0+. Start a local development session and press <code>e</code> in your terminal, or navigate to <code>/cdn-cgi/local/explorer</code> on your local dev server.</p>
<h4 id="supported-resources">Supported resources</h4>
<p>Local Explorer supports five resource types and works across multiple workers running locally:</p>
<ul>
<li><strong><a href="/kv/">KV</a></strong> — Browse keys, view values and metadata, create, update, and delete key-value pairs.</li>
<li><strong><a href="/r2/">R2</a></strong> — List objects, view metadata, upload files, and delete objects. Supports directory views and multi-select.</li>
<li><strong><a href="/d1/">D1</a></strong> — Browse tables and rows, run arbitrary SQL queries, and edit schemas in a full data studio.</li>
<li><strong><a href="/durable-objects/">Durable Objects</a></strong> (SQLite storage) — Browse individual object SQLite tables, run SQL queries, and edit schemas.</li>
<li><strong><a href="/workflows/">Workflows</a></strong> — List instances, view status and step history, trigger new runs, and pause, resume, restart, or terminate instances.</li>
</ul>
<h4 id="openapi-powered-rest-api">OpenAPI-powered REST API</h4>
<p>Local Explorer exposes a REST API at <code>/cdn-cgi/local/explorer/api</code> that provides programmatic access to the same operations available in the browser. The root endpoint returns an <a href="https://www.openapis.org/">OpenAPI specification</a> describing all available endpoints, parameters, and response formats.</p>
<pre tabindex="0"><code class="language-sh">curl http://localhost:8787/cdn-cgi/local/explorer/api&#10;</code></pre>
<p>Point an AI coding agent at <code>/cdn-cgi/local/explorer/api</code> and it can discover and interact with your local resources without manual setup. This enables iterative development loops where an agent can populate test data in KV or D1, inspect Durable Object state, trigger Workflow runs, or upload files to R2.</p>
<p>For more details, refer to the <a href="/workers/local-development/local-explorer/">Local Explorer documentation</a>.</p>
</div></article></div>
