<p>This page documents the filter format used by the legacy AutoRAG REST API. For the new AI Search REST API filter syntax, refer to <a href="/ai-search/configuration/retrieval/filtering/">Metadata filtering</a>.</p>
<h2 id="comparison-filter">Comparison filter</h2>
<p>Compare a metadata attribute (for example, <code>folder</code> or <code>timestamp</code>) with a target value:</p>
<pre><code class="language-js">filters: {&#10;  type: &quot;eq&quot;,&#10;  key: &quot;folder&quot;,&#10;  value: &quot;customer-a/&quot;&#10;}&#10;</code></pre>
<h3 id="operators">Operators</h3>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>eq</code></td>
<td>Equals</td>
</tr>
<tr>
<td><code>ne</code></td>
<td>Not equals</td>
</tr>
<tr>
<td><code>gt</code></td>
<td>Greater than</td>
</tr>
<tr>
<td><code>gte</code></td>
<td>Greater than or equal to</td>
</tr>
<tr>
<td><code>lt</code></td>
<td>Less than</td>
</tr>
<tr>
<td><code>lte</code></td>
<td>Less than or equal to</td>
</tr>
</tbody>
</table>
<h2 id="compound-filter">Compound filter</h2>
<p>Combine multiple comparison filters with a logical operator:</p>
<pre><code class="language-js">filters: {&#10;  type: &quot;and&quot;,&#10;  filters: [&#10;    { type: &quot;eq&quot;, key: &quot;folder&quot;, value: &quot;customer-a/&quot; },&#10;    { type: &quot;gte&quot;, key: &quot;timestamp&quot;, value: &quot;1735689600000&quot; }&#10;  ]&#10;}&#10;</code></pre>
<p>The available compound operators are <code>and</code> and <code>or</code>.</p>
<h3 id="limitations">Limitations</h3>
<ul>
<li>No nested combinations of <code>and</code> and <code>or</code>. You can only use one compound operator at a time.</li>
<li>When using <code>or</code>, only the <code>eq</code> operator is allowed and all conditions must filter on the same key.</li>
</ul>
<h2 id="starts-with-filter-for-folders">&quot;Starts with&quot; filter for folders</h2>
<p>To filter for all files within a folder and its subfolders, use a compound filter with range operators.</p>
<p>For example, consider this file structure:</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/3069.md")&#10;&#10;&#10;</pre>
<p>Using <code>{ type: &quot;eq&quot;, key: &quot;folder&quot;, value: &quot;customer-a/&quot; }</code> only matches files directly in that folder (like <code>profile.md</code>), not files in subfolders.</p>
<p>To match all files starting with <code>customer-a/</code>, use a compound filter:</p>
<pre><code class="language-js">filters: {&#10;  type: &quot;and&quot;,&#10;  filters: [&#10;    { type: &quot;gt&quot;, key: &quot;folder&quot;, value: &quot;customer-a//&quot; },&#10;    { type: &quot;lte&quot;, key: &quot;folder&quot;, value: &quot;customer-a/z&quot; }&#10;  ]&#10;}&#10;</code></pre>
<p>This filter matches all paths starting with <code>customer-a/</code> by using:</p>
<ul>
<li><code>gt</code> with <code>customer-a//</code> to include paths greater than the <code>/</code> ASCII character</li>
<li><code>lte</code> with <code>customer-a/z</code> to include paths up to and including the lowercase <code>z</code> ASCII character</li>
</ul>
<h2 id="related">Related</h2>
<ul>
<li><a href="/ai-search/configuration/retrieval/filtering/">Metadata filtering</a> - New AI Search REST API filter format</li>
<li><a href="/ai-search/api/migration/rest-api/">Migrate from AutoRAG Search API</a> - Migration guide with before/after examples</li>
</ul>
