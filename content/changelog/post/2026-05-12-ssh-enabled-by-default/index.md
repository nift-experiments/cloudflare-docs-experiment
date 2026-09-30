<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 12, 2026</time><h2 id="post-title">SSH through Wrangler is now enabled by default for Containers</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>SSH through Wrangler is now enabled by default for <a href="/containers/">Containers</a>. Previously, you had to set <code>ssh.enabled</code> to <code>true</code> in your Container configuration before you could connect.</p>
<p>This change does not expose any publicly accessible ports on your Container. The SSH service is reachable only through <a href="/workers/wrangler/commands/containers/#containers-ssh"><code>wrangler containers ssh</code></a>, which authenticates against your Cloudflare account. You also need to add an <code>ssh-ed25519</code> public key to <code>authorized_keys</code> before anyone can connect, so enabling SSH alone does not grant access.</p>
<p>To connect, add a public key to your Container configuration and run <code>wrangler containers ssh &lt;INSTANCE_ID&gt;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17711.md")</div>
<p>To disable SSH, set <code>ssh.enabled</code> to <code>false</code> in your Container configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17712.md")</div>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>
</div></article></div>
