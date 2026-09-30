<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 18, 2026</time><h2 id="post-title">Create PlanetScale Postgres and MySQL databases, billed to your Cloudflare account</h2>
<div class="changelog-badges"><span>hyperdrive</span><span>workers</span></div><div class="changelog-body"><p>You can create PlanetScale Postgres and MySQL databases from Cloudflare and bill PlanetScale database usage through your Cloudflare account as a pay-as-you-go customer. Cloudflare contract customers will be able to add PlanetScale usage to their contract in July so reach out to your Cloudflare account team if interested.</p>
<p>Create a PlanetScale database from the Cloudflare dashboard to check out globally distributed Workers optimized for regional data access.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/hyperdrive/planetscale-request-flow.svg" alt="Request flow from a user to Workers, Hyperdrive caches, connection pools, and PlanetScale." /></p>
<p>PlanetScale databases created from Cloudflare work with <a href="/workers/">Workers</a> through <a href="/hyperdrive/">Hyperdrive</a>. Hyperdrive manages database connection pools and query caching, so you can use PlanetScale as a centralized relational database for Workers applications without changing your database drivers, object-relational mapping (ORM) libraries, or SQL tooling.</p>
<p>PlanetScale usage appears on your Cloudflare invoice each billing period as a dollar total at PlanetScale's standard <a href="https://planetscale.com/pricing">pricing</a>. You can introspect per-database billing usage via PlanetScale's <a href="https://planetscale.com/docs/billing#organization-usage-and-billing-page">dashboard</a>.</p>
<p>When you create a PlanetScale database from the Cloudflare dashboard, you receive the same PlanetScale developer experience, including development branches, query insights, and Model Context Protocol (MCP) server support for agents.</p>
<p>To get started, refer to <a href="/hyperdrive/planetscale/">PlanetScale Postgres and MySQL with Hyperdrive</a>.</p>
</div></article></div>
