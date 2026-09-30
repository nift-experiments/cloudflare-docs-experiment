<p>Path filtering allows you to control which files or URLs are indexed by defining include and exclude patterns. Use this to limit indexing to specific content or to skip files you do not want searchable.</p>
<p>Path filtering works with both <a href="/ai-search/configuration/data-source/website/">website</a> and <a href="/ai-search/configuration/data-source/r2/">R2</a> data sources.</p>
<h2 id="configuration">Configuration</h2>
<p>You can configure path filters when creating or editing an AI Search instance. In the dashboard, open <strong>Path Filters</strong> and add your include or exclude rules. You can also update path filters at any time from the <strong>Settings</strong> page of your instance.</p>
<p>When using the REST API, specify <code>include_items</code> and <code>exclude_items</code> in the <code>source_params</code> of your configuration:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Limit</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>include_items</code></td>
<td><code>string[]</code></td>
<td>Maximum 10 patterns</td>
<td>Only index items matching at least one of these patterns</td>
</tr>
<tr>
<td><code>exclude_items</code></td>
<td><code>string[]</code></td>
<td>Maximum 10 patterns</td>
<td>Skip items matching any of these patterns</td>
</tr>
</tbody>
</table>
<p>Both parameters are optional. If neither is specified, all items from the data source are indexed.</p>
<h2 id="filtering-behavior">Filtering behavior</h2>
<h3 id="wildcard-rules">Wildcard rules</h3>
<p>Exclude rules take precedence over include rules. Filtering is applied in this order:</p>
<ol>
<li><strong>Exclude check</strong>: If the item matches any exclude pattern, it is skipped.</li>
<li><strong>Include check</strong>: If include patterns are defined and the item does not match any of them, it is skipped.</li>
<li><strong>Index</strong>: The item proceeds to indexing.</li>
</ol>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>No rules defined</td>
<td>All items are indexed</td>
</tr>
<tr>
<td>Only <code>exclude_items</code> defined</td>
<td>All items except those matching exclude patterns are indexed</td>
</tr>
<tr>
<td>Only <code>include_items</code> defined</td>
<td>Only items matching at least one include pattern are indexed</td>
</tr>
<tr>
<td>Both defined</td>
<td>Exclude patterns are checked first, then remaining items must match an include pattern</td>
</tr>
</tbody>
</table>
<h3 id="pattern-syntax">Pattern syntax</h3>
<p>Patterns use a case-sensitive wildcard syntax based on <a href="https://github.com/micromatch/micromatch">micromatch</a>:</p>
<table>
<thead>
<tr>
<th>Wildcard</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>*</code></td>
<td>Matches any characters except path separators (<code>/</code>)</td>
</tr>
<tr>
<td><code>**</code></td>
<td>Matches any characters including path separators (<code>/</code>)</td>
</tr>
</tbody>
</table>
<p>Patterns can contain:</p>
<ul>
<li>Letters, numbers, and underscores (<code>a-z</code>, <code>A-Z</code>, <code>0-9</code>, <code>_</code>)</li>
<li>Hyphens (<code>-</code>) and dots (<code>.</code>)</li>
<li>Path separators (<code>/</code>)</li>
<li>URL characters (<code>?</code>, <code>:</code>, <code>=</code>, <code>&amp;</code>, <code>%</code>)</li>
<li>Wildcards (<code>*</code>, <code>**</code>)</li>
</ul>
<h3 id="indexing-job-status">Indexing job status</h3>
<p>Items skipped by filtering rules are recorded in job logs with the reason:</p>
<ul>
<li>Exclude match: <code>Skipped by rule: {pattern}</code></li>
<li>No include match: <code>Skipped by Include Rules</code></li>
</ul>
<p>You can view these in the Jobs tab of your AI Search instance to verify your filters are working as expected.</p>
<h3 id="important-notes">Important notes</h3>
<ul>
<li><strong>Case sensitivity:</strong> Pattern matching is case-sensitive. <code>/Blog/*</code> does not match <code>/blog/post.html</code>.</li>
<li><strong>Full path matching:</strong> Patterns match the entire path or URL. Use <code>**</code> at the beginning for partial matching. For example, <code>docs/*</code> matches <code>docs/file.pdf</code> but not <code>site/docs/file.pdf</code>, while <code>**/docs/*</code> matches both.</li>
<li><strong>Single <code>*</code> does not cross directories:</strong> Use <code>**</code> to match across path separators. For example, <code>docs/*</code> matches <code>docs/file.pdf</code> but not <code>docs/sub/file.pdf</code>, while <code>docs/**</code> matches both.</li>
<li><strong>Trailing slashes matter:</strong> URLs are matched as-is without normalization. <code>/blog/</code> does not match <code>/blog</code>.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="r2-data-source">R2 data source</h3>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Pattern</th>
<th>Indexed</th>
<th>Skipped</th>
</tr>
</thead>
<tbody>
<tr>
<td>Index only PDFs in docs</td>
<td>Include: <code>/docs/**/*.pdf</code></td>
<td><code>/docs/guide.pdf</code>, <code>/docs/api/ref.pdf</code></td>
<td><code>/docs/guide.md</code>, <code>/images/logo.png</code></td>
</tr>
<tr>
<td>Exclude temp and backup files</td>
<td>Exclude: <code>**/*.tmp</code>, <code>**/*.bak</code></td>
<td><code>/docs/guide.md</code></td>
<td><code>/data/cache.tmp</code>, <code>/old.bak</code></td>
</tr>
<tr>
<td>Exclude temp and backup folders</td>
<td>Exclude: <code>/temp/**</code>, <code>/backup/**</code></td>
<td><code>/docs/guide.md</code></td>
<td><code>/temp/file.txt</code>, <code>/backup/data.json</code></td>
</tr>
<tr>
<td>Index docs but exclude drafts</td>
<td>Include: <code>/docs/**</code>, Exclude: <code>/docs/drafts/**</code></td>
<td><code>/docs/guide.md</code></td>
<td><code>/docs/drafts/wip.md</code></td>
</tr>
<tr>
<td>Scope an instance to one tenant</td>
<td>Include: <code>/customers/acme/**</code></td>
<td><code>/customers/acme/report.pdf</code></td>
<td><code>/customers/globex/report.pdf</code></td>
</tr>
</tbody>
</table>
<p>To give each tenant an isolated instance backed by a single shared bucket, refer to <a href="/ai-search/how-to/per-tenant-search/#r2">Multitenancy</a>.</p>
<h3 id="website-data-source">Website data source</h3>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Pattern</th>
<th>Indexed</th>
<th>Skipped</th>
</tr>
</thead>
<tbody>
<tr>
<td>Index only blog pages</td>
<td>Include: <code>**/blog/**</code></td>
<td><code>example.com/blog/post</code>, <code>example.com/en/blog/article</code></td>
<td><code>example.com/about</code></td>
</tr>
<tr>
<td>Exclude admin pages</td>
<td>Exclude: <code>**/admin/**</code></td>
<td><code>example.com/blog/post</code></td>
<td><code>example.com/admin/settings</code></td>
</tr>
<tr>
<td>Exclude login pages</td>
<td>Exclude: <code>**/login*</code></td>
<td><code>example.com/blog/post</code></td>
<td><code>example.com/login</code>, <code>example.com/auth/login-form</code></td>
</tr>
<tr>
<td>Index docs but exclude drafts</td>
<td>Include: <code>**/docs/**</code>, Exclude: <code>**/docs/drafts/**</code></td>
<td><code>example.com/docs/guide</code></td>
<td><code>example.com/docs/drafts/wip</code></td>
</tr>
</tbody>
</table>
<h3 id="api-format">API format</h3>
<p>When using the API, specify patterns in <code>source_params</code>:</p>
<pre><code class="language-json">{&#10;	&quot;source_params&quot;: {&#10;		&quot;include_items&quot;: [&quot;&lt;PATTERN_1&gt;&quot;, &quot;&lt;PATTERN_2&gt;&quot;],&#10;		&quot;exclude_items&quot;: [&quot;&lt;PATTERN_1&gt;&quot;, &quot;&lt;PATTERN_2&gt;&quot;]&#10;	}&#10;}&#10;</code></pre>
