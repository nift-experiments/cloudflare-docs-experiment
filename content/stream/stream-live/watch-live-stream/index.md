---
cp9:
  canonical: https://developers.cloudflare.com/stream/stream-live/watch-live-stream/
  description: Play Cloudflare Stream live video using the Stream Player or custom HLS and DASH players.
  full_title: Watch a live stream · Cloudflare Stream docs
  head_html: <title>Watch a live stream · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Play Cloudflare Stream live video using the Stream Player or custom HLS and DASH players."><link rel="canonical" href="https://developers.cloudflare.com/stream/stream-live/watch-live-stream/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/stream-live/watch-live-stream/index.md"><meta property="og:title" content="Watch a live stream · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Play Cloudflare Stream live video using the Stream Player or custom HLS and DASH players."><meta property="og:url" content="https://developers.cloudflare.com/stream/stream-live/watch-live-stream/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/stream-live/watch-live-stream/#page","headline":"Watch a live stream \u00b7 Cloudflare Stream docs","description":"Play Cloudflare Stream live video using the Stream Player or custom HLS and DASH players.","url":"https://developers.cloudflare.com/stream/stream-live/watch-live-stream/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/stream-live/watch-live-stream/
  schema: 1
---
<p>When a <a href="/stream/stream-live/start-stream-live/">Live Input</a> begins receiving a
broadcast, a new video is automatically created if the input's <code>mode</code> property
is set to <code>automatic</code>.</p>
<p>To watch, Stream offers a built-in Player or you use a custom player with the
HLS and DASH manifests.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14398.md")
</aside>
<h2 id="view-by-live-input-id-or-video-id">View by Live Input ID or Video ID</h2>
<p>Whether you use the Stream Player or a custom player with a manifest, you can
reference the Live Input ID or a specific Video ID. The main difference is what
happens when a broadcast concludes.</p>
<p>Use a Live Input ID in instances where a player should always show the active
broadcast, if there is one, or a &quot;Stream has not started&quot; message if the input
is idle. This option is best for cases where a page is dedicated to a creator, channel, or
recurring program. The Live Input ID is provisioned for you when you create the
input; it will not change.</p>
<p>Use a Video ID in instances where a player should be used to display a single
broadcast or its recording once the broadcast has concluded. This option is best for cases where
a page is dedicated to a one-time event, specific episode/occurrence, or date.
There is a <em>new</em> Video ID generated for each broadcast <em>when it starts.</em></p>
<p>Using DVR mode, explained below, there are additional considerations.</p>
<p>Stream's URLs are all templatized for easy generation:</p>
<p><strong>Stream built-in Player URL format:</strong></p>
<pre tabindex="0"><code>https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;INPUT_ID|VIDEO_ID&gt;/iframe&#10;</code></pre>
<p>A full embed code can be generated in Dash or with the API.</p>
<p><strong>HLS Manifest URL format:</strong></p>
<pre tabindex="0"><code>https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;INPUT_ID|VIDEO_ID&gt;/manifest/video.m3u8&#10;</code></pre>
<p>You can also retrieve the embed code or manifest URLs from Dash or the API.</p>
<h2 id="use-the-dashboard">Use the dashboard</h2>
<p>To get the Stream built-in player embed code or HLS Manifest URL for a custom player:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Live inputs</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select a live input from the list.</li>
<li>Locate the <strong>Embed</strong> and <strong>HLS Manifest URL</strong> beneath the video.</li>
<li>Determine which option to use and then select <strong>Click to copy</strong> beneath your choice.</li>
</ol>
<p>The embed code or manifest URL retrieved in Dash will reference the Live Input ID.</p>
<h2 id="use-the-api">Use the API</h2>
<p>To retrieve the player code or manifest URLs via the API, fetch the Live Input's
list of videos:</p>
<pre tabindex="0"><code class="language-bash">curl -X GET \&#10;&#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream/live_inputs/&lt;LIVE_INPUT_UID&gt;/videos&#10;</code></pre>
<p>A live input will have multiple videos associated with it, one for each broadcast.
If there is an active broadcast, the first video in the response will have a
<code>live-inprogress</code> status. Other videos in the response represent recordings
which can be played on-demand.</p>
<p>Each video in the response, including the active broadcast if there is one,
contains the HLS and DASH URLs and a link to the Stream player. Noteworthy
properties include:</p>
<ul>
<li><code>preview</code> -- Link to the Stream player to watch</li>
<li><code>playback</code>.<code>hls</code> -- HLS Manifest</li>
<li><code>playback</code>.<code>dash</code> -- DASH Manifest</li>
</ul>
<p>In the example below, the state of the live video is <code>live-inprogress</code> and the
state for previously recorded video is <code>ready</code>.</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;uid&quot;: &quot;6b9e68b07dfee8cc2d116e4c51d6a957&quot;,&#10;      &quot;thumbnail&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.jpg&quot;,&#10;&#10;      &quot;status&quot;: {&#10;        &quot;state&quot;: &quot;live-inprogress&quot;,&#10;        &quot;errorReasonCode&quot;: &quot;&quot;,&#10;        &quot;errorReasonText&quot;: &quot;&quot;&#10;      },&#10;      &quot;meta&quot;: {&#10;        &quot;name&quot;: &quot;Stream Live Test 23 Sep 21 05:44 UTC&quot;&#10;      },&#10;      &quot;created&quot;: &quot;2021-09-23T05:44:30.453838Z&quot;,&#10;      &quot;modified&quot;: &quot;2021-09-23T05:44:30.453838Z&quot;,&#10;      &quot;size&quot;: 0,&#10;      &quot;preview&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/watch&quot;,&#10;      ...&#10;&#10;      &quot;playback&quot;: {&#10;        &quot;hls&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.m3u8&quot;,&#10;        &quot;dash&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.mpd&quot;&#10;      },&#10;      ...&#10;    },&#10;    {&#10;      &quot;uid&quot;: &quot;6b9e68b07dfee8cc2d116e4c51d6a957&quot;,&#10;      &quot;thumbnail&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.jpg&quot;,&#10;      &quot;thumbnailTimestampPct&quot;: 0,&#10;      &quot;readyToStream&quot;: true,&#10;      &quot;status&quot;: {&#10;        &quot;state&quot;: &quot;ready&quot;,&#10;        &quot;pctComplete&quot;: &quot;100.000000&quot;,&#10;        &quot;errorReasonCode&quot;: &quot;&quot;,&#10;        &quot;errorReasonText&quot;: &quot;&quot;&#10;      },&#10;      &quot;meta&quot;: {&#10;        &quot;name&quot;: &quot;CFTV Staging 22 Sep 21 22:12 UTC&quot;&#10;      },&#10;      &quot;created&quot;: &quot;2021-09-22T22:12:53.587306Z&quot;,&#10;      &quot;modified&quot;: &quot;2021-09-23T00:14:05.591333Z&quot;,&#10;      &quot;size&quot;: 0,&#10;      &quot;preview&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/watch&quot;,&#10;      ...&#10;      &quot;playback&quot;: {&#10;        &quot;hls&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.m3u8&quot;,&#10;        &quot;dash&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.mpd&quot;&#10;      },&#10;    }&#10;  ],&#10;}&#10;</code></pre>
<p>These will reference the Video ID.</p>
<h2 id="live-input-status">Live input status</h2>
<p>You can check whether a live input is currently streaming and what its active
video ID is by making a request to its <code>lifecycle</code> endpoint. The Stream player
does this automatically to show a note when the input is idle. Custom players
may require additional support.</p>
<pre tabindex="0"><code class="language-bash">curl -X GET \&#10;&#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;INPUT_ID&gt;/lifecycle&#10;</code></pre>
<p>In the example below, the response indicates the <code>ID</code> is for an input with an active <code>videoUID</code>. The <code>live</code> status value indicates the input is actively streaming.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;isInput&quot;: true,&#10;	&quot;videoUID&quot;: &quot;55b9b5ce48c3968c6b514c458959d6a&quot;,&#10;	&quot;live&quot;: true&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;isInput&quot;: true,&#10;	&quot;videoUID&quot;: null,&#10;	&quot;live&quot;: false&#10;}&#10;</code></pre>
<p>When viewing a live stream via the live input ID, the <code>requireSignedURLs</code> and <code>allowedOrigins</code> options in the live input recording settings are used. These settings are independent of the video-level settings.</p>
<h2 id="live-stream-recording-playback">Live stream recording playback</h2>
<p>After a live stream ends, a recording is automatically generated and available within 60 seconds. To ensure successful video viewing and playback, keep the following in mind:</p>
<ul>
<li>If a live stream ends while a viewer is watching, viewers using the Stream player should wait 60 seconds and then reload the player to view the recording of the live stream.</li>
<li>After a live stream ends, you can check the status of the recording via the API. When the video state is <code>ready</code>, you can use one of the manifest URLs to stream the recording.</li>
</ul>
<p>While the recording of the live stream is generating, the video may report as <code>not-found</code> or <code>not-started</code>.</p>
<p>If you are not using the Stream player for live stream recordings, refer to <a href="/stream/stream-live/replay-recordings/">Record and replay live streams</a> for more information on how to replay a live stream recording.</p>
