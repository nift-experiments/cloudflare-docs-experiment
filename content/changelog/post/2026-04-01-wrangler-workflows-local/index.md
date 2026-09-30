<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 1, 2026</time><h2 id="post-title">All Wrangler commands for Workflows now support local development</h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>All <code>wrangler workflows</code> commands now accept a <code>--local</code> flag to target a Workflow running in a local <code>wrangler dev</code> session instead of the production API.</p>
<p>You can now manage the full Workflow lifecycle locally, including triggering Workflows, listing instances, pausing, resuming, restarting, terminating, and sending events:</p>
<pre><code class="language-sh">npx wrangler workflows list --local&#10;npx wrangler workflows trigger my-workflow --local&#10;npx wrangler workflows instances list my-workflow --local&#10;npx wrangler workflows instances pause my-workflow &lt;INSTANCE_ID&gt; --local&#10;npx wrangler workflows instances send-event my-workflow &lt;INSTANCE_ID&gt; --type my-event --local&#10;</code></pre>
<p>All commands also accept <code>--port</code> to target a specific <code>wrangler dev</code> session (defaults to <code>8787</code>).</p>
<p>For more information, refer to <a href="/workflows/build/local-development/">Workflows local development</a>.</p>
</div></article></div>
