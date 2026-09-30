<h2 id="limits">Limits</h2>
<p>The following limits apply based on your <a href="/workers/platform/pricing/">Workers plan</a>:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Search instances per account</td>
<td>100</td>
<td>5,000</td>
</tr>
<tr>
<td>Namespaces per account</td>
<td>100</td>
<td>100</td>
</tr>
<tr>
<td>Files per instance</td>
<td>100,000</td>
<td>1M or 500K for hybrid search</td>
</tr>
<tr>
<td>Pages per crawl, <code>discover</code> parse type</td>
<td>100,000</td>
<td>100,000</td>
</tr>
<tr>
<td>Max file size</td>
<td>4 MB</td>
<td>4 MB</td>
</tr>
<tr>
<td>Queries per month</td>
<td>20,000</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Instances per cross-instance search request</td>
<td>10</td>
<td>10</td>
</tr>
<tr>
<td>Maximum pages crawled per day</td>
<td>500</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Max custom metadata fields</td>
<td>5 per AI Search instance</td>
<td>5 per AI Search instance</td>
</tr>
<tr>
<td>Metadata per vector</td>
<td>10 KiB total, including system overhead</td>
<td>10 KiB total, including system overhead</td>
</tr>
<tr>
<td>Filterable indexed string data</td>
<td>First 64 UTF-8 bytes per string</td>
<td>First 64 UTF-8 bytes per string</td>
</tr>
</tbody>
</table>
<p>Website crawling is bounded by several of these limits at once. A <code>discover</code> crawl accepts up to 100,000 pages, but the files per instance and maximum pages crawled per day limits also apply, so the number of pages you end up with is whichever of those values is lowest. On Workers Free, the daily limit of 500 pages is the binding one.</p>
<p>For the limits that apply only to website data sources, refer to <a href="/ai-search/configuration/data-source/website/#limits">Website</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/2996.md")
</aside>
<h2 id="pricing">Pricing</h2>
<p>During the open beta, AI Search is free within these limits. <a href="/workers-ai/platform/pricing/">Workers AI</a> and <a href="/ai-gateway/reference/pricing/">AI Gateway</a> usage is billed separately. Pricing details will be communicated at least 30 days before any billing begins.</p>
<p>Storage, vector indexing, and the <a href="/browser-run/pricing/">Browser Run</a> usage that website crawling consumes are included with AI Search. You are not billed separately for them.</p>
<h2 id="historical-billing">Historical billing</h2>
<p>Instances created before AI Search moved to managed infrastructure ran on Cloudflare services in your own account, so older invoices may include separate charges for <a href="/r2/pricing/">R2</a>, <a href="/vectorize/platform/pricing/">Vectorize</a>, <a href="/workers-ai/platform/pricing/">Workers AI</a>, <a href="/ai-gateway/reference/pricing/">AI Gateway</a>, and <a href="/browser-run/pricing/">Browser Run</a>.</p>
<p>After the move, storage, vector indexing, and Browser Run usage for crawling are included. Workers AI and AI Gateway are still billed separately.</p>
<p>If your instance crawled a website, those pages now live in built-in storage. The dedicated R2 bucket AI Search originally created in your account is no longer used. It remains in your account, and any objects left in it may still count toward <a href="/r2/pricing/">R2 storage usage</a>. AI Search no longer writes to this bucket, so you can delete it if you no longer need its contents.</p>
