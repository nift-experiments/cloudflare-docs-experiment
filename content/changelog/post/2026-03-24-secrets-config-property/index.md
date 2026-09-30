<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 25, 2026</time><h2 id="post-title">Declare required secrets in your Wrangler configuration</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The new <code>secrets</code> configuration property lets you declare the secret names your Worker requires in your Wrangler configuration file. Required secrets are validated during local development and deploy, and used as the source of truth for type generation.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17802.md")</div>
<h4 id="local-development">Local development</h4>
<p>When <code>secrets</code> is defined, <code>wrangler dev</code> and <code>vite dev</code> load only the keys listed in <code>secrets.required</code> from <code>.dev.vars</code> or <code>.env</code>/<code>process.env</code>. Additional keys in those files are excluded. If any required secrets are missing, a warning is logged listing the missing names.</p>
<h4 id="type-generation">Type generation</h4>
<p><code>wrangler types</code> generates typed bindings from <code>secrets.required</code> instead of inferring names from <code>.dev.vars</code> or <code>.env</code>. This lets you run type generation in CI or other environments where those files are not present. Per-environment secrets are supported — the aggregated <code>Env</code> type marks secrets that only appear in some environments as optional.</p>
<h4 id="deploy">Deploy</h4>
<p><code>wrangler deploy</code> and <code>wrangler versions upload</code> validate that all secrets in <code>secrets.required</code> are configured on the Worker before the operation succeeds. If any required secrets are missing, the command fails with an error listing which secrets need to be set.</p>
<p>For more information, refer to the <a href="/workers/wrangler/configuration/#secrets-configuration-property"><code>secrets</code> configuration property</a> reference.</p>
</div></article></div>
