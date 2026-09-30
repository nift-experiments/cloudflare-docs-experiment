<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 1, 2026</time><h2 id="post-title">Images binding is now billed per unique transformation</h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p>The <a href="/images/optimization/binding/">Images binding</a> is now billed per unique transformation, matching the model already used for URL-based transformations. Repeat requests for the same combination of source image and parameters within the same calendar month are counted only once.</p>
<p>Previously, every call to the binding counted as a separate transformation regardless of whether the image or parameters were unique. With this change, you can call the binding on hot paths without paying for each individual request.</p>
<p>Calls to <a href="/images/optimization/binding/#infostream"><code>.info()</code></a> are no longer billed.</p>
<p>For more information, refer to <a href="/images/pricing/#images-transformed">Images pricing</a> and the <a href="/images/optimization/binding/">Images binding documentation</a>.</p>
</div></article></div>
