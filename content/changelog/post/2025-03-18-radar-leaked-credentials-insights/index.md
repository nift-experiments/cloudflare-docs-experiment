<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 18, 2025</time><h2 id="post-title">Leaked Credentials Insights in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has expanded its security insights, providing visibility into aggregate trends in authentication requests,
including the detection of leaked credentials through <a href="/waf/detections/leaked-credentials/">leaked credentials detection</a> scans.</p>
<p>We have now introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/leaked_credentials/subresources/summary/"><code>/leaked_credential_checks/summary/{dimension}</code></a>: Retrieves summaries of HTTP authentication requests distribution across two different dimensions.</li>
<li><a href="/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/"><code>/leaked_credential_checks/timeseries_groups/{dimension}</code></a>: Retrieves timeseries data for HTTP authentication requests distribution across two different dimensions.</li>
</ul>
<p>The following dimensions are available, displaying the distribution of HTTP authentication requests based on:</p>
<ul>
<li><code>compromised</code>: Credential status (clean vs. compromised).</li>
<li><code>bot_class</code>: <a href="/radar/concepts/bot-classes">Bot class</a> (human vs. bot).</li>
</ul>
<p>Dive deeper into leaked credential detection in this <a href="https://blog.cloudflare.com/password-reuse-rampant-half-user-logins-compromised/">blog post</a> and learn more about the expanded Radar security insights in our <a href="https://blog.cloudflare.com/cloudflare-radar-ddos-leaked-credentials-bots">blog post</a>.</p>
</div></article></div>
