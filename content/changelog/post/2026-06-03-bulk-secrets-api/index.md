<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 3, 2026</time><h2 id="post-title">New Workers bulk secrets API endpoint</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now create, update, or delete multiple secrets for your Worker in a single request using the <a href="/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update/">bulk secrets endpoint</a>.</p>
<ul>
<li>Include a secret with a value to create or update.</li>
<li>Set a secret to <code>null</code> to delete.</li>
<li>Secrets not included in the request are left unchanged.</li>
</ul>
<p>The following example creates <code>API_KEY</code>, updates the already existing <code>DB_PASSWORD</code>, and deletes <code>OLD_SECRET</code>:</p>
<pre><code class="language-json">{&#10;  &quot;secrets&quot;: {&#10;    &quot;API_KEY&quot;: { &quot;type&quot;: &quot;secret_text&quot;, &quot;name&quot;: &quot;API_KEY&quot;, &quot;text&quot;: &quot;my-api-key&quot; },&#10;    &quot;DB_PASSWORD&quot;: { &quot;type&quot;: &quot;secret_text&quot;, &quot;name&quot;: &quot;DB_PASSWORD&quot;, &quot;text&quot;: &quot;my-db-password&quot; },&#10;    &quot;OLD_SECRET&quot;: null&#10;  }&#10;}&#10;</code></pre>
<p>You can do the same from the command line using <a href="/workers/wrangler/commands/workers/#secret-bulk"><code>wrangler secret bulk</code></a>:</p>
<pre><code class="language-sh">npx wrangler secret bulk &lt; secrets.json&#10;</code></pre>
<p>To delete a key, set its value to <code>null</code> in the JSON file. Deletion is not supported with <code>.env</code> files.</p>
<p>Each request supports up to <strong>100 total operations</strong> (creates, updates, and deletes combined).</p>
</div></article></div>
