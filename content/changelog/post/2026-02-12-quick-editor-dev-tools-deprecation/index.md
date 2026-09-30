<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 16, 2026</time><h2 id="post-title">Quick Editor devtools replaced with log viewer</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Cloudflare has deprecated the Workers Quick Editor dev tools inspector and replaced it with a lightweight log viewer.</p>
<p>This aligns our logging with <code>wrangler tail</code> and gives us the opportunity to focus our efforts on bringing benefits from the work we have invested in observability, which would not be possible otherwise.</p>
<p>We have made improvements to this logging viewer based on your feedback such that you can log object and array types, and easily clear the list of logs. This does not include class instances. Limitations are documented in the <a href="/workers/playground/">Workers Playground docs</a>.</p>
<p>If you do need to develop your Worker with a remote inspector, you can still do this using Wrangler locally. Cloning a project from your quick editor to your computer for local development can be done with the <code>wrangler init --from-dash</code> command. For more information, refer to <a href="/workers/wrangler/commands/general/#init">Wrangler commands</a>.</p>
</div></article></div>
