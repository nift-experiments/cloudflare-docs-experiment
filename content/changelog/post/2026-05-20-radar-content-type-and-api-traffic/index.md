<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 20, 2026</time><h2 id="post-title">Content type distribution and API traffic share on Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes two new charts on the <a href="https://radar.cloudflare.com/traffic">traffic page</a> that provide deeper insights into the composition of HTTP traffic: a content type distribution chart and an API traffic share chart.</p>
<h4 id="content-type-distribution">Content type distribution</h4>
<p>The new <a href="https://radar.cloudflare.com/traffic#content-type"><strong>Content type</strong></a> chart displays the distribution of HTTP response content types, grouped into high-level categories. A traffic type selector allows filtering by human, bot, or all traffic. The existing <a href="https://radar.cloudflare.com/traffic#bot-vs-human"><strong>Bot vs. Human</strong></a> chart also gained a content type category filter, allowing users to see the bot/human split for specific content categories.</p>
<p><img src="/assets/upstream/images/radar/content-type-distribution.png" alt="Screenshot of the content type distribution chart on the Radar traffic page" /></p>
<p>Content type categories:</p>
<ul>
<li><strong>HTML</strong> — Web pages (<code>text/html</code>)</li>
<li><strong>Images</strong> — All image formats (<code>image/*</code>)</li>
<li><strong>JSON</strong> — JSON data and API responses (<code>application/json</code>, <code>*+json</code>)</li>
<li><strong>JavaScript</strong> — Scripts (<code>application/javascript</code>, <code>text/javascript</code>)</li>
<li><strong>CSS</strong> — Stylesheets (<code>text/css</code>)</li>
<li><strong>Plain Text</strong> — Unformatted text (<code>text/plain</code>)</li>
<li><strong>Fonts</strong> — Web fonts (<code>font/*</code>, <code>application/font-*</code>)</li>
<li><strong>XML</strong> — XML documents and feeds (<code>text/xml</code>, <code>application/xml</code>, <code>application/rss+xml</code>, <code>application/atom+xml</code>)</li>
<li><strong>YAML</strong> — Configuration files (<code>text/yaml</code>, <code>application/yaml</code>)</li>
<li><strong>Video</strong> — Video content and streaming (<code>video/*</code>, <code>application/ogg</code>, <code>*mpegurl</code>)</li>
<li><strong>Audio</strong> — Audio content (<code>audio/*</code>)</li>
<li><strong>Markdown</strong> — Markdown documents (<code>text/markdown</code>)</li>
<li><strong>Documents</strong> — PDFs, Office documents, ePub, CSV (<code>application/pdf</code>, <code>application/msword</code>, <code>text/csv</code>)</li>
<li><strong>Binary</strong> — Executables, archives, WebAssembly (<code>application/octet-stream</code>, <code>application/zip</code>, <code>application/wasm</code>)</li>
<li><strong>Serialization</strong> — Binary API formats (<code>application/protobuf</code>, <code>application/grpc</code>, <code>application/msgpack</code>)</li>
<li><strong>Other</strong> — All other content types</li>
</ul>
<p>The <code>CONTENT_TYPE</code> dimension and <code>contentType</code> filter are available on the HTTP <a href="/api/resources/radar/subresources/http/methods/summary_v2/">summary</a>, <a href="/api/resources/radar/subresources/http/methods/timeseries_groups_v2/">timeseries groups</a>, and <a href="/api/resources/radar/subresources/http/methods/timeseries/">timeseries</a> endpoints.</p>
<h4 id="api-traffic-share">API traffic share</h4>
<p>The new <a href="https://radar.cloudflare.com/traffic#api-traffic"><strong>API traffic</strong></a> chart shows the percentage of dynamic (non-cacheable) HTTP request traffic that is API-related. API traffic is identified by JSON or XML response content types (<code>application/json</code>, <code>application/xml</code>, <code>text/xml</code>) on HTTP requests that returned a 200 status code. A traffic type selector allows switching between human traffic, bot traffic, or all traffic.</p>
<p><img src="/assets/upstream/images/radar/api-traffic-share.png" alt="Screenshot of the API traffic share chart on the Radar traffic page" /></p>
<p>The <code>API_TRAFFIC</code> dimension is available on the existing HTTP <a href="/api/resources/radar/subresources/http/methods/summary_v2/">summary</a> and <a href="/api/resources/radar/subresources/http/methods/timeseries_groups_v2/">timeseries groups</a> endpoints. An <code>apiTraffic</code> filter (<code>API</code> or <code>NON_API</code>) can also be applied to <a href="/api/resources/radar/subresources/http/methods/timeseries/">HTTP timeseries</a> requests to retrieve raw request counts for API-only or non-API traffic.</p>
<p>Visit the <a href="https://radar.cloudflare.com/traffic">Radar traffic page</a> to explore these new charts.</p>
</div></article></div>
