---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/
  description: New updates and improvements at Cloudflare.
  full_title: Miniflare v5 prepares local development for the cf CLI · Changelog
  head_html: <title>Miniflare v5 prepares local development for the cf CLI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Miniflare v5 prepares local development for the cf CLI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/#page","headline":"Miniflare v5 prepares local development for the cf CLI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-09-08-miniflare-v5/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 8, 2026</time><h2 id="post-title">Miniflare v5 prepares local development for the cf CLI</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Miniflare v5 prepares Cloudflare local development tooling for the upcoming <code>cf</code> CLI.</p>
<p>Miniflare powers local Workers development behind <code>wrangler dev</code>, the Cloudflare Vite plugin, and <code>@cloudflare/vitest-plugin</code>.
Most projects should use those tools instead of depending on Miniflare directly, and Miniflare v5 will not require any action.</p>
<p>The most significant change is a new configuration shape which aligns Miniflare with <code>cloudflare.config.ts</code>, the programmatic Cloudflare configuration format now available for testing.</p>
<p>Other breaking changes include:</p>
<ul>
<li>Removed deprecated APIs and options, such as legacy alpha D1 bindings.</li>
<li>Removed now-unused, internal APIs like <code>wrappedBindings</code></li>
<li>Removed Miniflare's built-in module discovery; higher-level tools like Wrangler and the Vite plugin should be providing the module graph.</li>
<li>Moved local-only /cdn-cgi routes under /cdn-cgi/local.</li>
<li>Replaced per-resource persistence options with shared persistence root options.</li>
</ul>
<p>For a more comprehensive list, refer to <a href="https://github.com/cloudflare/workers-sdk/blob/main/packages/miniflare/CHANGELOG.md#5202607300-alpha">Miniflare's changelog</a></p>
<p>This work sets up a cleaner foundation for the next generation of local development tooling, including the new <code>cf</code> CLI.</p>
</div></article></div>
