<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 9, 2026</time><h2 id="post-title">New Durable Object namespaces must use the SQLite storage backend</h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>If your account does not already have a key-value (KV) backed Durable Object namespace, you can no longer create new ones. New Durable Object namespaces must use the <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage backend</a>, which has been recommended for all new Durable Objects since it became <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">generally available</a> in 2024.</p>
<p>Create a new class with a <code>new_sqlite_classes</code> migration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17719.md")</div>
<p>SQLite-backed Durable Objects have feature parity with the key-value backend — including the <a href="/durable-objects/api/sqlite-storage-api/#synchronous-kv-api">key-value storage API</a> — and additionally support relational <a href="/durable-objects/api/sqlite-storage-api/#sql-api">SQL queries</a> and <a href="/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api">point-in-time recovery</a> to restore an object's storage to any point in the past 30 days.</p>
<p>If you attempt to create a new key-value backed namespace (a <code>new_classes</code> migration) on an affected account, the deployment fails with the following error:</p>
<pre><code class="language-txt">Creating new key-value backed Durable Object namespaces is no longer supported on this account. Please create a namespace using a `new_sqlite_classes` migration instead.&#10;</code></pre>
<p>This change only affects accounts that are not already using the key-value storage backend. Accounts with at least one existing key-value backed namespace can still create new ones for now, and the Workers Free plan has only ever supported SQLite-backed Durable Objects. It is part of a broader move toward SQLite as the single storage backend for Durable Objects, ahead of a future migration path for existing key-value backed objects.</p>
<p>For more information, refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Objects migrations</a>.</p>
</div></article></div>
