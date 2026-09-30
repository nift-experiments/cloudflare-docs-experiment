<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 26, 2026</time><h2 id="post-title">Markdown responses for Cloudflare 1xxx errors</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare now returns structured Markdown responses for Cloudflare-generated 1xxx errors when clients send <code>Accept: text/markdown</code>.</p>
<p>Each response includes YAML frontmatter plus guidance sections (<code>What happened</code> / <code>What you should do</code>) so agents can make deterministic retry and escalation decisions without parsing HTML.</p>
<p>In measured 1,015 comparisons, Markdown reduced payload size and token footprint by over 98% versus HTML.</p>
<p>Included frontmatter fields:</p>
<ul>
<li><code>error_code</code>, <code>error_name</code>, <code>error_category</code>, <code>http_status</code></li>
<li><code>ray_id</code>, <code>timestamp</code>, <code>zone</code></li>
<li><code>cloudflare_error</code>, <code>retryable</code>, <code>retry_after</code> (when applicable), <code>owner_action_required</code></li>
</ul>
<p>Default behavior is unchanged: clients that do not explicitly request Markdown continue to receive HTML error pages.</p>
<h4 id="negotiation-behavior">Negotiation behavior</h4>
<p>Cloudflare uses standard HTTP content negotiation on the <code>Accept</code> header.</p>
<ul>
<li><code>Accept: text/markdown</code> -&gt; Markdown</li>
<li><code>Accept: text/markdown, text/html;q=0.9</code> -&gt; Markdown</li>
<li><code>Accept: text/*</code> -&gt; Markdown</li>
<li><code>Accept: */*</code> -&gt; HTML (default browser behavior)</li>
</ul>
<p>When multiple values are present, Cloudflare selects the highest-priority supported media type using <code>q</code> values. If Markdown is not explicitly preferred, HTML is returned.</p>
<h4 id="availability">Availability</h4>
<p>Available now for Cloudflare-generated 1xxx errors.</p>
<h4 id="get-started">Get started</h4>
<pre><code class="language-bash">curl -H &quot;Accept: text/markdown&quot; https://&lt;your-domain&gt;/cdn-cgi/error/1015&#10;</code></pre>
<p>Reference: <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></p>
</div></article></div>
