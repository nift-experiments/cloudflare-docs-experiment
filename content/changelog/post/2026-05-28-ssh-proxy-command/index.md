<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 28, 2026</time><h2 id="post-title">Wrangler supports SSH ProxyCommand for Containers</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><a href="/workers/wrangler/">Wrangler</a> supports using <code>wrangler containers ssh</code> as an OpenSSH <code>ProxyCommand</code> for <a href="/containers/">Containers</a>. This lets your local SSH client connect to a running Container through Wrangler.</p>
<pre><code class="language-sh">ssh -o ProxyCommand=&quot;wrangler containers ssh %h&quot; cloudchamber@&lt;INSTANCE_ID&gt;&#10;</code></pre>
<p>When standard input and output are piped, Wrangler forwards data to the SSH server in the Container. You can also pass <code>--stdio</code> to force this mode.</p>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>
</div></article></div>
