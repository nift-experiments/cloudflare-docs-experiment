<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 5, 2026</time><h2 id="post-title">Rollback support now available in Workflows</h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> now supports saga-style rollbacks,  allowing you to add compensating logic to each <code>step.do()</code> in case of downstream failures. If the instance fails, the rollback handlers will execute in reverse <code>step-start</code> order.</p>
<p>This is useful for multi-step operations that touch external systems, such as inventory reservations, payment authorization, ticket creation, or infrastructure provisioning. Instead of writing all cleanup logic in a top-level <code>catch</code>, you can keep each compensating action next to the step it undoes.</p>
<p>Rollback handlers support their own retry and timeout configuration, and Workflows now exposes rollback outcomes in instance status responses. Workflows analytics also emits rollback lifecycle events, making it easier to distinguish a forward execution failure from a rollback failure when debugging production workflows.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17832.md")</div>
<p>Refer to <a href="/workflows/build/workers-api/#rollback-options">rollback options</a> to learn more.</p>
</div></article></div>
