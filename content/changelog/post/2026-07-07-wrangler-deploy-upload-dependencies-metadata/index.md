<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 9, 2026</time><h2 id="post-title">Send npm package dependency metadata with Worker uploads</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now collects npm package dependency information from your project's <code>package.json</code> during <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> and <a href="/workers/wrangler/commands/general/#upload"><code>wrangler versions upload</code></a>, and includes it in the upload metadata sent to the Cloudflare API. This data, each dependency's name, declared version range, and exact installed version, enables dependency analytics and future supply chain security features such as vulnerability alerting.</p>
<p>To opt out, set <a href="/workers/wrangler/configuration/#top-level-only-keys"><code>dependencies_instrumentation.enabled</code></a> to <code>false</code> in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17805.md")</div>
<p>For more details, refer to <a href="/workers/wrangler/configuration/#top-level-only-keys">Wrangler configuration</a>.</p>
</div></article></div>
