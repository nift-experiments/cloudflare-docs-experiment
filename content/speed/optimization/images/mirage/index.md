<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/13925.md")
</aside>
<h2 id="what-was-mirage">What was Mirage?</h2>
<p>Cloudflare Mirage was a mobile image optimization feature that reduced bandwidth usage and accelerated image loading on slow mobile connections and HTTP/1.</p>
<p>Mirage worked by:</p>
<ul>
<li>Replacing images with low-resolution thumbnails bundled together into one file.</li>
<li>Acting as a lazy loader, deferring loading of higher-resolution images until they become visible.</li>
</ul>
<h2 id="why-was-it-deprecated">Why was it deprecated?</h2>
<p>Modern web standards and browser capabilities have evolved to provide native support for many of Mirage's features:</p>
<ul>
<li>Native lazy loading with the <code>loading=&quot;lazy&quot;</code> HTML attribute.</li>
<li>Responsive images using <code>srcset</code> and <code>&lt;picture&gt;</code> elements.</li>
<li>HTTP/2 and HTTP/3 providing better performance.</li>
<li>Improved mobile networks reducing the need for aggressive optimization.</li>
</ul>
<h2 id="migration-path">Migration path</h2>
<p>Instead of Mirage, use:</p>
<ul>
<li><strong><a href="/images/polish/">Polish</a></strong> - Seamlessly optimizes images for all browsers, not only mobile, and keeps images at full resolution.</li>
<li><strong><a href="/images/optimization/transformations/overview/">Image Resizing</a></strong> - Combined with <code>loading=&quot;lazy&quot;</code> and <code>srcset</code> HTML attributes, provides modern responsive image delivery.</li>
<li><strong><a href="/images/tutorials/optimize-mobile-viewing/">Lazy loading guide</a></strong> - Learn how to implement native lazy loading.</li>
<li><strong><a href="/images/optimization/make-responsive-images/">Responsive images guide</a></strong> - Create images that adapt to different devices.</li>
</ul>
