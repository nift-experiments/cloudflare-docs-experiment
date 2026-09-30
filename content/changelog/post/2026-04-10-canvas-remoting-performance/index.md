<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 10, 2026</time><h2 id="post-title">Canvas Remoting optimizes performance for productivity applications</h2>
<div class="changelog-badges"><span>browser-isolation</span></div><div class="changelog-body"><p>Remote Browser Isolation now supports <strong>Canvas Remoting</strong>, improving performance for HTML5 Canvas applications by sending vector draw commands instead of rasterized bitmaps.</p>
<h4 id="key-improvements">Key improvements</h4>
<ul>
<li><strong>10x bandwidth reduction:</strong> Microsoft Word and other Office apps use 90% less bandwidth</li>
<li><strong>Smooth performance:</strong> Google Sheets maintains consistent 30fps rendering</li>
<li><strong>Responsive terminals:</strong> Web-based development environments and AI notebooks work in real-time</li>
<li><strong>Zero configuration:</strong> Enabled by default for all Browser Isolation customers</li>
</ul>
<h4 id="how-it-works">How it works</h4>
<p>Instead of sending rasterized bitmaps for every Canvas update, Browser Isolation now:</p>
<ol>
<li>Captures Canvas draw commands at the source</li>
<li>Converts them to lightweight vector instructions</li>
<li>Renders Canvas content on the client</li>
</ol>
<p>This reduces bandwidth from hundreds of kilobytes per second to tens of kilobytes per second.</p>
<h4 id="managing-canvas-remoting">Managing Canvas Remoting</h4>
<p>To temporarily disable for troubleshooting:</p>
<ul>
<li>Right-click the isolated webpage background</li>
<li>Select <strong>Disable Canvas Remoting</strong></li>
<li>Re-enable the same way by selecting <strong>Enable Canvas Remoting</strong></li>
</ul>
<h4 id="limitations">Limitations</h4>
<p>Currently supports 2D Canvas contexts only. WebGL and 3D graphics applications continue using bitmap rendering. For more information, refer to <a href="/cloudflare-one/remote-browser-isolation/canvas-remoting/">Canvas Remoting</a>.</p>
</div></article></div>
