---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/
  description: New updates and improvements at Cloudflare.
  full_title: Hyperdrive exposes database connection pool size metrics · Changelog
  head_html: <title>Hyperdrive exposes database connection pool size metrics · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Hyperdrive exposes database connection pool size metrics · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/#page","headline":"Hyperdrive exposes database connection pool size metrics \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-15-hyperdrive-pool-size-metrics/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 15, 2026</time><h2 id="post-title">Hyperdrive exposes database connection pool size metrics</h2>
<div class="changelog-badges"><span>hyperdrive</span><span>workers</span></div><div class="changelog-body"><p>You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a>, you can see <code>waitingClients</code>, <code>currentPoolSize</code>, <code>availablePoolSlots</code>, and <code>maxPoolSize</code> for each of your configurations.</p>
<p>A new <strong>Pool connections</strong> chart has been added to the <strong>Metrics</strong> tab of each Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>. You can use the location selector to drill down into specific locations hosting your connection pool by airport code.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-pool-size-metrics-chart.png" alt="Hyperdrive pool size metrics chart" /></p>
<p>The chart shows:</p>
<ul>
<li><strong>Waiting clients</strong>: Client requests waiting for an available connection.</li>
<li><strong>Open connections</strong>: Active connections to your database.</li>
<li><strong>Pool size maximum</strong>: Your configured origin connection limit.</li>
</ul>
<p>Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider contacting Cloudflare to <a href="/hyperdrive/platform/limits/#request-a-limit-increase">increase your Hyperdrive connection limit</a>.</p>
<h4 id="pool-size-metrics">Pool size metrics</h4>
<p>The <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a> exposes the following key connection pool metrics for each Hyperdrive configuration:</p>
<p>Under <code>avg</code>:</p>
<ul>
<li><strong><code>currentPoolSize</code></strong> — Average number of connections currently open in the pool.</li>
<li><strong><code>availablePoolSlots</code></strong> — Average number of pool connections available for checkout.</li>
<li><strong><code>waitingClients</code></strong> — Average number of clients waiting for a connection from the pool.</li>
</ul>
<p>Under <code>max</code>:</p>
<ul>
<li><strong><code>maxPoolSize</code></strong> — Configured maximum size of the connection pool.</li>
<li><strong><code>currentPoolSize</code></strong> — Peak number of connections open in the pool.</li>
<li><strong><code>waitingClients</code></strong> — Peak number of clients waiting for a connection from the pool.</li>
</ul>
<p>For more information, refer to <a href="/hyperdrive/observability/metrics/">Metrics and analytics</a> and <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>
</div></article></div>
