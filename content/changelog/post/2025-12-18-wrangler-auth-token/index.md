<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 18, 2025</time><h2 id="post-title">Retrieve your authentication token with `wrangler auth token`</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now includes a new <a href="/workers/wrangler/commands/general/#auth-token"><code>wrangler auth token</code></a> command that retrieves your current authentication token or credentials for use with other tools and scripts.</p>
<pre><code class="language-sh">wrangler auth token&#10;</code></pre>
<p>The command returns whichever authentication method is currently configured, in priority order: API token from <code>CLOUDFLARE_API_TOKEN</code>, or OAuth token from <code>wrangler login</code> (automatically refreshed if expired).</p>
<p>Use the <code>--json</code> flag to get structured output including the token type:</p>
<pre><code class="language-sh">wrangler auth token --json&#10;</code></pre>
<p>The JSON output includes the authentication type:</p>
<pre><code class="language-jsonc">// API token&#10;{ &quot;type&quot;: &quot;api_token&quot;, &quot;token&quot;: &quot;...&quot; }&#10;&#10;// OAuth token&#10;{ &quot;type&quot;: &quot;oauth&quot;, &quot;token&quot;: &quot;...&quot; }&#10;&#10;// API key/email (only available with --json)&#10;{ &quot;type&quot;: &quot;api_key&quot;, &quot;key&quot;: &quot;...&quot;, &quot;email&quot;: &quot;...&quot; }&#10;</code></pre>
<p>API key/email credentials from <code>CLOUDFLARE_API_KEY</code> and <code>CLOUDFLARE_EMAIL</code> require the <code>--json</code> flag since this method uses two values instead of a single token.</p>
</div></article></div>
