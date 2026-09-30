<table>
<thead>
<tr>
<th>Feature</th>
<th>Free</th>
<th>Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Reads</td>
<td>100,000 reads per day</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Writes to different keys</td>
<td>1,000 writes per day</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Writes to same key</td>
<td>1 per second</td>
<td>1 per second</td>
</tr>
<tr>
<td>Operations/Worker invocation <sup><a href="#footnote-1">1</a></sup></td>
<td>1000</td>
<td>1000</td>
</tr>
<tr>
<td>Namespaces per account</td>
<td>1,000</td>
<td>1,000</td>
</tr>
<tr>
<td>Storage/account</td>
<td>1 GB</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Storage/namespace</td>
<td>1 GB</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Keys/namespace</td>
<td>Unlimited</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Key size</td>
<td>512 bytes</td>
<td>512 bytes</td>
</tr>
<tr>
<td>Key metadata</td>
<td>1024 bytes</td>
<td>1024 bytes</td>
</tr>
<tr>
<td>Value size</td>
<td>25 MiB</td>
<td>25 MiB</td>
</tr>
<tr>
<td>Minimum <a href="/kv/api/read-key-value-pairs/#cachettl-parameter"><code>cacheTtl</code></a> <sup><a href="#footnote-2">2</a></sup></td>
<td>30 seconds</td>
<td>30 seconds</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/9500.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="free-versus-paid-plan-pricing">Free versus Paid plan pricing</h3>
@markup("md", "content/.markup/bodies/9499.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-kv-rest-api-limits">Workers KV REST API limits</h3>
@markup("md", "content/.markup/bodies/9498.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Within a single invocation, a Worker can make up to 1,000 operations to external services (for example, 500 Workers KV reads and 500 R2 reads). A bulk request to Workers KV counts for 1 request to an external service.</li>
<li id="footnote-2">The maximum value is [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER).</li></ol></section>
