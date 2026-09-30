<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 24, 2026</time><h2 id="post-title">deleteAll() now deletes Durable Object alarm</h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p><code>deleteAll()</code> now deletes a Durable Object alarm in addition to stored data for Workers with a compatibility date of <code>2026-02-24</code> or later. This change simplifies clearing a Durable Object's storage with a single API call.</p>
<p>Previously, <code>deleteAll()</code> only deleted user-stored data for an object. Alarm usage stores metadata in an object's storage, which required a separate <code>deleteAlarm()</code> call to fully clean up all storage for an object. The <code>deleteAll()</code> change applies to both KV-backed and SQLite-backed Durable Objects.</p>
<pre><code class="language-js">// Before: two API calls required to clear all storage&#10;await this.ctx.storage.deleteAlarm();&#10;await this.ctx.storage.deleteAll();&#10;&#10;// Now: a single call clears both data and the alarm&#10;await this.ctx.storage.deleteAll();&#10;</code></pre>
<p>For more information, refer to the <a href="/durable-objects/api/sqlite-storage-api/#deleteall">Storage API documentation</a>.</p>
</div></article></div>
