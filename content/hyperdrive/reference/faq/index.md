---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/reference/faq/
  description: Frequently asked questions about Hyperdrive connectivity, caching, and supported databases.
  full_title: FAQ · Cloudflare Hyperdrive docs
  head_html: <title>FAQ · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Frequently asked questions about Hyperdrive connectivity, caching, and supported databases."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/reference/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/reference/faq/index.md"><meta property="og:title" content="FAQ · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Frequently asked questions about Hyperdrive connectivity, caching, and supported databases."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/reference/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/reference/faq/#page","headline":"FAQ \u00b7 Cloudflare Hyperdrive docs","description":"Frequently asked questions about Hyperdrive connectivity, caching, and supported databases.","url":"https://developers.cloudflare.com/hyperdrive/reference/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/reference/faq/
  schema: 1
---
<p>Below you will find answers to our most commonly asked questions regarding Hyperdrive.</p>
<h2 id="connectivity">Connectivity</h2>
<h3 id="does-hyperdrive-use-specific-ip-addresses-to-connect-to-my-database">Does Hyperdrive use specific IP addresses to connect to my database?</h3>
<p>Hyperdrive connects to your database using <a href="https://www.cloudflare.com/ips/">Cloudflare's IP address ranges</a>. These are shared by all Hyperdrive configurations and other Cloudflare products.</p>
<p>You can use this to configure restrictions in your database firewall to restrict the IP addresses that can access your database.</p>
<h3 id="does-hyperdrive-support-connecting-to-d1-databases">Does Hyperdrive support connecting to D1 databases?</h3>
<p>Hyperdrive does not support <a href="/d1">D1</a> because D1 provides fast connectivity from Workers by design.</p>
<p>Hyperdrive is designed to speed up connectivity to traditional, regional SQL databases such as PostgreSQL. These databases are typically accessed using database drivers that communicate over TCP/IP.
Unlike D1, creating a secure database connection to a traditional SQL database
involves multiple round trips between the client (your Worker) and your database server.
See <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive works</a> for more detail on why round trips are needed
and how Hyperdrive solves this.</p>
<p>D1 does not require round trips to create database connections. D1 is designed to be performant for access from Workers by default, without needing Hyperdrive.</p>
<h3 id="should-i-use-placement-with-hyperdrive">Should I use Placement with Hyperdrive?</h3>
<p>Yes, if your Worker makes multiple queries per request. <a href="/workers/configuration/placement/">Placement</a> runs your Worker near your database, reducing per-query latency from 20-30ms to 1-3ms. Hyperdrive handles connection pooling and setup. Placement reduces the network distance for query execution.</p>
<p>Use <code>placement.region</code> if your database runs in AWS, GCP, or Azure. Use <code>placement.host</code> for databases hosted elsewhere.</p>
<h2 id="caching">Caching</h2>
<h3 id="does-hyperdrive-invalidate-cached-reads-when-i-write-to-my-database">Does Hyperdrive invalidate cached reads when I write to my database</h3>
<p>No. Hyperdrive does not invalidate cached read query results when your application writes to your database. A matching read can return a cached result until the configured <code>max_age</code> expires, and Hyperdrive can serve that result during the <code>stale_while_revalidate</code> window while it refreshes the cache.</p>
<p>Use a cache-disabled Hyperdrive configuration for reads that must return fresh data, such as authentication, sessions, permissions, or reads immediately after a write. Refer to <a href="/hyperdrive/concepts/query-caching/#read-after-write-behavior">Query caching</a> to choose a caching strategy.</p>
<h3 id="can-i-use-hyperdrive-if-some-reads-need-read-after-write-consistency">Can I use Hyperdrive if some reads need read-after-write consistency</h3>
<p>Yes. Configure two Hyperdrive bindings to the same database: one with query caching enabled for reads that can tolerate short staleness, and one with query caching disabled for reads that must be fresh. The cache-disabled binding still gives you Hyperdrive's connection pooling and fast connection setup.</p>
<p>If an object-relational mapping (ORM) library or authentication library owns the SQL, create separate database clients for each binding and pass the cache-disabled client to the code that needs fresh reads.</p>
<h2 id="pricing">Pricing</h2>
<h3 id="does-hyperdrive-charge-for-data-transfer-egress">Does Hyperdrive charge for data transfer / egress?</h3>
<p>No.</p>
<h3 id="is-hyperdrive-available-on-the-workers-free-workers-platform-pricing-workers-plan">Is Hyperdrive available on the <a href="/workers/platform/pricing/#workers">Workers Free</a> plan?</h3>
<p>Yes. Refer to <a href="/hyperdrive/platform/pricing/">pricing</a>.</p>
<h3 id="does-hyperdrive-charge-for-additional-compute">Does Hyperdrive charge for additional compute?</h3>
<p>Hyperdrive itself does not charge for compute (CPU) or processing (wall clock) time. Workers querying Hyperdrive and computing results: for example, serializing results into JSON and/or issuing queries, are billed per <a href="/workers/platform/pricing/#workers">Workers pricing</a>.</p>
<h2 id="limits">Limits</h2>
<h3 id="are-there-any-limits-to-hyperdrive">Are there any limits to Hyperdrive?</h3>
<p>Refer to the published <a href="/hyperdrive/platform/limits/">limits</a> documentation.</p>
