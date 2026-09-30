<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 29, 2026</time><h2 id="post-title">D1 migrations support nested layouts via `migrations_pattern`</h2>
<div class="changelog-badges"><span>d1</span></div><div class="changelog-body"><p>You can now point <code>wrangler d1 migrations apply</code> at a nested migrations layout — such as the one produced by <a href="https://orm.drizzle.team/">Drizzle</a> (<code>migrations/0001_init/migration.sql</code>) — using the new <code>migrations_pattern</code> D1 binding config:</p>
<pre><code class="language-jsonc">{&#10;	&quot;d1_databases&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;DB&quot;,&#10;			&quot;database_name&quot;: &quot;my-database&quot;,&#10;			&quot;database_id&quot;: &quot;&lt;UUID&gt;&quot;,&#10;			&quot;migrations_dir&quot;: &quot;migrations&quot;,&#10;			&quot;migrations_pattern&quot;: &quot;migrations/*/migration.sql&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p><code>migrations_pattern</code> is a glob (relative to your Wrangler config file) used to discover migration files. It defaults to <code>${migrations_dir}/*.sql</code>, so existing projects keep working unchanged. Each migration's name is recorded in the migrations table as a path relative to <code>migrations_dir</code>.</p>
<p>To learn more, visit D1's <a href="/d1/reference/migrations/#nested-migration-layouts">migrations documentation</a>.</p>
</div></article></div>
