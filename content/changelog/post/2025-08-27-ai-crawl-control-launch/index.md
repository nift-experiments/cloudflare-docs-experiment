<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 27, 2025</time><h2 id="post-title">Enhanced crawler insights and custom 402 responses</h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>We improved AI crawler management with detailed analytics and introduced custom HTTP 402 responses for blocked crawlers. AI Audit has been renamed to AI Crawl Control and is now generally available.</p>
<p><strong>Enhanced Crawlers tab:</strong></p>
<ul>
<li>View total allowed and blocked requests for each AI crawler</li>
<li>Trend charts show crawler activity over your selected time range per crawler</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-table.png" alt="Updated AI Crawl Control table showing request counts and trend charts" /></p>
<p><strong>Custom block responses (paid plans):</strong>
You can now return HTTP 402 &quot;Payment Required&quot; responses when blocking AI crawlers, enabling direct communication with crawler operators about licensing terms.</p>
<p>For users on paid plans, when blocking AI crawlers you can configure:</p>
<ul>
<li><strong>Response code:</strong> Choose between 403 Forbidden or 402 Payment Required</li>
<li><strong>Response body:</strong> Add a custom message with your licensing contact information</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-block-response.png" alt="AI Crawl Control block response configuration interface" /></p>
<p>Example 402 response:</p>
<pre><code class="language-http">HTTP 402 Payment Required&#10;Date: Mon, 24 Aug 2025 12:56:49 GMT&#10;Content-type: application/json&#10;Server: cloudflare&#10;Cf-Ray: 967e8da599d0c3fa-EWR&#10;Cf-Team: 2902f6db750000c3fa1e2ef400000001&#10;&#10;{&#10;  &quot;message&quot;: &quot;Please contact the site owner for access.&quot;&#10;}&#10;</code></pre>
</div></article></div>
