<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 12, 2026</time><h2 id="post-title">Content Type Dimension for AI Bots in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes content type insights for AI bot and crawler traffic. The new <code>content_type</code> dimension and filter shows the distribution of content types returned to AI crawlers, grouped by MIME type category.</p>
<p>The content type dimension and filter are available via the following API endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2/"><code>/ai/bots/summary/content_type</code></a></li>
<li><a href="/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups/"><code>/ai/bots/timeseries_groups/content_type</code></a></li>
</ul>
<p>Content type categories:</p>
<ul>
<li><strong>HTML</strong> - Web pages (<code>text/html</code>)</li>
<li><strong>Images</strong> - All image formats (<code>image/*</code>)</li>
<li><strong>JSON</strong> - JSON data and API responses (<code>application/json</code>, <code>*+json</code>)</li>
<li><strong>JavaScript</strong> - Scripts (<code>application/javascript</code>, <code>text/javascript</code>)</li>
<li><strong>CSS</strong> - Stylesheets (<code>text/css</code>)</li>
<li><strong>Plain Text</strong> - Unformatted text (<code>text/plain</code>)</li>
<li><strong>Fonts</strong> - Web fonts (<code>font/*</code>, <code>application/font-*</code>)</li>
<li><strong>XML</strong> - XML documents and feeds (<code>text/xml</code>, <code>application/xml</code>, <code>application/rss+xml</code>, <code>application/atom+xml</code>)</li>
<li><strong>YAML</strong> - Configuration files (<code>text/yaml</code>, <code>application/yaml</code>)</li>
<li><strong>Video</strong> - Video content and streaming (<code>video/*</code>, <code>application/ogg</code>, <code>*mpegurl</code>)</li>
<li><strong>Audio</strong> - Audio content (<code>audio/*</code>)</li>
<li><strong>Markdown</strong> - Markdown documents (<code>text/markdown</code>)</li>
<li><strong>Documents</strong> - PDFs, Office documents, ePub, CSV (<code>application/pdf</code>, <code>application/msword</code>, <code>text/csv</code>)</li>
<li><strong>Binary</strong> - Executables, archives, WebAssembly (<code>application/octet-stream</code>, <code>application/zip</code>, <code>application/wasm</code>)</li>
<li><strong>Serialization</strong> - Binary API formats (<code>application/protobuf</code>, <code>application/grpc</code>, <code>application/msgpack</code>)</li>
<li><strong>Other</strong> - All other content types</li>
</ul>
<p>Additionally, individual <a href="https://radar.cloudflare.com/bots/directory/gptbot">bot information pages</a> now display content type distribution for AI crawlers that exist in both the Verified Bots and AI Bots datasets.</p>
<p><img src="/assets/upstream/images/radar/ai-bots-content-type.png" alt="Screenshot of the Content Type Distribution chart on the AI Insights page" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/ai-insights#content-type">AI Insights page</a> to explore the data.</p>
</div></article></div>
