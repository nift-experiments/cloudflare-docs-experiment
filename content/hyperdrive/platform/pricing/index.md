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
