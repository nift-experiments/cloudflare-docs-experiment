---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/
  description: Configure the maximum number of database connections in your Hyperdrive connection pool.
  full_title: Tune connection pooling · Cloudflare Hyperdrive docs
  head_html: <title>Tune connection pooling · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure the maximum number of database connections in your Hyperdrive connection pool."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/index.md"><meta property="og:title" content="Tune connection pooling · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure the maximum number of database connections in your Hyperdrive connection pool."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/#page","headline":"Tune connection pooling \u00b7 Cloudflare Hyperdrive docs","description":"Configure the maximum number of database connections in your Hyperdrive connection pool.","url":"https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/configuration/tune-connection-pool/
  schema: 1
---
<p>Hyperdrive maintains a pool of connections to your database that are shared across Worker invocations. You can configure the maximum number of these connections based on your database capacity and application requirements.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9030.md")
</aside>
<h2 id="configure-connection-pool-size">Configure connection pool size</h2>
<p>You can configure the connection pool size using the Cloudflare dashboard, the Wrangler CLI, or the Cloudflare API.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9034.md")
</div></div>
<p>All Hyperdrive configurations have a minimum of 5 connections. The maximum connection count depends on your <a href="/hyperdrive/platform/limits/">Workers plan</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9029.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9028.md")
</aside>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Start conservatively</strong>: Begin with a lower connection count and gradually increase it based on your application's performance.</li>
<li><strong>Monitor database metrics</strong>: Watch your database's connection usage and performance metrics to optimize the connection count.</li>
<li><strong>Consider database limits</strong>: Ensure your configured connection count does not exceed your database's maximum connection limit.</li>
<li><strong>Account for multiple configurations</strong>: If you have multiple Hyperdrive configurations connecting to the same database, consider the total connection count across all configurations.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/hyperdrive/concepts/connection-pooling/">Connection pooling concepts</a></li>
<li><a href="/hyperdrive/concepts/connection-lifecycle/">Connection lifecycle</a></li>
<li><a href="/hyperdrive/observability/metrics/">Metrics and analytics</a></li>
<li><a href="/hyperdrive/platform/limits/">Hyperdrive limits</a></li>
<li><a href="/hyperdrive/concepts/query-caching/">Query caching</a></li>
</ul>
