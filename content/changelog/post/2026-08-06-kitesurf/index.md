<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 6, 2026</time><h2 id="post-title">Introducing Kitesurf, an agent-first browser on Browser Run</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/kitesurf/">Kitesurf</a> is Cloudflare's new stateless, highly scalable browser that runs entirely on top of <a href="/workers/">Workers</a> and is designed for AI agents. It is available for free while in beta.</p>
<p>Compared to Chromium, Kitesurf uses 3–7× less CPU and memory for common agentic tasks like screenshots and HTML extraction, so you can run more sessions and scale better for bursty, AI-driven workloads.</p>
<p>Your existing clients already work. To opt in, add the <code>browser=kitesurf</code> parameter to any Browser Run <a href="/browser-run/cdp/">CDP</a> or <a href="/browser-run/quick-actions/">Quick Action</a> endpoint:</p>
<pre><code class="language-sh">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-run/screenshot?browser=kitesurf&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.png&quot;&#10;</code></pre>
<p>You can also explore Kitesurf without writing any code in the <a href="https://kitesurf.cloudflare.app/">public playground</a>.</p>
<p>For more information, refer to the <a href="/browser-run/kitesurf/">Kitesurf documentation</a> and the <a href="https://blog.cloudflare.com/kitesurf">blog announcement</a>.</p>
</div></article></div>
