<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 6, 2025</time><h2 id="post-title">Introducing Media Transformations from Cloudflare Stream</h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>Today, we are thrilled to announce Media Transformations, a new service that
brings the magic of <a href="/images/optimization/transformations/overview/">Image Transformations</a> to
<em>short-form video files,</em> wherever they are stored!</p>
<p>For customers with a huge volume of short video — generative AI output,
e-commerce product videos, social media clips, or short marketing content —
uploading those assets to Stream is not always practical. Sometimes, the
greatest friction to getting started was the thought of all that migrating.
Customers want a simpler solution that retains their current storage strategy to
deliver small, optimized MP4 files. Now you can do that with Media
Transformations.</p>
<p>To transform a video or image,
<a href="/stream/transform-videos/#getting-started">enable transformations</a> for your
zone, then make a simple request with a specially formatted URL. The result is
an MP4 that can be used in an HTML video element without a player library.
If your zone already has Image Transformations enabled, then it is ready to
optimize videos with Media Transformations, too.</p>
<pre><code class="language-text">https://example.com/cdn-cgi/media/&lt;OPTIONS&gt;/&lt;SOURCE-VIDEO&gt;&#10;</code></pre>
<p>For example, we have a short video of the mobile in Austin's office. The
original is nearly 30 megabytes and wider than necessary for this layout.
Consider a simple width adjustment:</p>
<video controls>
	<source src="https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4" />
</video>
<pre><code class="language-text">https://example.com/cdn-cgi/media/width=640/&lt;SOURCE-VIDEO&gt;&#10;https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4&#10;</code></pre>
<p>The result is less than 3 megabytes, properly sized, and delivered dynamically
so that customers do not have to manage the creation and storage of these
transformed assets.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>
</div></article></div>
