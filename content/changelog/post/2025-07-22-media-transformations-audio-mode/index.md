<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 22, 2025</time><h2 id="post-title">Audio mode for Media Transformations</h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>We now support <code>audio</code> mode! Use this feature to extract audio from a source video, outputting
an M4A file to use in downstream workflows like <a href="/workers-ai/">AI inference</a>, content moderation, or transcription.</p>
<p>For example,</p>
<pre><code class="language-text">https://example.com/cdn-cgi/media/&lt;OPTIONS&gt;/&lt;SOURCE-VIDEO&gt;&#10;https://example.com/cdn-cgi/media/mode=audio,time=3s,duration=60s/&lt;input video with diction&gt;&#10;</code></pre>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>
</div></article></div>
