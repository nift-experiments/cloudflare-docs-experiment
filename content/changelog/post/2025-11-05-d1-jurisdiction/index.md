<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 5, 2025</time><h2 id="post-title">D1 can restrict data localization with jurisdictions</h2>
<div class="changelog-badges"><span>d1</span><span>workers</span></div><div class="changelog-body"><p>You can now set a <a href="/d1/configuration/data-location/">jurisdiction</a> when creating a D1 database to guarantee where your database runs and stores data. Jurisdictions can help you comply with data localization regulations such as GDPR. Supported jurisdictions include <code>eu</code> and <code>fedramp</code>.</p>
<p>A jurisdiction can only be set at database creation time via wrangler, REST API or the UI and cannot be added/updated after the database already exists.</p>
<pre><code class="language-sh">npx wrangler@latest d1 create db-with-jurisdiction --jurisdiction eu&#10;</code></pre>
<pre><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/d1/database&quot; \&#10;     &#45;H &quot;Authorization: Bearer $TOKEN&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot; \&#10;     &#45;-data &#x27;{&quot;name&quot;: &quot;db-with-jurisdiction&quot;, &quot;jurisdiction&quot;: &quot;eu&quot; }&#x27;&#10;</code></pre>
<p>To learn more, visit D1's data location <a href="/d1/configuration/data-location/">documentation</a>.</p>
</div></article></div>
