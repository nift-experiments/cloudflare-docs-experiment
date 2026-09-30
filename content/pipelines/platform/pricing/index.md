<p>Pipelines charges based on two dimensions:</p>
<ol>
<li><strong>SQL transforms</strong>: The volume of data processed by stateless SQL.</li>
<li><strong>Sinks</strong>: The volume of data delivered to each sink destination.</li>
</ol>
<p>Ingress into a Pipeline stream is free. Standard <a href="/r2/pricing/">R2 storage and operations</a> charges apply for data written to R2 buckets. <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges apply when writing to Iceberg tables.</p>
<p>All included usage is on a monthly basis.</p>
<h2 id="pipelines-pricing">Pipelines pricing</h2>
<table>
<thead>
<tr>
<th></th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Streams (ingress)</strong></td>
<td></td>
</tr>
<tr>
<td>Included</td>
<td>Unlimited</td>
</tr>
<tr>
<td><strong>SQL transforms</strong></td>
<td></td>
</tr>
<tr>
<td>Included</td>
<td>50 GB / month</td>
</tr>
<tr>
<td>Additional</td>
<td>$0.04 / GB</td>
</tr>
<tr>
<td><strong>Sinks (egress)</strong> <sup><a href="#footnote-1">1</a></sup></td>
<td></td>
</tr>
<tr>
<td>Included</td>
<td>50 GB / month</td>
</tr>
<tr>
<td>R2 — JSON format</td>
<td>$0.03 / GB</td>
</tr>
<tr>
<td>R2 — Parquet / Iceberg</td>
<td>$0.06 / GB</td>
</tr>
</tbody>
</table>
<h3 id="streams">Streams</h3>
<p>Streams provide durable, distributed log storage that buffers incoming messages. Ingress into a stream is free regardless of volume. A single stream can be read by multiple pipelines.</p>
<h3 id="sql-transforms">SQL transforms</h3>
<p>SQL transforms let you filter, reshape, and compute over data before it reaches a sink. Any query currently counts as a transform.</p>
<p>Pricing covers stateless transforms (for example, filter, reshape, unnest, cast, and compute). Future stateful operations such as aggregations, joins, and windows may be priced separately.</p>
<h3 id="sinks">Sinks</h3>
<p>Sink pricing is based on the volume of uncompressed data delivered to the destination. The rate varies by output format:</p>
<ul>
<li><strong>JSON</strong>: $0.03 / GB — lowest compute cost, suitable for simple log forwarding.</li>
<li><strong>Parquet / Iceberg</strong>: $0.06 / GB — higher compute cost for columnar encoding and Iceberg table management. Best for analytics workloads.</li>
</ul>
<h2 id="billing-examples">Billing examples</h2>
<h3 id="example-filtered-ingest-to-iceberg-with-sql">Example: filtered ingest to Iceberg with SQL</h3>
<p>A pipeline ingests 500 GB of event data per month. A SQL transform filters and reshapes the data, reducing output to 300 GB written to an R2 Data Catalog Iceberg table.</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Streams</td>
<td>500 GB</td>
<td>Unlimited</td>
<td>0 GB</td>
<td>$0.00</td>
</tr>
<tr>
<td>SQL transforms</td>
<td>500 GB</td>
<td>50 GB</td>
<td>450 GB</td>
<td>$18.00</td>
</tr>
<tr>
<td>Sinks (Iceberg)</td>
<td>300 GB</td>
<td>50 GB</td>
<td>250 GB</td>
<td>$15.00</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$33.00</strong></td>
</tr>
</tbody>
</table>
<h2 id="cloudflare-billing-policy">Cloudflare billing policy</h2>
<p>To learn more about how usage is billed, refer to <a href="/billing/understand/billing-policy/">Cloudflare Billing Policy</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Sink egress is measured on uncompressed data.</li></ol></section>
