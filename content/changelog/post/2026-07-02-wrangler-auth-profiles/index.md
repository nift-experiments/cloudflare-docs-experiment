<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 2, 2026</time><h2 id="post-title">Work across multiple accounts with Wrangler auth profiles</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/wrangler/">Wrangler CLI</a> now supports auth profiles: named logins that you scope to specific Cloudflare accounts and switch between automatically, based on the directory you are working in.</p>
<p>A profile is a named OAuth login bound to a directory. Commands run in that directory, and its subdirectories, use the matching account — so you can move between accounts without re-running <code>wrangler login</code>.</p>
<p>Use profiles to keep a separate login for each client when working at an agency, or to separate staging and production into different accounts. Pair a profile with an <code>account_id</code> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> so a command cannot reach the wrong account.</p>
<pre><code class="language-sh">&#35; Create a profile for each account, choosing which accounts it can reach&#10;wrangler auth create client-a&#10;wrangler auth activate client-a ~/clients/client-a&#10;&#10;wrangler auth create client-b&#10;wrangler auth activate client-b ~/clients/client-b&#10;</code></pre>
<p>Use the <code>--profile</code> flag to run a single command with a specific profile:</p>
<pre><code class="language-sh">wrangler deploy --profile personal&#10;</code></pre>
<p>In CI and other automated environments, <code>CLOUDFLARE_API_TOKEN</code> still takes precedence over all profiles.</p>
<p>For setup, the resolution order, and the full command reference, refer to <a href="/workers/wrangler/profiles/">Authentication profiles</a>.</p>
</div></article></div>
