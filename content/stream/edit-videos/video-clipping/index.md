---
cp9:
  canonical: https://developers.cloudflare.com/stream/edit-videos/video-clipping/
  description: Trim Cloudflare Stream videos by setting start and end times to create new clips via the API.
  full_title: Clip videos · Cloudflare Stream docs
  head_html: <title>Clip videos · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Trim Cloudflare Stream videos by setting start and end times to create new clips via the API."><link rel="canonical" href="https://developers.cloudflare.com/stream/edit-videos/video-clipping/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/edit-videos/video-clipping/index.md"><meta property="og:title" content="Clip videos · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Trim Cloudflare Stream videos by setting start and end times to create new clips via the API."><meta property="og:url" content="https://developers.cloudflare.com/stream/edit-videos/video-clipping/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/edit-videos/video-clipping/#page","headline":"Clip videos \u00b7 Cloudflare Stream docs","description":"Trim Cloudflare Stream videos by setting start and end times to create new clips via the API.","url":"https://developers.cloudflare.com/stream/edit-videos/video-clipping/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/edit-videos/video-clipping/
  schema: 1
---
<p>With video clipping, also referred to as &quot;trimming&quot; or changing the length of the video, you can change the start and end points of a video so viewers only see a specific &quot;clip&quot; of the video. For example, if you have a 20 minute video but only want to share a five minute clip from the middle of the video, you can clip the video to remove the content before and after the five minute clip.</p>
<p>Refer to the <a href="/api/resources/stream/subresources/clip/methods/create/">Video clipping API documentation</a> for more information.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note:</h3>
@markup("md", "content/.markup/bodies/14469.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you can clip a video, you will need an API token. For more information on creating an API token, refer to <a href="/fundamentals/api/get-started/create-token/">Creating API tokens</a>.</p>
<h2 id="required-parameters">Required parameters</h2>
<p>To clip your video, determine the start and end times you want to use from the existing video to create the new video. Use the <code>videoUID</code> and the start end times to make your request.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14468.md")
</aside>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;clippedFromVideoUID&quot;: &quot;0ea62994907491cf9ebefb0a34c1e2c6&quot;,&#10;	&quot;startTimeSeconds&quot;: 20,&#10;	&quot;endTimeSeconds&quot;: 40&#10;}&#10;</code></pre>
<ul>
<li><strong><code>clippedFromVideoUID</code></strong>: The unique identifier for the video used to create the new, clipped video.</li>
<li><strong><code>startTimeSeconds</code></strong>: The timestamp from the existing video that indicates when the new video begins.</li>
<li><strong><code>endTimeSeconds</code></strong>: The timestamp from the existing video that indicates when the new video ends. <br/><br/></li>
</ul>
<pre tabindex="0"><code class="language-bash">curl --location --request POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;YOUR_ACCOUNT_ID_HERE&gt;/stream/clip&#x27; \&#10;&#45;-header &#x27;Authorization: Bearer &lt;YOUR_TOKEN_HERE&gt;&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data-raw &#x27;{&#10;    &quot;clippedFromVideoUID&quot;: &quot;0ea62994907491cf9ebefb0a34c1e2c6&quot;,&#10;    &quot;startTimeSeconds&quot;: 10,&#10;    &quot;endTimeSeconds&quot;: 15&#10;    }&#x27;&#10;</code></pre>
<p>You can check whether your video is ready to play on the <strong>Stream</strong> page of the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<p>While the clipped video processes, the video status response displays <strong>Queued</strong>. When the clipping process is complete, the video status changes to <strong>Ready</strong> and displays the new name of the clipped video and the new duration.</p>
<p>To receive a notification when your video is done processing and ready to play, you can <a href="/stream/manage-video-library/using-webhooks/">subscribe to webhook notifications</a>.</p>
<h2 id="set-video-name">Set video name</h2>
<p>When you clip a video, you can also specify a new name for the clipped video. In the example below, the <code>name</code> field indicates the new name to use for the clipped video.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;clippedFromVideoUID&quot;: &quot;0ea62994907491cf9ebefb0a34c1e2c6&quot;,&#10;	&quot;startTimeSeconds&quot;: 10,&#10;	&quot;endTimeSeconds&quot;: 15,&#10;	&quot;meta&quot;: {&#10;		&quot;name&quot;: &quot;overriding-filename-clip.mp4&quot;&#10;	}&#10;}&#10;</code></pre>
<p>When the video has been clipped and processed, your newly named video displays in your Cloudflare dashboard in the list videos.</p>
<h2 id="add-a-watermark">Add a watermark</h2>
<p>You can also add a custom watermark to your video. For more information on watermarks and uploading a watermark profile, refer to <a href="/stream/edit-videos/applying-watermarks">Apply watermarks</a>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;clippedFromVideoUID&quot;: &quot;0ea62994907491cf9ebefb0a34c1e2c6&quot;,&#10;	&quot;startTimeSeconds&quot;: 10,&#10;	&quot;endTimeSeconds&quot;: 15,&#10;	&quot;watermark&quot;: {&#10;		&quot;uid&quot;: &quot;4babd675387c3d927f58c41c761978fe&quot;&#10;	},&#10;	&quot;meta&quot;: {&#10;		&quot;name&quot;: &quot;overriding-filename-clip.mp4&quot;&#10;	}&#10;}&#10;</code></pre>
<h2 id="require-signed-urls">Require signed URLs</h2>
<p>When clipping a video, you can make a video private and accessible only to certain users by <a href="/stream/viewing-videos/securing-your-stream/">requiring a signed URL</a>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;clippedFromVideoUID&quot;: &quot;0ea62994907491cf9ebefb0a34c1e2c6&quot;,&#10;	&quot;startTimeSeconds&quot;: 10,&#10;	&quot;endTimeSeconds&quot;: 15,&#10;	&quot;requireSignedURLs&quot;: true,&#10;	&quot;meta&quot;: {&#10;		&quot;name&quot;: &quot;signed-urls-demo.mp4&quot;&#10;	}&#10;}&#10;</code></pre>
<p>After the video clipping is complete, you can open the Cloudflare dashboard and video list to locate your video. When you select the video, the <strong>Settings</strong> tab displays a checkmark next to <strong>Require Signed URLs</strong>.</p>
<h2 id="specify-a-thumbnail-image">Specify a thumbnail image</h2>
<p>You can also specify a thumbnail image for your video using a percentage value. To convert the thumbnail's timestamp from seconds to a percentage, divide the timestamp you want to use by the total duration of the video. For more information about thumbnails, refer to <a href="/stream/viewing-videos/displaying-thumbnails">Display thumbnails</a>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;clippedFromVideoUID&quot;: &quot;0ea62994907491cf9ebefb0a34c1e2c6&quot;,&#10;	&quot;startTimeSeconds&quot;: 10,&#10;	&quot;endTimeSeconds&quot;: 15,&#10;	&quot;thumbnailTimestampPct&quot;: 0.5,&#10;	&quot;meta&quot;: {&#10;		&quot;name&quot;: &quot;thumbnail_percentage.mp4&quot;&#10;	}&#10;}&#10;</code></pre>
