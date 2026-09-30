<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 20, 2026</time><h2 id="post-title">Use FUSE in local Containers development</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>Miniflare now automatically grants local Containers the Docker privileges required for Filesystem in Userspace (FUSE). This applies to <code>wrangler dev</code>, the Cloudflare Vite plugin, and direct Miniflare use.</p>
<p>Miniflare grants these privileges when the local Docker daemon runs inside a virtual machine (VM). This includes Docker engines on macOS and through Windows Subsystem for Linux (WSL). On Linux, Miniflare grants the privileges for local rootless Docker when <code>/dev/fuse</code> is available.</p>
<p>Rootful Docker on Linux does not support FUSE by default during local development. Miniflare does not grant FUSE privileges when the Docker daemon does not meet these conditions or cannot be inspected.</p>
<p>For requirements and troubleshooting, refer to <a href="/containers/guides/local-dev/#fuse-support">FUSE support during local development</a>. For a complete example, refer to <a href="/containers/examples/r2-fuse-mount/">Mount R2 buckets with FUSE</a>.</p>
</div></article></div>
