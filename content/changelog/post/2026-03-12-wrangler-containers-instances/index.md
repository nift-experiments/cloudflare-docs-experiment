<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 12, 2026</time><h2 id="post-title">List Container instances with `wrangler containers instances`</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>A new <a href="/workers/wrangler/commands/containers/#containers-instances"><code>wrangler containers instances</code></a> command lists all instances for a given Container application. This mirrors the instances view in the Cloudflare dashboard.</p>
<p>The command displays each instance's ID, name, state, location, version, and creation time:</p>
<pre><code class="language-sh">wrangler containers instances &lt;APPLICATION_ID&gt;&#10;</code></pre>
<p>Use the <code>--json</code> flag for machine-readable output, which is also the default format in non-interactive environments such as CI pipelines.</p>
<p>For the full list of options, refer to the <a href="/workers/wrangler/commands/containers/#containers-instances"><code>containers instances</code> command reference</a>.</p>
</div></article></div>
