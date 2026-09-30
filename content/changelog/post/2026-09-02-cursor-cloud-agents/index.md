<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 2, 2026</time><h2 id="post-title">Run Cursor Cloud Agents on Cloudflare via self-hosted machines</h2>
<div class="changelog-badges"><span>sandbox</span></div><div class="changelog-body"><p><a href="https://cursor.com/docs/cloud-agent/self-hosted">Cursor self-hosted machines</a> let you run Cursor Cloud Agents on Cloudflare. Each assigned session runs in its own isolated environment backed by <a href="/containers/">Cloudflare Containers</a>.</p>
<p><img src="/assets/upstream/images/changelog/sandbox/cursor-cloud-agents-self-hosted-pool.png" alt="Cursor Cloud Agents environment selector showing the cloudflare-pool self-hosted machine pool" /></p>
<p>Cursor hosts the agent loop, inference, and planning. Cloudflare runs commands, file edits, repository operations, and other tools inside infrastructure that you control. The open-source <a href="https://github.com/anysphere/cloudflare-workers">Cursor Cloudflare Workers template</a> deploys the Worker, Durable Object namespace, container application, R2 bucket binding, and cron trigger used by the integration.</p>
<p>To get started, refer to <a href="/sandbox/tutorials/cursor-cloud-agents/">Run Cursor Cloud Agents on Cloudflare via self-hosted machines</a>.</p>
</div></article></div>
