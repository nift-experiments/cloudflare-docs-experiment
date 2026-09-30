<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 24, 2026</time><h2 id="post-title">Stream live inputs can now be disabled and enabled</h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>You can now disable a live input to reject incoming RTMPS and SRT
connections. When a live input is disabled, any broadcast attempts will fail to
connect.</p>
<p>This gives you more control over your live inputs:</p>
<ul>
<li>Temporarily pause an input without deleting it</li>
<li>Programmatically end creator broadcasts</li>
<li>Prevent new broadcasts from starting on a specific input</li>
</ul>
<p>To disable a live input via the API, set the <code>enabled</code> property to <code>false</code>:</p>
<pre><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;enabled&quot;: false}&#x27;&#10;</code></pre>
<p>You can also disable or enable a live input from the <strong>Live inputs</strong> list page
or the live input detail page in the Dashboard.</p>
<p>All existing live inputs remain enabled by default. For more information, refer
to <a href="/stream/stream-live/start-stream-live/">Start a live stream</a>.</p>
</div></article></div>
