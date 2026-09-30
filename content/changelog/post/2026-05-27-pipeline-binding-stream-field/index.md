<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 4, 2026</time><h2 id="post-title">Pipeline binding configuration field renamed to stream</h2>
<div class="changelog-badges"><span>pipelines</span><span>workers</span></div><div class="changelog-body"><p>The <code>pipeline</code> field inside the <code>pipelines</code> binding configuration in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> has been renamed to <code>stream</code>. The old field is deprecated but still accepted.</p>
<p>Update your configuration to use <code>stream</code> to avoid the deprecation warning.</p>
<p><strong>Before (deprecated):</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17739.md")</div>
<p><strong>After:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17740.md")</div>
<p>No other changes are required. The binding name, TypeScript types, and runtime API (<code>env.MY_PIPELINE.send(...)</code>) remain the same.</p>
<p>For more information on configuring pipeline bindings, refer to <a href="/pipelines/streams/writing-to-streams/#configure-pipeline-binding">Writing to streams</a>.</p>
</div></article></div>
