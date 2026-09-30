---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/
  description: New updates and improvements at Cloudflare.
  full_title: Workers automatic tracing, now in open beta · Changelog
  head_html: <title>Workers automatic tracing, now in open beta · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Workers automatic tracing, now in open beta · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/#page","headline":"Workers automatic tracing, now in open beta \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-07-automatic-tracing/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 7, 2025</time><h2 id="post-title">Workers automatic tracing, now in open beta</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Enable automatic tracing on your Workers, giving you detailed metadata and timing information for every operation your Worker performs.</p>
<p><img src="/assets/upstream/images/workers-observability/R2_Screenshot.png" alt="Tracing example" /></p>
<p>Tracing helps you identify performance bottlenecks, resolve errors, and understand how your Worker interacts with other services on the Workers platform. You can now answer questions like:</p>
<ul>
<li>Which calls are slowing down my application?</li>
<li>Which queries to my database take the longest?</li>
<li>What happened within a request that resulted in an error?</li>
</ul>
<p><strong>You can now:</strong></p>
<ul>
<li>View traces alongside your logs in the Workers Observability dashboard</li>
<li>Export traces (and correlated logs) to any <a href="https://opentelemetry.io/docs/specs/otel/protocol/">OTLP-compatible destination</a>, such as <a href="/workers/observability/exporting-opentelemetry-data/honeycomb/">Honeycomb</a>, <a href="/workers/observability/exporting-opentelemetry-data/sentry/">Sentry</a> or <a href="/workers/observability/exporting-opentelemetry-data/grafana-cloud/">Grafana</a>, by configuring a tracing destination in the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/destinations">Cloudflare dashboard</a></li>
<li>Analyze and query across span attributes (operation type, status, duration, errors)</li>
</ul>
<h4 id="to-get-started-set">To get started, set:</h4>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;observability&quot;: {&#10;		&quot;traces&quot;: {&#10;			&quot;enabled&quot;: true,&#10;		},&#10;	},&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17790.md")</aside>
<h4 id="want-to-learn-more">Want to learn more?</h4>
<ul>
<li><a href="https://blog.cloudflare.com/workers-tracing-now-in-open-beta/">Read the announcement</a></li>
<li><a href="/workers/observability/traces/">Check out the documentation</a></li>
</ul>
</div></article></div>
