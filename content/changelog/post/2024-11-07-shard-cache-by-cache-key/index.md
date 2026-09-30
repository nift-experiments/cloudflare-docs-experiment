---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/
  description: New updates and improvements at Cloudflare.
  full_title: Shard cache using custom cache key values · Changelog
  head_html: <title>Shard cache using custom cache key values · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Shard cache using custom cache key values · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/#page","headline":"Shard cache using custom cache key values \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2024-11-07-shard-cache-by-cache-key/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 7, 2024</time><h2 id="post-title">Shard cache using custom cache key values</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Enterprise customers can now optimize cache hit ratios for content that varies by device, language, or referrer by <strong>sharding cache</strong> using up to ten values from previously restricted headers with <a href="/cache/how-to/cache-keys/">custom cache keys</a>.</p>
<h4 id="how-it-works">How it works</h4>
<p>When configuring <a href="/cache/how-to/cache-keys/">custom cache keys</a>, you can now include values from these headers to create distinct cache entries:</p>
<ul>
<li><strong><code>accept*</code> headers</strong> (for example, <code>accept</code>, <code>accept-encoding</code>, <code>accept-language</code>): Serve different cached versions based on content negotiation.</li>
<li><strong><code>referer</code> header</strong>: Cache content differently based on the referring page or site.</li>
<li><strong><code>user-agent</code> header</strong>: Maintain separate caches for different browsers, devices, or bots.</li>
</ul>
<h4 id="when-to-use-cache-sharding">When to use cache sharding</h4>
<ul>
<li>Content varies significantly by device type (mobile vs desktop).</li>
<li>Different language or encoding preferences require distinct responses.</li>
<li>Referrer-specific content optimization is needed.</li>
</ul>
<h4 id="example-configuration">Example configuration</h4>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;cache_key&quot;: {&#10;    &quot;custom_key&quot;: {&#10;      &quot;header&quot;: {&#10;        &quot;include&quot;: [&quot;accept-language&quot;, &quot;user-agent&quot;],&#10;        &quot;check_presence&quot;: [&quot;referer&quot;]&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>This configuration creates separate cache entries based on the <code>accept-language</code> and <code>user-agent</code> headers, while also considering whether the <code>referer</code> header is present.</p>
<h4 id="get-started">Get started</h4>
<p>To get started, refer to the <a href="/cache/how-to/cache-keys/">custom cache keys documentation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17702.md")</aside>
</div></article></div>
