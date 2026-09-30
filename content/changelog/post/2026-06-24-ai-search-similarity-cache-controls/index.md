---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-24-ai-search-similarity-cache-controls/
  description: New updates and improvements at Cloudflare.
  full_title: Control AI Search similarity cache freshness · Changelog
  head_html: <title>Control AI Search similarity cache freshness · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-24-ai-search-similarity-cache-controls/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Control AI Search similarity cache freshness · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-24-ai-search-similarity-cache-controls/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-24-ai-search-similarity-cache-controls/#page","headline":"Control AI Search similarity cache freshness \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-24-ai-search-similarity-cache-controls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-24-ai-search-similarity-cache-controls/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 24, 2026</time><h2 id="post-title">Control AI Search similarity cache freshness</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now gives you more control over <a href="/ai-search/configuration/retrieval/cache/">similarity cache</a> freshness. Similarity cache helps reduce latency and inference cost by reusing responses for semantically similar queries.</p>
<p>With these updates, you can choose how long responses are eligible for reuse and clear cached responses when they may be stale.</p>
<h4 id="cache-duration-now-defaults-to-48-hours">Cache duration now defaults to 48 hours</h4>
<p>Previously, AI Search cached responses for a fixed duration of 30 days. Cached responses now use the instance's <code>cache_ttl</code> setting, and the default is <strong>48 hours</strong>.</p>
<p>You can set <code>cache_ttl</code> when creating or updating an instance to choose a cache duration from 10 minutes to 6 days.</p>
<p>Use a shorter TTL when your source content changes frequently and freshness is more important. Use a longer TTL when your content is stable and you want more cache reuse.</p>
<p>For example, set <code>cache_ttl</code> to <code>518400</code> to retain cached responses for 6 days:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;cache_ttl&quot;: 518400&#10;}&#10;</code></pre>
<h4 id="purge-cached-responses">Purge cached responses</h4>
<p>You can also purge all cached responses for an instance on demand. Purging cached responses does not delete indexed content or source files.</p>
<p>It prevents AI Search from reusing previous cached responses, so subsequent similar queries generate fresh answers and repopulate the cache.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances/$INSTANCE_NAME/purge_cache&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>You can also purge cached responses from the instance settings page in the Cloudflare dashboard.</p>
<p>Refer to <a href="/ai-search/configuration/retrieval/cache/">similarity cache</a> for the full list of supported <code>cache_ttl</code> values and more details about cache behavior.</p>
</div></article></div>
