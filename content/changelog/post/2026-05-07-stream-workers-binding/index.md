<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 7, 2026</time><h2 id="post-title">Introducing Stream Bindings for Workers</h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>You can now interact with your Stream video library using new bindings for Workers! This allows customers to upload content to Stream, provision direct uploads, manage videos, and generate signed URLs from a Worker without making authenticated API calls. We're excited to bring Stream and Workers closer together to empower more programmatic pipelines, tighter integrations, and support generative AI and inference workloads.</p>
<p>Use the Stream binding when you want to:</p>
<ul>
<li>Upload videos from URLs or create basic direct upload links for end users</li>
<li>Generate signed playback tokens without managing signing keys</li>
<li>Manage video metadata, captions, downloads, and watermarks</li>
<li>Build video pipelines entirely within Workers</li>
</ul>
<p>To get started, add the Stream binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17756.md")</div>
<p><strong>Generate a video with AI and upload directly to Stream</strong> or send a URL of a file you already have:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17757.md")</div>
<p><strong>Generate a signed URL without using a signing key</strong> or an API call:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17758.md")</div>
<p><strong>Get and set video properties</strong> easily:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17759.md")</div>
<p>For setup instructions and the full API reference, refer to <a href="/stream/manage-video-library/bindings/">Bind to Workers API</a>.</p>
<h4 id="get-started-with-your-agent">Get started with your Agent</h4>
<blockquote>
<p>Add a binding for Cloudflare Stream (env.STREAM). On the watch page, use the
Stream binding to get info based on the ID, and leverage video.meta.name as
the page title.</p>
</blockquote>
</div></article></div>
