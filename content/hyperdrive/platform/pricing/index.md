---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/platform/pricing/
  description: Hyperdrive pricing details for Free and Workers Paid plans.
  full_title: Pricing · Cloudflare Hyperdrive docs
  head_html: <title>Pricing · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Hyperdrive pricing details for Free and Workers Paid plans."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/platform/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/platform/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Hyperdrive pricing details for Free and Workers Paid plans."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/platform/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Hyperdrive,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/platform/pricing/#page","headline":"Pricing \u00b7 Cloudflare Hyperdrive docs","description":"Hyperdrive pricing details for Free and Workers Paid plans.","url":"https://developers.cloudflare.com/hyperdrive/platform/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/platform/pricing/
  schema: 1
---
<p>Hyperdrive is included in both the Free and Paid <a href="/workers/platform/pricing/">Workers plans</a>.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free plan<sup><a href="#footnote-workers-hyperdrive-pricing-mdx-1">1</a></sup></th>
<th>Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Database queries<sup><a href="#footnote-workers-hyperdrive-pricing-mdx-2">2</a></sup></td>
<td>100,000 / day</td>
<td>Unlimited</td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9021.md")
</div></details>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-workers-hyperdrive-pricing-mdx-1">The Workers Free plan includes limited Hyperdrive usage. All limits reset daily at 00:00 UTC. If you exceed any one of these limits, further operations of that type will fail with an error.</li>
<li id="footnote-workers-hyperdrive-pricing-mdx-2">Database queries refers to any database statement made via Hyperdrive, whether a query (`SELECT`), a modification (`INSERT`,`UPDATE`, or `DELETE`) or a schema change (`CREATE`, `ALTER`, `DROP`).</li></ol></section>
<p>Hyperdrive limits are automatically adjusted when subscribed to a Workers Paid plan. Hyperdrive's <a href="/hyperdrive/concepts/how-hyperdrive-works/">connection pooling and query caching</a> are included in Workers Paid plan, so do not incur any additional charges.</p>
<h2 id="planetscale-postgres-mysql">PlanetScale Postgres &amp; MySQL</h2>
<p>You can create PlanetScale Postgres and MySQL databases from Cloudflare and bill PlanetScale database usage through your Cloudflare account as a pay-as-you-go customer.</p>
<p>PlanetScale database usage is separate from Hyperdrive usage. When you create a PlanetScale database from the Cloudflare dashboard, PlanetScale usage appears on your Cloudflare invoice each billing period as a dollar total at PlanetScale's standard <a href="https://planetscale.com/pricing">pricing</a>.</p>
<p>You can view per-database billing usage in the <a href="https://planetscale.com/docs/billing#organization-usage-and-billing-page">PlanetScale dashboard</a>. To learn how PlanetScale databases work with Workers and Hyperdrive, refer to <a href="/hyperdrive/planetscale/">PlanetScale Postgres and MySQL with Hyperdrive</a>.</p>
<h2 id="pricing-faq">Pricing FAQ</h2>
<h3 id="does-connection-pooling-or-query-caching-incur-additional-charges">Does connection pooling or query caching incur additional charges?</h3>
<p>No. Hyperdrive's built-in cache and connection pooling are included within the stated plans above. There are no hidden limits other than those <a href="/hyperdrive/platform/limits/">published</a>.</p>
<h3 id="are-cached-queries-counted-the-same-as-uncached-queries">Are cached queries counted the same as uncached queries?</h3>
<p>Yes, any query made through Hyperdrive, whether cached or uncached, whether query or mutation, is counted according to the limits above.</p>
<h3 id="does-hyperdrive-charge-for-data-transfer-egress">Does Hyperdrive charge for data transfer / egress?</h3>
<p>No.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9020.md")
</aside>
