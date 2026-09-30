<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 12, 2026</time><h2 id="post-title">Validate your generated types with `wrangler types --check`</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now supports a <code>--check</code> flag for the <code>wrangler types</code> command. This flag validates that your generated types are up to date without writing any changes to disk.</p>
<p>This is useful in CI/CD pipelines where you want to ensure that developers have regenerated their types after making changes to their Wrangler configuration. If the types are out of date, the command will exit with a non-zero status code.</p>
<pre><code class="language-sh">npx wrangler types --check&#10;</code></pre>
<p>If your types are up to date, the command will succeed silently. If they are out of date, you'll see an error message indicating which files need to be regenerated.</p>
<p>For more information, see the <a href="/workers/wrangler/commands/general/#types">Wrangler types documentation</a>.</p>
</div></article></div>
