<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 14, 2025</time><h2 id="post-title">Introducing Origin Restrictions for Media Transformations</h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>We are adding <a href="/stream/transform-videos/sources/">source origin restrictions</a> to
the Media Transformations beta. This allows customers to restrict what sources
can be used to fetch images and video for transformations. This feature is the
same as --- and uses the same settings as ---
<a href="/images/optimization/transformations/sources/">Image Transformations sources</a>.</p>
<p>When transformations is first enabled, the default setting only allows
transformations on images and media from the same website or domain being used to make
the transformation request. In other words, by default, requests to
<code>example.com/cdn-cgi/media</code> can only reference originals on <code>example.com</code>.</p>
<p><img src="/assets/upstream/images/images/allowed-origins.png" alt="Enable allowed origins from the Cloudflare dashboard" /></p>
<p>Adding access to other sources, or allowing any source,
<a href="/images/optimization/transformations/sources/">is easy to do</a>
in the <strong>Transformations</strong> tab under <strong>Stream</strong>. Click each domain enabled for
Transformations and set its sources list to match the needs of your content. The
user making this change will need permission to edit zone settings.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>
</div></article></div>
