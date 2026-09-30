<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 19, 2026</time><h2 id="post-title">Manage Cloudflare Tunnels with Wrangler</h2>
<div class="changelog-badges"><span>tunnel</span><span>workers</span></div><div class="changelog-body"><p>You can now manage <a href="/tunnel/">Cloudflare Tunnels</a> directly from <a href="/workers/wrangler/">Wrangler</a>, the CLI for the Cloudflare Developer Platform. The new <a href="/workers/wrangler/commands/tunnel/"><code>wrangler tunnel</code></a> commands let you create, run, and manage tunnels without leaving your terminal.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/wrangler-tunnel.gif" alt="Wrangler tunnel commands demo" /></p>
<p>Available commands:</p>
<ul>
<li><code>wrangler tunnel create</code> — Create a new remotely managed tunnel.</li>
<li><code>wrangler tunnel list</code> — List all tunnels in your account.</li>
<li><code>wrangler tunnel info</code> — Display details about a specific tunnel.</li>
<li><code>wrangler tunnel delete</code> — Delete a tunnel.</li>
<li><code>wrangler tunnel run</code> — Run a tunnel using the cloudflared daemon.</li>
<li><code>wrangler tunnel quick-start</code> — Start a free, temporary tunnel without an account using <a href="/tunnel/get-started/#quick-tunnels-development">Quick Tunnels</a>.</li>
</ul>
<p>Wrangler handles downloading and managing the <a href="/tunnel/downloads/">cloudflared</a> binary automatically. On first use, you will be prompted to download <code>cloudflared</code> to a local cache directory.</p>
<p>These commands are currently experimental and may change without notice.</p>
<p>To get started, refer to the <a href="/workers/wrangler/commands/tunnel/">Wrangler tunnel commands documentation</a>.</p>
</div></article></div>
