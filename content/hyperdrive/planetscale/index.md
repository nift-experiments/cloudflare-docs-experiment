---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/planetscale/
  description: Learn how Cloudflare partners with PlanetScale to provide managed Postgres and MySQL databases for Workers applications with Hyperdrive acceleration.
  full_title: PlanetScale Postgres & MySQL · Cloudflare Hyperdrive docs
  head_html: <title>PlanetScale Postgres &amp; MySQL · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Cloudflare partners with PlanetScale to provide managed Postgres and MySQL databases for Workers applications with Hyperdrive acceleration."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/planetscale/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/planetscale/index.md"><meta property="og:title" content="PlanetScale Postgres &amp; MySQL · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Cloudflare partners with PlanetScale to provide managed Postgres and MySQL databases for Workers applications with Hyperdrive acceleration."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/planetscale/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Hyperdrive,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/hyperdrive/planetscale/#page","headline":"PlanetScale Postgres & MySQL \u00b7 Cloudflare Hyperdrive docs","description":"Learn how Cloudflare partners with PlanetScale to provide managed Postgres and MySQL databases for Workers applications with Hyperdrive acceleration.","url":"https://developers.cloudflare.com/hyperdrive/planetscale/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/planetscale/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/939.md")
</div>
<p>Cloudflare partners with <a href="https://planetscale.com/">PlanetScale</a> to provide PlanetScale-hosted Postgres and MySQL (Vitess) databases to Workers. <a href="/hyperdrive/">Hyperdrive</a> connects <a href="/workers/">Workers</a> to PlanetScale databases with built-in database connection pooling and query caching for faster performance.</p>
<p>Get the best of both products, build for Workers global distribution and optimize for regional data access. Get started by creating a PlanetScale database in the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<h2 id="create-a-database-from-the-command-line">Create a database from the command line</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/938.md")
</aside>
<p>You can also create a Cloudflare-billed PlanetScale database from the command line with the <a href="https://planetscale.com/docs/reference/planetscale-cli">PlanetScale CLI</a> (<code>pscale</code>), using <a href="/workers/wrangler/">Wrangler</a> to authorize the Cloudflare billing side of the request. This requires <code>pscale</code> v0.313.0 or newer.</p>
<p>Generate the billing authorization:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler hyperdrive planetscale signature&#10;</code></pre>
<p>This prints a JSON payload:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;account_id&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;	&quot;timestamp&quot;: &quot;&lt;TIMESTAMP&gt;&quot;,&#10;	&quot;signature&quot;: &quot;&lt;SIGNATURE&gt;&quot;&#10;}&#10;</code></pre>
<p><code>pscale database create</code> accepts this payload through its <code>--cloudflare-billing</code> flag. Passing <code>@-</code> makes the PlanetScale CLI read it from standard input, which we recommend over passing the signature as a command line argument:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler hyperdrive planetscale signature | \&#10;  pscale database create &lt;DATABASE_NAME&gt; \&#10;    &#45;-org &lt;PLANETSCALE_ORG&gt; \&#10;    &#45;-engine postgresql \&#10;    &#45;-cloudflare-billing @- \&#10;    &#45;-format json&#10;</code></pre>
<p><code>pscale database create</code> defaults to Vitess, so pass <code>--engine postgresql</code> for a Postgres database, and <code>--format json</code> is recommended when the output is consumed by an agent.</p>
<p>Your PlanetScale credentials stay between you and <code>pscale</code>. Wrangler authorizes the Cloudflare billing side only.</p>
<p>The signature is a cryptographically signed token that authorizes creating a database billed to your Cloudflare account. Treat it as a credential and do not share it.</p>
<p>Refer to <a href="https://planetscale.com/docs/reference/database#create-a-database">PlanetScale's documentation</a> for the options <code>pscale database create</code> supports.</p>
<h2 id="workers-planetscale">Workers + PlanetScale</h2>
<p>With Workers, build your application to deploy anywhere across Cloudflare’s global network spanning 330+ cities. You can deploy with a single step, and users in new locations can reach your application without deploying regional infrastructure.</p>
<p>Workers compute runs close to your users for low latency. PlanetScale Postgres provides regional databases for your application's control plane or any centralized data that doesn't fit Cloudflare's edge distribution model. Use it for records such as customers, billing, account settings, or other relational data.</p>
<p>Hyperdrive provides the connection glue between Workers and PlanetScale. It pools database connections and uses Cloudflare's <a href="/cache/">Cache</a> for eligible read queries to make your application fast even when your database is centralized.</p>
<h2 id="how-you-benefit">How you benefit?</h2>
<p><img src="/assets/upstream/images/hyperdrive/planetscale-request-flow.svg" alt="Request flow from a user request to Workers, Hyperdrive caches, connection pools, and PlanetScale." /></p>
<ol>
<li>
<p><strong>Run near the user.</strong> When a user sends a request, Cloudflare routes it to a nearby location. Your Worker runs in that location, so request handling starts close to the user.</p>
</li>
<li>
<p><strong>Check for cached reads locally.</strong> On the same Cloudflare server handling the Worker request, Hyperdrive sets up your database connection in single digit milliseconds (p90 4ms) so that your database client/driver can send queries immediately. Hyperdrive's connection setup performs <a href="https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/?cf_target_id=09C713714C8E4B80173505A0C31C63BC">TCP</a> connection startup, <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/?cf_target_id=F13EF8B8F82B5AFEF99A8D9DA7DA3342">TLS</a> encryption, and client authentication all on the same local machine, removing any network roundtrips and latency to your database. Once the database connection is ready if the Worker sends a cacheable read query and the result is cached, Hyperdrive returns it without leaving that location.</p>
</li>
<li>
<p><strong>Forward when needed with caching in-between.</strong> If no local cached result exists, or if the query cannot be cached, Hyperdrive sends the query across Cloudflare's network to a location close to your PlanetScale database. Hyperdrive checks another cache in that location before it reaches the database; this cache is populated by multiple requests to your database to improve your cache hit ratios similar to tiered caching .</p>
</li>
<li>
<p><strong>Query PlanetScale only when necessary.</strong> If neither cache has the result, Hyperdrive sends the query to PlanetScale using an already available pool of database connections. Writes and other uncacheable queries go to PlanetScale so the database remains the source of truth. Multiple layers of caching reduce overall load on your database.</p>
</li>
</ol>
<p>Hyperdrive does not invalidate cached read results when your application writes to PlanetScale. If your application needs read-after-write consistency for authentication, sessions, permissions, or another critical path, use a separate cache-disabled Hyperdrive configuration for those reads. Refer to <a href="/hyperdrive/concepts/query-caching/#read-after-write-behavior">Query caching</a> for guidance.</p>
<h2 id="planetscale-developer-experience">PlanetScale developer experience</h2>
<h3 id="postgres-or-mysql">Postgres or MySQL</h3>
<p>Choose PlanetScale Postgres or MySQL, and keep using familiar database drivers, object-relational mapping (ORM) libraries, and SQL tooling.</p>
<h3 id="performance-and-reliability">Performance and reliability</h3>
<p>Run production databases on PlanetScale infrastructure with commitment to performance and reliability that power trusted <a href="https://planetscale.com/">customer workloads</a>.</p>
<h3 id="modern-development-workflow">Modern development workflow</h3>
<p>Use <a href="https://planetscale.com/docs/postgres/branching">development branches</a> to test database changes, <a href="https://planetscale.com/docs/postgres/monitoring/query-insights">query insights</a> to understand query performance, and the <a href="https://planetscale.com/docs/connect/ai-tooling">Model Context Protocol (MCP) server</a> to give agents access to database insights data, all without needing a database administrator (DBA).</p>
<h3 id="cloudflare-billing">Cloudflare billing</h3>
<p>When you create a PlanetScale database from the Cloudflare dashboard, you are billed via your Cloudflare account — you will see a line item on your Cloudflare invoice for your PlanetScale usage. The pricing for PlanetScale is the same when you create and use databases via Cloudflare as it is when you buy directly from PlanetScale. For more pricing details, refer to <a href="https://planetscale.com/pricing">PlanetScale's pricing</a>. You can introspect per-database billing usage via PlanetScale's <a href="https://planetscale.com/docs/billing#organization-usage-and-billing-page">dashboard</a>.</p>
<h2 id="faq">FAQ</h2>
<details class="nb-details" id="support-for-your-connected-planetscale-databases"><summary>How do I get support for my PlanetScale database?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/940.md")
</div></details>
<details class="nb-details"><summary>How is my PlanetScale database billed?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/941.md")
</div></details>
<div class="nb-card-grid">
@input("content/.markup/bodies/946.md")
</div>
