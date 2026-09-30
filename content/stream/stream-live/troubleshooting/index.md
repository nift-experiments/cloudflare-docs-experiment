---
cp9:
  canonical: https://developers.cloudflare.com/stream/stream-live/troubleshooting/
  description: Diagnose and resolve buffering, freezing, latency, and other Cloudflare Stream Live issues.
  full_title: Troubleshooting a live stream · Cloudflare Stream docs
  head_html: <title>Troubleshooting a live stream · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Diagnose and resolve buffering, freezing, latency, and other Cloudflare Stream Live issues."><link rel="canonical" href="https://developers.cloudflare.com/stream/stream-live/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/stream-live/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting a live stream · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Diagnose and resolve buffering, freezing, latency, and other Cloudflare Stream Live issues."><meta property="og:url" content="https://developers.cloudflare.com/stream/stream-live/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/stream-live/troubleshooting/#page","headline":"Troubleshooting a live stream \u00b7 Cloudflare Stream docs","description":"Diagnose and resolve buffering, freezing, latency, and other Cloudflare Stream Live issues.","url":"https://developers.cloudflare.com/stream/stream-live/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/stream-live/troubleshooting/
  schema: 1
---
<p>In addition to following the live stream troubleshooting steps in this guide, make sure that your video settings align with <a href="/stream/stream-live/start-stream-live/#recommendations-requirements-and-limitations">Cloudflare live stream recommendations</a>. If you use OBS, you can also check these <a href="/stream/examples/obs-from-scratch/#6-optional-optimize-settings">OBS-specific recommendations</a>.</p>
<h2 id="buffering-freezing-and-latency">Buffering, freezing, and latency</h2>
<p>If your live stream is buffering, freezing, experiencing latency issues, or having other similar issues, try these troubleshooting steps:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Live inputs</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>For the live input in use, select the <strong>Metrics</strong> tab.</p>
</li>
<li>
<p>Look at your <strong>Keyframe Interval</strong> chart.</p>
<p>It should be a consistent flat line that stays between 2s and 8s. If you see an inconsistent or wavy line, or a line that is consistently below 2s or above 8s, adjust the keyframe interval (also called GOP size) in your software or service used to send the stream to Cloudflare. The exact steps for editing those settings will depend on your platform.
* Start by setting the keyframe interval to 4s. If playback is stable but latency is still too high, lower it to 2s. If you are experiencing buffering or freezing in playback, increase it to 8s.</p>
<pre tabindex="0"><code> * If the keyframe interval is &quot;variable&quot; or &quot;automatic&quot;, change it to a specific number instead, like 4s.&#10;</code></pre>
 <details class="nb-details"><summary>What is a keyframe interval?</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/14399.md")
</div></details>
<ol start="3">
<li>
<p>Look at your <strong>Upload-to-Duration Ratio</strong> chart.</p>
<p>It should be a consistent flat line below 90%. If you see an inconsistent or wavy line, or a line that is consistently above 100%, try the following troubleshooting steps:</p>
<ul>
<li>
<p><a href="https://speed.cloudflare.com/">Check that your Internet upload speed</a> is at least 20 Mbps. If it is below 20 Mbps, use common troubleshooting steps such as restarting your router, using an Ethernet connection instead of Wi-Fi, or contacting your Internet service provider.</p>
</li>
<li>
<p>Check the video bitrate setting in the software or service you use to send the stream to Cloudflare.</p>
<ul>
<li>If it is &quot;variable&quot;, change it to &quot;constant&quot; with a specific number, like 8 Mbps.</li>
<li>If it is above 15 Mbps, lower it to 8 Mbps or 70% of your Internet speed, whichever is lower.</li>
</ul>
</li>
<li>
<p>Follow the steps above (the keyframe interval steps) to <em>increase</em> the keyframe interval in the software or service you use to send the stream to Cloudflare.</p>
</li>
</ul>
 <details class="nb-details"><summary>What is the upload-to-duration ratio?</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/14400.md")
</div></details>
<h2 id="encoder-failing-to-connect-or-keeps-disconnecting">Encoder failing to connect or keeps disconnecting</h2>
<p>If your encoder shows a connection error such as &quot;Failed to connect to server&quot; or repeatedly disconnects shortly after starting, try the following:</p>
<ul>
<li>
<p>Verify that your RTMPS URL, stream key, and encoder software are copied correctly into your broadcasting software.</p>
</li>
<li>
<p>If the connection fails, check whether the live input is <a href="/stream/stream-live/start-stream-live/#enable-or-disable-a-live-input">disabled</a> or its <a href="/stream/stream-live/start-stream-live/#rotate-broadcast-keys">broadcast keys have been rotated</a>.</p>
</li>
<li>
<p>If you use <a href="/stream/stream-live/webhooks/">Live Webhooks</a>, check for a <code>live_input.errored</code> event. The webhook payload includes an <a href="/stream/stream-live/webhooks/#error-codes">error code</a> that can help you troubleshoot the specific cause.</p>
</li>
</ul>
<h2 id="connecting-but-the-player-says-stream-has-not-started-yet">Connecting but the player says &quot;Stream has not started yet&quot;</h2>
<p>If your encoder is connected and the dashboard shows a green <strong>Connected</strong> status with valid metrics, but the player preview says <code>Stream has not started yet</code>, try the following:</p>
<ul>
<li>
<p>Wait thirty seconds. There is a brief delay between when your encoder connects and the stream becomes playable.</p>
</li>
<li>
<p>Restart the stream to clear any bad state from the initial connection.</p>
</li>
<li>
<p>Verify that your encoder is sending <a href="/stream/stream-live/start-stream-live/#recommendations-requirements-and-limitations">AAC audio</a>. If it is not, set your encoder's settings to AAC explicitly.</p>
</li>
<li>
<p>Verify that your encoder is sending keyframes at a fixed interval between two and eight seconds. If the keyframe interval is set to <em>variable</em> or <em>automatic</em>, change it to a specific value such as four seconds. For more details, refer to the keyframe information in <a href="#buffering-freezing-and-latency">Buffering, freezing, and latency</a>.</p>
</li>
</ul>
