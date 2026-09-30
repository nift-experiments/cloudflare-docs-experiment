<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 13, 2026</time><h2 id="post-title">`wrangler types` now generates types for all environments</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <code>wrangler types</code> command now generates TypeScript types for bindings from <strong>all environments</strong> defined in your Wrangler configuration file by default.</p>
<p>Previously, <code>wrangler types</code> only generated types for bindings in the top-level configuration (or a single environment when using the <code>--env</code> flag). This meant that if you had environment-specific bindings — for example, a KV namespace only in production or an R2 bucket only in staging — those bindings would be missing from your generated types, causing TypeScript errors when accessing them.</p>
<p>Now, running <code>wrangler types</code> collects bindings from all environments and includes them in the generated <code>Env</code> type. This ensures your types are complete regardless of which environment you deploy to.</p>
<h4 id="generating-types-for-a-specific-environment">Generating types for a specific environment</h4>
<p>If you want the previous behavior of generating types for only a specific environment, you can use the <code>--env</code> flag:</p>
<pre><code class="language-sh">wrangler types --env production&#10;</code></pre>
<p>Learn more about <a href="/workers/wrangler/commands/general/#types">generating types for your Worker</a> in the Wrangler documentation.</p>
</div></article></div>
