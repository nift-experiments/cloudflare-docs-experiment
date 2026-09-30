<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 31, 2025</time><h2 id="post-title">Workers for Platforms now supports Static Assets</h2>
<div class="changelog-badges"><span>workers-for-platforms</span></div><div class="changelog-body"><p>Workers for Platforms customers can now attach static assets (HTML, CSS, JavaScript, images) directly to User Workers, removing the need to host separate infrastructure to serve the assets.</p>
<p>This allows your platform to serve entire front-end applications from Cloudflare's global edge, utilizing caching for fast load times, while supporting dynamic logic within the same Worker. Cloudflare automatically scales its infrastructure to handle high traffic volumes, enabling you to focus on building features without managing servers.</p>
<h4 id="what-you-can-build">What you can build</h4>
<p><strong>Static Sites:</strong> Host and serve HTML, CSS, JavaScript, and media files directly from Cloudflare's network, ensuring fast loading times worldwide. This is ideal for blogs, landing pages, and documentation sites because static assets can be efficiently cached and delivered closer to the user, reducing latency and enhancing the overall user experience.</p>
<p><strong>Full-Stack Applications:</strong> Combine asset hosting with Cloudflare Workers to power dynamic, interactive applications. If you're an e-commerce platform, you can serve your customers' product pages and run inventory checks from within the same Worker.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17821.md")</div>
<p><strong>Get Started:</strong>
Upload static assets using the Workers for Platforms API or Wrangler. For more information, visit our <a href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/">Workers for Platforms documentation.</a></p>
</div></article></div>
