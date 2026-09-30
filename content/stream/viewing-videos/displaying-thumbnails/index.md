---
cp9:
  canonical: https://developers.cloudflare.com/stream/viewing-videos/displaying-thumbnails/
  description: Generate and customize thumbnail images from Cloudflare Stream videos.
  full_title: Display thumbnails · Cloudflare Stream docs
  head_html: <title>Display thumbnails · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Generate and customize thumbnail images from Cloudflare Stream videos."><link rel="canonical" href="https://developers.cloudflare.com/stream/viewing-videos/displaying-thumbnails/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/viewing-videos/displaying-thumbnails/index.md"><meta property="og:title" content="Display thumbnails · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generate and customize thumbnail images from Cloudflare Stream videos."><meta property="og:url" content="https://developers.cloudflare.com/stream/viewing-videos/displaying-thumbnails/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/viewing-videos/displaying-thumbnails/#page","headline":"Display thumbnails \u00b7 Cloudflare Stream docs","description":"Generate and customize thumbnail images from Cloudflare Stream videos.","url":"https://developers.cloudflare.com/stream/viewing-videos/displaying-thumbnails/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/viewing-videos/displaying-thumbnails/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14368.md")
</aside>
<h2 id="use-case-1-generating-a-thumbnail-on-the-fly">Use Case 1: Generating a thumbnail on-the-fly</h2>
<p>A thumbnail from your video can be generated using a special link where you specify the time from the video you'd like to get the thumbnail from.</p>
<p><code>https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.jpg?time=1s&amp;height=270</code></p>
<img src="https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.jpg?time=1s&height=270" alt="Example of thumbnail image generated from example video" />
<p>Using the <code>poster</code> query parameter in the embed URL, you can set a thumbnail to any time in your video. If <a href="/stream/viewing-videos/securing-your-stream/">signed URLs</a> are required, you must use a signed URL instead of video UIDs.</p>
<pre tabindex="0"><code class="language-html">&lt;iframe&#10;  src=&quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/iframe?poster=https%3A%2F%2Fcustomer-f33zs165nr7gyfy4.cloudflarestream.com%2F6b9e68b07dfee8cc2d116e4c51d6a957%2Fthumbnails%2Fthumbnail.jpg%3Ftime%3D%26height%3D600&quot;&#10;  style=&quot;border: none; position: absolute; top: 0; left: 0; height: 100%; width: 100%;&quot;&#10;  allow=&quot;accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;&quot;&#10;  allowfullscreen=&quot;true&quot;&#10;&gt;&lt;/iframe&gt;&#10;</code></pre>
<p>Supported URL attributes are:</p>
<ul>
<li><strong><code>time</code></strong> (default <code>0s</code>, configurable) time from the video for example <code>8m</code>, <code>5m2s</code></li>
<li><strong><code>height</code></strong> (default <code>640</code>)</li>
<li><strong><code>width</code></strong> (default <code>640</code>)</li>
<li><strong><code>fit</code></strong> (default <code>crop</code>) to clarify what to do when requested height and width does not match the original upload, which should be one of:
<ul>
<li><strong><code>crop</code></strong> cut parts of the video that doesn't fit in the given size</li>
<li><strong><code>clip</code></strong> preserve the entire frame and decrease the size of the image within given size</li>
<li><strong><code>scale</code></strong> distort the image to fit the given size</li>
<li><strong><code>fill</code></strong> preserve the entire frame and fill the rest of the requested size with black background</li>
</ul>
</li>
</ul>
<h2 id="use-case-2-set-the-default-thumbnail-timestamp-using-the-api">Use Case 2: Set the default thumbnail timestamp using the API</h2>
<p>By default, the Stream Player sets the thumbnail to the first frame of the video. You can change this on a per-video basis by setting the &quot;thumbnailTimestampPct&quot; value using the API:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST \&#10;&#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;d &#x27;{&quot;thumbnailTimestampPct&quot;: 0.5}&#x27; \&#10;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream/&lt;VIDEO_UID&gt;&#10;</code></pre>
<p><code>thumbnailTimestampPct</code> is a value between 0.0 (the first frame of the video) and 1.0 (the last frame of the video). For example, you wanted the thumbnail to be the frame at the half way point of your videos, you can set the <code>thumbnailTimestampPct</code> value to 0.5. Using relative values in this way allows you to set the default thumbnail even if you or your users' videos vary in duration.</p>
<h2 id="use-case-3-generating-animated-thumbnails">Use Case 3: Generating animated thumbnails</h2>
<p>Stream supports animated GIFs as thumbnails. Viewing animated thumbnails does not count toward billed minutes delivered or minutes viewed in <a href="/stream/getting-analytics/">Stream Analytics</a>.</p>
<h3 id="animated-gif-thumbnails">Animated GIF thumbnails</h3>
<p><code> https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.gif?time=1s&amp;height=200&amp;duration=4s</code></p>
<img src="https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.gif?time=1s&height=200&duration=4s" alt="Animated gif example, generated on-demand from Cloudflare Stream" />
<p>Supported URL attributes for animated thumbnails are:</p>
<ul>
<li><strong><code>time</code></strong> (default <code>0s</code>) time from the video for example <code>8m</code>, <code>5m2s</code></li>
<li><strong><code>height</code></strong> (default <code>640</code>)</li>
<li><strong><code>width</code></strong> (default <code>640</code>)</li>
<li><strong><code>fit</code></strong> (default <code>crop</code>) to clarify what to do when requested height and width does not match the original upload, which should be one of:
<ul>
<li><strong><code>crop</code></strong> cut parts of the video that doesn't fit in the given size</li>
<li><strong><code>clip</code></strong> preserve the entire frame and decrease the size of the image within given size</li>
<li><strong><code>scale</code></strong> distort the image to fit the given size</li>
<li><strong><code>fill</code></strong> preserve the entire frame and fill the rest of the requested size with black background</li>
</ul>
</li>
<li><strong><code>duration</code></strong> (default <code>5s</code>)</li>
<li><strong><code>fps</code></strong> (default <code>8</code>)</li>
</ul>
