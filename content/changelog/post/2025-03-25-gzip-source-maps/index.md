---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/
  description: New updates and improvements at Cloudflare.
  full_title: Source Maps are Generally Available · Changelog
  head_html: <title>Source Maps are Generally Available · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Source Maps are Generally Available · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/#page","headline":"Source Maps are Generally Available \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-03-25-gzip-source-maps/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 25, 2025</time><h2 id="post-title">Source Maps are Generally Available</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Source maps are now Generally Available (GA). You can now be uploaded with a maximum gzipped size of 15 MB.
Previously, the maximum size limit was 15 MB uncompressed.</p>
<p>Source maps help map between the original source code and the transformed/minified code that gets deployed
to production. By uploading your source map, you allow Cloudflare to map the stack trace from exceptions
onto the original source code making it easier to debug.</p>
<p><img src="/assets/upstream/images/workers-observability/without-source-map.png" alt="Stack Trace without Source Map remapping" /></p>
<p>With <strong>no source maps uploaded</strong>: notice how all the Javascript has been minified to one file, so the stack trace is missing information on file name, shows incorrect line numbers, and incorrectly references <code>js</code> instead of <code>ts</code>.</p>
<p><img src="/assets/upstream/images/workers-observability/with-source-map.png" alt="Stack Trace with Source Map remapping" /></p>
<p>With <strong>source maps uploaded</strong>: all methods reference the correct files and line numbers.</p>
<p>Uploading source maps and stack trace remapping happens out of band from the Worker execution,
so source maps do not affect upload speed, bundle size, or cold starts. The remapped stack
traces are accessible through Tail Workers, Workers Logs, and Workers Logpush.</p>
<p>To enable source maps, add the following to your
<a href="/pages/functions/source-maps/">Pages Function's</a> or <a href="/workers/observability/source-maps/">Worker's</a> wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17768.md")</div>
</div></article></div>
