<p>R2 Data Catalog charges based on two dimensions in addition to standard <a href="/r2/pricing/">R2 storage and operations</a>:</p>
<ol>
<li><strong>Catalog operations</strong>: Metadata operations such as creating tables, reading table metadata, and updating table properties.</li>
<li><strong>Compaction data processed</strong>: The volume of data processed and objects compacted when <a href="/r2-data-catalog/table-maintenance/">automatic table compaction</a> is turned on.</li>
</ol>
<p>All included usage is on a monthly basis.</p>
<h2 id="r2-data-catalog-pricing">R2 Data Catalog pricing</h2>
<table>
<thead>
<tr>
<th></th>
<th>Pricing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Catalog operations</strong></td>
<td></td>
</tr>
<tr>
<td>Included</td>
<td>1 million operations / month</td>
</tr>
<tr>
<td>Additional</td>
<td>$9.00 / million operations</td>
</tr>
<tr>
<td><strong>Data processed (Compaction)</strong> <sup><a href="#footnote-1">1</a></sup></td>
<td></td>
</tr>
<tr>
<td>Included</td>
<td>10 GB / month</td>
</tr>
<tr>
<td>Additional (data processed)</td>
<td>$0.005 / GB processed</td>
</tr>
<tr>
<td><strong>Objects processed (Compaction)</strong> <sup><a href="#footnote-1">1</a></sup></td>
<td></td>
</tr>
<tr>
<td>Included</td>
<td>1 million objects / month</td>
</tr>
<tr>
<td>Additional</td>
<td>$2.00 / million objects</td>
</tr>
</tbody>
</table>
<h3 id="catalog-operations">Catalog operations</h3>
<p>Catalog operations are metadata requests made to the Iceberg REST catalog, such as creating a table, retrieving table metadata, updating table properties, and listing tables in a namespace. These operations do not scan or move data.</p>
<h3 id="compaction">Compaction</h3>
<p>When you turn on <a href="/r2-data-catalog/table-maintenance/">automatic compaction</a>, R2 Data Catalog periodically rewrites small data files into larger, optimized files. This improves query performance and reduces the number of files in your table. Compaction is billed on two sub-dimensions:</p>
<ul>
<li><strong>Data processed</strong>: The total bytes read and rewritten during compaction.</li>
<li><strong>Objects processed</strong>: The number of data files compacted.</li>
</ul>
<p>Compaction charges only apply when compaction is turned on for a table. If you have not turned on compaction, you will not incur any compaction charges.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11320.md")
</aside>
<h3 id="snapshot-expiration">Snapshot Expiration</h3>
<p>When you turn on <a href="/r2-data-catalog/table-maintenance/#why-do-i-need-snapshot-expiration">automatic snapshot expiration</a>, R2 Data Catalog automatically deletes old snapshots and their associated data files after a specified retention period. Snapshot expiration is free of charge and does not incur any additional costs outside of the standard R2 storage and data catalog operations charges.</p>
<h2 id="billing-examples">Billing examples</h2>
<h3 id="example-1-low-volume-analytics-table">Example 1: Low-volume analytics table</h3>
<p>A user maintains a single Iceberg table with 50 GB of data. They make 500,000 catalog operations per month and have compaction turned on, which processes 20 GB across 200,000 files.</p>
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
<td>Catalog operations</td>
<td>500,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td>Compaction (data processed)</td>
<td>20 GB</td>
<td>10 GB</td>
<td>10 GB</td>
<td>$0.05</td>
</tr>
<tr>
<td>Compaction (objects)</td>
<td>200,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td><strong>Total (Data Catalog)</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$0.05</strong></td>
</tr>
</tbody>
</table>
<p>Standard R2 storage charges ($0.015 / GB-month) apply separately for the 50 GB of data stored.</p>
<h3 id="example-2-streaming-ingest-at-20-mb-s">Example 2: Streaming ingest at 20 MB/s</h3>
<p>A user streams data into an Iceberg table at 20 MB/s using <a href="/pipelines/">Pipelines</a>. Over a month (~30 days) this produces approximately 50,625 GB (~49 TB) of data, 347,000 catalog operations, and compaction processes roughly 50,625 GB across 43,200 files.</p>
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
<td>R2 storage</td>
<td>50,625 GB-month</td>
<td>10 GB-month</td>
<td>50,615 GB-month</td>
<td>$759.23</td>
</tr>
<tr>
<td>Catalog operations</td>
<td>347,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td>Compaction (data processed)</td>
<td>50,625 GB</td>
<td>10 GB</td>
<td>50,615 GB</td>
<td>$253.08</td>
</tr>
<tr>
<td>Compaction (objects)</td>
<td>43,200</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$1,012.31</strong></td>
</tr>
</tbody>
</table>
<p>For large-scale use cases, storage costs are typically the largest component of the bill.</p>
<h2 id="cloudflare-billing-policy">Cloudflare billing policy</h2>
<p>To learn more about how usage is billed, refer to <a href="/billing/understand/billing-policy/">Cloudflare Billing Policy</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Only applies when compaction is enabled for a table.</li></ol></section>
