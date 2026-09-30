<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 20, 2026</time><h2 id="post-title">AI Search path filtering for website and R2 data sources</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now includes <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> for both <a href="/ai-search/configuration/data-source/website/#path-filtering">website</a> and <a href="/ai-search/configuration/data-source/r2/#path-filtering">R2</a> data sources. You can now control which content gets indexed by defining include and exclude rules for paths.</p>
<p>By controlling what gets indexed, you can improve the relevance and quality of your search results. You can also use path filtering to split a single data source across multiple AI Search instances for specialized search experiences.</p>
<p><img src="/assets/upstream/images/ai-search/path-filtering.png" alt="Path filtering configuration in AI Search" /></p>
<p>Path filtering uses <a href="https://github.com/micromatch/micromatch">micromatch</a> patterns, so you can use <code>*</code> to match within a directory and <code>**</code> to match across directories.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Include</th>
<th>Exclude</th>
</tr>
</thead>
<tbody>
<tr>
<td>Index docs but skip drafts</td>
<td><code>**/docs/**</code></td>
<td><code>**/docs/drafts/**</code></td>
</tr>
<tr>
<td>Keep admin pages out of results</td>
<td>—</td>
<td><code>**/admin/**</code></td>
</tr>
<tr>
<td>Index only English content</td>
<td><code>**/en/**</code></td>
<td>—</td>
</tr>
</tbody>
</table>
<p>Configure path filters when creating a new instance or update them anytime from <strong>Settings</strong>. Check out <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> to learn more.</p>
</div></article></div>
