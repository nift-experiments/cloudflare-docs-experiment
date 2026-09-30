<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 12, 2026</time><h2 id="post-title">SSH into running Container instances</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>You can now SSH into running Container instances using Wrangler. This is useful for debugging, inspecting running processes, or executing one-off commands inside a Container.</p>
<p>To connect, enable <code>wrangler_ssh</code> in your Container configuration and add your <code>ssh-ed25519</code> public key to <code>authorized_keys</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17709.md")</div>
<p>Then connect with:</p>
<pre><code class="language-sh">wrangler containers ssh &lt;INSTANCE_ID&gt;&#10;</code></pre>
<p>You can also run a single command without opening an interactive shell:</p>
<pre><code class="language-sh">wrangler containers ssh &lt;INSTANCE_ID&gt; -- ls -al&#10;</code></pre>
<p>Use <code>wrangler containers instances &lt;APPLICATION&gt;</code> to find the instance ID for a running Container.</p>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>
</div></article></div>
