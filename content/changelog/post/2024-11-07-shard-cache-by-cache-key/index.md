<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 7, 2024</time><h2 id="post-title">Shard cache using custom cache key values</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Enterprise customers can now optimize cache hit ratios for content that varies by device, language, or referrer by <strong>sharding cache</strong> using up to ten values from previously restricted headers with <a href="/cache/how-to/cache-keys/">custom cache keys</a>.</p>
<h4 id="how-it-works">How it works</h4>
<p>When configuring <a href="/cache/how-to/cache-keys/">custom cache keys</a>, you can now include values from these headers to create distinct cache entries:</p>
<ul>
<li><strong><code>accept*</code> headers</strong> (for example, <code>accept</code>, <code>accept-encoding</code>, <code>accept-language</code>): Serve different cached versions based on content negotiation.</li>
<li><strong><code>referer</code> header</strong>: Cache content differently based on the referring page or site.</li>
<li><strong><code>user-agent</code> header</strong>: Maintain separate caches for different browsers, devices, or bots.</li>
</ul>
<h4 id="when-to-use-cache-sharding">When to use cache sharding</h4>
<ul>
<li>Content varies significantly by device type (mobile vs desktop).</li>
<li>Different language or encoding preferences require distinct responses.</li>
<li>Referrer-specific content optimization is needed.</li>
</ul>
<h4 id="example-configuration">Example configuration</h4>
<pre><code class="language-json">{&#10;  &quot;cache_key&quot;: {&#10;    &quot;custom_key&quot;: {&#10;      &quot;header&quot;: {&#10;        &quot;include&quot;: [&quot;accept-language&quot;, &quot;user-agent&quot;],&#10;        &quot;check_presence&quot;: [&quot;referer&quot;]&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>This configuration creates separate cache entries based on the <code>accept-language</code> and <code>user-agent</code> headers, while also considering whether the <code>referer</code> header is present.</p>
<h4 id="get-started">Get started</h4>
<p>To get started, refer to the <a href="/cache/how-to/cache-keys/">custom cache keys documentation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17702.md")</aside>
</div></article></div>
