<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 25, 2026</time><h2 id="post-title">Write structured queries to filter and search your Workers logs and traces</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/observability/">Workers Observability</a> now includes a query language that lets you write structured queries directly in the search bar to filter your logs and traces. The search bar doubles as a free text search box — type any term to search across all metadata and attributes, or write field-level queries for precise filtering.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-02-24-query-language.png" alt="Workers Observability search bar with autocomplete suggestions and Query Builder sidebar filters" /></p>
<p>Queries written in the search bar sync with the <a href="/workers/observability/">Query Builder</a> sidebar, so you can write a query by hand and then refine it visually, or build filters in the Query Builder and see the corresponding query syntax. The search bar provides autocomplete suggestions for metadata fields and operators as you type.</p>
<p>The query language supports:</p>
<ul>
<li><strong>Free text search</strong> — search everywhere with a keyword like <code>error</code>, or match an exact phrase with <code>&quot;exact phrase&quot;</code></li>
<li><strong>Field queries</strong> — filter by specific fields using comparison operators (for example, <code>status = 500</code> or <code>$workers.wallTimeMs &gt; 100</code>)</li>
<li><strong>Operators</strong> — <code>=</code>, <code>!=</code>, <code>&gt;</code>, <code>&gt;=</code>, <code>&lt;</code>, <code>&lt;=</code>, and <code>:</code> (contains)</li>
<li><strong>Functions</strong> — <code>contains(field, value)</code>, <code>startsWith(field, prefix)</code>, <code>regex(field, pattern)</code>, and <code>exists(field)</code></li>
<li><strong>Boolean logic</strong> — add conditions with <code>AND</code>, <code>OR</code>, and <code>NOT</code></li>
</ul>
<p>Select the help icon next to the search bar to view the full syntax reference, including all supported operators, functions, and keyboard shortcuts.</p>
<p>Go to the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/">Workers Observability dashboard</a> to try the query language.</p>
</div></article></div>
