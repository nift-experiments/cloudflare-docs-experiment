<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 10, 2026</time><h2 id="post-title">Use Cloudflare Containers with Codex via the OpenAI Agents API</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>The OpenAI Agents API gives your application access to Codex through an OpenAI-managed API.</p>
<p>OpenAI manages sessions, orchestration, context compaction, and recovery while your application provides tools and uses Cloudflare Containers as the execution environment.</p>
<p>Cloudflare Containers can now provide self-hosted execution environments for the OpenAI Agents API. The open-source <a href="https://github.com/cloudflare/sandbox-sdk/tree/main/openai/agents-api">OpenAI Agents API Workers template</a> provides a reference implementation. The Worker maintains a Cloudflare Container for each Codex session, keeps active work running, reconnects on follow-up input, and shuts down automatically when idle.</p>
<p>You can configure the reference implementation to meet your needs by extending the Container to provide controlled access to data and the network or by integrating it with other Cloudflare products.</p>
<p>To get started, refer to <a href="/sandbox/tutorials/openai-agents-api/">Run Codex on Cloudflare using the OpenAI Agents API</a>.</p>
</div></article></div>
