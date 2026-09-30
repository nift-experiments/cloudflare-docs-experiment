<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 7, 2025</time><h2 id="post-title">Inspect Cache Keys with Cloudflare Trace</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now see the exact cache key generated for any request directly in Cloudflare Trace. This visibility helps you troubleshoot cache hits and misses, and verify that your Custom Cache Keys — configured via Cache Rules or Page Rules — are working as intended.</p>
<p>Previously, diagnosing caching behavior required inferring the key from configuration settings. Now, you can confirm that your custom logic for headers, query strings, and device types is correctly applied.</p>
<p>Access Trace via the <a href="/rules/trace-request/how-to/#use-trace-in-the-dashboard">dashboard</a> or <a href="/api/resources/request_tracer/methods/trace/">API</a>, either manually for ad-hoc debugging or automated as part of your quality-of-service monitoring.</p>
<h4 id="example-scenario">Example scenario</h4>
<p>If you have a Cache Rule that segments content based on a specific cookie (for example, <code>user_region</code>), run a Trace with that cookie present to confirm the <code>user_region</code> value appears in the resulting cache key.</p>
<p>The Trace response includes the cache key in the <code>cache</code> object:</p>
<pre><code class="language-json">{&#10;  &quot;step_name&quot;: &quot;request&quot;,&#10;  &quot;type&quot;: &quot;cache&quot;,&#10;  &quot;matched&quot;: true,&#10;  &quot;public_name&quot;: &quot;Cache Parameters&quot;,&#10;  &quot;cache&quot;: {&#10;    &quot;key&quot;: {&#10;      &quot;zone_id&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;      &quot;scheme&quot;: &quot;https&quot;,&#10;      &quot;host&quot;: &quot;example.com&quot;,&#10;      &quot;uri&quot;: &quot;/images/hero.jpg&quot;&#10;    },&#10;    &quot;key_string&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353::::https://example.com/images/hero.jpg:::::&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="get-started">Get started</h4>
<p>To learn more, refer to the <a href="/rules/trace-request/">Trace documentation</a> and our guide on <a href="/cache/how-to/cache-keys/">Custom Cache Keys</a>.</p>
</div></article></div>
