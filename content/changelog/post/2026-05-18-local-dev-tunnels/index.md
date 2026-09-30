<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 18, 2026</time><h2 id="post-title">Share local dev servers through Cloudflare Tunnel in Wrangler and Vite</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now share local dev sessions through <a href="/tunnel/">Cloudflare Tunnel</a> and get a public URL when using either <a href="/workers/wrangler/">Wrangler</a> or the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>. This is useful when you need to share a preview, test a webhook, or access your app from another device.</p>
<p><img src="/assets/upstream/images/changelog/workers/vite-local-dev-tunnel.gif" alt="Vite local dev tunnel demo" /></p>
<p>This lets you either:</p>
<ul>
<li>start a temporary <a href="/tunnel/get-started/#quick-tunnels-development">Quick tunnel</a> with a random <code>*.trycloudflare.com</code> hostname, or</li>
<li>use an existing <a href="/tunnel/get-started/#create-a-tunnel">named tunnel</a> for a stable hostname and to restrict access with <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>.</li>
</ul>
<p>To start a tunnel, press <code>t</code> in Wrangler or <code>t + Enter</code> in Vite while your dev server is running. For details on setting up a named tunnel, refer to <a href="/workers/local-development/local-dev-tunnels/">Share a local dev server</a>.</p>
</div></article></div>
