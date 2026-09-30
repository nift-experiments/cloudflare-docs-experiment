<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 12, 2025</time><h2 id="post-title">Configurable multiplexing HTTP/2 to Origin</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now configure HTTP/2 multiplexing settings for origin connections on Enterprise plans. This feature allows you to optimize how Cloudflare manages concurrent requests over HTTP/2 connections to your origin servers, improving cache efficiency and reducing connection overhead.</p>
<h4 id="how-it-works">How it works</h4>
<p>HTTP/2 multiplexing allows multiple requests to be sent over a single TCP connection. With this configuration option, you can:</p>
<ol>
<li><strong>Control concurrent streams</strong>: Adjust the maximum number of concurrent streams per connection.</li>
<li><strong>Optimize connection reuse</strong>: Fine-tune connection pooling behavior for your origin infrastructure.</li>
<li><strong>Reduce connection overhead</strong>: Minimize the number of TCP connections required between Cloudflare and your origin.</li>
<li><strong>Improve cache performance</strong>: Better connection management can enhance cache fetch efficiency.</li>
</ol>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>Customizable performance</strong>: Tailor multiplexing settings to your origin's capabilities.</li>
<li><strong>Reduced latency</strong>: Fewer connection handshakes improve response times.</li>
<li><strong>Lower origin load</strong>: More efficient connection usage reduces server resource consumption.</li>
<li><strong>Enhanced scalability</strong>: Better connection management supports higher traffic volumes.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>Enterprise customers can configure HTTP/2 multiplexing settings in the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a> or through our <a href="/api/">API</a>.</p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="important-consideration">Important consideration</h4>
@markup("md", "content/.markup/bodies/17703.md")</aside>
</div></article></div>
