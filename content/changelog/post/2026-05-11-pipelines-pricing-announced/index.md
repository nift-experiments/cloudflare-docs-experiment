---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/
  description: New updates and improvements at Cloudflare.
  full_title: Pipelines pricing announced · Changelog
  head_html: <title>Pipelines pricing announced · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Pipelines pricing announced · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/#page","headline":"Pipelines pricing announced \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-11-pipelines-pricing-announced/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 28, 2026</time><h2 id="post-title">Pipelines pricing announced</h2>
<div class="changelog-badges"><span>pipelines</span></div><div class="changelog-body"><p><a href="/pipelines/">Cloudflare Pipelines</a> is a streaming data platform that ingests events, transforms them with SQL, and writes to <a href="/r2/">R2</a> as JSON, Parquet, or <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables. Pipelines now has published pricing based on two usage dimensions: the volume of data processed by SQL transforms and the volume of data delivered to sinks. Ingress into a Pipeline stream is free.</p>
<p><strong>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for Pipelines usage.</strong></p>
<p>Pipelines pricing model is designed to charge per GB based on what you use:</p>
<ul>
<li><strong>Streams (ingress)</strong>: Free, regardless of volume.</li>
<li><strong>SQL transforms</strong>: $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).</li>
<li><strong>Sinks</strong>: $0.03 / GB for JSON, $0.06 / GB for Parquet or Iceberg output.</li>
</ul>
<p>Workers Free plans include 1 GB / month for each dimension. Workers Paid plans include 50 GB / month.</p>
<p>For full pricing details and billing examples, refer to <a href="/pipelines/platform/pricing/">Pipelines pricing</a>.</p>
</div></article></div>
