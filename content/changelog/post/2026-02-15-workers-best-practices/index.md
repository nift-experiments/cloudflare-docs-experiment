---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/
  description: New updates and improvements at Cloudflare.
  full_title: New Best Practices guide for Workers · Changelog
  head_html: <title>New Best Practices guide for Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New Best Practices guide for Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/#page","headline":"New Best Practices guide for Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-15-workers-best-practices/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 15, 2026</time><h2 id="post-title">New Best Practices guide for Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>A new <a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a> guide provides opinionated recommendations for building fast, reliable, observable, and secure Workers. The guide draws on production patterns, Cloudflare internal usage, and best practices observed from developers building on Workers.</p>
<p>Key guidance includes:</p>
<ul>
<li><strong>Keep your compatibility date current and enable <code>nodejs_compat</code></strong> — Ensure you have access to the latest runtime features and Node.js built-in modules.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17799.md")</div>
- **Generate binding types with `wrangler types`** — Never hand-write your `Env` interface. Let Wrangler generate it from your actual configuration to catch mismatches at compile time.
- **Stream request and response bodies** — Avoid buffering large payloads in memory. Use `TransformStream` and `pipeTo` to stay within the 128 MB memory limit and improve time-to-first-byte.
- **Use bindings, not REST APIs** — Bindings to KV, R2, D1, Queues, and other Cloudflare services are direct, in-process references with no network hop and no authentication overhead.
- **Use Queues and Workflows for background work** — Move long-running or retriable tasks out of the critical request path. Use Queues for simple fan-out and buffering, and Workflows for multi-step durable processes.
- **Enable Workers Logs and Traces** — Configure observability before deploying to production so you have data when you need to debug.
- **Avoid global mutable state** — Workers reuse isolates across requests. Storing request-scoped data in module-level variables causes cross-request data leaks.
- **Always `await` or `waitUntil` your Promises** — Floating promises cause silent bugs and dropped work.
- **Use Web Crypto for secure token generation** — Never use `Math.random()` for security-sensitive operations.
<p>To learn more, refer to <a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a>.</p>
</div></article></div>
